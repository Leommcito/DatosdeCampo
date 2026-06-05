## Assessing a Multi-Camera System to Enhance Fruit Visibility for Robotic

## Harvesting in a V-Trellised Apple Orchard Juan Villacr´es a, Stavros Vougioukas a, *∗*

*a* *Department* * * *of* * * *Biological* * * *and* * * *Agricultural* * * *Engineering,* * * *University* * * *of* * * *California,* * * *Davis,* * * *USA* **Abstract**

Accurate detection and localization of fruits within the canopy are crucial for various tasks, such as per-

ception for robotic harvesters, vision-based yield estimation, and early disease detection. However, complex

canopy structures render fruit detection challenging due to obstructions from leaves, branches, and other

fruits. This study assesses the efficacy of utilizing multiple cameras at varying elevations and azimuthal an-

gles to enhance fruit visibility. We used a V-trellised apple orchard as a case study, where four cameras were

employed; the first was oriented normally to the fruit canopy, while three others maintained a fixed position

relative to the first but with variable orientation. Adjusting elevation and azimuthal angles revealed that,

in the region of interest of the canopy, a single camera whose optical axis was perpendicular to the canopy

could detect up to 88.3% of the fruits detected by four cameras. Adding one more camera - for a total of two

cameras - increased the detection rate up to 97.5% of the four-camera detection rate. Also, the experimental

results showed that three cameras could detect between 96.0% to 99.7% of fruits compared to four cameras

under the proposed camera configuration. Hence, the utility of adding a third or fourth camera would need

to be considered carefully, given the added cost and complexity. The results of this study are a step toward

exploring and optimizing multiple-camera perception systems for orchard operations, in particular, robotic harvesters.

*Keywords:* multi-camera, fruit visibility, V-shaped canopy **1.** ** ** **Introduction**

Fresh fruits are delicate and easily damaged if not handled with care. For this reason, the recommended

harvesting technique is manual picking, which is costly and time-consuming. Furthermore, there is a farm

labor shortage due to socioeconomic circumstances (Taylor et al., 2012). A promising solution to this

problem is the use of robotic harvesters, which have captured the interest of industry and academia due

to recent advances in robotics and artificial intelligence. An automated harvester typically consists of a

manipulation system with an end-effector, a vision system for fruit detection and localization, and a fruit

conveyance system (Zhang et al., 2019). Fruit detection can be very challenging due to the complexity of the

agricultural environment, where the principal influencing factors are sharp gradients in natural light intensity

and occlusions. The latter is caused by overhanging branches, leaves, or other fruit growing in clusters Gongal et al. (2016).

*∗* Corresponding author *Email* * * *address:* svougioukas@ucdavis.edu (Stavros Vougioukas)

© 2024 published by Elsevier. This manuscript is made available under the Elsevier user license <https://www.elsevier.com/open-access/userlicense/1.0/>

Version of Record: <https://www.sciencedirect.com/science/article/pii/S0168169924005556> Manuscript\_e17e39129b15cd958c1e2a511416b4ac

Moreover, fruit detection is necessary not only for robotic harvesting but also for yield estimation. Fruit

occlusion affects fruit identification and counting, leading to an error in yield estimation (Prabhu & Lakshmi,

2021). In this context, Bellocchio et al. (2019) highlighted the necessity to develop algorithms robust to fruit

occlusion when there is a dense cluster of fruit. In addition, Obsie et al. (2022) pointed out that occlusion

also poses challenges in disease detection, thus emphasizing the need for advanced solutions to overcome the

visibility limitations imposed by occlusion in various agricultural contexts. Appealing to the need to address

the occlusion of fruits in tree canopies for robotic harvesting, this paper presents an approach to evaluate

the improvements in fruit visibility when one, two, three, or four RGB-D cameras are used for fruit detection

at various orientations relative to the canopy, and reports results from using the approach in a V-trellised

apple orchard. A multi-camera system is set up to view the canopy from multiple angles concurrently. Such

a system is expected to increase the chances of fruits being fully or partially visible, thus extending the

approach of using a single camera with an optimized pose to detect fruits ( Tang et al. (2023).

Our target application is robotic harvesting in orchards with planar tree canopies. The goal is to increase

fruit visibility inside a region of interest (ROI) on the canopy plane that lies within the robot arms' workspace

so that more fruits can be picked. In a multi-camera system, the ROI is defined by the intersection of the

projections of the cameras' fields of view (FoVs) on the canopy. Cameras oriented at larger angles relative

to each other can provide different view angles of the same ROI and thus improve fruit visibility. However,

as the differences between camera orientation angles become larger, the intersection of their FoVs (the ROI)

becomes smaller; large orientation differences cause the ROI to disappear. ROIs that are too small are not

useful to a harvesting robot and do not contain enough fruits to assess the improvement in visibility when

multiple cameras are used. In this work, we selected the poses (positions, elevation, and azimuth angles)

of the cameras (section 3.2) in a way that balanced the above effects - for a given canopy geometry - thus

making it possible to assess the increase in the number of fruits visible within the selected ROI.

In principle, a 3D simulation could be used to guide the determination of camera poses that maximize

fruit visibility within an ROI. However, since fruits are occluded primarily by canopy foliage and tree limbs,

determining multi-view fruit visibility from 3D simulated canopies would require creating tree structures and

leaf and fruit spatial distributions (sizes, total number, positions, and orientations) and optical properties that

reflect real-world orchard trees, which have been trained and undergone grower-specific (and hard-to-model)

pruning and thinning practices. Tree and plant modeling is an actively researched discipline (Mitsanis et al.,

2024), but to our knowledge, calibrated models that incorporate all the above factors are not available yet.

In a nutshell, fruit visibility assessment based on 3D simulated trees cannot yet capture the visibility-related

effects in a manner that reflects real-world orchards. Therefore, our approach relies on data acquisition in real orchards.

To avoid introducing errors inherent in an automatic fruit detection system, we performed apple detection

in the acquired images by manual annotation. The apples annotated in each camera were projected onto the

other three cameras, and the total number of fruits used as the gold standard consists of the union of the

fruits visible in all four cameras. We should clarify that since our goal is to quantify the improvement in fruit

visibility in a given ROI, the actual number of fruits (yield) within the ROI is not important and should not

be used as ground truth because it does not contribute to the calculation of the visibility improvement.

The main contributions of this paper are (1) Development of a method to assess fruit visibility within

an ROI using a set of four RGB-D cameras with different poses; (2) introduction of the Multi-Camera Fruit

Detection Ratio (MC-FDR) as a metric to assess the fruit detection in a multi-camera system and (3) assess-

ment of apple detection performance in a V-trellised orchard under natural occlusion with 1vs4, 2vs4, and

3vs4 camera configurations. The paper is organized as follows: Section 2 presents the related work obtained

from the current literature, Section 3 outlines the materials and methods used for the evaluation, Section 4

presents the experiments and results, and Section 5 concludes the article with discussions summarizing the findings. **2.** ** ** **Related** ** ** **work**

Computer vision-based object detection is a well-defined task that has reached the state of the art through

Deep Learning-based (DL) methods. DL approaches that have been applied in the literature include the use

of Faster R-CNN for the detection of apples, coconuts, pears, and avocados (Vasconez et al., 2020; Parvathi

& Tamil Selvi, 2021; Pan & Ahamed, 2022; Villacr´es et al., 2023); Yolo for detecting apples (Abeyrathna

et al., 2023), strawberries (Du et al., 2023), and pitaya (Nan et al., 2023); single-shot detector (SSD) for the

detection of avocado, lemons, and apples (Vasconez et al., 2020), and EfficientDet for the detection of apple

flowers (Wu et al., 2020). The strategies mentioned above result in a bounding box with the coordinates of

the detected fruit and a score indicating how likely it is that the object belongs to that class. Other DL

approaches to semantic segmentation approximate the contour of the objects. Mask R-CNN, for instance, has

been used to segment strawberries in non-structural environments (Yu et al., 2019), grapes (Luo et al., 2022),

and apples in RGB images used on structure from motion 3D reconstruction (Gen´e-Mola et al., 2020) among

others. However, it is worth noting that occlusion has been reported in the literature to be an important

factor affecting fruit detection performance (Jia et al., 2020; Tang et al., 2023)

Several papers have included occluded fruits in the training dataset to achieve better detection responses

of the DL model under such conditions. For instance, Parvathi & Tamil Selvi (2021) used a single camera to

detect coconuts under clustering, overlapping, occlusion, varying illumination, and varying maturity states;

these conditions fall under the "category" of fruits with complex backgrounds. Chen et al. (2017) used

convolutional neural networks to detect oranges in complex environments, including highly occluded ones,

to improve detection robustness. A different approach consists of training the DL model to detect multiple

classes, where each class corresponds to different occlusion levels. As reported by Du et al. (2023), strawberries

were detected as non-occluded, mild occluded, moderate occluded, and severe occluded. Similarly, Nan et al.

(2023) considered three different obstructions: no-obstruction, fruit-obstruction, and branch-obstruction.

The average precision (AP) obtained for each obstruction type was 0.96, 0.84, and 0.77, respectively. The

results showed that the AP decreased in the presence of obstruction, especially with branch occlusion. Chen

et al. (2023) evaluated four categories of Camellia oleifera fruit, obtaining AP for classes without occlusion,

leaf occlusion, branch occlusion, and fruit occlusion of 0.97, 0.94, 0.93, and 0.92, respectively. Recent studies

used amodal segmentation to reconstruct partially occluded fruits or vegetables using visible parts captured

by the camera. For example, Gen´e-Mola et al. (2023) estimated the size of occluded apples using amodal

segmentation. Additionally, the proposal included the automatic detection of occlusion levels. The authors

found that the size estimation improved when using only apples with visibility higher than 60%. In Kim et al.

(2023), the authors employed amodal segmentation to reconstruct occluded cucumbers to help autonomous robots locate picking points.

A statistical study by Kurtser & Edan (2018) explored the impact of viewpoint variation on the de-

tectability of sweet peppers by robotic harvesters in greenhouses. The study revealed that in addition to

proximity, the camera's tilt angle positively influenced visibility across different growth seasons. Hem-

ming et al. (2014) also examined the influence of the camera azimuth and zenith angles on sweet pepper

detectability. The authors reported that a single camera view detected fruits with approximately 69% accu-

racy, whereas the incorporation of multiple viewpoints increased accuracy to 90%. Similarly, D. M. Bulanon

et al. (2009) analyzed the visibility of citrus fruits within a defined 0.5 *×* 0.5 *×* 0.5m region of interest from nine

different angles, achieving a visibility rate up to 91% through the integration of multiple viewpoints. Our

work extends these findings by evaluating the efficacy of multiple simultaneous camera views, unlike previous

studies, which utilized a single camera. Stein et al. (2016) highlighted the advantages of multi-view systems

in counting mangoes with a minimal error rate of 1.36%, emphasizing the superior counting accuracy pro-

vided by multi-view configurations compared to single or dual-view systems. Recent research in this domain

Xie et al. (2024) used four RGB-D cameras on a multi-arm apple harvester and demonstrated a reduction

in false detections, highlighting the potential benefits of a multi-camera setup. However, this work did not

explore the effect of the number of cameras and their poses on fruit visibility.

Detecting completely occluded apples with an RGB sensor is infeasible, as the field of view cannot capture

any portion of the target. Researchers have tried to increase vision system performance by simplifying the

environment, e.g., by removing the surrounding fruit and foliage. Such a solution may work for benchmark

purposes but can be impractical for real-world conditions (Arad et al., 2020; Rajendran et al., 2023).

A different approach involves active perception, which leverages numerous viewpoints to improve the scene

reconstruction. The different views, however, increase the time required for the task (Magalh˜aes et al., 2022).

To overcome this issue, a system can employ many cameras to benefit from concurrent multiple viewpoints and minimize total execution time.

**3.** ** ** **Materials** ** ** **and** ** ** **methods**

This section presents the data acquisition system and the orchard where the data were acquired. Next,

the methodology used to determine the positions and corresponding maximum azimuth and elevation angles

of the cameras is discussed. Finally, the procedure to extract ground truth data from the images (number

of visible fruits detected by a human) and an evaluation metric for comparing the visible fruits by sets of

cameras at specific angle combinations against ground truth is presented.

*3.1.* * * *Orchard* * * *and* * * *Data* * * *Acquisition* * * *system*

An orchard of Pink Lady apples located in Lodi, California, USA (38.075018, -121.182455) was used as a

research location on October 14, 2022, with an average temperature of 19.6 ° C; precipitation of 0 mm and

an approximate humidity of 40%. The apple orchard was arranged in a V-shaped configuration (Fig. 1a).

To keep the test as realistic as possible, the canopy was not simplified to increase visibility; there was no

pruning, leaf thinning, or apple removal to reduce clustering. The broadest segment on the top of the V-

shaped canopy was approximately 1.4 (m) wide. The heights of the lowest and highest apples on the canopy

were approximately 0.45 (m) and 3.2 (m) above the ground, respectively. The average number of fruits per

square meter in the orchard we tested was approximately 10 fruits. 1.4 (m) 2.75 (m) (a) Camera 1: Elevation: Azimuth Camera 2 Camera 4 Camera 3 (b)

Figure 1: Photographs of the field test in the apple orchard (a) depict the V-shaped canopy and (b) the cart with the four

cameras for data acquisition. The GPS antenna is on the top of the mast, which is not visible in the picture.

Four RGB-D cameras were mounted on a mast on a cart to facilitate the movement of the cameras inside

the orchard rows Fig. 1b. The cameras were identical Realsense D435i (Intel Corporation, Santa Clara,

California, USA). Cameras from this manufacturer have been used in agricultural applications such as apple

instance segmentation (Kang et al., 2022), tomato detection and localization (Li et al., 2023), detection of

table grape ears and stems (Jin et al., 2022), and cotton top bud recognition (Song et al., 2022) among

others. For each test, the camera elevation and azimuth angles were set to the desired angles and fine-tuned

using the Digital Angle Finder 35-408 (iGaging, San Clemente, California, USA). Subsequently, a calibration

checkerboard with a size of 7 × 9 and a square size of 60 (mm) was used to estimate the extrinsic matrices

between the cameras. The cart was pulled manually along the row, and images from the four cameras were

recorded simultaneously. The cart's position was obtained with a Piksi Multi Real-Time Kinematic (RTK)

GNSS receiver (Swift Navigation, San Francisco, California, USA) at 10 (Hz). The images were acquired

with a resolution of 1280x720 at 30 fps and were recorded between 11 AM and 2 PM, with no noticeable

shadow effects on the apples or glare on the camera images. The RGB and depth images were recorded with

their corresponding time stamp using the framework ROS (Robot Operating System) Noetic; the operating system running ROS was Ubuntu 20.04.

*3.2.* * * *Selection* * * *of* * * *camera* * * *positions* * * *and* * * *maximum* * * *view* * * *angles*

A methodology is presented to determine the positions and corresponding maximum azimuth and elevation

angles of the cameras. Our goal is to find angles that differ as much as possible while ensuring that the sizes

of the resulting ROIs - defined by the intersection of their FoVs - are large enough to contain enough fruits for evaluation purposes.

A graphical representation of the spatial layout of the cameras is depicted in Figure 2. We leverage the

fact that the V-shaped canopy creates a flat fruiting wall (Bargoti et al., 2015), therefore we assume the

canopy is a flat surface. A camera is said to be oriented at 0 ° elevation and 0 ° azimuth angles when the

camera's optical axis is normal to the canopy (see Figure 2a). Note that the elevation of 0 °, is relative to the

ground elevation with an angle Γ, as shown in 2a. The horizontal separation between the cameras is depicted

as "w" while the vertical separation is "h" as presented in Figure 2b. h Canopy *d* Canopy *h* Ref. 0 o

# G

# G

# D (a) w h (b)

Figure 2: Layout of the cameras in front of a V-shaped canopy. (a) Side view: Canopy *h* and Canopy *d* are the canopy height

and opening, respectively. ˆ *D* is the distance between the cameras and the center of the canopy, and Γ is the canopy inclination

angle. (b) Front view: the horizontal and vertical separations of the cameras are h and w, respectively.

The process of selecting the camera positions and maximum angles involves calculating the ROI geomet-

rically for a given multi-camera layout, defining the area of the desired ROI, selecting initial camera poses,

and iteratively increasing the angles and adjusting the camera separation distances until the resulting ROI

area drops below the desired one. The steps are described next. Camera 1 Plane of projection 1 Plane of projection 2 Plane of projection 3 Plane of projection 4 Intersection Camera 2 Camera 3 Camera 4

Figure 3: Rendered visualization of a multi-camera system setup, illustrating the four cameras' spatial arrangement and projec-

tion planes. The intersection corresponds to the ROI where the apple detection is evaluated.

- Get canopy and camera geometric parameters: In the orchard, we measure the canopy height (Canopy *h* )

and opening (Canopy *d* ), which define the angle of canopy inclination (Γ). We also measure the tree row

separation (D). From the camera's specifications, we record the horizontal and vertical fields of view (FoV) and resolution.

- Set the ROI's desired area: We select the desired area size of the region of interest (ROI) where fruit

visibility will be evaluated. The expected number of fruits in the ROI will depend on the fruit density

# (FD).

- Develop ROI calculator: We employ a symbolic mathematics library to model the canopy plane, calcu-

late the camera projections on the canopy using the extrinsic and intrinsic matrices, and compute the

intersections of these projections. Alternatively, software for 3D rendering could be used as well. The

*i* -th camera's (C *i* ) FoV can be modeled as a pyramid based on the camera's horizontal and vertical

FoV angles. The pyramid's projection on the canopy plane is denoted as * * *P* *Ci*. The intersection of all

the cameras' projections results in a polygonal region of interest (ROI) under study. In Fig 3, the FoV

of cameras 1-4 is shown in purple, yellow, green, and blue color, respectively. Each camera's projection

plane is plotted over the canopy plane, with the same color as the camera but with transparency, to

enable the visualization of the intersection planes. The diagonal black stripes represent the overlap between all the cameras' fields of view.

- Place reference camera: The reference (#1) camera is positioned at a distance ˆ D = * * *D/* 2 from the

canopy, which is equal to half the distance between adjacent rows. We also fix the elevation angle to

the inclination angle Γ and the azimuth angle to zero (see Fig. 2a). This angle mimics a direct view

without any tilt. Thus, the reference camera's plane is parallel to the canopy plane. The height of the

camera is adjusted to ensure that its FoV spans an area equal to the desired ROI area.

- Set the initial vertical and horizontal spacing of the cameras to a value equal to the square root of

the ROI area and place the other cameras relative to the reference camera. Using the ROI calculator,

adjust the elevation and azimuth angles to achieve an ROI with an area equal to the desired area. - Iterative camera pose selection:

**-** Increase the cameras' azimuth and elevation angles by a step.

**-** Use the ROI calculator to adjust the camera spacing so that the area of the ROI does not drop below the desired one. **-** If no such spacing exists, terminate.

Once the maximum view angles (azimuth and elevation) and camera separation have been determined,

experiments are performed at angles that fall within zero and the maximum values of the view angles.

*3.3.* * * *Fruit* * * *detection* * * *within* * * *the* * * *Region* * * *of* * * *Interest*

The total number of fruits detected by all * * *m* cameras working simultaneously has to be assessed within

the ROI. This number is used as the benchmark to compare the performance of a single, two, or three up to

*m* * −* 1 cameras. The fruit detection and ROI are depicted in the fourth step of Fig. 4. The ROI is obtained

following the algorithm 1. First, the original frame rate is sub-sampled during post-processing to avoid a

high overlap rate between consecutive images. Next, the apples and leaves that belong to other rows, as

well as the background, are removed using the depth information based on a distance threshold. After the

thresholding, the remaining pixels in the depth image * * *i* are then projected into the 3D coordinate system

( *xyz* *i* ) using their corresponding intrinsic matrix * * *K* *i*. The coordinate * * *xyz* *i* indicates the local camera frame

*i*, where * * *i* * * *∈\{* 1 *,* 2 *,..., m* *\}*. The points in the coordinate systems * * *xyz* 2 *,* 3 *,...,m* are converted into the base

system * * *xyz* 1 using the extrinsic matrices obtained during the calibration. Then, all the points per camera

are back-projected onto the pixel coordinates of the reference camera (#1) using the intrinsic matrix * * *K* 1.

The points projected in camera #1 form * * *m* * −* 1 images containing holes because there is no pixel-to-pixel

mapping, so the morphological operation dilation followed by erosion (i.e., closing) was applied to fill those

holes. Finally, the region of interest (ROI) corresponds to the intersection of the projections of the * * *m* * −* 1

cameras. The same processing is repeated * * *m* * −* 1 times, using cameras 2, 3, * * *...*, * * *m* as references instead of camera 1.

To obtain the total number of fruits inside the ROI, apples are manually detected as points (i.e., two

coordinates) within the ROI seen by the reference camera (# 1). These points are then projected onto the

remaining * * *m* * −* 1 cameras. If an apple is not visible in camera * * *i*, it is labeled as not visible. This process is

repeated for cameras 2, 3,..., * * *m*. Apples already visible in the reference camera do not need to be labeled

again in camera * * *i* to avoid multiple counting of the same fruit.

Cart with four cameras and angles adjustment Extrinsic calibration

| Data acquisition | RGB-D | 1280x720 @ 30 fps |
|:--- |:--- |:--- |
| Depth filtering, | ROI intersection | and apple detection |
| Multi-camera | Fruit detection | rate (MC-FDR) |
| 93 % | 78 % | 80 % |

Depth filtering, ROI intersection and apple detection Multi-camera Fruit detection rate (MC-FDR) 93 % 78 % 80 % 82 %

Figure 4: General scheme for the camera calibration, data acquisition and processing, and metrics evaluation. *3.4.* * * *Evaluation* * * *metric*

To evaluate the performance of a multi-camera system for fruit detection, we define the Multi-Camera

Fruit Detection Ratio (MC-FDR). The MC-FDR is calculated by counting the number of fruits detected in

the region of interest (ROI) by each camera in the set * * *k*, over the fruits detected by the total number of

cameras * m* used as a benchmark. The MC-FDR represents the effectiveness of using a specific set of cameras

for detecting fruits compared to using a larger set of cameras. MC-FDR = Number of fruits in S

*j* *∈* *k* * * *C* *j* Number of fruits in S *m* $$ l=1 Cl $$ (1)

**4.** ** ** **Experiments** ** ** **and** ** ** **Results**

This section outlines the experiments conducted to evaluate the multi-camera system's performance in

fruit detection within the defined regions of interest (ROIs). It details the four camera configurations, the

fruit annotation process, and the resulting performance metrics.

*4.1.* * * *Tests* * * *for* * * *Multi-Camera* * * *Configuration*

The tests conducted for the multi-camera system followed the methodology described in subsection 3.2.

The canopy geometry from the view presented in Fig. 1a was modeled as a triangle with a height (Canopy *h* )

of 2.75 meters and a base (Canopy *d* ) of 1.4 meters in where the size of the ROI was defined as 1 * ×* 1 *m*. To

develop the ROI calculator we used the symbolic mathematics library "SymPy," we defined the equations for

the canopy plane and the lines of each camera's frustum based on the camera specifications. The cameras

were initially simulated to be placed at the center of the row, with a horizontal and vertical separation of

1 meter (e.g., the square root of the desired ROI area) and the same elevation and azimuth angles as the

reference camera. The position and orientation of the cameras were then adjusted iteratively as described

in subsection 3.2. Considering our application requirements, we found that the maximum angle difference in

azimuth and elevation was 30 ° at a horizontal separation distance of 0.8 meters and a vertical distance of 0.8

**Algorithm** ** ** **1** Image Processing using Camera 1 as reference

1: ** ** **Input:** Images from cameras at 30 fps

2: ** ** **Output:** Processed 3D points in camera 1 frame

3: ** ** **Parameters:** Intrinsic matrices * * *K* *i* for cameras * * *i* = 1 *,* 2 *,* 3 *,* 4, extrinsic parameters * * *R* *j* *, T* *j* from cameras j = 2, 3, 4 to camera 1 4: ** ** **procedure** ProcessImages

5: **Subsample** ** ** **frames** ** ** **to** ** ** **0.5**

6: **for** each frame at time * * *t* ** ** **do** 7: **for** each camera * * *i* ** ** **do**

8: **Filter** ** ** **out** ** ** **points** with depth * * *D* *i* ( *x, y* ) * \>* 3( *m* ) from camera * * *i*

9: **Project** ** ** **remaining** ** ** **points** to 3D using intrinsic matrix * * *K* *i*

10: XY Zi = K−1 *i* *·* \[ *u* *i* *, v* *i* *,* 1\] *T* 11: **if** * * *i* * ̸* = 1 ** ** **then**

12: **Transform** ** ** **points** * * *XY Z* *i* to camera 1 frame 13: XY Z1i = Ri \cdot XY Zi + Ti 14: **end** ** ** **if** 15: **end** ** ** **for**

16: **Retro-project** ** ** **points** in camera 1 frame to pixel coordinates 17: $$ [U1, V1, 1]T = K1 \cdot XY Z1i $$

18: **Apply** ** ** **closing** ** ** **operation** to fill holes

19: **Determine** ** ** **Region** ** ** **of** ** ** **Interest** as the intersection of projections from all cameras 20: **end** ** ** **for** 21: ** ** **end** ** ** **procedure**

meters. The mast was placed close to the center of the row, and the distance between the row (trunks of the trees) and the mast was 2 (m)

For our experiments, we used elevation and azimuth angles of 0 °, 15 ° and 30 °. We tested four different

camera configurations, as presented in Figure 5. Throughout all the tests, the pose of camera 1 remained

constant as a reference. Camera 2's elevation was varied between 15 ° and 30 °. Negative angles could cause

a reduction or complete loss of intersection with camera 1's field of view. Similarly, due to the position of

camera 2 relative to camera 1, changes in the azimuth angle were expected to reduce or completely eliminate

their field of view intersection. As a result, no changes were made to the azimuth angle. A similar criterion

was used to define the angles for cameras 3 and 4. In particular, the camera 3 elevation angle was set at

zero while the azimuth angle was changed between 15 ° and 30 °. As for camera 4, all possible combinations of

azimuthal and elevation angles at 15 ° and 30 ° were examined. These details are illustrated in the lower right of each test on Figure 5. Test 1 Test 2 Test 3 Test 4 Elevation q Azimuth a Cam 1 Cam 3 Cam 2 Cam 4 0, q a $$ = $$ $$ = $$ 0, q a $$ = $$ $$ = $$

15, q a $$ = $$ $$ = $$ 15, q a $$ = $$ $$ = $$ Cam 1 Cam 3 Cam 2 Cam 4 0, q a $$ = $$ $$ = $$ 0, q a $$ = $$ $$ = $$

15, q a $$ = $$ $$ = $$ 15, q a $$ = $$ $$ = $$ Cam 1 Cam 3 Cam 2 Cam 4 0, q a $$ = $$ $$ = $$ 30, q a $$ = $$ $$ = $$ 0, q a $$ = $$ $$ = $$ 30, q a $$ = $$ $$ = $$ Cam 1 Cam 3 Cam 2 Cam 4 0, q a $$ = $$ $$ = $$ 30, q a $$ = $$ $$ = $$ 0, q a $$ = $$ $$ = $$ 30, q a $$ = $$ $$ = $$

Test *i* Looking towards the canopy \{ \} 1,2,3,4 *i* Î

Figure 5: Description of camera configuration for tests 1-4. The cameras are horizontally and vertically separated by 0.8m. The

elevation angle is considered 0 ° when the camera plane is parallel to the plane of the bell, i.e. the elevation angle is measured with respect to an inclination angle Γ. *4.2.* * * *Fruit* * * *annotation*

Following the procedure presented in subsection 3.3, the apples were manually annotated to keep the

visibility assessment independent of the performance of any object detector. We developed a customized

graphical user interface (GUI) based on Qt to annotate the apples in this multi-camera approach. Qt is a

development framework that contains tools for creating user interfaces for multiple platforms (available at:

<https://www.qt.io/).> It is worth noting that some apples have a small size -small number of pixels- due

to the distance between the camera and their positions in the canopy. Such a small size makes it difficult

to map the points (i.e., apple centers) from one camera to another, mainly because of limitations related

to the fact that the depth map decreases in accuracy with distance. Andriyanov et al. (2022) reported an

incremental error in estimating apple coordinates with increasing distance using a Realsense camera. The

small size of some apples in the camera frame can cause slight displacements when detected by one camera

and projected on another. To solve this problem, our graphical interface incorporates a feature that allows

manual repositioning of the apples to ensure their precise location. This adjustment is based on preserving

the spatial integrity of the apples in the four cameras. In addition, the apples identified with sufficient

integrity were used as a reference for refining the location of other apples, increasing the labels' correctness.

This technique is especially beneficial with clustered apples or apples that appear small in size relative to the

camera frame. The labeling details are as follows: the original acquisition rate of 30 fps was subsampled to

0.5 fps, and the threshold for removing leaves, fruits and the background was 3 (m).

The experiment consisted of four tests as mentioned in subsection 4.1, each using 100 images per camera,

meaning that 400 images were labeled per test. The tests were conducted along one long orchard row (402.92

m). The distances covered in tests 1-4 were 70.53 m, 98.56 m, 114.05 m, and 119.78 m, respectively. The

distance difference was due to variation in cart pulling speed, but this factor did not affect image quality, i.e.,

there was no blurring. We detected and labeled manually 1075, 1438, 1298, and 1380 fruits in the region of

interest (ROI) for tests 1-4, respectively (a total of 5191 apples). The number of fruits detected in the ROI

depends on the distance covered by the cart, the cameras' poses for each test, and the unstructured nature

of the environment. The unevenness of the terrain caused the cart to sometimes move closer or further away

from the canopy, leading to variations in the number of fruits detected in the ROI.

Figure 6 presents a snapshot of four images acquired simultaneously for Test 1. The images have the

same height as the camera recorded, but the width was cropped to focus on the fruits. The purple circle

indicates an easily visible apple captured by all the cameras, while the purple dashed line shows the apple's

connection in all four views. A zoom-in view of an occluded fruit is displayed in the black square. In the

view from camera 1, the fruit surrounded by a light-blue line is partially occluded by another fruit in front of

it. In the second zoom-in image, the apple surrounded by a light-blue line is mainly occluded by a leaf and a

thin branch. Camera 3's zoom-in shows a heavy occlusion by leaves, and the fruit is not visible in Camera 4. Camera 1 Camera 2 Camera 3 Camera 4

Figure 6: Example of apple occlusion captured during Test 1. The light purple circle represents a clearly visible apple, while

the light blue line depicts a partially obscured fruit seen from various angles. The green line represents the boundaries of the region of interest. *4.3.* * * *Multi-camera* * * *assessment*

Table 1 represents the results of the apple detection accuracy when detection uses one camera vs. when

all four cameras are used. In all four tests, using only camera 1 had the best performance compared to using

only camera 2, 3, or 4. If only one camera were to be used, it would have to be camera 1, whose optical

axis was consistently normal to the canopy. This result suggests that a normal camera is the best option

compared to the other orientations proposed in this research. This result can be associated with the flat

nature of the V-shaped canopy and its parallel alignment to the plane of the camera. Contrary to the best

performance, camera 4 resulted in the worst performance in all tests, with an MC-FDR as low as 70.4% in

test 2. The camera was located farthest from camera 1, and in test 2, its elevation was 30 degrees, and the

azimuth was 15 degrees. On the other hand, camera 2 performed well in all tests, except test 2, where camera 3 took the second position. Test 1 (%) Test 2 (%) Test 3 (%) Test 4 (%)

| Camera\{1\} | 86.3 | 87.3 | 88.2 | 88.3 |
|:--- | ---: | ---: | ---: | ---: |
| Camera\{2\} | 82.4 | 79.4 | 85.8 | 84.3 |
| Camera\{3\} | 80.8 | 84.2 | 85.0 | 83.4 |
| Camera\{4\} | 76.7 | 70.4 | 79.4 | 76.9 | Camera *\{* 2 *\}* 82.4 79.4 85.8 84.3 Camera *\{* 3 *\}* 80.8 84.2 85.0 83.4 Camera *\{* 4 *\}* 76.7 70.4 79.4 76.9

Table 1: MC-FDR of camera * * *i* (Camera *\{* *i* *\}* ) compared to four cameras. Test 1: cam 2, * * *θ*: 30 °; cam 3, * * *α*: 30 °; cam 4, * * *θ*: 30 °,

\alpha: 30°; Test 2: cam 2, \theta: 30 °; cam 3, \alpha: 15°; cam 4, \theta: 30 °, \alpha:, 15 °; Test 3: cam 2, \theta: 15 °; cam 3, \alpha: 30 °; cam 4: \theta: 15°,

\alpha: 30°; Test 4: cam 2, \theta: 15 °; cam 3, \alpha: 15°; cam 4, \theta: 15 °, \alpha: 15 °.

The detection performance when two (out of four) cameras were used is shown in Table 2. Based on the

single-camera detection performances, the pair with the better performance was expected to include camera

1. The results confirmed that the detection performance with camera 1 and camera 3 was better or equally

good with respect to the other pair combinations across all the tests. The best performance was 97.5%

detection in test 4; closely, this pair achieved 97.2% in test 3, which was expected because camera 3 has the

same setup in both of these tests. Considering the combinations where camera 1 was unavailable, pair 2 and

3 obtained the best performance if only two cameras were to be used. It is worth noting that camera 2 is

adjusted for elevation only, while camera 3 is adjusted for azimuth orientation only. In general terms, the

worst result involved the pairs with camera 4 jointly with camera 3 for three of the four tests.

Table 3 illustrates the detection performance when three cameras were used, as compared to all four

cameras. Based on the tests conducted in this research, cameras 1, 2, and 3 produced the best results.

The addition of camera 4 resulted in a minimal increase in apple detection ranging from 0.3% to 1.2% (as

indicated by MC-FDR in Table 3, row 1). Given the minimal improvements in the detection performance, it

is recommended to remove camera 4 if there is a need to reduce hardware cost and processing time.

## Test 1 (%) Test 2 (%) Test 3 (%) Test 4 (%)

| Camera\{1∪2\} | 93.2 | 92.6 | 95.1 | 94.9 |
|:--- | ---: | ---: | ---: | ---: |
| Camera\{1∪3\} | 95.3 | 97.0 | 97.2 | 97.5 |
| Camera\{1∪4\} | 94.7 | 93.7 | 95.2 | 95.3 |
| Camera\{2∪3\} | 95.3 | 95.1 | 97.0 | 96.5 |
| Camera\{2∪4\} | 90.3 | 87.1 | 92.8 | 91.5 |
| Camera\{3∪4\} | 89.1 | 88.9 | 91.9 | 90.8 |

## Camera \{ 1 ∪ 3 \} 95.3 97.0 97.2 97.5

## Camera \{ 1 ∪ 4 \} 94.7 93.7 95.2 95.3

## Camera \{ 2 ∪ 3 \} 95.3 95.1 97.0 96.5

## Camera \{ 2 ∪ 4 \} 90.3 87.1 92.8 91.5

## Camera \{ 3 ∪ 4 \} 89.1 88.9 91.9 90.8

Table 2: MC-FDR of camera * * *i* and * * *j* (Camera *\{* *i* *∪* *j* *\}* ) compared to four cameras. Test 1: cam 2, * * *θ*: 30 °; cam 3, * * *α*: 30 °; cam 4,

\theta: 30 °, \alpha: 30°; Test 2: cam 2, \theta: 30 °; cam 3, \alpha: 15°; cam 4, \theta: 30 °, \alpha:, 15 °; Test 3: cam 2, \theta: 15 °; cam 3, \alpha: 30 °; cam 4:

\theta: 15°, \alpha: 30°; Test 4: cam 2, \theta: 15 °; cam 3, \alpha: 15°; cam 4, \theta: 15 °, \alpha: 15 °.

## Test 1 (%) Test 2 (%) Test 3 (%) Test 4 (%)

| Camera\{1∪2∪3\} | 98.8 | 99.1 | 99.5 | 99.7 |
|:--- | ---: | ---: | ---: | ---: |
| Camera\{1∪2∪4\} | 97.5 | 96.1 | 97.5 | 97.3 |
| Camera\{1∪3∪4\} | 97.8 | 98.5 | 98.7 | 98.9 |
| Camera\{2∪3∪4\} | 96.7 | 96.0 | 98.1 | 97.9 |

## Camera \{ 1 ∪ 2 ∪ 4 \} 97.5 96.1 97.5 97.3

## Camera \{ 1 ∪ 3 ∪ 4 \} 97.8 98.5 98.7 98.9

## Camera \{ 2 ∪ 3 ∪ 4 \} 96.7 96.0 98.1 97.9

Table 3: MC-FDR of cameras * * *i*, * * *j* and * * *k* (Camera *\{* *i* *∪* *j* *∪* *k* *\}* ) compared to four cameras. Test 1: cam 2, * * *θ*: 30 °; cam 3, * * *α*: 30 °;

cam 4, \theta: 30 °, \alpha: 30°; Test 2: cam 2, \theta: 30 °; cam 3, \alpha: 15°; cam 4, \theta: 30 °, \alpha:, 15 °; Test 3: cam 2, \theta: 15 °; cam 3, \alpha: 30 °;

cam 4: \theta: 15°, \alpha: 30°; Test 4: cam 2, \theta: 15 °; cam 3, \alpha: 15°; cam 4, \theta: 15 °, \alpha: 15 °.

## 5. Discussions and conclusion

## This paper introduced a method to assess fruit visibility - and its improvement - when multiple RGB

## D cameras at different poses are viewing planar orchard canopies. The assessment of fruit visibility was

## performed within the ROI defined by the intersection of the FoVs of the cameras. The reason was that the

## target application is robotic harvesting, where fruit detection and localization must be done in targeted areas

## inside the arms' workspace. Results were presented from a V-trellised apple orchard when up to four cameras

## were used.

This type of canopy is highly advantageous as it intercepts more than 75% of the light, leading

## to a higher yield of apples, as reported by Robinson (2017). Moreover, the V-shaped canopy can be used

## for other fruit trees that are hand-picked in orchards (Hrotk´o, 2013). The experiment involved placing four

## cameras in fixed positions, three of which had varying elevation and azimuth angles.

## The results showed that a single camera with its optical axis perpendicular to the canopy obtained an

## MC-FDR ranging from 86.3% to 88.3%. Including a second camera improved the MC-FDR by about 9%

## compared to using only the camera with its optical axis normal to the canopy. The highest detection rate

## was achieved when using camera 1 and camera 3, with MC-FDR ranging from 95.3% to 97.5%. This finding

## emphasizes the importance of strategically selecting camera orientation and position. For example, Mehta &

## Burks (2016) studied the benefits of using multiple cameras in a layered vision system, where four cameras

achieved a localization efficiency of over 90%, even in the presence of noise. When three cameras were used,

the detection rate increased to 98.8% and 99.7% when using cameras 1, 2, and 3. These results raise questions

about the utility of using four cameras, as four cameras improved the detection rate by 1.2% and 0.3% with

respect to three cameras, respectively. In absolute terms, given the number of fruits in Test 1 and Test 4,

adding a fourth camera would help detect only 13 and 4 more apples out of 1075 and 1380, respectively.

The developed methodology is generic and can be applied to other planar orchard canopies. However, while

the experimental results provided valuable insights, it is important to acknowledge certain limitations. Data

were collected on a single apple variety in one orchard with V-trellised trees that underwent a pruning and

thinning regime specific to that orchard. Additionally, the data were gathered on a single day within a specific

time window (11 AM to 2 PM) along a 403-meter-long row. These factors may limit the generalizability of

our findings to other conditions and orchard management practices. Future research should aim to replicate

this study across different orchards and apple varieties and over multiple days and times to facilitate broader applicability.

This research presented an analysis focused on varying the orientation of multiple cameras for fruit

detection in targeted regions of V-shaped canopies. Camera angles were selected from a discrete range of

values. The results provided useful information for selecting the number of cameras and their configurations,

which is crucial to developing multi-camera configurations for orchard operations.

**Declaration** ** ** **of** ** ** **Generative** ** ** **AI** ** ** **and** ** ** **AI-Assisted** ** ** **Technologies** ** ** **in** ** ** **the** ** ** **Writing** ** ** **Process**

While preparing this work, the authors used Grammarly to improve the grammar and syntax of the

text. After using this tool/service, the authors reviewed and edited the content as needed and took full

responsibility for the content of the publication. **Acknowledgments**

This work was funded by USDA-NIFA Grant 2020-67021-30759 under the National Robotics Initiative,

USDA-NIFA Grant 2020-67021-32428, and Hatch project 1013396. **References**

Abeyrathna, R. M. R. D., Nakaguchi, V. M., Minn, A., & Ahamed, T. (2023). Recognition and Counting of

Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms for Robotic Harvesting Sys-

tems. * * *Sensors*, * * *23*, 3810. URL: <https://www.mdpi.com/1424-8220/23/8/3810>. doi: 10.3390/s23083810.

Andriyanov, N., Khasanshin, I., Utkin, D., Gataullin, T., Ignar, S., Shumaev, V., & Soloviev, V. (2022).

Intelligent System for Estimation of the Spatial Position of Apples Based on YOLOv3 and Real Sense

Depth Camera D415. * * *Symmetry*, * * *14*, 148. URL: <https://www.mdpi.com/2073-8994/14/1/148>. doi: 10. 3390/sym14010148.

Arad, B., Balendonck, J., Barth, R., Ben-Shahar, O., Edan, Y., Hellstr¨om, T., Hemming, J., Kurtser, P.,

Ringdahl, O., Tielen, T., & Van Tuijl, B. (2020). Development of a sweet pepper harvesting robot. * * *Journal*

*of* * * *Field* * * *Robotics*, * * *37*, 1027-1039. URL: <https://onlinelibrary.wiley.com/doi/10.1002/rob.21937>. doi: 10.1002/rob.21937.

Bargoti, S., Underwood, J. P., Nieto, J. I., & Sukkarieh, S. (2015). A Pipeline for Trunk Detection in Trellis

Structured Apple Orchards. * * *Journal* * * *of* * * *Field* * * *Robotics*, * * *32*, 1075-1094. URL: <https://onlinelibrary.>

wiley.com/doi/10.1002/rob.21583. doi: 10.1002/rob.21583.

Bellocchio, E., Ciarfuglia, T. A., Costante, G., & Valigi, P. (2019). Weakly Supervised Fruit Counting for

Yield Estimation Using Spatial Consistency. * * *IEEE* * * *Robotics* * * *and* * * *Automation* * * *Letters*, * * *4*, 2348-2355. URL:

<https://ieeexplore.ieee.org/document/8661632/>. doi: 10.1109/LRA.2019.2903260.

Chen, S., Zou, X., Zhou, X., Xiang, Y., & Wu, M. (2023). Study on fusion clustering and improved YOLOv5

algorithm based on multiple occlusion of Camellia oleifera fruit. *Computers* * * *and* * * *Electronics* * * *in* * * *Agri-*

*culture*, * * *206*, 107706. URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169923000947>. doi: 10.1016/j.compag.2023.107706.

Chen, S. W., Shivakumar, S. S., Dcunha, S., Das, J., Okon, E., Qu, C., Taylor, C. J., & Kumar, V.

(2017). Counting Apples and Oranges With Deep Learning: A Data-Driven Approach. * * *IEEE* * * *Robotics*

*and Automation Letters*, * 2*, 781-788. URL: <https://ieeexplore.ieee.org/document/7814145/>. doi: 10.

# 1109/LRA.2017.2651944.

- M. Bulanon, T. F. Burks, & V. Alchanatis (2009). Fruit Visibility Analysis for Robotic Citrus Harvesting.

*Transactions* * * *of* * * *the* * * *ASABE*, * * *52*, 277-283. URL: <http://elibrary.asabe.org/abstract.asp??JID=3&>

$$ AID=25933&CID=t2009&v=52&i=1&T=1. doi:10.13031/2013.25933. $$

Du, X., Cheng, H., Ma, Z., Lu, W., Wang, M., Meng, Z., Jiang, C., & Hong, F. (2023). DSW-YOLO:

A detection method for ground-planted strawberry fruits under different occlusion levels. *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *214*, 108304. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S0168169923006920. doi: 10.1016/j.compag.2023.108304.

Gen´e-Mola, J., Ferrer-Ferrer, M., Gregorio, E., Blok, P. M., Hemming, J., Morros, J.-R., Rosell-Polo, J. R.,

Vilaplana, V., & Ruiz-Hidalgo, J. (2023). Looking behind occlusions: A study on amodal segmentation

for robust on-tree apple fruit size estimation. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *209*, 107854.

URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169923002429>. doi: 10.1016/j.compag. 2023.107854.

Gen´e-Mola, J., Sanz-Cortiella, R., Rosell-Polo, J. R., Morros, J.-R., Ruiz-Hidalgo, J., Vilaplana, V., & Grego-

rio, E. (2020). Fruit detection and 3D location using instance segmentation neural networks and structure-

from-motion photogrammetry. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *169*, 105165. URL: https://

linkinghub.elsevier.com/retrieve/pii/S0168169919321507. doi: 10.1016/j.compag.2019.105165.

Gongal, A., Silwal, A., Amatya, S., Karkee, M., Zhang, Q., & Lewis, K. (2016). Apple crop-load esti-

mation with over-the-row machine vision system. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *120*, 26-35.

URL: <https://linkinghub.elsevier.com/retrieve/pii/S016816991500335X>. doi: 10.1016/j.compag. 2015.10.022.

Hemming, J., Ruizendaal, J., Hofstee, J., & Van Henten, E. (2014). Fruit Detectability Analysis for Different

Camera Positions in Sweet-Pepper. * * *Sensors*, * * *14*, 6032-6044. URL: <http://www.mdpi.com/1424-8220/> 14/4/6032. doi: 10.3390/s140406032.

Hrotk´o, K. (2013). Development in fruit trees production systems. * * *AgroLife* * * *Scientific* * * *Journal*, * * *2*.

Jia, W., Tian, Y., Luo, R., Zhang, Z., Lian, J., & Zheng, Y. (2020). Detection and segmentation of

overlapped fruits based on optimized mask R-CNN application in apple harvesting robot. *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *172*, 105380. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S0168169919326274. doi: 10.1016/j.compag.2020.105380.

Jin, Y., Yu, C., Yin, J., & Yang, S. X. (2022). Detection method for table grape ears and stems

based on a far-close-range combined vision system and hand-eye-coordinated picking test. *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *202*, 107364. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S016816992200672X. doi: 10.1016/j.compag.2022.107364.

Kang, H., Wang, X., & Chen, C. (2022). Accurate fruit localisation using high resolution LiDAR-camera

fusion and instance segmentation. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * 203*, 107450. URL: https://

linkinghub.elsevier.com/retrieve/pii/S016816992200758X. doi: 10.1016/j.compag.2022.107450.

Kim, S., Hong, S.-J., Ryu, J., Kim, E., Lee, C.-H., & Kim, G. (2023). Application of amodal segmentation on

cucumber segmentation and occlusion recovery. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *210*, 107847.

URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169923002351>. doi: 10.1016/j.compag. 2023.107847.

Kurtser, P., & Edan, Y. (2018). Statistical models for fruit detectability: spatial and temporal analyses

of sweet peppers. * * *Biosystems* * * *Engineering*, * * *171*, 272-289. URL: <https://linkinghub.elsevier.com/>

retrieve/pii/S1537511017305275. doi: 10.1016/j.biosystemseng.2018.04.017.

Li, T., Sun, M., He, Q., Zhang, G., Shi, G., Ding, X., & Lin, S. (2023). Tomato recognition and lo-

cation algorithm based on improved YOLOv5. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *208*, 107759.

URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169923001473>. doi: 10.1016/j.compag. 2023.107759.

Luo, L., Yin, W., Ning, Z., Wang, J., Wei, H., Chen, W., & Lu, Q. (2022). In-field pose estima-

tion of grape clusters with combined point cloud segmentation and geometric analysis. *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *200*, 107197. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S0168169922005130. doi: 10.1016/j.compag.2022.107197.

Magalh˜aes, S. A., Moreira, A. P., Santos, F. N. d., & Dias, J. (2022). Active Perception Fruit Harvesting

Robots - A Systematic Review. * * *Journal* * * *of* * * *Intelligent* * * *&* * * *Robotic* * * *Systems*, * * *105*, 14. URL: <https://doi.>

org/10.1007/s10846-022-01595-3. doi: 10.1007/s10846-022-01595-3.

Mehta, S., & Burks, T. (2016). Multi-camera Fruit Localization in Robotic Harvesting. * * *IFAC-PapersOnLine*,

*49*, 90-95. URL: <https://linkinghub.elsevier.com/retrieve/pii/S2405896316315798>. doi: 10.1016/ j.ifacol.2016.10.017.

Mitsanis, C., Hurst, W., & Tekinerdogan, B. (2024). A 3d functional plant modelling framework for agricul-

tural digital twins. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *218*, 108733. URL: <https://linkinghub.>

elsevier.com/retrieve/pii/S0168169924001248. doi: 10.1016/j.compag.2024.108733.

Nan, Y., Zhang, H., Zeng, Y., Zheng, J., & Ge, Y. (2023). Intelligent detection of Multi-Class pitaya fruits

in target picking row based on WGB-YOLO network. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *208*,

107780. URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169923001680>. doi: 10.1016/j. compag.2023.107780.

Obsie, E. Y., Qu, H., Zhang, Y.-J., Annis, S., & Drummond, F. (2022). Yolov5s-CA: An Improved Yolov5

Based on the Attention Mechanism for Mummy Berry Disease Detection. *Agriculture*, * * *13*, 78. URL:

<https://www.mdpi.com/2077-0472/13/1/78>. doi: 10.3390/agriculture13010078.

Pan, S., & Ahamed, T. (2022). Pear Recognition in an Orchard from 3D Stereo Camera Datasets to De-

velop a Fruit Picking Mechanism Using Mask R-CNN. * * *Sensors*, * * *22*, 4187. URL: <https://www.mdpi.com/>

1424-8220/22/11/4187. doi: 10.3390/s22114187.

Parvathi, S., & Tamil Selvi, S. (2021). Detection of maturity stages of coconuts in complex background using

Faster R-CNN model. *Biosystems* * * *Engineering*, * * *202*, 119-132. URL: <https://linkinghub.elsevier.>

com/retrieve/pii/S1537511020303329. doi: 10.1016/j.biosystemseng.2020.12.002.

Prabhu, A., & Lakshmi, S. (2021). Identification and Yield Estimation of Mature Fruits Using Modified

Watershed Algorithm. In * * *2021* * * *2nd* * * *International* * * *Conference* * * *for* * * *Emerging* * * *Technology* * * *(INCET)* (pp. 1-

6). Belagavi, India: IEEE. URL: <https://ieeexplore.ieee.org/document/9456198/>. doi: 10.1109/

# INCET51464.2021.9456198.

Rajendran, V., Debnath, B., Mghames, S., Mandil, W., Parsa, S., Parsons, S., & Ghalamzan-E., A. (2023).

Towards autonomous selective harvesting: A review of robot perception, robot design, motion planning

and control. * * *Journal* * * *of* * * *Field* * * *Robotics*, (p. rob.22230). URL: <https://onlinelibrary.wiley.com/doi/> 10.1002/rob.22230. doi: 10.1002/rob.22230.

Robinson, T. (2017). Can we manage light interception levels above 70% in apple orchards? *Acta*

*Horticulturae*, (pp. 79-86). URL: <https://www.actahort.org/books/1177/1177\_8.htm>. doi: 10.17660/ ActaHortic.2017.1177.8.

Song, P., Chen, K., Zhu, L., Yang, M., Ji, C., Xiao, A., Jia, H., Zhang, J., & Yang, W. (2022). An

improved cascade R-CNN and RGB-D camera-based method for dynamic cotton top bud recognition

and localization in the field. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *202*, 107442. URL: https://

linkinghub.elsevier.com/retrieve/pii/S0168169922007505. doi: 10.1016/j.compag.2022.107442.

Stein, M., Bargoti, S., & Underwood, J. (2016). Image Based Mango Fruit Detection, Localisation and Yield

Estimation Using Multiple View Geometry. * * *Sensors*, * * *16*, 1915. URL: <http://www.mdpi.com/1424-8220/> 16/11/1915. doi: 10.3390/s16111915.

Tang, Y., Qiu, J., Zhang, Y., Wu, D., Cao, Y., Zhao, K., & Zhu, L. (2023). Optimization strategies of fruit de-

tection to overcome the challenge of unstructured background in field orchard environment: a review. * * *Pre-*

*cision* * * *Agriculture*, * * *24*, 1183-1219. URL: <https://link.springer.com/10.1007/s11119-023-10009-9>. doi: 10.1007/s11119-023-10009-9.

Taylor, J. E., Charlton, D., & Y´unez-Naude, A. (2012). The End of Farm Labor Abundance. * * *Applied* * * *Eco-*

*nomic* * * *Perspectives* * * *and* * * *Policy*, * * *34*, 587-598. URL: <https://onlinelibrary.wiley.com/doi/10.1093/> aepp/pps036. doi: 10.1093/aepp/pps036.

Vasconez, J., Delpiano, J., Vougioukas, S., & Auat Cheein, F. (2020). Comparison of convolutional neural

networks in fruit detection and counting: A comprehensive evaluation. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agri-*

*culture*, * * *173*, 105348. URL: <https://linkinghub.elsevier.com/retrieve/pii/S016816991932232X>. doi: 10.1016/j.compag.2020.105348.

Villacr´es, J., Viscaino, M., Delpiano, J., Vougioukas, S., & Auat Cheein, F. (2023). Apple orchard production

estimation using deep learning strategies: A comparison of tracking-by-detection algorithms. * * *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *204*, 107513. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S0168169922008213. doi: 10.1016/j.compag.2022.107513.

Wu, D., Lv, S., Jiang, M., & Song, H. (2020). Using channel pruning-based YOLO v4 deep learning al-

gorithm for the real-time and accurate detection of apple flowers in natural environments. * * *Computers*

*and* * * *Electronics* * * *in* * * *Agriculture*, * * *178*, 105742. URL: <https://linkinghub.elsevier.com/retrieve/pii/>

S0168169920318986. doi: 10.1016/j.compag.2020.105742.

Xie, F., Sun, N., Li, J., Feng, Q., & Li, T. (2024). Fruit Distribution Acquisition With Multi-Vision for Multi-

Arm Harvesting Robots. In * 2023 8th International Conference on Control, Robotics and Cybernetics (CRC)*

(pp. 7-13). Changsha, China: IEEE. URL: <https://ieeexplore.ieee.org/document/10488608/>. doi: 10.1109/CRC60659.2023.10488608.

Yu, Y., Zhang, K., Yang, L., & Zhang, D. (2019). Fruit detection for strawberry harvesting robot in non-

structural environment based on Mask-RCNN. * * *Computers* * * *and* * * *Electronics* * * *in* * * *Agriculture*, * * *163*, 104846.

URL: <https://linkinghub.elsevier.com/retrieve/pii/S0168169919301103>. doi: 10.1016/j.compag. 2019.06.001.

Zhang, Q., Karkee, M., & Tabb, A. (2019). The Use of Agricultural Robots in Orchard Management. In

*Robotics* * * *and* * * *automation* * * *for* * * *improving* * * *agriculture* (p. 28). Burleigh Dodds Science Publishing. (1st ed.).