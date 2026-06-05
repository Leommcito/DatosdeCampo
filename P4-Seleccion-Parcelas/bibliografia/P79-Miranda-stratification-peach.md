_**agriculture**_ 

## _Article_ 

## **Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards** 

## **Carlos Miranda * ID , Luis G. Santesteban, Jorge Urrestarazu, Maite Loidi and José B. Royo** 

Departamento de Agronomía, Biotecnología y Alimentación, Universidad Pública de Navarra, 31006 Pamplona, Spain; gonzaga.santesteban@unavarra.es (L.G.S.); jorge.urrestarazu@unavarra.es (J.U.); maite.loidi@unavarra.es (M.L.); jbroyo@unavarra.es (J.B.R.) 

***** Correspondence: carlos.miranda@unavarra.es; Tel.: +34-948-169-850 

Received: 30 April 2018; Accepted: 30 May 2018; Published: 4 June 2018 

**Abstract:** A quick and accurate sampling method for determining yield in peach orchards could lead to better crop management decisions, more accurate insurance claim adjustment, and reduced expenses for the insurance industry. Given that sample size depends exclusively on the variability of the trees on the orchard, it is necessary to have a quick and objective way of assessing this variability. The aim of this study was to use remote sensing to detect the spatial variability within peach orchards and classify trees into homogeneous zones that constitute sampling strata to decrease sample size. Five mature peach orchards with different degrees of spatial variability were used. A regular grid of trees was established on each orchard, their trunk cross-sectional area (TCSA) was measured, and yield was measured as number of fruits/tree on the central tree of each one of them. Red Vegetation Index (RVI) was calculated from aerial images with 0.25 m _·_ pixel _[−]_[1] resolution, and used, either alone or in combination with TCSA, to delineate sampling strata using cluster _fuzzy k-means_ . Completely randomized (CRS) and stratified samplings were compared through 10,000 iterations, and the Minimum Sample Size required to obtain estimates of actual production for three quality levels of sampling was calculated in each case. The images allowed accurate determination of the number of trees, allowing a proper application of completely randomized sampling designs. Tree size and the canopy density estimated by means of multispectral indices are complementary parameters suitable for orchard stratification, decreasing the sample size required to determine fruit count up to 20–35% compared to completely randomized samples. 

**Keywords:** _Prunus persica_ L. Batsch; sampling strategy; sample size; stratification 

## **1. Introduction** 

Providing appropriate risk management tools for agriculture is a key challenge for agricultural development, and agricultural insurance systems play a central role in that process. In Spain, for instance, the insurance industry represents a large market of 13,500 million euros, and, in 2017 alone, more than 10[5] claims related to damages caused by weather events were made, for a net worth of indemnities paid of around 450 million euros [1]. The Spanish agricultural insurance system is claim-based, which means that once a meteorological event, such as a frost or hail, has caused damage in an orchard, the grower must present a claim to the insurer. The insurer must check the claim and determine the incidence of such damage and to calculate the indemnities paid by the insurance companies. In fruit trees, the specific rule for damage inspection in fruit orchards [2] states that both the damage verification and yield estimation must be performed in the orchard using a ground-based completely randomized sampling (CRS) procedure or a systematic one, stratifying if it is appropriate. 

A CRS allows to reliably know the probability that the values obtained approximate the true values in the orchard and, if the sample size is insufficient, how many additional trees should be 

_Agriculture_ **2018** , _8_ , 78; doi:10.3390/agriculture8060078 

www.mdpi.com/journal/agriculture 

_Agriculture_ **2018** , _8_ , 78 

2 of 9 

sampled. To apply a CRS properly [3], all trees in the orchard must have the same probability to be chosen; therefore, the number of trees must be known to avoid bias. The size of the sample needed to obtain an adequate assessment of the population mean depends on three criteria: the level of precision, the level of confidence or risk, and the degree of within-orchard variability in the parameter being measured [4], but in practice, most sampling protocols recommend modest number of samples out of practical considerations: for crop insurance companies, a single frost or hail event generally can affect a large number of orchards in the same region. In those cases, the minimum sample size (MSS) required for a determination with adequate levels of precision and confidence could be easily larger than what is feasible for many orchards. To overcome this, stratified sampling, the process of balancing sampling frequency among mutually exclusive strata, has been demonstrated to improve sampling efficiency by reducing standard error of samples and can be used to estimate population means and standard deviations [5]. A well-established approach to recognize homogeneous grouping in data is cluster analysis [6]. Several methods have been developed for agricultural data, and one of the most widely used algorithms is _fuzzy k-means_ clustering [7]. This algorithm uses a weighting exponent to control the degree to which membership sharing occurs between classes and has been extensively used to classify yield and quality data with remotely sensed images [6–10]. 

Tree fruit differs from most annual crops in that plants are clonal, suggesting that there should be minimal variability between them compared with annual crops. However, orchard management and site-specific soil and climate effects accumulated over the years lead to significant within-orchard spatial variability that influences yield [11,12]. In this context, remote sensing could improve the efficiency of ground sampling protocols for yield assessments by (i) identifying the exact number of bearing trees in the orchard and (ii) detecting the spatial variability using auxiliary variables such as the Normalized Difference Vegetation Index (NDVI) or crown size [3] so that precision agriculture (PA) techniques would aid in classifying trees into homogeneous zones, which constitute sampling strata, lowering the MSS required. 

In agriculture, many authors have shown that remote sensing and vegetation indexes such as Red Vegetation Index (RVI) or NDVI were correlated with the spatial variation of tree characteristics and yield [11–16]. However, contributions attempting to apply remote sensing in sampling designs are recent and mostly focused mostly in viticulture. To date, aerial NDVI images have been used to optimize sampling protocols in vineyards resulting in significant sample size reductions compared to random sampling used alone [14,16] or in combination with ancillary information [17]. The aim of this work has been to use remote sensing to detect the spatial variability within peach ( _Prunus persica_ L. Batsch) orchards and classify trees into homogeneous zones that constitute sampling strata to decrease sample size. 

## **2. Materials and Methods** 

## _2.1. Data Acquisition_ 

The research was conducted in 2015, in five mature commercial peach orchards located in Tudela (Southern Navarre, Spain). Orchards were trained as 3-scaffold vase (open center) and were chosen to encompass a wide range of within-field variability in tree size or abundance of canopy vegetation. Description of the orchards, including cultivars, orchard ages, and areas are provided in Table 1 and Figure 1. 

_Agriculture_ **2018** , _8_ , 78 

3 of 9 

**Table 1.** Description of the characteristics of the five orchards used in the study. 

|**Cultivar**|**Orchard**|**Area**<br>**(ha)**|**Age**<br>**(years)**|**Row**<br>**Spacing (m)**|**Tree**<br>**Spacing (m)**|**Trees/Orchard**|**Sampling**<br>**Nodes (SN)**|
|---|---|---|---|---|---|---|---|
|Catherine|BOL_01|8.9|12|6.0|3.9|3800|192|
|Tochino|MCI_01|8.1|10|6.0|4.0|3200|150|
|Baby Gold 6|VAL_01|9.7|22|6.0|4.5|3400|176|
|Miraflores|VAL_02|8.4|22|6.0|5.0|2650|159|
|Venus|ABL_01|4.5|20|5.0|2.5|3420|143|



**Figure 1.** Cadaster images and location of the orchards used in the study. ( **a** ) VAL_01; ( **b** ) VAL_02; ( **c** ) ABL_01; ( **d** ) MCI_01; ( **e** ) BOL_01; ( **f** ) Location of the study area, indicated by a black dot. 

A staggered regular sampling grid was defined for every orchard. Each node in the grid was composed by 6 trees in two consecutive rows (3 _×_ 2). Nodes were placed at 10 tree intervals in the row along two staggered rows (Figure 2). This resulted in a total of 143 to 192 sampling nodes (SN) per orchard, depending on their shape and area (Table 1). 

_·_ Canopy reflectance information was extracted from 0.25 m pixel _[−]_[1] resolution images acquired by an airborne RGB-NIR sensor, gathered in a commercial mission performed by a private company (Agropixel SA, Lleida, Spain) on 10 August 2015 using a high-resolution airborne multispectral sensor (HiRAMS) system with a four-channel camera mounted on a Cessna 172 Skyhawk. The sensor filters were adjusted to 450 nm (blue, band one), 550 nm (green, band two), 670 nm (red, band three) and 780 nm (near infrared, NIR, band four). The spectral bands were pre-processed by the provider to compensate for mis-registration due to lens distortion (<0.2 pixels). 

Prior to applying vegetation index to the mosaicked imagery, the provider performed a canopy classification procedure, separating image pixels dominated by tree canopy from those containing soil and/or inter-row vegetation. Following the classification procedure, RVI was calculated as the ratio between RED/NIR bands, and RVI values were normalized to an 8-bit scale (0–255). The image area corresponding to the six adjacent trees was cropped, and its mean RVI value was determined. 

_Agriculture_ **2018** , _8_ , 78 

4 of 9 

**Figure 2.** Close-up schematic of the upper part of VAL_02 orchard, indicating the sampling grid. 

In summer, after thinning and before harvest, trunk size (TCSA, cross-sectional area 15 cm above grafting point, cm[2] ) was recorded on each tree in the SN, whereas fruit number (fruit _·_ tree _[−]_[1] ) was recorded in the tree with TCSA closer to the average of the six trees in the SN. 

## _2.2. Data Analysis_ 

## 2.2.1. Delineation of Sampling Strata 

Unsupervised clustering was performed using trunk size and RVI information in combination, using the _fuzzy k-means_ algorithm to delineate sampling strata. Euclidean distance was used, considering the variables to be independent, and a stopping criterion of 0.0001 was used to obtain good convergence [8]. Cluster analysis was performed testing fuzzy exponents (m) that ranged between 1 and 2 at 0.1 intervals [18], considering 2, 3, and 4 as potential number of clusters (C), since greater sub-divisions would not be practical for sampling purposes. In order to determine the optimum C, the fuzziness performance index (FPI) and the modified partition entropy (MPE) as defined by [18] were calculated. Cluster number was chosen to obtain the smaller values for FPI and MPE. The trees in the sampling grid were then assigned to their respective homogeneous zones (strata). All the calculations were performed using FuzME v3.5c software (Australian Centre for Precision Agriculture, Sydney, Australia), accessible as freeware. 

## 2.2.2. Definition of Sample Sizes 

Sample size for complete randomized samples (SSCRS) was set on each orchard to the minimum sample size (MSS) suggested by the variability fou ~~nd w~~ ithin all the trunk sizes measured in the SPs. MSS was defined as (Equation (1), [4]), 

**==> picture [251 x 24] intentionally omitted <==**

where _Z_[2] is the abscissa of the normal curve that cuts off an area _α_ at the tails (1 _− α_ equals the desired confidence level), e is the desired level of precision, _p_ is the estimated proportion of the attribute, and _q_ is 1 _− p_ . SSOr was calculated for a 95% confidence interval, 10% precision, assuming maximum variability ( _p_ = 0.5), and corrected for small population size [4]. 

Sample size within the strata identified on stratified samplings (SSSTR) was defined as (Equation (2)): 

_Agriculture_ **2018** , _8_ , 78 

5 of 9 

**==> picture [255 x 22] intentionally omitted <==**

where SE is the number of sampling strata identified in the orchard. SSSTR were rounded up to the next integer. 

## 2.2.3. Sampling Methods 

Each type of sampling (completely randomized or stratified) was repeated 10[4] times by means of a script using the _sample_ function of R v3.2.2 statistic package [19] with RStudio v0.99.489 [20]. The MSS required to obtain estimates of actual production was calculated in each case for three sampling quality levels. 

- Fair: 90% confidence level, 15% precision; 

- Good: 95% confidence level, 15% precision; 

- Excellent: 95% confidence level, 10% precision. 

The performance of sampling strata at reducing MSS regarding complete randomized samples (CRS) was evaluated comparing the 95% confidence intervals for the mean of the MSSs obtained on each sampling type. 

## **3. Results** 

The orchards used in this study included high coefficients of variation (CV) for the groundmeasured parameters tree size, evaluated by means of TCSA, and fruit count (Table 2), which indicates the existence of considerable within-field variability. However, RVI was generally less variable than TCSA, and the variability was inversely correlated ( _R_[2] = 0.71, _p_ < 0.0001) to the mean RVI values. The particularly low variability in RVI found in VAL_02 and BOL_01, compared to the much higher CV values found for TCSA is probably indicating a saturation effect that appears once the vegetation density increases beyond a threshold value [21]. 

With regards to the clusters obtained with tree size and RVI combined, for all the runs, the optimum fuzziness exponents ranged between 1.2 and 1.3 depending on the orchard. FPI and MPE agreed that the number of clusters was 2 (MCI_01 and VAL_02) or 3 (all other orchards). In all cases, the values of both indices were closer to 0 than 1, which indicates a high degree of organization [22]. 

**Table 2.** Descriptive statistics (means and coefficient of variation, CV) for the characteristics measured in the trees of the sampling grids and sample sized used on complete randomized samples (SSCRS) and stratified samples (SSSTR). 

||**TCSA**|**(cm2)**||**RVI**|**Fruits****_·_Tree****_−_1**|**Fruits****_·_Tree****_−_1**|**Sample**|**Size**|
|---|---|---|---|---|---|---|---|---|
|**Orchard**|**Mean**|**CV (%)**|**Mean**|**CV (%)**|**Mean**|**CV (%)**|**SSCRS**|**SSSTR**|
|BOL_01|236.7|30.3|225.5|5.9|240.6|25.4|35.3|12.0|
|MCI_01|190.5|20.9|157.0|16.0|245.5|21.7|16.8|9.0|
|VAL_01|395.6|23.4|121.0|21.0|241.4|23.5|21.1|8.0|
|VAL_02|318.8|23.1|171.9|11.5|312.9|24.2|20.5|11.0|
|ABL_01|187.4|26.9|143.1|36.9|147.7|36.9|27.9|10.0|



Considered individually, both TCSA and RVI were poorly related to fruit count (Figure 3), but when they were combined (RVI _·_ TCSA _[−]_[1] ), the relationship with fruit count improved significantly. As expected, within-cluster variability for TCSA and RVI was significantly ( _p_ < 0.001) lower than within-orchard (Table 3), with average reductions in CV ranging from 19 to 42%. However, the clusters were less efficient in decreasing internal variability in fruit count, as average CV reductions were below 10% in four orchards. Furthermore, in MCI_01, which was the least variable orchard in the study, clusters were not significantly different ( _p_ = 0.217). 

_Agriculture_ **2018** , _8_ , 78 

6 of 9 

**Figure 3.** Relationships between tree size, evaluated by different methods, and fruits per tree. ( **a** ) Trunk cross-sectional area (TCSA); ( **b** ) Red Vegetation Index (RVI); ( **c** ) RVI per TCSA. Each dot corresponds to a sampling node ( _n_ = 950). 

_Agriculture_ **2018** , _8_ , 78 

7 of 9 

**Table 3.** Number of sampling strata identified in the orchards, mean decrease in variability (CV, %) of tree characteristics within each stratum compared to the variability detected in the whole orchard. 

|**Orchard**<br>**Sampling Strata (n****_◦_)**|**Mean Decrease in CV**|
|---|---|
||**TCSA**<br>**RVI**<br>**Fruit****_·_Tree****_−_1**|
|BOL_01<br>3<br>MCI_01<br>2<br>VAL_01<br>3<br>VAL_02<br>2<br>ABL_01<br>3|30<br>34<br>3<br>23<br>32<br>0 1<br>26<br>42<br>10<br>19<br>26<br>5<br>27<br>28<br>25|



1 Strata were not significantly different ( _p_ > 0.05) for this parameter. 

Once the trees in the sampling grid were assigned to their respective sampling strata, the MSS needed to determine fruit count was calculated (Table 4) and compared to that in the completely randomized sampling (CRS). In all orchards, MSS increased steeply when higher quality estimates were required: in average, getting from “Fair” to “Good” quality estimates increased MSS by 30–40% but from “Good” to “Excellent” doubled it (and tripled MSS in “Fair”). The number of trees required for “Fair” or “Good” estimates was rather moderate in most orchards, which highlights the relevance of using truly random sampling methods. However, when within-orchard variability was very high, as it was the case in ABL_01, the MSS required even for “Fair” quality estimates was much higher. In the three quality levels tested, the stratified sampling procedure effectively decreased MSS in most orchards, and in the worst case (MCI_01) did not increased it. Reduction was more evident as higher sampling quality was required, quality sample size decreased from 0 to 25% for “Fair,” whereas reductions from 10 to 35% were obtained for “Excellent” sampling quality specifications. 

**Table 4.** Minimum sample sizes (MSS) required to estimate fruit count in the orchards using completely randomized (CRS) or stratified samplings (Stratified). Values correspond to the 95% confidence intervals in 10[4] replicated samplings. 

|**Orchard**|**Fair Quality 1**<br>**Good Quality**<br>**Excellent Quality**|
|---|---|
||**CRS**<br>**Stratifed**<br>**CRS**<br>**Stratifed**<br>**CRS**<br>**Stratifed**|
|BOL_01<br>MCI_01<br>VAL_01<br>VAL_02<br>ABL_01<br>Mean|7–8<br>7–8<br>10–12<br>9–11<br>23–27<br>20–23<br>5–7<br>5–6<br>7–10<br>7–9<br>17–23<br>16–19<br>6–8<br>5–6<br>9–11<br>6–8<br>20–25<br>14–17<br>6–8<br>5–7<br>9–12<br>8–10<br>20–27<br>16–21<br>14–18<br>12–14<br>20–25<br>16–19<br>45–56<br>31–36<br>8–10<br>7–8<br>11–14<br>9–11<br>25–31<br>19–23|



> 1 Fair: MSS required to obtain estimates with confidence level = 90% and precision = 15%. Good: confidence level = 95%, precision = 15%. Excellent: confidence level = 95%, precision = 10%. 

## **4. Discussion** 

In peach trees, fruit load can be estimated with sufficient precision from tree size, planting density, and total shoot length per TCSA [23]. The latter acts on a peach variety as a surrogate for the number of leaves and, therefore, could be considered a vegetation index analogous to RVI. The results of this study show that using a vegetation index RVI in combination with a tree size estimator (TCSA) provided clusters significantly different in fruit load and more homogeneous internally than the whole orchard. Consequently, clustering has been of value to reduce the effort required to obtain accurate fruit load estimations in the peach orchards using stratified sampling strategies. Indeed, the sample size required to estimate fruit load for a given quality of the estimation could be decreased up to 35% using stratified sampling compared to CRS. 

In precision agriculture, sampling methods defined according to auxiliary data have been used for the calibration of spatial models [14,24], and vegetation indexes have been considered as relevant 

_Agriculture_ **2018** , _8_ , 78 

8 of 9 

auxiliary information to optimize sampling for yield estimations. In fact, many authors have shown that vegetation indexes are correlated with yield or yield components at the within-field level [13–15,25] in several perennial crops (grapevine, apple trees, or citrus, to cite some). However, to date, there are few contributions attempting to apply remote sensing in sampling designs for permanent crops, mostly focused in viticulture [5,14,16,17]. Our results are consistent with those obtained by [5,14]. The former decreased sample sizes up to a 24% using a spatially weighted template sampling instead of random sampling, whereas the latter used NDVI-based sampling strategies that improved vine yield estimates by at least 5–7% compared to the random method. 

This study offers promising results for improving yield sampling in peach orchards, but some practical issues should be solved before the methodology could be routinely implemented. We combined aerial, high-resolution multispectral information (RVI) with discrete, ground-based estimators of tree size (TCSA). However, RVI showed little sensitivity in some orchards, probably due to the decreased reflectance of NIR in dense canopies [21]. Using a multispectral index better adapted to those situations, like the ones proposed by [21], could improve the efficiency of the clustering process. Additionally, it would also be desirable to have continuous high-resolution aerial information for tree geometry and size, which could substitute the TCSA information measured in this study. In this regard, the high-resolution images provided by unmanned aerial vehicles (UAVs) could be used successfully to characterize the volumetric configuration (i.e., size) of the canopy [26]. 

## **5. Conclusions** 

A quick and accurate sampling method for determining losses could lead to better crop management decisions, more accurate insurance claim adjustment, and reduced expenses for the insurance industry. Therefore, the insurance industry may constitute an important application field for remote sensing. In fact, our results suggest that remote sensing could constitute a powerful tool for saving time and effort in the damage and yield assessing processes. Tree size and canopy density estimated by means of multispectral indices are complementary parameters, allowing a proper application of completely randomized sampling designs, which decrease the sample size required to determine yield up to 20–35% compared to completely randomized samples. 

**Author Contributions:** Conceptualization, C.M. and J.B.R.; Methodology, C.M. and L.G.S.; Formal Analysis, C.M.; Investigation, C.M., J.U., M.L.; Writing-Original Draft Preparation, C.M., L.G.S.; Writing-Review & Editing, C.M., L.G.S., J.U., M.L., J.B.R.; Funding Acquisition, J.B.R. 

**Funding:** This research was funded by the Agrupación Española de Entidades Aseguradoras de los Seguros Agrarios Combinados (AGROSEGURO, S.A.), Madrid, Spain. 

**Acknowledgments:** The authors also would like to express their gratitude to the owners and technical staff of the orchards for their cooperation and valuable help to perform this field experiment. 

**Conflicts of Interest:** The authors declare no conflict of interest. The founding sponsors had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, and in the decision to publish the results. 

## **References** 

1. Agroseguro. _Informe Anual (Annual Report)_ ; Agroseguro: Madrid, Spain, 2013. 

2. Boletín Oficial del Estado. _Orden PRE/1950/2005, de 17 de Junio, por la que se Aprueba la Norma Específica de Peritación de Daños en la Producción de Frutales, Amparados por el Seguro Agrario Combinado_ ; Ministerio de la Presidencia: Madrid, Spain, 2005; pp. 22172–22176. 

3. Wulfsohn, D.; Zamora, F.A.; Téllez, C.P.; Lagos, I.Z.; García-Fiñana, M. Multilevel systematic sampling to estimate total fruit number for yield forecasts. _Precis. Agric._ **2012** , _13_ , 256–275. [CrossRef] 

4. Cochran, W.G. _Sampling Techniques_ , 3rd ed.; John Wiley & Sons: New York, NY, USA, 1977; ISBN 047116240X. 

5. Meyers, J.; Sacks, G.; van Es, H.; Vanden Heuvel, J.E. Improving vineyard sampling efficiency via dynamic spatially explicit optimisation. _Aust. J. Grape Wine Res._ **2011** , _17_ , 306–315. [CrossRef] 

_Agriculture_ **2018** , _8_ , 78 

9 of 9 

6. Peeters, A.; Zude, M.; Käthner, J.; Ünlü, M.; Kanber, R.; Hetzroni, A.; Gebbers, R.; Ben-Gal, A. Getis-Ord’s hotand cold-spot statistics as a basis for multivariate spatial clustering of orchard tree data. _Comput. Electron. Agric._ **2015** , _111_ , 140–150. [CrossRef] 

7. Fridgen, J.J.; Kitchen, N.R.; Sudduth, K.A.; Drummond, S.T.; Wiebold, W.J.; Fraisse, C.W. Management Zone Analyst (MZA): Software for Subfield Management Zone Delineation. _Agron. J._ **2004** , _96_ , 100–108. [CrossRef] 

8. Fridgen, J.; Fraise, C.; Kitchen, N.; Sudduth, K. Delineation and analysis of site-specific management zones. In Proceedings of the Second International Conference on Geospatial Information in Agriculture and Forestry, Lake Buena Vista, FL, USA, 10–12 January 2000; ERIM International: Ann Arbor, MI, USA, 2000; pp. 402–411. 

9. Santesteban, L.G.; Urretavizcaya, I.; Miranda, C.; García, A.; Royo, J.B. Agronomic significance of the zones defined within vineyards early in the season using NDVI and fruit load information. Papers Presented at the 9th European Conference on Precision Agriculture, ECPA 2013, Lleida, Spain, 7–11 July 2013; pp. 641–647. 

10. Urretavizcaya, I.; Santesteban, L.G.; Tisseyre, B.; Guillaume, S.; Miranda, C.; Royo, J.B. Oenological significance of vineyard management zones delineated using early grape sampling. _Precis. Agric._ **2014** , _15_ , 111–129. [CrossRef] 

11. Perry, E.M.; Dezzani, R.J.; Seavert, C.F.; Pierce, F.J. Spatial variation in tree characteristics and yield in a pear orchard. _Precis. Agric._ **2010** , _11_ , 42–60. [CrossRef] 

12. Uribeetxebarria, A.; Daniele, E.; Escolà, A.; Arnó, J.; Martínez-Casasnovas, J.A. Spatial variability in orchards after land transformation: Consequences for precision agriculture practices. _Sci. Total Environ._ **2018** , _635_ , 343–352. [CrossRef] [PubMed] 

13. Zude-Sasse, M.; Fountas, S.; Gemtos, T.A.; Abu-Khalaf, N. Applications of precision agriculture in horticultural crops. _Eur. J. Hortic. Sci._ **2016** , _81_ , 78–90. [CrossRef] 

14. Carrillo, E.; Matese, A.; Rousseau, J.; Tisseyre, B. Use of multi-spectral airborne imagery to improve yield sampling in viticulture. _Precis. Agric._ **2016** , _17_ , 74–92. [CrossRef] 

15. Liakos, V.; Tagarakis, A.; Fountas, S.; Nanos, G.D.; Tsiropoulos, Z.; Gemtos, T. Use of NDVI to predict yield variability in a commercial apple orchard. In _Precision Agriculture ’15_ ; Wageningen Academic Publisher: Wageningen, The Netherlands, 2015; pp. 553–560. 

16. Meyers, J.M.; Vanden Heuvel, J.E. Use of normalized difference vegetation index images to optimize vineyard sampling protocols. _Am. J. Enol. Vitic._ **2014** , _65_ , 250–253. [CrossRef] 

17. Araya-Alman, M.; Acevedo-Opazo, C.; Guillaume, S.; Valdés-Gómez, H.; Verdugo-Vásquez, N.; Moreno, Y.; Tisseyre, B. Using ancillary yield data to improve sampling and grape yield estimation of the current season. _Adv. Anim. Biosci. Precis. Agric._ **2017** , _8_ , 515–519. [CrossRef] 

18. McBratney, A.; Moore, A. Application of fuzzy sets to climatic classification. _Agric. For. Meteorol._ **1985** , _35_ , 165–185. [CrossRef] 

19. R Core Team. _R: A Language and Environment for Statistical Computing_ ; R Foundation for Statistical Computing: Vienna, Austria, 2018; Available online: http://www.r-project.org (accessed on 25 April 2018). 

20. RStudio Team. _RStudio: Integrated Development for R_ ; RStudio, Inc.: Boston, MA, USA, 2015; Available online: http://www.rstudio.com (accessed on 25 April 2018). 

21. Gitelson, A.A.; Kaufman, Y.J.; Stark, R.; Rundquist, D. Novel algorithms for remote estimation of vegetation fraction. _Remote Sens. Environ._ **2002** , _80_ , 76–87. [CrossRef] 

22. Boydell, B.; McBratney, A. Identifying potential within-field management zones from cotton-yield estimates. _Precis. Agric._ **2002** , _3_ , 9–23. [CrossRef] 

23. Jiménez, C.M.; Royo Díaz, J.B. A statistical model to estimate potential yields in peach before bloom. _J. Am. Soc. Hortic. Sci._ **2003** , _128_ , 297–301. 

24. Lesch, S. Sensor-directed response surface sampling designs for characterizing spatial variation in soil properties. _Comput. Electron. Agric._ **2005** , _46_ , 153–179. [CrossRef] 

25. Bramley, R.G.V.; Hamilton, R.P. Understanding variability in winegrape production systems 1. Within vineyard variation in yield over several vintages. _Aust. J. Grape Wine Res._ **2005** , _10_ , 32–45. [CrossRef] 

26. Matese, A.; Di Gennaro, S.F.; Miranda, C.; Berton, A.; Santesteban, L.G. Evaluation of spectral-based and canopy-based vegetation indices from UAV and Sentinel 2 images to assess spatial variability and ground vine parameters. _Adv. Anim. Biosci._ **2017** , _8_ , 817–822. [CrossRef] 

   - © 2018 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). 

