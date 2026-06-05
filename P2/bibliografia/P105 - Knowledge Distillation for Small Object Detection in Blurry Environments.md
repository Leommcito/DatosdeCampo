Complex & Intelligent Systems (2025) 11:63 <https://doi.org/10.1007/s40747-024-01676-w>

# ORIGINAL ARTICLE

# A novel knowledge distillation framework for enhancing small object

**detection in blurry environments with unmanned aerial** **vehicle-assisted images**

**Sayed** ** ** **Jobaer** **1** ** ** **·** ** Xue-song** ** ** **Tang** **1,2** **·** ** Yihong** ** ** **Zhang** **1,2** ** ** **·** ** Gaojian** ** ** **Li** **3** ** ** **·** ** Foysal** ** ** **Ahmed** **1**

Received: 13 May 2024 / Accepted: 9 November 2024 / Published online: 4 December 2024 © The Author(s) 2024

**Abstract** Deep learning-based object detectors excel on mobile devices but often struggle with blurry images that are common in real-world scenarios, like unmanned aerial vehicle (UAV)-assisted images. Current models are designed for sharp images, leading to potential detection failures in blurry images. Using image deblurring before object detection is an option, but it demands signiﬁcant computing power and relies heavily on the accuracy of the deblurring algorithms. Another common issue is the suitable dataset for the speciﬁc problem. To address the aforementioned issues, we develop a UAV-assisted small object detection dataset and propose a novel knowledge distillation method for object detection in blurry images in complex environments. Following this, we employ a technique known as self-supervised knowledge distillation, where we introduce a deblurring subnet module with the help of two attention modules, where both networks are trained in a fully-supervised manner. Based on the experiment results, our proposed model achieves an improvement of 4.3% accuracy in the VisDrone synthetic motion blur dataset and 4.6% in detecting objects within synthetic blurry images in our developed small object detection dataset (SOD-Dataset), as well as competitive results compared with other state-of-the-art methods. Meanwhile, ablation experiments and a visualization analysis validate the contributions of each component of the model.

**Keywords** Knowledge distillation · Blur detection · Object detection · Visual sentiment · Depth-of-focus

## Introduction

Object detection has become increasingly essential for computer vision systems in recent decades. This is especially important in surveillance applications, where detecting pedestrians, automobiles, and other obstacles in complex environments in real-time is extremely difﬁcult. Border monitoring, in particular, has become a critical concern due to issues such as illegal immigration, human trafﬁcking, B Xue-song Tang tangxs@dhu.edu.cn

College of Information Science and Technology, Donghua University, Shanghai 201620, People's Republic of China

Engineering Research Center of Digitized Textile Apparel Technology, Ministry of Education, College of Information Science and Technology, Donghua University, Shanghai 201620, People's Republic of China

School of Electronic and Electrical Engineering, Shanghai University of Engineering Science, Shanghai 201620, People's Republic of China

and smuggling \[ 1 \]. Still, developing countries rely on manual patrolling to monitor their border safety, where human vision has limitations. For instance, human eyes need help to detect anything moving faster than 30 frames per second, and detecting objects far away from the inspector presents signiﬁcant challenges \[ 2 \]. Some developed countries have advanced patrolling systems for remote border areas, often utilizing closed-circuit television (CCTV) cameras. However, implementing such systems in remote and coastal regions takes much work. Recent research highlights the dire consequences of the lack of timely rescue operations in remote areas. According to the International Organization for Migration (IOM), 8,600 deaths were reported in 2023, with 64,084 people missing since 2014 due to migration attempts across international borders \[ 3 \]. The hope rests on unmanned aerial vehicle (UAV)-assisted patrolling systems to protect remote areas and carry out timely rescue operations. With modern technology and UAVs, we can monitor remote areas anonymously. UAV-assisted images provide a vast depth of ﬁeld, enabling us to understand complexity. However, the need for a perfect dataset hinders progress.

Page 2 of 27 Complex & Intelligent Systems (2025) 11:63

To address this issue, we developed a UAV-assisted small object detection dataset (SOD-Dataset) to solve the difﬁculties of detecting small objects in complex environments and address another crucial problem: blurry objects in images. During the capture of fast-moving objects, many blurry images were received. For this case, we can consider three scenarios: (1) Objects move so fast that the drone is immobilized, (2) Objects remain steady while the drone changes positionrapidly,and(3)Bothobjectsandthedronemovefast. Motion blur images with confusing objects are received in all these cases, making it challenging to identify and trace them without preprocessing. Human vision systems have limitations \[ 2 \]. Blur perception is fundamental to the human vision systems, aiding in focusing the eyes for clear vision and determining the depth of objects. Accurate blur perception is essential for scanning, detecting, driving, and reading tasks. Understanding blur perception in natural settings is crucial for daily activities and gaining insights into refractive error development. After a deep study of human visual perceptions, we understand that a notable study by Ciuffreda et al. \[ 4 \], introduced a groundbreaking conceptual model to understand how humans perceive blur. This model offers a quantitative approach incorporating two and threedimensional representations of retinal defocus and blur in free space. Importantly, it has profound implications for our depth perception and myopia development. The authors strive to elucidate the factors inﬂuencing blur perception in our visual ﬁelds, mainly focusing on the distances and angles at which human eyes perceive a blur and the challenges in detecting objects. Another research by Maiello et al. \[ 5 \], delvedintomonocularandbinocularblurperception,particularly in peripheral vision, comparing individuals with normal (emmetropic) and myopic individuals. It is well-documented that our tolerance for blur increases in the far and near peripheral visual ﬁelds. This is the exciting characteristic curve that blurs perception follows, with lower blur discrimination thresholds than detection thresholds for small blur levels and increasing discrimination thresholds as blur levels rise. This pattern remains consistent even in peripheral vision, where blur discrimination thresholds are lower than blur detection thresholds. Also, it reinforces the notion that blurred perception deteriorates in peripheral vision and conﬁrms this with a dipper-shaped function. In another study, Abdelhack et al. \[ 6 \] made a remarkable discovery about brain representations of blurred visual input. Top-down projections or recurrent connections in the visual cortex initiate internal processing, making the representations more deﬁned. The sharpeningeffectenhancesthealignmentofbrainrepresentations between blurred images and their original counterparts, even without prior exposure to the original images. This sharpening effect mirrors the visual hierarchy observed in the visual cortex.

The above biological studies explore how people perceive blur. One study introduces a model to understand blur perception, while another explores how our eyes detect blur in the periphery. A third study ﬁnds that our brain can make blurry images more straightforward, even if we have not seen the clear version before. These three articles inspired us to develop an advanced computer vision model to mimic human visual perception in blurry scenarios. Recent research works \[ 7 - 11 \], have demonstrated techniques such as similarity-based image retrieval, image transition, lossless image compression, and context-based scene understanding, among other approaches for enhancing current computer vision techniques. Subsequent studies \[ 12 - 20 \] have showcased numerous approaches for detecting objects in various scenarios. However, the detection of blurry objects in complex environments remains a challenge. In recent years, many object detection algorithms have played essential roles in the ﬁeld, such as YOLO \[ 21 \], ResNet \[ 22 \], and SSD \[ 23 \], which are famous for their accuracy. We propose a lightweight, single-stage knowledge distillation model based on YOLOv8 \[ 24 \]. Our approach incorporates a deblurring subnet module, two distinct attention modules, and a self-supervised learning framework to address the above-mentioned problems. The teacher network is trained with sharp images, while the student network is trained on blurry images. This allows the student network to detect small, fast-moving, blurry objects in complex environments where human vision typically struggles. The main contributions of this work can be summarized as follows:

1. We introduce an innovative self-supervised learning framework that enhances knowledge distillation (KD) architectures with attention modules and a specialized deblurring subnet. The attention modules focus the network on relevant features, while the deblurring subnet sharpens these features to improve detection accuracy. This approach signiﬁcantly enhances the detection of small, blurry objects in low-resolution images, offering a novel solution to this persistent challenge in complex environments. 2. We improve the feature fusion pyramid network with an adjacent feature fusion approach that combines new feature learning and revisits existing knowledge using two-level adjacent layer fusion. Integrate attention modules to enhance knowledge capture and preserve details on small, blurry objects, boosting detection accuracy. A deblurring subnet in the student network uses the teacher network's features for targeted feature-level deblurring. 3. We develop the SOD-Dataset and transform it into a unique synthetic motion blur dataset for detecting small and blurry objects across various classes in complex environments. Experiments show the algorithm's

Complex & Intelligent Systems (2025) 11:63 Page 3 of 27

effectiveness in real-world applications such as border patrolling, security, surveillance, military operations, trafﬁc monitoring, and forestry. The algorithm's performance is validated on the SOD-Dataset and demonstrated on the VisDrone \[ 44 \] dataset.

The paper is structured as follows: Section " Related work " provides an overview of prior work on the knowledge distillation process and blur object detection, highlighting challenges. In Section " Framework for knowledge transfer ", we detail our dynamic model based on KD. Section " Experiment results and analysis " presents experimental results and performance evaluation and explains how we constructed the specialized dataset. Section " Discussion " provides a discussion. Finally, Section " Conclusion " concludes the paper by summarizing ﬁndings and suggesting future research directions.

## Related work

In this section, we delve into the intriguing world of the knowledge distillation process and its implications for object detection and deblurring techniques within images captured under complex environments using UAVs. **Knowledge distillation**

Knowledge distillation, pioneered by Hinton et al. \[ 25 \], serves as a technique for model compression, initially applied within classiﬁcation networks. The process begins with training a teacher network with advanced complexity and robust feature extraction capabilities. Subsequently, the teacher network's output is used to supervise a student network's training, which has a more straightforward design and more rapid reasoning. As a result, the student network ﬁnds it more straightforward to learn from the teacher network \[ 26 \]. In contrast to the conventional object classiﬁcation or detection tasks that depend on binary labels, knowledge distillation uses the teacher network's probability outputs to label data, therebyindicatingthesimilaritiesamongvariousclasses.The knowledge distillation approach softens the classiﬁcation probabilities of objects by adding a temperature coefﬁcient *T* to the softmax function, resulting in more reﬁned classiﬁcation outputs; the calculation formula is as follows:

*q* *i*  exp *(* *z* *i* */* *T* * )*  *j* exp *(* *z* *i* */* *T* * )*, (1)

in this context, * * *q* *i* stands for the class * * *i* th output probability, while * * *z* *i* and * * *z* * j* stand for the softmax layer's input. The parameter * * *T* represents the temperature, and * * *T*  1 corresponds to the typical softmax function. The probability

distribution of the softmax output gets progressively softer as * * *T* rises. Figures 1 and 2 illustrate the proposed Knowledge Distillation (KD) model, showcasing its structure and mechanisms.

## Framework for knowledge transfer

To more effectively showcase our efforts, we reviewed \[ 27 \] existing knowledge distillation (KD) methods such as SSKD \[ 28 \], Mimicking \[ 29 \], and Fine-grained \[ 30 \], which guided students to use the same level of information. Other approaches, like OFD \[ 31 \], FSP \[ 32 \], SP \[ 33 \], and Review \[ 34 \], leveraged multilevel network information for knowledge transfer, utilizing attention maps, ﬂow matrices, and feature fusion strategies. Most knowledge distillation (KD) methods primarily focus on transferring knowledge within the same layer or block; an observation by \[ 26 \] sheds new light on this approach. It is clear that the teacher network specializes in encoding abstract semantic information fused by the deep layers, whereas the bottom layers are more adept at capturing more straightforward knowledge. Consequently, attempting to learn deeply abstract information directly at the beginning of the student network training presents considerable challenges. Addressing this, Cui-jin et al. \[ 26 \] introduced the adjacent feature fusion pyramid network. In contrast to previous knowledge extraction methods, the adjacent feature fusion pyramid network enhances knowledge transfer by fusing features from adjacent layers. The process involves sampling upper-layer features to match the current layer's scale, optimizing interpolated features through convolution, and fusing them with original input features. This approach mitigates information loss for small objects due to lower sampling rates while preserving information gain for larger objects. Further investigation suggests that, during advanced stages, the student network can learn important information from the teacher network's basic features, similar to human learning patterns. This emphasizes the importance of timely review and consolidation for better learning outcomes. We implement the same technique in our methods with the help of the attention module to ﬁlter the important features. Our proposed model employs a self-supervised KD-based learning framework, introducing a teacher network with a typical architecture and a student network with a deblurring subnet. The teacher network takes sharp images, providing hints and soft labels for feature-level deblurring in the student network. Inspired by \[ 26 \] and \[ 35 \], our one-stage detector utilizes an adjacent feature fusion network with the deblurring subnet and two attention modules in Fig. 1, enhancing performance with a novel focal loss function. This approach

Page 4 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 1** Introduces a new network structure that merges adjacent layer features for object detection. This structure, depicted in the backbone, incorporates the Residual Block (B1-B4) of CSPDarkNet53. The

deblurring subnet module is integrated into the student network after the convolution layer in the Residual Block (B1-B4)

aims to improve generalization and domain adaptation, especially in scenarios with low lighting, high altitudes, and ﬂat objects against complex backgrounds. **The proposed method**

Within this segment, we reveal the groundbreaking advancements that form the foundation of our designed knowledge distillation framework. Additionally, we introduce novel modules that outline the working mechanism and present the employed loss functions.

**Self-supervised blur-robust object detections**

To enhance object detection in blurry images, we introduce a novel framework, illustrated in Fig. 2. This framework is built based on the original YOLOv8 \[ 24 \] architecture, comprising three key components: the backbone, the neck, and the detectionhead.InFig. 2,thesecomponentsareredeﬁnedasasingle building block named the base, the feature pyramid network (FPN), and subnets within the teacher and student network sections. We replace the traditional feature pyramid network with an innovative adjacent feature fusion pyramid network, as shown in Fig. 3 (f). We employ the YOLOv8l \[ 24 \] model for the teacher network and incorporate the convolutional block attention module (CBAM) \[ 38 \] in the neck section following the C2f module to enhance feature extraction and focus. For the student network, we choose the YOLOv8s \[ 24 \] model, integrating squeeze-and-excitation networks V2 (SENetV2) \[ 39 \] in the backbone before the spatial pyramid

pooling-fast (SPPF) \[ 76 \] module and in the neck section after the C2f module, which improves feature recalibration and capture. Additionally, we introduce a deblurring subnet (DBSnet) module within the student network, placed after every convolution layer, shown in Fig. 4 f. This deblurring subnet module addressesimageblurandenhancesfeatureclarity.Inthiscontext, the deblurring subnet module focuses on the ﬁne details and speciﬁc features within the image. By targeting and correcting reﬁned image blur, the DBSnet module improves the image's overall sharpness, which is crucial for accurate object detection. This detailed correction helps ensure that the features extracted by the network are more precise and less affected by distortion. Unlike traditional self-distillation methods, which rely on the same distorted images for training, our approach employs differently distorted image pairs for self-guidance. This technique fosters mutual knowledge exchange between the networks, improving performance. The inclusion of the deblurring subnet is inspired by self-training principles, where the diverse dataset of motion-blurred images enables the student network to surpass the teacher network in performance. This advancement, which we term knowledge expansion, highlights the effectiveness of our method in tackling the challenges of detecting small and blurry objects in complex environments. *Developing* * * *problem* * * *scenarios*. In formal terms, we represent a randomly selected mini-batch of size * * *N* as  *I* *orig*, * * *I* *blur*, * * *H* *n*  *N* *n*  1, here * * *I* *orig* \_ *n*, * * *I* *blur* \_ *n*, and * * *H* *n* represents to the * n* th sharp image, its corresponding blurry image,

Complex & Intelligent Systems (2025) 11:63 Page 5 of 27

**Fig. 2** Presents the overarching framework of our proposed knowledge distillation method. It provides in detail the complicated steps and fundamental ideas behind our method. To explain our approach, we use a

clear image of a cat for the teacher network and a blurry image of the same cat for the student network

**Fig. 3** Presents the knowledge distillation framework for transmitting information across network layers. ** a** - **d** represent the process of transferring information within the same network layer. ** e** illustrates how the ﬁnal layer of the student network integrates knowledge from all layers of the teacher network. Moreover, ** f** introduces the implementation of

an adjacent feature fusion knowledge distillation structure. This structure leverages the current and preceding levels of the teacher network to guide student learning, enabling timely review of previous knowledge and facilitating enhanced learning outcomes

Page 6 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 4** Shows the exact locations where sampling takes place in a standard 3 × 3 convolution and deformable convolutions. ** ** **a** The typical sample grid, represented by the blue points, is used in standard convolution. ** ** **b** Illustrates the distorted sample positions (represented by dark blue points) and the increased displacements (shown by light blue arrows) in deformable convolution. The speciﬁc examples of

deformable convolution, denoted as ( **c** ) and ( **d** ), demonstrate the technique's ability to adapt various transformations, including changes in scale, aspect ratio, and rotation. ** ** **e** Visualizes the 3 × 3 deformable convolutions, while ** ** **f** demonstrates our proposed deblurring subnet (DBSnet) module

and their respective hard label. The feature representations for the * n* th input pair can be obtained as:

*F P* *T N* \_ *orig* \_ *n*   *f* *Porig*  *l* *n*  *L* *l*  *i*  * ε*  *I* *orig* \_ *n* , (2)

*F P* *SN* \_ *blur* \_ *n*   *(* * f* *Pblur* *)* *l* *n*  *L* *l*  *i*  * ε*  *I* *blur* \_ *n* , (3)

where * ε(.)* denotes the combined network containing the base and adjacent feature fusion pyramid subnet. Also *f* * * *l* *P* ( *.* ) *n*

refers to the * l* th level within the feature pyramid. The estimation of the detection subnet * * *Dsn* ( *.* ) is determined by utilizing the feature pyramids of both the teacher network *F P* *T N* \_ *orig* \_ *n* and the student network * F P* *SN* \_ *blur* \_ *n* as inputs, as follows:

*CL* *T N* \_ *orig* \_ *n*   ( *cl* *orig* ) *k* *n*, * * *bb* *k* *n*  *K*

*k*  1  * * *Dsn*  *F P* *T N* \_ *orig* \_ *n* , (4) (5)

*CL* * ST* \_ *blur* \_ *n*   ( *cl* *blur* ) *k* *n*, * * *bb* *k* *n*  *K* *k*  1

 * * *Dsn*  *DBsn*  *F P* *SN* \_ *blur* \_ *n* ,

where * CL* *T N* \_ *orig* \_ *n* and * CL* * ST* \_ *blur* \_ *n* represent the estimations of * * *n* th image pair * * *I* *orig* \_ *n* and * * *I* *blur* \_ *n*, respectively. ( *cl* ( *.* ) ) *k* *n* denotes the * k* th classiﬁcation logit before the SoftMax function is applied, while * bb* *k* *n* denotes its estimated bounding box, the term * * *DBsn* ( *.* ) refers to a deblurring subnet and * * *K* represents the total number of estimations. *Self-Supervised learning*. Self-supervised methods create various pretext tasks with labels derived from the data. By addressing these tasks, the network acquires valuable representations.Theseself-supervisedmethodscanbecategorized into several types based on the pretext tasks: constructionbased methods such as inpainting \[ 64 \] and colourization \[ 65 \], prediction-based methods \[ 66 - 68 \], cluster-based methods \[ 69 \], generation-based methods \[ 70, 71 \], and contrastivebased methods \[ 72, 73 \]. The core idea behind self-supervised learning is that the teacher's output contains rich structured knowledge from the teacher network and that mimicking

Complex & Intelligent Systems (2025) 11:63 Page 7 of 27

this output can enhance the student network's learning \[ 74, 75 \]. To apply this theory, our framework introduces a selfsupervised learning strategy for object detection, enhancing the use of sharp and blurry images for classiﬁcation and localization. For both the teacher and student networks, we adopt random initialization for the weights following the standard Xavier (Glorot) initialization strategy \[ 77 \], which sets the weights based on the number of input and output units. This initialization ensures that the gradients remain wellscaled during the early stages of training, avoiding issues like vanishing or exploding gradients. The teacher network is trained on sharp images, and the student network is trained on blurry images, starting with randomly initialized weights. The weight updates follow a standard gradient-based optimization procedure using stochastic gradient descent (SGD) with momentum. The model computes the loss for each mini-batch by combining the classiﬁcation and localization objectives. The classiﬁcation loss * * *L* *conf* is calculated using the cross-entropy loss between the student and teacher network's probability distributions, as in Eq. 7. In contrast, the localization loss * L* *reg* (Eq. 8 ) penalizes deviations in bounding box predictions between the sharp (teacher) and blurry (student) images. During training, the weights are updated based on backpropagation, minimizing this combined loss function. The gradients are calculated for each network's weights, and the SGD optimizer uses these gradients to adjust the weights. Assume that * CL* *T N* \_ *orig* \_ *n*, * c* and * CL* * SN* \_ *blur* \_ *n*, * c* denote the estimations from the * n* th image pair, * * *I* *orig* \_ *n* and *I* *blur* \_ *n*, respectively. This method transfers knowledge from a sharp representation to a blurry one to improve detection accuracy. The core of our approach is converting sharp image logits to soft labels, as shown in Eq. 6. Using weights to address sample imbalance, we differentiate between positive and negative samples, ensuring balanced learning inputs \[ 23 \]. Knowledge from sharp to blurry images is integrated via an objective function combining classiﬁcation and localization losses. The classiﬁcation objective is deﬁned in Eq. 7, and only foreground objects are considered for localization, applying a self-supervised regression loss shown in Eq. 8. The temperature parameter * * *τ* was proposed to control the smoothness of probability distribution \[ 25 \]. Similarly, the soft probability estimation from the blurry image * * *P* * * *K* *SN* *n*, * c* is attained as in Eq. 6. Using no temperature parameters produces the best results for complex tasks like object detection since the calculated probability distribution is already sufﬁciently soft, according to an experiment in \[ 36 \]. Thus, we set the temperature parameter * τ*  1.

*P* * * *K* *T N* *n*, * c*  exp  CLT N_orig_n, c/\tau 

 *C* *c*  1 exp  CLT N_orig_n, c/\tau , (6) *L* *conf*  − 1

# M

# N *n*  1

# K *k*  1

*w* *k* *n* + * v* *k* *n* *L* *C E* *(* *P* *SN* * )* *k* *n*, * c*, * * *(* *P* *T N* * * *)* *k* *n*, * c*, (7) *L* *reg*  1

# M

# N *n*  1

# K *k*  1 *w* *k* *n*

*(* *bb* *SN* *)* *k* *n* − *(* *bb* *T N* *)* *k* *n* 1, (8)

in this context, * * *P* * * *K* *T N* *n*, * c* represents the probability estimations from the sharp images of the teacher's network. For c  1..., C, where C denotes the total number of object categories. In Eq. 7, * L* *C E* indicates the cross-entropy loss function, and * w* *k* *n* denotes the positive sampled when the value is 1, the same as * * *w* *k* *n* denotes the negative sampled when the value is 1. And * * *M*   *N* *n*  1  *K* *k*  1 * * *w* *k* *n* is the total number of optimistic estimations inside the speciﬁed mini-batch. Here, ∥ *.* ∥ 1 stands for the * ℓ* 1 − norm. Thus, the loss function for self-supervised learning is deﬁned as:

*L* * SS*  * * *L* *conf* + * α* *L* *reg*, (9)

in our work, we consider the parameter * * *α* to be 0.5, which serves as a balancing factor between the two losses. **Embedded attention module**

We introduce a novel framework to improve knowledge distillation by integrating advanced attention mechanisms into the teacher and student networks. Recently, many studies have demonstrated the substantial enhancement of machine learning models through attention modules \[ 37 \]. In our approach, we integrate the Convolutional Block Attention Module \[ 38 \] into the teacher network and the multilayer feature fusion module \[ 39 \], an improved version of the Squeeze-and-Excitation Network (SENet), into the student network. This strategic integration leverages CBAM's Channel Attention Module (CAM) and Spatial Attention Module (SAM) in the teacher network to enhance feature representation from sharp images shown in Fig. 5. For the student network, integrating a multilayer feature fusion module helps adaptively recalibrate channel-wise feature responses based on global information, aligning feature representations despite working with inherently blurred input images. Accordingly, CBAM and multilayer feature fusion modules are incorporated to enhance the performance of the proposed networks. Figures 6, and 5 show the structure of the CBAM attention mechanism, and Fig. 7 a, b shows the multilayer feature fusion module. *The* * * *teacher* * * *network* * * *with* * * *convolution* * * *block* * * *attention* *module*. The CBAM module starts by creating a 1D channel attention feature map given the input feature * F* ∈ R *C* × *H* × *W*, then creates a 2D spatial attention feature map, and then combines them as the module's output. The input feature map

Page 8 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 5** Channel and spatial attention unit of CBAM

**Fig. 6** Convolutional block attention module

**Fig. 7** Representing Multilayer Feature Fusion Module

is simultaneously subjected to maximum pooling * * *F* *c* max and average pooling * * *F* *c* *a* *v* *g* within the channel attention module. After that, the data is processed by a multilayer perceptron (MLP), producing the ﬁnal feature map * * *M* *c* ∈ R *C* × 1 × 1. A dimensionality reduction factor * * *r*, represented as * * *M* *c* ∈ R *C* */* *r* × 1 × 1 in the MLP, is added to control computational complexity. The left side of Fig. 5 shows the channel attention process and formula as follows:

Mc(F)  \sigma(M PL(AvgPool(F)) + M PL(Max Pool(F))),

 \sigma *w* 1 *w* 0 *F* *c* *a* *v* *g* + * w* 1  *w* 0  *F* *c* max , (10)

where * σ* represents the sigmoid function, * w* 0 ∈ R *C* */* *r* × *C*, and *w* 1 ∈ R *C* × *C* */* *r* are MLP weights shared by inputs, and ReLu activation is followed by * w* 0. The spatial attention module also employs the two pooling methods mentioned above, followed by convolution, to

Complex & Intelligent Systems (2025) 11:63 Page 9 of 27

obtain the ﬁnal feature maps. The process is depicted on the right side of Fig. 5, and its expression is as follows:

Ms(F)  \sigma f 7\times7([AvgPool(F); Max Pool(F)]),

 \sigma f 7\times7 *F* *s* *a* *v* *g*; * * *F* *s* max , (11)

where * σ* denotes the sigmoid function, whereas * * *f* 7 × 7 refers to the application of a convolution operation utilizing a 7 × 7 ﬁlter size. *The student network with a multilayer feature fusion mod-* *ule*. SENetV2, a channel attention mechanism proposed in \[ 39 \], is illustrated in Fig. 7 a, b, and widely integrated into convolutional neural networks. The main objective is to improve the model's ability to extract features by learning channel features and reducing the importance of less signiﬁcant channel information. The SENet design comprises three fundamental components: squeeze, excitation, and scale. The squeezing process initially compresses the feature map, which has dimensions C × H × W, into a C × 1 × 1 feature map using global average pooling. In this context, C denotes the number of channels, whereas W and H reﬂect the width and height of the feature maps, respectively. Afterward, the excitation operation combines the output from the preceding stage to create a vector with dimensions of C/r. The vector is subject to ReLU activation and then concatenated. This process transforms it into a vector with C dimensions using sigmoid activation, ensuring the values are limited to 0 and 1. Finally, the channel undergoes reweighting, thereby completing the process of rescaling the original features.

**Feature-guided deblurring with self-supervised** **learning**

To enhance image quality, we integrate a deblurring Subnet (DBSnet) between the feature fusion pyramid and detection subnets in the student network. * * *F P* *T N* \_ *orig* and * * *F P* *SN* \_ *blur* denote feature pyramids from the same image but different observations. Assuming the teacher network receives sharp images, * F P* *T N* \_ *orig* guides the student network's blurry feature pyramid * * *F P* *SN* \_ *blur*. The deblurring subnet is utilized on every level of the feature pyramid to estimate a latent feature, shown as * * *(* * f* *Pdeblur* *)* *l* *n*. The latest methods for deblurring images \[ 40 \], such as deformable convolution \[ 41 \], have demonstrated impressive effectiveness in improving image deblurring. The convolution operation's sampling point distribution is adaptively modiﬁed, and deformable convolution efﬁciently tackles spatially variable blur distortions. Figure 4, shows the proposed deblurring Subnet (DBSnet) architecture, which incorporates deformable convolution into a straightforward but efﬁcient design.

The deblurring subnet enhances blurry images through convolutional operations and residual connections. Assume that * (* * f* *Pblur* *)* *l* *n* ∈ R *H* × *W* × *C* represents the input feature map, where * H* and * W* are the height and width of the image, and *C* is the number of channels. The process begins with a 1 × 1 convolution applied to blurry input feature * * *(* * f* *Pblur* *)* *l* *n*, producing a latent feature * (* * f* *Pdeblur* *)* *l* 1  W1\times1 ∗( fPblur)l *n*, where * * *W* 1 × 1 ∈ R 1 × 1 × *C* × *C* ′ is the convolution kernel, * * *C* ′

is the reduced number of channels. Batch normalization followed by the activation functions ReLU is then applied to the ﬁrst output blur feature * (* * f* *Pblur* *)* *l* 1, resulting in * (* * f* *Pdeblur* *)* *l* 2  ReLU( *BN* *(* * f* *Pblur* *)* *l* 1 ). A subsequent 3 × 3 convolution is performed on the second stage latent feature * * *(* * f* *Pblur* *)* *l* 2, resulting in * (* * f* *Pdeblur* *)* *l* 3  W3\times3 ∗( fPblur)l 2, where W3\times3 ∈ R 3 × 3 × *C* ′ × *C* ′′ is the kernel, and * * *C* ′′ is the number of output channels. An offset ﬁeld * * *ρ*  Offset * (* * f* *Pdeblur* *)* *l* is computed from the third stage latent feature * * *(* * f* *Pblur* *)* *l* 3, which adjusts the sampling grid in the deformable convolution. The deformable convention computes * (* * f* *Pdeblur* *)* *l* 4(\rho)   *k* * * *W* ( *k* ) 3\times3 · ( fPblur)l 2(\rho + \rhok), where W (k) 3\times3 \inR3\times3\timesC′\timesC′′

is the * * *k* -th ﬁlter and * * *ρ* *k* is the offset at position * * *k*. After deformable convolution, batch normalization, and the activation function ReLU are applied to the fourth latent feature *(* * f* *Pblur* *)* *l* 4, resulting in * (* * f* *Pdeblur* *)* *l* 5  ReLU( *BN* *(* * f* *Pblur* *)* *l* 4 ). A ﬁnal 1 × 1 convolution reﬁnes at the ﬁfth stage latent feature * * *(* * f* *Pblur* *)* *l* 5 to * * *(* * f* *Pdeblur* *)* *l* 6  W1\times1 ∗( fPblur)l 5, where *W* 1 × 1 ∈ R 1 × 1 × *C* ′′ × *C* ′ is the kernel. This output is then batch-normalized and activated to produce the last feature *(* * f* *Pdeblur* *)* *l* 7  ReLU( *BN* *(* * f* *Pblur* *)* *l* 6 ). Finally, a residual link is established by performing a 1 × 1 convolution between the input blurry feature * (* * f* *Pblur* *)* *l* *n* and the feature with recovered channel numbers to eliminate the blur component and extract a latent deburred feature * * *(* * f* *Pdeblur* *)* *l* *n*. We train the deblurring subnet in a self-supervised manner, in which the sharp feature  *f* *Porig*  *l* *n* serves as the target latent feature for the deburring subnet. To close the difference between the two feature distributions, each of the features  *f* *Porig*  *l* *n* and *(* * f* *Pdeblur* *)* *l* *n* is normalized by its * ℓ* 1 -norm before knowledge transfer. Next, we deﬁne the loss function for feature-level deblurring as follows: *L* *deblur* 

# N *n*  1

# L *l*  1

*(* * f* *Pdeblur* *)* *l* *n* −  *f* *Porig*  *l* *n*, (12)

typically, mean square error (MSE) or * * *ℓ* 1 loss functions are used for pixel-wise regression while training picture deblurring networks. Still different from standard image deblurring, our method with the DBSnet focuses on learning feature space deblurring. We employ the * ℓ* 1 loss empirically for feature-deblurring rather than the MSE method. Consequently, the overall objective function for our framework

Page 10 of 27 Complex & Intelligent Systems (2025) 11:63

combines these introduced loss functions as follows

*L* *total*  * * *L* det + * λ* 1 *L* * SS* + * λ* 2 *L* *deblur*, (13)

where * * *λ* 1, * * *λ* 2 represent the weights assigned to hard and soft, respectively, while * * *L* det signiﬁes a detection loss initially utilized in the training of an object detection network. Experimentally, we set * λ* 1  0 *.* 3 and * λ* 2  0 *.* 5.

## Experiment results and analysis

In this section, we delve deeper into the details of our experiments, providing a comprehensive overview of our methodology and results. We present quantitative and qualitative outcomes and an in-depth ablation analysis to offer a thorough understanding of our approach's performance and impact. **Training details**

All the models were executed on a machine with an Intel XEON CPU running Ubuntu 20.04, using two parallel Nvidia RTX 3090Ti 48 GB GPUs (CPU: Intel ® Xeon ® Silver 4210R @ 2.40 GHz, RAM: 128 GB, GPU: Nvidia RTX 3090Ti 48 GB) and Python 3.9.18. We employed our network architecture utilizing the YOLOv8 framework through PyTorch \[ 42 \], torch version 2.2.0. CUDA 11.0. Throughout the training, batch normalization was applied after each convolution layer to aid convergence speed. Speciﬁcally, YOLOv8l served as the teacher network, while YOLOv8s acted as the student network. Training parameters were set as follows: image size of 640 × 640, initial learning rate of 0.01, ﬁnal learning rate of 0.01, momentum 0.937, weight decay 0.0005, warmup epochs 3, warmup momentum 0.8, warmup bias learning rate 0.1, mosaic 1.0, close mosaic 10, batch size of 8, and 300 epochs, and stochastic gradient descent (SGD) optimizer was employed for training. All other parameters remained at their default values. **Datasets**

Commonly used public datasets for object detection \[ 62, 63 \], such as VOC \[ 51 \], COCO \[ 52 \], and KITTI \[ 53 \], are predominantly based on natural scenarios. However, their sample classes and feature distributions signiﬁcantly differ from UAV-assisted images. These datasets do not adequately reﬂect the unique characteristics of UAV-assisted object detection tasks. To assess the effectiveness of the proposed model in practical UAV contexts, we observed the following while handling widely employed datasets: The UAVDT \[ 54 \] dataset exhibits homogeneity issues due to sequential

video image capture. The VisDrone \[ 44 \] dataset shows variations in image sizes and capture altitudes. The Neovision2 Tower \[ 55 \] dataset includes videos captured from a ﬁxed camera mounted atop Stanford University's Hoover Tower. TheNWPUVHR-10\[ 56 \]imageswereacquiredfromGoogle Earth and the Vaihingen datasets. The LULC \[ 57 \] dataset, focused on land use and land cover, is publicly available and remotely sensed but lacks altitude information. The DOTA \[ 58 \] dataset, designed for object detection in aerial images, contains objects of different scales, orientations, and shapes but lacks altitude information. The VEDAI \[ 59 \] is an aerial image dataset with nine classes but lacks background complexity. The DIOR \[ 60 \] dataset is a large-scale public dataset for object detection in optical remote-sensing images, but it also lacks altitude information and background complexity. The UAV dataset \[ 61 \] includes more than nine thousand images captured via UAVs in different weather and lighting conditions and various complex backgrounds but suffers from blurriness and lacks altitude information. To address these challenges, we developed our SODDataset, which includes images captured under different weather and lighting conditions, with altitudes ranging from 100 to 200 m. Additionally, the dataset contains blurry and low-resolution images in complex environments, making it uniquely suited to solve challenging detection tasks. We compared our SOD-Dataset with the most used benchmark datasets: UAVDT \[ 54 \], VisDrone2019 \[ 44 \], Neovision2 Tower \[ 55 \], NWPU VHR-10 \[ 56 \], LULC \[ 57 \], DOTA \[ 58 \], VEDAI \[ 59 \], DIOR \[ 60 \], and the UAV dataset \[ 61 \]. Table 1 delineates the signiﬁcance and importance of developing this novel small object detection dataset. The dataset for small object detection (SOD-Dataset) was assembled in 2022 at Songjiang University Town, Shanghai, covering diverse weather conditions and times for real-world relevance, using the 'DJI MAVIC AIR 2' drone. Our dataset features varied lighting and backgrounds, enhancing authenticity. Despite large original image sizes, we normalized them to 2240 × 2240 based on our hardware capacity. The dataset includes nine object classes (Cargo, Person, Car, ElectricBike, Truck, Boat, Bus, Bicycle, Tram) and classiﬁes objects into four size categories (big, medium, small, tiny) detailed in Table 2. We used 'LabelImg' \[ 43 \] software for meticulous image annotations in plain text (.txt) format, ensuring multiple objects per image for robust training and evaluation. Our SOD-Dataset, demonstrated in Figs. 8 and 9, aims to enhance small object detection research and includes preprocessing steps to improve data quality. Among the dataset, we have thoughtfully set aside 600 images for the testing dataset, while the remaining 2400 images were dedicated to the training set. Also, we designed a synthetic motion blur dataset to address this blurry object detection issue by varying the camera speed ratio from normal to 100%. For experimental purposes, we increased the camera speed from

Complex & Intelligent Systems (2025) 11:63 Page 11 of 27

**Table 1** Provides an overview of commonly used datasets for small object detection

Dataset Application Shooting angle Video Image Resolution Object classes Blurry objects Altitudes ( *m* )

UAVDT \[ 54 \] Generic UAV based (RGB) -- 1080 \times 540 - - 30-70

VisDrone \[ 44 \] Generic UAV based (RGB) - - 10,209 800 \times 800 to 2000 \times 1500 -
Neovision2 Tower \[ 55 \] Generic On-board (RGB) √ -- 1920 \times 1080 -
NWPU VHR-10 \[ 56 \] Generic Satellite based (RGB&CIR) - - - -
LULC \[ 57 \] Generic Satellite based (RGB) -- 256 \times 256 -
DOTA \[ 58 \] Generic Aerial & Satellite based (RGB)

- - 11,268 800 \times 800 to 20,000 \times 20,000 -
VEDAI \[ 59 \] Generic Aerial based (GRB&NIR) -- 1024 \times 1024 -
DIOR \[ 60 \] Generic Satellite based (RGB) - - 23,463 800 \times 800 -
UAV dataset \[ 61 \] UAV-based detection Areal Perspective (RGB) - - - -
SOD-Dataset (Ours) Generic UAV based (RGB) -- 4000 \times 2250 √ 100-200

A checkmark ' √ ' denotes data availability, while a dash '-' indicates the absence of data

**Fig. 8** Displays a collection of images captured by UAVs from our dataset with a complex background. These images have been chosen randomly and showcase diverse timeframes, settings, and shooting perspectives

Page 12 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 9** Depicts the class distributions within our newly developed small object detection (SOD) Dataset

**Table 2** Diversity of small object detection dataset (SOD-Dataset) classes Index Name of the classes Descriptions C-1 Cargo Objects with large pixel intensity C-2 Tram

| C-3 | Bus | Objects with moderate pixel | intensity | C-4 | Track |
|:--- |:--- |:--- |:--- |:--- |:--- |
| C-5 | Car | Objects with relatively small pixel | intensity | C-6 | Boat |
| C-7 | Electric-bike | Objects with very small pixel | intensity | C-8 | Bicycle |

C-5 Car Objects with relatively small pixel intensity C-6 Boat

C-7 Electric-bike Objects with very small pixel intensity C-8 Bicycle C-9 Person

20 to 100% with a 20% interval gap and trained and evaluated our designed model alongside other state-of-the-art models. *VisDrone* \[ 44 \], The VisDrone Dataset, developed by the AISKYEYE team at Tianjin University, China, is a comprehensive benchmark for drone-based computer vision tasks. It comprises 288 video clips and 10,209 static images, encompassing diverse environments across 14 Chinese cities. The dataset contains meticulously annotated bounding boxes for ten classes, including pedestrians, persons, cars, trucks, buses, vans, cyclists, tricycles, motorcyclists, and nonmotorized vehicles. With over 2.6 million annotations, attributes like scene visibility and object occlusion enhance its utility for research and development. **Synthetic motion blur datasets**

The approach generates a motion-blurred version of an annotated image using a convolution operation with a motion-blur kernel using a pre-designed Python script. The process includes loading the image, deﬁning the motion blur kernel, applying the convolution, and updating the image and its annotations. Assume that the original annotated image * * *I* *orig* is loaded, where * * *I* *orig* is a two-dimensional metric representing pixel values. Then, we apply kernel deﬁnition to motion blur * * *K* of size * * *K* *size* × * * *K* *size*. The dimension of this kernel * * *K* *size* is determined based on a parameter called motion\_speed, which deﬁnes the extent of the motion effect. The kernel * * *K* deﬁnes its values as follows: *K* ( *x*, * y* )  ⎧ ⎨ ⎩

*K* *size* if ( *x*, * * *y* ) correspond to the motion direction, 0 otherwise *.* (14)

where the kernel * * *K* has non-zero values along a line in the direction of motion, with each non-zero entry being *K* *size* to ensure normalization, and ( *x*, * * *y* ) denotes the coordinates value of each pixel. We applied convolution to the original image * * *I* *orig* using the kernel * * *K* to generate a motion-blurred image * * *I* *blurred*. This convolution operation is expressed as: *I* *blurred* ( *x*, * * *y* )  *Ksize* *i*  − *Ksize* *Ksize* *j*  − *Ksize*

Complex & Intelligent Systems (2025) 11:63 Page 13 of 27

**Fig. 10** Represents transforming original annotated images into synthetic motion blur annotated images

*I* *orig* ( *x* − *i*, * * *y* − *j* ) *.* * K*  * K* *size* + * * *i*, * * *K* *size* + * * *j*  *.* (15)

where * * *I* *blurred* ( *x*, * * *y* ) represents the pixel value at the coordinate ( *x*, * * *y* ) in the blurred image. * * *I* *org* ( *x* − *i*, * * *y* − *j* ) denotes the original image's neighbouring pixel values and *K* *K* *size* + * i*, * * *K* *size*

+ * * *j* represents the corresponding kernel values. This convolution process accurately captures the motioninduced blurring effect and shows the transformation. For the annotation retrieval process, the list of annotations for the original image is labelled as * * *A* *orig*, where each annotation is a tuple (class\_id, x, y, width, height). These annotations provide essential object-speciﬁc details for further analysis. The enhanced image * * *I* *blurred* is saved in a designated output directory to preserve the motion-blurred image and ensure it is available for future use. The annotations for the motionblurred image are referred to as * * *A* *updated*. In Fig. 10, we represent a working follow diagram to process the synthetic blur dataset to an original dataset; in the beginning, we extract the image ﬁle (EIF) and extract the annotation ﬁle (EAF), and concatenate both the image and annotation ﬁle and create an annotated image (AI), then add the kernel (K) size, and base on the kernel size bounding box (BB) shift accordingly and generate new annotated images (NAI), again we decatenate (D) new annotated image and restore image ﬁle (RIF), and restore annotated ﬁle (RAF). In Fig. 11, we present the transformative effects of motion blur augmentation, with a 20% increase in blur ratio applied to original images (for instance, we present here the original image, motion speed 40%, and motion speed 100%). Three carefully selected pictures from our dataset, spanning nine classes, illustrate the diverse impact on various visual elements. This synthetic dataset aims to simulate real-world scenarios and assess algorithm robustness. **Evaluation metrics**

Each detected bounding box in our SOD-Dataset can be categorized into three scenarios. True positive ( *T* *ps* ) denotes a detected box with an intersection over union ( *IoU* ) value exceeding 50% about its corresponding ground truth box. In contrast, false positive  *F* *ps*  refers to a detected box with a value below 50%, and false negative ( *F* *ng* ) occurs when a ground truth box lacks coverage from any detection. Utilizing * T* *ps*, * F* *ps* and * F* *ng* we establish various evaluation metrics: Precision (Prec.), Recall (Rec.), and F1-measure (F1). We calculate the size of the model parameters (Params) and the mean time to detect (MT) of a single picture. Precision is a metric that evaluates the accuracy of a model's detections. It is calculated by dividing the number of true positives by the total number of detected bounding boxes:

*Precision* ( *Prec* *.* )  *T* *ps* *T* *ps* + * F* *ps* *.* (16)

Recall indicates a model's capability to encompass all ground truth bounding boxes. It is ﬁgured by dividing the number of true positives by the total number of true positives and false negatives:

*Recall* ( *Rec* *.* )  *T* *ps* *T* *ps* + * * *F* *ng* *.* (17)

F1-measure (F1) provides a balanced perspective by considering precision and recall. It is the harmonic mean of precision and recall, which provides information about the model's overall effectiveness: F1 −measure (F1)  2 × Prec. × Rec. *Prec* *.* + * * *Rec* *. * *.* (18)

Page 14 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 11** Depicts, from left to right, both the original annotated images and the images after applying a motion blur speed

## To conclude, the mean average precision ( mAP ) is formu lated as: *m AP*  *N* *c* *N* *c*

## i  1 *Prec* *(* *i* *)*, (19)

## in Eq. 19, N c represents the total number of object classes,

and * Prec* ( *i* ) represents the precision of each unique class as stated in Eq. 16. The inference speed is also an integral aspect of the algorithm performance quantiﬁcation, and this experiment uses the frames per second (FPS) to characterize the inference speed of the model. The formula for calculating FPS is expressed as:

## F PS 

*t* \_ *pre* + * inf erence* + * t* \_ *post*, (20)

## where t\_pre is the preprocessing time (image scaling,

padding, and channel transformation), * inference* is the time for the model to process the input and generate output, * t\_post* is the post-processing time (format conversion), and FPS is the model's inference speed.

## Ablation analysis

## Ablation experiments of the feature fusion. Our analysis

reveals that the fourth method demonstrates superior performance. When considering feature fusion methods ﬁve and six, we reference Hoeffding's inequality \[ 45 \], which indicates that a higher value of M may lead to overﬁtting,

**Table 3** Presents a comparison of detection results obtained by the knowledge distillation network when features from different layers are fused in the teacher network

Methods (Teacher → Student) *m AP* *v* *al* 50 − 95 *m AP* *v* *al* MT/ *ms* $$ TB1 \toSB1, TB4 \toSB4 $$ 44.5 60.2 2.98

$$ TB1 \toSB1, TB2 \toSB2 $$ $$ TB3 \toSB3, TB4 \toSB4 $$ 46.8 63.3 3.11

# \{T B1, T B2, T B3, T B4 \} → S B4 46.3 62.7 3.19

# TB1 \\toSB1, \{TB1, TB2\} \\to

S B2, $$ {TB2, TB3} \toSB3, $$ $$ {TB3, TB4} \toSB4 $$ 47.1 64.2 3.25

# TB1 \\toSB1, \{TB1, TB2\} \\to

S B2, \{T B1, T B2, T B3 \} → S B3, $$ {TB2, TB3, TB4} \toSB4 $$ 46.7 63.2 3.31

# TB1 \\toSB1, \{TB1, TB2\} \\to

S B2, \{T B1, T B2, T B3 \} → S B3, \{T B1, T B2, T B3, T B4 \} → S B4 45.1 61.8 3.42

## potentially compromising accuracy. Methods one, two, and

three, which involve knowledge transfer within the same layer or block, may limit the student's ability to capture ﬁne details in real-time, thereby increasing the likelihood of missed detections. After careful deliberation, we consider the fourth feature fusion method most suitable for our knowledge distillation feature transfer networks (see Table 3 ). *Ablation* * * *experiments* * * *of* * * *the* * * *deblurring* * * *subnet* * * *(DBSnet)* *module*. To enhance the student network's ability to learn

Complex & Intelligent Systems (2025) 11:63 Page 15 of 27

**Table 4** Presents a comparison of detection results obtained by the knowledge distillation network when features from different layers are fused in the student network

Methods (Student → Deblurring Subnet) *m AP* *v* *al* 50 − 95 *m AP* *v* *al* MT/ *ms*

S B1 → DBSnet 1, S B4 → DBSnet 4 39.7 55.4 3.36

S B1 → DBSnet 1, S B2 → DBSnet 2 S B3 → DBSnet 3, S B4 → DBSnet 4 42.9 59.2 3.37

# \{S B1, S B2, S B3, S B4 \} → DBSnet 4 38.1 56.5 3.34

S B1 → BDSnet 1, \{BDSnet 1, S B2 \} → DBSnet 2 DSBnet 2 → \{S B2, S B3 \} → DBSnet 3 DBSnet 3 → \{S B3, S B4 \} → DSBnet 4 46.9 64.1 3.39

## valuable information from the teacher network through fea

turefusion,weincrementallyincorporatetheDBSnetmodule into the student network at the B1, B2, B3, and B4 stages. The analysis presented in Table 4, reveals that the best detection outcomes occur when the DBSnet module reviews key features from the previous layer. This suggests a similarity to the process of students reviewing important features from the previous stage to achieve better learning outcomes. Despite several iterations, we observe minimal improvement in knowledge distillation with the increased inclusion of the deblurring subnet module in the student network. *Ablation* * * *experiments* * * *of* * * *the* * * *attention* * * *modules*. We enhance knowledge transfer from a teacher network to a student network by integrating CBAM \[ 38 \] into the teacher

## network and SENetV2 \[ 39 \] multilayer feature fusion atten

tion module into the student network at different stages (T1-T4 for the teacher network and S1-S4 for the student network). Various conﬁgurations are tested by adding or removing attention modules at these stages. Notably, our evaluation, as depicted in Table 5, highlights the superior performance when attention mechanisms are strategically deployed to review key features of previous layers. Version 9, with all attention modules retained, yields the best results, underscoring the signiﬁcance of comprehensive feature fusion across multiple stages for optimal performance in our model.

## Results on the SOD-dataset

## The total loss on the SOD-Dataset is shown in Fig. 12 a. Our

method demonstrates superior performance in terms of loss reductioncomparedtopreviousknowledgedistillationstrategies, and it achieves a faster rate of decline. At the 300th epoch, our model achieves a more minor loss than the student baseline network, suggesting that it achieves a higher learning efﬁcacy after incorporating an adjacent feature fusion knowledge distillation structure. The precision-recall curve of our approach in Fig. 12 b, outperforms that of other algorithms, demonstrating its superior performance. Moreover, Fig. 12 c, showcases the efﬁcacy of our suggested algorithm, exhibiting a mean average precision (mAP\_0.5) that surpasses the baseline by 4.6% and YOLOv8x \[ 24 \] by 3.2% at a motion speed of 100% data. Figure 13, shows that the teacher network produces sharp images and creates clear feature maps, while supervised and unsupervised student networks work with blurry images. Unlike the unsupervised network, the supervised student network mimics the

**Table 5** Ablation studies of CBAM and SENetV2, outlines the impact of these attention modules on model performance metrics Teacher Network + CBAM \[ 38 \] Student Network + SENetV2 \[ 39 \]

Ver T1 T2 T3 T4 S1 S2 S3 S4 C-1 C-2 C-3 C-4 C-5 C-6 C-7 C-8 C-9 Mean MT/ms Params

# V1

√ √ √ √ √ √ 73.5 61.7 70.6 55.5 88.4 68.1 46.8 58.8 52.3 63.9 3.17 13.045

# V2

√ √ √ √ √ √ 73.3 61.4 70.3 55.1 87.8 67.8 46.5 58.7 51.9 63.6 3.17 13.045

# V3

√ √ √ √ √ √ 72.8 60.7 70.1 54.7 87.4 67.6 46.1 58.3 51.5 63.2 3.17 13.045

# V4

√ √ √ √ √ √ 73.2 61.5 70.5 55.4 88.3 68.2 46.9 58.6 52.2 63.8 3.17 13.045

# V5

√ √ √ √ 70.8 59.2 69.1 54.7 86.9 66.9 45.8 57.4 50.4 62.3 3.29 13.028

# V6

√ √ √ √ 70.4 58.7 68.9 53.5 86.7 66.4 45.3 56.9 49.5 61.8 3.29 13.028

# V7

√ √ √ √ 69.3 56.8 66.9 52.8 85.2 65.2 43.9 55.2 47.8 60.3 3.29 13.028

# V8

√ √ √ √ 70.1 58.6 69.1 53.7 86.9 67.1 45.6 57.3 49.8 62.0 3.29 13.028

# V9

√ √ √ √ √ √ √ √ 73.7 61.9 70.8 55.7 88.6 68.5 47.3 59.1 52.5 64.2 3.37 13.062

Page 16 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 12** Illustrates a comparison of our method with others in terms of the loss function, precision-recall (P-R) curve, and mean average precision ( *mAP\_0.5* ) on both the SOD-Dataset and VisDrone datasets.

**a** and ** d** represent the overall loss functions, whereas ** b** and ** e** show the precision-recall curves. The mean average precision ( *mAP\_0.5* ) values are presented in ** c** and ** f**

**Fig. 13** Illustrates the output comparison between the teacher network and supervised and unsupervised student networks, highlighting the differences in feature extraction quality and detail resolution

teacher, better extracts detailed features, and closely resembles the teacher's output. This suggests that teacher-guided training enhances the supervised student network's ability to extract features from blurry images, improving performance. Figure 14, shows the feature map and detection results from our knowledge distillation network that our proposed network generates after feature fusion. Tables 6, 7 and 8 show the SOD-Database's results. These tables compare the performance of algorithms under different frameworks at various motion speed ratios. We choose the

data for motion speed 100% from Table 7 to present the F1measure (%) and mean average precision ( *mAP* \_0.5) for each class in Table 6. Our method outperforms the other frameworks regarding the mean average precision ( *mAP* \_0.5). In comparison, SuperYOLO \[ 50 \] performs better than the other models. Our model achieves a mean average precision ( *mAP* \_0.5) of 64.3% and an F1 score of 71.3%, while SuperYOLO \[ 50 \] reaches a * * *mAP* \_0.5 of 62.2% and an F1 score of 70.1%. Table 7 displays the data ranging from sharp to completely blurry images at a motion speed of 100%. Our proposed model achieves the best results. The mean average

Complex & Intelligent Systems (2025) 11:63 Page 17 of 27

**Fig. 14** Showcases the detection results on the SOD-Datasets. The images progress from the original input to motion-blurred images from left to right. After feature fusion, the feature map generated by our proposed network corresponds to the output of our knowledge distillation network's detection results

precision ( *mAP* \_0.5) for sharp input images is 66.8%, and the F1 measures 76.9%. As the motion speed increases by 20%, the mean average precision ( *mAP* \_0.5) drops by 0.5%, and theF1measuredropsby1.3%.Witha40%increaseinmotion speed, the mean average precision ( *mAP* \_0.5) decreases by 1.1%,andF1measures2.5%.At60%motionspeed,themean average precision ( *mAP* \_0.5) drops by 1.6%, F1 measures 3.3%, and at 80% motion speed, the mean average precision ( *mAP* \_0.5) decreases by 2.1%, F1 measures 4.5%. When the motion speed reaches 100%, the mean average precision

( *mAP* \_0.5) drops by 2.5%, and F1 measures 5.6%. In comparison, YOLOv8 \[ 24 \] experiences a mean average precision ( *mAP* \_0.5) drop of 4.6%, F1 measure 3.6%, while SuperYOLO \[ 50 \] experiences a mean average precision (mAP\_0.5) drop of 3.1%, F1 measure 5.1% at 100% motion speed. It is crucial to emphasize that the performance of other models declines more signiﬁcantly than our proposed model as motion speeds increase. This decline is likely due to the small size of the objects in our dataset and the visual similarities between the objects and their backgrounds.

Page 18 of 27 Complex & Intelligent Systems (2025) 11:63

**Table 6** Presents a class-wise quantitative comparison of various algorithms, including our proposed methods, on the SOD-Dataset test set with 100% motion speed

Measures Methods Backbone C-1 C-2 C-3 C-4 C-5 C-6 C-7 C-8 C-9 Mean

F1 (%) Baseline CSPDarknet53 75.8 68.6 84.8 50.7 85.8 65.6 49.8 62.7 50.6 66.0

Mimicking \[ 29 \] RPN and R-FCN 60.9 65.8 73.6 40.2 78.7 66.9 41.2 48.5 46.6 58.0

SSKD \[ 28 \] ResNet 66.8 63.7 69.5 43.7 81.6 53.7 43.2 47.6 44.9 57.1

Fine-grained \[ 30 \] Faster R-CNN 63.7 67.6 63.4 55.7 63.8 58.3 44.6 69.3 49.8 59.5

OFD \[ 31 \] ResNet 68.3 56.4 59.1 42.7 74.5 44.7 39.2 41.6 38.1 51.6

ReviewKD \[ 34 \] ResNet101 69.3 59.3 66.7 44.7 81.9 38.6 43.5 44.2 42.3 54.5

# SSD \[ 23 \]

VGG16 56.9 67.8 69.4 44.4 79.8 30.9 31.7 30.9 46.3 50.9

RetinaNet \[ 46 \] ResNet-101 59.5 69.6 73.8 47.7 82.7 37.7 44.8 45.6 49.5 56.7

YOLOv5 \[ 47 \] CSPDarknet53 59.7 68.1 78.2 54.3 82.4 68.2 52.3 49.9 47.8 62.3

YOLOv6 \[ 48 \] EfﬁcientRep 61.1 75.5 74.4 55.4 82.1 81.3 54.6 69.1 43.8 66.3

YOLOv7 \[ 49 \] RepConvN 68.9 **87.8** **88.6** 40.2 87.7 **82.0** 42.3 **78.5** 43.6 68.8

YOLOv8 \[ 24 \] CSPDarknet53 78.7 69.6 86.8 58.7 87.8 71.8 53.8 66.5 54.9 69.8

SuperYOLO \[ 50 \] 79.6 70.3 83.2 59.2 88.6 72.3 54.8 67.5 55.7 70.1

Ours **82.1** 70.3 85.5 **59.6** **89.9** 74.2 **55.6** 68.8 **56.4** **71.3**

*mAP* (%) Baseline CSPDarknet53 66.3 54.5 67.8 51.3 85.9 63.5 45.3 56.9 45.8 59.7

Mimicking \[ 29 \] RPN and R-FCN 59.2 65.3 66.4 31.3 83.2 65.3 25.1 28.3 47.2 52.3

SSKD \[ 28 \] ResNet 66.5 60.1 63.5 25.3 80.5 62.3 22.7 26.1 21.9 47.5

Fine-grained \[ 30 \] Faster R-CNN 64.5 **70.1** 66.3 27.4 79.4 65.3 20.3 23.6 19.5 48.4

OFD \[ 31 \] ResNet 57.8 64.7 60.4 26.7 67.8 47.5 17.8 20.6 17.7 42.3

ReviewKD \[ 34 \] ResNet101 64.3 57.9 59.7 24.4 83.3 64.4 21.6 27.3 22.5 47.2

# SSD \[ 23 \]

VGG16 58.4 56.1 51.4 36.3 55.1 37.2 18.1 18.3 26.3 39.6

RetinaNet \[ 46 \] ResNet-101 60.7 59.8 55.3 39.7 57.8 49.9 23.8 24.7 29.9 44.6

YOLOv5 \[ 47 \] CSPDarknet53 67.3 60.4 68.7 31.3 66.5 68.5 35.7 52.1 49.7 55.5

YOLOv6 \[ 48 \] EfﬁcientRep 70.6 66.7 67.5 29.4 64.5 66.5 32.5 51.8 43.8 54.8

YOLOv7 \[ 49 \] RepConvN 68.3 67.2 **71.6** 24.8 67.8 **69.3** 37.5 55.4 **54.3** 57.3

YOLOv8 \[ 24 \] CSPDarknet53 69.4 58.4 68.9 53.1 86.7 65.4 42.6 57.3 48.2 61.1

SuperYOLO \[ 50 \] 71.6 59.7 69.6 54.2 87.3 66.8 43.6 57.9 49.4 62.2

Ours **73.7** 61.9 70.8 **55.7** **88.6** 68.7 **47.6** **59.1** 52.7 **64.3**

The term 'Baseline' denotes results obtained without distillation. The best measures are in boldface

## In this study, we utilize the latest version of the YOLOv8

algorithm \[ 24 \], which is optimized for small object detection in-ﬂight scenarios. As our baseline, we select the YOLOv8s model due to its compact size, low computational cost, and ease of use. In contrast, other models are designed for more general purposes and do not meet the speciﬁc requirements of our task. Several knowledge distillation techniques, such as Mimicking \[ 29 \], SSKD \[ 28 \], Fine-grained \[ 30 \], OFD \[ 31 \], and ReviewKD \[ 34 \], are well-known. While these techniques perform well on general datasets, they struggle on our custom small object detection (SOD) dataset, which features small objects with low pixel intensity and low-light conditions. When motion blur is introduced into the dataset, the performance of these models declines further, as they are not tailored to handle small, blurry objects in complex environments. Similarly, models such as SSD \[ 23 \], RetinaNet \[ 46 \],

## YOLOv5 \[ 47 \], YOLOv6 \[ 48 \], YOLOv7 \[ 49 \], and SuperY

OLO \[ 50 \] exhibit high accuracy and performance but are high computational cost and slower in terms of frame rate, which is critical for real-world applications. Our proposed model effectively addresses these issues. Including a deblurring subnet module helps reduce blurriness, enabling our student model to generate deblurred latent features, which is the key function of the DBSNet module. Table 8 compares our proposed model against various state-of-the-art models, focusing on different metrics. We evaluate the models using different IoU threshold values, examining parameter count and model complexity measured in GFLOPs. Additionally, we compare model size, inference time, and frames per second (FPS). Our proposed model consistently outperforms other state-of-the-art models across these metrics. Notably, it achieves superior performance at different IoU thresholds.

Complex & Intelligent Systems (2025) 11:63 Page 19 of 27

**Table 7** Compares the category results of different algorithms on the SOD-Dataset test set, categorized by different motion speed pairs and displaying F1 and mean average precision ( *mAP* \_0.5) measures

Methods Sharp Motion speed 20% Motion speed 40% Motion speed 60% Motion speed 80% Motion speed 100%

# F1(%)

*mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%)

Baseline 70.1 62.2 69.2 61.7 68.4 61.2 67.6 60.7 66.8 60.2 66.0 59.7

Mimicking \[ 29 \] 60.8 54.8 60.3 54.5 59.7 53.1 59.1 52.9 58.5 52.6 58.0 52.3

# SSKD \[ 28 \]

59.8 49.4 59.4 49.0 58.7 48.6 58.1 48.2 57.6 47.9 57.1 47.6 Finegrained \[ 30 \]

61.7 50.4 61.2 49.9 60.7 49.5 60.3 49.1 59.8 48.6 59.5 48.4

# OFD \[ 31 \]

53.7 43.8 53.4 43.6 52.8 43.3 52.4 42.9 51.9 42.6 51.6 42.3

ReviewKD \[ 34 \] 58.3 48.9 57.9 48.6 57.4 48.2 56.9 47.8 56.1 47.5 54.5 47.2

# SSD \[ 23 \]

58.7 41.6 57.3 41.3 56.1 40.8 53.5 40.1 52.6 39.8 50.9 39.6

RetinaNet \[ 46 \] 61.6 46.7 61.3 45.9 59.4 45.7 58.7 45.3 57.1 44.9 56.7 44.6

# YOLOv5

\[ 47 \] 64.2 59.4 63.8 58.7 63.4 58.2 62.8 57.6 62.4 56.8 62.0 55.5

# YOLOv6

\[ 48 \] 68.4 57.3 67.8 56.8 66.8 56.2 66.3 55.7 64.9 55.2 66.3 54.8

# YOLOv7

\[ 49 \] 75.8 61.7 74.5 61.3 73.4 60.1 71.3 58.6 69.5 57.9 68.8 57.3

# YOLOv8

\[ 24 \] 73.4 65.7 72.9 65.2 72.4 64.5 71.9 63.7 71.4 62.9 69.8 61.1

SuperYOLO \[ 50 \] 75.2 65.3 74.3 64.8 73.6 64.1 72.5 63.5 71.3 62.8 70.1 62.2

Ours **76.9** **66.8** **75.6** **66.3** **74.4** **65.7** **73.6** **65.2** **72.4** **64.7** **71.3** **64.3**

The term 'Baseline' denotes results obtained without distillation. The best measures are in boldface

## The parameter count for our model is 13.06 million, com

parable to the baseline model's 11.13 million parameters. Furthermore, our model size is smaller than all other models, which was the primary objective of this study. Although the inference time is slightly higher than the baseline model at 0.3 ms, the FPS rate stands at 311.5, marginally lower than the baseline model. Notably, while the baseline model achievestheseresultswithoutdistillation,ourmodelachieves comparable performance through the knowledge distillation technique. The visual detection results for the YOLOv8 \[ 24 \] method and our proposed approach are shown in Fig. 15 across various scenes. Our proposed model outperforms YOLOv8 \[ 24 \] by accurately detecting objects that YOLOv8 \[ 24 \] either misses, misclassiﬁes, or detects with uncertainty. Detecting objects in blurry images, especially at small scales, is challenging. For instance, detecting persons, bicycles, and electric bikes can be difﬁcult due to their pixel-level similarity with the background. In contrast, SENet excels in preserving essential information during feature extraction by

## learning which channel features are important and reduc

ing the impact of less signiﬁcant channels. Consequently, self-supervised learning improving classiﬁcation accuracy is crucial for object detection tasks and location detection, where our method performs better in detecting small objects in blurry images with different motion speeds. In Fig. 16, we demonstrate that our model surpasses real-life data in performance. The deblurring subnet module effectively operates in complex environments, successfully deblurring blurry objects. We select blurry images from our SOD-Dataset, which includes various camera settings and lighting conditions. These images represent three scenarios: objects move so fast, and the drone remains steady; objects remain constant; in contrast, the drone changes position rapidly, and both objects and the drone move quickly. Our proposed method outperforms the YOLOv8 \[ 24 \] model in detection results. To illustrate this, we zoom in on small objects within the detection results to show that our model works effectively in real-life scenarios, wherein the deblurring subnet module can remove blurriness from objects.

Page 20 of 27 Complex & Intelligent Systems (2025) 11:63

**Table 8** Presents a comparative analysis of the accuracy and complexity of our proposed model and compares the results with other state-of-the-art models on the SOD-Dataset test set with 100% motion speed

Methods Backbone Model *m AP* *v* *al* 50 − 95 *m AP* *v* *al* Params ( *M* ) GFLOPs Model size ( *MB* ) Inference time ( *ms* ) FPS ( *f/s* )

Baseline CSPDarknet53 s 42.8 59.7 **11.13** 28.6 21.1 **2.8** **319.3**

Mimicking \[ 29 \] RPN and R-FCN - - 34.2 52.3 - - - 169.3 5.8 129.8

SSKD \[ 28 \] ResNet - - 29.4 47.5 - - - 44.6 4.7 180.1

Fine-grained \[ 30 \] Faster R-CNN - - 31.7 48.4 - - - 97.4 5.2 186.9

OFD \[ 31 \] ResNet - - 22.8 42.3 - - - 47.6 4.8 202.8

ReviewKD \[ 34 \] ResNet101 - - 28.9 47.2 - - - 134.7 6.8 103.2

# SSD \[ 23 \]

VGG16 - - 23.6 39.6 138.01 34.8 65.2 4.5 214.6

RetinaNet \[ 46 \] ResNet-101 - - 27.9 44.6 57.50 85.4 72.4 5.4 180.8

YOLOv5 \[ 47 \] CSPDarknet53 s 38.2 55.5 12.62 **16.8** 17.7 3.5 276.2

YOLOv6 \[ 48 \] EfﬁcientRep s 36.5 54.8 18.53 45.4 31.3 3.7 259.7

YOLOv7 \[ 49 \] RepConvN - - 38.6 57.3 36.52 103.2 74.9 4.6 209.2

YOLOv8 \[ 24 \] CSPDarknet53 l 43.3 61.1 43.71 165.2 83.5 6.4 151.3

SuperYOLO \[ 50 \] s 43.9 62.2 14.85 18.1 16.5 3.3 289.8

Ours s **47.5** **64.3** 13.06 33.2 **13.4** 3.1 311.5

The best results are highlighted in bold, indicating lower parameter counts, reduced GFLOPs, shorter inference times, and higher FPS rates. The mean average precision ( *mAP* ) values at different IoU thresholds demonstrate the model's effectiveness. The Model column indicates the network's capacity, where s denotes small, l denotes large, and a dash '-' means the absence of information. The term 'Baseline' denotes results obtained without distillation

## Additionally, our model's detection capability is superior to

YOLOv8 \[ 24 \], demonstrating its excellence.

## Results on the VisDrone dataset

## Table 9 presents the detection results on the VisDrone

\[ 44 \] dataset. The tables provide a comparative analysis of algorithm performance across different frameworks at various motion speed ratios. Focusing on the data for 100% motion speed from Table 9 presents each class's F1-measure (%) and mean average precision (mAP\_0.5). Our method demonstrates superior performance regarding mean average precision (mAP\_0.5). Speciﬁcally, our model achieves a mean average precision (mAP\_0.5) of 53.5% and an F1 score of 62.4%, outperforming SuperYOLO \[ 50 \], which records a mAP\_0.5 of 52.3% and an F1 score of 60.9%. Table 9 outlines performance metrics for image clarity ranging from sharp to completely blurry at 100% motion speed. Our proposed model consistently achieves the highest results. The mean average precision (mAP\_0.5) for sharp

## images is 56.3%, with an F1 score of 65.1%. As motion speed

increases, performance gradually declines. At a 20% increase in motion speed, the mean average precision (mAP\_0.5) decreases by 0.6%, and the F1 score drops by 0.6%. With a 40% increase in motion speed, the mAP\_0.5 decreases by 1.3%, and the F1 score declines by 1.2%. At 60% motion speed, the mean average precision (mAP\_0.5) reduces by 1.8%, and the F1 score drops by 1.7%. An 80% increase in motion speed leads to a 2.4% decrease in mean average precision (mAP\_0.5) and a 2.5% reduction in the F1 score. When the motion speed reaches 100%, the mean average precision (mAP\_0.5) shows the most signiﬁcant decline of 2.8%, with the F1 score dropping by 2.7%. In comparison, YOLOv8 \[ 24 \] experiences a more substantial decrease in performance, with the mean average precision (mAP\_0.5) dropping by 2.8% and the F1 score by 3.1% at 100% motion speed. SuperYOLO \[ 50 \] also drops signiﬁcantly, with the mean average precision (mAP\_0.5) decreasing by 2.8% and the F1 score by 2.5% at the same motion speed. Our model

Complex & Intelligent Systems (2025) 11:63 Page 21 of 27

**Fig. 15** Compares detection results for different motion speeds on the SOD-Dataset. The detection accuracy decreases as motion speed increases. Up to 40% motion speed, existing models can detect objects with low conﬁdence, whereas our proposed method effectively deblurs

the scene, making it easier to detect small and blurry objects. However, small objects gradually become difﬁcult for existing models to detect accurately in scenarios with motion speeds ranging from 40 to 100%. In contrast, our model performs better, although with lower conﬁdence

performs best despite increasing motion speed, demonstrating its robustness against motion blur. In Fig. 12 d, the overall loss on the VisDrone \[ 44 \] dataset is shown, indicating that our method exhibits smaller loss values than other knowledge distillation methods, decreasing more rapidly. By 300 epochs, our model's loss is lower than the different networks, suggesting superior learning effectiveness. Figure 12 e illustrates that our algorithm achieves the highest precision-recall curve, outperforming other algorithms. Additionally, in Fig. 12 f, our proposed algorithm demonstrates its effectiveness, with the mean average precision ( *mAP* \_0.5) being 4.3%, higher than the baseline and 3.3% higher than YOLOv8x \[ 24 \] on motion speed 100% data. Finally, Fig. 17 shows the accurate detection and positioning of small objects in blurry images with various motion speeds, exhibiting high conﬁdence.

## Discussion

The primary objective of our work was to improve the detection of small objects in complex environments. We introduced the small object detection dataset (SOD-Dataset) to achieve this. During our analysis, we encountered images with motion blur within the dataset. Current models, optimized for sharp images, often struggle with detecting objects in blurry images. Although image deblurring before object detection is a possible solution, it requires signiﬁcant computational resources and depends heavily on the accuracy of the deblurring algorithms. Furthermore, ﬁnding a suitable dataset that addresses this issue is another common challenge. To tackle these problems, we synthetically generated a motion-blur version of our SOD dataset and the VisDrone \[ 44 \] dataset, simulating various degrees of motion blur to accountforthelackofsufﬁcientblurredimages.Thisallowed

Page 22 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 16** Compares detection results in real-life scenarios, highlighting that our method achieves the best output. These comparisons show that our proposed method excels while the original YOLOv8 struggles to detect blurry objects in complex environments. Our deblurring subnet module effectively deblurs blurry objects, showcasing the superiority

of our models in detecting small and blurry objects in real-life images where motion blur exists. Our approach enhances detection accuracy and signiﬁcantly improves conﬁdence in detecting small and blurry objects commonly encountered in practical applications

us to test our model's robustness in detecting small, blurry objects in complex environments. In response to the challenges, we developed a knowledge distillation model based on the YOLOv8 \[ 24 \] architecture, using YOLOv8l as the teacher and YOLOv8s as the student network. The proposed model incorporates three key modules: a convolutional block attention module (CBAM) \[ 38 \] in the teacher network, a squeeze-and-excitation network (SENet) \[ 39 \] in the student network, and a deblurring subnet module (BDSNet) in the student network. Additionally, it introduces an adjacent feature fusion knowledge distillation structure, which leverages the current and previous layers of the teacher network to guide the student's learning, enabling continuous review of prior knowledge for enhanced learning. The teacher network was trained on sharp images in our training framework, while the student network was trained on motion-blurred images. This approach allowed the student network to learn from

the more accurate teacher network while being speciﬁcally trained to detect blurry objects. While the model performed well under moderate motion conditions, experiments revealed limitations as motion speeds increased. Speciﬁcally, as motion speed increased from60to100%,thedeblurringsubnetinthestudentnetwork struggled to sufﬁciently reduce blurriness, primarily due to the small object sizes and background similarities. This highlightsthechallengeofhandlingmotionblurinsuchscenarios, revealing a limitation of our model. Another key limitation of our current approach is that the dataset only addresses motion blur. Other forms of blurriness, such as focus blur, atmospheric haze, and vibration-induced blur, were not included, limiting the model's adaptability to diverse real-world conditions. Expanding the dataset to include blurriness and environmental noise would enhance the model's robustness across a broader range of scenarios. Future work will aim

Complex & Intelligent Systems (2025) 11:63 Page 23 of 27

**Table 9** Compares the category results of different algorithms on the VisDrone test sets, categorized by different motion speed pairs, and displays F1 and the mean average precision ( *mAP\_0.5* ) measures

Methods Sharp Motion speed 20% Motion speed 40% Motion speed 60% Motion speed 80% Motion speed 100%

# F1(%)

*mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%) F1(%) *mAP* (%)

Baseline 59.3 51.9 58.5 51.3 57.8 50.8 57.2 50.2 56.5 49.7 55.7 49.2

Mimicking \[ 29 \] 52.7 44.9 51.9 44.2 51.2 43.5 50.6 42.8 49.7 42.3 48.9 41.9

# SSKD \[ 28 \]

50.3 41.2 49.8 40.6 49.3 40.1 48.8 39.6 48.3 39.1 47.8 38.6 Finegrained \[ 30 \]

49.2 41.7 48.6 41.3 48.1 40.7 47.6 40.3 47.1 39.8 46.5 39.4

# OFD \[ 31 \]

45.6 34.8 44.9 34.1 44.3 33.7 43.7 33.2 43.2 32.8 42.6 32.3

ReviewKD \[ 34 \] 47.3 39.5 46.9 38.9 46.2 38.4 45.7 37.9 45.2 37.6 44.6 37.2

# SSD \[ 23 \]

45.3 36.2 44.6 35.5 43.9 34.8 43.1 34.3 42.5 33.6 41.8 30.3

RetinaNet \[ 46 \] 49.0 47.5 48.2 36.9 47.6 36.3 46.9 35.8 46.3 35.2 45.6 34.5

# YOLOv5

\[ 47 \] 56.8 48.7 56.1 48.3 55.3 47.7 54.8 47.2 54.4 46.5 53.8 46.1

# YOLOv6

\[ 48 \] 58.5 48.2 57.9 47.5 57.3 46.9 56.7 46.2 56.1 45.6 55.5 44.9

# YOLOv7

\[ 49 \] 59.1 51.4 58.5 49.5 58.1 48.8 57.6 48.4 57.1 47.9 56.5 47.5

# YOLOv8

\[ 24 \] 61.3 53.5 60.6 52.8 59.9 52.3 59.4 51.8 58.8 51.3 58.2 50.8

SuperYOLO \[ 50 \] 63.4 55.1 62.8 54.5 62.2 53.9 61.7 53.3 61.3 52.8 60.9 52.3

Ours **65.1** **56.3** **64.5** **55.7** **63.9** **55.0** **63.4** **54.5** **62.7** **53.9** **62.4** **53.5** The best measures are in boldface

## to extend the model to account for these additional factors.

Furthermore, we plan to improve the dataset by incorporating more complex environmental conditions like fog, smog, humidity, and dust to increase the model's performance and robustness in real-world environments. Although our model was tested in offboard scenarios, its lightweight design offers the potential for onboard deployment in UAV applications. In future research, we will explore optimizing the model to reduce computational overhead for real-time object detection while maintaining high accuracy. This development will be particularly valuable for UAV operations, where efﬁciency and processing speed are crucial for effective performance in dynamic environments.

## Conclusion

## We present a novel object detection compression tech

nique based on knowledge distillation, validated across the

## SOD-Dataset and VisDrone datasets. Our method demon

strates efﬁcacy and adaptability in challenging environments. We introduce a self-supervised learning framework for object detection in motion-blurred images, integrating feature fusion across adjacent layers to enrich student learning. Additionally, attention mechanisms are incorporated into both teacher and student networks to capture essential low-level information and mitigate network overﬁtting. Furthermore, a deblurring subnet is integrated into the student network. A training dataset is curated, comprising pairs of sharp and blurred images annotated with objects. Subsequently, teacher and student networks are designed to process sharp and blurred images. Both networks are simultaneously trained in a fully-supervised manner within the context of self-supervised learning. The student network uses the teacher network's soft labels and hints to enhance its blurrobust object detection capabilities. Experimental results demonstrate notable performance enhancements for widely used object detectors across blur-synthesized and real-life images. On the SOD-Dataset, the mean average precision

Page 24 of 27 Complex & Intelligent Systems (2025) 11:63

**Fig. 17** Compares detection results for various motion speeds on the VisDrone dataset. Starting with a sharp image, we apply motion speeds up to 100% and attempt to detect objects using the original YOLOv8 and our proposed method. All models perform well on images with motion

speeds from sharp to 40%. However, detection accuracy drops significantly as the motion speed increases from 60 to 100%. Despite this, our proposed model still struggles to detect blurry and small objects, while YOLOv8 fails to achieve any results at higher motion speeds. This comparison further highlights the advantages of our proposed method

## (mAP\_0.5) achieves 63.4%, a 4.6% improvement from the

baseline, while on the VisDrone dataset, the mean average precision (mAP\_0.5) reaches 53.5%, a 4.3% increase from the baseline. Despite surpassing the teacher network's performance, potential limitations in generalization to diverse datasets and real-world conditions should be noted. For future endeavours, we aim to extend our method to encompass a broader range of models, including two-stage models. Additionally, we plan to explore advanced learning techniques such as hard data augmentation and complex loss functions commonly employed in object detection methods.

| Acknowledgements This work is supported by the National Natural | Science Foundation of China (No. 62176052) and the Natural Science | Foundation of Shanghai (No. 21ZR1401700). |
|:--- |:--- |:--- |
| Author contributions Conceptualization, S.J., X-s.T.; data curation, | S.J., and F.A.; formal analysis, X-s.T., and Y.Z.; investigation, G.L.; | methodology, S.J., and X-s.T.; supervision, X-s.T., Y.Z., and G.L.; |
| validation, X-s.T.; visualization, S.J., and F.A.; writing original draft, | S.J.; All authors have read and agreed to the published version of the | manuscript. |

**Author** ** ** **contributions** Conceptualization, S.J., X-s.T.; data curation, S.J., and F.A.; formal analysis, X-s.T., and Y.Z.; investigation, G.L.; methodology, S.J., and X-s.T.; supervision, X-s.T., Y.Z., and G.L.;

validation, X-s.T.; visualization, S.J., and F.A.; writing original draft, S.J.; All authors have read and agreed to the published version of the manuscript.

**Data availability** The dataset supporting this study's ﬁndings is available at <https://github.com/dhuvisionlab/SOD-Dataset.git>. The authors conﬁrm that the data supporting this study's ﬁndings are available from the corresponding author, \[Xue-song Tang\], upon reasonable request, and the data can also be obtained from reference materials.

## Declarations

**Conﬂict of interest** The authors declare that they have no known competing ﬁnancial interests or personal relationships that could have inﬂuenced the work reported in this paper.

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative

Complex & Intelligent Systems (2025) 11:63 Page 25 of 27

Commons licence, and indicate if you modiﬁed the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopyright holder. To view a copy of this licence, visit <http://creativecomm> ons.org/licenses/by-nc-nd/4.0/.

## References

1. Button M, Knickmeier S (2022) Economic and industrial espionage: characteristics, techniques and response. In: Gill M (ed) The handbook of security. Palgrave Macmillan, Cham. <https://doi.> org/10.1007/978-3-030-91735-7\_13 2. Martin JG, Davis CE, Riesenhuber M, Thorpe SJ (2018) High resolution human eye tracking during continuous visual search. Front Hum Neurosci. <https://doi.org/10.3389/fnhum.2018.00374> 3. Kitimbo A, Lucey A, Maru MT (2021) World migration report 2022: chapter 6 - peace and security as drivers of stability, development and safe migration, Geneva: International Organization for Migration, 2021Research Report, 2021/06, World Migration Report. <https://cadmus.eui.eu/handle/1814/76616> 4. Ciuffreda KJ, Wang B, Vasudevan B (2007) Conceptual model of human blur perception. Vision Res 47:1245-1252 5. Maiello G, Walker L, Bex PJ, Vera-Diaz FA (2017) Blur perception throughout the visual ﬁeld in myopia and emmetropia. J Vis 17(5):3. <https://doi.org/10.1167/17.5.3> 6. Abdelhack M, Kamitani Y (2018) Sharpening of hierarchical visual feature representations of blurred images. eNeuro. <https://doi.org/> 10.1523/ENEURO.0443-17.2018 7. Lei T et al (2024) Lightweight structure-aware transformer network for remote sensing image change detection. IEEE Geosci Remote Sens Lett. 21:1-5. <https://doi.org/10.1109/LGRS.2023.3323534> 8. Xie G et al (2024) IM-IAD: industrial image anomaly detection benchmark in manufacturing. IEEE Trans Cybern 54(5):2720-2733. <https://doi.org/10.1109/TCYB.2024.3357213> 9. Liu J, Jin Y (2023) A comprehensive survey of robust deep learning in computer vision. J Automat Intell. <https://doi.org/10.1016/j.jai.> 2023.10.002 10. Lei T et al (2023) Ultralightweight spatial-spectral feature cooperation network for change detection in remote sensing images. IEEE Trans Geosci Remote Sens 61:1-14. <https://doi.org/10.1109/> TGRS.2023.3261273 11. Xue D et al (2023) Triple change detection network via joint multifrequency and full-scale swin-transformer for remote sensing images. IEEE Trans Geosci Remote Sens 61:1-15. <https://doi.> org/10.1109/TGRS.2023.3320288 12. Wei W, Cheng Y, He J et al (2024) A review of small object detection based on deep learning. Neural Comput Applic 36:6283-6303. <https://doi.org/10.1007/s00521-024-09422-6> 13. Li M, Chen Y, Zhang T et al (2024) TA-YOLO: a lightweight small object detection model based on multi-dimensional transattention module for remote sensing images. Complex Intell Syst 10:5459-5473. <https://doi.org/10.1007/s40747-024-01448-6> 14. Hu X, Lin S (2024) DFFNet: a lightweight approach for efﬁcient feature-optimized fusion in steel strip surface defect detection. Complex Intell Syst. <https://doi.org/10.1007/s40747-024-01512-1> 15. Wan Y, Li J (2024) LGP-YOLO: an efﬁcient convolutional neural network for surface defect detection of light guide plate. Complex Intell Syst 10:2083-2105. <https://doi.org/10.1007/s40747023-01256-4>

16. Wang X, Liu J, Liu X et al (2022) Ship feature recognition methods for deep learning in complex marine environments. Complex Intell Syst 8:3881-3897. <https://doi.org/10.1007/s40747-022-00683-z> 17. Li X, He M, Liu Y et al (2023) SPCS: a spatial pyramid convolutional shufﬂe module for YOLO to detect occluded object. Complex Intell Syst 9:301-315. <https://doi.org/10.1007/s40747022-00786-7> 18. Zhang Y, Zhang Z, Zhang P et al (2023) Salient object detection for RGBD video via spatial interaction and depth-based boundary reﬁnement. Complex Intell Syst 9:6343-6358. <https://doi.org/10.> 1007/s40747-023-01072-w 19. Xie W, Zeng Y (2024) A knowledge distillation based cross-modal learning framework for the lithium-ion battery state of health estimation. Complex Intell Syst. <https://doi.org/10.1007/s40747-02401458-4> 20. Dong Y, Jiang Z, Tao F et al (2023) Multiple spatial residual network for object detection. Complex Intell Syst 9:1347-1362. <https://doi.org/10.1007/s40747-022-00859-7> 21. Terven JR, Esparza DM, Romero-González J (2023) A comprehensive review of YOLO architectures in computer vision: from YOLOv1 to YOLOv8 and YOLO-NAS. Mach Learn Knowl Extr 5:1680-1716 22. He K, Zhang X, Ren S, Sun J (2016) Deep residual learning for image recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, pp 770-778. https:// doi.org/10.1109/CVPR.2016.90 23. Liu W et al (2016) SSD: single shot multibox detector. In: Leibe B, Matas J, Sebe N, Welling M (eds) Computer vision ECCV 2016 ECCV2016.Lecturenotesincomputerscience,vol9905.Springer, Cham. <https://doi.org/10.1007/978-3-319-46448-0\_2> 24. Reis D, Kupec J, Hong J, Daoudi A (2023) Real-time ﬂying object detection with YOLOv8. <https://arxiv.org/abs/2305.09972> 25. Hinton GE, Vinyals O, Dean J (2015) Distilling the knowledge in a neural network. <https://arxiv.org/abs/1503.02531> 26. Jin Li C, Qu Z, Ye Wang S (2023) A method of knowledge distillation based on feature fusion and attention mechanism for complex trafﬁc scenes. Eng. Appl. Artif. Intell. 124:106533. <https://doi.org/> 10.1016/j.engappai.2023.106533 27. Gou J, Yu B, Maybank SJ et al (2021) Knowledge distillation: a survey. Int J Comput Vis 129:1789-1819. <https://doi.org/10.1007/> s11263-021-01453-z 28. Gao M, Shen Y, Li Q, Yan J, Wan L, Lin D, Loy CC, Tang X (2018) An embarrassingly simple approach for knowledge distillation. Comput Vis Pattern Recognit. <https://arxiv.org/abs/1708.> 29. Li Q, Jin S, Yan J (2017) Mimicking very efﬁcient network for object detection. IEEE Conf Comput Vision Pattern Recogn (CVPR) 2017:7341-7349 30. Wang T, Yuan L, Zhang X, Feng J (2019) Distilling object detectors with ﬁne-grained feature imitation. IEEE/CVF Conf Comput Vision Pattern Recogn (CVPR) 2019:4928-4937 31. Heo B, Kim J, Yun S, Park H, Kwak N, Choi JY (2019) A comprehensive overhaul of feature distillation. 2019 IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, Korea (South). pp. 1921-1930. <https://doi.org/10.1109/ICCV.> 2019.00201. 32. Yim J, Joo D, Bae J, Kim J (2017) A gift from knowledge distillation: fast optimization, network minimization and transfer learning. IEEE Conf Comput Vision Pattern Recogn (CVPR) 2017:7130-7138 33. Tung F, Mori G (2019) Similarity-preserving knowledge distillation. 2019 IEEE/CVF International Conference on Computer Vision (ICCV), Seoul, Korea (South). pp. 1365-1374. <https://doi.> org/10.1109/ICCV.2019.00145.

Page 26 of 27 Complex & Intelligent Systems (2025) 11:63

34. Chen P, Liu S, Zhao S, Jia J (2021) Distilling Knowledge via Knowledge Review. 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville. 2021. pp. 5006-5015. <https://doi.org/10.1109/CVPR46437.2021.00497>. 35. Cho S, Kim S, Jung S, Ko S (2022) Blur-robust object detection using feature-level deblurring via self-guided knowledge distillation. IEEE Access 10:79491-79501 36. Tao X, Gao H, Shen X, Wang J, Jia J (2018) Scale-recurrent network for deep image deblurring. 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, Salt Lake City. pp. 8174-8182. <https://doi.org/10.1109/CVPR.2018.00853>. 37. He Y, Li J (2023) TSRes-YOLO: an accurate and fast cascaded detector for waste collection and transportation supervision. Eng. Appl. Artif. Intell. 126:106997. <https://doi.org/10.1016/j.engappai.> 2023.106997 38. Woo S, Park J, Lee JY, Kweon IS (2018) CBAM: Convolutional block attention module. In: Ferrari V, Hebert M, Sminchisescu C, Weiss Y (eds) Computer Vision - ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11211. Springer, Cham. <https://doi.org/10.1007/978-3-030-01234-2\_1> 39. Narayanan M (2023). SENetV2: aggregated dense layer for channelwise and global representations. ArXiv, abs/2311.10807. 40. Xiang Y, Zhou H, Li C, Sun F, Li Z, Xie Y (2024) Application of deep learning in blind motion deblurring: current status and future prospects. <http://arxiv.org/abs/2401.05055> 41. Dai J, et al. (2017) Deformable Convolutional Networks. 2017 IEEE International Conference on Computer Vision (ICCV), Venice. pp. 764-773. <https://doi.org/10.1109/ICCV.2017.89>. 42. Paszke A, Gross S, Massa F, Lerer A, Bradbury J, Chanan G, Killeen T, Lin Z, Gimelshein N, Antiga L, Desmaison A, Köpf A, Yang E, DeVito Z, Raison M, Tejani A, Chilamkurthy S, Steiner B, Fang L, Bai J, Chintala S (2019) PyTorch: an imperative style, high-performance deep learning library. <https://arxiv.org/abs/1912.> 43. Tzutalin, "labelImg. 2015. Available online: <https://github.com/> tzutalin/labelImg (accessed on 27 July 2015)" 44. Zhu PF, Wen L, Bian X, Ling H, Hu Q (2018) Vision meets drones: a challenge. <https://arxiv.org/abs/1804.07437> 45. Cheng X, Li Y (2022) An improved Hoeffding's inequality for sum of independent random variables. Stat Prob Lett. <https://doi.org/10.> 1016/j.spl.2021.109349 46. Lin TY, Goyal P, Girshick R, He K, Dollár P (2017) Focal loss for dense object detection. 2017 IEEE International Conference on Computer Vision (ICCV), Venice. pp. 2999-3007. <https://doi.org/> 10.1109/ICCV.2017.324. 47. Ultralytics, "YOLOv5. 2020. Available online: <https://github.com/> ultralytics/yolov5 (accessed on 25 June 2020)". 48. Li C, Li L, Jiang H, Weng K, Geng Y, Li L, Ke Z, Li Q, Cheng M, Nie W, Li Y, Zhang B, Liang Y, Zhou L, Xu X, Chu X, Wei X, Wei X (2022) YOLOv6: a single-stage object detection framework for industrial applications. ArXiv, abs/2209.02976. 49. Wang C, Bochkovskiy A, Liao HM (2022) YOLOv7: trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. IEEE/CVF Conf Comput Vision Pattern Recogn (CVPR) 2023:7464-7475 50. Zhang J, Lei J, Xie W, Fang Z, Li Y, Du Q (2023) SuperYOLO: super resolution assisted object detection in multimodal remote sensing imagery. IEEE Trans Geosci Remote Sens 61:1-15. https:// doi.org/10.1109/TGRS.2023.3258666 51. Everingham M, Van Gool L, Williams CK, Winn J, Zisserman A (2010) The pascal visual object classes (voc) challenge. Int J Comput Vision 88(2):303-338 52. Lin TY, Maire M, Belongie S, Hays J, Perona P, Ramanan D, Dollar P, Zitnick CL (2014) Microsoft coco: common objects in context. In: European Conference on Computer Vision. Springer, Cham, pp 740-755

53. Geiger A, Lenz P, Urtasun R (2012) Are we ready for autonomous driving? The kitti vision benchmark suite. In: 2012 IEEE Conference on Computer Vision and Pattern Recognition. IEEE. pp. 3354-3361. 54. Du D, Qi Y, Yu H, Yang Y, Duan K, Li G, Zhang W, Huang Q, Tian Q (2018) The unmanned aerial vehicle benchmark: Object detection and tracking. Proceedings of the European Conference on Computer Vision. pp. 370-386. 55. Khosla D, Chen Y, Kim K (2014) A neuromorphic system for video object recognition. Front Comput Neurosci 8:147 56. ChengG,HanJ,ZhouP,GuoL(2014)Multi-classgeospatialobject detection and geographic image classiﬁcation based on collection of part detectors. ISPRS J Photogramm Remote Sens 98:119-132 57. Yang Y, Newsam S (2011) Spatial pyramid co-occurrence for image classiﬁcation. In: 2011 International Conference on Computer Vision. IEEE. pp. 1465-1472. 58. Xia G-S, Bai X, Ding J, Zhu Z, Belongie S, Luo J, Datcu M, Pelillo M, Zhang L (2018) Dota: a large-scale dataset for object detection in aerial images. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. pp. 3974-3983. 59. Razakarivony S, Jurie F (2016) Vehicle detection in aerial imagery: a small target detection benchmark. J Vis Commun Image Represent 34:187-203 60. Li K, Wan G, Cheng G, Meng L, Han J (2020) Object detection in optical remote sensing images: a survey and a new benchmark. ISPRS J Photogramm Remote Sens 159:296-307 61. Ye T, Qin W, Zhao Z, Gao X, Deng X, Ouyang Y (2023) Real-time object detection network in uav-vision based on cnn and transformer. IEEE Trans Instrum Meas 72:1-13 62. Rekavandi AM, Xu L, Boussaid F, Seghouane A, Hoefs S, Bennamoun (2022) A guide to image and video based small object detection using deep learning: case study of maritime surveillance. ArXiv, abs/2207.12926. 63. Rekavandi AM, Rashidi S, Boussaid F, Hoefs S, Akbas E, Bennamoun M (2023) Transformers in small object detection: a benchmark and survey of state-of-the-art. <https://arxiv.org/abs/> 2309.04902 64. Pathak D, Krähenbühl P, Donahue J, Darrell T, Efros AA (2016) Context encoders:feature learning by inpainting. In: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 2536-2544. <https://doi.org/10.> 1109/CVPR.2016.278 65. Zhang R, Isola P, Efros AA (2016) Colorful image colorization. In: Leibe B, Matas J, Sebe N, Welling M (eds) ECCV 2016. LNCS vol 9907. Springer, Cham. pp 649-666 66. Noroozi M, Vinjimoor A, Favaro P, Pirsiavash H (2018) Boosting self-supervised learning via knowledge transfer. IEEE/CVF Conf Comput Vision Pattern Recogn 2018:9359-9367 67. Xu G, Liu Z, Li X, Loy CC (2020) Knowledge distillation meets self-supervision. European Conference on Computer Vision. Springer International Publishing, Cham 68. Yin J, Qiu J, Zhang S, Ma Z, Guo J (2020) SSKD: Self-Supervised Knowledge Distillation for Cross Domain Adaptive Person ReIdentiﬁcation. 2021 7th IEEE International Conference on Network Intelligence and Digital Content (IC-NIDC). pp 81-85. 69. Zhan X, Xie J, Liu Z, Ong YS, Loy CC (2020) Online deep clustering for unsupervised representation learning. IEEE/CVF Conf Comput Vision Pattern Recogn (CVPR) 2020:6687-6696 70. Donahue J, Simonyan K (2019) Large scale adversarial representation learning. In:Advances in Neural Information Processing Systems. pp. 10541-10551 71. Dumoulin V, Belghazi I, Poole B, Lamb A, Arjovsky M, Mastropietro O, Courville AC (2016) Adversarially learned inference. <https://arxiv.org/abs/1606.00704>

Complex & Intelligent Systems (2025) 11:63 Page 27 of 27

72. Chen T, Kornblith S, Norouzi M, Hinton GE (2020) A simple framework for contrastive learning of visual representations. <https://arxiv.org/abs/2002.05709> 73. Hénaff OJ, Srinivas A, Fauw JD, Razavi A, Doersch C, Eslami SM, Oord AV (2019) Data-efﬁcient image recognition with contrastive predictive coding. <https://arxiv.org/abs/1905.09272> 74. Balestriero R, Ibrahim M, Sobal V, Morcos AS, Shekhar S, Goldstein T, Bordes F, Bardes A, Mialon G, Tian Y, Schwarzschild A, Wilson AG, Geiping J, Garrido Q, Fernandez P, Bar A, Pirsiavash H, LeCun Y, Goldblum M (2023) A cookbook of self-supervised learning. <https://arxiv.org/abs/2304.12210> 75. GuiJ,ChenT,ZhangJ,CaoQ,SunZ,LuoH,TaoD(2023)Asurvey on self-supervised learning: algorithms, applications, and future trends. IEEE Trans Pattern Anal Mach Intell 46(12):9052-9071. <https://doi.org/10.1109/TPAMI.2024.3415112> 76. He K, Zhang X, Ren S, Sun J (2015) Spatial pyramid pooling in deep convolutional networks for visual recognition. IEEE Trans Pattern Anal Mach Intell. 37(9):1904-1916. <https://doi.org/> 10.1109/TPAMI.2015.2389824

77. Glorot Xavier, Yoshua Bengio (2010) Understanding the difﬁculty of training deep feedforward neural networks. International Conference on Artiﬁcial Intelligence and Statistics.

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afﬁliations.