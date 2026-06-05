# 

**GOOD VIBRATIONS? HOW IMAGE STABILISATION INFLUENCES **

# PHOTOGRAMMETRY - Nocerino 1, F. Menna 2, G. J. Verhoeven 3

1 Dipartimento di Scienze Umanistiche e Sociali, University of Sassari, Sassari, Italy; enocerino@uniss.it

2 3D Optical Metrology (3DOM) unit, Bruno Kessler Foundation (FBK), Trento, Italy; fmenna@fbk.eu 3 Ludwig Boltzmann Institute for Archaeological Prospection & Virtual Archaeology (LBI ArchPro), Vienna, Austria; Geert.Verhoeven@archpro.lbg.ac.at **Commission II **

**KEY WORDS: ** image and video stabilisation, motion blur, accuracy potential, camera calibration, interior orientation **ABSTRACT: ** Image stabilisation (IS) is a family of approaches whose aim is to reduce motion blur in still images and shaking effect in video frames. A variety of techniques are currently implemented in cameras and camcorders: some involve hardware solutions, other are software approaches. In general, IS for still photography entails hardware in-camera or in-lens solutions. Video stabilisation, on the other hand, can be accomplished with software algorithms, either in real-time within the camera or in post-processing. Whereas IS aids photography and video making, its influence on the photogrammetric 3D modelling process has not been investigated. This article addresses this aspect. To this purpose, several laboratory and real-world tests were carried out, whose results showed that IS must be disabled when accuracy matters in photogrammetric projects. Details are provided in the manuscript. ** **

# 1. INTRODUCTION

Many factors contribute to the sharpness of an image: the wavelength of the imaged electromagnetic radiation, the size of the lens aperture (the primary influencer of depth of field and the amount of diffraction softening), incorrect focusing, monochromatic lens aberrations (such as coma, astigmatism, and spherical aberration), longitudinal/axial and transverse/lateral chromatic aberrations, the amount and type of image noise plus possible denoising measures. Finally, there are also various causes for motion-induced unsharpness. This paper mainly focuses on the latter. Unsharpness due to motion is either caused by movement of the object/scene to be photographed or motion of the camera (known as camera shake). Camera shake is not only present when shooting from very dynamic platforms like aeroplanes, satellites, UAVs, or cars, but even applicable when photographing handheld as user tremor can result in vibrations whose magnitude is too big to be counteracted by the shutter speed. This hand-shake induced blur worsens with longer focal length lenses. To still obtain a sharp image from a hand-held camera and lens combination, the general rule-of-thumb is that the exposure time should be equal or shorter than the reciprocal of the 35mm format equivalent focal length in use. As an example: a 50 mm lens necessitates a shutter speed of at least 1/50 s. In photography, this guideline is known as the reciprocal rule. In situations where the object/scene is static, several techniques exist to extend this exposure time (i.e. slowing down the shutter speed): either via extra camera support (passive like a tripod or active via a gimbal) or exploiting a function available in most photographic systems, i.e. the image stabilisation. Although this function can mean the difference between a blurry picture and a sharp one, its use in photogrammetric image acquisition is usually discouraged as it continuously changes the camera's interior orientation. This paper wants to check if this advice is valid by delving into image stabilisation techniques and

quantifying their possible negative influence on the photogrammetric process. **1.1 Image stabilisation techniques **

The term image stabilisation (IS) refers to a range of techniques developed to reduce motion blur in images and frame-to-frame jitter in videos (Figure 1). A first, basic distinction can be made between hardware and software stabilisation. In the first case, it is referred to as optical stabilisation (OIS), which can take place in the lens (lens-based IS), in the camera body on the imaging sensor (sensor-shift or inbody IS) or via a combination of the two methods (dual IS). The different OIS techniques are named differently depending on the camera manufacturer. For example, the in-lens IS implemented by Nikon is called vibration reduction (VR), while Canon dubs its system image stabilizer (IS). Software stabilisation implemented in some video cameras can perform in real-time and it is called digital IS (DIS) or electronic IS (EIS). If, on the other hand, videos are edited in post processing (offline), then stabilisation algorithms, also known as stabilisation filters, are used. While OIS is effective in reducing blur due to the motion of a camera, including involuntary hand shaking, EIS does not solve the problem of motion blur but improves the smoothness of the video by reducing the trembling or jitter between frames. OIS uses sensors, such as gyroscopes, to detect camera movement and actuators to move the lens and/or sensor to counteract the motion. Over time, systems have evolved from techniques based on inertial sensors arranged on 2-axis to current 5-axis methods such as those implemented in Olympus or Sony. In EIS, gyroscopes or accelerometers are also employed to measure hand jitter and the frames are shifted by a commensurate number of pixels. EIS requires the frames to be cropped with respect to the full sensor size, as the sensor edges are used as buffer zones to compensate for the motion (Sachs et al., 2006).

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.

**Figure 1**: Image stabilisation techniques.

# CAMERA BODY SENSOR LENS

# TESTED ACQUISITION

# MODE

# IMAGE STABILISATION Nikon D750 24.2 Mpx full-frame

# DSLR Tamron 70-210mm f/4

Di VC USD still images in-lens Tamron SP 24-70mm f/2.8 Di VC USD Olympus OM-D E-M1 Mark II 20 Mpx Micro Four Thirds mirrorless Olympus Zuiko 12-45 f/4 lens still images 5-axis in-body Olympus OM-D E-M5 Mark II 16 Mpx Micro Four Thirds mirrorless Olympus Zuiko 12-45 f/4 lens still images 5-axis in-body video 5-axis in-body 5-axis in-body + DIS Nikon Z7 II 45.4 Mpx full-frame mirrorless

# NIKKOR Z 20mm f/1.8 S still images in-body

**Table 1**. Imaging systems tested Cameras or camcorders may adopt a hybrid IS (HIS) combining OIS and EIS: OIS acts on the blurring of individual frames (intraframe IS), while EIS smooths out the video flow reducing the abrupt shifts from one frame to the next (inter-frame IS). OIS is highly desirable and useful in still photography, as it allows shooting hand-held by increasing exposure times and keeping ISO values low in low light conditions. Similarly, EIS is widely used in video making. Offline stabilisation algorithms track the movement of pixels from one frame to another and correct for jitter by moving and cropping the image frame. An overview of possible methods is provided in Guilluy (2018). In addition to the IS techniques presented here, there are 'external' solutions that employ 3-axis gimbals as stabilisation systems to eliminate vibration and shake in hand-held shooting or cameras attached to vehicles. In this article we focus on OIS and EIS and their impact on the photogrammetric process. While the benefit for photography and video making is unquestionable, we aim at exploring the positive or negative effects that these techniques can have in photogrammetry.

# 2. RELATED RESEARCH

Although it is difficult to quantify the influence of image quality on the photogrammetric process, it is of paramount importance

to ensure the acquisition of sharp, correctly focused images, with minimal optical aberrations to reduce the influence of effects that cannot be easily modelled or quantified. Different scholars dealt with image quality and its impact in different contexts. For example, Menna et al. (2017) analysed the accuracy potential lost in underwater photogrammetry due to optical aberrations introduced by the underwater port. Chromatic aberrations have been addressed for high precision photogrammetry (Luhmann et al., 2006) and in underwater photogrammetry as well (Neyer et al., 2019; Helmholz and Lichti, 2020). An automatic detection and removal approach of blurred UAV images was developed by Sieberth et al. (2016) to improve analysis and interpretation of the data, as well as the accuracy of the photogrammetric processing. The effect of rolling shutter has also been investigated and shown to negatively influence the accuracy potential of UAV photogrammetry. Several approaches have been proposed to mitigate or correct it, methods that have also been implemented in both research and commercial software (Vautherin et al., 2016; Zhou et al., 2020). However, to the authors' knowledge, there is no systematic investigation of the impact of IS methods.

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.

# 3. MATERIALS AND METHODS **3.1 Preliminary considerations **

Portability is among the most appreciated characteristics of modern digital cameras and, consequently, part of the popularity of photogrammetry in architectural and archaeological 3D modelling projects. Since the camera is usually kept immobile during the exposure time in such close-range scenarios, tripods are ideal to provide the sought-after camera stability. However, using a tripod can significantly lengthen the overall time required for the image acquisition, often making a non-negligible difference for the project. In addition, some working environments might also hamper the use of a tripod (e.g. Verhoeven et al., 2021). Luckily, tripods are not always needed; thanks to the steady improvements imaging sensors and camera electronics have undergone in the past decade, digital cameras with a Micro Four Thirds or larger imaging sensor can now be used with relatively high ISO values (i.e. ISO 1600 to ISO 3200) and still yield images with an acceptable noise level; such high ISO values enable the use of shutter speeds that are usually fast enough to freeze the subtle camera motion caused by user tremor, thus making hand-held photography possible in many photogrammetry projects. For hand-held image acquisitions, the camera can be set in manual exposure mode, stopping down the aperture to reach a compromise between depth of field, optical aberration reduction and diffraction softening. The shutter speed is chosen according to the reciprocal rule mentioned above, typically with some conservatism. The ISO value is fixed or set in auto mode depending on whether lighting conditions are constant. In this scenario, IS acts on the ISO setting, thus mainly affecting the noise level of the image. An IS claiming a 5 exposure stops improvement means that an image taken normally at 3200 ISO can be acquired at ISO 100 by slowing down the shutter speed by 5 stops (or 32 times).

**Figure 2**: 3D (left) and planar (right) test fields. **3.2 Experiments **

With above considerations in mind, we designed laboratory and real word experiments to specifically study the influence of IS on the accuracy of photogrammetric measurements and support a quantitative analysis on the pros and cons of IS in 3D modelling projects. **3.2.1 ** **In the lab: ** Table 1 reports the results of the laboratory calibrations carried out using different camera systems. The tested configurations entailed in-body IS, in-lens IS and DIS technologies. The experiments were performed in the 3DOMFBK laboratory where two test fields (Figure 2) of different sizes (3x3x3 m 3 and 1.5x1 m 2 ) and shapes (3D and planar) are available with known ground truth 3D coordinates. Their estimated accuracy was better than 0.1mm and 0.02mm for the 3D and planar test fields, respectively. Each camera system was used to acquire the test field once with the IS on and once with the IS off. Manual focus was used for all

the cameras and kept unchanged during the two image acquisitions (on/off). In each test the shutter speed was chosen according to the rule-of-thumb of the reciprocal of the equivalent focal length and image acquisition carried out first with the IS off. Then the shutter speed was slowed down with about three stops and IS activated. The camera network geometry for both still and video modes comprised multi-convergent poses (about 50. with roll diversity. Care was taken to obtain a very similar  camera network geometry for the IS on and off photo acquisitions, with a difference in the exterior orientation parameters of only a few centimetres/degrees. **3.2.2 ** **In the field: ** An additional experiment was carried out in the context of the graffiti documentation project INDIGO (<https://projectindigo.eu),> simulating a real photogrammetric survey application. The subject of the survey was a 35 m long graffiti-covered wall in the city centre of Vienna (Figure 3). The image acquisition took place in daylight with twin cameras (Nikon Z 7II equipped with a Nikon NIKKOR Z 20mm f/1.8 S lens) mounted on a rigid stereo bar so that the cameras' imaging sensors were about 20 cm apart. The optical axes of the systems were not entirely parallel to make the field of views as similar as possible. The stereo bar was initially mounted on a tripod, allowing both cameras to be focused on the same object area (using the smallest autofocus point). Afterwards, autofocus got disabled and both focusing rings were immobilised with cellophane tape. The two cameras featured identical image acquisition and processing settings with one exception: the sensor-shift IS was deactivated in one camera and activated in the other. After simultaneously starting a five-second interval shooting on both cameras, the stereo rig was removed from the tripod and hand-held to acquire a dense convergent network of 99 photos featuring various roll angles and different object distances. Photographing with this imaging setup yielded two sets of nearly identical images, making it safe to assume that any difference in their photogrammetric processing is due to the influence of the in-body IS (and not related to different processing parameters or dissimilar camera networks). Well-recognisable features on the graffiti wall were measured reflectorless with a Lecia TS16 total station (TS), yielding coordinates of 26 object points with an estimated 3D accuracy better than 1.5 cm. Since these points were intended as reference points to assess the accuracy of the final image orientation, they were indicated as homogenous as possible in both image sets. To assess the influence of the two IS settings (on and off) on the 3D modelling results, a comparison between the generated mesh models was also performed.

# 4. RESULTS **4.1** ** ** **Laboratory experiments **

Table 2 summarises the results from the laboratory tests. There is clearly an increase in uncertainty in the determination of the interior orientation parameters (principal distance and principal point) and a deterioration in both precision and accuracy in image and object space when IS is active. This overall worsening of bundle adjustment (BA) results is most noticeable with in-body IS systems, where a factor up to 300% both in image and object space is observed (tests n. 5-6 in Table 2). For the in-lens IS in the camera configuration Nikon D750 + Tamron 70-210mm f/4 Di VC USD @ 70 mm (tests n. 1-2 in Table 2) there is no significant difference between networks acquired with or without IS. A slight worsening of about 20% is observed for the Nikon D750 + Tamron SP 24-70mm f/2.8 Di VC USD @ 24 mm (tests - 3-4 in Table 2).

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.

# TEST NUMB. CAMERA SYSTEM IS TESTFIELD

# PRINCIPAL

# DISTANCE \[pix\] PPAx \[pix\] PPAy \[pix\] RMS reprojection error on targets \[pix\] GSD \[mm\]

# RMSE on targets \[mm\] Nikon D750 + Tamron 70-210mm f/4 Di VC USD @ 70 mm (still images)

ON Planar 13378.1 ± 0.34 -44.78 ± 0.37 23.26 ± 0.26 0.34 0.14 0.062

OFF Planar 13375.7 ± 0.37 -43.11 ± 0.43 0.24 ± 0.31 0.34 0.14 0.064 Nikon D750 + Tamron SP 24-70mm f/2.8 Di

# VC USD @ 24 mm (still images)

# ON

3D 4063.96 ± 0.14 4.39 ± 0.10 -6.81 ± 0.09 0.80 0.5 0.94

# OFF

3D 4067.12 ± 0.10 11.09 ± 0.07 -2.68 ± 0.06 0.62 0.5 0.77 Olympus OM-D E-M5 Mark II + Zuiko @ 35mm (still images) ON Planar 9698.82 \pm 1.18 20.0218 \pm 1.16 28.41 \pm 0.96 1.07 0.20 0.330

OFF Planar 9699.98 \pm 0.36 46.37 \pm 0.36 25. 03 \pm 0.31 **0.31 ** **0.20 0.098 ** Olympus OM-D E-M5 Mark II + Zuiko @ 12mm (still images)

ON 3D 3338.4 \pm 0.16 -4.72 ± 0.13 -11.2 ± 0.12 1.12 0.8 1.45

OFF 3D 3340.75 ± 0.05 -4.11 \pm0.05 -5.20 ± 0.04 **0.41 ** **0.8 ** **0.86 ** Olympus OM-D E-M5 Mark II + Zuiko @ 12mm (Full HD video)

ON (in-body) 3D 1406.09 ± 0.32 2.47 ± 0.36 -4.99 ± 0.27 2.06 1.6 4.46 ON (in-body +

digital) 3D 1625.71 \pm 0.32 32.72 \pm 0.4 15.09 \pm 0.29 1.89 1.6 2.84

OFF 3D 1389.12 ± 0.13 -0.16 ± 0.13 -3.2 ± 0.11 0.77 1.6 2.36 Olympus OM-D E-M1 Mark II + Zuiko @ 12mm (still images)

# ON

3D 3749.98 ± 0.21 -12.86 ± 0.20 -25.03 ± 0.17 1.77 0.7 1.63

# OFF

3D 3749.68 ± 0.07 -8.04 ± 0.06 -12.36 ± 0.05 0.66 0.7 0.75

**Table 2**. Results of the calibration tests in laboratory.

# CAMERA SYSTEM

IS PRINCIPAL DISTANCE \[pix\] PPAx \[pix\] PPAy \[pix\] RMS reprojection error on reference points \[pix\] GSD \[mm\] RMSE on reference points \[mm\]

Nikon Z7 II + NIKKOR Z 20mm f/1.8 S (still images)

ON 4665.81 \pm 0.11 74.53 ± 0.11 -26.47 ± 0.09 2.69 1.55 9.74

OFF 4677.5 \pm 0.04 18.34 \pm 0.04 83.62 \pm 0.04 0.63 1.55 7.66

**Table 2**. Results from the INDIGO experiment. **4.2** ** ** **Real-world test **

These laboratory test results were confirmed by the photo sequences of the graffiti wall. With IS on, the recovered IO showed a much higher uncertainty (up to a factor 3), with the standard deviations of the principal distance and principal point up to 3-times higher than when IS was deactivated (Table 3). This finding is confirmed by the residuals (reprojection error) in image space of the marked reference points which are much higher for the system with IS on than with IS off (by a factor of 4). The discrepancy in object space is not equally evident, probably because the accuracy of measuring and indicating the reference points is not sufficient to reveal any meaningful difference between the two systems. To better highlight the differences in object space, an analysis of the meshes produced with the two setups was carried out (Figure 3). Each mesh was extracted from depth maps that leveraged all image pixels in Agisoft Metashape 1.7.5. As can easily be seen, the mesh produced for the sensor-stabilised images is less detailed in large parts and much noisier in others (Figure 3 first row). Even the small statue in the front right of the scene did not get modelled from the IS-active photo collection. These inferior results are also apparent from the third row in Figure 3: the

number of stereo pairs that contributed to the matching is significantly lower (colour-coded with red and green) for the ISactive photo set, than the number of stereo pairs for the mesh generated from the IS deactivated set (colour-coded with blue, Figure 3 third row). The poorer quality mesh reflects a less precise image orientation.

# 5. CONCLUSIONS

Image stabilisation is a revolutionary feature in photography and video making. For still images it provides images of superior quality in terms of noise and details (Figure 4); it gives wobble/vibration-free footage in video applications. Unfortunately, for photogrammetric applications, the benefits provided by this feature may be lessened by the worsening of accuracy. The experimentation carried out within this study provided, for the first time, an assessment of the influence of image stabilisation for photogrammetric applications through systematic tests. A total of 13 camera calibrations and 2 image acquisitions in a real-world test showed that in-lens IS does not significantly affect the potential accuracy, while in-body IS always provides worse precision and accuracy metrics both in image (RMS reprojection error on targets) and object space (RMSE on targets), respectively.

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.

# IS ON IS OFF Mesh Vertex-coloured (RGB) mesh

Mesh coloured according to the total number of stereo pairs per vertex. Red corresponds to a single stereo pair (higher

uncertainty), green to 5 stereo pairs, blue to 100 stereo pairs (lower uncertainty).

Figure 3: Comparison between meshes from the INDIGO dataset. The left column shows a detail of the mesh obtained from the images with the IS on; the right column displays the same detail from the images with IS off. A significant improvement (less noise, lower uncertainty and more details) can easily be observed in the mesh produced from the images with IS off.

# IS ON - 1/8s f/8 - ISO 200 IS OFF - 1/60s f/8 ISO 2000

Figure 4. Image quality difference on a target imaged in tests number 5 (IS on) and 6 (IS off) respectively. In order to obtain a sharp image a faster shutter speed was compensated by a higher ISO value. The resulting image is much noisier. The authors plan to further elaborate on the different types of IS in the future. Through testing additional cameras and lenses from different manufacturers and reporting on extra case studies in real photogrammetric survey conditions, they aim to

better investigate the reasons why in-body IS causes such a deterioration of the photogrammetric process compared to the in-lens IS.

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.

# ACKNOWLEDGEMENTS

Project INDIGO is funded by the Heritage Science Austria programme of the Austrian Academy of Sciences (ÖAW).

# REFERENCES

Guilluy, W., 2018. Video stabilisation: A synopsis of current challenges, methods and performance evaluation (Doctoral dissertation, Université Sorbonne Paris Cité). <https://tel.archives-ouvertes.fr/tel-03006243/document>

Helmholz, P. and Lichti, D.D., 2020. Investigation of Chromatic Aberration and Its Influence on the Processing of Underwater Imagery. Remote Sensing, 12(18), p.3002.

Luhmann, T., Hastedt, H. and Tecklenburg, W., 2006, September. Modelling of chromatic aberration for high precision photogrammetry. In Commission V Symp. on Image Engineering and Vision Metrology, Proc. ISPRS (Vol. 36, No. 5, pp. 173-178).

Menna, F., Nocerino, E. and Remondino, F., 2017, June. Optical aberrations in underwater photogrammetry with flat and hemispherical dome ports. In Videometrics, Range Imaging, and Applications XIV (Vol. 10332, p. 1033205). International Society for Optics and Photonics.

Neyer, F., Nocerino, E. and Grün, A., 2019. Image quality improvements in low-cost underwater photogrammetry. International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 42(2/W10), pp.135142.

Sachs, D., Nasiri, S. and Goehl, D., 2006. Image stabilisation technology overview. InvenSense Whitepaper. <https://www.digikey.at/Web%20Export/Supplier%20Content> /invensense-1428/pdf/invensense-image-stabilisationtechnology.pdf

Sieberth, T., Wackrow, R. and Chandler, J.H., 2016. Automatic detection of blurred images in UAV image sets. ISPRS Journal of Photogrammetry and Remote Sensing, 122, pp.1-16.

Vautherin, J., Rutishauser, S., Schneider-Zapp, K., Choi, H.F., Chovancova, V., Glass, A. and Strecha, C., 2016. Photogrammetric accuracy and modeling of rolling shutter cameras. ISPRS Annals of Photogrammetry, Remote Sensing & Spatial Information Sciences, 3(3).

Verhoeven, G., Santner, M. and Trinks, I., 2021. From 2D (to 3D) to 2.5 D: not all gridded digital surfaces are created equally. In 28th CIPA Symposium "Great Learning & Digital Emotion" (Vol. 8, pp. 171-178).

Zhou, Y., Daakir, M., Rupnik, E. and Pierrot-Deseilligny, M., 2020. A two-step approach for the correction of rolling shutter  distortion in UAV photogrammetry. ISPRS Journal of Photogrammetry and Remote Sensing, 160, pp.51-66.

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLVI-2/W1-2022 9th Intl. Workshop 3D-ARCH "3D Virtual Reconstruction and Visualization of Complex Architectures", 2-4 March 2022, Mantua, Italy

This contribution has been peer-reviewed. <https://doi.org/10.5194/isprs-archives-XLVI-2-W1-2022-395-2022> \| © Author(s) 2022. CC BY 4.0 License.