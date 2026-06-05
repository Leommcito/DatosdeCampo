Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20  * <https://doi.org/10.1007/s44462-025-00020-w>

# RESEARCH **Open Access**

© The Author(s) 2025. **Open Access**  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit <http://​creat​iveco​mmons.​org/​licen​ses/​by-​nc-​nd/4.​0/>.

# Full‑surface detection of apple fruits using enhanced YOLOv5

## Muhammad Hilal Kabir 1,2,3, Zhao Zhang 1,2,3\*, Xiaolong Li 4\*, Bo Han 5, Xu Li 6\*, Liling Yang 7, Wenyu Kong 8,

Mustafa Mhamed 1,2,3, Afshin Azizi 1,2,3, Jiangfan Yu 1,2,3, Man Zhang 1,2,3, Simphiwe Mngomezulu 9  and - I. Oladele 9

## Abstract

Accurate detection of apple surfaces under various orientations in a sorting machine is crucial for applications in precision agriculture, particularly for tasks such as automated quality control. Traditional image processing methods often struggle with complexities introduced by varying fruit orientations. In this study, an enhanced version of the You Only Look Once (YOLOv5) model for full-surface detection of apples is proposed, with a key modification in which the original backbone network is replaced with a more robust architecture. Additionally, the model integrates Convolutional Block Attention Modules (CBAM) for improved feature extraction, which enhances its ability to handle occlusions and complex backgrounds. This innovation optimizes automated sorting and quality control systems, reducing losses and ensuring consistent apple quality. Results show that the enhanced YOLOv5 model performed better than traditional methods, achieving precision rates of 76.80%, 88.40%, 88.20%, and 88.20%, recall rates of 82.30%, 83.20%, 93.10%, and 93.10%, as well as mean average precision (mAP) of 86.00%, 91.70%, 95.00%, and 95.00% respectively for stem up, stem down, sideways, and diagonal orientations. The highest F1-score (90.58) and mAP (95.00) were achieved in the sideways orientation, demonstrating superior performance in this orientation. The model's enhanced accuracy makes it highly suitable for applications in smart agriculture, particularly in automated apples quality control, where reliable and consistent surface detection is essential. **Keywords**   Full-surface, Fruit detection, Orientation of apples, Automated quality control, YOLOv5

\*Correspondence: Zhao Zhang zhaozhangcau@cau.edu.cn Xiaolong Li 262450313@qq.com Xu Li lixu2866@126.com 1 College of Information and Electrical Engineering, China Agricultural University, Beijing 100083, China 2 Key Laboratory of Smart Agriculture System Integration, Ministry of Education, Beijing 100083, China 3 Key Laboratory of Agricultural Information Acquisition Technology, Ministry of Agriculture and Rural Affairs, Beijing 100083, China 4 Institute of Horticulture, Ningxia Academy of Agriculture and Forestry Sciences, Ningxia 750002, China 5 Shandong Inspur Intelligent Production Technology Co., Ltd., Jinan 250101, China 6 Tarim University, College of Information Engineering, Aral, China 7 Xinjiang Academy of Agricultural Sciences, Agricultural Mechanization Institute, Urumqi 830,091, China 8 China Agricultural University, College of Engineering, Beijing, China

9 University of KwaZulu‑Natal, Department of Agricultural Extension and Rural Resource Management, Pietermaritzburg 3201, South Africa

Page 2 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

**Introduction** Rising global demand for high-quality apples is driving the adoption of automated sorting and grading systems using unmanned aerial vehicle (UAV) imaging and deep learning to enhance orchard management and production efficiency \[ 1 - 4 \]. Apples are among the most widely cultivated fruits, grown commercially in over 90 countries \[ 5 \]. Given the scale of production, efficient and reliable grading is essential, which can only be achieved through automation \[ 6, 7 \]. Being one of the most commonly cultivated temperate fruits, inspection is necessary to check its size, shape, color and surface defects \[ 8 - 10 \]. Traditionally, manual inspection has been the predominant method for assessing the fruit quality, both in orchards and sorting facilities. However, these methods are inherently labor-intensive, time-consuming, and prone to subjective errors, particularly given the scale of commercial apple production \[ 11 \]. Automated systems leveraging advanced imaging and machine learning techniques are increasingly being deployed \[ 12 - 14 \]. Apple orientation significantly impacts machine vision's ability to accurately capture and analyze surface features, leading to potential misclassification due to uneven feature extraction \[ 4, 15 - 17 \]. Irregular apple rotation and positioning on conveyors, caused by size, shape, and over-packing, leads to incomplete surface data and complex multi-camera tracking challenges in automated inspection \[ 18 - 22 \]. Techniques like Fourier descriptors, while effective in controlled environments, struggle with real-world complexities where apples slip or remain stationary, highlighting the need for more robust solutions \[ 20, 23, 24 \]. Existing apple inspection technologies lack comprehensive research on issues like apples getting stuck, over-packed, or experiencing irregular rotation due to size, shape, and bouncing \[ 7, 10, 25 - 27 \]. You Only Look Once (YOLO) models are among popular approaches of automated apple inspection. These models excel in real-time object detection, offering fast and accurate identification and localization of apples in images. Their ability to process large volumes of data quickly make them a practical choice for largescale inspection tasks. Additionally, it can be trained to detect apples in various orientations and sizes, making it versatile in different inspection environments. However, YOLO models also face challenges in handling irregular rotations. When apples are not oriented properly, or if their surfaces are partially obscured, their detection accuracy can suffer. This limitation means that YOLO might struggle to provide a complete or accurate information, especially when apples are rotating unpredictably or are partially visible \[ 3, 4 \]. The main contributions of this study are as follows: For the first time, this study integrates a more advanced

backbone architecture into the YOLOv5 model, by replacing the original C3 modules with a Convolutional Block Attention Modules (CBAM), significantly enhancing its detection capabilities for apples in multiple orientations. Secondly, the study introduces a novel method for detecting and analyzing the full-surface of apples, addressing the gaps left by previous studies that focused only on partial surfaces or specific areas of apples. This approach improves the completeness of surface data in automated inspections. Finally, by considering both the full-surface and multiple orientations, this research optimizes the efficiency of automated sorting and quality control systems, reducing losses and ensuring more consistent apple quality detection. Figure  1 illustrates the complete process of apple full surface detection, from image acquisition and preprocessing to visualization of detection results. This process aims to accurately identify the entire surface of apples.

**Materials and methods** **Sample selection** The physical dimensions of different varieties of apples were obtained by a manual vernier caliper (111103 V-10G, Guilin Guanglu Measuring Instrument Co., Ltd., Guangxi, China), a renowned company in precision measurement tools. The caliper provides an accuracy of ± 0.02 mm, making it suitable for reliable and consistent measurements. The minimum height-Diameter *H* 1, maximum height in mm-Diameter *H* 2, equatorial diameter *D* of apples, and weights were taken using accurate weighing scales in grams (Fig.  2 ). These measurements are crucial for knowing variability in size and shape of the apple samples. The samples were then positioned under the camera at a distance of approximately 25 cm/250 mm \[ 26, 28, 29 \]. Data acquisition was carried out by capturing the conveyor's movement in real-time and storing it as a video file. This video was later manually cropped for each individual apple.

**Experimental environment** A windows 11 pro  ×  64-bit operating system was used for training and testing the experimental models in this study. The experimental programming environment is Python 3.11.7, with Cudnn for GPU acceleration, and apple hierarchical model training is implemented using PyTorch 1.7 deep learning framework. A description of the experimental environment is given in Table  1. The model was trained with a weight decay coefficient of 0.001, a learning rate of 0.917, and a maximum of 16 training batches. The Intersection over Union (IoU) threshold was set at 0.5. Figure  3 illustrates a flow-chart depicting the overall training process.

Page 3 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

**Image acquisition and data augmentation** ***Image acquisition*** In this study, 120 apples were randomly selected, of which 60 were 'Fuji' apples and 60 were 'Golden Delicious'. These 2 varieties have been chosen because of their popularity and availability in almost all markets, besides showing variable characteristics regarding texture, color, and surface structure. Apples were selected within a diameter of 70 − 110 mm range and thus represent a good approximation of sizes that show up at the commercial markets \[ 30, 31 \]. For every apple analysis and detection, the detection on the whole surface had its surface divided into 16 distinct groups labeled as A to P. This is the methodology of segmentation, and it is used here because it was necessary to outline a model that would serve as an indicator in the complete detection of the apple's surface. Segmenting this apple into such regions does not allow even a part of the surface to remain unaccounted for. In this kind of division, the 16 groups formed correspond exclusively to a certain portion of the apple's surface and have been lettered from A to P. This systematic labeling helps in tracking specific areas of apples with ease. It allows for clear and well-detailed comparison of an apple's surface across all sections, which is useful when considering the detection and analysis of surface features that include color variations, textures, and other possible defects \[ 4 \].

The overall workflow of image processing for augmented image generation is illustrated in Fig.  4. It starts with an image video using a roller system, progresses through image extraction and annotation. Augmented images include tiling, horizontal mirroring, vertical mirroring and combined horizontal and vertical mirroring of the annotated images, producing a number of augmented images, and forming an augmented image dataset. The machine is made up of an industrial camera (MV-CB013-A0UM-C, Hikrobot, Hangzhou, Zhejiang, China) and six bar-shaped light sources \[ 3 \] (LSNBLI22045-W, Dongguan, Shenzhen, China). Each channel consists of two screw conveyors equipped with variable-pitch threads, which facilitate the separation and singulation of apples \[ 32 \]. In addition to transporting the apples, the two conveyors rotate in the same direction, using friction with the apples to rotate them, thereby ensuring that the grading system captures the complete surface information of the apples. The camera is fixed at a height of 537 mm from the conveyors, covering an area of 800 mm  ×  600 mm, allowing it to simultaneously capture motion videos of apples in 3 channels. The camera operates at a frame rate of 20 FPS, with apples moving within the field of view for 4 − 6  s, allowing each apple to be captured in at least 80 frames. To improve image quality and ensure segmentation accuracy, 6 bar-shaped light sources are installed on both sides of the apple

**Fig. 1 ** Overall study procedure for the full-surface detection of apples

Page 4 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

## movement direction for illumination. A CPU (Intel ®

Core ™ i9-14900HX, Santa Clara California, USA) and a GPU (NVIDIA GeForce RTX 4060, Santa Clara California, USA) are used to process the captured videos \[ 16 \].

## Dataset annotation

The apple images were annotated using MakeSense ( <https://​www.​makes​ense.​ai/> ), a user-friendly annotation tool, which enabled precise labeling of image categories

**Fig. 2 ** ( **A** ) Apple size measurement; ( **B** ) Apple shape index; ( **C** ) Maximum length; ( **D** ) Maximum cross-sectional diameter; ( **E** ) Diameter of outer circle; ( **F** ) Vernier caliper; ( **G** ) Weighing balance **Table 1**   Experimental environment

| Computer configuration | Specific parameters |
|:--- |:--- |
| CPU | Intel® Core™ i9-14900HX |
| GPU | NVIDIA GeForce RTX 4060 |
| Operating system | Windows 11 pro |
| Random access memory | DDR5 32G |
| CUDA | 12.5 | CPU Intel ® Core ™ i9-14900HX

# GPU NVIDIA GeForce RTX 4060 Operating system Windows 11 pro Random access memory DDR5 32G

# CUDA 12.5

Page 5 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

and bounding boxes. The annotations were saved in XML format, following the Pascal VOC standard, that provided detailed object information along with their spatial coordinates within each image. To further enhance the dataset's diversity and robustness, data augmentation techniques were applied using Python 3.11.7. These techniques included horizontal and vertical mirroring to create flipped versions of the images, multi-angle rotation to capture various orientations, and image tiling to zoom in on smaller regions of interest. This augmentation not only increased the dataset size but also improved its variability, helping it generalize better during training. After the augmentation, the dataset was carefully divided into training, test, and validation sets with a 7:2:1 ratio using a stratified random splitting method. This was performed to minimize bias and ensure that each set is representative of the overall dataset, thereby providing a robust evaluation of our model's generalization capabilities. Regarding, Kolmogorov-Smirnov (KS) grouping, while it is a powerful technique for ensuring similar statistical distributions across groups, stratified random split was found to be sufficient for our dataset given its characteristics and the specific goals of maintaining class balance. This ensured that the model could learn from the majority of the data while also being tested

and validated on independent subsets. Since the original annotations were in XML format, they were converted to YOLO format to ensure compatibility with the YOLOv5 framework. This conversion was essential for smooth integration into the training pipeline. With this enriched and well-structured dataset, the YOLOv5 model was equipped with a diverse and comprehensive set of data, improving its ability to detect the full surface of apples under various conditions \[ 33 - 35 \]. Table  2 shows the distribution of original versus augmented images for various datasets, sorted by orientation or condition (e.g., "Stem up", "Stem down", "Sideways", and "Diagonal"). The table clearly shows that the augmented images in the training dataset significantly outnumbered the original images for each orientation. This augmentation technique guarantees that the training data is more diverse and stronger, enabling the model to train from an extensive variety of orientation conditions. In particular, for each orientation, the training dataset is expanded using data augmentation techniques, and thus a substantial increase in the number of images is observed with respect to the original dataset. No augmentation was applied in the validation and test datasets. This provides an unbiased assessment of the model's generalization capability, as using the data that still resembles

**Fig. 3 ** Flow-chart of the overall training process

Page 6 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

## the original, unprocessed circumstances guarantee the

model's effectiveness retains its basis in real-world applications, rather than operating under altered conditions. The study proposed expanding the training set, through data augmentation while keeping the validation and test sets unchanged, this strategy enhances model performance without compromising interpretability and fairness in evaluation.

## YOLOv5

YOLOv5, an improved version of YOLOv3, which can transform object detection into a regression problem. Compared to YOLOv4, YOLOv5 offers better accuracy and speed balance \[ 36 \]. YOLOv5's architecture consists of three main components: a backbone, a neck, and a detection head. The backbone uses the CSP-Darknet53 structure, incorporating CBS, C3, and SPPF modules. CBS combines Conv, BN, and SiLU activation functions. The C3 module, key for residual feature learning, has 2 branches-one with Bottlenecks and convolutions, the other with a basic convolution. The SPPF module resolves multi-scale object detection by integrating MaxPool2d

**Fig. 4 ** Overall workflow of image processing for augmented image generation

**Table 2**   Details of the dataset for the various orientations of apples

**Orientation** **Dataset** **Number of ** **original images** **Number of ** **augmented ** **images** Stem up Training 5 076 Validation Test Total 1 208 5 438 Stem down Training 1 770 5 310 Validation Test Total 2 526 6 068 Sideways Training 1 804 5 412 Validation Test Total 2 591 6 199 Diagonal Training 1 804 5 412 Validation Test Total 2 591 6 199

Page 7 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

at varying sizes. With a 640  ×  640 input, the backbone outputs feature maps of 80 \times 80 \times 128, 40 \times 40 \times 256, and 20  ×  20  ×  512. The path aggregation network functions as the neck \[ 37 \]. Like YOLOv3, YOLOv5 uses three detection heads to detect small (80  ×  80  ×  128), medium (40 × 40 × 256), and large objects (20 × 20 × 512). The feature maps are divided into grids, and the k-means algorithm generates anchor boxes for predicting object boundaries. Each detection box produces a feature vector containing the predicted center ( *x*, *y* ), width, height, confidence score, and class probability. Non-maximum suppression removes redundant boxes, and the final detection is rescaled to match the original image size \[ 38 \]. YOLOv5's architecture includes 5 scales: YOLOv5n, YOLOv5s, YOLOv5m, YOLOv5l, and YOLOv5x (nano to extra-large). It takes 640  ×  640 images, dividing them into cells to predict bounding boxes and confidence scores for each object \[ 39, 40 \]. Fig.  5 shows the original YOLOv5 network structure. The structure of the enhanced YOLOv5 is shown in Fig.  6, Its basic structure includes the Focus module, the CBS module, the SPP module, and the C3 module; the Focus module is used to subsample the input image without information loss to achieve faster computation, and the SPP module serves to address the problem of

inconsistent input image size through multiple receptive field fusion. The backbone network is composed mainly of the CBS module and the C3 module stacked in series to extract feature information from images. The neck network is designed using a strategy of fusing a feature pyramid network (FPN) and pixel aggregation network (PAN) to increase feature reuse and better exploit the extracted features. Finally, the detection head performs a prediction with these extracted image features and outputs the location and category information of the object.

***Model evaluation indicators*** In order to accurately evaluate the detection performance of the model on the surface of apples, 5 evaluation indicators are used: precision (P), recall (R), F1-score, average precision (AP), mean average precision (mAP) \[ 41 - 46 \]. Equations  ( 1 - 5 ) show the formulas for P, R, F1, AP, and mAP.

# (1) $$ P = $$ TP TP + FP

# (2) $$ R = $$ TP TP + FN

**Fig. 5 ** Structure of original YOLOv5 model

Page 8 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

*Q* represents the total number of classes, Ap ( *k* ) indicates the AP value of the *k* th class, and *k*   =  16 in this study.

**Results and discussions** **Experimental results and comparative analysis** The accuracy and fairness of classifications are dependent on the orientation of the apples when sorting machines operate with apples on conveyor belts \[ 4 \]. Images of apples moving across a conveyor are shown in Fig.  7 in various orientations stem up (Fig.  7 A), stem down (Fig.  7 B), sideways (Fig.  7 C), and diagonal (Fig.  7 D). Tables  3 and 4 provide a summary of the performance metrics for different detection algorithms. The precision rates are specifically obtained from our model's performance when analyzing data acquired from the best (3) F1 −score = 2PR

# P + R (4) $$ AP(k) = $$

# P ( R ) dR

# (5) mAP = Q 1 AP ( k )

# Q

orientations of apple fruits **.** Our methodology involves a full surface detection approach, which systematically presents all sides of the apple including its top, bottom, sideways, and diagonal orientations **.** This comprehensive capture process ensures that optimal perspectives are obtained, which are then utilized for subsequent analysis. Table  3 provides a comprehensive comparison of different YOLOv5 models, focusing on their performance in detecting 'stem up' and 'stem down' orientations. Several key metrics are evaluated, including P, R, mAP0.5 (mAP at 50% intersection over union), mAP0.5:0.95 (mAP across IoUs from 50% to 95%), and F1-score, which balances P and R. The result obtained reveals that the improved versions of YOLOv5 models consistently outperform their non-improved counterparts across all metrics. For instance, improved-YOLOv5l outperforms YOLOv5l with an increase in P (76.80%) and R (82.30%), resulting in a significant rise in mAP0.5 (86.00%) and a notable  F1-score of 79.46%. Similarly, improvedYOLOv5m shows enhancements in both P and R, leading to a higher mAP0.5 of 79.90% and an improved F1-score of 75.28% compared to the original YOLOv5m. In the 'stem up' orientation, improved-YOLOv5x achieves the best performance with an F1-score of 75.28%, demonstrating the potential of optimization to enhance

**Fig. 6 ** Structure of enhanced YOLOv5 model

Page 9 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

## detection accuracy for more complex tasks. When exam

ining the 'stem down' orientation, improved-YOLOv5n leads the pack, boasting an impressive F1-score of 85.72%, with superior R (88.40%) and R (83.20%), along with the highest mAP0.5:0.95 value (52.30%). This highlights the model's capability to handle difficult detection

## tasks, improving the overall performance in varied ori

entations. On the other hand, models like YOLOv5x and YOLOv5s show good performance but lag behind their improved versions, particularly in F1-scores and mAP0.5:0.95. The improved YOLOv5 models, especially improved-YOLOv5n and improved-YOLOv5x,

**Fig. 7 ** Apples on a conveyor and visual comparisons of YOLOv5 model performance across different orientations. ( **A** ) Stem up; ( **B** ) Stem down; ( **C** ) Sideways; and ( **D** ) Diagonal

Page 10 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

**Table 3**   Comparison of the performance metrics for stem up and stem down orientations

**Model** **P (%)** **R (%)** **mAP0.5 (%)** **mAP0.5:0.95 (%)** **F1-score** **Stem up**

| YOLOv5l | 75.30 | 55.80 | 71.30 | 41.30 | 64.10 |
|:--- | ---: | ---: | ---: | ---: | ---: |
| Improved-YOLOv5l | 76.80 | 82.30 | 86.00 | 51.40 | 79.46 |
| YOLO5m | 72.70 | 62.10 | 72.70 | 41.90 | 66.98 |
| Improved-YOLOv5m | 88.30 | 65.60 | 79.90 | 47.20 | 75.28 |
| YOLOv5n | 72.70 | 62.10 | 72.70 | 41.90 | 66.98 |
| Improved-YOLOv5n | 80.80 | 76.20 | 87.10 | 51.30 | 78.43 |
| YOLOv5s | 75.90 | 74.70 | 78.60 | 46.40 | 75.30 |
| Improved-YOLOv5s | 79.50 | 55.60 | 68.90 | 39.50 | 65.44 |
| YOLOv5x | 75.30 | 55.80 | 71.30 | 41.30 | 64.10 |
| Improved-YOLOv5x | 88.30 | 65.60 | 79.90 | 47.20 | 75.28 |

Improved-YOLOv5l **76.80** **82.30** **86.00** **51.40** **79.46**

# YOLO5m 72.70 62.10 72.70 41.90 66.98

Improved-YOLOv5m 88.30 65.60 79.90 47.20 75.28 YOLOv5n 72.70 62.10 72.70 41.90 66.98

Improved-YOLOv5n 80.80 76.20 87.10 51.30 78.43 YOLOv5s 75.90 74.70 78.60 46.40 75.30

Improved-YOLOv5s 79.50 55.60 68.90 39.50 65.44 YOLOv5x 75.30 55.80 71.30 41.30 64.10

Improved-YOLOv5x 88.30 65.60 79.90 47.20 75.28 **Stem down**

| YOLOv5l | 79.60 | 84.50 | 87.60 | 50.90 | 81.98 |
|:--- | ---: | ---: | ---: | ---: | ---: |
| Improved-YOLOv5l | 86.70 | 78.10 | 89.90 | 53.10 | 82.18 |
| YOLOv5m | 79.30 | 79.10 | 85.50 | 50.20 | 79.20 |
| Improved-YOLOv5m | 79.30 | 87.10 | 90.20 | 52.40 | 83.20 |
| YOLOv5n | 78.20 | 78.10 | 84.70 | 49.30 | 78.15 |
| Improved-YOLOv5n | 88.40 | 83.20 | 91.70 | 52.30 | 85.72 |
| YOLOv5s | 82.70 | 80.10 | 85.50 | 49.00 | 81.38 |
| Improved-YOLOv5s | 85.00 | 85.30 | 90.30 | 53.00 | 85.15 |
| YOLOv5x | 83.20 | 73.50 | 85.40 | 49.30 | 78.05 |
| Improved-YOLOv5x | 81.50 | 83.90 | 89.40 | 50.70 | 82.68 |

Improved-YOLOv5l 86.70 78.10 89.90 53.10 82.18 YOLOv5m 79.30 79.10 85.50 50.20 79.20

Improved-YOLOv5m 79.30 87.10 90.20 52.40 83.20 YOLOv5n 78.20 78.10 84.70 49.30 78.15

Improved-YOLOv5n **88.40** **83.20** **91.70** **52.30** **85.72** YOLOv5s 82.70 80.10 85.50 49.00 81.38

Improved-YOLOv5s 85.00 85.30 90.30 53.00 85.15 YOLOv5x 83.20 73.50 85.40 49.30 78.05

Improved-YOLOv5x 81.50 83.90 89.40 50.70 82.68

**Table 4**   Comparison of the performance metrics for sideways and diagonal orientations

**Model** **P (%)** **R (%)** **mAP0.5 (%)** **mAP0.5:0.95 (%)** **F1-score** **Sideways**

| YOLOv5l | 88.00 | 89.40 | 92.00 | 53.60 | 88.70 |
|:--- | ---: | ---: | ---: | ---: | ---: |
| Improved-YOLOv5l | 88.20 | 93.10 | 95.00 | 56.70 | 90.58 |
| YOLOv5m | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
| Improved-YOLOv5m | 87.50 | 90.40 | 94.60 | 56.10 | 88.93 |
| YOLOv5n | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
| Improved-YOLOv5n | 87.90 | 85.40 | 93.60 | 55.20 | 86.63 |
| YOLOv5s | 83.60 | 83.00 | 87.30 | 51.60 | 83.30 |
| Improved-YOLOv5s | 86.50 | 89.10 | 93.30 | 55.20 | 87.78 |
| YOLOv5x | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
| Improved-YOLOv5x | 89.00 | 88.10 | 94.30 | 56.00 | 88.55 |

Improved-YOLOv5l **88.20** **93.10** **95.00** **56.70** **90.58** YOLOv5m 86.10 82.30 89.60 52.70 84.16

Improved-YOLOv5m 87.50 90.40 94.60 56.10 88.93 YOLOv5n 86.10 82.30 89.60 52.70 84.16

Improved-YOLOv5n 87.90 85.40 93.60 55.20 86.63 YOLOv5s 83.60 83.00 87.30 51.60 83.30

Improved-YOLOv5s 86.50 89.10 93.30 55.20 87.78 YOLOv5x 86.10 82.30 89.60 52.70 84.16

Improved-YOLOv5x 89.00 88.10 94.30 56.00 88.55 **Diagonal**

| YOLOv5l | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
|:--- | ---: | ---: | ---: | ---: | ---: |
| Improved-YOLOv5l | 88.20 | 93.10 | 95.00 | 56.70 | 90.58 |
| YOLOv5m | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
| Improved-YOLOv5m | 87.50 | 90.40 | 94.60 | 56.10 | 88.93 |
| YOLOv5n | 86.10 | 82.30 | 89.60 | 52.70 | 84.16 |
| Improved-YOLOv5n | 87.50 | 90.40 | 94.60 | 56.10 | 88.93 |
| YOLOv5s | 83.60 | 83.00 | 87.30 | 51.60 | 83.30 |
| Improved-YOLOv5s | 88.70 | 89.04 | 95.00 | 56.50 | 88.87 |
| YOLOv5x | 87.70 | 88.30 | 91.50 | 54.20 | 87.10 |
| Improved-YOLOv5x | 87.50 | 90.40 | 94.60 | 56.10 | 88.93 |

Improved-YOLOv5l **88.20** **93.10** **95.00** **56.70** **90.58** YOLOv5m 86.10 82.30 89.60 52.70 84.16

Improved-YOLOv5m 87.50 90.40 94.60 56.10 88.93 YOLOv5n 86.10 82.30 89.60 52.70 84.16

Improved-YOLOv5n 87.50 90.40 94.60 56.10 88.93 YOLOv5s 83.60 83.00 87.30 51.60 83.30

Improved-YOLOv5s 88.70 89.04 95.00 56.50 88.87 YOLOv5x 87.70 88.30 91.50 54.20 87.10

Improved-YOLOv5x 87.50 90.40 94.60 56.10 88.93

Page 11 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

demonstrate significant advancements in P, R, and overall detection performance, proving the value of model optimization in enhancing both the efficiency and accuracy of apple full surface detection systems in multiple orientations. A comparison of various version of YOLOv5 models is provided in Table  4, highlighting their performance across two distinct orientations: Sideways and Diagonal. It includes original versions of YOLOv5 (YOLOv5l, YOLOv5m, YOLOv5n, YOLOv5s, YOLOv5x) and their corresponding improved versions, which are denoted with the 'Improved' prefix. The metrics analyzed include P, R, mAP0.5, mAP0.5:0.95, and F1-Score, all of which offer insights into the models'  overall ability to detect full-surface of apple fruits with accuracy, robustness, and efficiency. The 'Improved-YOLOv5l' model excels in both orientations, achieving the highest P (88.20%) and R (93.10%), which demonstrates its strong capability in correctly identifying objects with minimal false negatives. This model also leads in F1-score (90.58%), an important metric combining both precision and recall into one value to assess the model's overall effectiveness. The improved models consistently outperform their base counterparts, especially in terms of recall, which signifies a better ability to detect true positives. The improvedYOLOv5m shows enhanced performance with a higher R (90.40%) and F1-Score (88.93%) compared to its base version, YOLOv5m, which lags behind with R (87.50%) and F1-Score (88.09%). While the 'Improved' versions generally show superior performance, the base models such as YOLOv5l and YOLOv5x maintain strong results, especially in mAP0.5 and mAP0.5:0.95. YOLOv5x, achieves good R (82.30%) and performs reasonably well in both mAP0.5 (89.60%) and mAP0.5:0.95 (52.70%). However, YOLOv5s, which is designed to be a lighter and faster version, shows slightly weaker results across the board, particularly in terms of mAP0.5:0.95, indicating that its reduced complexity comes at the cost of precision and recall. This underscores the trade-off between model size and performance, where lighter models like YOLOv5s may be suitable for applications requiring faster inference times but are less effective in accuracy-sensitive tasks. Several factors likely contribute to the higher performance in the sideways orientation. The apple typically presents a larger, more consistent, and less occluded surface area to the camera compared to, for example, topdown or bottom-up views where the stem or calyx might obscure a significant portion, or frontal views where overlapping fruits are more common. A larger, clearer visible surface provides more robust visual cues for the model to learn from. The sideways orientation offers the model a more unambiguous, geometrically consistent, and richly featured view of the apple, leading to

more accurate bounding box predictions and thus higher F1-scores and mAP.

***Stem up orientation*** Figure  8 A shows that the distribution of instances across classes in the stem up orientation is nearly equal, with approximately 14 instances per class. Based on this analysis, it appears that apples are positioned in a more or less neutral position, whose orientation is consistent across all fruits. The features that can be seen from this perspective are therefore relatively uniform, leading to an accurate representation of classes. A uniform class distribution may be attributed to features such as the top of the apple and its stem, which may be more easily recognizable and consistent across instances when viewed from this orientation. Moreover, the low degree of variation in the instance count across classes implies that the default position minimizes the distortions that may be caused by orientation-related biases.

***Stem down orientation*** The variability in instance counts becomes more pronounced in the stem down orientation (Fig.  8 B). Certain classes, such as A, G, and J, exhibit higher numbers of instances, indicating that the apple's features are more distinctive in this position. As the apple rotates, characteristics, such as base shape, color, or texture, become more easily visible, allowing the machine learning system to classify specific types of apples more accurately. Some apples may be easier to distinguish from the bottom due to their more pronounced or symmetrical shapes. However, this orientation limits the visibility of all surfaces, leading to variations within the classes.

***Sideways orientation*** The sideways orientation increases the total number of instances and further enhances the variation between classes (Fig.  8 C). In this orientation, apples are rotated to allow the machine vision system to view their sides, clearly highlighting the width of the apple, skin texture, and side markings. Classes such as A, G, and H have higher counts, likely because apples with more elongated or asymmetrical shapes are more noticeable from the side, emphasizing their distinctive features. On the other hand, classes like P and N appear less frequently in this orientation, suggesting that apples in these categories are more uniform or symmetrical, making them less noticeable from the side. This orientation leads to a wide variation in instance counts, with some classes being overrepresented while others are underrepresented in the dataset.

Page 12 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

***Diagonal orientation*** The wide variations in sideways orientation is extended further within the diagonal orientation (Fig.  8 D), where the count often surpasses 30, showing further complexity with respect to data augmentation. In this orientation, apples are rotated to an angle such that the camera captures many of their surfaces. Everything can be seen from top to sides of the apple, with all asymmetries and special textures. The classes A and G keep on dominating due to their unique features such as elongated shape or big surface features. This orientation results in a higher total number of instances; thus, it provides a more complete training dataset but introduces extra variability in the class distribution due to the increased number of instances. Such increased diversity might be helpful for some classes, while others might remain underrepresented.

***Impact of rotation on the distribution of instances*** Depending on the orientation, some surface labels or letters are not evenly distributed across classes, leading to biases in the training of the model. It could be hard for

the model to learn distinguishing features for sparsely populated classes, such as P and N. Due to this imbalance, the underrepresented classes may be less accurately classified, and the model will tend to prefer the classes that show up more often, such as A, G, H, etc. Rotations should carefully be kept so that significant bias is not introduced while performing data augmentation increasing the diversity. These could be overcome by techniques such as class balancing, oversampling of classes that are underrepresented, or data augmentation so that all classes are equally represented. Finding the performance of the model for all orientations, not just the most common or prominent ones, is important to ensure fairness and accuracy.

**Comparative analysis of precision, recall, and mAP ** **across multiple orientations** The YOLOv5l (large version) demonstrated the bestperforming model for "stem up", whereas YOLOv5n (nano version) provided the best results for "stem down". It is shown in Fig.  9 that the original YOLOv5 model, shown in Figs.  9 A and C, is compared with the enhanced YOLOv5 model, shown in Figs.  9 B and D. Orientations of

**Fig. 8 ** Instances of different orientations of apple. ( **A** ) Stem up; ( **B** ) Stem down; ( **C** ) Sideways; and ( **D** ) Diagonal. The full-surface of each apple fruit was divided into 16 regions (labeled A to P)

Page 13 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

"stem up" and "stem down" highlights trends of improvement and decline, respectively. Figures  9 A and C indicate that metrics such as precision, recall, and mAP values improved steadily after an initial period of instability. As the training progresses, these upward trends become more consistent, reflecting the gradual optimization of the model. The recall and precision metrics in Fig.  9 C show significant "stem down" dips, perhaps caused by incorrect gradient estimates or underfitting for the early epochs. As shown in Figs.  9 B and D, the enhanced YOLOv5 model exhibits much stronger and more stable "stem up" trends. In contrast to the original YOLOv5, metrics such as mAP0.5 and mAP0.5:0.95 have risen steadily, reaching higher overall values than the original YOLOv5. The improvements suggest the enhanced model is able to learn more effectively and converge more rapidly. Additionally, the enhanced YOLOv5 exhibits a minimal drop in precision and recall during the initial epochs, as well as minimal "stem down" fluctuation. As a result, the training

process appears to be more stable and robust. Fig.  9 displays the best results for stem up and stem down orientations, with metrics presented in Figs.  9 A and C for the original YOLOv5 and (Figs.  9 B and D) for the enhanced YOLOv5. The best results can be seen in Fig.  9 A from the original YOLOv5 and Fig.  9 B from the enhanced YOLOv5. In Fig.  9 B, the enhanced YOLOv5 is significantly more stable and achieves higher metrics than the original. As shown in Fig.  9 C of the original YOLOv5, the initial dips are more pronounced, whereas the improved model in Fig.  9 D significantly reduces these early dips, resulting in a more consistent and smooth performance improvement. A better stem up trend and reduced dips are evident in the enhanced YOLOv5 model, compared to the original. According to these results, the improvements made to the YOLOv5 architecture resulted in better convergence, improved metrics, and increased overall stability. Fig.  10 shows a comparison of performance between the original and enhanced YOLOv5 models for both

**Fig. 9 ** Comparison of best evaluation indicators for stem up and stem down orientations. ( **A** ) and ( **C** ) Original YOLOv5; and ( **B** ) and ( **D** ) Enhanced YOLOv5

Page 14 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

sideways and diagonal orientations. Metrics such as precision, recall, mAP0.5, and mAP0.5:0.95 are displayed for each subplot. The metrics exhibited in Figs.  10 A and C show inconsistent trends across both orientations for the original YOLOv5. The recall and mAP values are exhibiting notable dips and fluctuations, indicative of unstable training dynamics. While the precision and recall values of the model increase gradually, they are still uneven, which shows the struggle of this model in capturing nuances for the sideways and diagonal orientations precisely. By contrast, Figs.  10 B and D from the improved YOLOv5 model demonstrate much improvement; in both orientations, metrics are stably and smoothly converged along with the training process. It gives a better mAP0.5 and mAP0.5:0.95 than the original YOLOv5, hence justifying the architectural enhancements of the model. Also, precision and recall trends show less variability across epochs. Among them, the large version of YOLOv5, was found to be the most effective model in terms of both sideways and diagonal orientations. It is stronger in convergence and reaches higher precision, recall, and mAP of the best

performance consistently across all metrics. In particular, the improved YOLOv5 model exhibits greatly improved performance for both diagonals and sideways compared to the original YOLOv5. Further, these validate its superior stability and accuracy as proof that the architectural improvements have made it optimal for such challenging tasks. Figures  10 A and C depict original YOLOv5 and Figs.  10 B and D for the enhanced version. The above subplots give the proper idea about the performance and improvements brought in by the models. The original YOLOv5 model is oriented in a stem up position evaluated in Fig.  10 A; from the heatmap, the model seems to classify most of the instances correctly. However, offdiagonal elements show misclassifications for some categories, indicating some inconsistencies. Besides, not all values along the diagonal are uniform, which means some classes have better classification accuracy than others. A comparison of performance of enhanced YOLOv5 models for analyzing 'stem up' versus 'stem down' orientations is shown in Fig.  11. There are 2 subplots Figs.  11 A and C showing the original YOLOv5 model, and 2 subplots Figs.  11 B and D showing the enhanced YOLOv5

**Fig. 10 ** Comparison of best evaluation indicators for sideways and diagonal orientations. ( **A** ) and ( **C** ) Original YOLOv5; and ( **B** ) and ( **D** ) Enhanced YOLOv5

Page 15 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

model. Comparing these subplots shows how the models perform and improve through modifications. For the 'stem up' orientation, the original YOLOv5 model evaluated in Fig.  11 A has exhibited reasonably enough diagonal dominance that its model correctly classifies a majority of the instances. Although there is some misclassification for some categories off the diagonal, it has performed with some inconsistency. Moreover, the values along the diagonal are not uniform, suggesting that the classification accuracy varies between class. That would include Fig.  11 D, which is the enhanced YOLOv5 on stem down orientation. Similar to the structure shown in Fig.  11 B, it is much enhanced, meaning for good diagonality, the percentage of elements off the diagonal is low, making the class accuracy even higher. Therefore, compared to its original model, enhanced outperformed stability and higher metrics, specifically the metric of stem down orientation, hence proved robust and effective. A significant improvement has been made in the performance of YOLOv5, with more stable trends, higher metrics, and a reduction in errors in both 'stem up' and 'stem down' orientations. Figure  12 illustrates how models or configurations perform along sideways and diagonally. Diagonal patterns indicate correct classifications, whereas off-diagonal elements indicate errors or

misclassifications. A heatmap was used to compare two model configurations, such as the original and enhanced versions of YOLOv5. Specifically, classification accuracy and error patterns are evaluated based on diagonal and sideways orientations. Heatmaps with diagonal orientations indicate correct predictions, where the predicted category matches the actual category. As can be seen in Figs.  12 A and C, which represent the original configurations, the diagonal patterns are less pronounced, indicating moderate classification accuracy but with a variety of inconsistencies across categories. Conversely, Figs.  12 B and D, which represent enhanced configurations, show stronger and more distinct diagonal lines. As a result, the enhanced models are able to achieve greater accuracy and stability during classification, thus resulting in better identification of categories. In the heatmaps, sideways orientations correspond to off diagonal intensities, highlighting instances when predictions do not align with the actual labels, resulting in misclassifications. There is a lot of off-diagonal noise in the Figs.  12 A and C, showing that the original models have more tendencies to misclassify, especially between some categories. Figures  12 B and D show a great reduction in off-diagonal noise. It is obvious that this can be justified by the enhanced configurations, due to their

**Fig. 11 ** Comparison of heatmpas for for stem up and stem down orientations. ( **A** ) and ( **C** ) Original YOLOv5; and ( **B** ) and ( **D** ) Enhanced YOLOv5. The full-surface of each apple fruit was divided into 16 regions (labeled A to P)

Page 16 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

general ability in reducing errors, hence, more stable and robust performances appear for all categories. In all the heatmaps, the last column is the "Background" category. Indeed, it is assured that all configurations are performing reasonably well by the high intensity of this column. It can be seen from sharper and more uniform results yielded that the enhanced configurations of Figs.  12 B and D highlight their higher precision and stability in handling background elements. In terms of classification accuracy and error reduction, the enhanced configurations in Figs.  12 B and D outperform the original models. Indeed, their stronger diagonal trends and reduced sideways noise make them more capable of learning and generalizing. The enhanced configurations demonstrate greater reliability and stability when handling orientation-specific tasks, such as "stem up" and "stem down". With the improvements on the models, their performances across the categories have increased significantly. Color gradients from blue to red denote poor-to-higher values for each metric. The improved YOLO models outperform their original versions across all metrics, as evidenced by the prevalence of the red-shaded bars. Figures  13 A-D corresponds to a test of performance on a different orientation. Apart from orientation, the improved models of YOLOv5 performed better in several key aspects

compared to the standard versions, as shown in Tables  3 and 4. Notably, metrics such as precision, recall, and mAP were significantly enhanced, indicating the effectiveness of the improvements. The improved precision and recall have a recorded an increase in the improved model, indicating that these models are able to detect most of the true objects among the predictions. Improved models guarantee better accuracy according to mAP0.5, one common measurement of average precision at 0.5 IoU threshold. Also, the improved models perform well in the stricter range of mAP0.5:0.95, showing their robustness for any IoU threshold. Similarly, the F1-score, which balances precision and recall, confirms the superior detection capability of the improved variants. A consistent dominance of improved models in Fig.  13 demonstrates their robustness and adaptability. There is a strong advantage to be gained from improved YOLO variants in conditions requiring stringent detection capabilities. Such consistent performance gains emphasize the practical utility of the improved models for applications where high detection accuracy and reliability are essential, such as autonomous full surface detection. The differences in the detection performance across the different orientations could be attributed to multiple factors related to both the model structure and the algorithmic approach. In terms of model structure, the network

**Fig. 12 ** Comparison of heatmpas for sideways and diagonal orientations. ( **A** ) and ( **C** ) Original YOLOv5; and ( **B** ) and ( **D** ) Enhanced YOLOv5. The full-surface of each apple fruit was divided into 16 regions (labeled A to P)

Page 17 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

architecture, including the type and depth of convolutional layers, played a critical role in how well the model captured directional features. Convolutional layers that were not rotationally invariant struggled to detect features when the object was oriented differently. Additionally, pooling strategies employed in the network may have caused the loss of directional information, contributing to the observed performance variability. At the algorithmic level, data augmentation techniques, such as random rotations or flipping, enhanced the model's ability to generalize across various orientations. Without adequate augmentation, the model became biased toward detecting features from specific directions, leading to suboptimal performance when the input image's orientation varied. The loss function also played a significant role. The model struggled to adapt to different orientations if the loss function failed to account for directional variations or assign appropriate weights to orientationspecific features. Specifically, the primary conclusions that can be drawn from Fig.  13 are: based on Fig.  13 A, we observe that the system exhibits good performance when subjected to stem up orientations. Comparing the performance across Figs.  13 B-D, it becomes evident that performance is most consistent under orientation 'Sideways' and 'Diagonal'. The system maintains high accuracy within these orientation range. A small increase occurs at orientation 'Stem down'. This suggests the adaptability and strengths of multiple orientations changes concerning full surface detection. Overall, Fig.  13 demonstrates

the system's performance across all tested orientations. The system generally maintains good performance across multiple range of orientations. These findings are crucial for understanding the system's practical applicability and identifying areas for future improvement.

**Conclusion** In this study, an enhanced YOLOv5 model is proposed and validated for full surface detection of apples under various orientations in a sorting machine, addressing a crucial challenge in precision agriculture. With a robust backbone network, the proposed model outperforms the original YOLOv5 model in terms of precision, recall, mAP, and F1-score. According to the results, the enhanced YOLOv5 model significantly outperformed original methods, The precision rates (P) achieved were 76.80%, 88.40%, 88.20%, and 88.20%, while the recall rates (R) were 82.30%, 83.20%, 93.10%, and 93.10%, and mAPs were 86.00%, 91.70%, 95.00%, and 95.00%, for stem up, stem down, sideways, and diagonal orientations, respectively. Notably, the highest F1-score 90.58 and mAP 95.00% were achieved in the sideways orientation, demonstrating superior performance in this orientation. The experimental results demonstrate its reliability and accuracy, making it a promising solution for applications such as automated apples quality control. The study serves to demonstrate the potential of integrating deep learning models into agricultural systems in order to enhance efficiency and productivity. To further enhance its practical

**Fig. 13 ** Performance comparison of various YOLOv5 model variants. ( **A** ) Stem up; ( **B** ) Stem down; ( **C** ) Sideways; ( **D** ) Diagonal

Page 18 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

## application, future research can investigate the scalability

of this approach to other fruits as well as its integration with real-time agricultural machinery.

**Acknowledgements** This work was financially supported by the Key R&D Project of Autonomous Region (2024AAC05077), the Independent Innovation Special Project of the Academy of Agricultural Sciences (NGSB-2021-1-01), the National Key Research and Development Program of China (2023YFE0122600) and the 2115 Talent Development Program of China Agricultural University.

**CRediT authorship contribution statement** Conceptualization: M.H.K; Data curation: M.H.K, J.Y; Formal analysis: M.H.K; Funding acquisition: Z.Z, X.L (Xiaolong Li), X.L (Xu Li); Investigation: M.H.K, X.L (Xiaolong Li), B.H, X.L (Xu Li); Methodology: M.H.K; Project administration, resources: Z.Z; Software: M.H.K; Validation:, L.Y, W.K, M.Z, S.M, O.I.O; Visualization: Z.Z, M.M, A.A; Writing-original draft: M.H.K; Writing-review and editing: Z.Z, X.L (Xiaolong Li), B.H, X.L (Xu Li), L.Y, W.K, M.M, A.A, J.Y, M.Z, S.M, O.I.O. Allauthors have read and agreed to the published version of the manuscript.

**Data availability** No datasets were generated or analysed during the current study.

## Declarations

**Competing interests** The authors declare no competing interests.

Received: 24 April 2025   Revised: 25 June 2025   Accepted: 30 June 2025

**References** 1.  Mhamed M, Zhang Z, Hua W, et al. Apple varieties and growth prediction with time series classification based on deep learning to impact the harvesting decisions. Comput Ind. 2025;164:104191. <https://​doi.​> org/​10.​1016/j.​compi​nd.​2024.​104191. 2.  Mhamed M, Kabir MH, Zhang Z. Developments of the automated equipment of apple in the orchard: a comprehensive review. Towards Unmanned Apple Orchard Production Cycle: Recent New Technol. 2023:1-49. <https://​doi.​org/​10.​1007/​978-​981-​99-​6124-5\_1>. 3.  Yu J, Zhang Z, Li YF, et al. Apple size estimation method with 3D projection correction for in-field grading system. Sens Auton Syst. Springer Nature Singapore: Singapore. 2024, pp. 109-26. <https://​doi.​org/​10.​> 1007/​978-​981-​97-​7778-5\_5. 4.  Yu J, Zhang Z, Li YF, et al. In-field grading and sorting technology of apples: a state-of-the-art review. Comput Electron Agric. 2024;226:109383. <https://​doi.​org/​10.​1016/j.​compag.​2024.​109383>. 5.  Kolanowski W, Zakrzewska M. Apple processing wastes as potential source of new edible oil. J Food Nutr Res. 2019;58:92-8. 6.  Chopde S, Patil M, Shaikh A, et al. Developments in computer vision system, focusing on its applications in quality inspection of fruits and vegetables-a review. Agric Rev. 2017;38(2):94-102. <https://​doi.​org/​10.​> 18805/​ag.​v38i02.​7940. 7.  Eissa AHA, Khalik AA, Abdel A. Understanding color image processing by machine vision for biological materials. Struct Funct Food. 2012:227-274. <https://​doi.​org/​10.​5772/​50796>. 8.  Harris SA, Robinson JP, Juniper BE. Genetic clues to the origin of the apple. Trends Genet. 2002;18(8):426-30. <https://​doi.​org/​10.​1016/​s0168-​> 9525(02)​02689-6. 9.  Cornille A, Tatiana G, Marinus JMS, et al. The domestication and evolutionary ecology of apples. Trends Genet. 2014;30(2):57-65. <https://​doi.​org/​10.​> 1016/j.​tig.​2013.​10.​002. 10. Zhang B, Gu B, Tan G, et al. Challenges and solutions of optical-based  nondestructive quality inspection for robotic fruit and vegetable grading systems: a technical review. Trends Food Sci Technol. 2018;81:213-31. <https://​doi.​org/​10.​1016/j.​tifs.​2018.​09.​018>.

| 11. | Yan T, Mhamed M. Developments in automated harvesting equipment |
|:--- |:--- |
| for the apple in the orchard: review. Smart Agric Technol. 2024;9:100491. |  |
| https://​doi.​org/​10.​1016/j.​atech.​2024.​100491. |  |
| 12. | Mhamed M, Zhang Z, Yu J, et al. Advances in apple's automated |
| orchard equipment: a comprehensive research. Comput Electron Agric. |  |
| 2024;221:108926. https://​doi.​org/​10.​1016/j.​compag.​2024.​108926. |  |
| 13. | Melnychenko O, Savenko O, Radiuk P, et al. Apple detection with occlu- |
| sions using modified YOLOv5-v1. 2023 IEEE Int Conf Intell Data Acquis |  |
| Adv Comput Syst. 2023. https://​doi.​org/​10.​1109/​IDAAC​S58523.​2023.​ |  |
| 10348​779. |  |
| 14. | Melnychenko O, Scislo L, Savenko O, et al. Intelligent integrated system |
| for fruit detection using multi-uav imaging and deep learning. Sens. |  |
| 2024;24(6):1913. https://​doi.​org/​10.​3390/​s2406​1913. |  |
| 15. | Lefcourt AM, Narayanan P, Tasch U, et al. Orienting apples for imaging |
| using their inertial properties and random apple loading. Biosyst Eng. |  |
| 2009;104(1):64-71. https://​doi.​org/​10.​1016/j.​biosy​stems​eng.​2009.​06.​002. |  |
| 16. | Li Y, Yu J, Zhang Z, et al. Research on the fruit movement mecha- |
| nism of apple in-field sorting equipment. Sens. Auton. Syst. Springer |  |
| Nature Singapore: Singapore. 2024:127-45. https://​doi.​org/​10.​1007/​ |  |
| 978-​981-​97-​7778-5\_6. |  |
| 17. | Narayanan P, Marc Lefcourt A, Tasch U, et al. Theoretical aspects of orient- |
| ing fruit using stability properties during rotation. ASAE Annu Meet. |  |
| 2006:061144. https://​doi.​org/​10.​13031/​2013.​21093. |  |
| 18. | Wilson A, Ben-Tal G, Heather J, et al. Calibrating cameras in an industrial |
| produce inspection system. Comput Electron Agric. 2017;140:386-96. |  |
| https://​doi.​org/​10.​1016/j.​compag.​2017.​06.​014. |  |
| 19. | Bakker HH, Flemmer RC, Flemmer CL, et al. Coverage of apple surface for |
| adequate machine vision inspection. IEEE ­24th Int Conf Mechatronics and |  |
| Machine Vision in Practice (M2VIP), 2017.https://​doi.​org/​10.​1109/​M2VIP.​ |  |
| 2017.​82114​93. |  |
| 20. | Baek I, Byoung-Kwan C, Stephen AG, et al. A novel hyperspectral line-scan |
| imaging method for whole surfaces of round shaped agricultural prod- |  |
| ucts. Biosyst Eng. 2019;188:57-66.https://​doi.​org/​10.​1016/j.​biosy​stems​ |  |
| eng.​2019.​09.​014. |  |
| 21. | Sadegaonkar V, Wagh K. Automatic sorting using computer vision & |
| image processing for improving apple quality. Int J Innov Res Dev. |  |
| 2015;4(1):11-4. |  |
| 22. | Sofu MM, Er O, Kayacan MC, et al. Design of an automatic apple sorting |
| system using machine vision. Comput Electron Agric. 2016;127:395-405. |  |
| https://​doi.​org/​10.​1016/j.​compag.​2016.​06.​030. |  |
| 23. | Currie A, Ganeshanandam S, Noiton DA, et al. Quantitative evaluation of |
| apple (Malus × domestica Borkh.) fruit shape by principal component |  |
| analysis of fourier descriptors. Euphytica. 2000;111:221-7. https://​doi.​org/​ |  |
| 10.​1023/A:​10038​62525​814. |  |
| 24. | Paulus I, Schrevens E. Shape characterization of new apple cultivars by |
| fourier expansion of digitized images. J Agric Eng Res. 1999;72(2):113-8. |  |
| https://​doi.​org/​10.​1006/​jaer.​1998.​0352. |  |
| 25. | Flemmer C, Bakker H, Flemmer R. Analysis of the stochastic excursions of |
| tumbling apples. Comput Electron Agric. 2021;188:106362. https://​doi.​ |  |
| org/​10.​1016/j.​compag.​2021.​106362. |  |
| 26. | Neupane C, Pereira M, Koirala A, et al. Fruit sizing in orchard: a review |
| from caliper to machine vision with deep learning. Sens. 2023:23. https://​ |  |
| doi.​org/​10.​3390/​s2308​3868. |  |
| 27. | Sari YA, Gofuku A. Measuring food volume from RGB-depth image with |
| point cloud conversion method using geometrical approach and robust |  |
| ellipsoid fitting algorithm. J Food Eng. 2023;358:111656. https://​doi.​org/​ |  |
| 10.​1016/j.​jfood​eng.​2023.​111656. |  |
| 28. | Whitelock DP, Brusewitz GH, Stone ML. Apple shape and rolling orienta- |
| tion. Appl Eng Agric. 2006;22(1):87-94. https://​doi.​org/​10.​13031/​2013.​ |  |
| 20177. |  |
| 29. | Luo T, Zhou J, Zhang S, et al. Theoretical analysis and experimental |
| research on the apple auto-orientation based on flexible roller. Horticul- |  |
| turae. 2023;9(11):1235. https://​doi.​org/​10.​3390/​horti​cultu​rae91​11235. |  |
| 30. | Zhang P, Shen B, Ji H, et al. Nondestructive prediction of mechanical |
| parameters to apple using hyperspectral imaging by support vector |  |
| machine. Food Anal Methods. 2022;15(5):1397-406. https://​doi.​org/​10.​ |  |
| 1007/​s12161-​021-​02201-2. |  |
| 31. | Lin P, Yang H, Cheng S, et al. An improved YOLOv5s method based bruises |

Page 19 of 19 Kabir  *et al. Agricultural Products Processing and Storage            (2025) 1:20 *

| 32. | Zhang Z, Pothula A, Lu R. Development and preliminary evaluation of |
|:--- |:--- |
| a new bin filler for apple harvesting and in-field sorting machine. Trans |  |
| ASABE. 2017;60:1839-49. https://​doi.​org/​10.​13031/​trans.​12488. |  |
| 33. | Terven J, Córdova-Esparza DM, Romero-González JA. A comprehensive |
| review of yolo architectures in computer vision: from YOLOv1 to YOLOv8 |  |
| and YOLO-NAS. Mach Learn Knowl Extract. 2023;5(4):1680-716. https://​ |  |
| doi.​org/​10.​3390/​make5​040083. |  |
| 34. | He K, Zhang X, Ren S, et al. Deep residual learning for image recognition. |
| IEEE Conf Comput Vis Pattern Recognit. 2016.https://​doi.​org/​10.​1109/​ |  |
| CVPR.​2016.​90. |  |
| 35. | Ismail N, Malik OA. Real-time visual inspection system for grading fruits |
| using computer vision and deep learning techniques. Inf Process Agric. |  |
| 2022;9(1):24-37. https://​doi.​org/​10.​1016/j.​inpa.​2021.​01.​005. |  |
| 36. | Wang L, Zhao Y, Xiong Z, et al. Fast and precise detection of litchi fruits for |
| yield estimation based on the improved YOLOv5 model. Front Plant Sci. |  |
| 2022;13:965425. https://​doi.​org/​10.​3389/​fpls.​2022.​965425. |  |
| 37. | Liu S, Qi L, Qin H, et al. Path aggregation network for instance segmenta- |
| tion. IEEE Conf Comput Vis Pattern Recognit. 2018:8759-68. https://​doi.​ |  |
| org/​10.​1109/​CVPR.​2018.​00913. |  |
| 38. | Wang CY, Marl Liao HY, Wu YH, et al. CSPNet: a new backbone that can |
| enhance learning capability of cnn. IEEE Conf Comput Vis Pattern Recog- |  |
| nit. 2019:1571-1580. https://​doi.​org/​10.​1109/​CVPRW​50498.​2020.​00203. |  |
| 39. | Liu C, Li W, Feng Y, et al. ATC-YOLOv5: fruit appearance quality classifica- |
| tion algorithm based on the improved YOLOv5 model for passion fruits. |  |
| Math. 2023;11(16):3615. https://​doi.​org/​10.​3390/​math1​11636​15. |  |
| 40. | Rong J, Fu J, Zhang Z, et al. Development and evaluation of a water- |
| melon-harvesting robot prototype: vision system and end-effector. |  |
| Agronomy. 2022;12(11):2836. https://​doi.​org/​10.​3390/​agron​omy12​ |  |
| 112836. |  |
| 41. | Kurniawan H, AndiArief MA, Manggala B, et al. Advanced detection of for- |
| eign objects in fresh-cut vegetables using YOLOv5. LWT-Food Sci Technol. |  |
| 2024;212:116989. https://​doi.​org/​10.​1016/j.​lwt.​2024.​116989. |  |
| 42. | Kabir MH, Guindo ML, Chen R, et al. Geographic origin discrimination |
| of millet using Vis-NIR spectroscopy combined with machine learning |  |
| techniques. Foods. 2021;10(11):2767. https://​doi.​org/​10.​3390/​foods​10112​ |  |
| 767. |  |
| 43. | Kabir MH, Guindo ML, Chen R, et al. Deep learning combined with |
| hyperspectral imaging technology for variety discrimination of fritillaria |  |
| thunbergii. Molecules. 2022;27(18):86042. https://​doi.​org/​10.​3390/​molec​ |  |
| ules2​71860​42. |  |
| 44. | Li Y, Zhang Z, Azizi A, et al. Seeding detection and distribution evalua- |
| tion using the developed automatic maize seeding machine. Comput |  |
| Electron Agric. 2024;220:108872. https://​doi.​org/​10.​1016/j.​compag.​2024.​ |  |
| 108872. |  |
| 45. | Luo Y, Huang Y, Wang Q, et al. An improved YOLOv5 model: application |
| to leaky eggs detection. LWT-Food Sci Technol. 2023;187:115313. https://​ |  |
| doi.​org/​10.​1016/j.​lwt.​2023.​115313. |  |
| 46. | Wang B, Li M, Wang Y, et al. A smart fruit size measuring method and |

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.