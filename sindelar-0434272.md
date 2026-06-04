# **A SMARTPHONE APPLICATION FOR REMOVING HANDSHAKE BLUR AND COMPENSATING ROLLING SHUTTER** 

_Ondˇrej Sindel´aˇr[ˇ][⋆] , Filip Sroubek[ˇ][⋆] , Peyman Milanfar[†][∗]_ 

> _⋆_ UTIA, Academy of Sciences of the Czech Republic, Prague, Czech Republic 

> _†_ University of California, Santa Cruz, U.S.A. 

## **ABSTRACT** 

Smartphones are now widely used as photographic devices. Equipped with cheap cameras they are prone to many degradations, most notably handshake in combination with rolling shutter causes severe space-variant blur. Removing blur without any information about the camera motion is a computationally demanding and unstable process. We use built-in gyroscopes to record the motion trajectory of the camera during exposure and then remove blur from the acquired photograph based on the reconstructed trajectory. The proposed deblurring application is implemented on Android smartphones with close-to-real-time performance. 

_**Index Terms**_ **—** space-variant deconvolution; gyroscope; mobile phone; rolling shutter 

## **1. INTRODUCTION** 

One of the most frequent problems in photography is blur induced by camera motion under poor light conditions. As the exposure time increases, involuntary camera motion has a growing effect on the acquired image. Image stabilization (IS) devices that help to reduce the motion blur by moving the camera sensor in the opposite direction are becoming more common. However, such hardware remedy has its limitations as it can compensate only for motion of a very small extent and speed. In addition, mobile phones are currently not equipped with IS. Deblurring the image offline using mathematical algorithms is usually the only choice we have in order to obtain a sharp image. Arbitrary camera motion blur can be modeled by space-variant (SV) convolution and the deblurring process is referred to as SV deconvolution [1]. This is a hard ill-posed problem if the blur shape is completely unknown. 

Camera motion blur is SV for several reasons. First, it is caused by the camera projection itself. Phone cameras are usually equipped with wide-angle lenses (field of view around 60 _[◦]_ ), which distort objects close to image borders. The blur caused by rotation around _x_ and _y_ axes is therefore different 

> _∗_ This work was supported in part by the Academy of Sciences of the Czech Republic under project M100751201 and by the Grant Agency of the Czech Republic under project GA13-29225S. 

in the image center and borders. The SV blur are particularly noticeable when rotation around _z_ axis is significant. Second, the camera-object distance influences the blur caused by camera translation and the knowledge of depth map is thus necessary. However, phone cameras have a focal length of a few millimeters and the scene projected into the camera image plane moves by less than a pixel if the objects are more than 2m away, so the camera translation in such cases can be neglected [2]. In our work we consider purely rotational motion of the camera, which has additional advantages. Unlike accelerometers, gyroscopes are sufficiently accurate for angular speed estimation but drift. We use gyroscope data to estimate rotation and compensate for the drift by calibrating a still camera. 

Another reason for SV blur, unrelated to camera motion but intrinsic to camera hardware design, is rolling shutter [3]. In image sensors on mobile devices, contrary to systems with mechanical shutter, values of illuminated pixels are read successively line by line while the sensor is exposed to light. The readout from the CMOS sensor takes several tens of milliseconds, which results in a picture not taken at a single moment, but with a slight time delay between the first and last row of pixels. The rolling shutter effect is therefore another cause of space variance as the blur depends on the vertical position in the image. An example in Fig. 1 illustrates the rolling shutter effect. We took a snapshot of a LCD screen displaying a grid of white points on black background. Due to camera motion, the points appear as streaks on the captured image. To model accurately the blur at every position, it is necessary to shift the exposure-time window in which the gyroscope data are fetched according to the vertical position. 

Our work demonstrates the use of built-in gyroscopes in smartphones for accurate blur estimation. The proposed solution is simple and practical. It removes blur induced by camera rotation and simultaneously overcomes rolling-shutter effect, which, to our knowledge, has not been considered in the deconvolution problem before. As a testing platform we have chosen a Samsung Galaxy S II smartphone with Android operating system. 

A similar system was proposed by Joshi _et al._ in [4] but they have designed an expensive measuring apparatus consisting of a DSLR camera and an external inertial module, 

ICIP 2014 

2160 

978-1-4799-5751-4/14/$31.00 ©2014 IEEE 

priors and the solution is usually found by some iterative minimization algorithms, such as Alternating Direction Method of Multipliers (ADMM). To perform full image deblurring with SV blur would be computationally very expensive and not feasible on a mobile device. Instead, we split the image into overlapping patches and generate one blur for each patch. We use a division to 6 _×_ 8 squares with 25% overlap in every directions. Each patch is then reconstructed individually using the Wiener filter for the corresponding blur: 

**==> picture [160 x 25] intentionally omitted <==**

where Φ is the inverse signal to noise ratio, and _G_ , _H_ and _U_ are discrete Fourier transforms of the observed image patch, blur and the estimated image patch, respectively. To avoid ringing artifacts around patch borders, edge tapering is applied prior to filtering. Due to patch overlaps, we blend the reconstructed patches by weighting them with Hamming windows, which results in virtually seamless images. 

**Fig. 1** . Rolling shutter effect: A snapshot (exposure time 1 _/_ 14s) of a point grid. The right column shows a series of blur kernels rendered using data from the gyroscope sensor shifted in time. Blurs were created from sensor data starting 0–60 ms after a synchronization timestamp. 

and perform image deblurring offline on a computer. Contrary to low-cost cameras, rolling shutter is not present in DSLR cameras. Sindelar _et al._ [2] tested simple deconvolution running on smartphones, but they have considered only space-invariant blur, which limits applicability of their solution. A different approach to minimize handshake in smartphones was proposed in [5], where they take a burst of shortexposure noisy images, align them using gyroscope data and average them. Gyro-based deconvolution in [6] assumes multiple blurred photos and the authors argue that deconvolution in general outperforms the align-and-average approach. 

## **2. SMARTPHONE APPLICATION** 

The tested device is equipped with all the apparatus needed for our demo system, namely a relatively high-quality camera, inertial sensors, fast CPU (ARM Cortex-A9) and enough RAM to perform computations. A block diagram of the deblurring application is in Fig. 2. 

We first perform offline calibration to obtain camera intrinsic parameters, rolling shutter delay and gyroscope drift. 

During the photo acquisition, samples of angular velocity are recorded using the embedded gyroscopes, which are afterwards trimmed to match the exposure period. Integrating the position track from the recorded gyroscope data allows us to render a correct blur at every pixel of the image. Stateof-the-art non-blind deconvolution methods use sparse image 

The intensity values of the reconstructed image sometimes lie outside the working bit-depth range (0-255), therefore we added optional normalization with clipping of outliers. The normalization is especially useful in the case of larger blurs and scene with high luminance. 

For the Fourier transformation, we use the FFTW library ported to ARM CPUs, supporting two cores and a SIMD instruction set (NEON). FFTW proved to be remarkably fast on the tested smartphone. 

The acquired images with native camera resolution of 3264 _×_ 2448 are by default scaled down to 2048 _×_ 1536 to take advantage of better performance of FFTW when the image size is a factor of small primes. 

The Wiener filtering consists of several FFTs: one for the blur and two (forward and backward for inverse) for each color channel. That yields a total of 7 FFT operations for each patch. The deconvolution of the image enlarged by the overlaps takes about 7s; the whole process starting from the camera shutter is done in a little over 10s. This includes image resizing, blur estimation, compressing and saving the original and deblurred image files. 

We have identified several issues that hamper our solution. Correct synchronization of camera shutter with the gyroscope samples is critical. Even a few millisecond error can produce annoying artifacts. We managed to find a good synchronization mechanism for our test device, which will be unfortunately hard to port to other models, because Android provides no general aid for precise camera handling. Gyroscope drift is substantial and without any compensation results in a biased blur estimator. Correct calibration is still an open question. Internal image post-processing done by the phone presents another serious problem for deconvolution. Since the original raw data from the image sensor are not available, we are forced to work with JPEG (compressed) images, which are processed by gamma correction and most likely also by un- 

ICIP 2014 

2161 

978-1-4799-5751-4/14/$31.00 ©2014 IEEE 

documented image enhancement steps. We have employed the inversion of gamma correction, which indeed improves the results to some degree. 

Three examples of the application output are in Fig. 3. More examples and a demo video showing how the application runs are available on http://zoi.utia.cas.cz/mobile. 

## **3. CONCLUSIONS** 

**Fig. 2** . The block diagram of the smartphone application: During camera exposure, the application records data from the built-in gyroscopes. The data are processed and blurs are estimated. The captured photo is divided into overlapping patches, Wiener deconvolution is performed on every patch and the reconstructed patches are blended to generate the sharp photo. The whole process, entirely done on the smartphone, takes around 10s. 

This work presents an image deblurring method that can effectively remove blur caused by camera motion using information from gyroscopes. The deconvolution method incorporates spatially varying blur, which allows us to handle both complex camera motion and rolling shutter. The proposed method runs on a smartphone device. 

There are several topics for future research. Implementing smarter deblurring algorithms that avoid ringing artifacts is viable. Gyroscope data are not precise and one could use the calculated blurs as an initial estimate and apply modified blind deconvolution methods to improve their accuracy. Camera-gyroscope synchronization errors could be solved by formulating a minimization problem over a single parameter – the synchronization shift. 

## **4. REFERENCES** 

- [1] O. Whyte, J. Sivic, A. Zisserman, and J. Ponce, “Nonuniform deblurring for shaken images,” _International Journal of Computer Vision_ , vol. 98, no. 2, pp. 168–186, 2012. 

- [2] Ondˇrej Sindel´aˇr and Filip[ˇ] Sroubek,[ˇ] “Image deblurring in smartphone devices using built-in inertial measurement sensors,” _Journal of Electronic Imaging_ , vol. 22, no. 1, pp. 011003–011003, 2013. 

- [3] P Forssen and Erik Ringaby, “Rectifying rolling shutter video from hand-held devices,” in _Computer Vision and Pattern Recognition (CVPR), 2010 IEEE Conference on_ . IEEE, 2010, pp. 507–514. 

- [4] Neel Joshi, Sing Bing Kang, C. Lawrence Zitnick, and Richard Szeliski, “Image deblurring using inertial measurement sensors,” _ACM Trans. Graph._ , vol. 29, pp. 30:1–30:9, July 2010. 

- [5] E. Ringaby and P.-E. Forssen, “A virtual tripod for handheld video stacking on smartphones,” in _Computational Photography (ICCP), 2014 IEEE International Conference on_ , 2014, pp. 1–9. 

**Fig. 3** . Examples of captured and reconstructed images using our demo system. Best viewed on a computer screen and zoomed in. 

- [6] S.H. Park and M. Levoy, “Gyro-based multi-image deconvolution for removing handshake blur,” in _Proceedings of IEEE CVPR_ , 2014, pp. 3366–3373. 

ICIP 2014 

2162 

978-1-4799-5751-4/14/$31.00 ©2014 IEEE 

