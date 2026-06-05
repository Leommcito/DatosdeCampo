## DeepOIS: Gyroscope-Guided Deep Optical Image Stabilizer Compensation

Haipeng Li 1 Shuaicheng Liu 2 *,* 1 Jue Wang 1

1 Megvii Technology 2 University of Electronic Science and Technology of China

## Abstract

*Mobile* * * *captured* * * *images* * * *can* * * *be* * * *aligned* * * *using* * * *their* * * *gy-* *roscope sensors.* * * *Optical image stabilizer (OIS) terminates* *this* * * *possibility* * * *by* * * *adjusting* * * *the* * * *images* * * *during* * * *the* * * *captur-* *ing.* * * *In* * * *this* * * *work,* * * *we* * * *propose* * * *a* * * *deep* * * *network* * * *that* * * *com-* *pensates* * * *the* * * *motions* * * *caused* * * *by* * * *the* * * *OIS,* * * *such* * * *that* * * *the* *gyroscopes* * * *can* * * *be* * * *used* * * *for* * * *image* * * *alignment* * * *on* * * *the* * * *OIS* *cameras* 1 *.* * * *To achieve this, first, we record both videos and* *gyroscopes with an OIS camera as training data.* * * *Then, we* *convert* * * *gyroscope* * * *readings* * * *into* * * *motion* * * *fields.* * * *Second,* * * *we* *propose* * * *a* * * *Fundamental* * * *Mixtures* * * *motion* * * *model* * * *for* * * *rolling* *shutter cameras, where an array of rotations within a frame* *are extracted as the ground-truth guidance.* * * *Third, we train* *a convolutional neural network with gyroscope motions as* *input* * * *to* * * *compensate* * * *for* * * *the* * * *OIS* * * *motion.* *Once* * * *finished,* *the compensation network can be applied for other scenes,* *where* * * *the* * * *image* * * *alignment* * * *is* * * *purely* * * *based* * * *on* * * *gyroscopes* *with no need for images contents, delivering strong robust-* *ness.* * * *Experiments* * * *show* * * *that* * * *our* * * *results* * * *are* * * *comparable* *with that of non-OIS cameras, and outperform image-based* *alignment results with a relatively large margin.*

## 1. Introduction

Image alignment is a fundamental research problem that has been studied for decades, which has been applied in various applications \[ 4, 45, 12, 41, 24 \]. Commonly adopted registration methods include homography \[ 10 \], mesh-based deformation \[ 45, 22 \], and optical flow \[ 8, 29 \]. These methods look at the image contents for the registration, which often require rich textures \[ 21, 46 \] and similar illumination variations \[ 37 \] for good results. In contrast, gyroscopes can be used to align images, where image contents are no longer required \[ 17 \]. The gyroscope in a mobile phone provides the camera 3D rotations, which can be converted into homographies given camera intrinsic parameters for the image alignment \[ 17,

1 Code will be available on <https://github.com/lhaippp/DeepOIS>. **(a)** **(b)** **(d)** **(c)**

Figure 1. (a) inputs without the alignment, (b) gyroscope alignment on a non-OIS camera, (c) gyroscope alignment on an OIS camera, and (d) our method on an OIS camera. We replace the red channel of one image with that of the other image, where misaligned pixels are visualized as colored ghosts. The same visualization is applied for the rest of the paper.

14 \]. In this way, the rotational motions can be compensated. We refer to this as gyro image alignment. One drawback is that translations cannot be handled by the gyro. Fortunately, rotational motions are prominent compared with translational motions \[ 34 \], especially when filming scenes or objects that are not close to the camera \[ 23 \]. Compared with image-based methods, gyro-based methods are attractive. First, it is irrelevant to image contents, which largely improves the robustness. Second, gyros are widely available and can be easily accessed on our daily mobiles. Many methods have built their applications based on the gyros \[ 15, 13, 44 \]. On the other hand, the cameras of smartphones keep evolving, where optical image stabilizer (OIS) becomes more and more popular, which promises less blurry images and smoother videos. It compensates for 2D pan and tilt motions of the imaging device through lens mechan-

# arXiv:2101.11183v2 \[cs.CV\] 4 Jul 2023

ics \[ 5, 42 \]. However, OIS terminates the possibility of image registration by gyros. As the homography derived from the gyros is no longer correspond to the captured images, which have been adjusted by OIS with unknown quantities and directions. One may try to read pans and tilts from the camera module. However, this is not easy as it is bounded with the camera sensor, which requires assistance from professionals of the manufacturers \[ 19 \]. In this work, we propose a deep learning method that compensates the OIS motion without knowing its readings, such that the gyro can be used for image alignment on OIS equipped cell-phones. Fig. 1 shows an alignment example. Fig. 1 (a) shows two input images. Fig. 1 (b) is the gyro alignment produced by a non-OIS camera. As seen, the images can be well aligned with no OIS interferences. Fig. 1 (c) is the gyro alignment produced by an OIS camera. Misalignments can be observed due to the OIS motion. Fig. 1 (d) represents our OIS compensated result. Two frames are denoted as * * *I* *a* and * * *I* *b*, the motion from gyro between them as * G* *ab*. The real motion (after OIS adjustment) between two frames is * * *G* *′* *ab*. We want to find a mapping function that transforms * G* *ab* to * G* *′* *ab*: *′* ab = f(Gab). (1)

We propose to train a supervised convolutional neural network for this mapping. To achieve this, we record videos and their gyros as training data. The input motion * G* *ab* can be obtained directly given the gyro readings. However, obtaining the ground-truth labels for * * *G* *′* *ab* is non-trivial. We propose to estimate the real motion from the captured images. If we estimate a homography between them, then the translations are included, which is inappropriate for rotation-only gyros. The ground-truth should merely contain rotations between * * *I* *a* and * * *I* *b*. Therefore, we estimate a fundamental matrix and decompose it for the rotation matrix \[ 14 \]. However, the cell-phone cameras are rolling shutter (RS) cameras, where different rows of pixels have slightly distinct rotations matrices. In this work, we propose a Fundamental Mixtures model that estimates an array of fundamental matrices for the RS camera, such that rotational motions can be extracted as the ground-truth. In this way, we can learn the mapping function. For evaluations, we capture a testing dataset with various scenes, where we manually mark point correspondences for quantitative metrics. According to our experiments, our network can accurately recover the mapping, achieving gyro alignments comparable to non-OIS cameras. In summary, our contributions are:

- We propose a new problem that compensates OIS motions for gyro image alignment on cell-phones. To the best of our knowledge, the problem is not explored yet, but important to many image and video applications.

- We propose a solution that learns the mapping function between gyro motions and real motions, where a Fundamental Mixtures model is proposed under the RS setting for the real motions.

- We propose a dataset for the evaluation. Experiments show that our method works well when compared with non-OIS cameras, and outperforming image-based opponents in challenging cases.

## 2. Related Work **2.1. Image Alignments**

Homography \[ 10 \], mesh-based \[ 45 \], and optical flow \[ 37 \] methods are the most commonly adopted motion models, which align images in a global, middle, and pixel level. They are often estimated by matching image features or optimize photometric loss \[ 21 \]. Apart from classical traditional features, such as SIFT \[ 25 \], SURF \[ 3 \], and ORB \[ 32 \], deep features have been proposed for improving robustness, e.g., LIFT \[ 43 \] and SOSNet \[ 38 \]. Registration can also be realized by deep learning directly, such as deep homography estimation \[ 20, 46 \]. In general, without extra sensors, these methods align images based on the image contents. **2.2. Gyroscopes**

Gyroscope is important in helping estimate camera rotations during mobile capturing. The fusion of gyroscope and visual measurements have been widely applied in various applications, including but not limited to, image alignment and video stabilization \[ 17 \], image deblurring \[ 26 \], simultaneous localization and mapping (SLAM) \[ 15 \], gesturebased user authentication on mobile devices \[ 13 \], and human gait recognition \[ 44 \]. In mobiles, one important issue is the synchronization between the timestamps of gyros and video frames, which requires gyro calibration \[ 16 \]. In this work, we access the gyro data at the Hardware Abstraction Layer (HAL) of the android layout \[ 36 \], to achieve accurate synchronizations. **2.3. Optical Image Stabilizer**

Optical Image Stabilizer (OIS) has been around commercially since the mid-90s \[ 33 \] and becomes more and more popular in our daily cell-phones. Both the image capturing and video recording can benefit from OIS, producing results with less blur and improved stability \[ 19 \]. It works by controlling the path of the image through the lens and onto the image sensor, which is achieved by measuring the camera shakes using sensors such as gyroscope, and move the lens horizontally or vertically to counteract shakes by electromagnet motors \[ 5, 42 \]. Once a mobile is equipped with OIS, it cannot be turn-off easily \[ 27 \]. On one hand, OIS is

good for daily users. On the other hand, it is not friendly to mobile developers who need gyros to align images. In this work, we enable the gyro image alignment on OIS cameras.

## 3. Algorithm

Our method is built upon convolutional neural networks. It takes one gyro-based flow * G* *ab* from the source frame * I* *a* to the target frame * I* *b* as input, and produces OIS compensated flow * * *G* *′* *ab* as output. Our pipeline consists of three modules: a gyro-based flow estimator, a Fundamental Mixtures flow estimator, and a fully convolutional network that compensates the OIS motion. Fig. 2 illustrates the pipeline. First, the gyro-based flows are generated according to the gyro readings (Fig. 2 (a) and Sec. 3.1 ), then they are fed into a network to produce OIS compensated flows * G* *′* *ab* as output (Fig. 2 (b) and Sec. 3.3 ). To obtain the ground-truth rotations, we propose a Fundamental Mixtures model, so as to produce the Fundamental Mixtures flows * F* *ab* (Fig. 2 (d) and Sec. 3.2 ) as the guidance to the network (Fig. 2 (c)). During the inference, the Fundamental Mixtures model is not required. The gyro readings are converted into gyro-based flows and fed to the network for compensation. **3.1. Gyro-Based Flow**

We compute rotations by compounding gyro readings consisting of angular velocities and timestamps. In particular, we read them from the HAL of android architecture for synchronization. The rotation vector * * *n* = ( *ω* *x* *, ω* *y* *, ω* *z* ) * * *∈* R 3 is computed from gyro readings between frames * I* *a* and *I* *b* \[ 17 \]. The rotation matrix * R* ( *t* ) * ∈* *SO* (3) can be produced according to the Rodrigues Formula \[ 6 \]. If the camera is global shutter, the homography is modeled as: $$ H(t) = KR(t)K−1, $$ (2)

where * K* is the intrinsic camera matrix and * R* ( *t* ) denotes the camera rotation from * I* *a* to * I* *b*. In an RS camera, every row of the image is exposed at a slightly different time. Therefore, Eq.( 2 ) is not applicable since every row of the image has slightly different rotation matrices. In practice, assigning each row of pixels with a rotation matrix is unnecessary. We group several consecutive rows into a row patch and assign each patch with a rotation matrix. Fig. 3 shows an example. Let * t* *s* denotes the camera readout time that is the time duration between the exposure of the first row and the last row of pixels. ta(i) = tI + ts i

# N, (3)

where * * *t* *a* ( *i* ) denotes the start of the exposure of the * * *i* - *th* patch in * I* *a* as shown in Fig. 3, * t* *I* denotes the starting timestamp of the corresponding frame, * N* denotes the number of patches per frame. The end of the exposure is: $$ tb(i) = ta(i) + tf, $$ (4)

where * * *t* *f* = 1 */FPS* is the frame period. Here, the homography between the * * *i* -th row at frame * * *I* *a* and * * *I* *b* can be modeled as: H = KR (tb) R⊤(ta) K−1, (5)

where ** R** ( *t* *b* ) ** R** *⊤* ( *t* *a* ) can be computed by accumulating rotation matrices from * t* *a* to * t* *b*. In our implementation, we divide the image into 6 patches which computes a homography array containing 6 horizontal homographies between two consecutive frames. We convert the homography array into a flow field \[ 26 \] so that it can be fed as input to a convolutional neural network. For every pixel * p* in the * I* *a*, we have: p′ = H(t)p, (u, v) = p′ −p, (6)

computing the offset for every pixel produces a gyro-based flow * G* *ab*. **3.2. Fundamental Mixtures**

Before introducing our model of Fundamental Mixtures, we briefly review the process of estimating the fundamental matrix. If the camera is global-shutter, every row of the frame is imaged simultaneously at a time. Let * * *p* 1 and * * *p* 2 be the projections of the 3D point * * *X* in the first and second frame, * * *p* 1 = * * *P* 1 *X* and * * *p* 2 = * * *P* 2 *X*, where * * *P* 1 and * * *P* 2 represent the projection matrices. The fundamental matrix satisfies the equation \[ 14 \]: *T* $$ 1 Fp2 = 0, $$ (7)

where p1 = (x1, y1, 1)T and p2 = (x′ 1 *, y* *′* 1 *,* 1) *T*. Let ** f** be the 9-element vector made up of * F*, then Eq.( 7 ) can be written as:   *′* 1 *x* 1 *, x* *′* 1 *y* 1 *, x* *′* 1 *, y* *′* 1 *x* 1 *, y* *′* 1 *y* 1 *, y* *′* 1 *, x* 1 *, y* 1 *,* 1  $$ f = 0, $$ (8)

given * n* correspondences, yields a set of linear equations: Af =  

*′* 1 *p* *T* *′* 1 *p* *T* *T*......... *′* *n* *p* *T* *n* *′* *n* *p* *T* *n* *T* *n*  f = 0. (9)

Using at least 8 matching points yields a homogenous linear system, which can be solved under the constraint * * *∥* **f** *∥* 2 = 1 using the Singular Value Decomposition(SVD) of * * *A* = *UDV* * * *⊤* where the last column of * V* is the solution \[ 14 \]. In the case of RS camera, projection matrices * P* 1 and * P* 2 vary across rows instead of being frame-global. Eq.( 7 ) does not hold. Therefore, we introduce Fundamental Mixtures assigning each row patch with a fundamental matrix. We detect FAST features \[ 40 \] and track them by KLT \[ 35 \] between frames. We modify the detection threshold for uniform feature distributions \[ 11, 12 \].

(d) Fundamental-Flow estimator (c)  Flow loss (b) Network structure Source Fundamental Mixtures Output **L1 ** **loss** Target (a) Gyro-Flow estimator Homography Array

Figure 2. The overview of our algorithm which includes (a) gyro-based flow estimator, (d) the fundamental-based flow estimator, and (b) neural network predicting an output flow. For each pair of frames * I* *a* and * I* *b*, the homography array is computed using the gyroscope readings from * t* *I* *a* to * t* *I* *b*, which is converted into the source motion * G* *ab* as the network input. On the other side, we estimate a Fundamental Mixtures model to produce the target flow * F* *ab* as the guidance. The network is then trained to produce the output * G* *′* *ab*.............

Figure 3. Illustration of rolling shutter frames. * * *t* *I* *a* and * t* *I* *b* are the frame starting time. * * *t* *s* is the camera readout time and * t* *f* denotes the frame period ( *t* *f* * * *\>* * * *t* *s* ). * * *t* *a* ( *i* ) and * t* *b* ( *i* ) represent the starting time of patch * i* in * I* *a* and * I* *b*.

To model RS effects, we divide a frame into * N* patches, resulting in * N* unknown fundamental matrices * F* *i* to be estimated per frame. If we estimate each fundamental matrix independently, the discontinuity is unavoidable. We propose to smooth neighboring matrices during the estimation as shown in Fig. 2 (d), where a point * * *p* 1 not only contributes to its own patch but also influences its nearby patches weighted by the distance. The fundamental matrix for point * p* is the mixture: $$ F(p1) = $$

# N X $$ i=1 $$ *F* *i* *w* *i* ( *p* 1 ) *,* (10)

where * * *w* *i* ( *p* 1 ) is the gaussian weight with the mean equals to the middle of each patch, and the sigma * σ* = 0 *.* 001 * ∗* *h*, where * h* represents the frame height. To fit a Fundamental Mixtures * F* *i* given a pair of matching points ( *p* 1 *, p* 2 ), we rewrite Eq.( 7 ) as: $$ 0 = pT $$ $$ 1 Fp1p2 = $$

# N X

$$ i=1 $$ *w* *i* ( *p* 1 ) * ·* ** p** *T* 1 ** ** **F** **i** **p** 2 *,* (11)

where ** p** *T* 1 ** ** **F** **k** **p** 2 can be transformed into:

*i* $$ p1fi = $$   *′* 1 *p* *T* *′* 1 *p* *T* *T*  *f* *i* *,* (12)

where * * *f* *i* denotes the vector formed by concatenating the columns of * * *F* *i*. Combining Eq.( 11 ) and Eq.( 12 ) yields a 1 * ×* 9 *i* linear constraint:

 *w* 1 ( *p* 1 ) *A* 1 *p* 1 * * *... w* *i* ( *p* 1 ) *A* *i* *p* 1  \| \{z \} *A* *p* 1   ... *i*    \| \{z \} *f* $$ = Ap1f = 0. $$ (13)

Aggregating all linear constraints * A* *p* *j* for every match point ( *p* *j* *, p* *j* +1 ) yields a homogenous linear system * A* **f** = 0 that can be solved under the constraint * ∥* **f** *∥* 2 = 1 via SVD. For robustness, if the number of feature points in one patch is inferior to 8, Eq.( 13 ) is under constrained. Therefore, we add a regularizer to constrain * λ*

*A* *i* *p* * * *−* *A* *i* *−* 1 *p* $$ 2 = 0 $$ to the homogenous system with * λ* = 1. **3.2.1** **Rotation-Only Homography**

Given the fundamental matrix * * *F* *i* and the camera intrinsic *K*, we can compute the essential matrix * E* *i* of the * i* -th patch: **E** **i** = ** K** *T* ** ** **F** **i** **K** *.* The essential matrix * E* *i* \[ 14 \] can be decomposed into camera rotations and translations, where only rotations * R* *i* are retained. We use * R* *i* to form a rotation-only homography similar to Eq.( 2 ) and convert the homography array into a flow field as Eq.( 6 ). We call this flow field as Fundamental Mixtures Flow * F* *ab*. Note that, * R* *i* is spatially smooth, as * F* *i* is smooth, so does * F* *ab*. **3.3. Network Structure**

The architecture of the network is shown in Fig. 2 that utilizes a backbone of UNet \[ 30 \] consists of a series of convolutional and downsampling layers with skip connections. The input to the network is gyro-based flow * * *G* *′* *ab* and the ground-truth target is Fundamental Mixtures flow * F* *ab*. Our network aims to produce an optical flow of size * H* * ×* * W* * ×* 2 which compensates the motion generated by OIS between *G* *′* *ab* and * * *F* *ab*. Besides, the network is fully convolutional which accepts input of arbitrary sizes. 5( 0) // /7

Figure 4. A glance at our evaluation dataset. Our dataset contains 4 categories, regular(RE), low-texture(LT), low-light(LL) and moving-foreground(MF). Each category contains 350 pairs, a total of 1400 pairs, with synchronized gyroscope readings.

Our network is trained on 9 *k* rich-texture frames with resolution of 360 x 270 pixels over 1 *k* iterations by an Adam $$ optimizer [18] whose lr = 1.0 \times 10−4, \beta1 = 0.9, \beta2 = $$ 0 *.* 999. The batch size is 8, and for every 50 epochs, the learning rate is reduced by 20%. The entire training process costs about 50 hours. The implementation is in PyTorch and the network is trained on one NVIDIA RTX 2080 Ti.

## 4. Experimental Results **4.1. Dataset**

Previously, there are some dedicated datasets which are designed to evaluate the homography estimation \[ 46 \] or the image deblurring with the artificial-generated gyroscopeframe pair \[ 26 \], whether none of them combine real gyroscope readings with corresponding video frames. So we propose a new dataset and benchmark GF4. **Training Set** To train our network, we record a set of videos with the gyroscope readings using a hand-held cellphone. We choose scenes with rich textures so that sufficient feature points can be detected to calculate the Fundamental Mixtures model. The videos last 300 seconds, yielding 9, 000 frames in total. Note that, the scene type is not important as long as it can provide enough features as needed for Fundamental Mixtures estimation. **Evaluation Set** For the evaluation, we capture scenes with different types, to compare with image-based registration methods. Our dataset contains 4 categories, including regular (RE), low-texture (LT), low-light (LL), and movingforegrounds (MF) frame-gyroscope pairs. Each scene contains 350 pairs. So, there are 1400 pairs in the dataset. We show some examples in Fig. 4. For quantitative evaluation, we manually mark 6 * * *∼* 8 point correspondences per pair, distributing uniformly on frames. Fig. 5 shows some examples.

Figure 5. We mark the correspondences manually in our evaluation set for quantitative metrics. For each pair, we mark 6 * * *∼* 8 point matches. Non-OIS Camera OIS Camera Ours

Geometry Distance 0.688 1.038 0.709 Table 1. Comparisons with non-OIS camera. **4.2. Comparisons with non-OIS camera**

Our purpose is to enable gyro image alignment on OIS cameras. Therefore, we compare our method with non-OIS cameras. In general, our method should perform equally well as non-OIS cameras, if the OIS motion could be compensated successfully. For comparison, ideally, we should use one camera with OIS turn on and off. However, the OIS cannot be turned off easily. Therefore, we use two cellphones with similar camera intrinsics, one with OIS and one without, and capture the same scene twice with similar motions. Fig. 6 shows some examples. Fig. 6 (a) shows the input frames. Fig. 6 (b) shows the gyro alignment on a nonOIS camera. As seen, images can be well aligned. Fig. 6 (c) shows the gyro alignment on an OIS camera. Due to the OIS interferences, images cannot be aligned directly using the gyro. Fig. 6 (d) shows our results. With OIS compensation, images can be well aligned on OIS cameras. We also calculate quantitative values. Similarly, we mark the ground-truth for evaluation. The average geometry distance between the warped points and the manually labeled GT points are computed as the error metric (the lower the better). Table 1 shows the results. Our result 0 *.* 709 is comparable with non-OIS camera 0 *.* 688 (slightly worse), while no compensation yields 1 *.* 038, which is much higher. **4.3. Comparisons with Image-based Methods**

Although it is a bit unfair to compare with image-based methods as we adopt additional hardware. We desire to show the importance and robustness of the gyro-based alignment, to highlight the importance of enabling this ca-

# D ,QSXW E 1RQ2,6&DPHUD F 2,6&DPHUD G 2XUV

Figure 6. Comparisons with non-OIS cameras. (a) input two frames. (b) gyro alignment results on the non-OIS camera. (c) gyro alignment results on the OIS camera. (d) our OIS compensation results. Without OIS compensation, clear misalignment can be observed in (c) whereas our method can solve this problem and be comparable with non-OIS results in (b). pability on OIS cameras. **4.3.1** **Qualitative Comparisons**

Firstly, we compare our method with one frequently used traditional feature-based algorithm, i.e. SIFT \[ 25 \] and RANSAC \[ 9 \] that compute a global homography, and another feature-based algorithm, i.e. Meshflow \[ 22 \] that deforms a mesh for the non-linear motion representation. Moreover, we compare our method with the recent deep homography method \[ 46 \]. Fig. 7 (a) shows a regular example where all the methods work well. Fig. 7 (b), SIFT+RANSAC fails to find a good solution, so does deep homography, while Meshflow works well. One possible reason is that a single homography cannot cover the large depth variations. Fig. 7 (c) illustrates a moving-foreground example that SIFT+RANSAC and Meshflow cannot work well, as few features are detected on the background, whereas Deep Homography and our method can align the background successfully. A similar example is shown in Fig. 7 (d), SIFT+RANSAC and Deep Homography fail. Meshflow works on this example as sufficient features are detected in the background. In contrast, our method can still align the background without any difficulty. Because we do not need the image contents for the registration. Fig. 7 (e) is an example of low-light scenes,

and Fig. 7 (f) is a low-texture scene. All the image-based methods fail as no high-quality features can be extracted, whereas our method is robust. **4.3.2** **Quantitative Comparisons**

We also compare our method with other feature-based methods quantitatively, i.e., the geometry distance. For the feature descriptors, we choose SIFT \[ 25 \], ORB \[ 31 \], SOSNet \[ 38 \], SURF \[ 3 \]. For the outlier rejection algorithms, we choose RANSAC \[ 9 \] and MAGSAC \[ 2 \]. The errors for each category are shown in Table 2 followed by the overall averaged error, where * I* 3 *×* 3 refers to a 3 * ×* 3 identity matrix as a reference. In particular, feature-based methods sometimes crash, when the error is larger than * I* 3 *×* 3 error, we set the error equal to * I* 3 *×* 3 error. Regarding the motion model, from 3 ) to 10 ) and 12 ) are single homography, 11 ) is meshbased, and 13 ) is a homography array. In Table 2, we mark the best performance in red and the second-best in blue. As shown, except for comparing to feature-based methods in RE scenes, our method outperforms the others for all categories. It is reasonable because, in regular(RE) scenes, a set of high-quality features is detected which allows to output a good solution. In contrast, gyroscopes can only compensate for rotational motions, which decreases scores to some extent. For the rest scenes, our method beats

# 2XUV

#,QSXW $$ 6,)75$16$& $$ 0HVK)ORZ 'HHS+RPRJUDSK\\

# D

# E

# F

# G

# H

# I

Figure 7. Comparisons with image-based methods. We compare with SIFT \[ 25 \] + RANSAC \[ 9 \], Meshflow \[ 22 \], and the recent deep homography \[ 46 \] method. We show examples covering all scenes in our evaluation dataset. Our method can align images robustly while image-based methods contain some misaligned regions.

the others with an average error being lower than the 2 nd best by 56 *.* 07%. Especially for low-light(LL) scenes, our method computes an error which is at least lower than the 2 nd best by 43 *.* 9%. **4.4. Ablation Studies** **4.4.1** **Fully Connected Neural Network**

Our network is fully convolutional, where we convert gyroscope data into homography arrays, and then into flow fields as image input to the network. However, there is another option where we can directly input homography ar-

rays as input. Similarly, on the other side, the Fundamental Mixtures are converted into rotation-only homography arrays and then used as guidance. Fig. 8 shows the pipeline, where we test two homography representations, including 3 *×* 3 homography matrix elements and * H* 4 *pt* representation from \[ 7 \] that represents homography by 4 motion vectors. The network is fully connected and L2 loss is adopted for the regression. We adopt the same training data as described above. The result is that neither representations converge, where the * * *H* 4 *pt* is slightly better than directly regressing matrix elements.

# 1) RE LT LL MF Avg

2. I3\times3 7.098(+2785.37%) 7.055(+350.80%) 7.035(+519.55%) 7.032(+767.08%) 7.055(+313.97%)

# 3) SIFT \[ 25 \]+ RANSAC \[ 9 \]

0.340(+38.21%) 6.242(+298.85%) 2.312(+103.58%) 1.229(+51.54%) 2.531(+48.49%) 4. SIFT \[ 25 \] + MAGSAC \[ 2 \] 0.213(−13.41%) 5.707(+264.66%) 2.818(+148.17%) 0.811(+0.00%) 2.387(+40.08%) 5. ORB \[ 31 \] + RANSAC \[ 9 \] 0.653(+165.45%) 6.874(+339.23%) 1.136(+0.00%) 2.27(+179.28%) 2.732(+60.30%) 6. ORB \[ 31 \] + MAGSAC \[ 2 \] 0.919(+273.58%) 6.859(+338.27%) 1.335(+17.60%) 2.464(+203.82%) 2.894(+69.83%) 7. SOSNET \[ 39 \] + RANSAC \[ 9 \] 0.246(+0.00%) 5.946(+279.94%) 1.977(+74.11%) 0.907(+11.84%) 2.269(+33.14%) 8. SOSNET \[ 39 \] + MAGSAC \[ 2 \] 0.309(+25.61%) 5.585(+256.87%) 1.972(+73.67%) 1.142(+40.81%) 2.252(+32.14%) 9. SURF \[ 3 \] + RANSAC \[ 9 \] 0.343(+39.43%) 3.161(+101.98%) 2.213(+94.89%) 1.420(+75.09%) 1.784(+4.69%) 10. SURF \[ 3 \] + MAGSAC \[ 2 \] 0.307(+24.80%) 3.634(+132.20%) 2.246(+97.78%) 1.267(+56.23%) 1.863(+9.34%)

11. MeshFlow \[ 22 \] 0.843(+242.68%) 7.042(+349.97%) 1.729(+52.27%) 1.109(+36.74%) 2.681(+57.30%)

12. Deep Homography \[ 46 \] 1.342(+445.53%) 1.565(+0.00%) 2.253(+98.41%) 1.657(+104.32%) 1.704(+0.00%)

13. Ours 0.609(+147.56%) 1.01(−35.27%) 0.637(−43.90%) 0.736(−9.25%) 0.749(−56.07%) Table 2. Quantitative comparisons on the evaluation dataset. The best performance is marked in red and the second-best is in blue.   

# /ORVV

# PLQLPL\]H 

Figure 8. Regression of the homography array using the fully connected network. For each pair of frames * I* *a* and * I* *b*, a homography array is computed by using gyro readings, which is fed to the network. On the other side, a Fundamental Mixtures model is produced as targets to guide the training process.

Perhaps, there exist other representations or network structures that may work well or even better than our current proposal. Here, as the first try, we have proposed a working pipeline and want to leave the improvements as future works.

**4.4.2** **Global Fundamental vs.** ** ** **Mixtures**

To verify the effectiveness of our Fundamental Mixtures model, we compare it with a global fundamental matrix. Here, we choose the evaluation dataset of the regular scenes to alleviate the feature problem. We estimate global fundamental matrix and Fundamental Mixtures, then convert to the rotation-only homographies, respectively. Finally, we align the images with rotation-only homographies accordingly. An array of homographies from Fundamental Mixtures produces an error of ** 0.451**, which is better than an error of ** 0.580** produced by a single homography from a global fundamental matrix. It indicates that the Fundamental Mixtures model is functional in the case of RS cameras. Moreover, we generate GT with the two methods and train our network, respectively. As shown in Table 3, the network trained on Fundamental Mixtures-based GT outperforms the global fundamental matrix, which demonstrates the effectiveness of our Fundamental Mixtures. Ground Truth RE LT LL MF Avg

Global Fundamental 0.930 1.189 0.769 0.917 0.951 Fundamental Mixtures 0.609 1.010 0.637 0.736 0.749 Table 3. The performance of networks trained on two different GT. **4.4.3** **Backbone**

# RE LT LL MF Avg

R2UNet\[ 1 \] 0.713 1.006 0.652 0.791 0.791 AttUNet\[ 28 \] 0.896 1.058 0.752 0.993 0.925 R2AttUNet\[ 1 \] 0.651 1.014 0.668 0.722 0.764

Ours 0.609 1.01 0.637 0.736 0.749 Table 4. The performance of networks with different backbones.

We choose the UNet \[ 30 \] as our network backbone, we also test several other variants \[ 1, 28 \]. Except for AttUNet \[ 28 \], performances are similar, as shown in Table 4.

## 5. Conclusion

We have presented a DeepOIS pipeline for the compensation of OIS motions for gyroscope image registration. We have captured the training data as video frames as well as their gyro readings by an OIS camera and then calculated the ground-truth motions with our proposed Fundamental Mixtures model under the setting of rolling shutter cameras. For the evaluation, we have manually marked point correspondences on our captured dataset for quantitative metrics. The results show that our compensation network works well when compared with non-OIS cameras and outperforms other image-based methods. In summary, a new problem is proposed and we show that it is solvable by learning the OIS motions, such that gyroscope can be used for image registration on OIS cameras. We hope our work can inspire more researches in this direction.

## References

\[1\] Md Zahangir Alom, Mahmudul Hasan, Chris Yakopcic, Tarek M Taha, and Vijayan K Asari. Recurrent residual convolutional neural network based on u-net (r2u-net) for medical image segmentation. * arXiv* *preprint arXiv:1802.06955*, 2018. 8

\[2\] Daniel Barath, Jiri Matas, and Jana Noskova. Magsac: marginalizing sample consensus. In * * *Proc.* * * *CVPR*, pages 10197-10205, 2019. 6, 8

\[3\] Herbert Bay, Tinne Tuytelaars, and Luc Van Gool. SURF: speeded up robust features. In * * *Proc.* * * *ECCV*, volume 3951, pages 404-417, 2006. 2, 6, 8

\[4\] Matthew Brown and David G. Lowe. Recognising panoramas. In * * *Proc.* * * *ICCV*, pages 1218-1227, 2003.

\[5\] Chi-Wei Chiu, Paul C-P Chao, and Din-Yuan Wu. Optimal design of magnetically actuated optical image stabilizer mechanism for cameras in mobile phones via genetic algorithm. *IEEE* * * *Trans.* * * *on* * * *Magnetics*, 43(6):2582-2584, 2007. 2

\[6\] Jian S Dai. Euler-rodrigues formula variations, quaternion conjugation and intrinsic connections. *Mechanism* * * *and* * * *Machine* * * *Theory*, 92:144-152, 2015.

\[7\] Daniel DeTone, Tomasz Malisiewicz, and Andrew Rabinovich. Deep image homography estimation. * * *arXiv* *preprint arXiv:1606.03798*, 2016. 7

\[8\] Alexey Dosovitskiy, Philipp Fischer, Eddy Ilg, Philip H¨ausser, Caner Hazirbas, Vladimir Golkov, Patrick van der Smagt, Daniel Cremers, and Thomas Brox. Flownet: Learning optical flow with convolutional networks. In * Proc. ICCV*, 2015. 1

\[9\] Martin A. Fischler and Robert C. Bolles. Random sample consensus: A paradigm for model fitting with applications to image analysis and automated cartography. * * *Commun.* * * *ACM*, 24(6):381-395, 1981. 6, 7,

\[10\] Junhong Gao, Seon Joo Kim, and Michael S Brown. Constructing image panoramas using dualhomography warping. In * * *Proc.* * * *CVPR*, pages 49-56, 2011. 1, 2

\[11\] Matthias Grundmann, Vivek Kwatra, Daniel Castro, and Irfan Essa. Calibration-free rolling shutter removal. In * * *IEEE* * * *international* * * *conference* * * *on* * * *compu-* *tational photography (ICCP)*, pages 1-8, 2012. 3

\[12\] Heng Guo, Shuaicheng Liu, Tong He, Shuyuan Zhu, Bing Zeng, and Moncef Gabbouj. Joint video stitching and stabilization from moving cameras. * * *IEEE Trans.* *on Image Processing*, 25(11):5491-5503, 2016. 1, 3

\[13\] Dennis Guse and Benjamin M¨uller. Gesturebased user authentication for mobile devicesusing accelerometer and gyroscope. In * * *Informatiktage*, pages 243-246, 2012. 1, 2

\[14\] Richard Hartley and Andrew Zisserman. *Multiple* *view* * * *geometry* * * *in* * * *computer* * * *vision*. Cambridge university press, 2003. 1, 2, 3, 4

\[15\] Weibo Huang and Hong Liu. Online initialization and automatic camera-imu extrinsic calibration for monocular visual-inertial slam. In * * *IEEE* * * *In-* *ternational* * * *Conference* * * *on* * * *Robotics* * * *and* * * *Automation* *(ICRA)*, pages 5182-5189, 2018. 1, 2

\[16\] Chao Jia and Brian L Evans. Online calibration and synchronization of cellphone camera and gyroscope. In * IEEE Global Conference on Signal and Information* *Processing*, pages 731-734, 2013. 2

\[17\] Alexandre Karpenko, David Jacobs, Jongmin Baek, and Marc Levoy. Digital video stabilization and rolling shutter correction using gyroscopes. *CSTR*, 1(2011):2, 2011. 1, 2, 3

\[18\] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. *arXiv* * * *preprint* *arXiv:1412.6980*, 2014. 5

\[19\] Jun-Mo Koo, Myoung-Won Kim, and Byung-Kwon Kang. Optical image stabilizer for camera lens assembly, Feb. 10 2009. US Patent 7,489,340. 2

\[20\] Hoang Le, Feng Liu, Shu Zhang, and Aseem Agarwala. Deep homography estimation for dynamic scenes. In * Proc. CVPR*, pages 7652-7661, 2020. 2

\[21\] Kaimo Lin, Nianjuan Jiang, Shuaicheng Liu, LoongFah Cheong, Minh N Do, and Jiangbo Lu. Direct photometric alignment by mesh deformation. In * Proc.* *CVPR*, pages 2701-2709, 2017. 1, 2

\[22\] Shuaicheng Liu, Ping Tan, Lu Yuan, Jian Sun, and Bing Zeng. Meshflow: Minimum latency online video stabilization. In * * *Proc.* * * *ECCV*, volume 9910, pages 800-815, 2016. 1, 6, 7, 8

\[23\] Shuaicheng Liu, Binhan Xu, Chuang Deng, Shuyuan Zhu, Bing Zeng, and Moncef Gabbouj. A hybrid approach for near-range video stabilization. *IEEE* *Trans. on Circuits and Systems for Video Technology*, 27(9):1922-1933, 2017. 1

\[24\] Shuaicheng Liu, Lu Yuan, Ping Tan, and Jian Sun. Bundled camera paths for video stabilization. * * *ACM* *Trans. Graphics*, 32(4), 2013. 1

\[25\] David G. Lowe. Distinctive image features from scaleinvariant keypoints. *Int.* * * *J.* * * *Comput.* * * *Vis.*, 60(2):91- 110, 2004. 2, 6, 7, 8

\[26\] Janne Mustaniemi, Juho Kannala, Simo S¨arkk¨a, Jiri Matas, and Janne Heikkila. Gyroscope-aided motion

deblurring with deep networks. In * * *2019* * * *IEEE* * * *Win-* *ter* * * *Conference* * * *on* * * *Applications* * * *of* * * *Computer* * * *Vision* *(WACV)*, pages 1914-1922. IEEE, 2019. 2, 3, 5

\[27\] Steven S Nasiri, Mansur Kiadeh, Yuan Zheng, ShangHung Lin, and SHI Sheena. Optical image stabilization in a digital still camera or handset, May 1 2012. US Patent 8,170,408. 2

\[28\] Ozan Oktay, Jo Schlemper, Loic Le Folgoc, Matthew Lee, Mattias Heinrich, Kazunari Misawa, Kensaku Mori, Steven McDonagh, Nils Y Hammerla, Bernhard Kainz, et al. Attention u-net: Learning where to look for the pancreas. *arXiv* * * *preprint* * * *arXiv:1804.03999*, 2018. 8

\[29\] Jerome Revaud, Philippe Weinzaepfel, Zaid Harchaoui, and Cordelia Schmid. Epicflow: Edgepreserving interpolation of correspondences for optical flow. In * Proc. CVPR*, pages 1164-1172, 2015. 1

\[30\] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-net: Convolutional networks for biomedical image segmentation. In * International Conference on Medical* *image computing and computer-assisted intervention*, pages 234-241. Springer, 2015. 4, 8

\[31\] Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary Bradski. Orb: An efficient alternative to sift or surf. In * Proc. ICCV*, pages 2564-2571, 2011. 6, 8

\[32\] Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary R. Bradski. ORB: an efficient alternative to SIFT or SURF. In * Proc. ICCV*, pages 2564-2571, 2011. 2

\[33\] Koichi Sato, Shigeki Ishizuka, Akira Nikami, and Mitsuru Sato. Control techniques for optical image stabilizing system. * * *IEEE Trans. on Consumer Electronics*, 39(3):461-466, 1993. 2

\[34\] Qi Shan, Wei Xiong, and Jiaya Jia. Rotational motion deblurring of a rigid object from a single image. In * 2007 IEEE 11th International Conference on Com-* *puter Vision*, pages 1-8. IEEE, 2007. 1

\[35\] Jianbo Shi et al. Good features to track. In * 1994 Pro-* *ceedings of IEEE conference on computer vision and* *pattern recognition*, pages 593-600. IEEE, 1994. 3

\[36\] Vividh Siddha, Kunihiro Ishiguro, and Guillermo A Hernandez. Hardware abstraction layer, Aug. 28 2012. US Patent 8,254,285. 2

\[37\] Deqing Sun, Xiaodong Yang, Ming-Yu Liu, and Jan Kautz. Pwc-net: Cnns for optical flow using pyramid, warping, and cost volume. In * Proc. CVPR*, pages 8934-8943, 2018. 1, 2

\[38\] Yurun Tian, Xin Yu, Bin Fan, Fuchao Wu, Huub Heijnen, and Vassileios Balntas. Sosnet: Second order similarity regularization for local descriptor learning. In * Proc. CVPR*, pages 11016-11025, 2019. 2, 6

\[39\] Yurun Tian, Xin Yu, Bin Fan, Fuchao Wu, Huub Heijnen, and Vassileios Balntas. Sosnet: Second order similarity regularization for local descriptor learning. In * Proc. CVPR*, pages 11016-11025, 2019. 8

\[40\] Miroslav Trajkovi´c and Mark Hedley. Fast corner detection. *Image* * * *and* * * *vision* * * *computing*, 16(2):75-87, 1998. 3

\[41\] Bartlomiej Wronski, Ignacio Garcia-Dorado, Manfred Ernst, Damien Kelly, Michael Krainin, Chia-Kai Liang, Marc Levoy, and Peyman Milanfar. Handheld multi-frame super-resolution. * * *ACM* * * *Trans.* * * *Graphics*, 38(4):28:1-28:18, 2019. 1

\[42\] DH Yeom. Optical image stabilizer for digital photographing apparatus. * IEEE Trans. on Consumer Elec-* *tronics*, 55(3):1028-1031, 2009. 2

\[43\] Kwang Moo Yi, Eduard Trulls, Vincent Lepetit, and Pascal Fua. LIFT: learned invariant feature transform. In * * *Proc.* * * *ECCV*, volume 9910, pages 467-483, 2016.

\[44\] Tirra Hanin Mohd Zaki, Musab Sahrim, Juliza Jamaludin, Sharma Rao Balakrishnan, Lily Hanefarezan Asbulah, and Filzah Syairah Hussin. The study of drunken abnormal human gait recognition using accelerometer and gyroscope sensors in mobile application. In * 2020 16th IEEE International Colloquium on* *Signal* * * *Processing* * * *&* * * *Its* * * *Applications* * * *(CSPA)*, pages 151-156, 2020. 1, 2

\[45\] Julio Zaragoza, Tat-Jun Chin, Michael S Brown, and David Suter. As-projective-as-possible image stitching with moving dlt. In * * *Proc.* * * *CVPR*, pages 2339- 2346, 2013. 1, 2

\[46\] Jirong Zhang, Chuan Wang, Shuaicheng Liu, Lanpeng Jia, Jue Wang, Ji Zhou, and Jian Sun. Content-aware unsupervised deep homography estimation. In * * *Proc.* *ECCV*, 2020. 1, 2, 5, 6, 7, 8