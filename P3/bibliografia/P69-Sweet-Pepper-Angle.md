## Fruit detectability analysis for

**different camera positions in sweet-pepper **

Jochen Hemming 1 \*, Jos Ruizendaal 2, Jan Willem Hofstee 2, Eldert J. van Henten 1,2

*1* *Wageningen UR Greenhouse Horticulture, P.O. Box 644, Wageningen, The Netherlands * *2* *Farm Technology Group, Wageningen University, Wageningen, The Netherlands  * *\*Corresponding author. E-mail: * jochen.hemming@wur.nl **Abstract **

For robotic harvesting of sweet-pepper fruits in greenhouses a sensor system is required to detect and to localize the fruits on the plants. Due to the complex structure of the plant, most fruits are (partly) occluded when an image is taken from one viewpoint only. In this research the effect of multiple camera positions and viewing angles on fruit visibility and detectability was investigated. A measurement setup was built which allowed to place the camera under different azimuth and zenith angles and to move the camera horizontally along the crop row. Fourteen camera positions were chosen and the fruit visibility in the recorded images was manually determined for each position. For images taken from one position only with the criterion of maximum 50% occlusion per fruit, the fruit detectability (FD) was in no case higher than 66%. The best single positions were the front view and looking with a zenith/elevation angle of 60° upwards. The FD increases when a combination was made of multiple viewpoint positions. With a combination of five positions the maximum FD was 86%.

**Key words**: fruit visibility, sweet-pepper, occlusion, harvesting, robotics **1. Introduction  **

In the framework of the European FP7 project Clever Robots for Crops - CROPS (<https://www.crops-robots.eu)> several highly configurable and modular demonstrators are currently under development for robotic harvesting of high value greenhouse vegetables and fruits in orchards. One of the key issues in automated fruit harvesting is the detection of the fruits on the plant by means of a sensor system. The desired situation is to detect close to 100% of all ripe fruits on the plant. For robotic harvesting of sweet-pepper fruits in greenhouses a computer vision system, based on camera images taken from a device placed in between the plant rows, is a possible approach. However, in many cases fruits are not completely visible because leaves or branches hang in front or more fruits are growing in a cluster. The occlusion minimizes the visible part of the fruits. Publications from e.g. Jiménez *et al.* (1999) or Plebe and Grasso (2000) confirm that the main problem in automated fruit harvesting is the visibility of the fruits in the crop. In other studies multiple camera viewpoints were used to acquire images of the crop. In the research of Van Henten *et al.* (2002), images of cucumber plants were taken with a linear displacement of 0.33 m. Thereby every plant was visible in three subsequent images. The plant shifted in the images and was seen from a different angle in every picture. With three different pictures of one plant, on some pictures the fruits were occluded while on another picture of the same plant, the fruit was totally visible. In this way more than 95% of the cucumbers were detected correctly. Tanigaki *et al.* (2008) did a research on a cherry harvesting robot and investigated different positions around the crop to increase visibility. Images were taken from four different positions around the trunk of the plant. They stated that 59% of the fruits were visible when all images were used. Bulanon *et * *al.* (2009) investigated multiple positions around a citrus tree to determine the positions that were needed to get the highest fruit visibility. A combination of up to 6 views resulted in a significant higher visibility.

In this research, the effect of multiple camera positions and viewing angles on fruit detectability in a sweet-pepper greenhouse crop was investigated. The objective was to

determine the optimal camera position or combination of positions which yields the maximum visibility of the sweet-pepper fruits on the plant for the purpose of robotized harvesting. **2. Materials and Methods ** 2.1 Terms and definitions

*Azimuth angle*: a celestial coordinate system is used that sets the camera's local horizon as the fundamental plane. The azimuth is the angle of the object around the horizon. As illustrated in Fig. 2 an azimuth of 90% defines to a camera position straight in front of the crop row.

*Zenit angle*: The zenith is a vector pointing up from a point of interest, perpendicular to the fundamental plane. In this case, the zenith is pointing up from the middle of the camera. As illustrated in Fig. 2 the zenith angle is defined as the angle between the vector from the camera to the crop row and the zenith vector.

*Fruit visibility (FV): * The visible part of a fruit in an image expressed as a percentage of total fruit area which would be seen in an image without occlusion. Ranging from 0% visibility (not visible at all) to 100% visibility (completely visible).

*Fruit detectability (FD)*: The relative number of fruits (%) on a plant that is visible for at least a certain FV percentage. Example: with a FV threshold set to 40%, a fruit which is occluded for not more than 60% in an image will be counted as detected. In case of using several viewpoint combinations, a fruit is counted as detected if its FV was above the set threshold in at least one of the images. ** ** 2.2 Crop

Images were taken of greenhouse crops of yellow and red cultivars of sweet pepper ( *Capsicum annum* ) at two different commercial growers in the Netherlands. Besides the difference in colour, the crops also differed in density. The red species had more leaves and the plants were more hanging towards the middle of the row than the yellow cultivar. Table 1 gives an overview of the crop characteristics. The free space between the rows was limited by the plants which were hanging towards the middle of the row. This gave a free space of about 50 cm from sensor to plant canopy on average.

TABLE 1: Crop characteristics during the measurements

**Session ** **Measurement date ** **Cultivar ** **Fruit colour ** **Crop height ** 17-5-2011 Helsinki Yellow 1.5 m 24-6-2011 Nagano Red 2.4 m 7-9-2011 Nagano Red 2.75 m ** ** 2.3 Recording device

A measurement frame was built which allowed placing the camera under different azimuth and zenith angles. The frame was placed on a crop handling cart so it could easily be moved along the crop row (Fig.1). The height of the platform was changed for every plant to have the lowest coloured fruit in the middle of the image.

A 1/1.8 inch CCD Stingray F201C colour camera (Allied Vision Technology, Germany) was used for the recording. On top of the camera, a PerkinElmer MVS 5002 flash light (PerkinElmer, The Netherlands) was mounted to ensure constant illumination conditions.

FIGURE 1: Photo of the camera setup in the crop row, with azimuth=90º and zenith=90º 2.4 Positioning of the camera

The camera was placed on several positions and orientations which were changed in three different ways: The azimuth angle, zenith angle and the horizontal position with respect to the crop row. In total ten plants were recorded during every measurement from 14 different viewpoints. The camera was positioned on a metal arc with a diameter of 1.00 m and the device was positioned such that the recorded plant was located in the center of the arc. As shown in Fig. 2 the camera was placed in five different azimuth angles, namely 30°, 60°, 90°, 120° and 150° with respect to the crop row. The zenith angle was set to angles of 60°, 90° and 120°.

FIGURE 2: Azimuth angles (left figure) and zenith angles (right figure) for the camera ** **

Fig. 3 shows the numbers used for labelling the different camera positions and orientations. The zenith angles were numbered from 1 - 9 and the azimuth angles were numbered from 10 - 14. Label 5 and 12 account for the same positions but were numbered separately due to the experimental setup. ** **

FIGURE 3: Label numbers for the different positions from which images were taken. The square represents the crop canopy (left). Label numbers for the different azimuth (right) 2.5 Image evaluation

For every experiment, ground truth data was collected in the greenhouse to be able to evaluate the results for the fruits visible in the recorded images. The number and positions of individual fruits on the plants were registered. Images that were acquired were examined manually offline and the visibility of every fruit (FV) was estimated from the images. To assess the detectability of the fruits the FD was calculated. During the detectability assessment, thresholds in the range of 5% to 100% minimum FV were used. In addition to this, all unique viewpoint combinations were computed and the FD for each combination was calculated. For 14 different positions, 16 383 possible unique combinations are possible if the number of used positions used ranges from 1 up to 14. ** ** **3. Results ** 3.1 Azimuth angles

Fig. 4 shows example images taken of the same plant from different azimuth angles. Whereas at position 11 no red coloured fruit is visible at all position 13 shows 2 coloured fruits and position 14 shows one of the coloured fruits even with a low percentage of occlusion. ** **

** ** ** ** ** ** ** ** *               Position 11               Position 12                 Position 13               Position 14 * FIGURE 4: Example images from the same plant taken from different camera viewpoints

Applying a FV threshold of 50%, the FD ranged from 44% to 66% in the yellow cultivar (1st session), from 20% to 31% for the 2nd session and from 29% to 51% for the 3rd session (red sweet-pepper). Fig. 5 shows the detailed results.

FIGURE 5: FD for different azimuth angles, for the yellow sweet-pepper (1st session, left figure) and the for the red sweet-pepper (3rd session, right figure)

The middle positions (60°, 90° and 120°) show a higher FD than the other two positions. However, this does not mean positions 10 and 14 were not useful. These positions can give valuable information about the location of fruits which were not visible in positions 11, 12 or 13. 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8

# FD **Position number** 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8

# FD **Position number** 3.2 Zenith angles

The measurements for the different zenith angles were only performed for the red sweetpepper during the 2nd and 3rd measurement session. Also here, to calculate the FD the threshold for a sweet pepper to be counted as visible was set to 50% visibility. Positions 1, 2 and 3 show the lowest FD, with a minimum value of 3.5% for position 3. Position 3 shows a notable lower FD on the first measurement. In Fig. 6 these results are presented.

In the positions 1, 2 and 3 the images were taken with a zenith angle of 60°. With this angle the leaves were about perpendicular to the camera which resulted in covered fruits by leaves on the images. The covering of the fruits by the leaves from this position is probably a natural protection of the fruits by the crop for direct sunlight. The positions 4 to 9 all have a FD between 31% and 41% for the 2nd session and between 34% and 52% for the 3rd session. In these positions, images were taken with a zenith angle of 90° and 120°. They show most information about the location of the fruits.

** ** FIGURE 6: FD for position 1 - 9 in red species, with a FV threshold of 50%. 2 nd session (solid bars) and 3 rd session (hatched bars)

For images taken from one position only with the criterion of a minimum 50% fruit visibility, the FD was in no case higher than 66%. The best single positions were the front view (number 5) and looking with a zenith angle of 60° upwards (numbers 7, 8 and 9). ** ** 3.3 Combined positions

As expected, the FD increases when a combination was made of multiple viewpoint positions. With a combination of five positions, the maximum FD was 86% in case a fruit was counted as visible when a minimum part of 50% of the fruit surface was visible. This set of images consisted of two images with a zenith of 120° and an azimuth of 90° with a horizontal displacement of 15 cm and three images with a zenith of 90° and an azimuth of 30°, 90° and 120°. In addition to this, Table 2 shows also the results for FV threshold values of 40% and 60%. In case a fruit was counted as visible with a fruit visibility threshold of 10%, three camera positions only were needed to yield a FD of 93%. For this situation the addition of more positions did not further increase the FD. Table 3 shows more details for different visibility thresholds.

TABLE 2: FD for different FV threshold values and different number of angles combined from the 3rd measurement.

**FV threshold value** **Positions ** 40% 50% 60% 0.59 0.52 0.48 5 - 7 0.79 0.69 0.66 5 - 8 - 10 0.79 0.72 0.72 5 - 7 - 8 - 10 0.93 0.86 0.83 5 - 7 - 8 - 10 - 13 0.93 0.86 0.83 0.1 0.2 0.3 0.4 0.5 0.6

# FD **Position number**

TABLE 3: Maximum FD and the number of positions needed to reach that FD for different FV threshold values (Th.). Values given for 2nd measurement (2) and the 3rd measurement (3). **Th. ** **Max. ** **FD (2) **

**Pos. ** **needed ** **(2) ** **Max. ** **FD (3) ** **Pos. ** **needed ** **(3) ** **Th. ** **Max. ** **FD (2)**

**Pos. ** **need** **ed (2) ** **Max. ** **FD (3) **

**Pos. ** **needed ** **(3) ** **\[%\] ** **\[%\] ** **\[#\] ** **\[%\] ** **\[#\] ** ** ** **\[%\] ** **\[%\] ** **\[#\] ** **\[%\] ** **\[#\] ** ** ** **4. Discussion and conclusions **

An accurate determination of a percentage of FV of a fruit was difficult. In the presented study this percentage is estimated based on one image only. Due to the irregular shape and size of the fruits an exact measurement of the visible part of the fruit was not possible. To increase the accuracy two images must be taken from every position. One image of the natural scene and one image with all fruits 100% visible, for example by picking leaves.

For robotic harvesting of fruits, the detection and localization of the fruits on the plant is mandatory. Using one fixed viewpoint position only, the FD was in no case higher than 66% (with the criterion of a minimum 50% fruit visibility), which is much lower than the desired 100%. This FD however, strongly depends on the minimum amount of fruit surface needed to be visible before a sensor system would be able to detect the target. Combining multiple viewpoint positions enhanced the result. As described above the maximum FD was 86% (min. 50% FV) or 93% (min. 10% FV). As laid out in Table 2 the maximum FD (min. 50% FV) was reached with a combination of five positions, with the addition of more positions the FD did not increase.

In conclusion, a camera system for sweet-pepper fruit detection used by an autonomous harvesting robot will need to acquire images from multiple viewpoints of the same plant. Also, the system should be able to detect the presence of a fruit already when only a small part of the fruit surface is visible in the image. To reach a high percentage of harvested product, an additional sensor system mounted on the robotic arm could help. Such a sensor can enter the crop canopy to detect fruits not visible at all from the main path due to the heavy occlusion. However, taking images from several viewpoints will either be time consuming due to the repositioning of the sensor, resulting in lower cycle times for the harvest operation, or will increase the costs of the system because multiple sensors mounted at different viewpoints are needed. An economical tradeoff must be found between the needed percentage of detected product and the available room for investment. **Acknowledgements  **

The authors gratefully acknowledge the support of the sweet-pepper growers Vollebregt (Bleiswijk, NL) and Van Dijk Bedrijven (Harmelen, NL). The authors wish to thank Wouter Bac and Bart van Tuijl for assistance in building the measurement device.

This research was partly funded by the European Commission in the 7th Framework Programme (CROPS GA no 246252). **References  **

Bulanon, D.M., T.F. Burks, and V. Alchanatis (2010). "A multispectral imaging analysis for enhancing citrus fruit detection". Environmental Control in Biology. 48(2): p. 81-91.

Jiménez, A.R., R. Ceres, and J.L. Pons (2000). "A survey of computer vision methods for locating fruit on trees". Transactions of the ASAE. 43(6): p. 1911-1920.

Plebe, A. and G. Grasso (2000). "Localization of spherical fruits for robotic harvesting". Machine Vision and Applications. 13(2): p. 70-79.

van Henten, E.J., J. Hemming, B.A.J. van Tuijl, J.G. Kornet, J. Meuleman, J. Bontsema, and E.A. van Os (2002). "An autonomous robot for harvesting cucumbers in greenhouses". Autonomous Robots. 13(3): p. 241-258.

Tanigaki, K., T. Fujiura, A. Akase, and J. Imagawa (2008). "Cherry-harvesting robot". Computers and Electronics in Agriculture. 63(1): p. 65-72. **  **