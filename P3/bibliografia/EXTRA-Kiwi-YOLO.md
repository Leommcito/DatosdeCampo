Academic Editor: Jayme Garcia Arnal Barbedo Received: 12 July 2025 Revised: 3 August 2025 Accepted: 6 August 2025 Published: 20 October 2025 **Citation:** Zhou, J.; Sun, F.; Wu, H.; Lv, Q.; Feng, F.; Zhao, B.; Li, X. Kiwi-YOLO: A Kiwifruit Object Detection Algorithm for Complex Orchard Environments. * Agronomy* **2025**, * 15*, 2424. <https://doi.org/> 10.3390/agronomy15102424 **Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (<https://creativecommons.org/> licenses/by/4.0/).

# Article

**Kiwi-YOLO: A Kiwifruit Object Detection Algorithm for** **Complex Orchard Environments**

**Jie Zhou** ** ** **1** **, Fuchun Sun** ** ** **1,** **\*, Haorong Wu** ** ** **2** **, Qiurong Lv** ** ** **1** **, Fan Feng** ** ** **2** **, Bangtai Zhao** ** ** **3** ** ** **and Xiaoxiao Li** ** ** **1**

School of Mechanical Engineering, Chengdu University, Chengdu 610106, China; 212024085501027@cdu.edu.cn (J.Z.); 212023085501014@cdu.edu.cn (Q.L.); lixiaoxiao@cdu.edu.cn (X.L.) School of Electronic Information and Electrical Engineering, Chengdu University, Chengdu 610106, China; wuhaorong3150@cdu.edu.cn (H.W.); feng\_sylvie@163.com (F.F.) Sichuan Academy of Agricultural Machinery Sciences, Chengdu 610066, China; 212024085501028@cdu.edu.cn **\*** Correspondence: sfc@cdu.edu.cn; Tel.: +86-199-8040-9129 **Abstract**

To address the challenges of poor model adaptability and high computational complexity in complex orchard environments characterized by variable lighting, severe occlusion, and dense fruit clusters, an enhanced kiwifruit detection network, Kiwi-YOLO, is proposed based on YOLOv8. Firstly, replacing the main network with the * * *MobileViTv1* module reduces computational load and parameters, thus enhancing inference efficiency for mobile deployment. Secondly, incorporating * BiFPN* into the model's neck as a replacement for PANet improves feature distinguishability between background regions and target instances. Additionally, incorporating * MCA* module promotes cross-dimensional feature interactions, strengthening model robustness and generalization performance. Finally, the *MPDIoU* loss function is adopted to minimize bounding box vertex distances, mitigating detection box distortion caused by sample heterogeneity while accelerating convergence and enhancing localization accuracy. Experimental results indicate that the enhanced model achieves improvements of 2.1%, 1.5% and 0.3% in * precision*, * recall*, and * mAP*, respectively, over the baseline YOLOv8, while reducing * parameters (Params)* and * computational complexity* *(GFLOPs)* by * 19.71* million and * 2.8* billion operations. Moreover, it surpasses other comparative models in performance. Furthermore, in experiments detecting kiwifruit targets under complex lighting and occlusion conditions, the Kiwi-YOLO model demonstrated excellent adaptability and robustness. Its strong environmental adaptability provides technical guidance for advancing the practical application of unmanned intelligent kiwifruit harvesting.

**Keywords:** kiwifruit; machine vision; YOLOv8; attention mechanism; deep learning

## 1. Introduction

With the steady growth of domestic and international market demand, China's kiwifruit production and planting area have also been expanding continuously. As the world's leading producer of kiwifruit, China boasts an annual output exceeding 3 million tons \[ 1 \], ranking first globally in both cultivation area and production volume \[ 2 \]. Kiwifruit has become a vital cash crop for the country. In this context, harvesting, being the most labor-intensive and time-consuming stage of the production process, underscores its critical importance \[ 3 \]. Currently, kiwifruit is primarily harvested manually, which involves high labor intensity. Additionally, as China's population ages, the available workforce is shrinking, leading to rising agricultural production costs \[ 4 \]. Additionally, kiwifruit harvesting must occur within a narrow timeframe to preserve quality; delayed <https://doi.org/10.3390/agronomy15102424> 2 of 22

picking causes softening, compromising subsequent transport and storage \[ 5 \]. Therefore, intelligent harvesting robot development yields considerable potential. Achieving precise fruit recognition by mitigating complex environmental interference represents a critical technical challenge in developing intelligent kiwifruit harvesting systems. Traditional visual detection methods typically follow the technical workflow of "image preprocessingfeature engineering-classification recognition" \[ 6 \], utilizing techniques such as color space transformation \[ 7 \] (e.g., HSV, Lab), morphological operations \[ 8 \], and texture feature segmentation \[ 9 \] for target detection. While these algorithms demonstrate some effectiveness under ideal lighting conditions and in unobstructed scenarios, their recognition accuracy and robustness significantly decline when faced with complex environmental conditions commonly encountered in natural settings, such as leaf obstruction, fruit overlap, and sudden changes in lighting (e.g., strong light reflection or shadow coverage). This exposes inherent limitations such as poor environmental adaptability, significant fluctuations in misclassification rates, and inability to meet real-time operational requirements \[ 10 \]. These constraints have motivated the accelerated adoption and advancement of deep learning-based detection methodologies in this domain. In agricultural intelligent application scenarios, deep learning methods have demonstrated breakthrough progress in visual tasks such as fruit phenotyping and pest and disease identification through multi-layer nonlinear feature extraction mechanisms \[ 11, 12 \]. Compared to algorithms that rely on manually designed features, models based on convolutional neural networks \[ 13 \] or Transformer architectures \[ 14 \] leverage their robust feature self-learning capabilities and end-to-end optimization properties. This not only significantly enhances the robustness of object detection in complex field environments (e.g., continuous tracking of occluded fruits) but also achieves dual breakthroughs in detection accuracy (AP values improved by 15-30%) and processing efficiency (FPS reaching 40+) under the guidance of advanced frameworks such as YOLO \[ 15 \] and Mask R-CNN \[ 16 \] and other advanced frameworks, achieving dual breakthroughs in detection accuracy (AP values improved by 15-30%) and processing efficiency (FPS reaching 40+), providing innovative solutions for the visual perception systems of agricultural equipment. Dai et al. \[ 17 \] built an improved model for precise kiwifruit detection based on the YOLOv5s model, combining stereo vision technology with the Coordinate Attention mechanism and the Bidirectional Feature Pyramid Network (BiFPN). Liu et al. \[ 18 \] achieved accurate detection of green apples by introducing the ResNeXt network into DETR and adding a variable attention mechanism. Jia et al. \[ 19 \] significantly improved apple detection accuracy by modifying the Mask R-CNN model to combine residual networks (ResNet) with dense connection convolutional networks (DenseNet). Xie et al. \[ 20 \] presented YOLOv5-Litchi, a YOLOv5-based detection framework for lychee targets in agricultural settings. By introducing the CBAM attention mechanism and using non-maximum suppression (NMS) as the prediction box fusion method, they achieved significant results in lychee detection. Li et al. \[ 21 \] proposed an improved YOLOv7-tiny model, which employs lightweight Ghost convolutions, coordinate attention (CA) modules, and WIoU loss functions to achieve accurate identification of strawberries at different growth stages. Sun et al. \[ 22 \] optimized the YOLOv7 model by adding the MobileOne module, SPPFCSPC pyramid pooling, and Focal-EIoU loss function, thereby improving grape detection accuracy and reducing model parameters. Li et al. \[ 23 \] proposed a YOLOv7-CS model, which introduced SPD-Conv detection heads, a global attention mechanism (GAM), and a Wise-IoU loss function, achieving good results in bayberry detection. Lv et al. \[ 24 \] used YOLOv7 as the base model, constructing PC-ELAN and GS-ELAN modules and embedding a BiFormer attention mechanism to achieve precise identification of citrus fruits. 3 of 22

While prior research has achieved substantial improvements in fruit recognition algorithms, most experiments are still based on idealized environmental parameter settings. Specifically, in the context of kiwifruit orchards, the complex environmental conditions pose multiple challenges to detection technology: first, the high-density planting system formed by the main trunk-type wide-row dense planting structure results in high canopy closure, with fruit spatial distribution exhibiting typical cluster-like characteristics, and widespread phenomena of multiple branch and leaf obstructions and fruit overlap; second, the strong canopy heterogeneity caused by the cultivation mode results in uneven light intensity distribution, with significant differences in visible light reflectance characteristics among fruits on different sides of individual trees. The interaction between these morphological features and optical properties affects the precise detection of kiwifruit. To overcome these limitations, this study introduces Kiwi-YOLO, a novel deep learning model designed specifically for robust kiwifruit detection in complex orchard environments. This study made the following improvements to the proposed Kiwi-YOLO kiwifruit detection network:

(1) In the main network, the Conv and C2f modules are replaced with MobileViTv1 modules to reduce computational load and parameter count, thereby improving inference efficiency on mobile devices. (2) The bidirectional feature pyramid network (BiFPN) is introduced into the feature fusion layer of the base model to replace the original PANet structure, enhancing the model's ability to distinguish between obstacles and backgrounds through the efficient fusion of cross-scale features. (3) To improve the model's interference resistance and transfer performance, a multidimensional collaborative attention (MCA) mechanism is introduced to strengthen the robustness of feature expression. (4) By using the MPDIoU loss function and minimizing the distance between the corners of the bounding box, we can effectively mitigate geometric distortion of the detection box caused by sample differences, accelerate model convergence, and improve target localization accuracy.

## 2. Materials and Methods *2.1.* * * *Experimental Data*

This study employs a publicly accessible dataset. Further details are available at: <https://data.mendeley.com/datasets/stm3cb6y7r/1> (accessed on 1 May 2025) \[ 25 \]. The kiwifruits in the dataset were cultivated using dwarf intensive planting, resulting in high canopy closure and typical cluster-like spatial distribution of the fruit. The dataset contains 2836 kiwifruit images. After removing images with high similarity and high blurring, 2170 high-quality original kiwifruit images were obtained. The dataset comprises JPGformat images at 3024 * ×* 4032 pixel resolution. The dataset covers kiwifruit under various lighting and distance conditions, including scenarios with leaf obstruction, fruit overlap, single fruits, and multiple fruits, effectively reflecting the complexity of natural environments. Kiwifruit specimens under varying conditions are presented in Figure 1. *2.2.* * * *Dataset Creation*

To mitigate interference from illumination variance, image clarity degradation, and sensor noise in kiwifruit detection, the original dataset was augmented to enhance environmental complexity and representational fidelity. This expansion facilitates comprehensive learning of kiwifruit morphological signatures within naturalistic settings, thereby improving model generalization under challenging field conditions. The augmentation protocol incorporated: brightness adjustment, Gaussian blurring, Gaussian noise injection, mirror- 4 of 22

ing, rotation, and translation operations. Representative augmented samples are depicted in Figure 2. Furthermore, kiwifruit instances were manually annotated using LabelImg (version 1.8.5) software with axis-aligned bounding boxes assigned the class label "kiwi", subsequently exported as YOLO-format annotation files. ( **a** ) ( **b** ) ( **c** ) ( **d** ) ( **e** ) ( **f** ) ( **g** ) ( **h** )

**Figure 1.** Images of a kiwifruit: ( **a** ) single fruit; ( **b** ) multiple fruits; ( **c** ) overcast; ( **d** ) sunny; ( **e** ) leaves occlusion; ( **f** ) stem occlusion; ( **g** ) overlap; ( **h** ) long distance. ( **a** ) ( **b** ) ( **c** ) ( **d** ) ( **e** ) ( **f** ) ( **g** ) ( **h** )

**Figure 2.** Kiwifruit data augmentation: ( **a** ) original image; ( **b** ) darkened; ( **c** ) brightened; ( **d** ) Gaussian blurring; ( **e** ) Gaussian noise; ( **f** ) rotation; ( **g** ) translation; ( **h** ) mirroring. *2.3.* * * *YOLOv8 Network Model*

The YOLOv8 framework incorporates three fundamental modules: a feature extraction backbone, a multi-scale feature fusion neck, and a detection head \[ 26 \]. As an evolutionary upgrade to YOLOv5, YOLOv8 employs a CSPDarkNet-53 backbone for hierarchical feature extraction. The backbone network's core enhancement involves substituting the 5 of 22

conventional C3 module with a C2f module-a cross-stage partially connected structure featuring dual convolutional layers-yielding three optimized feature layers. Subsequently, the Neck module employs an enhanced PAN-FPN architecture, adapted from YOLOv5's feature fusion paradigm, to aggregate multi-scale features (P3, P4, P5) from the backbone network. This hierarchical integration optimizes discriminative feature representation for detection tasks. Finally, YOLOv8 employs a decoupled head, which consists of independent classifiers and bounding box regressors for predicting the category and position of objects at feature points, respectively. The YOLOv8 algorithm architecture is depicted in Figure 3. Conv Conv C2f Conv C2f Conv C2f Conv C2f

# SPPF Upsample Concat C2f Upsample Concat C2f Conv Concat C2f Conv Concat Detect Detect Detect C2f

C2f Conv Split Bottleneck Bottleneck Concat Conv

SPPF Conv MaxPool2d MaxPool2d MaxPool2d Contcat Conv Conv Conv2d BatchNorm2d Conv2d Bottleneck Conv Conv Input Backbone Head **Figure 3.** YOLOv8 structural diagram.

YOLOv8 offers five model specifications (n, s, m, l, x) to accommodate a wide range of needs, from resource-constrained scenarios to those seeking peak performance. These architecturally homogeneous models modulate network width (channel count) and depth (layer count) to optimize the speed-accuracy trade-off. Among them, the compact YOLOv8n variant achieves minimal computational overhead and accelerated inference throughput, rendering it optimal for edge deployment and high-frame-rate applications. In contrast, the largest YOLOv8x model offers the highest detection accuracy but also comes with higher model complexity and computational overhead. To meet high FPS requirements and simplify deployment processes, this study focuses on optimizing YOLOv8n, minimizing resource consumption while ensuring real-time detection capabilities. *2.4.* * * *Kiwi-YOLO Algorithm*

The YOLOv8 enhances computational efficiency through its Cross Stage Partial (CSP) backbone architecture and anchor-free prediction head, eliminating redundant operations. Compared to YOLOv5 and YOLOv7, it achieves faster inference speeds at the same accuracy level, but still faces issues such as large model size \[ 27 \]. Additionally, in complex orchard environments with uneven lighting conditions, it struggles to effectively detect occluded, 6 of 22

dense, and distant targets. Therefore, this study proposes a model improvement for the YOLOv8 algorithm, introducing a more efficient kiwifruit object detection algorithm called Kiwi-YOLO. First, the backbone network is supplanted by MobileViT, effectuating a significant reduction in learnable parameters and computational complexity. Second, the BiFPN is integrated into the model's neck section, replacing the initial PANet architecture to strengthen feature discrimination between background and target objects. Additionally, the MCA module is incorporated to boost the model's robustness and generalization capabilities. Lastly, the MPDIoU loss function is implemented; by minimizing vertex distances of bounding boxes, it effectively alleviates detection box distortion induced by sample heterogeneity while accelerating convergence and enhancing object localization precision. The architectural framework of the enhanced Kiwi-YOLO algorithm is delineated in Figure 4. Conv MobileNetV2 MobileNetV2 MobileNetV2 MobileNetV2 MobileNetV2 MobileViT MobileNetV2 MobileViT MobileNetV2 MobileViT Upsample

# BiPFN C2f Upsample

# BiPFN C2f Conv

# BiPFN C2f Conv

# BiPFN C2f

# MCA Detect Detect Detect Detect Conv Conv Conv Conv Conv2d Conv2d Bbox Loss Cls Loss

MobileNetV2 Conv BN ReLU ReLU BN DWconv Conv BN Backone Head **Figure 4.** Kiwi-YOLO Block Diagram. 2.4.1. MobileViTv1 Model

MobileViTv1 employs a hardware-efficient hybrid architecture that fuses convolutional inductive biases with transformer-based global context modeling, optimized for mobile compute constraints. The model works through the collaboration of two structures, retaining the high efficiency of CNNs while also possessing the global perception capabilities of Transformers. Specifically, traditional CNNs excel at local feature extraction but struggle with capturing global correlations and suffer from information decay due to high-frequency convolutions; while Transformers excel at modeling long-range dependencies and analyzing adjacent region relationships, their complex structure and lack of inherent inductive biases for visual tasks can lead to performance degradation when directly applied to detection tasks. To balance performance and efficiency, MobileViTv1 offers three streamlined configuration options: XS/S/XXS. This study adopts the MobileViT-XXS model, which is the lightest version in the MobileViTv1 series. It maintains low computational complexity 7 of 22

while still providing acceptable performance, meeting the dual requirements of real-time processing and accuracy in mobile image recognition scenarios. Its core architecture is composed of two innovative modules: MobileViT and MobileNetV2 \[ 28 \]. The MobileNetV2 module is a lightweight convolutional structure optimized for mobile devices. Its core design incorporates an inverted residual architecture and a linear bottleneck layer: first, channel cardinality is modulated via 1 * ×* 1 pointwise convolutions, succeeded by 3 * * *×* 3 depthwise separable convolutions for spatial context aggregation, and finally, 1 * * *×* 1 convolutions are employed to compress the channels while retaining linear activations. This approach avoids the loss of low-dimensional information caused by traditional ReLU activations. The architectural configuration is depicted in Figure 5. This structure enhances feature expression capabilities through a strategy of first increasing and then reducing dimensions, combined with separable convolutions to substantially compress parameter count and computational demands. It attains real-time performance while preserving competitive accuracy, with broad deployment in mobile vision tasks including image classification and object detection.

Conv 1 ｘ 1 BN ReLU DWconv BN ReLU Conv 1 ｘ 1 BN **Figure 5.** MobileNetV2 module.

The MobileViT module comprises three primary components: a local representation block, a global representation block, and a feature fusion block, with its architecture denoted as Figure 6. Initially, an input feature map of dimensions W * ×* H with C channels, represented as X * ∈* R (H *×* W *×* C), undergoes feature extraction through an * n* * ×* * n* convolution operation to capture kiwifruit image characteristics. Subsequently, channel adjustment is performed via a 1 * * *×* 1 convolutional layer. Subsequently, global feature modeling is performed sequentially through sequence unfolding, Transformer, and sequence folding structures, and the channels are adjusted back to their original size using a 1 * ×* 1 convolution kernel; finally, the feature map is concatenated with the original feature map, and feature fusion is performed using an * n* * ×* * n* convolution kernel to obtain the final kiwifruit feature results. x

# C

# H

# W Conv n ｘ n Conv 1 ｘ 1 Transfermer Conv 1 ｘ 1

| Conv | nｘn |
|:--- |:--- |
| Local | characteristic |
| global | representation |
| d | d | Local characteristic global representation *d* *d*

# H

# W

# N *P* *L* ｘ * * *d*

# N

# P *W*

# H *d* C

# H *W*

# C

# H

# W

# 2C

# H *W*

Serial expansion Serial folding Feature fusion **Figure 6.** MobileViT module.

2.4.2. BiFPN Bidirectional Feature Pyramid Network

YOLOv8's neck network incorporates the PANet framework with dual pathways: a top-down FPN for multi-scale feature aggregation and a bottom-up feature refinement path for spatial enhancement. Despite employing bidirectional fusion for multi-scale feature integration, the architecture exhibits limitations in cross-layer semantic alignment \[ 29 \], the PANet structure is shown in Figure 7. To address this, this study adopts the BiFPN bidi- 8 of 22

rectional weighted feature pyramid for architectural upgrading: this structure optimizes cross-scale jump connections, removes single-input edge nodes (redundant feature layers), and establishes bidirectional interaction channels between nodes at the same level, forming a weighted feature re-calibration mechanism. This architecture substantially optimizes cross-level feature propagation efficacy between spatially rich shallow representations and semantically abstract deep features. The BiFPN structure is shown in Figure 8. By dynamically adjusting the contribution of features at different resolutions through learnable feature weights, the network improves its representation capability for multi-scale targets in complex scenes while maintaining computational complexity comparable to the original PANet.

# C5

# C4

# C3

# C2

# P5

# P4

# P3

# P2

# N2

# N3

# N4

# N5

# N2=P2 (a) (b) Input

**Figure** ** ** **7.** PANet architecture: ( **a** ) FPN architecture; ( **b** ) bottom-up architecture. ( **a**, **b** ) together constitute the PANet architecture. Red dashed paths denote bottom-up feature propagation from lower to higher hierarchies via multi-step convolutional transformations, while green dashed paths implement cross-layer fusion where lower-level features integrate into adjacent and subsequent layers until the final stage (C2 *→* P2 *→* N2 *→* N5), substantially compressing convolutional operations count. P7\_in P6\_in P5\_in P4\_in P3\_in P6\_td P5\_td P4\_td P7\_0ut P6\_0ut P5\_0ut P4\_0ut P3\_0ut

# P7

# P6

# P5

# P4

# P3

# W2

# W1

# W1' W2' Resize W3' Resize Input

**Figure 8.** BiFPN structure. P3, P4, and P5 represent the backbone's multi-resolution output features, which are downsampled twice to obtain P6 and P7, followed by a convolution operation to adjust the channels and obtain the input * * *P* *in* *n*. The middle part is * * *P* *td* *n* in the following equation; * W* *n* is the weighting factor; the right part is * P* *out* *n*.

Furthermore, each bidirectional fusion network-comprising top-down and bottomup pathways-is treated as a feature network layer. This structure is iteratively stacked to perform weighted feature fusion. During fusion, learnable weight parameters are assigned 9 of 22

## to emphasize target-specific features, which are optimized through training. The formal

expression for BiFPN's weighted feature fusion is given below:

## O = \\sumi

*W* *i* * ×* * I* *i* *ϵ* + ∑ *j* * W* *j* (1)

## In the formula: ε represents the learning rate, set to 0.0001 to ensure numerical stability;

*W* *i* and * W* *j* represent weight parameters; * I* *i* represents input factors. Using sixth-layer feature fusion as an example, the computational expression is:

## P td 6 = Conv

## \\omega1 \\cdot Pin 6 + \omega2 \cdot Resize   *P* *in* 

## \\omega1 + \\omega2 + ϵ

##!

## (2)

## P out = * Conv*

## \\omega′

1 * * *·* * P* *in* 6 + \omega′ 2 * * *·* * P* *td* 6 + \omega′ 3 * * *·* * Resize* ( *P* *out* ) \omega′ 1 + \omega′ 2 + \omega′ 3 + * ϵ*

##!

## (3)

## In the formula: P in

*a* denotes the features of the input nodes in layer a, * Resize* refers to upsampling or downsampling, * Conv* denotes convolution, * P* *td* *a* denotes the features of the intermediate nodes between the input and output nodes in layer a, and * P* *out* *a* denotes the features of the output nodes in layer a.

## 2.4.3. MCA Mechanism

## The MCA module constitutes a lightweight yet efficient attention mechanism, exhibit

ing robust generalization capabilities across diverse network architectures and datasets. As depicted in Figure 9, MCA's structure integrates three parallel branches that concurrently model attention along distinct dimensions: the top branch processes feature interactions across spatial dimension W, the middle branch handles interactions along spatial dimension H, while the bottom branch manages cross-channel correlations. Within the spatial branches (W/H), permutation operations capture long-range dependencies between channel and spatial dimensions. The integration phase subsequently aggregates all branch outputs through simple averaging. Input Residual Permute AvgPool&StdPool Permute 1 ｘ K Conv2d Permute Permute C ｘ H ｘ W H ｘ C ｘ W H ｘ 1 ｘ 1 1 ｘ 1 ｘ *H* 1 ｘ 1 ｘ *H* H ｘ 1 ｘ 1 H ｘ C ｘ W Sigmoid Permute AvgPool&StdPool Permute 1 ｘ K Conv2d Permute Permute C ｘ H ｘ W W ｘ H ｘ C W ｘ 1 ｘ 1 1 ｘ 1 ｘ W 1 ｘ 1 ｘ W W ｘ 1 ｘ 1 Sigmoid W ｘ H ｘ C AvgPool&StdPool Permute 1 ｘ K Conv2d Permute C ｘ H ｘ W C ｘ 1 ｘ 1 1 ｘ 1 ｘ C 1 ｘ 1 ｘ C C ｘ 1 ｘ 1 C ｘ H ｘ W C ｘ H ｘ W C ｘ H ｘ W Sigmoid Output

## Figure 9. Schematic diagram of MCA module structure.

## MCA's fundamental constituents encompass Squeeze Transformation \[ 30 \] and Exci

tation Transformation \[ 31 \]. The Squeeze Transformation in MCA leverages an adaptive 10 of 22

fusion mechanism to integrate features derived from average pooling and standard deviation pooling. This integration introduces input-dependent dynamics, thereby enhancing the discriminative power of the resultant feature descriptors. Meanwhile, MCA does not employ a nonlinear dimension reduction strategy to capture global feature interactions but instead designs a simple strategy in the excitation transformation to adaptively determine the coverage of interactions, thereby capturing local feature interactions and achieving a balance between performance and complexity. The principle of the MCA module is illustrated in Figure 10.

# H

# W C Premu tation

# H

# W C Premu tation Identity AvgPool&StdPool Squeeze Transformation 1 ｘ K Conv2d Excitation Transformation

# K Sigmoid Sigmoid Sigmoid

# H

# W C Premut ation

# H

# W C Premut ation Identity Integration H

# W C

# H C W

# C W H

# H W C

# H

# W C

# H W C

# H W C

# H W C 1/3 1/3 1/3 Refine Feature Input Feature **Figure 10.** MCA module schematic diagram. 2.4.4. MPDIoU Loss Function

In the context of automated kiwifruit harvesting, visual interference caused by complex foliage obstruction and dense fruit distribution significantly increases the difficulty of identifying target fruits for harvesting robots. The CIoU loss \[ 32 \], implemented in YOLOv8, enhances geometric robustness through multifaceted optimization of bounding box overlap, centroid displacement, and aspect ratio consistency. However, its algorithm design has two limitations: first, the function involves joint optimization of multiple parameters, resulting in high computational complexity and potentially increased resource consumption by the hardware system; second, it exhibits excessive sensitivity to changes in aspect ratio, which may lead to the model overfitting aspect ratio features during training while weakening its ability to model other critical spatial relationships (such as effective feature extraction under occlusion conditions). These characteristics may impose constraints on convergence efficiency during the model optimization process. To mitigate the aforementioned challenges, this work proposes the MPDIoU loss function, schematically represented in Figure 11. MPDIoU adopts minimum point distance as its bounding box similarity metric, simultaneously streamlining computational complexity while enhancing localization precision. By incorporating point-distance optimization, this formulation effectively resolves optimization convergence failures occurring when predicted and ground-truth bounding boxes exhibit identical aspect ratios notwithstanding significant dimensional discrepancies, thereby improving model robustness in complex environments. Furthermore, MPDIoU reduces computational overhead, facilitating accelerated training convergence. Building upon the CIoU foundation, our method introduces several architectural enhancements that jointly optimize both regression accuracy and training efficiency. For agricultural target recognition applications, MPDIoU more accurately quantifies inter-bounding-box divergences, enabling precise kiwifruit localization. The formulation intrinsically accommodates morphological variations in fruit geometry, consequently enhancing detection robustness and quantitative accuracy. Comparative analysis confirms MPDIoU's superior computational efficiency relative to conventional IoU metrics. 11 of 22 (x 1 prd, y 1 prd ) (x 2 prd, y 2 prd ) (x 1 gt, y 1 gt ) (x 2 gt, y 2 gt ) d1 d2 w h **Figure 11.** MPDIoU schematic diagram.

The calculations for IoU and MPDIoU are as follows:

# IoU = A ∩ B

# A ∪ B ′ (4) *d* 2 $$ 1 = $$  *x* *prd* *−* *x* *gt*  2 +  *y* *prd* *−* *y* *gt*  2 (5) *d* 2 $$ 2 = $$  *x* *prd* *−* *x* *gt*  2 +  *y* *prd* *−* *y* *gt*  2 (6)

*MPDIoU* = * * *IoU* * −* *d* 2 *w* 2 + * h* 2 * * *−* *d* 2 *w* 2 + * h* 2 (7)

In the formula: IoU measures the coincidence degree between two bounding boxes. The numerator represents the intersection area, while the denominator corresponds to the union area; hence, their ratio quantifies the intersection-over-union; * * *x* *prd* and * * *y* *prd*

represent the coordinates of the top-left and bottom-right corners of the predicted box, respectively; * x* *gt* and * y* *gt* represent the coordinates of the top-left and bottom-right corners of the ground truth box, respectively; and the term * d* designates the Euclidean distance between coordinate points.

## 3. Results *3.1.* * * *Experimental Platform*

The experimental operating system is Windows 11, with a 13th Gen Intel ® Core™ i9-13980HX 2.20 GHz processor (Intel, Santa Clara, CA, USA), an NVIDIA GeForce RTX 4060 graphics card (NVIDIA, Santa Clara, CA, USA), and 16 GB of RAM. PyTorch (version 2.0.1+cu118) is used as the framework for developing deep learning models, with Python version 3.10, CUDA version 11.8, and cuDNN version 8.9.5. The model saves the weight file after every 25 training iterations. Table 1 shows the parameter settings for the training strategy. In terms of model configuration, an image size of 640 * ×* 640 pixels is adopted. This size has been widely established as the standard input size in the YOLO series of models, as it achieves a good balance between target detection accuracy and computational efficiency. The learning rate is set to 0.01, combined with the stochastic gradient descent (SGD) optimizer, which is a common configuration in this field. The SGD optimizer 12 of 22

updates the model's weight parameters based on a uniform global learning rate. An initial learning rate of 0.01 has been validated to provide an effective parameter update step size while maintaining high training stability in object detection tasks. Given that object detection tasks typically require a longer training period to fully learn complex feature representations, setting the training period to 300 epochs is generally sufficient for the YOLOv8 model to reach convergence. **Table 1.** Parameter settings. **Parameter Name** **Parameter Value**

Image size 640 \times 640 Batch size Multi-threaded Momentum 0.937 Initial learning rate 0.01 Optimizer SGD Epoches *3.2.* * * *Evaluation Indicators*

This study selected precision (P), recall (R), mean average precision (mAP), frames per second (FPS), model size (Size), algorithm memory usage (Params), and GFLOPs to effectively evaluate the proposed model \[ 33 \]. The corresponding computational formulations are presented below.

# P = *TP* *TP* + * FP* (8)

# R = *TP* *TP* + * FN* (9)

In the formula: TP denote kiwifruit instances correctly identified by the object detection model, FP represents non-kiwifruit objects erroneously classified as kiwifruit, and FN represents undetected kiwifruit instances that the model failed to recognize. mAP = *N* *c* ∑ $$ i=1 $$ *AP* *i* *N* *c* (10)

In the formula: * N* *c* denotes the total number of all objects in the target dataset; mAP@0.5 represents the mean average precision for kiwifruit detection at an IoU threshold of 0.5; while * AP* *i* signifies the average precision for the i-th class, which serves as a comprehensive performance metric encapsulating both precision and recall characteristics.

*3.3.* * * *Attention Mechanism Comparison Experiment*

To comparatively evaluate different attention modules, this study integrated CBAM \[ 34 \], ECA \[ 35 \], SE \[ 36 \], SimAM \[ 37 \], and MCA modules into the YOLOv8 model and conducted detection experiments using the same kiwi dataset on the same server platform. The FPS in the experiment is for statistical verification. Ten consecutive inferences are performed for each model, and the average FPS is calculated. Table 2 shows the detection results of the models. The experimental results show that after introducing different attention modules, the parameter counts (Params) and computational requirements (GFLOPs) of the YOLOv8 model remain stable. Among them, when the MCA mechanism is used in the network structure, the model achieves the best overall performance, with an improvement of 0.3% in accuracy and 0.2% in recall. During image processing, the MCA mechanism effectively combines attention information from channels, width, and 13 of 22

height to enhance the network's expressive capabilities. Through optimization of the fusion and processing workflow for kiwifruit features, the model's fruit recognition capability is enhanced, significantly improving detection accuracy.

**Table 2.** Detection results of different attention mechanism models.

**Modal** **P (%)** **R (%)** **mAP@50 (%)** **Params (M)** **GFLOPs (G)** **FPS (f** *·* **s** *−* **1** **)**

Baseline 92.3 93.4 97.6 30.1 8.2 126.56 CBAM 91.9 93.5 97.4 30.8 8.2 129.45 ECA 91.1 93.4 97.5 30.1 8.2 127.90 SE 87.9 93.1 97.8 30.1 8.2 130.24 SimAM 88.4 93.3 97.9 30.1 8.2 125.30 MCA 92.6 93.6 97.5 30.1 8.2 131.59

*3.4.* * * *Loss Function Comparison Experiment*

To assess MPDIoU's efficacy in kiwifruit detection, a comparative framework incorporating DIoU \[ 38 \], EIoU \[ 39 \], GIoU \[ 40 \], SIoU \[ 41 \], and MPDIoU loss functions was implemented within the Kiwi-YOLO architecture, with rigorous benchmarking conducted under identical experimental conditions. The detection performance of different loss functions is shown in Table 3. Results demonstrate that the MPDIoU loss function yields a statistically significant improvement over the baseline CIoU loss function, achieving a 0.6% increase in precision (P), a 1.5% increase in recall (R), and a 3.42 FPS enhancement in inference speed. The FPS in the experiment is for statistical verification. Ten consecutive inferences are performed for each model, and the average FPS is calculated. Additionally, MPDIoU exhibits superior comprehensive performance across all evaluated metrics, establishing its optimal efficacy for this specific detection task.

**Table 3.** Experimental results comparing loss functions.

**IoU-loss** **P (%)** **R (%)** **mAP@50** **Params (M)** **GFLOPs (G)** **FPS (f** *·* **s** *−* **1** **)**

# CIoU

93.8 93.4 97.7 11.86 5.4 94.28 DIoU 93.6 93.1 97.5 11.86 5.4 93.09 EIoU 94.0 93.5 97.4 11.86 5.4 91.98 GIoU 94.2 93.5 97.4 11.86 5.4 98.21 SIoU 93.9 94.1 97.6 11.86 5.4 95.29 MPDIoU 94.4 94.9 97.7 11.86 5.4 97.70 *3.5.* * * *Ablation Experiment*

This experiment employs YOLOv8 as the baseline model and analyzes incorporated modules through individual integration and combinatorial configurations. The ablation study results are presented in Table 4. Structural replacement of YOLOv8's backbone with MobileViTv1 yields a 3.9 MB reduction in model size concurrently with a 2.8 GFLOP decrease in operations, as quantified in Table 4. The introduction of the BiFPN module yielded a 0.5% improvement in precision (P) and a 0.1% increase in mean Average Precision (mAP). Embedding the MCA mechanism enhanced precision (P) by 0.3% and mAP by 0.1%. The MPDIoU loss function enhanced regression efficiency for kiwifruit targets, elevating precision (P) by 1% and mean average precision (mAP) by 0.2%. When using the MobileViTv1 module and BiFPN module together, not only did the model's accuracy improve, but its size and GFLOPs also decreased significantly, achieving model lightweighting. When using the MobileViTv1, BiFPN, and MCA modules together, the model's accuracy P and average precision mAP improved by 1.5% and 0.3%, respectively. After integrating the four improved modules, the model's overall detection performance reached its best, with the 14 of 22

Kiwi-YOLO model achieving an accuracy P of 94.4% and an average precision of 97.7. The experiments further validated the effectiveness of the four improved modules in enhancing multiple model metrics, successfully reducing the number of parameters, conserving computational resources, and lowering computational time, laying the foundation for deploying this model on kiwifruit harvesting robot object detection devices. **Table 4.** Ablation experiment.

**Baseline** **MobileViT** **BiFPN** **MCA** **MPDIoU** **P (%)** **mAP@50 (%)** **Size (MB)** **GFLOPs (G)** YOLOv8n

\times \times \times \times 92.3 97.4 6.2 8.2 *√* \times \times \times 90.4 97.3 2.7 5.4 \times *√* \times \times 92.8 97.5 6.2 8.2 \times \times *√* \times 92.6 97.5 6.2 8.2 \times \times \times *√* 93.3 97.6 6.2 8.2 *√* *√* \times \times 93.0 97.5 2.7 5.4 *√* *√* *√* \times 93.8 97.7 2.7 5.4 *√* *√* *√* *√* 94.4 97.7 2.7 5.4

*3.6.* * * *Improved Kiwi-YOLO Comparison Experiment*

This study established a controlled evaluation framework to verify Kiwi-YOLO's detection advantage for orchard kiwifruit clusters. Rigorous benchmarking against YOLOv8 was performed with matched environmental covariates and standardized training regimens, ensuring methodological consistency throughout validation. According to the data analysis in Table 5, compared to the YOLOv8 model, the Kiwi-YOLO model achieved performance improvements in kiwifruit recognition: The precision rate P increased by 2.1%, the recall rate R increased by 1.5%, and the mAP increased by 0.3%. Additionally, through model architecture optimization, the Kiwi-YOLO model reduced its parameters (Params) and GFLOPs by 19.71 M and 2.8 G, respectively, while increasing the frames per second (FPS) by 2.73 f *·* s *−* 1. Collectively, these optimizations substantially diminish the model's computational resource and storage requirements while accelerating detection throughput. This enhanced efficiency robustly facilitates high-performance kiwifruit detection within the demanding context of complex orchard settings.

**Table 5.** Comparison of model performance before and after improvement.

**Model** **P (%)** **R (%)** **mAP@50 (%)** **Params (M)** **GFLOPs (G)** **FPS (f** *·* **s** *−* **1** **)**

YOLOv8n 92.3 93.4 97.4 31.57 8.2 83.50 Kiwi-YOLO 94.4 94.9 97.7 11.86 5.4 86.27

As illustrated in Figure 12, Kiwi-YOLO accelerates bounding box regression convergence and reduces post-convergence localization loss more effectively than the original model. Enhanced convergence in recall and mAP curves further validates the improved model's superior detection fidelity for kiwifruit targets. Experimental results confirm Kiwi-YOLO's enhanced stability and superior detection capabilities. Figure 13 compares YOLOv8 and Kiwi-YOLO kiwifruit detection across diverse scenarios, with white bounding boxes indicating missed detections. Both architectures maintain consistent detection efficacy under frontal illumination scenarios and densely clustered target arrangements. However, the YOLOv8 algorithm exhibits missed detections when handling backlit and occluded targets. This is because the standard convolutional kernels in YOLOv8 struggle to adaptively adjust their receptive fields under extreme lighting conditions. Additionally, modules such as SPPE in YOLOv8 tend to overlook local differences in areas with uneven lighting during feature compression, making it difficult for the model 15 of 22

to effectively distinguish fruits from the background in complex orchard environments \[ 42 \]. Benchmarked against YOLOv8, Kiwi-YOLO achieves significant false negative mitigation and enhanced multi-scene detection fidelity. The model's invariant perception of kiwifruit morphologies under unstructured orchard conditions empirically corroborates its enhanced cross-scenario generalizability.

## ( a ) ( **b** )

## ( c ) ( **d** )

**Figure 12.** Model loss function and accuracy change curve: ( **a** ) location loss function; ( **b** ) mAP@50; ( **c** ) precision; ( **d** ) recall.

*3.7.* * * *Comparison of Mainstream Detection Models*

To objectively demonstrate the superiority of the Kiwi-YOLO model, we conducted comparative experiments with Faster R-CNN \[ 43 \], YOLOv5 \[ 44 \], YOLOv6 \[ 45 \], YOLOv7 \[ 46 \], YOLOv8, YOLOv10 \[ 47 \], YOLOv11 \[ 48 \], and YOLOv12 \[ 49 \]. To control variables and ensure comparability of results, all comparative experiments strictly followed the same parameter configurations outlined in Table 1, with the number of training iterations uniformly limited to 300. This standardized process effectively eliminated the interference of training strategy differences, ensuring that performance evaluation results were solely attributable to differences in model architecture. As shown in Table 6, compared to Faster R-CNN, YOLOv5, YOLOv6, YOLOv7, and YOLOv8, the Kiwi-YOLO model achieves a precision rate (P) of 94.4%, second only to YOLOv7, and significantly outperforms Faster 16 of 22

R-CNN, YOLOv5, YOLOv6, and YOLOv8, with improvements of 4.7%, 2.3%, 2.8%, and 2.1%, respectively. In terms of computational complexity, Kiwi-YOLO has a clear advantage, with only 11.86 million parameters (Params) and a computational load (FLOPs) as low as 5.4 G, both of which outperform the other five comparison models. In terms of real-time performance, the model demonstrates outstanding capabilities, achieving a frame rate (FPS) of 86.27 frames per second, representing improvements of 54.91, 28.56, 31.81, 22.29, and 2.77 frames per second compared to Faster R-CNN, YOLOv5, YOLOv6, YOLOv7, and YOLOv8, respectively. Compared to the three new versions of the model-YOLOv10, YOLOv11, and YOLOv12-the Kiwi-YOLO model is slightly inferior in terms of accuracy, but it outperforms the three comparison models in terms of parameter count and computational complexity. Additionally, the Kiwi-YOLO model shows a significant improvement in mAP compared to the other three models. This triad of metrics-detection accuracy, computational efficiency, and inference speed-confirms Kiwi-YOLO's optimal balance, significantly reducing memory footprint and computational overhead to enable practical deployment of fruit detection systems on resource-constrained edge devices.

## Original image

# YOLOv8

## Kiwi YOLOv8

## ( a ) ( **b** ) ( **c** ) ( **d** )

**Figure 13.** Model detection effect: ( **a** ) frontlight; ( **b** ) backlight; ( **c** ) overlapping fruits; ( **d** ) intensive. 17 of 22

**Table 6.** Comparison of different model performance.

**Model** **P (%)** **R (%)** **mAP@50 (%)** **Params (M)** **GFLOPS (G)** **FPS (f** *·* **s** *−* **1** **)**

# Faster R-CNN

89.7 89.62 97.3 136.75 368.3 31.36 YOLOv5 92.1 92.6 97.2 46.14 108.2 57.71 YOLOv6 91.6 92.3 97.0 34.87 85.3 54.46 YOLOV7 95.6 93.3 97.1 37.20 105.1 63.98 YOLOv8n 92.3 94.1 97.4 31.57 8.2 83.50 YOLOv10 95.1 94.7 85.4 27.07 8.4 81.92 YOLOv11 96.0 95.0 89.3 25.82 6.3 87.89 YOLOv12 95.8 94.0 88.0 25.56 6.3 83.60 Kiwi-YOLO 94.4 94.9 97.7 11.86 5.4 86.27

## 4. Discussion

Automated kiwifruit harvesting in unstructured field conditions encounters challenges including lighting variations and fruit occlusion. To rigorously assess the algorithm's robustness and performance efficacy, this study executed validation on a kiwifruit dataset representing diverse fruit states.

*4.1.* * * *Testing Under Different Lighting Conditions*

To quantify illumination robustness in orchard environments, systematic evaluation was conducted using test sets under full-sun and overcast conditions. Quantitative detection metrics across varying illumination scenarios are presented in Table 7. As shown in Table 7, under sunny conditions, the Kiwi-YOLO model achieved a precision rate P of 93.6, an mAP50 of 97.6, and an FPS of 86.88 fps. Under cloudy conditions, the Kiwi-YOLO model achieved a precision rate P of 93.0, an mAP50 of 97.4, and an FPS of 83.96 fps. In summary, although the accuracy rate P, mAP50, and FPS under cloudy conditions are slightly lower than those under sunny conditions, the overall core indicators remain stable and maintain a high accuracy range. The contrastive presentation of kiwifruit in divergent luminous regimes is illustrated in Figure 14. Experimental outcomes confirm the model's capability to accurately identify kiwifruit targets across diverse illumination scenarios, with few missed detections and high accuracy, demonstrating reliable recognition capabilities and good adaptability.

**Table 7.** Detection outcomes across varying illumination.

**Model** **Light** **P (%)** **R (%)** **mAP@50** **FPS (f** *·* **s** *−* **1** **)**

Kiwi-YOLO Sunny 93.6 93.1 97.6 86.88 Overcast 93.0 93.0 97.4 83.96

*4.2.* * * *Detection Under Different Occlusion Conditions*

This research evaluates Kiwi-YOLO's occlusion detection capabilities in kiwifruit orchard environments. Its effectiveness is comprehensively evaluated based on performance in three scenarios: no obstruction, leaf obstruction, and branch obstruction. Table 8 below shows the detection results under different obstruction conditions. The analysis results show that the Kiwi-YOLO model achieves high precision rates (P) of 94.3%, 94.0%, and 93.6% in unobstructed, leaf-obstructed, and branch-obstructed scenarios, respectively, with mAP50 values reaching 97.8%, 97.5%, and 97.4%, respectively. As shown in Figure 15, the model successfully detects all obstructed kiwifruit. The results confirm the model's precision in core feature representation, effective resolution of occlusion-driven information loss, and exceptional stability under partial occlusion scenarios. 18 of 22 ( **a** ) ( **b** ) ( **c** ) ( **d** ) ( **e** ) ( **f** )

**Figure 14.** Detection results under different lighting conditions: ( **a** - **c** ) sunny; ( **d** - **f** ) overcast.

**Table 8.** Detection results under varying occlusion conditions.

**Model** **Type** **P (%)** **R (%)** **mAP@50 (%)** **FPS (f** *·* **s** *−* **1** **)**

Kiwi-YOLO Unobstructed 94.3 95.0 97.8 88.66 Leaves occlusion 94.0 94.6 97.5 87.57 Stem occlusion 93.6 93.7 97.4 85.90

** ** ** ** ( **a** ) ** ** ( **b** ) ** ** ( **c** ) ** **

** ** ** ** ** ** ( **d** ) ( **e** ) ( **f** )

**Figure 15.** Detection results under different occlusion conditions: ( **a**, **b** ) unobstructed; ( **c**, **d** ) leaves occlusion; ( **e**, **f** ) stem occlusion. 19 of 22

## 5. Conclusions

To overcome the challenges of limited adaptability and high computational demands in kiwifruit detection models operating in natural environments, this research enhances the YOLOv8 framework and introduces the Kiwi-YOLO model, attaining an optimal balance between inference efficiency and recognition precision. Firstly, the MobileViTv1 model is used to replace the backbone network, effectively reducing its parameter count and computational load. Secondly, the BiFPN is integrated into the neck of the base model, replacing the original PANet, thereby enhancing the model's ability to distinguish between backgrounds and obstacles. Additionally, the MPDIoU loss function is utilized to minimize inter-vertex distances of bounding boxes, mitigating detection distortion induced by sample heterogeneity, which accelerates convergence and enhances localization precision. Furthermore, the MCA module is instituted to augment the model's robustness and generalization capabilities. Kiwi-YOLO demonstrates outstanding performance in complex environments for kiwifruit recognition, achieving precision (P), recall (R), and mean average precision (mAP) of 94.4%, 98.9%, and 97.7%, respectively. On the kiwifruit dataset in an orchard environment, Kiwi-YOLO demonstrates the best overall performance compared to mainstream models and significantly reduces the false negative rate. Compared to the baseline model YOLOv8, its parameter count and floating-point operations (FLOPs) are reduced by 19.71 M and 2.8 G, respectively, while the inference speed (FPS) is improved by 2.73 f *·* s *−* 1, enhancing its compatibility with resource-constrained mobile platforms. Additionally, in experiments involving complex scene instance recognition with varying lighting conditions and occlusions, Kiwi-YOLO attains superior detection accuracy with enhanced environmental robustness, enabling reliable visual perception for automated kiwifruit harvesting in occlusion-intensive orchards. Despite its strong performance in detecting kiwifruit under complex conditions, the Kiwi-YODO model's generalization capability still requires further enhancement. First, the current training dataset primarily includes images of kiwifruit at the mature stage (with yellowish-brown or brownish-brown skin), lacking samples of unripe kiwifruit (dark green). This lack of sample diversity may limit the model's performance in identifying kiwifruit of different colors and maturity levels. Second, the dataset in this study is primarily based on red-fleshed kiwifruit and was collected from dwarf-cultivated orchards. This variety accounts for a significant proportion of local cultivation areas and is the most representative type in commercial production. Prioritizing its detection issues can directly address industrial needs. In the early stages of this study, the focus was on addressing general environmental disturbances such as "lighting and obstruction," so the variables related to variety and cultivation mode were temporarily simplified. Additionally, due to research progress issues and the lack of relevant technology, this study did not address issues such as target tracking. Finally, this study focuses on addressing the unique challenges of kiwifruit harvesting, with all experimental designs and parameter optimizations tailored to kiwifruit characteristics. Therefore, the recognition algorithms developed in this study cannot currently be applied to other fruits. Future improvement plans include prioritizing the collection and incorporation of kiwifruit images spanning different growth stages, including the unripe stage, to build a more diverse dataset, simultaneously exploring the expansion of data on other kiwifruit varieties and different cultivation modes (such as trellis systems), and conducting cross-variety and cross-mode generalization capability testing and optimization. Additionally, when technical conditions mature, the study will explore extended functions such as target tracking to enhance the model's generalization performance and practical adaptability in detecting kiwifruit across different growth stages. 20 of 22

**Author Contributions:** Conceptualization, J.Z. and F.S.; methodology, J.Z. and F.S.; software, J.Z.; validation, B.Z. and H.W.; formal analysis, X.L.; investigation, Q.L. and F.F.; resources, X.L.; data curation, J.Z.; writing-original draft preparation, J.Z.; writing-review and editing, J.Z., Q.L. and H.W.; funding acquisition, F.S. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by the Sichuan Provincial Department of Science and Technology under grant number 2024YFHZ0147.

**Data Availability Statement:** The dataset supporting this research is available within the article. Data access requests should be addressed to the corresponding author.

**Conflicts of Interest:** The authors declare no conflicts of interest.

## References

1. Fu, M.; Guo, S.; Chen, A.; Cheng, R.; Cui, X. Design and experimentation of multi-fruit envelope-cutting kiwifruit picking robot. *Front.* * * *Plant Sci.* ** ** **2024**, * 15*, 1338050. \[ CrossRef \] 2. Wang, F.; Lv, C.; Pan, Y.; Zhou, L.; Zhao, B. Efficient Non-Destructive Detection for External Defects of Kiwifruit. * * *Appl.* * * *Sci.* ** ** **2023**, *13*, 11971. \[ CrossRef \] 3. Wang, X.; Hao, W.; Zhang, J.; He, Z.; Ding, X.; Cui, Y. Development and evaluation of a soft end effector for kiwifruit harvesting. *N. Z. J. Crop Hortic.* * * *Sci.* ** ** **2025**, 1-29. \[ CrossRef \] 4. Li, L.; Li, K.; He, Z.; Li, H.; Cui, Y. Kiwifruit segmentation and identification of picking point on its stem in orchards. * * *Comput.* *Electron.* * * *Agric.* ** ** **2025**, * 229*, 109748. \[ CrossRef \] 5. Liu, Y.; Hao, J.; Yang, P.; Li, Z.; Tchuenbou-Magaia, F.; Tang, W. Development of a novel packaging box with on-demand ripening function for fast kiwifruit logistics. * * *Postharvest Biol.* * * *Technol.* ** ** **2025**, * 227*, 113595. \[ CrossRef \] 6. Lu, G.; Ge, X.; Zhong, T.; Hu, Q.; Geng, J. Preprocessing enhanced image compression for machine vision. * * *IEEE Trans.* * * *Circuits* *Syst.* * * *Video Technol.* ** ** **2024**, * 34*, 13556-13568. \[ CrossRef \] 7. Wang, D.; Wang, J.; Shi, Y.; Yin, B.; Ling, N. Collaborative point cloud geometry compression for both human vision and machine vision. * * *Multimed.* * * *Syst.* ** ** **2025**, * 31*, 255. \[ CrossRef \] 8. Wang, S.; Wang, Z.; Wang, S.; Ye, Y. Deep image compression toward machine vision: A unified optimization framework. * * *IEEE* *Trans.* * * *Circuits Syst.* * * *Video Technol.* ** ** **2022**, * 33*, 2979-2989. \[ CrossRef \] 9. Bao, R.; Zhang, W.; Guo, R. Spectral calculation model for machine vision image enhancement. * * *Opt.* * * *Laser Technol.* ** ** **2025**, * 181*, 111806. \[ CrossRef \] 10. Wu, H.; Luo, Z.; Sun, F.; Li, X.; Zhao, Y. An improvement method for improving the surface defect detection of industrial products based on contour matching algorithms. * * *Sensors* ** 2024**, * 24*, 3932. \[ CrossRef \] 11. Kuan, Y.; Goh, K.; Lim, L. Systematic review on machine learning and computer vision in precision agriculture: Applications, trends, and emerging techniques. * * *Eng.* * * *Appl.* * * *Artif.* * * *Intell.* ** ** **2025**, * 148*, 110401. \[ CrossRef \] 12. Bayoudh, K. A survey of multimodal hybrid deep learning for computer vision: Architectures, applications, trends, and challenges. *Inf.* * * *Fusion* ** 2024**, * 105*, 102217. \[ CrossRef \] 13. Zhao, X.; Wang, L.; Zhang, Y.; Han, X.; Deveci, M.; Parmar, M. A review of convolutional neural networks in computer vision. *Artif.* * * *Intell.* * * *Rev.* ** ** **2024**, * 57*, 99. \[ CrossRef \] 14. Liu, W.; Prasad, S.; Crawford, M. Investigation of hierarchical spectral vision transformer architecture for classification of hyperspectral imagery. * * *IEEE Trans.* * * *Geosci.* * * *Remote Sens.* ** ** **2024**, * 62*, 1-19. \[ CrossRef \] 15. Kang, S.; Hu, Z.; Liu, L.; Zhang, K.; Cao, Z. Object detection YOLO algorithms and their industrial applications: Overview and comparative analysis. * * *Electronics* ** 2025**, * 14*, 1104. \[ CrossRef \] 16. Sapkota, R.; Ahmed, D.; Karkee, M. Comparing YOLOv8 and Mask R-CNN for instance segmentation in complex orchard environments. * * *Artif.* * * *Intell.* * * *Agric.* ** ** **2024**, * 13*, 84-99. \[ CrossRef \] 17. Dai, J.-S.; He, Z.-Q. Real-Time Recognition and Localization of Kiwifruit Based on Improved YOLOv5s Algorithm. * * *IEEE Access* **2024**, * 12*, 156261-156272. \[ CrossRef \] 18. Liu, Q.; Meng, H.; Zhao, R.; Ma, X.; Zhang, T.; Jia, W. Green apple detector based on optimized deformable detection transformer. *Agriculture* ** 2024**, * 15*, 75. \[ CrossRef \] 19. Jia, W.; Tian, Y.; Luo, R.; Zhang, Z.; Lian, J.; Zheng, Y. Detection and segmentation of overlapped fruits based on optimized mask R-CNN application in apple harvesting robot. * * *Comput.* * * *Electron.* * * *Agric.* ** ** **2020**, * 172*, 105380. \[ CrossRef \] 20. Xie, J.; Peng, J.; Wang, J.; Chen, B.; Jing, T.; Sun, D.; Gao, P.; Wang, W.; Lu, J.; Yetan, R. Litchi detection in a complex natural environment using the YOLOv5-litchi model. * * *Agronomy* ** 2022**, * 12*, 3054. \[ CrossRef \] 21. Li, C.; Wu, H.; Zhang, T.; Lu, J.; Li, J. Lightweight network of multi-stage strawberry detection based on improved YOLOv7-Tiny. *Agriculture* ** 2024**, * 14*, 1132. \[ CrossRef \] 21 of 22

22. Sun, F.; Lv, Q.; Bian, Y.; He, R.; Lv, D.; Gao, L.; Wu, H.; Li, X. Grape Target Detection Method in Orchard Environment Based on Improved YOLOv7. * * *Agronomy* ** 2025**, * 15*, 42. \[ CrossRef \] 23. Li, S.; Tao, T.; Zhang, Y.; Li, M.; Qu, H. YOLO v7-CS: A YOLO v7-based model for lightweight bayberry target detection count. *Agronomy* ** 2023**, * 13*, 2952. \[ CrossRef \] 24. Lv, Q.; Sun, F.; Bian, Y.; Wu, H.; Li, X.; Li, X.; Zhou, J. A Lightweight Citrus Object Detection Method in Complex Environments. *Agriculture* ** 2025**, * 15*, 1046. \[ CrossRef \] 25. Shan, W. * Kiwifruit Detection, Mendeley Data*; Version 1; Huaibei Normal University: Huaibei, China, 2024. \[ CrossRef \] 26. Jia, Z.; Zhang, M.; Yuan, C.; Liu, Q.; Liu, H.; Qiu, X.; Zhao, W.; Shi, J. ADL-YOLOv8: A field crop weed detection model based on improved YOLOv8. * * *Agronomy* ** 2024**, * 14*, 2355. \[ CrossRef \] 27. Cheng, S.; Wang, Z.; Liu, S.; Han, Y.; Sun, P.; Li, J. Attention-Based Lightweight YOLOv8 Underwater Target Recognition Algorithm. * * *Sensors* ** 2024**, * 24*, 7640. \[ CrossRef \] 28. Suman, M.; Arulanantham, G. Efficient differentiation of biodegradable and non-biodegradable municipal waste using a novel MobileYOLO algorithm. * * *Trait.* * * *Du Signal* ** 2023**, * 40*, 1833. \[ CrossRef \] 29. Yu, H.; Wang, J.; Han, Y.; Fan, B.; Zhang, C. Research on an intelligent identification method for wind turbine blade damage based on CBAM-BiFPN-YOLOV8. * * *Processes* ** 2024**, * 12*, 205. \[ CrossRef \] 30. Tan, W.; Bao, Y.; Meng, F.; Li, C.; Liang, Y. Adaptive cross-channel transformation based on self-modulation for learned image compression. * * *Signal Process.* * * *Image Commun.* ** ** **2025**, * 138*, 117325. \[ CrossRef \] 31. Yang, H.; Yang, L.; Wu, T.; Yuan, Y.; Li, J.; Li, P. MFD-YOLO: A fast and lightweight model for strawberry growth state detection. *Comput.* * * *Electron.* * * *Agric.* ** ** **2025**, * 234*, 110177. \[ CrossRef \] 32. Li, Y.; Li, S.; Du, H.; Chen, L.; Zhang, D.; Li, Y. YOLO-ACN: Focusing on small target and occluded object detection. * * *IEEE Access* **2020**, * 8*, 227288-227303. \[ CrossRef \] 33. Ye, R.; Shao, G.; He, Y.; Gao, Q.; Li, T. YOLOv8-RMDA: Lightweight YOLOv8 network for early detection of small target diseases in tea. * * *Sensors* ** 2024**, * 24*, 2896. \[ CrossRef \] 34. Wang, N.; Zhang, Z.; Hu, H.; Li, B.; Lei, J. Underground defects detection based on GPR by fusing simple linear iterative clustering phash (SLIC-Phash) and convolutional block attention module (CBAM)-YOLOv8. * * *IEEE Access* ** 2024**, * 12*, 25888-25905. \[ CrossRef \] 35. Li, Y.; Wang, Z.; Yang, A.; Yu, X. Integrating evolutionary algorithms and enhanced-YOLOv8+ for comprehensive apple ripeness prediction. * * *Sci.* * * *Rep.* ** ** **2025**, * 15*, 7307. \[ CrossRef \] \[ PubMed \] 36. Wu, T.; Dong, Y. YOLO-SE: Improved YOLOv8 for remote sensing object detection and recognition. * * *Appl.* * * *Sci.* ** ** **2023**, * * *13*, 12977. \[ CrossRef \] 37. Cheng, Z.; Du, X.; Liu, Q.; Zhan, S.; Yu, B.; Wang, H.; Zhu, X.; Xu, C. Object detection in autonomous driving scenario using YOLOv8-SimAM: A robust test in different datasets. * * *Transp.* * * *A Transp.* * * *Sci.* ** ** **2025**, 1-22. \[ CrossRef \] 38. Jinbo, G.; Shenghuai, W.; Xiaohui, C.; Chen, W.; Wei, Z. QL-YOLOv8s: Precisely optimized lightweight YOLOv8 pavement disease detection model. * * *IEEE Access* ** 2024**, * 12*, 128392-128403. \[ CrossRef \] 39. Zhou, H.; Yu, Y.; Wang, K.; Hu, Y. A YOLOv8-based approach for real-time lithium-ion battery electrode defect detection with high accuracy. * * *Electronics* ** 2023**, * 13*, 173. \[ CrossRef \] 40. Nie, L.; Li, B.; Jiao, F.; Lu, W.; Shi, X.; Song, X.; Shi, Z.; Yang, T.; Du, Y.; Liu, Z. EVIT-YOLOv8: Construction and research on African Swine Fever facial expression recognition. * * *Comput.* * * *Electron.* * * *Agric.* ** ** **2024**, * 227*, 109575. \[ CrossRef \] 41. Ma, S.; Zhao, X.; Wan, L.; Zhang, Y.; Gao, H. A lightweight algorithm for steel surface defect detection using improved YOLOv8. *Sci.* * * *Rep.* ** ** **2025**, * 15*, 8966. \[ CrossRef \] 42. He, L.; Wu, D.; Zheng, X.; Xu, F.; Lin, S.; Wang, S.; Ni, F.; Zheng, F. RLK-YOLOv8: Multi-stage detection of strawberry fruits throughout the full growth cycle in greenhouses based on large kernel convolutions and improved YOLOv8. * * *Front.* * * *Plant Sci.* **2025**, * 16*, 1552553. \[ CrossRef \] 43. Sun, Y.; Liu, Q. Attribute recognition from clothing using a Faster R-CNN based multitask network. * * *Int.* * * *J. Wavelets Multiresolut.* *Inf.* * * *Process.* ** ** **2018**, * 16*, 1840009. \[ CrossRef \] 44. Zhang, L.; Li, J.; Zhang, F. An efficient forest fire target detection model based on improved YOLOv5. * * *Fire* ** 2023**, * 6*, 291. \[ CrossRef \] 45. Norkobil Saydirasulovich, S.; Abdusalomov, A.; Jamil, M.K.; Nasimov, R.; Kozhamzharova, D.; Cho, Y.-I. A YOLOv6-based improved fire detection approach for smart city environments. * * *Sensors* ** 2023**, * 23*, 3161. \[ CrossRef \] 46. Zhao, L.; Zhu, M. MS-YOLOv7: YOLOv7 based on multi-scale for object detection on UAV aerial photography. * * *Drones* ** 2023**, *7*, 188. \[ CrossRef \] 47. Saha, U.; Saha, B.; Imran, M.A. A weather-adaptive convolutional neural network framework for better license plate detection. *Sensors* ** 2024**, * 24*, 7841. \[ CrossRef \] 22 of 22

48. Huang, Z.; Lee, W.S.; Yang, P.; Ampatzidis, Y.; Shinsuke, A.; Peres, N.A. Advanced canopy size estimation in strawberry production: A machine learning approach using YOLOv11 and SAM. * Comput.* * * *Electron.* * * *Agric.* ** ** **2025**, * 236*, 110501. \[ CrossRef \] 49. Sapkota, R.; Flores-Calero, M.; Qureshi, R.; Badgujar, C.; Nepal, U.; Poulose, A.; Zeno, P.; Vaddevolu, U.B.P.; Khan, S.; Shoman, M. YOLO advances to its genesis: A decadal and comprehensive review of the You Only Look Once (YOLO) series. * * *Artif.* * * *Intell.* * * *Rev.* **2025**, * 58*, 274. \[ CrossRef \]

**Disclaimer/Publisher's** ** ** **Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.