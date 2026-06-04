## _Article_ 

## **Geo-Referenced Factor-Graph SLAM for Orchard-Scale 3D Apple Reconstruction and Yield Estimation** 

**Dheeraj Bharti[1] , Lilian Nogueira de Faria[1] , Luciano Vieira Koenigkan[1] , Luciano Gebler[2] Andrea de Rossi[2] and Thiago Teixeira Santos[1,] *** 

**,** 

- 1 Embrapa Agricultura Digital, Campinas 13083-886, Brazil; dheeraj.bharti@colaborador.embrapa.br (D.B.); lilian.faria@colaborador.embrapa.br (L.N.d.F.); luciano.vieira@embrapa.br (L.V.K.) 

- 2 Embrapa Uva e Vinho, Vacaria 95200-000, Brazil; luciano.gebler@embrapa.br (L.G.); andrea.derossi@embrapa.br (A.d.R.) 

- Correspondence: thiago.santos@embrapa.br 

## **Abstract** 

Accurate and spatially resolved yield estimation is a critical requirement for precision agriculture and orchard management. This paper presents a geometrically consistent, orchardscale apple yield estimation framework that integrates GNSS–visual-inertial odometry (VIO) fusion, deep learning-based object detection, multi-frame tracking, three-dimensional triangulation, and incremental factor-graph optimization. Camera poses are obtained using ZED GNSS–VIO fusion and subsequently refined using an iSAM2-based nonlinear smoothing approach that incorporates strong relative-motion constraints and soft global ENU (East-North-Up) translation priors. Apples are detected using a YOLO-based model and associated across frames via CoTracker3, enabling robust multi-view landmark reconstruction. Reprojection factors and landmark priors are incorporated into a unified nonlinear factor graph to jointly optimize camera trajectories and 3D apple positions. The reconstructed apples are spatially aggregated into a grid-based mass map, where individual fruit volumes are estimated assuming spherical geometry and converted to mass using density models. The resulting ENU-referenced yield plot provides a structured representation of orchard production variability. Experimental results demonstrate significant reductions in reprojection error after optimization and improved global consistency of the trajectory, leading to stable and spatially coherent 3D reconstructions. The proposed pipeline bridges perception, geometry, and optimization, providing a scalable solution for orchard-scale yield mapping and decision support in precision agriculture. 

**Keywords:** SLAM; visual odometry; iSAM2; 3D reconstruction; yield estimation 

Academic Editors: Alessandra Vinci and Daniela Farinelli 

Received: 25 February 2026 Revised: 20 March 2026 Accepted: 23 March 2026 Published: 30 March 2026 

**Copyright:** © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license. 

## **1. Introduction** 

Accurate and fine-grained estimates of fruit yield are central to decision-making in modern orchards, affecting harvest logistics, labor planning, storage capacity, and market strategy. Conventional yield estimation relies heavily on manual sampling and visual inspection, which are labor-intensive, subjective, and difficult to scale to commercial production. As a result, vision-based yield monitoring has attracted substantial attention, particularly for high-value crops such as apples. Recent advances in field robotics and precision agriculture have enabled data acquisition at orchard scale using mobile ground platforms equipped with cameras and navigation sensors [1,2]. However, achieving reliable yield estimation in real-world orchards remains challenging due to variable illumination, occlusions, fruit clustering, motion blur, and long trajectories spanning thousands of frames. 

_Agriculture_ **2026** , _16_ , 764 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

2 of 34 

A key limitation in many vision-only yield pipelines is the lack of geometric consistency across time. Frame-wise detectors can provide apple counts per image, but they suffer from double counting when fruit are observed repeatedly, and under-counting when fruit are missed in individual frames. Temporal association through multi-object tracking can reduce these issues, but tracking alone does not resolve geometric ambiguities, especially when motion is complex or when fruit appearance changes due to viewpoint and illumination. Robust orchard-scale estimation therefore benefits from combining detection and tracking with 3D reasoning, where fruit are reconstructed as landmarks and associated across frames via camera poses. 

In parallel, orchard mapping and navigation have progressed rapidly through the adoption of visual-inertial odometry (VIO), stereo depth, and GNSS. Nevertheless, pose estimates produced by such systems can drift, exhibit local inconsistencies, or show misalignment with global coordinate references. Several works have explored sensor fusion and global alignment strategies for agricultural platforms, emphasizing the need for reliable geo-referencing to support downstream tasks such as mapping, yield estimation, and decision support [3,4]. This motivates an optimization-based formulation that can reconcile local motion constraints, global positioning cues, and image measurements into a single consistent estimate. 

In this work, we present an orchard-scale pose and landmark refinement pipeline based on incremental factor-graph optimization [5]. Starting from fused raw poses (camerato-world) and ENU measurements, we (i) triangulate apple landmarks from multi-view 2D tracks, and (ii) jointly refine camera poses and apple landmarks using iSAM2 [6] with a graph comprising strong relative-motion constraints (between consecutive poses), soft ENU translation priors, and reprojection factors linking poses and landmarks. This formulation explicitly enforces geometric consistency across long sequences while remaining robust to outliers through robust loss models on priors and reprojection residuals. The approach builds on the broader trend of integrating robotic sensing and optimization for scalable agricultural monitoring [7–9]. 

## _1.1. Motivation and Challenges_ 

Orchard scenes present unique difficulties for vision-based mapping and fruit reconstruction. Apples often appear in dense clusters, are partially occluded by foliage, and exhibit low texture and specular highlights. Camera motion from ground vehicles introduces viewpoint changes and potential motion blur, while the orchard environment yields repetitive structures that can degrade purely visual localization. Additionally, GNSS readings in orchards may suffer from multipath and canopy attenuation, introducing bias and increased noise. These conditions demand a pipeline that (i) uses temporal association to maintain identity consistency, (ii) leverages multi-view geometry to resolve depth, and (iii) fuses relative and global constraints to stabilize long trajectories. 

## _1.2. Contributions_ 

The main contributions of this work are: 

- A factor-graph formulation to jointly refine camera poses and apple landmarks for orchard trajectories that combines strong raw relative-motion constraints, soft ENU translation priors (after displacement-based alignment), reprojection factors and a separate strong prior on the first pose only. It prevents the entire optimized trajectory and landmark map from drifting or rotating as a whole, thereby fixing the global reference frame of the solution. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

3 of 34 

- A robust landmark initialization strategy using multi-view triangulation from tracked apple observations, with quality gating and configurable view selection to control computational cost on long sequences. 

- A reproducible orchard-scale evaluation workflow that reports reprojection consistency and pose-change diagnostics, enabling systematic debugging and sensitivity analysis. 

## _1.3. Paper Organization_ 

The remainder of this paper is organized as follows. Section 2 reviews related work in fruit detection, tracking, agricultural sensing, and optimization-based mapping. Section 3 describes the proposed pipeline, including ENU alignment, landmark initialization, and the iSAM2 factor-graph formulation. Section 4 presents experimental results. Section 5 discusses the results and limitations. Finally, Section 6 concludes the paper and outlines future directions. 

## **2. Related Work** 

Orchard-scale yield estimation from vision has increasingly evolved from frame-wise counting into a mapping problem that requires (i) robust fruit perception under strong visual variability, (ii) reliable association to avoid double counting across time and viewpoints, and (iii) geometric reconstruction in a metric and often geo-referenced frame to support orchard analytics. In parallel, advances in SLAM and factor-graph optimization have enabled large-scale state estimation with heterogeneous sensors, motivating pipelines that couple perception with geometry rather than treating them as separate stages. This section reviews prior work most relevant to our end-to-end design—geo-referenced pose estimation (GNSS-VIO), detection and association for counting, multi-view 3D fruit localization, and SLAM back-end refinement—and positions our contribution within this landscape. 

## _2.1. Proximal Sensing Platforms and Orchard-Scale Yield Mapping_ 

Early orchard yield studies relied on limited-view sampling and hand-engineered image processing, which struggles to generalize across illumination, canopy structure, and phenological stage [10]. Large-scale monitoring requires systematic acquisition strategies and mobile platforms that can scan corridors with repeatable coverage [11,12]. Sensorrich platforms combining cameras with additional modalities (e.g., LiDAR or RGB-D) have enabled orchard mapping beyond per-image detection, supporting canopy/row structure estimation and yield-related spatial products [1,13,14]. Recent work has emphasized persistent mapping and dataset development for long-term orchard monitoring, including metric-semantic representations designed for repeated traversals [15]. In this context, our SEEmear platform and data collection protocol align with the broader trend toward proximal robotic sensing for permanent crops [16], while our pipeline specifically targets orchard-block fruit mapping from a single continuous run. 

## _2.2. Fruit Detection and Instance-Level Perception in Orchards_ 

Fruit detection remains the entry point for most vision-based yield pipelines, yet it is challenged by high instance density, foliage occlusion, and strong appearance variation. Deep detectors significantly improved robustness over classical feature/thresholding approaches and enabled practical fruit detection at scale [2,17]. Within agricultural detection literature, YOLO-style one-stage detectors are widely adopted due to favorable speed– accuracy trade-offs for embedded deployment, and recent architectural advances further improve feature aggregation and training dynamics [7,18]. For orchard-specific counting, apple detection is frequently paired with temporal integration and domain heuristics to mitigate re-detection and partial visibility [4,8,19]. Our work follows this lineage by using modern detection as a high-recall front-end, but differs in how detections are consolidated: 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

4 of 34 

we treat association and geometry as first-class components, ultimately validating fruit instances through 3D reconstruction and SLAM refinement. 

## _2.3. Association for Counting: Tracking-by-Detection and Orchard-Specific Pipelines_ 

Avoiding double counting requires associating repeated detections so that each physical fruit contributes once to the final estimate. The dominant multi-object tracking paradigm is tracking-by-detection, which links detections over time using motion models, overlap criteria, and/or appearance embeddings [20–22]. These methods have strong empirical performance in general MOT (Multi-Object Tracking) benchmarks, but orchard imagery introduces distinct failure modes: fruits are small, visually similar, frequently clustered, and subject to intermittent occlusion, all of which can increase identity fragmentation and ID switches [8,19]. Additionally, traversal patterns with turns and scanning both sides of a row produce abrupt viewpoint changes that can break IoU- and motion-based association. These challenges motivate alternative association primitives (beyond box overlap) and the integration of geometry for verification. Our evaluation of multiple trackers (including IoU/Hungarian baselines, SORT, and ByteTrack) reflects this broader literature, while our final design prioritizes association stability as a prerequisite for reliable multi-view triangulation and map-level de-duplication. 

## _2.4. Point Tracking for Robust Sssociation Under Occlusion and Viewpoint Change_ 

Point tracking has re-emerged as a powerful alternative to box-based association, particularly for small objects and scenes with repeated texture. Modern transformer-based point trackers can follow arbitrary points through occlusion and long temporal gaps, enabling association that is less sensitive to bounding box jitter and partial visibility [23]. CoTracker introduced joint multi-point tracking that models dependencies among trajectories, improving robustness over independent point tracking [24]. CoTracker3 further simplified the architecture and proposed a semi-supervised training strategy using pseudo-labeling on real videos, improving robustness while reducing reliance on synthetic supervision [25]. These developments directly match orchard conditions, where fruits are often partially occluded and appear in dense clusters. Accordingly, our pipeline uses point tracking (CoTracker3) to construct temporally coherent fruit tracks that serve as the association backbone for geometric reconstruction. 

## _2.5. Multi-View 3D Reconstruction, Bundle Adjustment, and Semantic Fruit Mapping_ 

Mapping-oriented yield estimation benefits from multi-view geometry: repeated observations can be consolidated by triangulating fruit into a 3D landmark, naturally reducing double counting and enabling spatial analytics. Video-based apple counting and mapping approaches have demonstrated the value of linking detections through time and projecting results into a common spatial frame [8,19]. More broadly, orchard monitoring research has explored spatio-temporal reconstruction and “4D agriculture” concepts, where spatial maps evolve over time [26]. Traditional structure-from-motion pipelines emphasize triangulation and global refinement via bundle adjustment; systems such as COLMAP exemplify robust multi-view reconstruction in generic settings [27]. Recently, neural scene representations (e.g., NeRF-based counting) have also been proposed to unify reconstruction and counting, highlighting an alternative direction for multi-view integration [9]. Our approach remains in the geometric regime: we triangulate fruit landmarks from tracked 2D observations under geo-referenced poses and then refine the joint pose–landmark configuration using factor-graph optimization, which is especially suitable for long orchard traversals with dense observation graphs. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

5 of 34 

## _2.6. SLAM, Factor Graphs, and Geo-Referenced Pose Estimation with GNSS-VIO_ 

Accurate 3D mapping requires reliable camera poses. Visual-inertial estimation provides strong short-term motion accuracy but drifts over long traversals unless anchored by global constraints [28–30]. In outdoor robotics, GNSS provides global position information and is increasingly fused with VIO/SLAM to obtain metric, drift-controlled trajectories suitable for mapping [31–33]. Factor-graph formulations provide a principled framework for combining heterogeneous measurements and priors in a single optimization problem [5]. iSAM2 extends this framework with incremental smoothing and efficient relinearization, enabling scalable SLAM back-ends for long sequences [6]. In our system, ZED Fusion API provides per-frame geo-referenced poses in a consistent world frame [34], which we treat as a globally anchored initialization. We then apply iSAM2 as the SLAM back-end to jointly refine poses and fruit landmarks using dense reprojection constraints, improving multi-view consistency at orchard scale. 

## _2.7. Evaluation Practices for Detection, Tracking, Reconstruction, and Orchard-Scale_ 

## _Yield Products_ 

Evaluation of orchard yield pipelines typically combines detection quality, association stability, geometric consistency, and final counting or yield accuracy. For tracking, metrics that decouple detection and identity behavior are critical for diagnosing whether a tracker is suitable for downstream geometric aggregation. HOTA explicitly balances detection and association accuracy and has become a standard for analyzing tracker behavior under identity fragmentation and ID switches [35]. In agricultural vision, however, evaluation is rarely limited to tracking alone. Recent orchard-scale systems increasingly report a combination of detection or tracking metrics, geometric reconstruction quality, and tasklevel outputs such as fruit count, size, or spatial yield products. 

For example, Wang et al. combined Grounded-SAM2-based MOTS, structure-frommotion, and DeepSDF-based fruit completion for UAV-based monocular 3D panoptic mapping in orchards and evaluated the system using MOTS metrics, Chamfer distance for 3D shape reconstruction, and diameter error under different occlusion levels [36]. Their study is relevant because it demonstrates a multi-level evaluation strategy spanning tracking, reconstruction, and orchard deployment. Nevertheless, its main objective is fruit shape completion and phenotyping from UAV imagery, whereas our work focuses on ground-robot, geo-referenced orchard-scale yield mapping with explicit SLAM backend refinement of poses and landmarks. In particular, our pipeline differs by integrating GNSS–VIO initialization, incremental factor-graph smoothing, multi-view triangulation, and geo-referenced orchard products such as density and mass maps. 

Similarly, Pichhika et al. evaluated a YOLOv8s with EKF tracking pipeline for mango yield estimation using both harvest count and manual labeling count, showing the importance of validating counting systems not only with image-level annotations but also with operational agronomic ground truth [37]. This is closely aligned with our emphasis on orchard-level validation. However, their system remains fundamentally a 2D detection-andtracking counting pipeline, whereas our method reconstructs explicit 3D fruit landmarks, refines them jointly with the camera trajectory through iSAM2, and produces geo-referenced orchard-scale outputs beyond counting alone. 

Other closely related studies also reinforce this multi-layer evaluation view. Liu et al. [38,39] combined deep learning, tracking, and structure-from-motion for robust fruit counting and later extended this idea to monocular fruit counting and mapping with semantic data association, highlighting the importance of 3D reasoning for reducing double counting across views. Villacrés et al. [40] compared tracking-by-detection algorithms for apple orchard production estimation, showing that counting accuracy is 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

6 of 34 

highly sensitive to association quality under occlusion and variable illumination. For sizeoriented evaluation, Gené-Mola et al. [41,42] compared photogrammetry-based apple size estimation methods under occlusion and later studied amodal segmentation for robust on-tree apple size estimation, demonstrating that geometric and occlusion-aware metrics are essential whenever yield products depend on fruit size rather than count alone. 

Our evaluation follows this same multi-layer logic but is tailored to a geo-referenced SLAM-based yield pipeline. We analyze association quality using MOT metrics, verify geometric consistency through reprojection statistics and triangulation validity, and report orchard-scale outputs enabled by the refined 3D landmark map, including geo-referenced density surfaces, fruit counts, and mass proxies. In this sense, our work sits at the intersection of agricultural MOT evaluation, multi-view fruit mapping, and SLAM-based orchard-scale yield analytics. 

## _2.8. Positioning of This Work_ 

Prior orchard yield systems often excel in either per-frame detection or platform localization, but integrating (a) occlusion-robust association in dense fruit clusters with (b) geo-referenced 3D fruit reconstruction and (c) SLAM back-end refinement at orchard scale remains less common in a single deployable pipeline. Our work addresses this gap by coupling point-tracking-based association (CoTracker3) with multi-view triangulation under GNSS-VIO geo-referenced poses and by refining the joint pose–landmark state with iSAM2. This design yields a unified orchard-scale map from which counting, spatial density visualization, and size-derived yield proxies can be derived in a consistent global frame. 

## **3. Materials and Methods** 

## _3.1. Overview End-to-End Sensing and Reconstruction Workflow_ 

Figure 1 below summarizes the complete end-to-end workflow, from on-board sensing to orchard-level outputs. The pipeline consumes synchronized stereo vision and RTKGNSS streams, produces a globally referenced camera trajectory via visual-inertial and GNSS data fusion (ZED Fusion), associates apple observations over time using detectionconditioned tracking, reconstructs a 3D apple landmark map by multi-view triangulation, and refines the joint pose–landmark solution using incremental bundle adjustment (iSAM2). The final products include refined camera poses, a refined geo-referenced 3D apple map, orchard-level fruit count, and a size-derived yield proxy in terms of total weight estimates. Given an image sequence _{It}t[T]_ =1[and GNSS fixes] _[ {]_[(] **[g]** _[n]_[,] _[ τ][n]_[)] _[}] nN_ = _g_ 1[,][the workflow pro-] ceeds through the following stages: 

1. Sensors and data acquisition (ZED X + RTK-GNSS): the ZED X provides time-stamped rectified RGB frames (left camera stream used for detection and tracking), while an RTK-capable GNSS receiver provides global geodetic position fixes. Both streams are logged during a single continuous traversal that covers multiple orchard rows on both sides and includes headland turns. 

2. Pose estimation and geo-referencing (ZED Fusion: GNSS + VIO): ZED Fusion fuses stereo visual-inertial odometry with GNSS constraints to estimate a globally referenced camera trajectory in the ZED `WORLD` frame. Each frame _t_ is associated with a fused pose **T** _WC[t][∈][SE]_[(][3][)][ (Equation (][5][)) below, enabling consistent projection geometry.] Because the `WORLD` frame is geo-referenced, the reconstructed 3D landmarks inherit global consistency and can be exported to ENU/ECEF/LLA for mapping. 

3. Apple detection and temporal association (SLAM Frontend): apples are detected per-frame using YOLOv9 and filtered by confidence and non-maximum suppression (Section 3.5). Only detections with confidence above _τ_ conf = 0.55 are used. CoTracker3 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

7 of 34 

then operates in online mode, periodically refreshing queries every 10 frames, to generate temporally coherent tracks representing candidate unique apples. 

4. SLAM Backend and 3D reconstruction (iSAM2 incremental bundle adjustment): for each track _Tk_ , a single 3D apple center **X** _k_ is initialized by multi-view triangulation using the camera intrinsics **K** and fused poses _{_ **T** _WC[t][}]_[.][Robust estimation (RANSAC)] and geometric validity checks are applied, including cheirality, reprojection gating, minimum parallax, and a maximum sensing range (Section 3.8). 

The initial pose and landmark configuration are further refined using iSAM2 on a factor-graph formulation dominated by reprojection constraints. This step improves global multi-view consistency across the orchard traversal and yields refined poses and a refined landmark map that serve as the basis for counting and yield analytics. 

5. Outputs (mapping, counting, and weight proxy): the final outputs are: (i) refined camera poses, (ii) a refined geo-referenced 3D apple map _{_ **X** _k}_ suitable for visualization and GIS export, (iii) the orchard-level apple count _N_ apples (Equation (31)), and (iv) a size-derived weight proxy computed from reconstructed radii via a density-based model (Equations (37) and (38)). 

This organization makes the data flow explicit: sensor streams _→_ fused geo-referenced poses _→_ detection and tracking (SLAM front-end) _→_ iSAM2 refinement (SLAM back-end) and 3D reconstruction _→_ orchard-scale products. 

**Figure 1.** Complete pipeline of orchard-scale 3D reconstruction and yield prediction. ZED X and RTK-GNSS provide synchronized sensory streams; ZED Fusion produces a geo-referenced trajectory; YOLOv9 and CoTracker3 generate object tracks; iSAM2 performs incremental bundle adjustment to refine poses and landmarks for multi-view triangulation of 3D landmarks; final outputs include refined camera poses, refined 3D apple map, count, and weight proxy. 

## _3.2. Field Site and Platform_ 

Data is collected in an apple orchard located at the Temperate Climate Fruit Growing Experimental Station (EFCT)—Embrapa Grape and Wine, Vacaria, Brazil in March 2025. The cultivar considered in this work is Fuji. The orchard block also contains Gala rows used primarily as pollinators, although Gala harvesting has been completed before data acquisition, and consequently these rows contain negligible fruit observations in the recorded sequences. The orchard is organized in rows with an approximate inter-row spacing of around 3.5 m between the Fuji and Gala rows. 

A single continuous run is performed in the afternoon, covering approximately 500 m and traversing four Fuji rows in a continuous path that includes turns and headland maneuvers. The scan covers both sides of the row during traversal, producing strong viewpoint changes that are representative of operational orchard scouting and that stresstest long-horizon association and geometric reconstruction. 

Figure 2 below shows the complete acquisition path and the specific palmette-trained plot used for analysis. Figure 2a shows the full GNSS track of the data collection. Figure 2b,c show progressively closer views of the palmette orchard, highlighting the maneuvering and inter-row translation present in the trajectory. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

8 of 34 

**==> picture [11 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a )<br>**----- End of picture text -----**<br>


( **b** ) ( **c** ) 

**Figure 2.** System path across EFCT orchards performed in March 2025. ( **a** ) The entire path (shown as yellow dots) recorded by the GNSS system. ( **b** ) Orchard under the palmette training. ( **c** ) Closer view of the palmette orchard, showing maneuvering and inter-row translation. 

All field data is collected using the SEEmear mobile sensing platform shown in Figure 3 below, described in detail in [16]. In brief, SEEmear integrates an on-board compute unit and a co-located sensing head combining: (i) a ZED X stereo camera (wide-angle lens) used for synchronized image acquisition and visual-inertial odometry (VIO), and (ii) an RTK-capable GNSS receiver that provides geodetic fixes (latitude, longitude, altitude). RTK correction is performed using a base station and the trajectory is post-processed (PPK). This work uses the left camera stream as the monocular input for detection and tracking; rectification is performed by the ZED X system during recording. 

Apple tree training systems strongly shape plant architecture and canopy porosity, directly affecting light interception, fruit exposure, and the degree of self-occlusion in image-based sensing. Classical central leader systems maintain a dominant main axis with lateral branches, forming a relatively voluminous canopy, whereas spindle (slender axis) systems adapt the central leader to higher-density plantings by promoting a narrower canopy with short, renewable laterals and a higher proportion of fruiting structures close to the axis [43,44]. More intensified wall-like architectures can also be obtained with multileader training, where multiple vertical axes per plant are supported to form a continuous productive wall with improved light distribution but typically increased within-canopy overlap when viewed from ground-level platforms [45,46]. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

9 of 34 

**==> picture [193 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a ) ( b )<br>**----- End of picture text -----**<br>


**Figure 3.** SEEmear sensing platform and field deployment (adapted from [16]). ( **a** ) Front view of the integrated sensing head, comprising the RTK-GNSS antenna, stereo camera units with embedded IMUs, rover-mounted compute module, and protective housing. ( **b** ) Deployment on a tractor during orchard acquisition, illustrating corridor-level operation for row scanning; the elevated mast geometry enables simultaneous imaging of both sides of the orchard row. 

In the EFCT block used in this work, the scanned rows are not all trained identically; in particular, the final scanned row follows a different training configuration with denser canopy structure. This difference is relevant for interpretation of row-level results because denser architectures increase fruit occlusion and reduce the effective visibility time of individual fruits, which can lower track continuity and landmark recall under a singlepass traversal. 

## _3.3. Data Acquisition Protocol and GNSS-VIO Fusion_ 

During acquisition, the platform traversed orchard corridors at approximately 5 km/h. Video frames are recorded at approximately 30 fps and GNSS fixes at 5 Hz. The run produced approximately 29,000 time-stamped frames and a synchronized fused camera pose sequence obtained from GNSS-VIO fusion. 

The camera provides an image stream 

**==> picture [277 x 13] intentionally omitted <==**

with timestamps _tt_ at an average rate _f_ cam. The GNSS provides geodetic fixes 

**==> picture [290 x 16] intentionally omitted <==**

where ( _φ_ , _λ_ , _h_ ) denote latitude, longitude, and altitude, at a nominal rate _f_ gnss = 5 Hz. ZED Fusion combines VIO with GNSS to generate a metric, geo-referenced camera trajectory in a consistent world reference [34]. A central property of our workflow is that 3D apple landmarks are reconstructed directly in this geo-referenced `WORLD` coordinate system, enabling GIS-ready outputs without a separate post-hoc alignment stage. Accordingly, the aim of this work is not to benchmark alternative odometry modalities such as LiDAR and inertial fusion, but to refine a practical geo-referenced visual-inertial trajectory for fruit landmark reconstruction and yield mapping. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

10 of 34 

## 3.3.1. Temporal Synchronization 

The fusion module aligns camera and GNSS measurements in time by associating each image timestamp _tt_ with the closest GNSS timestamp _τn_ : 

**==> picture [251 x 15] intentionally omitted <==**

This nearest-neighbor association is required because the camera ( _f_ cam) and GNSS sampling rates ( _f_ gnss) are not equal to each other, i.e., _f_ cam = _f_ gnss. 

## 3.3.2. Spatial Alignment and Calibration Transform 

VIO produces a camera trajectory in a local (arbitrary) coordinate system, denoted as frame _V_ (VIO world). GNSS provides positions in a global geodetic system. ZED Fusion estimates a rigid alignment that maps the VIO world to a GNSS-consistent world frame _W_ : 

**==> picture [283 x 31] intentionally omitted <==**

The rigid transform estimated by the upstream fusion stage accounts for the sensorframe alignment required to express the camera trajectory in the geo-referenced `WORLD` frame. Accordingly, the iSAM2 back-end in this work refines already fused camera poses and does not separately re-estimate the GNSS-antenna-to-camera lever-arm inside the factor graph. Any such extrinsic handling is therefore inherited from the ZED Fusion calibration and fusion pipeline rather than modeled as an additional optimization variable here. 

After fusion, each camera pose is expressed in the fused `WORLD` frame _W_ and inherits geo-referencing; consequently, any 3D point reconstructed in the same `WORLD` frame also inherits this global reference. 

## 3.3.3. Fused Camera Pose Convention 

Let the fused camera pose at time _t_ be 

**==> picture [264 x 31] intentionally omitted <==**

mapping camera-frame coordinates to `WORLD` coordinates. The corresponding inverse (WORLD-to-camera) transform is 

**==> picture [363 x 31] intentionally omitted <==**

The camera center in `WORLD` coordinates is 

**==> picture [232 x 13] intentionally omitted <==**

## _3.4. Camera Model and Projection Geometry_ 

We assume a pinhole camera model with intrinsics 

**==> picture [241 x 43] intentionally omitted <==**

The intrinsics ( _fx_ , _fy_ , _cx_ , _cy_ ) are obtained from the ZED X calibration corresponding to the acquisition configuration. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

11 of 34 

For frame _t_ , the world-to-camera projection matrix is 

**==> picture [259 x 14] intentionally omitted <==**

Given a homogeneous 3D point in `WORLD` coordinates **X**[˜] = [ _X_ , _Y_ , _Z_ , 1] _[⊤]_ , the homogeneous image projection is 

**==> picture [281 x 31] intentionally omitted <==**

## _3.5. Apple Detection Using YOLOv9_ 

We detect apples in each rectified RGB frame using YOLOv9. YOLOv9 was selected because the primary objective was to build a practical, end-to-end orchard pipeline with a favorable speed–accuracy trade-off and straightforward deployment on embedded robotic hardware. We therefore prioritized a detector family that is widely adopted in real-time agricultural perception, rather than conducting a broader architectural benchmark against transformer-based detectors. Such comparisons remain relevant future work, particularly for small-object detection in dense and highly cluttered canopy regions. In the present work, the role of the detector is to provide reliable initializations for the tracking module (Section 3.6), typically obtained from frames captured during favorable viewing geometries arising from camera translation. YOLOv9 is used directly for inference without additional training. For each frame _It_ , YOLO outputs a set of axis-aligned bounding boxes 

**==> picture [251 x 14] intentionally omitted <==**

with confidence score _si[t]_[.][We retain detections satisfying] 

**==> picture [220 x 13] intentionally omitted <==**

with _τ_ conf = 0.55. Non-maximum suppression (NMS) is applied with IoU threshold _τ_ nms = 0.45. 

The pixel center of the _i_ -th detection in frame _t_ is 

**==> picture [267 x 48] intentionally omitted <==**

In the present pipeline, illumination artefacts may still reduce detector recall locally, but their effect on the final 3D map is partially mitigated by temporally coherent association in the tracker and geometric consistency checks in the downstream stages. 

## _3.6. Temporal Association and Tracking (CoTracker3)_ 

The objective of tracking is to assign a stable identity to each physical apple over its visible duration, producing a set of tracks _{Tk}k[K]_ =1[.][This][is][challenging][in][orchard] environments due to repeated appearance patterns (many visually similar apples), partial occlusions by foliage, and rapid viewpoint changes around turns and during scanning of both sides of the rows. 

## 3.6.1. Tracking Configuration (Online Mode with Periodic Queries) 

CoTracker3 is employed in online mode. Only detections satisfying _si[t][≥]_[0.55 are used] to initialize tracking hypotheses. To maintain robustness over long sequences while keeping computation bounded, we periodically refresh the tracker state by providing new query 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

12 of 34 

detections every 10th frame. The value was chosen based on the speed of data acquisition, the frame rate, and the visibility of the landmarks in the field of view. This online update mechanism supports continued association through viewpoint changes while avoiding the need to re-process the entire sequence offline. 

## 3.6.2. Track Representation and Minimum Support 

A track _k_ is represented as an ordered set of observations across frames: 

**==> picture [248 x 14] intentionally omitted <==**

where Ω _k ⊆{_ 1, . . . , _T}_ indexes frames where apple _k_ is visible. Tracks shorter than _L_ min = 5 frames are discarded prior to triangulation to ensure sufficient multi-view constraints. Since each row side is traversed once in a single pass, apples naturally leave the camera field of view as the platform advances; hence tracks terminate when the apple exits the image rather than by long-term re-identification. 

## _3.7. Tracker Selection Protocol and Benchmark_ 

To quantify association quality, we evaluate all trackers using `TrackEval` on a representative orchard segment under the MOTChallenge 2D bounding box configuration with IoU threshold 0.5. We report Higher-Order Tracking Accuracy (HOTA) and its decomposition into detection accuracy (DetA) and association accuracy (AssA), the CLEAR MOT metric MOTA, and identity-based metrics (IDF1, IDR, IDP). Table 1 below reports the comparison results for the different trackers. 

CoTracker3 achieves the highest overall tracking quality according to HOTA (42.63%), substantially exceeding the Hungarian baseline (28.13%) and both SORT and ByteTrack (11.98% and 12.34%, respectively). The HOTA decomposition shows that CoTracker3 is particularly effective at maintaining identity over time: AssA reaches 55.97%, compared to 20.42% for Hungarian, 24.41% for SORT, and 38.74% for ByteTrack. Identity metrics further corroborate this behavior: CoTracker3 attains an IDF1 score of 50.75%, whereas Hungarian, SORT, and ByteTrack reach 26.63%, 8.91%, and 6.56%, respectively. 

**Table 1.** Tracking performance using TrackEval (MOTChallenge 2D box configuration with IoU threshold 0.5). All values are percentages except for the last two columns. HOTA, DetA, and AssA are Higher-Order Tracking Accuracy components; MOTA is the CLEAR MOT accuracy; IDF1 is the identity F1 score. Best results in bold. 

|**Tracker**|**HOTA**|**DetA**|**AssA**|**MOTA**|**IDF1**|**#IDs**|**#GT IDs**|
|---|---|---|---|---|---|---|---|
|Hungarian|28.13|**40.55**|20.42|**25.44**|26.63|2146|253|
|SORT|11.98|6.05|24.41|3.93|8.91|402|253|
|ByteTrack|12.34|3.94|38.74|3.78|6.56|90|253|
|CoTracker|**42.63**|33.56|**55.97**|3.04|**50.75**|320|253|



In contrast, the Hungarian baseline achieves higher MOTA (25.44%), driven by fewer false positives, but exhibits severe identity fragmentation, as evidenced by the large number of predicted track IDs (2146) relative to the 253 ground-truth identities. For downstream geometric aggregation, identity persistence is essential because longer and cleaner trajectories provide stronger multi-view constraints and more reliable triangulation. Therefore, we adopt CoTracker as the tracking component for 3D reconstruction and final counting in the main pipeline, as justified. 

This behavior reflects the limitations of MOTA in densely occluded orchard scenes. Because MOTA heavily penalizes missed detections, false positives, and identity switches, it can remain low even when a tracker provides trajectories that are sufficiently stable for 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

13 of 34 

downstream multi-view geometry. In our application, association persistence is more important than frame-wise detection purity, since longer and cleaner tracks provide stronger constraints for triangulation and SLAM back-end refinement. 

Figure 4 above provides a qualitative illustration of the tracking behavior in a representative orchard segment. Figure 4a–c show the CoTracker3 outputs of the ZED left camera images with projected tracks and persistent apple IDs. The visualization highlights that CoTracker3 maintains identity continuity across successive frames despite dense fruit clusters, partial occlusions, and appearance similarity, thereby providing longer and cleaner trajectories for triangulation and SLAM back-end refinement. 

**==> picture [262 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a ) ( b ) ( c )<br>**----- End of picture text -----**<br>


**Figure 4.** Qualitative example of apple tracking with CoTracker3 on consecutive ZED left-camera frames. ( **a** – **c** ) The images row shows the corresponding tracking overlays with unique track IDs assigned to apple instances. 

## _3.8. 3D Reconstruction by Multi-View Triangulation_ 

Given a track _Tk_ , we estimate a single 3D apple center **X**[˜] _k_ in `WORLD` coordinates using multi-view triangulation under fused GNSS-VIO poses. It is important to note that the present reconstruction is not obtained from a single-frame stereo depth value assigned independently to each detection. Instead, each apple center is estimated by pose-based multi-view triangulation from tracked 2D observations across multiple frames. As a result, geometric reliability at larger camera–fruit distances is controlled through multi-view conditioning rather than raw stereo disparity alone, and weak configurations are subsequently filtered by cheirality, reprojection gating, parallax thresholding, and a maximum camera–fruit distance constraint. 

## 3.8.1. Linear Multi-View Triangulation (DLT) 

For each observation ( ˜ **u** _[t]_ , **P** _[t]_ ), the homogeneous triangulation constraints are 

**==> picture [283 x 14] intentionally omitted <==**

Stacking constraints over frames _t ∈_ Ω _k_ yields 

**==> picture [219 x 12] intentionally omitted <==**

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

14 of 34 

The solution is obtained from the right-singular vector corresponding to the smallest singular value: 

**==> picture [248 x 19] intentionally omitted <==**

and dehomogenization yields **X** _k_ = [ _Xk_ , _Yk_ , _Zk_ ] _[⊤]_ . 

## 3.8.2. Cheirality Constraint 

For frame _t_ , the 3D point in camera coordinates is 

**==> picture [242 x 14] intentionally omitted <==**

and we enforce _ZC[t][>]_[ 0 in inlier views to ensure the point lies in front of the camera.] 

## 3.8.3. Reprojection Error 

The reprojection of **X**[˜] _k_ into frame _t_ yields ( ˆ _u[t]_ , _v_ ˆ _[t]_ ) via Equation (10). The reprojection error is 

**==> picture [274 x 19] intentionally omitted <==**

## 3.8.4. Robust Triangulation via RANSAC and Geometric Gating 

To mitigate outliers induced by tracking jitter and partial occlusions, we apply RANSAC over minimal subsets of views. For a hypothesis **X** , the inlier set is 

**==> picture [300 x 14] intentionally omitted <==**

where _τ_ reproj = 10 pixels. We perform RANSAC iterations, retain the hypothesis maximizing _|I_ ( **X** ) _|_ , and re-triangulate using all inliers. 

## 3.8.5. Parallax (Baseline) Quality Filtering 

Triangulation becomes ill-conditioned under small baselines. For frames _ta_ , _tb_ , define viewing rays 

**==> picture [284 x 26] intentionally omitted <==**

and parallax 

**==> picture [242 x 19] intentionally omitted <==**

We retain reconstructions only if max _a_ , _b∈I θab ≥ θ_ min with _θ_ min = 1.2 _[◦]_ . 

## _3.9. SLAM Refinement via iSAM2 Incremental Bundle Adjustment_ 

Although ZED Fusion yields a geo-referenced trajectory, long orchard traversals with turns, partial occlusions, and repeated structure can still introduce residual geometric inconsistency between camera poses, 2D observations, and triangulated 3D landmarks. Figure 5 below illustrates the effect of successive levels of refinement on the estimated trajectory. Figure 5a shows the complete orchard path obtained using only visual–inertial odometry, which exhibits substantial drift. Figure 5b shows the trajectory after GNSS fusion, which is geo-referenced but still contains enough residual geometric error to produce noticeable reprojection inconsistency over long traversals. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

15 of 34 

**==> picture [171 x 213] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a )<br>aemscs =:> SVKosa,< yasgiNS 3 —&SSSE0»LEeS owi -a6“SEAOo’eyrs, "g cs<br>N)BsoS 8g B&Vo gQA 3 xaxy y bsXHO 8 ‘<br>RgiS©m0&Oom aGg2 bey£,0©SaS6~ ‘Qtaaaal~oFoy Ee)Abyaixq otyaawy“Hy bna:nowqLab @oa<br><a Le) as holn lo of<br>eeC‘a‘o csaooG aLe‘7s< &aaaa* a xLnLyLy wyaaala4A isziLn aB_4A3Gj4<br>5 A +4)Fs 6<br>FowDyog : “g‘g] aaaf Kj a ,cf a<br>;<br>va bs -oy isaa:al Yi¥ 3A<br>‘s5ag ig aa 44HU6 4; a<br>¥ ey<br>e v B Vi ¥ ,<br>SyCAiv7,i ra 4 HhH fsa iaiF,<br>F C= 5S anFe SsCs 9 ome eat "3 Sprya<br>( b ) ( c )<br>**----- End of picture text -----**<br>


**Figure 5.** Comparison of camera trajectory estimates across the orchard. ( **a** ) VIO-only trajectory, showing pronounced drift over the full traversal. ( **b** ) ZED Fusion (GNSS-VIO) trajectory in the geo-referenced `WORLD` frame; although globally anchored, residual multi-view inconsistency remains (mean reprojection error 40.31 px). ( **c** ) iSAM2-refined trajectory after incremental bundle adjustment using reprojection constraints, yielding a substantially tighter solution (mean reprojection error 8.74 px) suitable for orchard-scale 3D reconstruction and mapping. 

To better understand this error, consider an apple detected in an image. The detector provides its image location in pixels, here approximated by the center of the bounding box. Using the estimated camera pose and the reconstructed 3D landmark position, this 3D apple can be projected back onto the image plane. If the projected pixel location does not coincide with the detected pixel location, the difference is called the reprojection error. Although it is measured in image pixels, its geometric effect can be much larger in 3D space: a small angular error at the camera can correspond to several centimeters, or even tens of centimeters, of spatial displacement when the fruit is several meters away. Over long orchard traversals, these errors accumulate and degrade the global consistency of both the trajectory and the reconstructed apple landmarks. 

Figure 5c shows the refined poses after optimization, resulting in a more accurate and globally consistent orchard representation. We therefore refine the joint solution using incremental bundle adjustment based on iSAM2, which we treat as the SLAM back-end of our system: the front-end provides data association (tracks) and initial geometry (trian- 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

16 of 34 

gulated landmarks), while the back-end enforces global consistency through multi-view reprojection constraints, relative-motion constraints, and soft geo-referenced pose priors. 

3.9.1. SLAM Formulation: States, Measurements, and Factor Graph Let _{_ **T** _WC[t][}] t[T]_ =1[denote camera poses and] _[ {]_ **[X]** _[k][}] k[N]_ =1[denote 3D apple landmarks,][both] expressed in the fused geo-referenced `WORLD` frame _W_ . The SLAM state is 

**==> picture [275 x 19] intentionally omitted <==**

The measurement set consists of: 

1. 2D landmark observations **z** _t_ , _k_ = [ _ut_ , _k_ , _vt_ , _k_ ] _[⊤]_ obtained from the tracked detection centers (Section 3.6); 

2. relative-motion constraints between consecutive poses, derived from the fused/raw trajectory; 

3. absolute ENU-derived translation priors associated with each pose, obtained from the geo-referenced ZED Fusion trajectory. 

Each observation ( _t_ , _k_ ) yields a reprojection constraint 

**==> picture [245 x 13] intentionally omitted <==**

where _π_ ( _·_ ) is the pinhole projection (Equation (10)), **K** are camera intrinsics, and **T** _CW[t]_[= (] **[T]** _WC[t]_[)] _[−]_[1][.][Defining the residual] 

**==> picture [267 x 13] intentionally omitted <==**

the reprojection cost is 

**==> picture [269 x 25] intentionally omitted <==**

where _O_ is the set of valid track observations and Σ _t_ , _k_ is the image-space noise covariance. 

In addition, the relative motion between consecutive poses is constrained using strong between-pose factors. If **Z** _t_ , _t_ +1 denotes the relative motion measurement between poses _t_ and _t_ + 1, the corresponding residual is 

**==> picture [283 x 19] intentionally omitted <==**

which preserves local trajectory consistency. 

Finally, each pose is softly constrained by an ENU-derived absolute translation prior. Let[¯] **t** _t_ denote the ENU translation associated with pose _t_ from the fused geo-referenced trajectory. Then the prior residual may be written as 

**==> picture [240 x 13] intentionally omitted <==**

where **t** _t_ is the translation component of **T** _WC[t]_[.][In implementation, this is applied as a pose] prior with a very large rotational covariance, so that the prior acts effectively as a soft translation-only constraint. Because the ENU term is not enforced as a hard positional constraint, the optimizer can rely more heavily on the between-pose relative-motion factors and the dense reprojection constraints when the geo-referenced measurements become locally less reliable. Consequently, the factor graph does not eliminate GNSS degradation altogether, but it reduces the propagation of such errors by balancing global translation cues with local geometric consistency. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

17 of 34 

In addition, each initialized landmark is associated with a prior centered at its DLTbased initialization, which stabilizes the optimization and limits large deviations for sparsely observed landmarks. 

Robustness to outliers is handled using a Huber loss on the reprojection factors, which reduces the influence of imperfect detections, tracking jitter, and partial occlusions. In the implementation used for the reported experiments, the Huber parameter is set to _k_ = 1.345. The ENU translation priors and the first-pose gauge prior are modeled as Gaussian pose priors; robust ENU priors can also be used when required. 

The resulting graph is therefore a coupled pose–landmark factor graph in which pose nodes **T** _WC[t]_[and landmark nodes] **[ X]** _[k]_[are connected by reprojection factors, pose nodes are] linked to one another by relative-motion factors, and each pose is also associated with a soft ENU translation prior. In our setting, this graph is highly observation-rich because apples are tracked across many frames, producing multiple constraints per landmark. In Figure 6 above, we show a part of the factor graph with the variables and factors along with the generalised objective, where, _r f_ is the residual associated with factor _f_ and Σ _f_ is its covariance matrix. The function _ρ_ ( _·_ ) denotes an optional robust loss, for example, Huber loss for reprojection factors in our case. 

**==> picture [388 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Strong<br>first-pose<br>prior T 1 T 2Between factors T 3 T 4 T 5 Tt · · · Graph contents State: Factors X =  {Tt ,  Xk}<br>1. Prior( T 1)<br>2. Between( Tt ,  Tt +1)<br>Soft ENU translation priors 3. ENU prior( Tt )<br>4. Prior( Xk )<br>Reprojection factors Objective 5. Reproj( Tt ,  Xk ,  z t , k )<br>· · · min X [∑] f ρ � ∥r f ∥ [2] Σ [−] f [1] �<br>X 1 X 2 X 3 X 4 Xk<br>Landmark priors<br>**----- End of picture text -----**<br>


**Figure 6.** Factor graph used for pose–ENU–landmark optimization in the proposed iSAM2 back-end. Circular nodes denote variables and square nodes denote factors. Pose variables _Tt_ are connected by strong between factors that preserve local motion consistency. Each pose is also associated with a soft ENU translation prior, while the first pose is anchored by a strong prior to remove gauge freedom. Landmark variables _Xk_ are initialized with landmark priors and connected to pose variables through reprojection factors induced by tracked apple 2-D observations _zt_ , _k_ . 

- 3.9.2. Front-End/Back-End SLAM Coupling in Our Pipeline 

Our overall system follows a classical SLAM decomposition: 

- Front-end (data association and initialization): YOLOv9 detects apples; CoTracker3 produces temporally consistent tracks _Tk_ ; each track is initialized as a 3D landmark via robust multi-view triangulation (Section 3.8) subject to cheirality, reprojection gating, and parallax constraints. These steps provide both the measurement correspondences ( _t_ , _k_ ) and an initial **X** _k_ . 

- Back-end (global consistency/bundle adjustment): iSAM2 refines _{_ **T** _WC[t][}]_[ and] _[ {]_ **[X]** _[k][}]_ jointly by minimizing the combined reprojection, relative-motion, and ENU-prior objective, thereby improving global consistency across long sequences and turns. 

This coupling is particularly suitable for orchards: the visual scene is highly repetitive, with similar foliage, fruit appearance, and row structure, so robust association is essential. Once stable correspondences are available, global reprojection consistency becomes a strong geometric cue that can correct residual local drift accumulated by the front-end trajectory estimate. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

18 of 34 

## 3.9.3. Incremental Optimization with iSAM2 

Direct batch bundle adjustment over all poses and landmarks scales poorly with orchard-length trajectories. iSAM2 performs incremental smoothing and mapping by updating the solution as new variables and factors are introduced. 

Given a current estimate _X_[ˆ] , each nonlinear factor residual is linearized around _X_[ˆ] : 

**==> picture [263 x 14] intentionally omitted <==**

where _δ_ is a perturbation in the tangent space of the state (poses in se(3) and landmarks in R[3] ), and **J** _t_ , _k_ is the Jacobian of the projection residual with respect to the connected variables. Stacking all linearized factors yields the sparse least-squares problem 

**==> picture [233 x 18] intentionally omitted <==**

whose sparsity directly reflects the factor graph topology. 

iSAM2 maintains a Bayes tree representation of this factorization and performs localized relinearization and partial re-factorization whenever new factors are introduced. In our pipeline, each new frame contributes: 

- a new pose node **T** _WC[t]_[initialized from ZED Fusion,] 

- strong relative-motion factors linking **T** _WC[t]_[to adjacent poses,] 

- a soft ENU-derived translation prior associated with **T** _[t]_ 

   - _WC_[,] 

- reprojection factors connecting **T** _WC[t]_[to existing landmarks,] 

- and, when a new apple track is created and passes the geometric checks, a new landmark node **X** _k_ with its associated reprojection factors. 

This incremental update pattern corresponds to online SLAM: mapping (landmark refinement) and smoothing (pose refinement) proceed together as observations arrive. 

## 3.9.4. Geo-Referenced Anchoring and Gauge Handling 

Bundle adjustment is defined up to a gauge freedom unless explicitly anchored. In our graph, this is handled by applying a strong prior to the first pose, which fixes the reference frame of the optimization. This gauge prior serves a different purpose from the ENU priors and the relative-motion constraints. The first-pose prior removes the global ambiguity of the optimization, the relative-motion factors preserve local trajectory consistency, and the soft ENU translation priors provide global positional guidance throughout the trajectory. Together, these constraints ensure that the refined solution remains in the same geo-referenced coordinate frame used for orchard mapping outputs. 

## 3.9.5. Practical Role of SLAM Refinement in Orchard-Scale Reconstruction 

In the proposed pipeline, iSAM2 refinement acts as a consistency-enforcing backend that: 

- reduces accumulated multi-view inconsistency between the fused trajectory and trackderived 2D measurements, 

- stabilizes landmark positions by exploiting repeated observations across multiple frames, 

- improves turn segments by globally distributing reprojection corrections across connected poses and landmarks, 

- reduces the effect of residual geo-referencing drift through soft ENU translation priors on each pose, 

- and produces a refined, globally coherent set of poses and apple landmarks used for counting, density mapping, and yield estimation. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

19 of 34 

The refined solution is then used as the basis for all downstream orchard analytics reported in Section 4. 

## _3.10. Geo-Referencing, Outputs, and Yield Proxy_ 

Because reconstruction is performed in the fused geo-referenced `WORLD` frame, the final 3D apple landmarks can be exported directly to mapping formats (ENU/ECEF/LLA and KML) and visualized in GIS software. After triangulation and iSAM2 refinement, the orchard-level apple count is 

**==> picture [250 x 13] intentionally omitted <==**

In addition to count, we report a size-derived yield proxy by converting reconstructed radii to volume and mass. 

The radius _rk_ of the _k_ -th apple is estimated from its multi-view 2D observations and the optimized 3D geometry. For each observing frame _i_ , let _wik_ and _hik_ denote the detected bounding-box width and height in pixels, and let _zik_ denote the depth of the reconstructed landmark in the camera frame, obtained from the optimized pose and landmark geometry. Using the pinhole camera model, the apparent metric diameter is estimated separately along the image _x_ - and _y_ -directions as 

**==> picture [271 x 26] intentionally omitted <==**

where _fx_ and _fy_ are the focal lengths in pixels. The per-view diameter estimate is then computed as 

**==> picture [249 x 21] intentionally omitted <==**

and the corresponding per-view radius is 

**==> picture [220 x 21] intentionally omitted <==**

Because each apple is typically observed in multiple frames, the final radius _rk_ is obtained as the median of the per-view radius estimates over the selected top views with the largest bounding boxes, which correspond to the most reliable close-range observations: 

**==> picture [249 x 16] intentionally omitted <==**

This yields a robust multi-view radius estimate for each reconstructed apple, which is then used to compute its spherical volume. We use 15 views of each apple in our work, ensuring highly precise radius calculations. 

The volume is given as, 

**==> picture [223 x 22] intentionally omitted <==**

and using a bulk density _ρ_ (kg/m[3] ), the mass estimate is 

**==> picture [221 x 11] intentionally omitted <==**

yielding the orchard-scale estimate 

**==> picture [255 x 28] intentionally omitted <==**

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

20 of 34 

To obtain a dataset-specific nominal bulk density for the mass proxy, we calibrate _ρ_ using reference measurement of diameter _d_ ref = 8.0 cm and mass _m_ ref = 200 g. Under the spherical approximation, _V_ ref = 3[4] _[π]_[(] _[d]_[ref][/2][)][3][, yielding] 

**==> picture [255 x 22] intentionally omitted <==**

We report orchard-scale mass using this calibrated density as the nominal value, and additionally provide a sensitivity interval _ρ ∈_ [650, 850] kg/m[3] to reflect variability due to cultivar, maturity, and the spherical-shape approximation. 

## _3.11. Implementation Details and Hyperparameters_ 

The complete pipeline can be run on a Jetson AGX Orin, running Linux 35.4.1, using Python 3.10, ZED SDK 5.1.1, and CoTracker3. Images are acquired at 1920 _×_ 1200 pixels and 30 fps. GNSS measurements are logged at 5 Hz. We mention the key hyper-parameters of our pipeline in Table 2 below. 

**Table 2.** Key hyperparameters used in the proposed pipeline. 

|**Parameter**|**Value**|**Parameter**|**Value**|
|---|---|---|---|
|Detection confdence threshold<br>_τ_conf|0.55|Reprojection gate_τ_reproj (px)|10|
|NMS IoU threshold_τ_nms|0.45|Reprojection loss|Huber|
|CoTracker online query update<br>period|every 10 frames|Huber parameter_k_|1.345|
|Min. track length_L_min (frames)|5|Reprojection sigma (px)|10|
|RANSAC iterations|84|Between translation sigma (m)|0.01|
|Min parallax_θ_min (deg)|1.2|Between rotation sigma (deg)|0.3|
|Max camera–fruit distance<br>_d_max (m)|5|ENU translation sigma (m)|0.50|
|First-pose translation sigma (m)|10_−_4|ENU rotation sigma (deg)|180|
|First-pose rotation sigma (deg)|10_−_3|Landmark prior sigma (m)|0.05|



## **4. Results** 

This section reports quantitative and qualitative outcomes of the proposed orchardscale reconstruction pipeline with iSAM2 refinement. We emphasize (i) reconstruction and optimization behavior at scale, (ii) reprojection consistency before and after optimization, (iii) the magnitude and structure of pose corrections, and (iv) downstream geo-referenced aggregation for orchard-level counting and yield-proxy estimation. 

## _4.1. Reconstruction and Optimization Overview_ 

The full optimization was executed over _NX_ = 11,307 camera poses and _NL_ = 9739 triangulated apple landmarks initialized from multi-frame 2D tracks. From 11,793 candidate tracks (minimum track length = 5 frames, minimum triangulation observations = 5), a total of 9739 landmarks were successfully initialized by DLT under a reprojection gating threshold of 10 px. The resulting factor graph contained 411,739 reprojection factors, forming a dense, observation-rich bundle adjustment problem at orchard scale. 

After optimization, the 3D reconstruction remained spatially coherent and visually consistent with orchard structure. For qualitative verification, we rendered the refined camera trajectory and landmark cloud in Open3D and applied a maximum camera-tolandmark distance filter of 5 m to remove far-range reconstructions with limited parallax support. This retained 9738 landmarks and produced a stable landmark distribution across the traversed rows. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

21 of 34 

Figure 7 shows the refined reconstruction from multiple viewpoints. Figure 7a provides a global overview of the orchard traversal, where the refined trajectory is visually smooth and the landmarks align along the row structure. Figure 7b highlights a spatial gap in the reconstructed landmark distribution that corresponds to an actual gap in fruit presence along the scanned row, indicating that the reconstruction preserves meaningful orchard-level structure rather than producing a uniformly dense artifact cloud. Figure 7c provides a closer view of the landmarks and the camera pose frustums. 

**==> picture [11 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a )<br>**----- End of picture text -----**<br>


**==> picture [208 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
( b ) ( c )<br>**----- End of picture text -----**<br>


**Figure 7.** Orchard-scale 3D reconstruction after iSAM2 refinement. The raw and optimized camera poses are shown in blue and orange, respectively. The 3D apples are shown as red dots. ( **a** ) Global view of the reconstructed traversal and landmark distribution. ( **b** ) Example of a reconstructed gap along a row, consistent with a fruit-absence gap observed in the orchard. ( **c** ) Close-up view around maneuvering and inter-row translation, illustrating stable landmark geometry under viewpoint change. 

## _4.2. Reprojection Consistency Before and After iSAM2 Refinement_ 

Reprojection error provides a direct measure of multi-view geometric consistency between estimated poses, triangulated 3D landmarks, and the underlying 2D measurements. Prior to iSAM2 refinement (i.e., using the ENU-aligned pose initialization and DLT landmark initialization), the reprojection residual distribution was heavy-tailed: 

mean = 40.31 px, median = 22.70 px, _p_ 90 = 104.41 px, _p_ 95 = 135.57 px. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

22 of 34 

A total of 76.63% of residuals exceeded 5 px and 65.40% exceeded 10 px. These statistics indicate that although landmark initialization succeeded at scale, the initial joint pose– landmark configuration contained substantial inconsistency, which is expected for long orchard traversals with turns, partial occlusions, and association noise. 

After iSAM2 optimization over pose and landmark variables, reprojection residuals were substantially reduced, with a pronounced improvement in the tail: 

**==> picture [324 x 11] intentionally omitted <==**

The proportion of residuals above 10 px decreased to 25.38% (from 65.40%), while the fraction above 5 px decreased to 53.57%. Qualitatively, this improvement corresponds to a reconstruction in which landmarks are more consistently supported across views and the refined trajectory yields tighter agreement between tracked 2D measurements and projected 3D landmarks. 

To localize remaining failure modes, we inspected frames with the highest median reprojection error. The worst frames were concentrated around a small set of frame ID ranges (e.g., _f id_ = 9896–9900 and _f id ≈_ 7658–7825), suggesting localized segments with degraded tracking geometry, reduced landmark support, and/or rapid viewpoint change (consistent with turn and maneuver segments). 

## _4.3. Pose Correction Magnitude and Internal Consistency_ 

To quantify how strongly the refined solution deviates from the ZED Fusion initialization, we measured pose deltas between optimized and initial poses. Across all 11,307 poses, iSAM2 applied moderate but non-negligible corrections: 

**==> picture [327 x 11] intentionally omitted <==**

**==> picture [294 x 12] intentionally omitted <==**

The largest corrections were concentrated near the end of the trajectory (e.g., _fid_ = 11310–11319), reaching _∼_ 1.27 m and _∼_ 23.5 _[◦]_ . This behavior indicates that the optimizer redistributed accumulated inconsistency across the graph, correcting segments where the initial solution was weakly constrained or affected by drift and association noise. 

Importantly, the refined solution remained consistent with local motion constraints. Between-residuals (optimized vs. raw between-measurements) were small: 

trans residual mean = 0.0055 m, rot residual mean = 0.108 _[◦]_ , 

and normalized residuals (residual/ _σ_ ) remained well-behaved (means _<_ 1), with worstcase edges remaining below _∼_ 5 _σ_ . This indicates that iSAM2 improved global multi-view consistency primarily through reprojection-driven adjustments while preserving locally smooth motion implied by sequential constraints. 

## _4.4. Orchard-Scale Apple Counting Against Ground Truth_ 

Using the finalized landmark set after geometric filtering and iSAM2 refinement, we compared the total predicted apple count against the orchard ground-truth total. The pipeline produced _N_ pred = 9739 landmarks versus _N_ GT = 9985 apples, corresponding to an absolute error of 246 apples and an aggregate undercount of 2.46%. The ground-truth value is established by physically harvesting the scanned orchard block and manually counting all collected fruits, thereby providing a directly measured reference for quantitative comparison. This result demonstrates that, at the orchard-block scale and under a single continuous scan with turns and strong viewpoint changes, the proposed system provides a 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

23 of 34 

close estimate of total fruit cardinality while simultaneously producing a geo-referenced 3D landmark map suitable for downstream orchard analytics. 

Figure 8 above shows the top-down geo-referenced distribution of the reconstructed apples in QGIS. The aligned rows and the spatial continuity of apple points indicate that the refined pose and landmark solution is consistent with the orchard layout. Qualitatively, the plot also preserves meaningful local structure: for example, in the final row on the right side of the map, a visible gap in the apple distribution coincides with the ground truth where two consecutive trees had no apples, providing qualitative evidence that the reconstruction captures spatial variations in fruit presence rather than producing a homogeneous distribution. 

**Figure 8.** Top-down geo-referenced visualization of reconstructed apples (shown as red squares) in QGIS after iSAM2 refinement. The spatial distribution aligns with the traversed rows and preserves local gaps consistent with observed fruit absence. 

To characterize how counting error is distributed, we report a row-level breakdown in Appendix A.1. 

Row-wise counting bias is influenced not only by perception and geometry, but also by orchard architecture. Training systems alter canopy depth and fruit exposure [43–45]. In our dataset, the final scanned row is trained under a different and denser configuration, which increases self-occlusion and reduces the number of frames in which fruits remain visible with sufficient parallax for stable tracking and triangulation. This provides a fieldconsistent explanation for the stronger undercount observed for that row in Appendix A.1, relative to the other scanned rows. These factors are consistent with the spatial distribution seen in Figure 8. 

## _4.5. Geo-Referenced Apple Density Mapping and Size-Derived Yield Proxy_ 

A key outcome of the proposed pipeline is that each detected-and-tracked apple is reconstructed as a geo-referenced 3D landmark in the fused `WORLD` frame, enabling 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

24 of 34 

orchard-scale spatial products in addition to counting. Specifically, the refined landmark set supports: (i) a spatial density map of fruit occurrence and (ii) a size-derived yield proxy obtained from reconstructed fruit radii. 

## 4.5.1. Geo-Referenced Apple Density Map 

Figure 9 shows a top-down heatmap of reconstructed apples projected into a local ENU coordinate system. The density image is computed by binning apple landmark locations in the horizontal plane. Let **X** _k_ = [ _Ek_ , _Nk_ , _Uk_ ] _[⊤]_ denote the ENU coordinates of apple _k_ . For a chosen bin size ∆ (m), the 2D density map is the histogram 

**==> picture [457 x 28] intentionally omitted <==**

where 1 ( _·_ ) is the indicator function and ( _i_ , _j_ ) indexes grid cells. This representation converts the sparse landmark set into an orchard-scale product that highlights where fruit detections concentrate along the traversed rows and around turns, and it provides a direct substrate for row-wise, block-wise, or corridor-wise aggregation. 

**Figure 9.** Top-down apple density heatmap generated by binning geo-referenced 3D landmarks in the ENU plane. The heatmap summarizes fruit occurrence patterns along the scanned rows and around turning segments. 

## 4.5.2. Size-Derived Mass Estimate from Reconstructed Radii 

In addition to spatial density, the reconstructed apple radii enable an orchard-scale estimate of total mass under a density-based physical model. For each apple _k_ , the reconstruction provides a radius _rk_ (m). Under a spherical approximation, apple volume 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

25 of 34 

is given by Equation (36) and mass is modeled as Equation (37). where _ρ_ is apple bulk density (kg/m[3] ). For the reconstructed set of _N_ = 9738 apples, using the calibrated density _ρ_ ref = 746 kg/m[3] (Equation (39)), we obtain a nominal orchard-scale mass estimate of _M_ (746) = 1485.108 kg. Under a conservative density range of _ρ ∈_ [650, 850] kg/m[3] , the estimate varies from _M_ (650) = 1293.927 kg to _M_ (850) = 1692.059 kg. Table 3 above summarizes these results. 

**Table 3.** Orchard-scale apple mass estimate from reconstructed fruit radii using a density-based model. The nominal density is calibrated from a reference fruit (Equation (39)); the interval reflects sensitivity to plausible density variation. 

|**Quantity**|**Value**|**Notes**|
|---|---|---|
|Number of apples (_N_)|9738|After geometric fltering|
|Nominal density (_ρ_ref)|746 kg/m3|From reference fruit<br>(Equation (39))|
|Density range|650–850 kg/m3|Sensitivity interval|
|Total mass _M_(746)|1485.108 kg|Nominal estimate|
|Total mass range<br>_M_(650)–_M_(850)|1293.927–1692.059 kg|Density sensitivity|



The reported mass values should be interpreted as a size-derived yield proxy conditioned on (i) the reconstructed radius distribution, (ii) the spherical approximation, and (iii) the assumed bulk density. Nevertheless, Equation (38) makes the dependence on _ρ_ explicit, and couples geo-referenced mapping with yield estimation, enabling consistent comparisons between orchard segments under fixed modelling assumptions. 

## **5. Discussion** 

## _5.1. End-to-End Integration: From Geo-Referenced Sensing to Orchard-Scale Products_ 

This work demonstrates a fully integrated orchard-scale pipeline that couples multisensor geo-referenced pose estimation (ZED Fusion: GNSS-VIO), perception (YOLOv9), long-horizon association (CoTracker3), geometric initialization (multi-view triangulation), and SLAM back-end refinement (iSAM2 incremental bundle adjustment). The key design principle is to enforce multi-view geometric consistency throughout the workflow. Rather than aggregating detections in image space, the proposed method reconstructs fruit as 3D landmarks and refines the joint pose–landmark state, yielding outputs that are inherently compatible with orchard mapping: refined poses, a refined geo-referenced 3D apple map, and derived orchard-level analytics (count, density, and a weight proxy). Liu et al. [39] similarly employed fruit as landmarks in a structure-from-motion framework, also leveraging multi-view consistency; however, their approach used a Kalman filter and optical flow for tracking, whereas the present work employs a transformer-based tracking solution (CoTracker3). 

The geo-referenced pose stream produced by GNSS-VIO fusion provides an important initialization and a global reference. However, orchard traversals (particularly those including turns and repeated structure) still produce residual inconsistencies that propagate into 3D reconstruction if left uncorrected. The proposed approach uses this geo-referenced trajectory as a strong prior but relies on the subsequent SLAM refinement stage to reconcile the fused trajectory with the dense set of multi-view reprojection constraints induced by tracked fruit observations. 

## _5.2. SLAM Interpretation: Front-End Association and Back-End Bundle Adjustment_ 

A useful lens to interpret the system is the classical SLAM decomposition. The frontend is responsible for producing reliable correspondences: YOLOv9 localizes candidate 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

26 of 34 

apples in each frame and CoTracker3 associates detections over time into tracklets that approximate persistent landmarks. This step is central in orchards, where appearance is repetitive and occlusions are frequent. The back-end uses these correspondences to enforce a globally consistent solution via factor-graph optimization: each track observation yields a reprojection factor linking the corresponding pose and landmark, producing a dense bipartite graph spanning the full traversal. 

In this context, iSAM2 functions as an incremental bundle adjustment back-end that jointly refines camera poses and apple landmarks. The incremental nature of iSAM2 is particularly aligned with orchard-scale sequences, because constraints arrive sequentially as the robot moves and because the number of variables (poses and landmarks) can be large. The resulting refinement improves global consistency without requiring a separate loop-closure infrastructure or marker deployment in the orchard as seen in other works [47]. 

## _5.3. Impact of SLAM Refinement on Trajectory and Reconstruction Quality_ 

The results provide clear evidence that iSAM2 refinement improves geometric consistency relative to both VIO-only and GNSS-VIO fused trajectories. The qualitative comparison in Figure 5 illustrates progressive stabilization: VIO-only poses exhibit strong drift across the traversal; GNSS-VIO fusion anchors the trajectory globally but still leaves notable residual multi-view inconsistency which causes large errors in fruit localization; and iSAM2 refinement yields a tighter trajectory with substantially reduced reprojection error. 

This improvement is consistent with the role of bundle adjustment in distributing error globally through multi-view constraints. Importantly, pose corrections are moderate in magnitude, suggesting that refinement is not arbitrarily deforming the trajectory but rather correcting accumulated inconsistency where constraints are weaker (e.g., latestage portions and maneuver segments). The fact that between-residuals remain small indicates that local motion regularity is preserved while global reprojection agreement is improved—a desirable property in orchard traversals, where smooth motion along rows must coexist with sharp curvature at headland turns. 

## _5.4. Landmark Stability and Orchard-Scale Structure Preservation_ 

A central question for yield mapping is whether the 3D landmark cloud is both stable and structurally meaningful. The reconstruction results in Figure 7 indicate that the refined solution yields a coherent landmark distribution aligned with the orchard geometry and robust to viewpoint changes. The presence of spatial gaps consistent with the real orchard (as visible both in 3D renderings and in top-down GIS visualization) suggests that the reconstruction captures genuine variations in fruit presence rather than generating an overly smooth or artificially dense map. 

The constraint design used in landmark initialization and filtering (minimum track length, reprojection gating, parallax threshold, and range filtering) supports stability by discarding ill-conditioned triangulations and short-lived detections that are unlikely to yield consistent 3D structure. This combination is especially important in orchards, where occlusion-induced track fragmentation and insufficient parallax for distant fruit can otherwise produce unstable depth estimates. 

## _5.5. Counting Performance and Spatial Diagnostics_ 

At the orchard-block level, the system produces a close estimate of total fruit cardinality (2.46% aggregate undercount), while simultaneously providing a geo-referenced 3D map. This dual output is significant: many counting pipelines can report a number, but cannot support spatial auditing of where fruit instances were reconstructed. Here, the top-down QGIS visualization (Figure 8) provides a qualitative diagnostic layer that helps interpret counting performance. The alignment of reconstructed points to the orchard 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

27 of 34 

rows and the preservation of local gaps consistent with ground observations indicate that the reconstruction is not only quantitatively plausible but also spatially interpretable. 

The row-wise breakdown (Appendix A.1) exhibits heterogeneous bias, which is consistent with orchard field reality. Dense canopy and training-system differences can reduce recall through occlusion, while maneuver-induced viewpoint changes can increase the likelihood of track fragmentation and duplicate landmark creation. These mechanisms also align with the reprojection diagnostics that localize higher-error frame clusters to specific trajectory segments. 

## _5.6. From Point Landmarks to Yield Surfaces: Density and Mass Proxies_ 

The geo-referenced landmark set enables a transition from discrete detections to spatial yield representations. The density heatmap (Figure 9) summarizes fruit occurrence patterns as a spatial field over ENU coordinates, providing an orchard-scale view of fruit distribution along rows and around turns. This representation supports aggregation at arbitrary spatial resolutions, which is useful for block-level analyses and for comparison across orchard sections. 

The weight proxy further extends this representation by associating each landmark with a size-derived mass estimate based on reconstructed radii and a density model. While absolute mass depends on modeling assumptions (spherical approximation and bulk density), the formulation makes this dependence explicit and supports sensitivity analysis through a density range. Although the spherical approximation is a first-order model, more accurate alternatives exist; for example, the geometric neural representation employed by Wang et al. [36]. 

It is important to distinguish centroid reconstruction from size estimation. In the present pipeline, each landmark corresponds to an estimated fruit centre obtained from tracked image observations and multi-view triangulation; the fruit size model is applied only afterward to derive radius- and density-based mass proxies. Consequently, variable fruit size does not directly change the projective geometry of the landmark state, but it can indirectly affect centroid accuracy when bounding-box centres deviate from true fruit centres under partial occlusion object detection. 

## _5.7. Limitations and Error Sources_ 

The proposed pipeline is most likely to degrade under three practical conditions. First, low fruit visibility caused by dense canopy, severe leaf-to-fruit occlusion, strong backlighting, rapid viewpoint change, or near-row-end turns—can reduce detector recall, shorten track length, and increase identity fragmentation. In these situations, fewer stable observations are available for triangulation, and some fruit may remain unreconstructed or may generate unstable landmarks. Practical mitigation includes slower traversal in highly occluded segments, stronger detector fine-tuning for orchard-specific imagery, dual-side or repeated-row observation, and the use of more occlusion-tolerant association strategies. 

Second, the method may underperform when landmarks are sparse. Because apples serve as the primary visual landmarks in the present implementation, rows or segments with low fruit density provide fewer reprojection constraints to stabilize pose refinement—a limitation inherent to any system that relies on fruit as the primary landmark type [39]. This may reduce the corrective effect of the SLAM back-end, especially in long segments with limited geometric diversity. A practical mitigation is to augment the graph with additional non-fruit landmarks, such as generic visual feature tracks or structural points, so that optimization does not depend exclusively on fruit visibility. 

Third, strong GNSS degradation under dense canopy, poor satellite geometry, or multipath conditions can introduce local inconsistencies in the fused geo-referenced trajectory. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

28 of 34 

In such cases, the soft ENU priors may become less informative, and the solution must rely more heavily on relative-motion constraints and reprojection consistency. Practical mitigation includes stronger outlier handling on the geo-referenced priors, adaptive prior weighting based on GNSS quality indicators, and the integration of complementary depth or ranging sensors such as LiDAR. 

From a geometric perspective, triangulation quality also depends strongly on baseline and parallax. Distant fruit, near-fronto-parallel viewing, and short temporal support reduce depth observability, which is why the pipeline applies minimum track-length, reprojection, parallax, and range filters. The consequence is that distant or heavily occluded fruit may be underrepresented in the final map. Multi-sensor depth support, repeated viewpoints, and stronger robust modeling of outlier correspondences are therefore practical directions for improving reliability in these conditions. 

The present association pipeline is designed primarily for temporally continuous tracking within a traversal segment and does not explicitly solve long-gap re-identification after a fruit fully disappears and later re-enters the field of view under a strong viewpoint reversal, such as a row-end turn. In such cases, the same fruit may be assigned a new track identity, which is a limitation of the current front-end rather than of the factor-graph back-end. 

## _5.8. Scalability and Operational Feasibility_ 

The incremental SLAM formulation enables scaling to orchard-length sequences with many poses and landmarks. The factor-graph structure and iSAM2 updates support efficient refinement without requiring repeated full batch optimization, making the approach compatible with long runs and dense observation graphs. Although optimization is performed after acquisition in the current study, the architecture supports near real-time operation: detection and tracking can run online, factors can be added incrementally, and smoothing can be performed periodically. This property is important for deployment on robotic platforms that must produce actionable yield maps during continuous orchard operation. 

## _5.9. Future Directions_ 

Several directions are identified to extend and strengthen the proposed framework. From a perception standpoint, integrating additional sensing modalities—such as LiDAR—could improve depth robustness and reduce reliance on motion parallax for distant or occluded fruit. More expressive robust loss functions and explicit outlier modeling within the reprojection factors may further reduce the influence of incorrect correspondences in challenging, cluttered segments. To complement visual fruit landmarks, future work will also explore the use of semantic segmentation to identify rigid, stable scene elements—such as trunks, support poles, and the ground plane — as more reliable anchors for the factor graph, particularly in scenarios where fruit landmarks are absent or scarce. 

The current static-scene assumption, which treats fruit landmarks as approximately fixed over the timescale of a single row traversal, is a recognized limitation under windinduced branch sway. Addressing this will require explicit dynamic-scene modeling, for instance through motion segmentation or branch-motion priors, to prevent transient landmark displacement from degrading track consistency and localization accuracy. 

On the localization side, a dedicated investigation into system behavior under controlled GNSS degradation scenarios—including prolonged signal loss, varying canopy density, and severe multipath—is planned, with the aim of providing a rigorous quantitative characterization of drift accumulation and recovery. Incorporating uncertainty propagation from pose and landmark estimates into the density and mass maps would 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

29 of 34 

further enable probabilistic yield surfaces, offering better-calibrated confidence measures for agronomic decision support. 

A further open problem concerns the potential double-counting of fruit observed from opposing sides of a row during adjacent-row traversals. While preliminary visual inspection suggests that most fruit in the palmette training systems examined are not simultaneously visible from both viewpoints, a systematic evaluation based on fruit-level re-identification across opposing viewpoints is needed to rigorously quantify this effect. Developing robust cross-view fruit association—potentially leveraging appearance descriptors, geometric constraints, or learned re-identification models—represents a meaningful direction for future work. 

The system will be evaluated on orchard training systems with larger canopies, greater fruit occlusion, and higher structural variability to assess generalization beyond the conditions examined in the present study. A particularly promising avenue for future work is 4D monitoring [26]—the integration of 3D reconstruction over time—which enables the analysis of crop development. Lei et al. [15] recently applied this concept to apple orchards using a multi-sensor setup that includes a LiDAR device. Such spatio-temporal analyses could be carried out using the precise geo-referenced models produced by the present work. 

## **6. Conclusions** 

This work develops an end-to-end, orchard-scale mapping approach that connects geo-referenced sensing, multi-view perception, and factor-graph optimization into a single coherent workflow for yield assessment. By treating fruit instances as persistent 3D landmarks rather than frame-level detections, the pipeline naturally supports orchard-scale aggregation, spatial auditing, and GIS-compatible outputs while maintaining geometric consistency through incremental SLAM refinement. The results indicate that a tightly integrated front-end (detection and association) and back-end (bundle adjustment) can deliver reliable orchard-block estimates from a single continuous traversal, and can further support derived products such as spatial density representations and size-based yield proxies. Looking forward, the most impactful extensions are to strengthen robustness under dense canopy and rapid viewpoint change, to incorporate uncertainty-aware mapping so that yield products include confidence measures, and to calibrate or learn fruit mass/shape models using limited ground truth samples. These directions would move the system from accurate mapping toward decision-grade yield forecasting, enabling repeatedseason monitoring, block-to-block comparability, and real-time deployment on autonomous orchard platforms. 

**Author Contributions:** Conceptualization, D.B. and T.T.S.; validation, D.B., L.N.d.F. and T.T.S.; formal analysis, T.T.S.; investigation, L.V.K.; resources, L.G. and A.d.R.; data curation, T.T.S.; writing—original draft preparation, D.B. and T.T.S.; writing—review and editing, D.B. and T.T.S.; visualization, D.B. and T.T.S.; supervision, T.T.S. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was funded by Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP), grants 2022/09319-9, 2024/10267-9 and 2024/19729-5. 

**Data Availability Statement:** The original data presented in the study are openly available in Zenodo at https://doi.org/10.5281/zenodo.17750202. 

**Acknowledgments:** During the preparation of this manuscript, the author(s) used large-language models to improve English clarity and readability. The authors have reviewed and edited the output and take full responsibility for the content of this publication. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

30 of 34 

**Conflicts of Interest:** The authors declare no conflicts of interest. The funders had no role in the design of the study, in the collection, analysis, or interpretation of data, in the writing of the manuscript, or in the decision to publish the results. 

## **Appendix A** 

## _Appendix A.1_ 

The orchard rows included in the traversal are not trained identically. Apple training systems (e.g., central leader, spindle, and multi-leader) determine canopy architecture and fruit exposure, affecting the degree of occlusion observed by ground-based vision systems [43–46]. In particular, the last scanned row in our experiment follows a different training configuration with denser canopy structure. Under a single-pass scan, this increases the probability that fruits remain partially or fully occluded and reduces the temporal support available for long-horizon association and triangulation, which can decrease landmark recall. The row-wise breakdown in Table A1 should therefore be interpreted in light of these agronomic/structural differences, rather than as a uniform failure mode of the reconstruction pipeline. It is to be noted that the Fuji rows are even-numbered, while the odd-numbered rows are allotted to Gala rows. 

**Table A1.** Row-wise apple counts from optimized landmarks vs. ground truth. 

|**Row**|**(Fila)**|**GT**|**Predicted**|**Abs. Error**|**% Error**|
|---|---|---|---|---|---|
|Row|2|2721|2634|87|3.20%|
|Row|4|2535|2899|364|14.36%|
|Row|6|2564|2707|143|5.58%|
|Row|8|2165|1499|666|30.77%|
|Total||9985|9739|246|2.46%|



## _Appendix A.2_ 

## Reproducibility checklist 

To strengthen reproducibility, we will release the full inference pipeline as a public repository, including the YOLO detection script, the CoTracker3-based 2D–3D apple tracking module, and the GTSAM/iSAM2 pose refinement code, together with example run commands and configuration files. The repository will include: (i) the data interface specification for input frames, camera intrinsics, pose/GNSS CSV files, and detection labels; (ii) the exact detector, tracker, triangulation, and optimization settings used in our experiments; and (iii) an exported software environment listing the versions of Python, PyTorch, CUDA, OpenCV, SciPy, and GTSAM. In the current implementation, the main configurable values are explicitly exposed in the scripts, including YOLO image size, confidence and NMS thresholds; CoTracker3 birth interval, duplicate suppression radius, visibility threshold, RANSAC triangulation parameters, and frame subrange; and iSAM2 factor weights, reprojection noise, ENU prior strength, triangulation thresholds, landmark prior strength, and relinearization settings. We will also provide one small example sequence and its expected outputs to facilitate end-to-end verification. 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

31 of 34 

**Table A2.** Reproducibility details for the proposed apple tracking and pose refinement pipeline. Values correspond to the implementation used in our experiments unless otherwise noted. File paths are omitted for brevity and should be replaced by the public repository structure or supplementary material. 

|**Stage**|**Component/Parameter**|**Value Used**|
|---|---|---|
|Detection|Weights|YOLOv9 checkpoint reported in<br>the experiment confguration.|
|Detection|Input size|`640` _×_ `640`; set by`–imgsz`with<br>default`(640, 640)`.|
|Detection|Confdence threshold|`0.55`; set by`–conf-thres`.|
|Detection|NMS IoU threshold|`0.45`; set by`–iou-thres`.|
|Detection|Maximum detectionsper image|`1000`; set by`–max-det`.|
|Detection|Frame sampling|`vid-stride=1`; all frames<br>processed bydefault.|
|2D tracking|Tracker|CoTracker3 online|
|2D tracking|Detection confdence threshold<br>for tracker input|`0.55`; set by`–conf-thres`in the<br>CoTracker script.|
|2D tracking|trackgeneration strategy|Periodic with default 10;|
|2D tracking|Duplicate suppression radius|`17.0 px`; set by`–dup-radius`.|
|2D tracking|Visibilitythreshold|`0.6`; set by`–vis-thresh`.|
|3D triangulation|Pose–image timestamp tolerance|`80,000,000`ns; set by<br>`–max-pose-dt-ns`.|
|3D triangulation|Maximum viewsper track|`24`; set by`–max-views`.|
|3D triangulation|RANSAC iterations|`84`; set by`–ransac-iters`.|
|3D triangulation|Re-estimation frequency|Every 2 frames; set by<br>`–reestimate-every-3d`.|
|3D triangulation|Minimum observations for 3D<br>usability|`3`; tracks with fewer than 3<br>observations are excluded<br>from triangulation.|
|||Max. geometric error: 20.0 px;|
|||inlier ratio: 0.30; max. distance:|
|3D triangulation|Geometric acceptance thresholds|1200.0; min. inliers kept: 3; min.|
|||angle: 0.75_◦_; max. median|
|||reprojection error: 20.0px.|
|||iSAM2 implemented with|
|Pose refnement|Optimizer|GTSAM; current script performs<br>a single graph update followed|
|||by`calculateEstimate()`.|
|||Pose3 camera poses and Point3|
|Pose refnement|Variables|landmarks; unknowns are pose<br>nodes`X(fid)`and landmark|
|||nodes`L(tid)`.|
|||Raw relative pose, aligned ENU|
|Pose refnement|Input priors/factors|prior, reprojection factors,|
|||and landmarkpriors.|
|Pose refnement|Frame range|`1000:28,425`; set by<br>`–fid-range`.|



https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

32 of 34 

**Table A2.** _Cont._ 

|**Stage**|**Component/Parameter**|**Value Used**|
|---|---|---|
|Pose refnement|Between translation sigma|`0.01 m`; set by<br>`–between-trans-sigma`.|
|Pose refnement|Between rotation sigma|`0.3 deg`; set by<br>`–between-rot-sigma-deg`.|
|Pose refnement|ENU translation sigma|`0.50 m`; set by`–enu-sigma`.|
|||`180 deg`; set by|
|Pose refnement|ENU rotation sigma|`–enu-rot-sigma-deg`, effectively<br>translation-only|
|||ENU regularization.|
|||Disabled by default;|
|Pose refnement|Robust ENU prior|`–robust-enu=False`, Huber|
|||parameter`1.345`.|
|||`rot=1e-3 deg`,`trans=1e-4`;|
|Pose refnement|First-pose gauge prior|set by<br>`–first-pose-rot-sigma-deg`|
|||and`–first-pose-trans-sigma`.|
|||Global frame ids;|
|Pose refnement|MOT frame convention|`–mot-frame-is-global=1`.|
|||If local,`–mot-start-frame=202`.|
|||Pinhole projection with`Cal3_S2`;|
|Pose refnement|Measurement model|intrinsics parsed from text fle<br>and used in `GenericProjection-`|
|||`FactorCal3_S2`.|
|Pose refnement|Minimum track length|`5`; set by`–min-track-length`.|
|Pose refnement|Triangulation minimum<br>observations|`5`; set by`–triang-min-obs`.|
|Pose refnement|Triangulation maximum views|`10`; set by`–triang-max-views`.|
|Pose refnement|Triangulation reprojection gate|`100,000.0 px`; set by<br>`–triang-reproj-gate-px`.|
|Pose refnement|Reprojection sigma|`10.0 px`; set by<br>`–meas-sigma-px`.|
|Pose refnement|Robust reprojection loss|`–robust-reproj=True`with<br>Huberparameter`1.345`.|
|Pose refnement|Landmark prior sigma|`0.05 m`; set by<br>`–landmark-prior-sigma`.|



## **References** 

1. Underwood, J.P.; Hung, C.; Whelan, B.; Sukkarieh, S. Mapping almond orchard canopy volume, flowers, fruit and yield using lidar and vision sensors. _Comput. Electron. Agric._ **2016** , _130_ , 83–96. [CrossRef] 

2. Sa, I.; Ge, Z.; Dayoub, F.; Upcroft, B.; Perez, T.; McCool, C. DeepFruits: A Fruit Detection System Using Deep Neural Networks. _Sensors_ **2016** , _16_ , 1222. [CrossRef] [PubMed] 

3. Santos, T.T.; Koenigkan, L.V. Geo-referenced 3-D mapping of vineyards using factor graph and CNN-based depth estimation. In Proceedings of the Present and Future of Agricultural Robotics and Technologies: Academic and Industry Perspectives Workshop, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), IEEE, Detroit, MI, USA, 1–5 October 2023. [CrossRef] 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

33 of 34 

4. Santos, T.T.; de Souza, K.X.; Camargo Neto, J.; Koenigkan, L.V.; Moreira, A.S.; Ternes, S. Multiple orange detection and tracking with 3-D fruit relocalization and neural-net based yield regression in commercial sweet orange orchards. _Comput. Electron. Agric._ **2024** , _224_ , 109199. [CrossRef] 

5. Dellaert, F.; Kaess, M. _Factor Graphs for Robot Perception_ ; Foundations and Trends in Robotics; Now Publishers: Hanover, MA, USA, 2017. 

6. Kaess, M.; Johannsson, H.; Roberts, R.; Ila, V.; Leonard, J.; Dellaert, F. iSAM2: Incremental smoothing and mapping with fluid relinearization and incremental variable reordering. In Proceedings of the 2011 IEEE International Conference on Robotics and Automation, Shanghai, China, 9–13 May 2011; pp. 3281–3288. [CrossRef] 

7. Badgujar, C.M.; Poulose, A.; Gan, H. Agricultural object detection with You Only Look Once (YOLO) Algorithm: A bibliometric and systematic literature review. _Comput. Electron. Agric._ **2024** , _223_ , 109090. [CrossRef] 

8. Matos, G.P.; Santiago, C.; Costeira, J.P.; Saldanha, R.L.; Morgado, E.M. Tracking and Counting Apples in Orchards Under Intermittent Occlusions and Low Frame Rates. In Proceedings of the 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), Seattle, WA, USA, 17–18 June 2024; pp. 5413–5421. [CrossRef] 

9. Meyer, L.; Gilson, A.; Schmid, U.; Stamminger, M. FruitNeRF: A Unified Neural Radiance Field based Fruit Counting Framework. In Proceedings of the 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Abu Dhabi, United Arab Emirates, 14–18 October 2024; pp. 1–8. [CrossRef] 

10. Huang, Y.; Ren, Z.; Li, D.; Liu, X. Phenotypic techniques and applications in fruit trees: A review. _Plant Methods_ **2020** , _16_ , 107. [CrossRef] 

11. Vougioukas, S.G. Agricultural Robotics. _Annu. Rev. Control Robot. Auton. Syst._ **2019** , _2_ , 365–392. [CrossRef] 

12. Shamshiri, R.R.; Navas, E.; Käthner, J.; Höfner, N.; Koch, K.; Dworak, V.; Hameed, I.; Paraforos, D.S.; Fernández, R.; Weltzien, C. Agricultural robotics to revolutionize farming: Requirements and challenges. In _Mobile Robots for Digital Farming_ ; CRC Press: Boca Raton, FL, USA, 2025; pp. 107–155. 

13. Vulpi, F.; Marani, R.; Petitti, A.; Reina, G.; Milella, A. An RGB-D multi-view perspective for autonomous agricultural robots. _Comput. Electron. Agric._ **2022** , _202_ , 107419. [CrossRef] 

14. Cheng, D.; Cladera, F.; Prabhu, A.; Liu, X.; Zhu, A.; Green, P.C.; Ehsani, R.; Chaudhari, P.; Kumar, V. TreeScope: An Agricultural Robotics Dataset for LiDAR-Based Mapping of Trees in Forests and Orchards. In Proceedings of the 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 13–17 May 2024; pp. 14860–14866. [CrossRef] 

15. Lei, J.; Prabhu, A.; Liu, X.; Cladera, F.; Mortazavi, M.; Ehsani, R.; Chaudhari, P.; Kumar, V. Spatio-Temporal Metric-Semantic Mapping for Persistent Orchard Monitoring: Method and Dataset. _IEEE Robot. Autom. Lett._ **2025** , _10_ , 8610–8617. [CrossRef] 

16. Santos, T.; Koenigkan, L.; Bharti, D.; Gebler, L. SEEmear: High-Resolution georeferenced 3D Mapping Methodology for Proximal Monitoring of Permanent Crops. In Proceedings of the XV Congresso Brasileiro de Agroinformática, Online, 10–12 December 2025. 

17. Xiao, F.; Wang, H.; Xu, Y.; Zhang, R. Fruit Detection and Recognition Based on Deep Learning for Automatic Harvesting: An Overview and Review. _Agronomy_ **2023** , _13_ , 1625. [CrossRef] 

18. Wang, C.Y.; Yeh, I.H.; Liao, H.Y.M. YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information. _arXiv_ **2024** , arXiv:2402.13616. [CrossRef] 

19. Gené-Mola, J.; Felip-Pomés, M.; Net-Barnés, F.; Morros, J.R.; Miranda, J.C.; Arnó, J.; Asín, L.; Lordan, J.; Ruiz-Hidalgo, J.; Gregorio, E. Video-Based Fruit Detection and Tracking for Apple Counting and Mapping. In Proceedings of the 2023 IEEE International Workshop on Metrology for Agriculture and Forestry (MetroAgriFor), Pisa, Italy, 6–8 November 2023; pp. 301–306. [CrossRef] 

20. Bewley, A.; Ge, Z.; Ott, L.; Ramos, F.; Upcroft, B. Simple online and realtime tracking. In Proceedings of the 2016 IEEE International Conference on Image Processing (ICIP), Phoenix, AZ, USA, 25–28 September 2016; pp. 3464–3468. [CrossRef] 

21. Wojke, N.; Bewley, A.; Paulus, D. Simple Online and Realtime Tracking with a Deep Association Metric. In Proceedings of the 2017 IEEE International Conference on Image Processing (ICIP), Beijing, China, 7–20 September 2017; pp. 3645–3649. [CrossRef] 

22. Zhang, Y.; Sun, P.; Jiang, Y.; Yu, D.; Weng, F.; Yuan, Z.; Luo, P.; Liu, W.; Wang, X. ByteTrack: Multi-Object Tracking by Associating Every Detection Box. In Proceedings of the European Conference on Computer Vision (ECCV), Tel Aviv, Israel, 23–27 October 2022. 

23. Doersch, C.; Yang, Y.; Vecerik, M.; Gokay, D.; Gupta, A.; Aytar, Y.; Carreira, J.; Zisserman, A. TAPIR: Tracking Any Point with Per-Frame Initialization and Temporal Refinement. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), Paris, France, 1–6 October 2023. 

24. Karaev, N.; Rocco, I.; Graham, B.; Neverova, N.; Vedaldi, A.; Rupprecht, C. CoTracker: It is Better to Track Together. _arXiv_ **2023** , arXiv:2307.07635. [CrossRef] 

25. Karaev, N.; Makarov, I.; Wang, J.; Neverova, N.; Vedaldi, A.; Rupprecht, C. CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos. _arXiv_ **2024** , arXiv:2410.11831. [CrossRef] 

https://doi.org/10.3390/agriculture16070764 

_Agriculture_ **2026** , _16_ , 764 

34 of 34 

26. Dong, J.; Burnham, J.G.; Boots, B.; Rains, G.; Dellaert, F. 4D crop monitoring: Spatio-temporal reconstruction for agriculture. In Proceedings of the 2017 IEEE International Conference on Robotics and Automation (ICRA), Singapore, 29 May–3 June 2017; pp. 3878–3885. [CrossRef] 

27. SchÖnberger, J.L.; Zheng, E.; Frahm, J.M.; Pollefeys, M., Pixelwise View Selection for Unstructured Multi-View Stereo. In _Computer Vision—ECCV 2016_ ; Springer International Publishing: Berlin/Heidelberg, Germany, 2016; pp. 501–518. [CrossRef] 

28. Huang, G. Visual-Inertial Navigation: A Concise Review. In Proceedings of the 2019 International Conference on Robotics and Automation (ICRA), Montreal, QC, Canada, 20–24 May 2019; pp. 9572–9582. [CrossRef] 

29. Mourikis, A.I.; Roumeliotis, S.I. A Multi-State Constraint Kalman Filter for Vision-Aided Inertial Navigation. In Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), Rome, Italy, 10–14 April 2007; pp. 3565–3572. [CrossRef] 

30. Leutenegger, S.; Lynen, S.; Bosse, M.; Siegwart, R.; Furgale, P. Keyframe-based visual–inertial odometry using nonlinear optimization. _Int. J. Robot. Res._ **2015** , _34_ , 314–334. [CrossRef] 

31. Liu, J.; Gao, W.; Hu, Z. Optimization-Based Visual-Inertial SLAM Tightly Coupled with Raw GNSS Measurements. In Proceedings of the 2021 IEEE International Conference on Robotics and Automation (ICRA), Xi’an, China, 30 May–5 June 2021; pp. 11612–11618. [CrossRef] 

32. Cao, S.; Lu, X.; Shen, S. GVINS: Tightly Coupled GNSS–Visual–Inertial Fusion for Smooth and Consistent State Estimation. _IEEE Trans. Robot._ **2022** , _38_ , 2004–2021. [CrossRef] 

33. Cadena, C.; Carlone, L.; Carrillo, H.; Latif, Y.; Scaramuzza, D.; Neira, J.; Reid, I.; Leonard, J.J. Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age. _IEEE Trans. Robot._ **2016** , _32_ , 1309–1332. [CrossRef] 

34. Stereolabs. Global Localization Overview. 2025. Available online: https://www.stereolabs.com/docs/fusion/global-localization (accessed on 20 October 2025). 

35. Luiten, J.; Osep, A.; Dendorfer, P.; Torr, P.; Geiger, A.; Leal-Taixé, L.; Leibe, B. HOTA: A Higher Order Metric for Evaluating Multi-Object Tracking. _Int. J. Comput. Vis._ **2021** , _129_ , 548–578. [CrossRef] 

36. Wang, K.; Pan, Y.; Magistri, F.; Kooistra, L.; Stachniss, C.; Wang, W.; Valente, J. UAV-based Monocular 3D Panoptic Mapping for Fruit Shape Completion in Orchard. _Isprs J. Photogramm. Remote Sens._ **2026** , _231_ , 608–621. [CrossRef] 

37. Pichhika, H.C.; Subudhi, P.; Yerra, R.V.P. Extended Kalman Filter Based Tracking Method for Accurate Fruit Yield Estimation Preserving SE(3) Equivariance. _IEEE Trans. Agrifood Electron._ **2025** , _3_ , 200–212. [CrossRef] 

38. Liu, X.; Chen, S.W.; Aditya, S.; Sivakumar, N.; Dcunha, S.; Qu, C.; Taylor, C.J.; Das, J.; Kumar, V. Robust Fruit Counting: Combining Deep Learning, Tracking, and Structure from Motion. In Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, Spain, 1–5 October 2018; pp. 1045–1052. 

39. Liu, X.; Chen, S.W.; Liu, C.; Shivakumar, S.S.; Das, J.; Taylor, C.J.; Underwood, J.; Kumar, V. Monocular Camera Based Fruit Counting and Mapping With Semantic Data Association. _IEEE Robot. Autom. Lett._ **2019** , _4_ , 2296–2303. [CrossRef] 

40. Villacrés, J.; Viscaíno, M.; Delpiano, J.; Vougioukas, S.; Cheein, F.A. Apple Orchard Production Estimation Using Deep Learning Strategies: A Comparison of Tracking-by-Detection Algorithms. _Comput. Electron. Agric._ **2023** , _204_ , 107513. [CrossRef] 

41. Gené-Mola, J.; Sanz-Cortiella, R.; Rosell-Polo, J.R.; Escolà, A.; Gregorio, E. In-Field Apple Size Estimation Using PhotogrammetryDerived 3D Point Clouds: Comparison of 4 Different Methods Considering Fruit Occlusions. _Comput. Electron. Agric._ **2021** , _188_ , 106343. [CrossRef] 

42. Gené-Mola, J.; Ferrer-Ferrer, M.; Gregorio, E.; Blok, P.M.; Hemming, J.; Morros, J.R.; Rosell-Polo, J.R.; Vilaplana, V.; Ruiz-Hidalgo, J. Looking Behind Occlusions: A Study on Amodal Segmentation for Robust On-Tree Apple Fruit Size Estimation. _Comput. Electron. Agric._ **2023** , _209_ , 107854. [CrossRef] 

43. Robinson, T.L. Apple orchard planting systems. In _Apples: Botany, Production and Uses_ ; Ferree, D.C., Warrington, I.J., Eds.; CABI Publishing: Wallingford, UK, 2003; pp. 345–407. 

44. Rufato, A.R.; Kretzschmar, A.A.; Rufato, L. _Sistemas de Condução Para a Cultura da Macieira_ ; Epagri: Florianópolis, Brazil, 2008. 

45. Palladini, L.A.; Rufato, A.R. _Principais Sistemas de Condução Disponíveis Para a Cultura da Macieira_ ; Technical Report; Embrapa Uva e Vinho: Bento Gonçalves, Brazil, 2011. 

46. Dorigoni, A.; Micheli, F. Development of a cultivation system for multi-leader trees. _EFM_ **2019** , _5_ , 8–13. 

47. Zheng, Y.; Liu, A.; Huang, A.; Kim, D.H.; Shen, Y.; Lee, K.H. Realtime multi-RGBD SLAM framework for 3D reconstruction and phenotyping in large-scale apple orchards. _Comput. Electron. Agric._ **2026** , _240_ , 111170. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

https://doi.org/10.3390/agriculture16070764 

