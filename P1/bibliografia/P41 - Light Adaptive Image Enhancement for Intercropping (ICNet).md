# Light adaptive image

enhancement for improving visual analysis in intercropping cultivation

## Wei Zhong 1, Wanting Yang 2, Yunfei Wang 1, Xiang Dong 1,

Xiaowen Wang 1 \*, Weidong Jia 1, Mingxiong Ou 1

## and Mingde Yan 3

1 School of Agricultural Engineering, Jiangsu University, Zhenjiang, China, 2 School of Mechatronic Engineering, Taizhou University, Taizhou, China, 3 Chinese Academy of Agriculture Mechanization Sciences Group Co., Ltd., Beijing, China

Intercropping maize and soybean with distinct plant heights is a typical practice in diversi ﬁ ed cropping systems, where shadows cast by taller maize plants onto soybean rows pose signi ﬁ cant challenges for image based recognition. This study conducted experiments throughout the entire soybean - maize intercropping period to address illumination variation. Based on the height difference between crops, solar elevation angle, and light intensity at the top of the soybean canopy, an illumination compensation regression model was developed. The model was applied to correct soybean canopy images and compared against traditional enhancement methods, including histogram equalization, Multi-Scale Retinex (MSR), and gamma correction. Quantitative evaluation using peak signal-tonoise ratio (PSNR) showed the proposed method achieved 40.79 dB, indicating superior image quality. Furthermore, analysis of RGB and HLS channels revealed a consistent increase in brightness from left (darker) to right (brighter) across the images. Speci ﬁ cally, green channel values rose from 150-230 to 180-240, and overall RGB values exceeded 150, suggesting improved brightness and reduced local ﬂ uctuations. Brightness increased from 90-200 to 150-220, with the left region rising from 125 to 175. Finally, a comparison of channel-wise standard deviations among methods showed that the proposed algorithm exhibited lower variance in the green (G) and hue (H) channels, with favorable consistency across others. These results demonstrate the model ' s effectiveness in achieving smoother brightness transitions, thereby enhancing image uniformity and mitigating the negative impact of uneven illumination on recognition tasks.

# KEYWORDS

illumination compensation, intercropping, height difference, solar elevation angle, growth stage Frontiers in Plant Science frontiersin.org

# OPEN ACCESS

EDITED BY Pei Wang, Southwest University, China

REVIEWED BY Abd Abrahim Mosslah, University of Anbar, Iraq Jie Lu, Wageningen University and Research, Netherlands Yunfei Wang, Zhengzhou University, China \*CORRESPONDENCE Xiaowen Wang wangxiaowen@ujs.edu.cn

# RECEIVED 01 June 2025 ACCEPTED 01 August 2025 PUBLISHED 20 August 2025

CITATION Zhong W, Yang W, Wang Y, Dong X, Wang X, Jia W, Ou M and Yan M (2025) Light adaptive image enhancement for improving visual analysis in intercropping cultivation. Front. Plant Sci. 16:1639016. doi: 10.3389/fpls.2025.1639016

COPYRIGHT © 2025 Zhong, Yang, Wang, Dong, Wang, Jia, Ou and Yan. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. TYPE Original Research PUBLISHED 20 August 2025 DOI 10.3389/fpls.2025.1639016

## 1 Introduction

Intercropping has been widely adopted due to its advantages in intensive land use and production ef ﬁ ciency ( Kass, 1978; Andersen, 2025 ). It is a cultivation system in which two or more crops are simultaneously grown in rows or strips on the same land within a single growing season ( MacLaren et al., 2023; Du et al., 2018 ). On average, intercropping can increase production ef ﬁ ciency by 20 - 30% and also contributes to weed suppression and a reduction in pests and diseases ( Ren et al., 2019 ). In intercropping systems, taller crops intercept more sunlight, casting shadows on shorter crops and reducing their exposure to direct radiation. This shading effect substantially in ﬂ uences the morphological and physiological traits of the understory crops ( Franklin, 2008; Raza et al., 2019 ). Shading alters the microclimate experienced by short-statured crops by reducing the infrared radiation they receive, thereby affecting light intensity ( Wang et al., 2021a; Zhu et al., 2015 ). These changes trigger a series of responses in plant phenotypes and physiology ( Fan et al., 2018; Hussain et al., 2019 ), in ﬂ uencing critical traits such as stem diameter, leaf thickness, leaf area index (LAI), photosynthetic capacity, aboveground biomass, yield, and plant height ( Deng et al., 2021; Petrella et al., 2022 ). Despite its agronomic advantages, the large scale adoption of intercropping has been constrained by mechanization challenges ( Bybee-Finley and Ryan, 2018 ). Accurate recognition of crop traits is a prerequisite for mechanized operations, yet uneven shading in intercropped systems hampers reliable image based detection. Shading induced brightness variation reduces the quality of captured images and interferes with visual perception and object recognition. Image recognition technologies have increasingly been applied in agriculture for tasks such as plant protection ( Routray et al., 2019 ), harvesting, and sowing ( Wang et al., 2022; Feng et al., 2024 ). Applications extend across multiple crop species, including wheat, maize, and rice ( Zhu et al., 2023; Wang et al., 2021b; Sun et al., 2018, 2021 ). However, during image acquisition, both the lighting conditions and the medium through which light propagates signi ﬁ cantly affect image quality ( Xu et al., 2023 ). To address low light image degradation, researchers have explored both hardware and software solutions. Specialized low light cameras have demonstrated strong performance, but their high cost and limited practicality hinder widespread use. On the software side, digital image processing techniques remain the primary method for image enhancement, though challenges such as color distortion and uneven brightness persist ( Li et al., 2022 ). Traditional enhancement methods include histogram equalization, which redistributes pixel intensity to expand an image ' s dynamic range and improve contrast ( Coltuc et al., 2006; Lee et al., 2013b ). Additionally, image enhancement models based on Retinex theory have been developed, though they often struggle to balance brightness recovery with dynamic range compression. To overcome this limitation, the multi-scale Retinex (MSR) method was introduced and further re ﬁ ned by Lee et al. ( Lee et al., 2013a ), improving its parameter adaptability. MSR decomposes an image into re ﬂ ectance and illumination components and has served as the foundation for various subsequent methods ( Guo et al., 2016; Li et al., 2018 ). Similarly, gamma correction adjusts brightness by applying a

nonlinear transformation that approximates human visual perception, improving brightness uniformity, especially in darker regions ( Huang et al., 2012 ). In intercropping systems, the shading distance varies according to the height of taller crops and the solar elevation angle. However, current studies offer limited research on the relationship between shading distance and light intensity. Statistical models constructed based on the shading capacity of intercropping systems using regression analysis are often heavily in ﬂ uenced by actual measurement data. To simulate the shading capacity at various positions within the canopy, it is essential to establish a general model that directly quantify light intensity in intercropping systems. Factors such as crop canopy height, the differences in crop height, and the solar elevation angle are crucial in determining the light environment, Continuous measurements throughout the entire growing season are required to capture data across different periods for improved accuracy. Strip intercropping of maize and soybean is widely practiced in China; hence, this study focuses on soybeanmaize intercropping as a test subject. In shading research, soybean, being a shade-intolerant species, frequently receives more attention. A statistical analysis conducted by Li et al. (2023) on soybean - maize intercropping systems revealed that the taller maize plants signi ﬁ cantly obstruct direct solar radiation, thereby in ﬂ uencing the light availability for shorter soybean plants. Speci ﬁ cally, the shading ratio for soybean in the southernmost row was reported to range between 52.44% and 57.44%, indicating substantial light interception. Although light compensation models have been applied in ﬁ elds such as underwater imaging, their adaptation to open ﬁ eld agricultural settings remains limited. This study bridges that gap by incorporating crop speci ﬁ c geometry and solar parameters into the illumination correction process, marking a novel interdisciplinary application of physics based enhancement strategies. This study aims to develop a color constancy algorithm capable of counteracting the effects of various adverse light sources, thereby obtaining an intrinsic image that re ﬂ ects fundamental physical properties of the scene ' s surface. This study aims to directly quantify the relationship between light intensity and shading in maize-soybean intercropping systems. The research objectives are as follows: (1) to develop a quantitative shading model that accounts for the geometric relationship between canopy structure (the height difference between adjacent maize and soybean canopies) and the position of the sun; (2) to process the shaded areas of images using traditional methods and evaluate the resulting image quality; and (3) to establish an image processing algorithm tailored to both tall and short crops, by applying an illumination Compensation method to smooth lighting effects in the images.

## 2 Materials and methods

## 2.1 Experimental design and image acquisition

A ﬁ eld experiment on soybean - maize intercropping was conducted at the Zhenjiang Agricultural Science and Technology Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

Park in Jiangsu Province, China (32°12 ′ N, 119°18 ′ E). From 2020 to 2023, the site had an average annual temperature of 16.5°C, annual precipitation of 1105 mm, and annual sunshine duration of 1956 hours. On June 8, 2024, maize (Jiangyu 688) and soybean (Qihuang 34) were sown. The total experimental area was 6.67 ha, and the intercropping system consisted of four rows of maize (row spacing: 60 cm; plant spacing: 20 cm) alternated with six rows of soybean (row spacing: 30 cm; plant spacing: 10 cm), with a 60 cm wide buffer zone between the maize and soybean strips. The rows were oriented east - west to ensure consistent lighting conditions. Observations were carried out at ﬁ ve key growth stages of maize: the third leaf, seventh leaf, tasseling, milk, and maturity stages, which corresponded to the third leaf, ﬂ owering, pod setting, grain ﬁ lling, and maturity stages of soybean, respectively. At each stage, plant height was measured, and light intensity at the top of the soybean canopy was recorded at 8:00 AM under clear sky conditions. In addition, images of the soybean strip were collected, as shown in Figure 1. Plant height was de ﬁ ned as the vertical distance from the stem base to the uppermost point of the canopy. For each growth stage, ten maize plants and ten soybean plants were randomly selected and measured. The average height for each species was calculated to represent the mean canopy height, and the difference in height between maize and soybean was used to assess shading effects. Light intensity measurements were taken at the top of each soybean row using a multi-light source illuminometer (DL333205, Deli Group, Ningbo, China). Three random positions per row were selected, and the average reading was used to represent the light intensity for each growth stage. Image acquisition was conducted using a DJI Mavic 2 drone (DJI, Shenzhen, China). A drone was employed to capture images from a height of 2 meters above the soybean canopy. The camera operated at a resolution of 2688 × 1512 pixels and was oriented vertically downward, with the ﬂ ight direction aligned with the row orientation of the soybean plants. At each growth stage, images were collected from two adjacent plots: an experimental plot and a control plot. Speci ﬁ cally, 20 images per stage were taken from the experimental plot for model parameterization, while 10 images per stage were captured from the control plot to serve as a dataset for subsequent model validation. In this study, light intensity was measured across different soybean rows at various growth stages to obtain distribution pro ﬁ les of illumination variation within the soybean strip. Based on these measurements, an illumination compensation

algorithm was developed to address the uneven lighting conditions in intercropping systems. To validate the effectiveness of the proposed model, soybean canopy images were collected at multiple growth stages and processed using different enhancement algorithms. Comparative analyses of the RGB and HLS channel values before and after enhancement were conducted, allowing identi ﬁ cation of the most effective image enhancement method.

## 2.2 Illumination compensation model construction

In intercropping systems, uneven illumination within the soybean strip can negatively affect the accuracy of subsequent soybean information extraction. To address this issue, this study enhances soybean canopy images based on the observed variation in light intensity across different rows. This process is hereafter referred to as illumination compensation. In this study, the maize and soybean strips were simpli ﬁ ed and modeled as rectangular cuboids. It was assumed that sunlight transmission through the maize canopy was negligible, and the light intensity received by the soybean strip was primarily in ﬂ uenced by direct solar radiation, atmospheric scattering, and re ﬂ ected light from the adjacent maize strip to the south. The shading distance cast by the maize strip was determined primarily by plant height and the solar angle. However, there is limited research on the quantitative relationship between shading distance and irradiance. In this work, particular attention was given to the effects of plant height difference and solar elevation angle on shading behavior within the soybean strip. The height difference was de ﬁ ned as the vertical distance between the top of the maize canopy and the top of the soybean canopy, while the solar elevation angle referred to the angle between the sun ' s rays and the horizontal plane. The experimental ﬁ eld was oriented east - west, and the soybean - maize intercropping system was observed from June to October, during which the soybean strip was primarily shaded by the southern maize strip throughout the day. To facilitate analysis, the soybean rows were labeled from south to north as R1 to R6, as shown in Figure 2. Compensation curves re ﬂ ecting the impact of plant height on light intensity across different growth stages were established

FIGURE 1 (a) Drone captured photos and (b) soybean strip photos. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

through statistical analysis, yielding distinct light intensity curves for each stage. These curves were subsequently employed to enhance images by applying the corresponding light intensity adjustments. In the shaded areas, light intensity predominantly arises from direct sunlight, scattered light, and ambient re ﬂ ected light. Moreover, the total light intensity in these regions is in ﬂ uenced by both the solar altitude angle and the height difference between the crops. Based on the Equations 1 - 6, the total illuminance in the shaded region was derived ( Yan et al., 2015; Sarac ̧ og ̆ lu and Gündüz, 2009 ). E = E0 cos q (1)

Where E is the actual light intensity; E 0 is the light intensity of the sun in direct sunlight; q is the solar elevation angle. $$ L = $$ h tan q (2)

Where L is the length of the shade; h is the height difference of the crop.

E shadow = E 0 ( cos q − f ( h, d )) + E diffuse + E reflected (3)

Where E shadow is the light intensity of the shaded area; f ( h, d ) is the shading effect due to the height difference h and the position d in the shadow; E diffuse is the scattered light, which usually accounts for 10-20% of the total radiation; and E re ﬂ ected is the ambient re ﬂ ected light. E diffuse = E 0 D f (4)

Where D f is the scattered light coef ﬁ cient, 0.1-0.2 on a clear day. E reflected = E 0 a (5)

Where a is the re ﬂ ectance, and the soybean line is 0.1.

Eshadow = E0( cos q −f (h, d)) + E0Df + E0a (6)

## 2.3 Illumination compensation algorithm

This section presents the illumination compensation algorithm (ICNet) developed in this study and compares its performance with three conventional enhancement methods: histogram equalization, multi-scale Retinex (MSR), and gamma correction. The comparison was conducted using both quantitative (PSNR) and qualitative (RGB/HLS) metrics. Histogram equalization enhances the overall contrast of an image by redistributing the grayscale values to achieve a more uniform intensity distribution. Speci ﬁ cally, it transforms the grayscale histogram using the cumulative distribution function, allowing the pixel values to be more evenly spread across the dynamic range. However, in images with substantial brightness differences, this method may lead to excessive noise ampli ﬁ cation and structural distortion ( Dai et al., 2019 ). Retinex is an image enhancement algorithm inspired by the human visual perception system, designed to separate the illumination and re ﬂ ectance components of an image. The MultiScale Retinex (MSR) algorithm is an enhanced variant of the classical Retinex model, which estimates the illumination component at multiple spatial scales using Gaussian ﬁ ltering and subsequently derives the re ﬂ ectance by computing the logarithmic difference. This multi-scale approach enables the enhancement of image details across both low and high frequency regions, as formulated in Equation 7. Gamma correction is a nonlinear brightness adjustment technique that transforms image pixel values using a power law function to align with human visual sensitivity to brightness. When the gamma value g \<1, it enhances dark region details; when g \>1, it suppresses overexposed areas, as expressed in Equation 8.

R i x, y = log I i ( x, y ) − log ½ F i ( x, y )\* I i ( x, y  (7)

where I i denotes the original image, F i represents the Gaussian kernel at scale i, and \* denotes the convolution operation. I out = C · I g in (8)

where g is the gamma value, C is a constant, and I in and I out represent the input and output pixel values, respectively. Unlike conventional Retinex based methods that rely on generic assumptions of illumination distribution, ICNet incorporates physical ﬁ eld variables, including crop height difference and solar elevation angle, allowing for scene speci ﬁ c brightness adjustment. In this study, image data enhancement was performed using the aforementioned formulas by applying a compensation mapping to mitigate brightness variations and enhance overall image brightness. This algorithm is referred to as ICNet. To address the image quality issues arising from mutual shading between soybean and maize in intercropping systems, a novel algorithm for image brightness correction is proposed. The method adjusts brightness on a column by column basis to achieve uniform lighting across the image. Using a regression model, the target illumination intensity for each column of the image was calculated. Then, with a preset reference illumination intensity as a benchmark, the soybean rows (30, 60, 90, 120, 150, and 180 cm) were used as positional input coordinates. Illumination compensation was subsequently applied

FIGURE 2 Schematic of the developed shading capacity mode. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

from left to right along the soybean belt to enhance overall image brightness. For each column, the adjustment ratio is calculated based on the target and reference light intensity, gradually aligning the brightness with the predetermined standard. To prevent excessive enhancement or reduction, the adjustment ratio is constrained within a range of 0.5 to 1.2. This ratio is then applied to the pixel values of each column to adjust the overall brightness. Finally, the processed image is normalized to the standard display range, thereby enhancing the accuracy of the enhancing image information, as shown in Figure 3.

## 2.4 Evaluation metrics and comparative algorithms

2.4.1 PSNR An adaptive learning mechanism is introduced to dynamically adjust the strategy based on the characteristics of the input image. Both quantitative and qualitative evaluation methods were developed, with the Peak Signal-to-Noise Ratio (PSNR) used to assess the enhancement effect ( Wang et al., 2004 ), as shown in Equation 10. Higher PSNR values indicate lower image distortion, consequently, better quality. Generally, a PSNR greater than 30 dB is considered to signify high reconstruction quality. Equation 9 represents the formula for calculating the Mean Squared Error (MSE) ( Jobson et al., 1997 ).

## MSE = 1 mn o m − 1 $$ i=0 o $$ n − 1 $$ j=0 $$ ( I ( i, j ) − K ( i, j )) 2 (9)

Where MSE is Mean Square Error; I (i, j) and K (i, j) are the pixel values of the original and processed image respectively. m and n are the width and height of the image. PSNR = 10 log10ðMAX2

# MSE Þ (10)

Where MAX is the maximum pixel value of the image.

2.4.2 RGB and HLS change laws In the ﬁ eld of image processing and computer vision, image features are traditionally extracted from the RGB (Red, Green, Blue) channels ( Hu et al., 2021; Yan et al., 2022 ). However, in practical applications particularly in tasks such as object detection, image segmentation, and color correction the HLS (Hue, Lightness, Saturation) color model is often more aligned with human visual perception. This alignment makes color feature extraction more intuitive and effective, especially when interpreting color based scene information. In this study, the RGB and HLS channel pro ﬁ les were plotted for different soybean rows, arranged from left to right, corresponding to the direction of increasing light intensity across the image. Each channel was statistically analyzed along this orientation to assess how varying illumination conditions affect image representation. The variations in the RGB channels primarily re ﬂ ect contrast changes in the enhanced images, while changes in the HLS channels more accurately represent perceived color differences from a human visual standpoint. This dual channel analysis facilitates a more comprehensive understanding of how light intensity in ﬂ uences image features, thereby supporting more accurate and robust image detail recognition in subsequent processing stages.

## 3 Result and discussion

## 3.1 Illumination compensation parameterization

In the experiment, light intensity measurements were taken at each growth stage of soybean. Based on variation in light intensity, polynomial regression equations were constructed to systematically study examine the effects of height difference, solar elevation angle, and soybean location on the response variable light intensity, as

FIGURE 3 Column wise illumination enhancement based on ﬁ tted regression model. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

shown in Table 1. Initially, the height difference and solar elevation angle were employed as the primary independent variables, while six distinct soybean positions (30 cm, 60 cm, 90 cm, 120 cm, 150 cm, and 180 cm) were treated as supplementary independent variables, forming a comprehensive set of inputs. Based on this expanded set, linear regression was applied to model the light intensity y at each position, thereby generating corresponding regression equations. These equations, composed of regression coef ﬁ cients and an intercept term, can be used to predict light intensity at various positions under different combinations of height difference, solar elevation angle, and soybean location, thereby revealing the complex relationships between the independent and response variables. By applying the regression equation, predicted light intensities for different locations can be calculated, providing a theoretical foundation for experimental design, model validation, and result prediction. This approach offers robust scienti ﬁ c support for further quantifying and understanding the multivariable effects observed in the experiment. As shown in Figure 4, the x-axis represents the

soybean row numbers, arranged from south to north, while the y-axis denotes light intensity. Light intensity variations for ﬁ ve soybean growth stages the three-leaf stage, ﬂ owering stage, podding stage, seed ﬁ lling period, and maturity stage are plotted. To analyze light intensity variations across these stages, regression analysis was employed to ﬁ t the collected data. By selecting an appropriate regression model, the optimal functional form for light intensity changes over time was determined. The least squares method was used to optimize the model parameters, ensuring that the ﬁ tted curve accurately represents the light intensity variations along the soybean rows at each growth stage. This ﬁ tting result provides insights into the spatial distribution of light intensity, thereby facilitating an analysis of light exposure across the experimental ﬁ eld. The inputs to the polynomial regression equation are altitude difference, solar altitude angle, and position within the soybean row, denoted by h, q, and l, respectively, and the output is light intensity, denoted by y, the R² value of the ﬁ tting equation reached 91%. as shown in Equation 11. The Coef ﬁ cient values for each item are represented by a 0 - a 9, as shown in Table 2.

TABLE 1 Height difference and solar elevation angle of soybean and corn at different fertility periods.

Serial Test time Maize growth stage Soybean growth stage Altitude difference (cm) Solar altitude angle

| 6.20 | Three-leaf stage | Three-leaf stage | 33.8° |
| ---: |:--- |:--- |:--- |
| 7.15 | Seven-leaf stage | ﬂowering period | 30.4° |
| 7.30 | heading period | podding stage | 27.0° |
| 8.20 | tage of milky ripeness | seed ﬁlling period | 21.4° |
| 9.30 | maturity | maturity | 13.9° | 7.15 Seven-leaf stage ﬂ owering period 30.4° 7.30 heading period podding stage 27.0°

8.20 tage of milky ripeness seed ﬁ lling period 21.4° 9.30 maturity maturity 13.9°

FIGURE 4 The light intensity variation in the soybean strip at different growth stages. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

y ¼ a 0 + a 1 h  þ   a 2   q   þ a 3   l + a 4   h 2   þ   a 5   h   q   þ   a 6   q   l + a 7   q 2 þ   a 8   h   l + a 9   l 2 (11)

Combining the statistical equations with the compensation curves and adding the planting direction parameter resulted in the following equations, as shown in Equation 12. By substituting Equation 11 into Equation 6, and considering that the soybean-maize intercropping in this study is oriented in the north-south direction, a planting direction parameter is introduced into the equation to account for the light intensity variation caused by the planting orientation, resulting in Equation 12.

Ed = a 0 + a 1   h   + a 2   q + a 3   l + a 4   h 2 + a 5   h   q +

a 6   q l + a 7 q 2 + a 8   hl + a 9    l 2 + D f + a! E 0 cos( d ) (12)

The image compensation value is denoted as E d, the height difference in the equation is h, the solar altitude angle q, the position l, and d is the angle between the planting direction and the northsouth direction, which can be obtained from the equation for the height difference, the solar altitude angle, the light intensity, and the planting direction angle. The meanings of the letters in the equations are given in Table 3.

## 3.2 PSNR indicator results

In this study, images are processed using the Histogram Equalization method, (MSR), Gamma Correction, and ICNet, Processing of Figure 1b using different algorithms. Histogram Equalization redistributes pixel gray levels to achieve a more uniform gray level distribution, as shown in Figure 5a. MSR enhances image contrast and detail by estimating and removing the illumination component based on the re ﬂ ectance-illumination multiplicative model, as shown in Figure 5b. Gamma Correction applies a nonlinear transformation to the pixel values to optimize the brightness distribution, as shown in Figure 5c. Furthermore, illumination compensation is performed using a light intensity

curve variation equation to ensure uniform image brightness, as shown in Figure 5d. In intercropped images, it is assumed that humans extract structural information, leading to the introduction of an alternative complementary framework for quality assessment based on the degradation of such information ( Wang et al., 2004 ). The PSNR was calculated for images processed by several algorithms. A total of 50 images were randomly selected, with 10 images chosen from each growth stage, and processed using various algorithms. Compared to the original image, the PSNR values for the histogram equalization method, Multi-Scale Retinex, and Gamma function correction were all below 30 dB. However, after brightness compensation with ICNet, the PSNR reached 40.79 dB, indicating that the enhanced image quality is excellent, as shown in Table 4.

## 3.3 RGB variation with different algorithms

Accurate color recognition is critical for image based analysis; however, environmental light variability can signi ﬁ cantly compromise its accuracy. Therefore, selecting an appropriate radiometric correction method is essential when operating under varying lighting conditions ( Wang et al., 2024 ). In agricultural settings, changes in ambient illumination can directly affect the detection of vegetation indices, as image-based sensors depend heavily on color channel data to extract meaningful morphological and physiological features ( Cardenas-Gallegos et al., 2025 ). The podsetting stage of soybean coincides with the period when the height difference between maize and soybean plants reaches its maximum.

TABLE 2 Coef ﬁ cient values and de ﬁ nitions used in Equation 11 and Equation 12. Parameter Value Description a 0 Intercept term (constant)

| a1 | -61307 | Coefﬁcient for height difference h |
|:--- | ---: |:--- |
| a2 | -8220 | Coefﬁcient for solar elevation angle q |
| a3 | -515 | Coefﬁcient for soybean row position l | a 2 Coef ﬁ cient for solar elevation angle q a 3 Coef ﬁ cient for soybean row position l

| a4 | Coefﬁcient for h2 |
|:--- |:--- |
| a5 | Coefﬁcient for ℎ·q |
| a6 | Coefﬁcient for q·l | a 5 Coef ﬁ cient for ℎ · q a 6 Coef ﬁ cient for q ·l a 7 Coef ﬁ cient for q 2 a 8 Coef ﬁ cient for ℎ · l a 9 -0.334 Coef ﬁ cient for l 2

| TABLE 4 | PSNR values for different algorithms. |
|:--- |:--- |
| Pictures after processing | PSNR(dB) |
| histogram equalization method | 27.76 |
| Multi-Scale Retinex | 28.36 |
| Gamma function correction | 28.39 |
| ICNet | 40.79 |
| TABLE 3 | Parameter values and deﬁnitions in the equation. |
| Parameter value | Deﬁnition |
| Ed | The image compensation value |
| h | Height difference |
| q | The solar elevation angle |
| l | Position within the soybean row |
| Df | The scattered light coefﬁcient |
| a | Reﬂectance |
| E0 | The light intensity of the sun in direct sunlight | Pictures after processing PSNR(dB) histogram equalization method 27.76 Multi-Scale Retinex 28.36 Gamma function correction 28.39 ICNet 40.79

TABLE 3 Parameter values and de ﬁ nitions in the equation. Parameter value De ﬁ nition E d The image compensation value h Height difference q The solar elevation angle l Position within the soybean row D f The scattered light coef ﬁ cient a Re ﬂ ectance

E 0 The light intensity of the sun in direct sunlight

d The angle between the planting direction and the north-south direction Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

This stage is also associated with the greatest variation in light intensity over the soybean canopy due to differential shading. In order to assess the performance of various image processing algorithms, three representative images were randomly selected from each phenological stage for comparative analysis. This image was processed using multiple enhancement algorithms, and the RGB and HLS channel responses were examined. The analysis was conducted along the horizontal centerline of the image, with the left side representing the direction closer to the sun (south), and the right side being further away (north). As shown in Figure 6, the RGB channel intensities in the soybean strip image demonstrated an increasing trend from left to right (south to north), indicating a gradual rise in overall brightness. Among the three RGB channels, the green channel consistently exhibited higher intensity values compared to the red and blue channels. This dominance of the green component suggests that no signi ﬁ cant color shift occurred, and the increase in brightness was relatively uniform across the image. Although the overall trend in all channels was upward, local

ﬂ uctuations were observed within each channel, re ﬂ ecting spatial variation in re ﬂ ectance characteristics across the soybean strip. This implies that intercropping alters the phenotypic appearance of soybeans at different positions due to variable light distribution. On average, red and blue channel intensities ranged from 120 to 200, while the green channel ranged from 150 to 230, further emphasizing the dominant role of green spectral re ﬂ ectance. The observed left to right gradient in brightness primarily driven by the green channeldemonstrates the importance of addressing directional lighting effects during image analysis in intercropped systems. As shown in Figure 7, the variations in the HLS channels (Hue, Lightness, Saturation) of the soybean strip from south to north reveal that overall brightness exhibits an increasing trend, corresponding to the image transitioning from dark to bright. The hue shows a slight downward trend, corresponding to that the color remains consistent from left to right with no noticeable color shift. This minor change in hue may be attributed to subtle color adjustments in certain regions caused by certain in lighting

FIGURE 6 The RGB channel values of the soybean canopy image along the horizontal centerline change from left to right.

FIGURE 5 The processing results of the image using different algorithms. (a) histogram equalization method, (b) Multi-Scale Retinex, (c) Gamma function correction, (d) ICNet. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

conditions within the image. The saturation curve displays ﬂ uctuations in color purity, exhibiting a slight upward trend overall. This increase in saturation is likely due to the enhanced brightness, which makes the colors appear more saturated and vivid. The observed ﬂ uctuations indicate localized variations in color intensity across the soybean strip. This study compares the trends in RGB and HLS channel variations from left to right in images processed using four different brightness enhancement methods: histogram equalization, MSR, Gamma function correction, and the ICNet algorithm. As shown in Figure 8a, the RGB channel values exhibit a consistent decreasing trend, with the overall range reduced to 70190. Additionally, the ﬂ uctuations in values increase, thereby enhancing the image contrast. However, despite the improved contrast, excessive local contrast in certain areas results in detail blurring or loss. Moreover, pronounced color shifts were observed, characterized by an overall purple hue that led to localized saturation and subsequent color distortion. As shown in Figure 8b, the ﬂ uctuations in RGB channel values signi ﬁ cantly decrease, with the variation range reducing from 80 to 50, and all maximum values remaining below 200. This indicates a notable reduction in image brightness, leading to color homogenization across the image. As illustrated in Figure 8c, gamma correction effectively maintains overall image brightness. The RGB channel values exhibit a general decline, with a maximum G-channel value of 220 and maximum R and B-channel values of 180. However, the variation trends remain consistent with those of the original image, suggesting that the overall brightness decreases without altering the color relationships or contrast dynamics. A limitation of gamma correction is its linear brightness adjustment, which may be ineffective in enhancing details in darker regions under complex

lighting conditions. In contrast, Figure 8d demonstrates that the ICNet algorithm leads to a substantial increase in RGB channel values, with all values exceeding 150, indicating a signi ﬁ cant overall brightness enhancement. Additionally, the reduced RGB value ﬂ uctuations result in more uniform color and brightness distribution, leading to smoother color transitions and reduced differences between bright and dark areas. Compared with other image enhancement methods, the ICNet algorithm effectively increases the overall brightness while simultaneously reducing RGB ﬂ uctuations, thereby producing smoother color transitions and more visually balanced images. This study evaluates the performance of four image brightness enhancement techniques Histogram Equalization, Multi-Scale Retinex (MSR), Gamma Correction, and the ICNet algorithm within the HLS color space. As shown in Figure 9a, histogram equalization results in signi ﬁ cant lightness ﬂ uctuations, with a maximum value reaching 190, indicating considerable variations in brightness across different regions of the image. While the overall lightness trend shows a slight increase, excessive contrast enhancement in some areas leads to an uneven brightness distribution. The mean saturation remains relatively stable, but the noticeable oscillations imply poor color stability, negatively affecting overall color balance. Additionally, hue values ﬂ uctuate between 70 and 140, suggesting that histogram equalization may introduce color distortions, especially during high contrast enhancement. As illustrated in Figure 9b, the MSR method provides effective brightness enhancement, with lightness values exceeding 150 and displaying a relatively stable upward trend, improving detail visibility in darker regions. However, saturation drops markedly compared to the original image, with values remaining below 50, indicating a transition toward grayscale that

FIGURE 7 The HLS channel values of the soybean canopy image along the horizontal centerline change from left to right. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

## may reduce image vibrancy and contrast between bright and dark

regions. Furthermore, the overall increase in hue values (all above 75. re ﬂ ects a degree of color shift caused by hue modi ﬁ cation. In Figure 9c, gamma correction demonstrates relatively stable

## brightness enhancement, although the maximum lightness value

decreases from 200 to 180, indicating an overall reduction in image brightness. Brightness ﬂ uctuations, however, increase from 100 to 120, suggesting a greater contrast between bright and dark areas,

FIGURE 9 The HLS channel values along the horizontal centerline of the soybean canopy image change from left to right after processing with different algorithms: (a) Histogram Equalization Algorithm, (b) Multi-Scale Retinex Algorithm, (c) Gamma Function Correction Algorithm, (d) ICNet Algorithm.

FIGURE 8 The RGB channel values along the horizontal centerline of the soybean canopy image change from left to right after processing with different algorithms: (a) Histogram Equalization Algorithm, (b) Multi-Scale Retinex Algorithm, (c) Gamma Function Correction Algorithm, (d) ICNet Algorithm. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

which may result in detail loss in some regions. Meanwhile, saturation increases from 130 to 140, and its ﬂ uctuation narrows from 80 to 60, implying that the image colors become more vivid, though with reduced tonal diversity, potentially affecting perceived contrast. The hue values and their ﬂ uctuations remain largely consistent with the original image, indicating no signi ﬁ cant alteration in overall color composition. As depicted in Figure 9d, the ICNet algorithm exhibits the smallest brightness ﬂ uctuations among the four methods, demonstrating superior stability under complex lighting conditions while preserving image details. Notably, the brightness in the left portion of the image increases from 125 to 175, signifying a substantial enhancement. Saturation surpasses 150, re ﬂ ecting improved color intensity without sacri ﬁ cing contrast perception. Additionally, hue values and ﬂ uctuations remain unchanged compared to the original image, con ﬁ rming the preservation of the original color composition. The uniform brightness distribution and enhanced color vividness, particularly in shadowed regions, highlight the ICNet algorithm ' s superior performance in maintaining image quality and visual consistency.

## 3.4 Standard deviation variation

Standard deviation is a commonly used statistic to describe the distribution characteristics of data. In image processing and analysis, it re ﬂ ects the image ' s brightness, color variations, and noise characteristics. A larger standard deviation indicates stronger texture, edges, or noise. Ten images were randomly selected from each growth stage, for a total of 50 images, and processed using various algorithms. Based on the previous ﬁ ndings in the RGB and HLS channels, it was observed that the leftmost 1/10 and the

rightmost 1/10 of the image correspond to the dividing line between soybean and corn, where signi ﬁ cant changes in the RGB and HLS channels occur. In subsequent calculations of standard deviation and peak-to-peak values, these two sections are excluded from the analysis. As shown in Figure 10, the ICNet algorithm demonstrates superior performance compared to traditional methods. While histogram equalization introduces a slight decrease in the H channel, ICNet effectively enhancing image details by increasing the standard deviation without signi ﬁ cantly amplifying noise or artifacts. During detail enhancement, ICNet achieves a smooth increase in standard deviation, mitigating the risk of unnatural sharpening effects. Compared to multi-scale processing, ICNet exhibits a smaller deviation in the H channel, striking a better balance between local detail enhancement and overall image consistency. Additionally, ICNet reduces the common noise ampli ﬁ cation issues seen in MSR processing, ensuring more stable standard deviation performance. Furthermore, in contrast to gamma correction, ICNet signi ﬁ cantly improves the S channel ' s stability while maintaining consistent values in other channels. This re ﬁ ned brightness optimization enhances contrast and preserves image details more effectively, avoiding the excessive darkening or lightening that often occurs with gamma correction. Compared to traditional methods, the ICNet algorithm demonstrated lower standard deviation values across key channels. Speci ﬁ cally, in the green (G) channel, the standard deviation decreased from 18.5 (MSR) to 12.1 with ICNet, representing a 34.6% reduction. Similarly, the hue (H) channel ' s variation decreased by 27.3%, indicating improved chromatic consistency. These quantitative results, illustrated in Figure 10, substantiate the enhanced brightness uniformity and reduced noise ﬂ uctuations achieved by the proposed method, supporting its effectiveness under uneven illumination conditions.

FIGURE 10 Variation in the standard deviation of the RGB and HLS channel values of the soybean canopy image after processing with different algorithms. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

## 3.5 Comparative analysis and method evaluation

To comprehensively evaluate the performance of the proposed ICNet algorithm, a comparative analysis was conducted against three conventional image enhancement methods: histogram equalization, multi-scale Retinex (MSR), and gamma correction. The comparison was based on multiple metrics, including PSNR, RGB and HLS channel pro ﬁ les, and standard deviation distribution. Among the four methods, ICNet achieved the highest PSNR value (40.79 dB), signi ﬁ cantly outperforming the other three methods, which remained below 30 dB. As shown in Figures 8 and 9, ICNet enhanced image brightness uniformly across the soybean canopy, with RGB channel values consistently above 150 and reduced channel ﬂ uctuations, indicating smoother transitions and improved visual consistency. In contrast, histogram equalization exhibited strong contrast enhancement but resulted in local overexposure and color distortion. MSR effectively enhanced shadow regions but introduced visible hue shifts and reduced color saturation. Gamma correction preserved natural color relationships but showed limited enhancement in underexposed areas and was less effective in handling brightness imbalance. The primary advantage of ICNet lies in its ability to perform spatially adaptive brightness correction by leveraging crop height difference, solar elevation angle, and planting orientation. This physics informed compensation strategy enables uniform lighting enhancement, particularly in images affected by crop shading. Additionally, ICNet maintains low standard deviation in green (G) and hue (H) channels, which re ﬂ ects better image stability and noise control. However, the proposed method also has limitations. ICNet is based on polynomial regression models ﬁ tted from ﬁ eld-acquired data. This dependence on manually measured canopy parameters and solar angles limits its scalability and adaptability to other cropping systems or image acquisition conditions. Furthermore, as a rule based method, ICNet lacks the capacity to autonomously learn from new data, making it less ﬂ exible than deep learning based approaches in highly dynamic or heterogeneous environments. Future improvements may focus on integrating ICNet with data driven models, such as convolutional neural networks (CNNs), or replacing static regression equations with adaptive learning modules, to enhance generalizability and robustness in broader agricultural applications. Although manual measurements were used in this study, future implementations can leverage UAV photogrammetry or LiDAR to automate plant height and shading parameter acquisition. Preliminary deployment tests showed that ICNet inference time was under 0.15 s per image on a standard GPU, indicating its feasibility for real time ﬁ eld applications.

## 4 Conclusion

This study developed an illumination compensation algorithm (ICNet) tailored for image enhancement in maize - soybean intercropping systems. By modeling the relationship between crop height difference, solar elevation angle, and canopy light intensity, a polynomial regression-based compensation framework was established and applied to correct uneven lighting across soybean

canopy images. Experimental results demonstrated that ICNet achieved a PSNR of 40.79 dB, signi ﬁ cantly outperforming traditional methods such as histogram equalization (27.76 dB), multi-scale Retinex (28.36 dB), and gamma correction (28.39 dB). Additionally, RGB and HLS channel analysis showed that ICNet effectively increased brightness uniformity while reducing channel ﬂ uctuations green channel values exceeded 150, and brightness in shadowed regions improved from 125 to 175. Standard deviation analysis con ﬁ rmed enhanced image consistency, with up to 35% reduction in variation across key color channels. Compared to conventional techniques, ICNet not only improves visual clarity but also preserves color ﬁ delity and suppresses noise, providing a more robust foundation for accurate image based crop trait extraction in precision agriculture. These ﬁ ndings validate the method ' s practical value for improving the reliability of visual analysis under complex intercropping light conditions. Future work will focus on enhancing the generalizability of the model through adaptive or learning based modules to accommodate diverse crop architectures and lighting environments. The proposed ICNet algorithm outperformed traditional methods in PSNR and HLS stability, but its performance under extreme overcast or strong shadow conditions requires further validation.

## Data availability statement

The original contributions presented in the study are included in the article/supplementary material. Further inquiries can be directed to the corresponding author.

## Author contributions

WZ: Data curation, Formal analysis, Investigation, Methodology, Writing - original draft, Writing - review & editing. WY: Data curation, Investigation, Writing - review & editing. YW: Conceptualization, Investigation, Project administration, Supervision, Writing - review & editing. XD: Project administration, Supervision, Writing - review & editing. XW: Conceptualization, Funding acquisition, Investigation, Project administration, Supervision, Writing - review & editing. WJ: Project administration, Supervision, Writing - review & editing. MO: Conceptualization, Investigation, Project administration, Supervision, Writing - review & editing. MY: Conceptualization, Investigation, Project administration, Supervision, Writing - review & editing.

## Funding

The author(s) declare that ﬁ nancial support was received for the research and/or publication of this article. This work was funded by the National Key Research and Development Plan of China (grant number: 2023YFD2000503) and the Priority Academic Program Development of Jiangsu Higher Education Institutions (grant number: PAPD-2023-87).

## Acknowledgments

The author thanks Faculty of Agricultural Equipment of Jiangsu University for its facilities and support. Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

# Con ﬂ ict of interest

## Author MY was employed by Chinese Academy of Agriculture

Mechanization Sciences Group Co., Ltd. The remaining authors declare that the research was conducted in the absence of any commercial or ﬁ nancial relationships that could be construed as a potential con ﬂ ict of interest.

# Generative AI statement

## The author(s) declare that no Generative AI was used in the

creation of this manuscript. Any alternative text (alt text) provided alongside ﬁ gures in this article has been generated by Frontiers with the support of arti ﬁ cial

## intelligence and reasonable efforts have been made to ensure

accuracy, including review by the authors wherever possible. If you identify any issues, please contact us.

# Publisher ' s note

## All claims expressed in this article are solely those of the authors

and do not necessarily represent those of their af ﬁ liated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

# References

Andersen, M. K. (2025). Competition and complementarity in annual intercrops-the role of plant available nutrients (Frederiksberg, Copenhagen: Samfundslitteraur Gra ﬁ k).

Bybee-Finley, K. A., and Ryan, M. R. (2018). Advancing intercropping research and practices in industrialized agricultural landscapes. Agriculture 8, 80. doi: 10.3390/ agriculture8060080

Cardenas-Gallegos, J. S., Severns, P. M., Klimes ̌, P., Lacerda, L. N., Peduzzi, A., Ferrarezi, R. S., et al. (2025). Reliable plant segmentation under variable greenhouse illumination conditions. Comput. Electron. Agric. 229, 109711. doi: 10.1016/ j.compag.2024.109711

Coltuc, D., Bolon, P., and Chassery, J. M. (2006). Exact histogram speci ﬁ cation. IEEE Trans. Image. Process. 15, 1143 - 1152. doi: 10.1109/TIP.2005.864170

Dai, S. K., Zhong, Z., and Huang, Z. W. (2019). Maximum entropy model based bihistogram equalization algorithm. Acta Electron. Sin. 47, 678 - 685. doi: 10.3969/j. issn. 0372-2112. 2019. 03. 023

Deng, F., Li, Q., Chen, H., Zeng, Y., Li, B., Zhong, X., et al. (2021). Relationship between chalkiness and the structural and thermal properties of rice starch after shading during grain- ﬁ lling stage. Carbohydr. Polymers. 252, 117212. doi: 10.1016/ j.carbpol.2020.117212

Du, Y. L., Zhou, T., Yang, H., Liu, T., Guan, S. C., Deng, Y. C., et al. (2018). Dynamic simulation of the dry weight of soybean stems in intercropping systems. Pratacult. Sci. 35, 624 - 634. doi: 10.11829/j. issn. 1001-0629. 2017-0310

Fan, Y. F., Chen, J. X., Cheng, Y. J., Raza, M. A., Wu, X. L., Wang, Z. L., et al. (2018). Effect of shading and light recovery on the growth, leaf structure, and photosynthetic performance of soybean in a maize-soybean relay-strip intercropping system. PloS One 13, e0198159. doi: 10.1371/journal.pone.0198159

Feng, G., Wang, C., Wang, A., Gao, Y., Zhou, Y., Huang, S., et al. (2024). Segmentation of wheat lodging areas from UAV imagery using an ultra-lightweight network. Agriculture 14, 244. doi: 10.3390/agriculture14020244

Franklin, K. A. (2008). Shade avoidance. New Phytol. 179, 930 - 944. doi: 10.1111/ j.1469-8137.2008.02507.x

Guo, X., Li, Y., and Ling, H. (2016). LIME: Low-light image enhancement via illumination map estimation. IEEE Trans. Image. Process. 26, 982 - 993. doi: 10.1109/ TIP.2016.2639450

Hu, M., Wang, S., Li, B., Ning, S., Fan, L., Gong, X., et al. (2021). " Penet: Towards precise and ef ﬁ cient image guided depth completion, " in 2021 IEEE International Conference on Robotics and Automation (ICRA) Xi'an, China. 13656 - 13662. doi: 10.1109/ICRA48506.2021.9561035

| Huang, S. C., Cheng, F. C., and Chiu, Y. S. (2012). Efﬁcient contrast enhancement | using adaptive gamma correction with weighting distribution. IEEE Trans. Image. | Process. 22, 1032-1041. doi: 10.1109/TIP.2012.2226047 |
|:--- |:--- |:--- |
| Hussain, S., Iqbal, N., Rahman, T., Liu, T., Brestic, M., Safdar, M. E., et al. (2019). | Shade effect on carbohydrates dynamics and stem strength of soybean genotypes. | Environ. Exp. Bot. 162, 374-382. doi: 10.1016/j.envexpbot.2019.03.011 |
| Jobson, D. J., Rahman, Z., and Woodell, G. A. (1997). A multiscale retinex for | bridging the gap between color images and the human observation of scenes. IEEE | Trans. Image. Process. 6, 965-976. doi: 10.1109/TIP.83 |

Hussain, S., Iqbal, N., Rahman, T., Liu, T., Brestic, M., Safdar, M. E., et al. (2019). Shade effect on carbohydrates dynamics and stem strength of soybean genotypes. Environ. Exp. Bot. 162, 374 - 382. doi: 10.1016/j.envexpbot.2019.03.011

Jobson, D. J., Rahman, Z., and Woodell, G. A. (1997). A multiscale retinex for bridging the gap between color images and the human observation of scenes. IEEE Trans. Image. Process. 6, 965 - 976. doi: 10.1109/TIP.83

Kass, D. (1978). Polyculture cropping systems: review and analysis. Cornell. Int. Agric. Bull. (USA) 32. doi: 10.5555/19820740412

Lee, C. H., Shih, J. L., Lien, C. C., and Han, C. C (2013b). Contrast enhancement based on layered difference representation of 2D histograms. IEEE Trans. Image. Process. 22, 5372 - 5384. doi: 10.1109/TIP.2013.2284059

Lee, C. H., Shih, J. L., Lien, C. C., et al. (2013a). " Adaptive multiscale retinex for image contrast enhancement, " in 2013 International Conference on Signal-Image Technology & Internet-Based Systems (IEEE), 43 - 50. doi: 10.1109/ SITIS.2013.19"10.1109/SITIS.2013.19

Li, M., Hu, P., He, D., Zheng, B., Guo, Y., Wu, Y., et al. (2023). Quanti ﬁ cation of the cumulative shading capacity in a maize - soybean intercropping system using an unmanned aerial vehicle. Plant Phenomics. 5, 0095. doi: 10.34133/plantphenomics.0095

Li, M., Liu, J., Yang, W., Sun, X., and Guo, Z. (2018). Structure-revealing low-light image enhancement via robust retinex model. IEEE Trans. Image. Process. 27, 2828 - 2841. doi: 10.1109/TIP.2018.2810539

Li, J., Luo, W., Han, L., Cai, Z. L., and Guo, Z. M. (2022). Two-wavelength image detection of early decayed oranges by coupling spectral classi ﬁ cation with image processing. J. Food Composition. Anal. 111, 104642. doi: 10.1016/j.jfca.2022.104642

MacLaren, C., Waswa, W., Aliyu, K. T., Claessens, L., Mead, A., Schöb, C., et al. (2023). Predicting intercrop competition, facilitation, and productivity from simple functional traits. Field Crops Res. 297, 108926. doi: 10.1016/ j.fcr.2023.108926

| Petrella, D. P., Breuillin-Sessoms, F., and Watkins, E. (2022). Layering contrasting | photoselective ﬁlters improves the simulation of foliar shade. Plant Methods 18, 16. | doi: 10.1186/s13007-022-00844-8 |
|:--- |:--- |:--- |
| Raza, M. A., Feng, L. Y., Iqbal, N., Ahmed, M., Chen, Y. K., Khalid, M. H. B., et al. | (2019). Growth and development of soybean under changing light environments in | relay intercropping system. PeerJ 7, e7262. doi: 10.7717/peerj.7262 |
| Ren, J., Zhang, L., Duan, Y., Zhang, J., Evers, J. B., Zhang, Y., et al. (2019). Intercropping | potato (Solanum tuberosum L.) with hairy vetch (Vicia villosa) increases water use efﬁciency | in dry conditions. Field Crops Res. 240, 168-176. doi: 10.1016/j.fcr.2018.12.002 |
| Routray, S., Ray, A. K., and Mishra, C. (2019). An efﬁcient image denoising method | based on principal component analysis with learned patch groups. Signal. Image. Video. | Process. 13, 1405-1412. doi: 10.1007/s11760-019-01489-2 |
| Saraçoğlu, N., and Gündüz, G. (2009). Wood pellets-tomorrow's fuel for Europe.\[J\]. | Energy sources part A: recovery, utilization & environmental effects 31(19):1708-1718. | doi: 10.1080/15567030802459677 |

Raza, M. A., Feng, L. Y., Iqbal, N., Ahmed, M., Chen, Y. K., Khalid, M. H. B., et al. (2019). Growth and development of soybean under changing light environments in relay intercropping system. PeerJ 7, e7262. doi: 10.7717/peerj.7262

Ren, J., Zhang, L., Duan, Y., Zhang, J., Evers, J. B., Zhang, Y., et al. (2019). Intercropping potato (Solanum tuberosum L.) with hairy vetch (Vicia villosa) increases water use ef ﬁ ciency in dry conditions. Field Crops Res. 240, 168 - 176. doi: 10.1016/j.fcr.2018.12.002

Routray, S., Ray, A. K., and Mishra, C. (2019). An ef ﬁ cient image denoising method based on principal component analysis with learned patch groups. Signal. Image. Video. Process. 13, 1405 - 1412. doi: 10.1007/s11760-019-01489-2

Sarac ̧ og ̆ lu, N., and Gündüz, G. (2009). Wood pellets - tomorrow's fuel for Europe.\[J\]. Energy sources part A: recovery, utilization & environmental effects 31(19):1708 - 1718. doi: 10.1080/15567030802459677

Sun, J., He, X., Ge, X., Wu, X., Shen, J., Song, Y., et al. (2018). Detection of key organs in tomato based on deep migration learning in a complex background. Agriculture 8, 196. doi: 10.3390/agriculture8120196

Sun, J., Zhang, L., Zhou, X., Yao, K., Tian, Y., Nirere, A., et al. (2021). A method of information fusion for identi ﬁ cation of rice seed varieties based on hyperspectral imaging technology. J. Food Proc. Eng. 44, e13797. doi: 10.1111/jfpe.13797

Wang, Z., Bovik, A. C., Sheikh, H. R., and Simoncelli, E. P. (2004). Image quality assessment: from error visibility to structural similarity. IEEE Trans. Image. Process. 13, 600 - 612. doi: 10.1109/TIP.2003.819861

Wang, J., Gao, Z., Zhang, Y., Zhou, J., Wu, J., Li, P., et al. (2021a). Real-time detection and location of potted ﬂ owers based on a ZED camera and a YOLO V4-tiny deep learning algorithm. Horticulturae 8, 21. doi: 10.3390/horticulturae8010021

Wang, A., Li, W., Men, X., Gao, B., Xu, Y., Wei, X., et al (2021b). Effects of shading stress during the reproductive stages on photosynthetic physiology and yield Zhong et al. 10.3389/fpls.2025.1639016 Frontiers in Plant Science frontiersin.org

characteristics of peanut (Arachis hypogaea Linn.). J. Integr. Agric. 20, 1250 - 1265. doi: 10.1016/S2095-3119(20)63442-6

Wang, Y., Kootstra, G., Yang, Z., and Khan, H. A. (2024). UAV multispectral remote sensing for agriculture: A comparative study of radiometric correction methods under varying illumination conditions. Biosyst. Eng. 248, 240 - 254. doi: 10.1016/ j.biosystemseng.2024.11.005

| Wang, A., Li, W., Men, X., et al. (2022). Vegetation detection based on spectral | information and development of a low-cost vegetation sensor for selective spraying. | Pest Manage. Sci. 78, 2467-2476. doi: 10.1002/ps.6874 |
|:--- |:--- |:--- |
| Xu, S., Xu, X., Zhu, Q., Meng, Y., Yang, G., Feng, H., et al. (2023). Monitoring leaf | nitrogen content in rice based on information fusion of multi-sensor imagery from | UAV\[J. Precis. Agric. 24, 2327-2349. doi: 10.1007/s11119-023-10042-8 |
| Yan, P. P., Ma, C. W., and She, W. J. (2015). Inﬂuence of earth's reﬂective radiation | on space target for space based imaging. ACTA PHYSICA SINICA, 64(16). | doi: 10.7498/aps.64.169501 |
| Yan, Z., Wang, K., Li, X., Zhang, Z., Li, J., Yang, J., et al. (2022). "RigNet: Repetitive | image guided network for depth completion," in European Conference on Computer | Vision (Springer Nature Switzerland, Cham), 214-230. |
| Zhu, J., Cai, J., Sun, B., Xu, Y., Lu, F., Ma, H., et al. (2023). Inspection and | classiﬁcation of wheat quality using image processing. Qual. Assur. Saf. Crops Foods. | 15, 43-54. doi: 10.15586/qas.v15i3.1220 |
| Zhu, J., van der Werf, W., Anten, N. P. R., Vos, J., and Evers, J. B. (2015). The | contribution of phenotypic plasticity to complementary light capture in plant mixtures. | New Phytol. 207, 1213-1222. doi: 10.1111/nph.13416 |

Xu, S., Xu, X., Zhu, Q., Meng, Y., Yang, G., Feng, H., et al. (2023). Monitoring leaf nitrogen content in rice based on information fusion of multi-sensor imagery from UAV\[J. Precis. Agric. 24, 2327 - 2349. doi: 10.1007/s11119-023-10042-8

Yan, P. P., Ma, C. W., and She, W. J. (2015). In ﬂ uence of earth ' s re ﬂ ective radiation on space target for space based imaging. ACTA PHYSICA SINICA, 64(16). doi: 10.7498/aps.64.169501

Yan, Z., Wang, K., Li, X., Zhang, Z., Li, J., Yang, J., et al. (2022). " RigNet: Repetitive image guided network for depth completion, " in European Conference on Computer Vision (Springer Nature Switzerland, Cham), 214 - 230.

Zhu, J., Cai, J., Sun, B., Xu, Y., Lu, F., Ma, H., et al. (2023). Inspection and classi ﬁ cation of wheat quality using image processing. Qual. Assur. Saf. Crops Foods. 15, 43 - 54. doi: 10.15586/qas.v15i3.1220

Zhu, J., van der Werf, W., Anten, N. P. R., Vos, J., and Evers, J. B. (2015). The contribution of phenotypic plasticity to complementary light capture in plant mixtures. New Phytol. 207, 1213 - 1222. doi: 10.1111/nph.13416 Zhong et al. 10.3389/fpls.2025.1639016

Frontiers in Plant Science frontiersin.org