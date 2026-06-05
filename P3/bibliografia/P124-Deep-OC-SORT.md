# DEEP OC-SORT: MULTI-PEDESTRIAN TRACKING BY ADAPTIVE RE-IDENTIFICATION

*Gerard Maggiolino* * * *∗* *, Adnan Ahmad* * * *∗* *, Jinkun Cao, Kris Kitani*

## Carnegie Mellon University

# ABSTRACT

Motion-based association for Multi-Object Tracking (MOT) has recently re-achieved prominence with the rise of powerful object detectors. Despite this, little work has been done to incorporate appearance cues beyond simple heuristic models that lack robustness to feature degradation. In this paper, we propose a novel way to leverage objects' appearances to adaptively integrate appearance matching into existing high-performance motion-based methods. Building upon the pure motion-based method OC-SORT, we achieve ** ** **1st** ** ** **place** **on** ** ** **MOT20** and ** ** **2nd** ** ** **place** ** ** **on** ** ** **MOT17** with 63.9 and 64.9 HOTA, respectively. We also achieve 61.3 HOTA on the challenging DanceTrack benchmark as a new state-of-theart even compared to more heavily-designed methods. The code and models are available at <https://github.com/> GerardMaggiolino/Deep-OC-SORT.

***Index Terms*** **-** multi-object tracking; Kalman ﬁlter

# 1. INTRODUCTION

With the success of advanced object detectors and motionbased association algorithms \[1, 2, 3\], the effective integration of visual appearance with motion-based matching remains relatively under-explored beyond simple moving average models \[3, 4\]. In this work, we start from a recent pure motion-based tracking algorithm OC-SORT \[2\] and improve the tracking robustness by incorporating visual appearance with a novel approach. Bounding box-level visual features from strong embedding models still contain signiﬁcant noise due to occlusion, motion blur, or objects of similar appearance. We propose a dynamic and adaptive heuristic-based model to incorporate the visual appearance with motionbased cues in a single stage for object association. Without ﬁne-grained semantics, such as instance segmentation, we improve the accuracy of using visual comparison among objects for association. In addition to the contribution of more effectively adding appearance cues to motion-based object association, we integrate camera motion compensation, boosting performance by complementing the object-centric motion model. Our method provides a new and effective baseline model for future works. It sets a new state-of-the-art among all published works on MOT17 \[5\], MOT20 \[6\], and \*: indicates equal contribution

DanceTrack \[7\] benchmarks. As our focus is to introduce visual appearance to OC-SORT, we name our method Deep OC-SORT. We note that the adaptive way we incorporate visual appearance with the motion-based method is newly designed, instead of a straightforward adaptation of what DeepSORT \[8\] does upon SORT \[9\].

**2.** ** ** **RELATED WORKS** **Motion-based** ** ** **Multi-Object** ** ** **Tracking.** Given the rapid improvement of object detectors, many modern end-toend MOT models still underperform against classic motion model-based tracking algorithms. The Kalman ﬁlter \[10\] is the foundation of the most famous line of tracking-bydetection methods. Among this line of work, SORT \[9\] uses a linear motion assumption to associate tracks by IoU. ByteTrack \[1\] is recently proposed to ﬁx missing predictions by using low-conﬁdence candidates in association, achieving good performance by balancing the detection quality and tracking conﬁdence. More recently, OC-SORT \[2\] improves the robustness of tracking in non-linear motion scenarios and relieves the inﬂuence from object occlusion or disappearance by more heavily relying on detections directly. **Appearance-based** ** ** **Multi-Object** ** ** **Tracking.** Visual identiﬁcation is a straightforward cue to associate targets over time. DeepSORT \[8\] is one of the earliest to use deep visual features for object association. Since then more methods \[11, 12, 13\] have improved upon integrating visual information by training discriminative appearance models in an endto-end manner. More recently, the rise of transformers \[14\] has started another wave of using appearance for multi-object tracking, where the task of object association is modeled as a query matching problem \[15, 16, 17, 13\]. However, appearance-based methods are observed to be less effective when the objects of interest have similar appearance \[7\] or are occluded \[6, 7\]. Despite having more complicated architectures, these methods fail to outperform simple motion association algorithms that leverage strong detectors. Some recent attempts to add appearance cues \[3, 4\] to motionbased methods use simple moving averages for appearance embedding updates, achieving moderate success.

# 3. METHODS

In this section, we describe the three modules of Deep OCSORT: Camera Motion Compensation (CMC), Dynamic Ap-

# arXiv:2302.11813v1 \[cs.CV\] 23 Feb 2023

pearance (DA) and Adaptive Weighting (AW). The algorithm pipeline is illustrated in Figure 1.

**3.1.** ** ** **Preliminary:** ** ** **OC-SORT**

Our work is built upon the recent Kalman-ﬁlter-based tracking algorithm OC-SORT \[2\], which is an extension of SORT \[9\]. SORT relies on the linear motion assumption of object tracking and leverages the Kalman ﬁlter to associate predictions from an object detector with the position estimates from the motion model by IoU. When the video frame rate is high, the linear motion assumption can be effective for object displacement on adjacent video frames. However, when tracking targets disappear under occlusion, the missed measurements during Kalman ﬁlter updates compound error quadratically over time in the Kalman ﬁlter's parameters. OC-SORT proposes three modules to help resolve the motionmodel based error: OCM (observation-centric momentum), OCR (observation-centric recovery), and OOS (observationcentric online smoothing). We invite the reader to refer to its paper \[2\] for details. We inherit the overall pipeline of OC-SORT, including the Hungarian algorithm to associate matches from a cost matrix. **Fig. 1:** Illustration of Deep OC-SORT.

**3.2.** ** ** **Camera Motion Compensation (CMC)**

As OC-SORT is highly dependent on the detection quality, we introduce CMC to more accurately localize objects from frame to frame in moving scenes. Given a scaled rotation matrix * M* *t* = * s* *t* *R* *t* and a translation * T* *t* where * M* *t* * * *∈* R 2 *×* 2 and *T* *t* * * *∈* R 2 *×* 1, we apply them to OC-SORT's three components respectively:

1. ** ** **OOS** ** ** **+** ** ** **CMC.** The Kalman ﬁlter is updated from the linearly interpolated path, starting at the last known measurement. This last known measurement is comprised of \[ *x* *c* *, y* *c* *, a, s* \], with the ﬁrst two entries as the center of the bounding box. The center of the bounding box is similarly transformed by * * *c* * * *←* *M* *t* *c* + * * *T* *t*, so that the path is interpolated starting from the camera corrected measurement.

2. ** ** **OCM + CMC.** Let * p* 1 *, p* 2 be the upper-left and lowerright corner points of a bounding box. OCM uses the last ∆ *t* = 3 bounding boxes to compute a bounding box angular velocity. At each timestep * t*, we apply the

transformation * * *p* *i* * * *←* *M* *t* *p* *i* + * T* *t* to the bounding box. This goes from * t* * −* ∆ *t* to timestep * t* during OCM.

3. ** ** **OCR + CMC.** For the last-seen bounding box position in OCR, at each timestep * t*, we apply * p* *i* * * *←* *M* *t* *p* *i* + * T* *t* to adjust its position under CMC.

For OC-SORT, the Kalman state is ** x** = \[ *x* *c* *, y* *c* *, a, s,* ˙ *x* *c* *,* ˙ *y* *c* *,* ˙ *a* \]. We apply CMC to correct the Kalman state:           

**x** \[0: 2\] * ←* *M* *t* **x** \[0: 2\] + * T* *t* *,*

**x** \[4: 6\] * ←* *M* *t* **x** \[4: 6\] *,*

# P \[0: 2, 0: 2\] ← M t P \[0: 2, 0: 2\] M T *t* * * *,*

# P \[4: 6, 4: 6\] ← M t P \[4: 6, 4: 6\] M T *t* * * *.* (1)

We note that we could apply the * scale* of the CMC transform to the area * a*, or approximate rotation to change the aspect ratio * s*. However, in contrast to the center point, the enclosing bounding box of a rotated object is not approximated linearly and requires a ﬁne-grained mask of the enclosed object. While the approximation works well with OCM and OCR, the Kalman ﬁlter is empirically more sensitive to approximate changes. We apply this CMC update before the Kalman extrapolation step so that the * prediction* stage is from the CMC-corrected states. **3.3.** ** ** **Dynamic Appearance**

In previous work \[3, 4\], the deep visual embedding used to describe a tracklet is given by an Exponential Moving Average (EMA) of the deep detection embeddings frame by frame. This requires a weighting factor * * *α* to adjust the ratio of the visual embedding from historical and current time steps. We propose to modify the * α* of the EMA on a per-frame basis, depending on the detector conﬁdence. This ﬂexible * α* allows selectively incorporating appearance information into a track's model only in high-quality situations. We use low detector conﬁdence as a proxy to recognize image degradation due to occlusion or blur, allowing us to reject corrupted embeddings. Let ** e** *t* be the tracklet's appearance embedding at time * t*. The standard EMA is

$$ et = \alphaet−1 + (1 −\alpha)enew, $$ (2) where ** e** new is the appearance of the matched detection being added to the model. We propose replacing * α* with a changing *α* *t* deﬁned as $$ \alphat = \alphaf + (1 −\alphaf)(1 −sdet −\sigma $$ 1 −\sigma ), (3)

where * s* det is the detector conﬁdence, and * σ* is a detection conﬁdence threshold to ﬁlter noisy detections, a common practice of previous works \[9, 2, 1, 4\]. We set the ﬁxed value *α* *f* = 0 *.* 95. The detector prediction provides * s* det, controlling the dynamic operation. With * * *s* det = * * *σ*, we have * * *α* *t* = 1, so that the new appearance embedding is totally ignored. In contrast, * s* det = 1 implies * α* *t* = * α* *f*, and ** e** new is maximally added to the update of tracklet visual embedding. The value scales linearly with detector conﬁdence. The operation to generate

## Table 1: Results on MOT17-test and MOT20-test. Methods in the blue blocks share the same detections.

# MOT17

Tracker HOTA *↑* MOTA *↑* IDF1 *↑* FP( 10 4 ) *↓* FN( 10 4 ) *↓* IDs *↓* Frag *↓* AssA *↑* AssR *↑*

FairMOT \[11\] 59.3 73.7 72.3 2.75 11.7 3,303 8,073 58.0 63.6 TransCt \[18\] 54.5 73.2 62.2 2.31 12.4 4,614 9,519 49.7 54.2 TransTrk \[16\] 54.1 75.2 63.5 5.02 8.64 3,603 4,872 47.9 57.1 GRTU \[19\] 62.0 74.9 75.0 3.20 10.8 1,812 **1,824** 62.1 65.8 QDTrack \[12\] 53.9 68.7 66.3 2.66 14.66 3,378 8,091 52.7 57.2 MOTR \[15\] 57.2 71.9 68.4 2.11 13.6 2,115 3,897 55.8 59.2 TransMOT \[20\] 61.7 76.7 75.1 3.62 9.32 2,346 7,719 59.9 66.5

ByteTrack \[1\] 63.1 **80.3** 77.3 2.55 **8.37** 2,196 2,277 62.0 68.2 OC-SORT \[2\] 63.2 78.0 77.5 **1.51** 10.8 1,950 2,040 63.2 67.5 StrongSORT \[4\] 63.5 78.3 78.5 - - 1,446 - - 63.7 - - \*StrongSORT++ \[4\] 64.4 79.6 79.5 2.79 8.62 1,194 **1,866** 64.4 **71.0** Deep OC-SORT **64.9** 79.4 **80.6** 1.66 9.88 **1,023** 2,196 **65.9** 70.1

# MOT20

Tracker HOTA *↑* MOTA *↑* IDF1 *↑* FP( 10 4 ) *↓* FN( 10 4 ) *↓* IDs *↓* Frag *↓* AssA *↑* AssR *↑*

FairMOT \[11\] 54.6 61.8 67.3 10.3 8.89 5,243 7,874 54.7 60.7 Semi-TCL \[21\] 55.3 65.2 70.1 6.12 11.5 4,139 8,508 56.3 60.9 CSTrack \[22\] 54.0 66.6 68.6 2.54 14.4 3,196 7,632 54.0 57.6 GSDT \[23\] 53.6 67.1 67.5 3.19 13.5 3,131 9,875 52.7 58.5 TransMOT \[20\] 61.9 77.5 75.2 3.42 **8.08** 1,615 2,421 60.1 66.3

ByteTrack \[1\] 61.3 **77.8** 75.2 2.62 8.76 1,223 1,460 59.6 66.2 OC-SORT \[2\] 62.1 75.5 75.9 1.80 10.8 1,198 62.0 67.5 StrongSORT \[4\] 61.5 72.2 75.9 - - 1,066 - - 63.2 \*StrongSORT++ \[4\] 62.6 73.8 77.0 **1.66** 11.8 **1,003** 64.0 69.6 Deep OC-SORT **63.9** 75.6 **79.2** 1.69 10.8 1,536 **65.7** **70.8**

\*: StrongSORT++ requires ofﬂine post-processing while ByteTrack, OC-SORT, StrongSORT and Deep OC-SORT are for online multi-object tracking.

## Table 2: Results on DanceTrack test set. Methods in the blue block use the same detections.

Tracker HOTA *↑* DetA *↑* AssA *↑* MOTA *↑* IDF1 *↑*

CenterTrack \[24\] 41.8 78.1 22.6 86.8 35.7 FairMOT \[11\] 39.7 66.7 23.8 82.2 40.8 QDTrack \[12\] 45.7 72.1 29.2 83.0 44.8 TransTrk\[16\] 45.5 75.9 27.5 88.4 45.2 TraDes \[25\] 43.3 74.5 25.4 86.2 41.2 MOTR \[15\] 54.2 73.5 40.2 79.7 51.5

SORT \[9\] 47.9 72.0 31.2 91.8 50.8 DeepSORT \[8\] 45.6 71.0 29.7 87.8 47.9 ByteTrack \[1\] 47.3 71.6 31.4 89.5 52.5 OC-SORT \[2\] 55.1 80.3 38.3 92.0 54.6 \*StrongSORT++ \[4\] 55.6 80.7 38.6 91.1 55.2 Deep OC-SORT **61.3** **82.2** **45.8** **92.3** **61.5**

\*: StrongSORT++ requires ofﬂine post-processing while others are for online tracking.

## the dynamic appearance introduces no new hyper-parameters to the standard EMA.

## 3.4. Adaptive Weighting

## Our Adaptive Weighting increases the weight of appearance

features depending on the discriminativeness of appearance embeddings. Using standard cosine similarity across track and box embeddings results in an * * *M* * * *×* * * *N* appearance cost matrix, * A* *c* where * M* and * N* are the numbers of tracks and detections respectively. * A* *c* \[ *m, n* \] indicates the entry at the intersection of the * m* -th row and the * n* -th column. This is typically combined with the IoU cost matrix * I* *c* as * C* = * I* *c* + *a* *w* *A* *c*, with a linear sum assignment minimizing cost over * −* *C*. We propose to boost individual track-box scores based on discriminativeness, adding * w* *b* ( *m, n* ) to the global * a* *w*. Let * τ* *m*

## represent a track and d n represent a detection. When τ m has

a high similarity score to only one box (included in the row *A* *c* \[ *m,*:\] ), we increase appearance weight over row * A* *c* \[ *m,*:\]. The same operation is applied to the columns of * * *A* *c* if a detection * d* *n* is associated discriminatively with only one track. We use * * *z* diff to measure the discriminativeness of box-track pairs, which is deﬁned as the difference between the highest and second-highest values at a row or a column: *z* det diff ( *A* *c* *, n* ) = min (max *i* *A* *c* \[ *i, n* \] * −* max j̸=i Ac[j, n], ϵ),

## z track

diff ( *A* *c* *, m* ) = min (max *i* *A* *c* \[ *m, i* \] * −* max j̸=i Ac[m, j], ϵ), (4)

## where ϵ is a hyper-parameter to cap the boost where there's

a large difference in appearance cost between the ﬁrst and second best matches. Then, we derive the weighting factor as wb(m, n) =  *z* track diff ( *A* *c* *, m* ) + * z* det diff ( *A* *c* *, n* )  */* 2 *,* (5)

## which results in the ﬁnal cost matrix C as

C[m, n] = IoU[m, n] + [aw + wb(m, n)] Ac[m, n]. (6)

## We choose to measure the discriminativeness based on only

the ﬁrst and second-highest scores rather than probability distribution metrics like KL divergence, as the spread of values between lower-scoring matches are irrelevant. A true positive appearance match is indicated by one high score having a large distance from the next best match.

# 4. EXPERIMENTS

## In this section, we provide experimental evidence to demon

strate the effectiveness of Deep SORT. We also analyze the

**Table 3:** Ablation study on MOT17-val, MOT20-val and DanceTrack-val set. MOT17-val MOT20-val DanceTrack-val

# Appr.

DA CMC AW HOTA *↑* AssA *↑* IDF1 *↑* HOTA *↑* AssA *↑* IDF1 *↑* HOTA *↑* AssA *↑* IDF1 *↑*

68.13 70.06 79.52 58.35 56.11 74.77 53.07 35.93 52.43 ✓ 69.66 72.72 82.44 58.33 56.12 74.63 53.57 36.68 53.30 ✓ 68.59 70.63 80.18 59.10 57.47 75.71 58.03 42.37 57.73 ✓ ✓ 68.65 70.85 80.45 59.16 57.60 75.87 58.36 43.00 58.17 ✓ ✓ ✓ 69.80 72.86 82.56 59.35 58.00 76.11 58.46 43.33 58.83 ✓ ✓ ✓ ✓ **70.20** **73.46** **82.78** **59.45** **58.16** **76.30** **58.53** **43.41** **59.06**

inﬂuence of each module we introduce over OC-SORT \[2\]. **Datasets** ** ** **and** ** ** **Metrics.** We conduct experiments on multiple datasets to ensure the generalizability of the proposed method. The investigated datasets include the popular pedestrian tracking datasets MOT17 \[5\], MOT20 \[6\], and DanceTrack \[7\]. We follow the HOTA protocol\[26\] for quantitative evaluation, which provides a more comprehensive measurement of the tracking quality. HOTA is the main metric we refer to for tracking performance. AssA is the metric to measure association accuracy and DetA is for detection accuracy. We also report the metrics in the classic CLEAR protocol \[27\] for reference where MOTA indicates a overall performance of detection and tracking and IDF1 provides a measurement of association accuracy. **Implementations** Our implementation is based on OCSORT \[2, 28\]. We use the same YOLOX detector as recent works \[4, 3, 13, 1\] to make a fair comparison of tracking performance. For Re-ID, we use SBS50 from the fast-reid \[29\] library. For CMC, we adopt the OpenCV contrib VidStab module to generate similarity transforms using feature point extraction, optical ﬂow, and RANSAC, as previous works \[3\] choose. Across all experiments, we use a ﬁxed * * *α* = 0 *.* 95 for Dynamic Appearance. For experiments on MOT17 and MOT20, we set * a* *w* = 0 *.* 75 and * ϵ* = 0 *.* 5 for Adaptive Weighting. We use * * *a* *w* = 1 *.* 25 for DanceTrack, where we see appearance is more beneﬁcial than IoU, and * ϵ* = 1 *.* 0. **4.1.** ** ** **Benchmark Results**

We conduct experiments on MOT17 \[5\], MOT20 \[6\], and DanceTrack \[7\]. The results on MOT17-test and MOT20test are shown in Table 1. On MOT17-test, Deep OC-SORT achieves 64.9 HOTA, which outperforms all published methods and ranks 2nd on the leaderboard. On MOT20-test, Deep OC-SORT achieves 63.9 HOTA, ranking 1st on the leaderboard. Finally, on the most challenging dataset DanceTrack, where tracking algorithms usually suffer from heavy occlusion and frequent crossovers, our method achieves a new state-of-the-art among published methods as shown in Table 2. On all three datasets, using the same detections, our method beats the existing comparisons including SORT \[9\], DeepSORT \[8\], ByteTrack \[1\], OC-SORT \[2\], and StrongSORT \[4\]. Being online and without ofﬂine post-processing, our method still shows better association accuracy even compared to StrongSORT++, which is the ofﬂine version of StrongSORT, enhanced by ofﬂine post-processing of tracking

trajectories. The benchmark results make strong evidence of the advanced performance of Deep OC-SORT.

**4.2.** ** ** **Ablation Study** To demonstrate the effectiveness of the proposed modules, we perform an ablation study on validation sets of MOT17, MOT20, and DanceTrack. With a baseline of OC-SORT, we describe performance with the addition of: Appearance Embedding with a ﬁxed EMA (Appr.), Dynamic Appearance (DA), Camera Motion Compensation (CMC), and Adaptive Weighting (AW). The results are shown in Table 3. We ﬁnd that CMC improves performance on MOT17-val and DanceTrack-val sets while providing no improvements on MOT20-val, which is captured from static cameras. Appearance cues (Appr.) improve performance on all datasets across all metrics. Further applying Dynamic Appearance similarly boosts performance on all metrics, while adding no additional hyper-parameters and entirely negligible computation. Finally, Adaptive Weighting provides yet another consistent improvement in performance across all metrics and datasets.

# 5. CONCLUSION

In this work, we start from a motion-only multi-object tracking algorithm OC-SORT \[2\] and propose a novel way of incorporating visual appearance. The proposed adaptive reidentiﬁcation uses a weighted appearance similarity and compares across detection-track matches to create a blended visual cost. The extra camera motion compensation also provides beneﬁts for tracking objects under moving cameras. We hope the implemented method can serve as a strong baseline for future studies with both motion and appearance cues taken into multi-object tracking.

# 6. ACKNOWLEDGEMENTS

We would like to thank Rahul Nallamothu, Sam Pepose, Xiaochen Han and Chengxiang Yin from the Portal team at Meta for their useful advice and mentorship that helped shape the ideas for this work.

# 7. REFERENCES

\[1\] Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Zehuan Yuan, Ping Luo, Wenyu Liu, and Xinggang Wang, "Byte-

track: Multi-object tracking by associating every detection box," * * *arXiv preprint arXiv:2110.06864*, 2021.

\[2\] Jinkun Cao, Xinshuo Weng, Rawal Khirodkar, Jiangmiao Pang, and Kris Kitani, "Observation-centric sort: Rethinking sort for robust multi-object tracking," *arXiv* * * *preprint* *arXiv:2203.14360*, 2022.

\[3\] Nir Aharon, Roy Orfaig, and Ben-Zion Bobrovsky, "Bot-sort: Robust associations multi-pedestrian tracking," 2022.

\[4\] Yunhao Du, Zhicheng Zhao, Yang Song, Yanyun Zhao, Fei Su, Tao Gong, and Hongying Meng, "Strongsort: Make deepsort great again," *IEEE* * * *Transactions* * * *on* * * *Multimedia*, pp. 1-14, 2023.

\[5\] Anton Milan, Laura Leal-Taix´e, Ian Reid, Stefan Roth, and Konrad Schindler, "Mot16: A benchmark for multi-object tracking," * * *arXiv preprint arXiv:1603.00831*, 2016.

\[6\] Patrick Dendorfer, Hamid Rezatoﬁghi, Anton Milan, Javen Shi, Daniel Cremers, Ian Reid, Stefan Roth, Konrad Schindler, and Laura Leal-Taix´e, "Mot20: A benchmark for multi object tracking in crowded scenes," * * *arXiv* * * *preprint* *arXiv:2003.09003*, 2020.

\[7\] Peize Sun, Jinkun Cao, Yi Jiang, Zehuan Yuan, Song Bai, Kris Kitani, and Ping Luo, "Dancetrack: Multi-object tracking in uniform appearance and diverse motion," *arXiv* * * *preprint* *arXiv:2111.14690*, 2021.

| \[8\] Nicolai Wojke, Alex Bewley, and Dietrich Paulus, "Simple | online and realtime tracking with a deep association metric," | in ICIP. IEEE, 2017, pp. 3645-3649. |
|:--- |:--- |:--- |
| \[9\] Alex Bewley, Zongyuan Ge, Lionel Ott, Fabio Ramos, and | Ben Upcroft, "Simple online and realtime tracking," in ICIP. | IEEE, 2016, pp. 3464-3468. |
| \[10\] Rudolf Emil Kalman et al., "Contributions to the theory of | optimal control," Bol. soc. mat. mexicana, vol. 5, no. 2, pp. | 102-119, 1960. |

\[9\] Alex Bewley, Zongyuan Ge, Lionel Ott, Fabio Ramos, and Ben Upcroft, "Simple online and realtime tracking," in * ICIP*. IEEE, 2016, pp. 3464-3468.

\[10\] Rudolf Emil Kalman et al., "Contributions to the theory of optimal control," * * *Bol.* * * *soc.* * * *mat.* * * *mexicana*, vol. 5, no. 2, pp. 102-119, 1960.

\[11\] Yifu Zhang, Chunyu Wang, Xinggang Wang, Wenjun Zeng, and Wenyu Liu, "Fairmot: On the fairness of detection and re-identiﬁcation in multiple object tracking," * * *IJCV*, vol. 129, no. 11, pp. 3069-3087, 2021.

\[12\] Jiangmiao Pang, Linlu Qiu, Xia Li, Haofeng Chen, Qi Li, Trevor Darrell, and Fisher Yu, "Quasi-dense similarity learning for multiple object tracking," in * CVPR*, 2021, pp. 164-173.

\[13\] Jinkun Cao, Hao Wu, and Kris Kitani, "Track targets by dense spatio-temporal position encoding," *arXiv* * * *preprint* *arXiv:2210.09455*, 2022.

\[14\] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin, "Attention is all you need," * * *NeurIPS*, vol. 30, 2017.

\[15\] Fangao Zeng, Bin Dong, Tiancai Wang, Xiangyu Zhang, and Yichen Wei, "Motr: End-to-end multiple-object tracking with transformer," * * *arXiv preprint arXiv:2105.03247*, 2021.

\[16\] Peize Sun, Jinkun Cao, Yi Jiang, Rufeng Zhang, Enze Xie, Zehuan Yuan, Changhu Wang, and Ping Luo, "Transtrack: Multiple object tracking with transformer," *arXiv* * * *preprint* *arXiv:2012.15460*, 2020.

\[17\] Tim Meinhardt, Alexander Kirillov, Laura Leal-Taixe, and Christoph Feichtenhofer, "Trackformer: Multi-object tracking with transformers," * * *arXiv preprint arXiv:2101.02702*, 2021.

\[18\] Yihong Xu, Yutong Ban, Guillaume Delorme, Chuang Gan, Daniela Rus, and Xavier Alameda-Pineda, "Transcenter: Transformers with dense queries for multiple-object tracking," *arXiv preprint arXiv:2103.15145*, 2021.

\[19\] Shuai Wang, Hao Sheng, Yang Zhang, Yubin Wu, and Zhang Xiong, "A general recurrent tracking framework without real data," in * ICCV*, 2021, pp. 13219-13228.

\[20\] Peng Chu, Jiang Wang, Quanzeng You, Haibin Ling, and Zicheng Liu, "Transmot: Spatial-temporal graph transformer for multiple object tracking," *arXiv* * * *preprint* *arXiv:2104.00194*, 2021.

\[21\] Wei Li, Yuanjun Xiong, Shuo Yang, Mingze Xu, Yongxin Wang, and Wei Xia, "Semi-tcl: Semi-supervised track contrastive representation learning," *arXiv* * * *preprint* *arXiv:2107.02396*, 2021.

\[22\] Chao Liang, Zhipeng Zhang, Yi Lu, Xue Zhou, Bing Li, Xiyong Ye, and Jianxiao Zou, "Rethinking the competition between detection and reid in multi-object tracking," *arXiv* *preprint arXiv:2010.12138*, 2020.

| \[23\] Yongxin Wang, Kris Kitani, and Xinshuo Weng, "Joint ob- | ject detection and multi-object tracking with graph neural net- | works," in ICRA. IEEE, 2021, pp. 13708-13715. |
|:--- |:--- |:--- |
| \[24\] Xingyi Zhou, Vladlen Koltun, and Philipp Kr¨ahenb¨uhl, | "Tracking objects as points," in ECCV. Springer, 2020, pp. | 474-490. |
| \[25\] Jialian Wu, Jiale Cao, Liangchen Song, Yu Wang, Ming Yang, | and Junsong Yuan, "Track to detect and segment: An online | multi-object tracker," in CVPR, 2021, pp. 12352-12361. |

\[24\] Xingyi Zhou, Vladlen Koltun, and Philipp Kr¨ahenb¨uhl, "Tracking objects as points," in * * *ECCV*. Springer, 2020, pp. 474-490.

\[25\] Jialian Wu, Jiale Cao, Liangchen Song, Yu Wang, Ming Yang, and Junsong Yuan, "Track to detect and segment: An online multi-object tracker," in * CVPR*, 2021, pp. 12352-12361.

| \[26\] Jonathon Luiten, Aljosa Osep, Patrick Dendorfer, Philip Torr, | Andreas Geiger, Laura Leal-Taix´e, and Bastian Leibe, "Hota: | A higher order metric for evaluating multi-object tracking," | International journal of computer vision, vol. 129, no. 2, pp. | 548-578, 2021. |
|:--- |:--- |:--- |:--- |:--- |
| \[27\] Keni Bernardin and Rainer Stiefelhagen, | "Evaluating mul- | tiple object tracking performance: the clear mot metrics," | EURASIP Journal on Image and Video Processing, vol. 2008, | pp. 1-10, 2008. |
| \[28\] MMTracking Contributors, | "MMTracking: | OpenMM- | Lab video perception toolbox and benchmark," https:// | github.com/open-mmlab/mmtracking, 2020. |

\[27\] Keni Bernardin and Rainer Stiefelhagen, "Evaluating multiple object tracking performance: the clear mot metrics," *EURASIP Journal on Image and Video Processing*, vol. 2008, pp. 1-10, 2008.

\[28\] MMTracking Contributors, "MMTracking: OpenMMLab video perception toolbox and benchmark," https:// github.com/open-mmlab/mmtracking, 2020.

\[29\] Lingxiao He, Xingyu Liao, Wu Liu, Xinchen Liu, Peng Cheng, and Tao Mei, "Fastreid: A pytorch toolbox for general instance re-identiﬁcation," * * *arXiv* * * *preprint* * * *arXiv:2006.02631*, 2020.