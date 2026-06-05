Received May 6, 2021, accepted May 19, 2021, date of publication May 31, 2021, date of current version June 9, 2021.

*Digital Object Identifier 10.1109/ACCESS.2021.3084968*

# Robust Single Image Deblurring Using Gyroscope Sensor

SEOWON JI, JUN-PYO HONG, JEONGMIN LEE, SEUNG-JIN BAEK, AND SUNG-JEA KO, (Fellow, IEEE) School of Electrical Engineering, Korea University, Seoul 02841, South Korea

Corresponding author: Seung-Jin Baek (sjinbaek@korea.ac.kr)

**ABSTRACT** Motion blur in an image is caused by the movement of the camera during exposure time; thus, awareness of the camera motion is a key factor in image deblurring algorithms. Among the various sensors that can be utilized while taking a picture in handheld devices, a gyroscope sensor, which measures the angular velocity, can help in estimating the camera motion. To achieve accurate and efﬁcient single-image deblurring with a gyroscope sensor, we present a novel deep network with a ﬂexible receptive ﬁeld that is appropriate for training features related to the nature of the blur. Two specialized modules are sequentially placed in the proposed network to adaptively convert the shapes of the convolutional kernels. The ﬁrst module directly transforms the kernel shape into the direction of the camera motion indicated by the gyroscope measurements. In the middle of the network, where the feature abstraction is sufﬁciently proceeded, the second module integrates features from the blurry image along with the information from the gyroscope to convert the kernel shape effectively, even when the gyroscope sensor is unreliable. Using a new gyro-image paired dataset, extensive experiments were conducted to show the effects of the reliability of the gyroscope measurements on the deblurring performance and to prove the effectiveness of our strategy.

**INDEX TERMS** Convolutional neural network, gyroscope sensor, homography, single-image deblurring.

**I.** ** ** **INTRODUCTION** Despite the rapid development of handheld cameras, motion blur in an image is still visible when the device moves during the image exposure time. Motion blur not only affects the visual quality of the image but also degrades the performance of various applications such as object detection, image segmentation, and visual odometry. Therefore, further improvements in single-image deblurring, in which a latent sharp image is recovered from a blurry one, are now being actively researched. From a classical perspective, the research on single-image deblurring can be divided into two sub-categories: non-blind deblurring and blind deblurring. The non-blind methods \[1\], \[2\] employ a given blur kernel followed by deconvolution of the blurry image. In contrast, blind deblurring methods use only the blurry image to recover the sharp image. However, in many cases, blind methods \[3\]-\[7\] attempt to perform deblurring by ﬁrst estimating the precise blur kernel from a blurry image and then adopting the estimated kernel in a

The associate editor coordinating the review of this manuscript and

approving it for publication was Tomasz Trzcinski.

non-blind deblurring approach to recover the sharp image. Therefore, the deblurring performance of both methods depends heavily on the quality of the blur kernel. Owing to the rapid development of deep learning, various blind deblurring methods that adopt convolutional neural networks (CNNs) have been proposed. Early CNN-based methods were trained with blurry images synthesized using a uniform blur kernel \[8\]-\[10\]. In \[11\], the network was trained to classify the blur kernel used in traditional deblurring. Later, Nah * et al.* presented a new realistic blurry image dataset that includes the ground truth \[12\]. This was followed by the development of various methods \[13\]-\[19\] in which sophisticated relationships between realistic blurry images and their corresponding sharp images are learnt through CNN. In addition to these works that utilize only the image, approaches for using external information to provide better blur estimates have also been proposed. In these previous studies \[20\]-\[22\], inertial sensors such as accelerometers and gyroscopes have proven to be helpful in improving the blur estimation. In particular, gyroscopes are substantially useful in blur estimation because the angular velocities measured by a gyroscope indicate the rotational motion of the camera,

VOLUME 9, 2021 This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see <https://creativecommons.org/licenses/by/4.0/>

which affects the formation of blur artifacts. Moreover, the gyroscope data can be easily obtained because most mobile devices are equipped with inertial measurement units (IMUs), which gather a collection of sensory information, including gyroscope measurements. Mustaniemi * et al.* were the ﬁrst researchers to apply gyroscope data to CNN-based non-blind deblurring in a network referred to as DeepGyro \[23\]. They designed a wide and deep network for image deblurring and exploited the gyroscope information along with the input blurry image. Based on the data from a gyroscope sensor, a 2-channel blur ﬁeld indicating the camera motion during exposure time is ﬁrst computed. This blur ﬁeld is then concatenated to a blurry image as a guide and used as an input to the network, similar to general CNN-based parameterized image operators \[24\]. However, as pointed out in \[25\], this approach results in limited performance improvement owing to the network components, such as the receptive ﬁelds and weights, being ﬁxed regardless of the variation in the guidance parameters. In real-case scenarios, the gyroscope measurements may become unreliable because of two dominant causes, namely, 1) the inherent noise in the sensor and 2) the miscalibration in which the gyroscope and image sensors are not accurately synchronized, thereby giving rise to erroneous deblurring results. Furthermore, the wide and deep network design results in a large receptive ﬁeld, which leads to an increased number of network parameters and high computational complexity. To improve the sensor robustness and image deblurring network efﬁciency performance, an effective gyroscopeguided network (EggNet) with a ﬂexible receptive ﬁeld is presented in this paper. We adaptively transform the receptive ﬁeld of the network so that the network is trained with image features related to the direction and magnitude of the blur. In the front of the network, the kernel shape of the convolutional layer is converted in the direction indicated by the gyroscope measurements to reﬂect the device motion. Because the gyroscope measurements are occasionally degraded by noise or miscalibration, the feature information extracted from the gyroscope and the blurry image is integrated in the middle of the network to correctly convert the kernel shape by exploiting the appropriate features from both the image and the gyroscope information. Hence, the proposed network performs deblurring robustly, even if unreliable gyroscope information is provided. We established a new massive gyroscope-image paired database to train the proposed network. To validate the effectiveness of our proposed network, two types of experiments were conducted: the controlled case where the noise and miscalibration were perfectly controlled, and the raw case where both problems existed. In addition, in view of industrial considerations, we comprehensively analyzed the deblurring performance in terms of the noise level and the calibration accuracy of the gyroscope measurements. The remainder of this paper is organized as follows. Related works are presented in Section II. In Section III, we describe the proposed EggNet in detail. The experimental

setup and results are presented in Section IV to demonstrate the superiority of the proposed method. In Section V, we present our conclusions.

**II.** ** ** **RELATED WORKS** *A.* * * *HOMOGRAPHY FROM GYROSCOPE MEASUREMENTS* To utilize the rotational angular velocity obtained from the gyroscope sensor for image deblurring, the measurements must ﬁrst be transformed into an appropriate form. Based on the multi-view geometry \[26\] and camera motion model \[27\], we transform the gyroscope measurements into a rotational matrix that indicates the angular motion of the camera. The rotational matrix for a speciﬁc time duration * 1* *t* can be calculated as follows:

$$ R(\theta1t) = Rx(\theta1t $$ x )Ry(\theta1t y )Rz(\theta1t *z* ) *,* (1) Rx(\theta1t $$ x ) = $$ 

 0 cos   −\theta1t *x*  − sin   −\theta1t *x*  0 sin   −\theta1t *x*  cos   −\theta1t *x*    *,* (2) Ry(\theta1t $$ y ) = $$   cos  −\theta1t *y*  0 sin  −\theta1t *y* 

− sin  −\theta1t *y*  0 cos  −\theta1t *y*    *,* (3) Rz(\theta1t $$ z ) = $$ 

 cos \theta1t *z* sin \theta1t *z* −sin \theta1t *z* cos \theta1t *z*   *,* (4)

where \theta1t = n \theta1t x, \theta1t y, \theta1t *z* o represents the changes in rotational angles during * * *1* *t* and  *R* *x* *,* * R* *y* *,* * R* *z* represent the rotational matrices for each axis. The rotational matrix applies only to the angular motion of the camera coordinates. Therefore, the intrinsic camera matrix * * *K* should be considered to convert the motion into an image coordinate system. A homography matrix in * 1* *t* can be derived as

$$ H(\theta1t) = K(R(\theta1t) + D)K −1. $$ (5)

When the scene is far away or the motion is only caused by rotation, the term * D* can be omitted from ( 5 ). Then, the equation can be rewritten as $$ H(\theta1t) = KR(\theta1t)K −1. $$ (6)

Using the homography transformation matrix, the camera motion during * * *1* *t* can be expressed as a 2D vector by calculating the coordinate differences between an initial point ( *x* *t* *i* *,* * y* *t* *i* ) and an end point ( *x* *t* *i* + *1* *t* *,* * y* *t* *i* + *1* *t* ). The end point is computed as *w*   *x* *t* *i* + *1* *t* *y* *t* *i* + *1* *t*  $$ = H(\theta1t) $$   *x* *t* *i* *y* *t* *i*   *,* (7)

where * w* is a scale factor introduced to convert the resulting matrix into homogeneous coordinates.

# VOLUME 9, 2021

**FIGURE 1.** Overall framework of the proposed image deblurring network.

*B.* * * *TRANSFORMATION OF RECEPTIVE FIELD* To enhance the geometric transformation capability of CNN models, we introduce a deformable convolution \[28\] that transforms the receptive ﬁeld. The deformable convolution adds 2D offsets learned from the feature map to the regular grid location of the basic convolution operation, thereby enabling the receptive ﬁeld to be transformed ﬂexibly. For conciseness of explanation, let us assume that the number of channels in the input and output feature maps is equal to one. Then, the output of the deformable convolution at pixel ** p** 0 on the input feature map * X* ∈ R *h* × *w* is deﬁned as $$ Y(p0) = $$

# K X

$$ k=1 $$ *W* ( **p** *k* ) *X* ( **p** 0 + ** p** *k* + * 1* **p** *k* ) *,* (8)

where * Y* is the output feature map, * W* is the learnable weight kernel of size * * *K*, and ** ** **p** *k* ∈ ( − ( √

# K − 1) / 2, − ( √

# K − 1. */* 2) *,...,* (( √

# K − 1) / 2, ( √

*K* − 1) */* 2) indicates the location of the convolution kernel with a dilation of 1. When * * *1* **p** *k* has a fractional value, bilinear interpolation is applied to the input feature map to sample the value at that position. For *X* ∈ R *c* × *h* × *w*, the 2D offsets are applied equally to all the channels. The ﬂexible 2D offsets at ** p** 0 are learned from the input feature map as follows:

$$ 1pk = (1px $$ *k* *,* * 1* p *y* *k* ) *,* (9) *1* p *x* $$ k = $$

# L X

$$ l=1 $$ *W* * * *x* *,* *k* *O* ( **p** *l* ) *X* ( **p** 0 + ** p** *l* ) *,* (10) *1* p *y* $$ k = $$

# L X

$$ l=1 $$ *W* * * *y* *,* *k* *O* ( **p** *l* ) *X* ( **p** 0 + ** p** *l* ) *,* (11)

where * L* is the spatial size of the learnable weight kernel for the offset * * *W* *O* = \{ *W* * * *x* *,* 1 *O* * * *,* * W* * y* *,* 1 *O* * * *,...,* * W* * x* *,* *K* *O* *,* * W* * * *y* *,* *K* *O* \}. In short,

the deformable convolution * f* *D* can be expressed as

# Y = f D ( X; W, W O ). (12)

**III.** ** ** **PROPOSED METHOD** We present EggNet, which robustly transforms the receptive ﬁeld by exploiting information from both the input image and the gyroscope for efﬁcient image deblurring. As shown in Fig. 1, the proposed method employs multi-modal input data, i.e., image and gyroscope data, for the U-Net-based \[29\] architecture, which incorporates two specialized modules, namely, the gyro-aided transformation module (GTM) and the image-gyro-aided transformation module (IGTM). In the pre-processing step, the gyroscope measurements are converted into motion guidance vectors (MGVs) based on the camera motion. These MGVs are then exploited throughout the network. Each step is described in detail in the following subsections.

*A.* * * *IMAGE-GYRO PAIRED DATASET* To train the proposed network, following data are required:

1. The input blurry images and their corresponding target sharp images 2. Gyroscope measurements recorded during the exposure time of the input blurry images

We used the camera module in a smartphone device to obtain the sharp image sequences and the gyroscope measurements, as shown in Fig. 2. The images were captured in Bayer format, and the 2D gyroscope sensor for lens-shift optical image stabilization in the camera module was used to obtain the two rotational velocities ( *θ* *x* *, θ* *y* ). To generate the input and target images, we followed the methodology in \[12\], \[30\]. A blurry image is generated by accumulating the sharp images captured over the collective exposure time, which is the time

# VOLUME 9, 2021

**FIGURE 2.** Image and gyroscope data acquisition process. ( *M* and * N* are the numbers of sampled images and gyroscope measurements during the exposure time, respectively. For conciseness of explanation, we assume that * M* and * N* are odd numbers.)

duration of the image sensor receiving light, as follows: $$ B \simeq1 $$

# M

# M X $$ i=1 $$ *S* *i* *,* (13)

where * * *M* is the number of sampled images, which determines the exposure time of the blurry image, and * * *S* *i* is the *i* *th* sharp image. Since the desired original texture can be assumed that it is located in the center of the blur artifact \[31\], the corresponding target image for the blurry image is set to the central image * * *S* ( *M* + 1) */* 2 of the sampled sharp images. In addition, the gyroscope measurements \{ ***θ*** 1 *,* · · · * * *,* *** θ*** *N* \}, which are recorded simultaneously over identical exposure times, are saved in pairs together with the blurry and target sharp images. The target sharp image and the input blurry image are hence generated, as shown in Figs. 3 (a) and (b).

*B.* * * *MOTION GUIDANCE VECTOR (MGV)* Among the two types of data described above, the sharp and blurry images are used without pre-processing for training the proposed network. In contrast, the angular velocities measured by the gyroscope are converted into MGVs for utilization in the network. The MGVs for a single blurry image are divided into two vectors: the pro-MGV indicating the camera motion from the center to the end of the exposure time, and the pre-MGV indicating the movement from the center to the start of the exposure time. The pro-MGV is computed as

MGV Pro ( *x* *,* * y* ) *x* *,* *y* ∈ *w* *,* *h* =  * x* *t* *E* − *x* *t* *C* *y* *t* *E* − *y* *t* *C*  *,* (14)

where * * *h* and * * *w* represent the height and width of the blurry input image, respectively. ( *x* *t* *E* * * *,* * y* *t* *E* ) and ( *x* *t* *C* * * *,* * y* *t* *C* ) denote the 2D coordinates at the end and the center of the exposure time, respectively. The 2D coordinates ( *x* *t* *E* * * *,* * y* *t* *E* ) can be computed from ( *x* *t* *C* * * *,* * y* *t* *C* ) using the gyroscope measurements recorded

**FIGURE 3.** Paired data for training the proposed network. (a) Target sharp image; (b) input blurry image; (c) magnified patches of (a) and (b). The MGVs are shown in the magnified part of (b).

**FIGURE 4.** Conceptual visualization of the red pixel receptive field in blurry image * B*. (a) Visualized receptive fields on the stack of warped images. * B* Pre and * B* Pro are the warped images obtained using * H* Pre and *H* Pro, respectively, and (b) visualization of the receptive fields projected on * B*. during the corresponding exposure time as *w*   *x* *t* *E* *y* *t* *E*   = * H* Pro   *x* *t* *C* *y* *t* *C*   (15)

where * H* Pro is calculated using ( 1 ) and ( 5 ), *H* Pro = * K*

# N − 1 Y

$$ n=(N+1)/2 $$ R(\thetan+1 −\thetan)K −1. (16)

The pre-MGV can be obtained in the same manner. As shown in Fig. 3 (c), the MGVs indicate the motion during the exposure time. The set of MGVs is utilized in the GTM and the IGTM.

*C.* * * *TRANSFORMATION OF RECEPTIVE FIELD* As proved in \[32\], not all the pixels in the receptive ﬁeld contribute equally to the response of an output unit. Thus, if the receptive ﬁeld can be adaptively transformed to include the pixels that contribute signiﬁcantly to the resultant image, an efﬁcient CNN model can be designed. In our previous work \[33\], we presented an approach that exploits a channel-wise stacking of the warped images in which blur artifacts caused by camera motion are aligned in the input data for the CNN model. As shown in Fig. 4, when the receptive ﬁelds in the stacked images are projected onto the original blurry image, the union of the projected receptive ﬁelds is equivalent to a receptive ﬁeld transformed in the blur direction. Therefore, the network to be trained directly uses the pixels related to the direction and magnitude

# VOLUME 9, 2021

**FIGURE 5.** Detailed structure of the gyro-aided transformation module.

of the blur. This results in a promising performance improvement compared to using a single blurry image as the input data without increasing the number of network parameters. Therefore, it can be argued that such a transformation of the receptive ﬁeld enables an effective network design that uses the gyroscope data for guidance. Several methods that ﬂexibly transform the rigid receptive ﬁelds of regular CNN models \[28\], \[34\]-\[36\] have been proposed. Among these methods, deformable convolution \[28\] can effectively transform the receptive ﬁeld with low computational complexity. Based on \[28\], we present two transformation modules that adaptively convert the shape of the receptive ﬁeld using the blur information obtained from the gyroscope and the blurry image.

1. GTM The ﬁrst module, the GTM, is placed in the front of the network, as shown in Fig. 1. It transforms the receptive ﬁeld in the blur direction using the gyroscope measurements. As shown in Fig. 5, the GTM is composed of a regular convolution followed by an offset convolution. The GTM can be expressed as

\{ *F* out *,* MGO \} = * f* GTM ( *F* in *,* MGVs; * W* *R* *,* * W* OC ) *,* (17)

where * * *f* GTM represents the GTM parameterized by * * *W* *R* and *W* OC, which are respectively the learnable weight kernels for the regular and offset convolution for performing convolution with the converted kernel. * * *F* out and * * *F* in are the output and input feature maps, respectively. Using the regular convolution layer, the motion guidance offset (MGO), which indicates the 2D offsets of the weight kernel in the offset convolution, is ﬁrst learned from the MGVs. Using this MGO, the offset convolution then transforms the * * *W* OC to be ﬁtted in the blur direction, and the transformed kernel is applied to *F* in to compute * * *F* out using ( 8 ). Finally, the resultant * * *F* out is fed into the main network, and the MGO is transferred to the next transformation module, i.e., the IGTM.

**FIGURE 6.** Detailed structure of image and gyro-aided transformation module.

2. IGTM The second module, the IGTM, is used twice in the network, as shown in Fig. 1. To robustly transform the receptive ﬁeld in the blur direction regardless of the reliability of the gyroscope measurements, the IGTM exploits both the gyroscope and the image information. As shown in Fig. 6, the IGTM is composed of a set of regular convolutions (Conv A, Conv B, Conv C, and Conv D ), and one offset convolution. The IGTM can be expressed as

# \{ F out, MGO \} = f IGTM ( F in, MGO P; W Rs, W OC ), (18)

where * * *f* IGTM represents the IGTM parameterized by * * *W* *Rs* and * * *W* OC, which are learnable weight kernels for the set of regular convolutions and the offset convolution, respectively, and MGO P is the MGO computed in the previous GTM (or IGTM). To fuse the information from the gyroscope and the blurry image, i.e., MGO P, and * F* in, respectively, we apply a convolutional layer Conv A with a stride of 2 to MGO P, which results in MGO P ↓. Then, Conv B is applied to * F* in to match the number of channels to that of MGO P ↓, resulting in * * *F* ′. The MGO is computed by applying the serial operation Conv C ReLu-Conv D to the concatenation of the two features MGO P ↓

and * * *F* ′. Finally, similar to the GTM, the offset convolution uses the MGO to transform * W* OC in the direction of blur and applied to * F* in to calculate * F* out. The * F* out again ﬂows into the main network, and the MGO is transferred to the next IGTM until it reaches the last IGTM.

**IV.** ** ** **EXPERIMENTAL RESULTS** *A.* * * *IMPLEMENTATION DETAILS AND DATASET* 1. IMPLEMENTATION DETAILS The detailed structure of the proposed EggNet is presented in Table 1. The input Bayer image is reshaped into four channel (Gr, R, Gb, and B) images and fed into the proposed network. If the input image is normal RGB or gray, the input

# VOLUME 9, 2021 **TABLE 1.** Detailed architecture of EggNet.

image can be directly fed into the network without reshaping. The network reconstructs the latent sharp image ˆ *S* by producing a residual image * R* and adding * R* to the input image * B*. The L1 criterion is applied as the loss for training the network. It can be formulated as *Loss* = ˆ *S* − *S* 1 * * *,* (19)

where * S* is the target sharp image. We used the Adam \[37\] optimizer with a mini-batch size of two for training. After 1 × 10 5 iterations, the learning rate was decreased to 1 */* 2 of the initial learning rate. The entire training required 2 × 10 5 iterations to converge. We used the PyTorch \[38\] library. All the experiments were conducted on a PC with an Intel i3-8100 CPU and an NVIDIA Titan Xp GPU. The proposed EggNet took

approximately 30 hours and 120 hours to train on the controlled case and the raw case, respectively.

2. DATASET Because there is no available image-gyro paired dataset, we made variations in our dataset and conducted extensive experiments. The deblurring performance of EggNet was evaluated for two cases: the controlled case and the raw case. Both cases consisted of 2,119 sets (1,923 sets for training and 196 sets for testing) of gyroscope measurements, blurry images, and sharp images. The resolutions of the images in the controlled case and the raw case were 512 \times 512 and 1024 \times 1024, respectively. To simulate the gyroscope sensor noise and miscalibration in the controlled case, we synthesized the blurry image by integrating the homographies over the exposure time, as explained in \[20\]. Because the gyroscope records discrete measurements, the blurry image can be expressed as $$ B \simeq1 $$

# M

# N X $$ n=1 $$ H(\thetai −θ *N* + 1

# 2 ) S. (20)

In addition, to validate the effectiveness of the proposed method in the presence of noise and miscalibration, two variations of the controlled case dataset were generated: 1) random noise vectors were added to the MGVs to imitate noise, and 2) the MGVs were generated with delayed gyroscope measurements to mimic miscalibration. In the raw case, we used the training and test data, as explained in III-A. The numbers of sampled images * * *M* and that of the gyroscope measurements * * *N* were 7 and 13, respectively. The exposure time for each image was dependent on the lighting conditions. The average exposure time was 20 ms. The deblurring performance was evaluated using the peak signal-to-noise ratio (PSNR) and structural similarity (SSIM) in Bayer format, and the resultant images were displayed as RGB images using the de-mosaic algorithm in \[39\].

*B.* * * *SELF-COMPARISON* To analyze the effectiveness of the proposed method in detail, we conducted self-comparison experiments. For these evaluations, we designed modiﬁed forms of EggNet, as shown in Fig. 7. The ﬁrst network Base Deform substitutes the GTM and the IGTM with deformable convolutions, and it takes a blurry image as input. The second network Base I&G exploits the concatenation of the blurry images and MGVs and adopts deformable convolutions instead of the proposed modules. Therefore, the offsets for the ﬁrst deformable convolution in Base I&G are computed from the integrated features of the image and gyroscope in a similar manner to the IGTM. The third network, Base GTM, includes the GTM, but substitutes the IGTMs with deformable convolutions. The decoder part of these networks are the same as that of EggNet. Furthermore, in order to validate the effectiveness of L1 loss over L2 loss in image deblurring task, we additionally trained

# VOLUME 9, 2021

**FIGURE 7.** Architectures for self-comparison: (a) Base network with only deformable convolutions on the blurry image (Base Deform ); (b) base network with deformable convolution and concatenation of blurry image and MGVs as input (Base I&G ); (c) base network with the proposed GTM, and deformable convolutions instead of IGTM (Base GTM ).

**TABLE 2.** Average PSNR and SSIM on the controlled case and the raw case.

EggNet with L2 loss (EggNet L2 ). These networks were trained and tested on both the controlled and raw cases, and the results are listed in Table 2. In terms of loss function, EggNet trained with L1 loss outperforms EggNet L2 trained with L2 loss in both the cases.

1. EFFECTIVENESS OF FLEXIBLE RECEPTIVE FIELD First, we compared Base Deform with DeepGyro to evaluate the effectiveness of the ﬂexible receptive ﬁeld for image deblurring. As listed in Table 2, the Base Deform outperforms

**FIGURE 8.** Visualized MGVs (red arrows), the MGO used in the GTM (yellow colored dashed line with circle), and the MGO used in the first IGTM (green dashed line with circle) on the sample images. (a) Sample images in which the GTM spreads the kernel in the blur direction indicated by the MGVs; (b) sample images in which the weight kernels of the GTM are spread in the wrong direction because of the degraded MGVs, and the weight kernels of the IGTM, which are correctly converted in the blur direction.

DeepGyro in every case, even though both methods adopt the U-shaped network architecture. Moreover, DeepGyro exploits the additional gyroscope information and has ﬁve times more parameters than Base Deform. These results validate the application of the ﬂexible receptive ﬁeld to achieve efﬁcient network design.

2. EFFECTIVENESS OF GYROSCOPE-BASED FLEXIBLE RECEPTIVE FIELD IN CONTROLLED CASE The GTM aims to transform the receptive ﬁeld in the blur direction using conﬁdent gyroscope measurements. The visualized MGO of the GTM shown in Fig. 8 (a) proves that the GTM performs as intended and transforms the kernel in the blur direction when conﬁdent gyroscope measurements are provided. To demonstrate the effectiveness of the GTM, we compared the deblurring performance in the controlled case. As shown in Table 2, Base GTM outperforms Base Deform

in terms of PSNR by 1.92 (from 35.78 to 37.70). Therefore, it can be concluded that expanding the receptive ﬁeld in the blur direction using the gyroscope measurements is more effective than deformable convolution in improving the deblurring performance. Compared with Base I&G, Base GTM

shows a PSNR improvement of 0.60 (from 37.10 to 37.70).

# VOLUME 9, 2021

**FIGURE 9.** Experimental data and resulting images for various blur images in the controlled cases. From lightly blurred image (top) to heavily blurred image (bottom). The magnified parts of the images are shown at the bottom of each image. (a) Input blurry images; (b) target sharp images; (c) resultant images from DeepGyro; (d) resultant images from PSS-NSC; (e) resultant images from DMPHN; (f) resultant images from EggNet.

Consequently, it can be seen that converting the shape of the weight kernel in the front of the network using the gyroscope measurements is more effective than using both the image and gyroscope measurements if reliable gyroscope measurements are provided. Based on these results, we can assume that the features from the blurry image in the front of the network might not be sufﬁcient for computing the offsets for the blur direction and magnitudes.

3. EFFECTIVENESS OF GYROSCOPE & IMAGE-BASED FLEXIBLE RECEPTIVE FIELD IN RAW CASE When the gyroscope sensor is affected by noise or miscalibration, the gyroscope measurements may become unreliable. To prevent adverse effects from the degraded gyroscope measurements while exploiting the useful information from them, the IGTM aims to transform the receptive ﬁeld in the blur direction using both the gyroscope measurements and the

# VOLUME 9, 2021

**FIGURE 10.** Experimental data and resulting images for various blur images in the raw cases. From lightly blurred image (top) to heavily blurred image (bottom). The magnified parts of the images are shown at the bottom of each image. (a) Input blurry images; (b) target sharp images; (c) resultant images from DeepGyro; (d) resultant images from PSS-NSC; (e) resultant images from DMPHN; (f) resultant images from EggNet.

feature maps from the input image. As shown in Fig. 8 (b), the IGTM spreads the kernel in the blur direction even when the GTM spreads the kernel in the wrong direction because of unreliable gyroscope measurements. We also compared the results of EggNet and Base GTM in the raw case. As shown in Table 2, EggNet improves the deblurring performance in terms of PSNR by 0.23 (from 35.79 to 36.02). Base I&G

also exhibits a performance improvement of 0.04 dB (from 35.79 to 35.83) compared with Base GTM. The visualized kernel and the comparison result demonstrate that converting

the kernel shape using the integrated features from the gyroscope and image robustly transforms the kernel in the blur direction even if the gyroscope is adversely affected by noise or miscalibration.

*C.* * * *DEBLURRING UNDER DIVERSE CONDITIONS:* *PERFORMANCE vs. NOISE & MISCALIBRATION* As mentioned in the previous sections, the gyroscope sensor can be affected and degraded by noise and miscalibration. Continuing from Section IV-B3, we conducted more

# VOLUME 9, 2021

**FIGURE 11.** Average PSNR of EggNet and Base GTM on the variant dataset. (a) Average PSNR measured on the dataset with noise; (b) average PSNR measured on the dataset with miscalibration.

experiments under diverse conditions to validate the effectiveness of EggNet in detail. First, we studied the condition in which the gyroscope measurements are corrupted by noise. Because the gyroscope measurements cannot be directly expressed in the image domain, we added noise to the MGVs which indicate pixel movements in the image domain. Random noise offsets were added to each channel of the MGVs because the values of the MGVs change monotonically. Based on the fact that the values in the MGVs were usually distributed in range of \[ − 10 *,* 10\], we considered Gaussian noise with sigma of 0 (\sigma1), 0.125 (\sigma2), 0.25 (\sigma3), and 1 (\sigma4). The blurry and sharp image pairs used in the controlled case and the noise-added MGVs were used for network training. The bar chart in Fig. 11 (a) presents the average PSNR of EggNet and Base GTM on the diverse noise-added MGVs. To improve the reliability of the results considering the randomness of the noise, the reported PSNR was averaged by performing 10 repeats of the experiments on the test data. Under the noise-free condition, * * *σ* 1, the performance difference between EggNet and Base GTM is imperceptible. With * * *σ* 2 noise, EggNet still showed comparable results, but Base GTM failed to prevent adverse effects from the noise. Under harsher noise conditions, although the PSNR of both methods decreased, the performance of EggNet deteriorated less compared with that of Base GTM. We next considered the presence of miscalibration between the gyroscope sensor and image sensor. Similar to the noise case, the blurry and sharp images from the controlled case and the MGVs computed from the delayed gyroscope measurements were exploited to model the miscalibration. The bar chart in Fig. 11 (b) presents the average PSNR of EggNet and Base GTM when miscalibration were present. In Fig. 11 (b), *1* *T* is one-tenth of the image exposure time. EggNet robustly performed image deblurring compared with Base GTM even in the presence of miscalibration. From these results, we validated the ability of EggNet to effectively exploit the gyroscope measurements and robustly perform image deblurring even if these measurements are degraded. From an industrial perspective, noise and miscalibration should be addressed thoroughly so that the image

**TABLE 3.** Average PSNR, SSIM, and execution time on the controlled case and the raw case.

and gyroscope sensors can be simultaneously exploited for image deblurring. This would increase the hardware or software complexity. We found that using our proposed EggNet, the degradation under * σ* 2 noise and * 1* *T* miscalibration is still acceptable, and therefore the increment of the hardware or software complexity can be mitigated.

*D.* * * *COMPARISON WITH OTHER NETWORKS* We carried out quantitative and qualitative comparisons of EggNet with other deblurring networks. Because there are no other gyro-aided deblurring methods except for DeepGyro \[23\], we compared the proposed EggNet with nongyro-aided deblurring networks. Among the various stateof-the-art non-gyro-aided deblurring networks \[16\]-\[19\], DMPHN \[16\] and PSS-NSC \[17\], which have been publicly released by their authors, were trained on our gyro-image paired dataset. Except for DMPHN, which was trained with a mini-batch size of one owing to memory limitations, a mini-batch size of two was used for training in the raw case, and the learning schedules of each network were followed in accordance to the strategy of the network. As demonstrated in Table 3, the proposed EggNet outperforms the competing networks in terms of PSNR and SSIM. In addition to the superior PSNR and SSIM, EggNet used the smallest number of parameters. Compared with the conventional gyro-aided deblurring network DeepGyro, the proposed EggNet achieved signiﬁcant improvement in both cases while using only one-ﬁfth the number of parameters used in DeepGyro. Although EggNet outperformed both DMPHN and PSS-NSC in terms of accuracy and efﬁciency, both of these methods were not designed for gyro-aided deblurring. In consideration of this, our approach can be integrated with the approaches used in DMPHN and PSS-NSC. In these two networks, a sharp image is obtained in a progressive manner and the parameters are shared through the network to further improve the deblurring performance and reduce the model complexity. Overall, the proposed network showed the best performance in terms of PSNR and SSIM, exploited the fewest number of parameters, and recorded the second-fastest processing time. The resultant images for the controlled case and the raw case from our image-gyro paired dataset are shown in Fig. 9 and Fig. 10, respectively. For clarity, the magniﬁed parts of each image are displayed at the bottom. As can be seen,

# VOLUME 9, 2021

## the proposed EggNet successfully restores the latent sharp

images and produces sharpest detailed textures in all cases.

## V. CONCLUSION

We presented an effective gyroscope-guided network (EggNet) that exploits a ﬂexible receptive ﬁeld to achieve effective image deblurring using an additional gyroscope sensor. Two specialized modules, namely, the GTM and the IGTM, are sequentially placed in EggNet. They adaptively transform the weight kernel in the blur direction to train the network with features related to the nature of the blur. The extensive experiments conducted on variants of our image-gyro dataset clearly demonstrate the effectiveness of our approach. The proposed EggNet robustly performs gyroscope-aided image deblurring compared to conventional methods.

## ACKNOWLEDGMENT

*(Seowon* * * *Ji,* * * *Jun-Pyo* * * *Hong,* * * *and* * * *Jeongmin* * * *Lee* * * *contributed* *equally to this work.)* The authors thank Cheol-Hwan Yoo of Korea University for capturing image-gyro paired dataset.

# REFERENCES

\[1\] S. Cho, J. Wang, and S. Lee, ''Handling outliers in non-blind image deconvolution,'' in * Proc. Int. Conf. Comput. Vis.*, Nov. 2011, pp. 495-502. \[2\] S. Tang, W. Gong, W. Li, and W. Wang, ''Non-blind image deblurring method by local and nonlocal total variation models,'' * * *Signal* * * *Process.*, vol. 94, pp. 339-349, Jan. 2014. \[3\] D. Krishnan, T. Tay, and R. Fergus, ''Blind deconvolution using a normalized sparsity measure,'' in * Proc. CVPR*, Jun. 2011, pp. 233-240. \[4\] L. Sun, S. Cho, J. Wang, and J. Hays, ''Edge-based blur kernel estimation using patch priors,'' in * * *Proc.* * * *IEEE* * * *Int.* * * *Conf.* * * *Comput.* * * *Photogr.* * * *(ICCP)*, Apr. 2013, pp. 1-8. \[5\] L. Xu, S. Zheng, and J. Jia, ''Unnatural L0 sparse representation for natural image deblurring,'' in * * *Proc.* * * *IEEE* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* * * *Recognit.*, Jun. 2013, pp. 1107-1114. \[6\] O. Whyte, J. Sivic, and A. Zisserman, ''Deblurring shaken and partially saturated images,'' * * *Int.* * * *J.* * * *Comput.* * * *Vis.*, vol. 110, no. 2, pp. 185-201, Nov. 2014. \[7\] J. Pan, D. Sun, H. Pﬁster, and M.-H. Yang, ''Blind image deblurring using dark channel prior,'' in * * *Proc.* * * *IEEE* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* * * *Recognit.* *(CVPR)*, Jun. 2016, pp. 1628-1636. \[8\] L. Xu, J. S. Ren, C. Liu, and J. Jia, ''Deep convolutional neural network for image deconvolution,'' in * Proc. Adv. Neural Inf. Process. Syst.*, vol. 27, 2014, pp. 1790-1798. \[9\] C. J. Schuler, M. Hirsch, S. Harmeling, and B. Scholkopf, ''Learning to deblur,'' * * *IEEE* * * *Trans.* * * *Pattern* * * *Anal.* * * *Mach.* * * *Intell.*, vol. 38, no. 7, pp. 1439-1451, Jul. 2016. \[10\] A. Chakrabarti, ''A neural approach to blind motion deblurring,'' in * Proc.* *Eur. Conf. Comput. Vis.* New York, NY, USA: Springer, 2016, pp. 221-235. \[11\] J. Sun, W. Cao, Z. Xu, and J. Ponce, ''Learning a convolutional neural network for non-uniform motion blur removal,'' in * * *Proc.* * * *IEEE* * * *Conf.* *Comput. Vis. Pattern Recognit.*, Jun. 2015, pp. 769-777. \[12\] S. Nah, T. H. Kim, and K. M. Lee, ''Deep multi-scale convolutional neural network for dynamic scene deblurring,'' in * Proc. IEEE Conf. Comput. Vis.* *Pattern Recognit. (CVPR)*, Jul. 2017, pp. 3883-3891. \[13\] X. Tao, H. Gao, X. Shen, J. Wang, and J. Jia, ''Scale-recurrent network for deep image deblurring,'' in * * *Proc.* * * *IEEE* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* *Recognit.*, Jun. 2018, pp. 8174-8182. \[14\] O. Kupyn, V. Budzan, M. Mykhailych, D. Mishkin, and J. Matas, ''DeblurGAN: Blind motion deblurring using conditional adversarial networks,'' in * * *Proc.* * * *IEEE/CVF* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* * * *Recognit.*, Jun. 2018, pp. 8183-8192. \[15\] O. Kupyn, T. Martyniuk, J. Wu, and Z. Wang, ''DeblurGAN-v2: Deblurring (orders-of-magnitude) faster and better,'' in * Proc. IEEE/CVF Int. Conf.* *Comput. Vis. (ICCV)*, Oct. 2019, pp. 8878-8887.

\[16\] H. Zhang, Y. Dai, H. Li, and P. Koniusz, ''Deep stacked hierarchical multipatch network for image deblurring,'' in * Proc. IEEE/CVF Conf. Comput.* *Vis. Pattern Recognit. (CVPR)*, Jun. 2019, pp. 5978-5986. \[17\] H. Gao, X. Tao, X. Shen, and J. Jia, ''Dynamic scene deblurring with parameter selective sharing and nested skip connections,'' in * * *Proc.* *IEEE/CVF* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* * * *Recognit.* * * *(CVPR)*, Jun. 2019, pp. 3848-3856. \[18\] M. Suin, K. Purohit, and A. N. Rajagopalan, ''Spatially-attentive patch-hierarchical network for adaptive motion deblurring,'' in * * *Proc.* *IEEE/CVF* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* * * *Recognit.* * * *(CVPR)*, Jun. 2020, pp. 3606-3615. \[19\] K. Purohit and A. Rajagopalan, ''Region-adaptive dense network for efﬁcient motion deblurring,'' in * * *Proc.* * * *AAAI* * * *Conf.* * * *Artif.* * * *Intell.*, Apr. 2020, pp. 11882-11889. \[20\] N. Joshi, S. B. Kang, C. L. Zitnick, and R. Szeliski, ''Image deblurring using inertial measurement sensors,'' * ACM Trans. Graph.*, vol. 29, no. 4, pp. 1-9, Jul. 2010. \[21\] O. Sindelar and F. Sroubek, ''Image deblurring in smartphone devices using built-in inertial measurement sensors,'' * * *J.* * * *Electron.* * * *Imag.*, vol. 22, no. 1, Feb. 2013, Art. no. 011003. \[22\] O. Sindelar, F. Sroubek, and P. Milanfar, ''Space-variant image deblurring on smartphones using inertial sensors,'' in * Proc. IEEE Conf. Comput. Vis.* *Pattern Recognit. Workshops*, Jun. 2014, pp. 191-192. \[23\] J. Mustaniemi, J. Kannala, S. Sarkka, J. Matas, and J. Heikkila, ''Gyroscope-aided motion deblurring with deep networks,'' in * Proc. IEEE* *Winter Conf. Appl. Comput. Vis. (WACV)*, Jan. 2019, pp. 1914-1922. \[24\] Q. Chen, J. Xu, and V. Koltun, ''Fast image processing with fullyconvolutional networks,'' in * * *Proc.* * * *IEEE* * * *Int.* * * *Conf.* * * *Comput.* * * *Vis.* * * *(ICCV)*, Oct. 2017, pp. 2497-2506. \[25\] Q. Fan, D. Chen, L. Yuan, G. Hua, N. Yu, and B. Chen, ''Decouple learning for parameterized image operators,'' in * Proc. Eur. Conf. Comput.* *Vis. (ECCV)*, Sep. 2018, pp. 442-458. \[26\] A. M. Andrew, ''Multiple view geometry in computer vision,'' * Kybernetes*, vol. 30, pp. 1333-1341, Dec. 2001. \[27\] A. Karpenko, D. Jacobs, J. Baek, and M. Levoy, ''Digital video stabilization and rolling shutter correction using gyroscopes,'' * Continuously Stirred* *Tank Reactor*, vol. 1, no. 2, p. 13, 2011. \[28\] J. Dai, H. Qi, Y. Xiong, Y. Li, G. Zhang, H. Hu, and Y. Wei, ''Deformable convolutional networks,'' in * * *Proc.* * * *IEEE* * * *Int.* * * *Conf.* * * *Comput.* * * *Vis.* * * *(ICCV)*, Oct. 2017, pp. 764-773. \[29\] O. Ronneberger, P. Fischer, and T. Brox, ''U-Net: Convolutional networks for biomedical image segmentation,'' in * * *Proc.* * * *Int.* * * *Conf.* * * *Med.* *Image Comput.-Assisted Intervent.* New York, NY, USA: Springer, 2015, pp. 234-241. \[30\] M. Hirsch, C. J. Schuler, S. Harmeling, and B. Scholkopf, ''Fast removal of non-uniform camera shake,'' in * Proc. Int. Conf. Comput. Vis.*, Nov. 2011, pp. 463-470. \[31\] A. Z. Averbuch, A. Schclar, and D. L. Donoho, ''Deblocking of blocktransform compressed images using weighted sums of symmetrically aligned pixels,'' * IEEE Trans. Image Process.*, vol. 14, no. 2, pp. 200-212, Feb. 2005. \[32\] W. Luo, Y. Li, R. Urtasun, and R. Zemel, ''Understanding the effective receptive ﬁeld in deep convolutional neural networks,'' in * * *Advances* *in* * * *Neural* * * *Information* * * *Processing* * * *Systems*, D. Lee, M. Sugiyama, - Luxburg, I. Guyon, and R. Garnett, Eds., vol. 29. Red Hook, NY, USA: Curran Associates, 2016, pp. 4898-4906. \[33\] J. Lee, S.-W. Ji, S.-J. Cho, J.-P. Hong, and S.-J. Ko, ''Deep learning-based deblur using gyroscope data,'' in * Proc. IEEE Int. Conf. Consum. Electron.* *(ICCE-Asia)*, Nov. 2020, pp. 1-4. \[34\] M. Jaderberg, K. Simonyan, A. Zisserman, and K. Kavukcuoglu, ''Spatial transformer networks,'' in * * *Proc.* * * *Adv.* * * *Neural* * * *Inf.* * * *Process.* * * *Syst.*, vol. 28, 2015, pp. 2017-2025. \[35\] Y. Jeon and J. Kim, ''Active convolution: Learning the shape of convolution for image classiﬁcation,'' in * * *Proc.* * * *IEEE* * * *Conf.* * * *Comput.* * * *Vis.* * * *Pattern* *Recognit. (CVPR)*, Jul. 2017, pp. 4201-4209. \[36\] X. Zhu, H. Hu, S. Lin, and J. Dai, ''Deformable ConvNets v2: More deformable, better results,'' in * Proc. IEEE/CVF Conf. Comput. Vis. Pattern* *Recognit. (CVPR)*, Jun. 2019, pp. 9308-9316. \[37\] D. P. Kingma and J. Ba, ''Adam: A method for stochastic optimization,'' 2014, *arXiv:1412.6980*. \[Online\]. Available: <https://arxiv.org/abs/1412.6980> \[38\] A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, - Desmaison, L. Antiga, and A. Lerer, ''Automatic differentiation in Pytorch,'' in * Proc. NIPS Autodiff Workshop*, Long Beach, CA, USA, 2017. \[39\] G. Bradski, ''The OpenCV library,'' * Dr. Dobb's J. Softw. Tools*, 2000.

# VOLUME 9, 2021

SEOWON JI received the B.S. degree in electrical engineering from Korea University, Seoul, South Korea, in 2015, where he is currently pursuing the Ph.D. degree in electrical engineering. His research interests include image processing, computer vision, and deep-learning.

JUN-PYO HONG received the B.S. degree in electronics engineering from Tinghua University, in 2013. He joined the Computer Vision and Image Processing Laboratory, Department of Electronic Engineering, Korea University, in 2019. His interests include image processing, computer vision, and deep-learning.

JEONGMIN LEE received the B.S. degree in electrical engineering from Korea University, in 2020. He joined the Computer Vision and Image Processing Laboratory, Department of Electrical Engineering, Korea University, in 2020. His interests include image processing, computer vision, and deep-learning.

SEUNG-JIN BAEK received the B.S. and Ph.D. degrees in electrical engineering from Korea University, Seoul, South Korea, in 2007 and 2013, respectively. He joined the Digital Media and Communications Research and Development Center, Samsung Electronics Company Ltd., Suwon, South Korea, in 2013, where he was as a Senior Engineer, from 2014 to 2015. He was a Staff Engineer with the Visual Display Business Division, Samsung Electronics Company Ltd., from 2015 to 2020. He is currently a Research Professor with the Research Institute of Information and Communication Technology, Korea University. His current research interests include deep learning, image processing applications, and computer vision.

SUNG-JEA KO (Fellow, IEEE) received the B.S. degree in electronic engineering from Korea University, in 1980, and the M.S. and Ph.D. degrees in electrical and computer engineering from the State University of New York at Buffalo, in 1986 and 1988, respectively. From 1988 to 1992, he was an Assistant Professor with the Department of Electrical and Computer Engineering, University of MichiganDearborn. In 1992, he joined the Department of Electronic Engineering, Korea University, where he is currently a Professor. He has published over 210 international journals articles. He also holds over 60 registered patents in ﬁelds, such as video signal processing and computer vision. Prof. Ko is currently a member of the National Academy of Engineering of Korea. He was a recipient of the 1999 LG Research Award. He received the Hae-Dong Best Paper Award from the Institute of Electronics and Information Engineers (IEIE), in 1997, the Best Paper Award from the IEEE Asia Paciﬁc Conference on Circuits and Systems, in 1996, the Research Excellence Award from Korea University, in 2004, the Technical Achievement Award from the IEEE Consumer Electronics (CE) Society, in 2012, the 15-Year Service Award from the TPC of ICCE, in 2014, and the Chester Sall Award (First Place Transaction Paper Award) from the IEEE CE Society, in 2017. He was honored with the Science and Technology Achievement Medal from the Korean Government, in 2020. He has served as the General Chairman for ITC-CSCC 2012 and the General Chairman for IEICE 2013. He was the President of the IEIE, in 2013, the Vice President of the IEEE CE Society, from 2013 to 2016, and a Distinguished Lecturer of the IEEE, from 2015 to 2017. He is also an Editorial Board Member of the IEEE T RANSACTIONS ON C ONSUMER E LECTRONICS.

# VOLUME 9, 2021