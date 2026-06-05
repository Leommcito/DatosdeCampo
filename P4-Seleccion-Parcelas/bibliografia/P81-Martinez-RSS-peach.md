Document downloaded from: 

http://hdl.handle.net/10459.1/66692 

The final publication is available at: 

https://doi.org/10.1016/j.compag.2019.104931 

Copyright 

cc-by-nc-nd, (c) Elsevier, 2019 

Està subjecte a una llicència de Reconeixement-NoComercial-SenseObraDerivada 3.0 de Creative Commons 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## **Assessing ranked set sampling and ancillary data to improve fruit** 

## **load estimates in peach orchards** 

**Asier Uribeetxebarria[1] · José A. Martínez-Casasnovas[2] · Bruno Tisseyre[3] · Serge Guillaume[3] · Alexandre Escolà[1] · Joan R. Rosell-Polo[1] · Jaume Arnó[1]** 

Asier Uribeetxebarria (*) 

Uribeetxebarria.asier@gmail.com 

Jaume Arnó (*) 

JArno@eagrof.udl.cat 

> 1 Research Group in AgroICT & Precision Agriculture, Department of Agricultural and Forest Engineering, University of Lleida - Agrotecnio Centre, Rovira Roure, 191, Lleida, 25198, Catalonia, Spain 

> 2 Research Group in AgroICT & Precision Agriculture, Department of Environmental and Soil Sciences, University of Lleida - Agrotecnio Centre, Rovira Roure, 191, Lleida, 25198, Catalonia, Spain 

3 ITAP, Montpellier SupAgro, Irstea, Univ Montpellier, Montpellier, France 

**Abstract** Fruit load estimation at plot level before harvest is a key issue in fruit growing. To face this challenge, two sampling methods to estimate fruit load in a peach tree orchard were compared: simple random sampling (SRS) and ranked set sampling (RSS). The study was carried out in a peach orchard ( _Prunus persica_ cv. 'Platycarpa') covering a total area of 2.24 ha. Having previously sampled the plot systematically to cover the entire area (104 individual trees or sampling points), both sampling methods (SRS and RSS) were tested by taking samples from this population with varying sample sizes from _N_ = 4 to _N_ = 12. Since RSS requires ancillary information to obtain the samples (ranking mechanism), several proximal and remote sensors 

1 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

already used or recently introduced in agriculture were assessed as data sources. A total of 14 variables provided by 5 different sensors and platforms were considered as potential ancillary variables. Among them, RGB images captured by an unmanned aerial vehicle (UAV), and used to estimate the canopy projected area of individual trees, proved to be the best of the options. This was shown by the high correlation (R = 0.85) between this area and the fruit load, providing RSS with the UAV-based canopy projected area the lowest Coefficient of Error ( _CE_ ) for a given tree sample size. Then, comparing relative efficiency between random sampling (SRS) and RSS, the latter enables more precise fruit load estimates for any of the considered sample sizes. Interest and opportunity of RSS can be raised from two points of view. In terms of confidence, RSS managed to reduce the variance of fruit load estimates by about half compared to SRS. Sampling errors above the 10% threshold were always produced significantly fewer times using RSS, regardless of the sample size. In terms of operation within the plot, sample size could be reduced by 50%, from _N_ = 10 for SRS to _N_ = 5 for RSS, and this being expected sampling errors less than 10% in practically 70% of the samplings performed in both cases. In summary, fruit growers can take advantage of the combined use of appropriate data (RGB images from UAV) and RSS to optimize sample sizes and operational sampling costs in fruit growing. 

**Keywords** Ranked set sampling · Fruit growing · Sampling efficiency · Yield estimation 

## **List of abbreviations and symbols** 

|DMSC|Digital multispectral camera|
|---|---|
|ECa|Soil apparent electrical conductivity|
|MTLS|Mobile terrestrial laser scanner|
|NDRE|Normalized difference red edge|
|NDVI|Normalized difference vegetation index|
|RSS|Ranked set sampling|
|SRS|Simple random sampling|
|TCA|Tree canopy projected area|
|TCSA|Trunk cross-sectional area|



2 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

|UAV<br>_B_<br>_CE_<br>𝐸"𝑌[%]'<br>_MSE_<br>_N_<br>_PR_<br>_RE_<br>𝑣𝑎𝑟"𝑌<br>'<br>𝑌[%]<br>𝑌<br><<br>𝑌.<br>1−𝑓|Unmanned aerial vehicle<br>Number of realizations used (_B_= 1000) in the bootstrap method<br>Coefficient of Error<br>Expected yield value corresponding to the order statistic_j_(coincident with the order<br>parameter𝜇[%]<br>∗)<br>Mean squared error<br>Sample size<br>Percentage of individual realizations over the total of_B_= 1000 with sampling error<br>*+<br>,-+.*<br>+.<br>× 100greater than 10%<br>Relative efficiency<br>Variance of the sample mean𝑌<br>Ranked yield value (fruit load) corresponding to the order statistic_j_ (𝑗= 1, … , 𝑁)<br>within a sample of size_N_<br>Sample mean for each of the_B_= 1000 realizations generated by bootstrap resampling<br>Average of the total trees sampled within the plot (or better estimate of the population<br>mean𝜇)<br>Finite populationcorrection|
|---|---|



## **1. Introduction** 

Fruit tree crops are considered high value products (Aggelopoulou et al. 2010), but they demand more tasks from farmers compared to arable crops. Among the tasks required in peach orchards, harvesting is a complex process that, necessarily done by hand, usually also needs to be finished in a short time window. Because of that, a large amount of labor is often needed once the quality standards demanded by the market have been reached (ripening of the fruit). Hence, obtaining a reliable yield estimate in advance would improve the logistics of the entire process (Wulfsohn et al. 2012), also contributing to anticipate operational costs more effectively. 

In perennial crops, it is known that regular patterns are adopted by planting commercial plots with genetically uniform plant material (Miranda et al. 2015). Therefore, it is expected to achieve regular growths and certain homogeneity in production and quality. From this point of view, making an estimate of the yield should not raise any issue. By randomly choosing a few trees, the estimation of yield should be quite accurate knowing the total number of trees within the plot. However, perennial plots are not always homogeneous and spatial variability is present 

3 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

due to environmental factors, as it has been shown in different studies (Berman et al. 1996; Taylor et al. 2005; Arnó et al. 2012). Moreover, since many of the factors that affect yield (or fruit load) are spatial dependent, yield spatial distribution within the orchards usually presents patterns and is not random (Aggelopoulou et al. 2013). Under this scenario of structured variability with yield potential varying for each tree and for the different productive areas within the plot, simple random sampling (SRS) strategy may be inefficient for estimating average crop loading per tree. In order to fulfill fruit grower demands, yield forecast should be made by using 5-6 sampling trees and with maximum error of 10%. Therefore, SRS may not be the best option since it does not take into account any spatial organization of the variable to estimate. Moreover, a large sample size may be needed to fulfill growers’ constraints (Carrillo et al. 2016). Only the simplicity to implement and understand the results of SRS would explain why this method is still used in agriculture in forecasting tasks. Therefore, the Precision Agriculture concept allows this issue to be overcome since, as a management strategy, it is about gathers, processes and analyzes temporal, spatial and individual data and combines it with other information to support management decisions according to estimated variability for improved resource use efficiency, productivity, quality and sustainability of agricultural production (ISPA Newsletter, 2019). 

Although it is fair to mention that one of the pioneering work on sampling in fruit trees was published in the forties (Pearce, 1944), sampling methods making use of ancillary information provided by high spatial resolution sensors have been proposed in recent years. Previous analysis of the within-field variability of such information is often key when designing the sampling strategy. Even spatial variability on a smaller scale has also been the option used by other authors. So in 1990, Monestiez et al. proposed a geostatistical approach to optimally sample within the trees to improve yield estimates. Wulfshon et al. (2012) discussed using 

4 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

images to optimize sample sizes and opted for a multilevel systematic sampling to estimate the number of fruits reaching errors of just 10%, then extending this same method to estimate quality parameters (Martinez Vega et al. 2013). More recently, stratified sampling based on the use of auxiliary information for the spatial stratification of the sample has also shown promising results. Examples of this research are shown in Arnó et al. (2017) and Miranda et al. (2015, 2018). Specifically, trees were stratified using clustered NDVI-based aerial images (NDVINormalized Difference Vegetation Index), either alone or in combination with other information layers such as the trunk cross-sectional area (TCSA). In fact, because of the increasingly widespread use of remote sensing in fruit growing, there are companies that already offer advice for yield estimation based on the use of images in stratified sampling schemes. This practice manages to improve efficiency compared to random sampling, although sample sizes are still needed above what would be desirable. In addition, obtaining the representative NDVI value for an individual canopy or, even more, a manual measurement of the trees is not always a simple task (Fountas et al. 2011). 

The use of ancillary information to stratify sampling has been favored by the availability and rapid access to proximal and remote sensors data. Among the sources of information most used for this purpose, it is worth mentioning the NDVI images (Meyers and Vanden Heuvel 2014), the apparent electrical conductivity (ECa) of the soil (Mann et al. 2011; Arnó et al. 2017), and time series of yield maps provided by manual harvesting or monitored by sensors on harvesters (Araya et al. 2017). Other data are also available while other technologies for acquiring crop data have been fine-tuned. It refers to RGB and multispectral cameras (Ulzii-Orshikh et al. 2017), mounted on terrestrial platforms or unmanned aerial vehicles (UAV), and mobile terrestrial laser scanners (MTLS) based on 2D LiDAR sensors (Rosell et al. 2009; Escolà et al. 

5 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

2017), offering new possibilities for capturing canopy information from fruit trees. These higher resolution data allow the trees to be characterized in greater detail, but possible advantages of their use in sampling have not yet been verified. 

As already mentioned, SRS is a well-known method in agriculture. It is statistically consistent, but not always the most efficient. Moreover, there is a growing interest in developing sampling methods that, in addition to provide accurate and unbiased yield estimates, allow small sample sizes to be used. Stratified sampling (Cochran 1977) may be an option, because it fulfills the characteristics described above. However, to stratify the samples based on ancillary variable maps, fruit growers have to define the strata as a preliminary step by choosing between different classifications and zoning techniques. How many strata, how the strata are obtained, and how sampling points should be allocated in each stratum are decisions to be made. Therefore, this combination of subjective factors probably ends up affecting the goodness of yield estimates. Another option is using the Ranked Set Sampling (RSS) (McIntyre 1952). This method is interesting from the operational point of view because it does not need these preliminary steps. To obtain the sample, once the number of sites to sample is set, RSS only requires applying a ranking mechanism based on the distribution of an auxiliary variable (Wolfe 2010). This ranking mechanism allows the trees (sampling points), previously taken randomly in a first iteration from the population, to be ranked from lowest to highest, according to the value that in these trees takes an ancillary variable. More details about the ranking mechanism and the different iterations of the whole process can be found in the corresponding section below ( _Basics of the sampling methods_ ). With everything, the ancillary information is therefore key in the procedure since it has to present high correlation with the variable to estimate (the fruit 

6 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

load, in the case of this work). In short, finding the best ancillary information to perform RSS in fruit orchards is a pending issue to solve. 

Focusing our research on comparing RSS and SRS, the main objective of the present work was to evaluate whether the use of ranked samples significantly improves fruit load estimates in fruit growing. To do this, two main issues were addressed: i) to determine the most appropriate ancillary information to be used in the ranking process, and ii) to assess the efficiency in terms of coefficient of error when comparing RSS to SRS for different sample sizes. 

## **2. Materials and methods** 

## _2.1. Study plot_ 

The study was carried out in a commercial peach orchard located in Aitona (45° 94’ 71” N, 0° 29’ 20” E, ETRS89, 160 m a.s.l., Lleida, Catalonia, Spain). The plot covered an area of 2.24 ha. It was planted in 2012 with white peach ( _Prunus persica_ cv. ‘Platycarpa’) according to a regular plantation pattern of 5x2 m (Fig. 1). The total number of trees was 1816, which were delimited and counted using an airborne image. 

7 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Fig 1** Location of the study area and orthophoto (2016) showing the 104 trees sampled within the plot. (Orthophoto source: Cartographic and Geologic Institute of Catalonia). 

Peach trees were planted in form of “Catalan” vessel shape, which is the most common training system in Catalonia. This canopy management system produces some visible gaps between trees within the same row, being relatively easy to individualize each tree. Regarding agricultural tasks, the plot was managed like many of the commercial orchards in the region. Drip irrigation system was used for water and fertilizers supply. 

The plot was representative of the so-called Ebro depression area, characterized by the presence of broad flat regions resulting from infilled valley bottoms and residual landforms. Climate is typical of hot semi-arid areas, with strong seasonal temperature variations and an annual rainfall frequently below 400 mm. As a consequence, soils in the region usually have high concentrations of calcium carbonate (CaCO3) and low content of organic matter (OM). However, as a main feature, within-field soil heterogeneity is prevalent in many plots due to 

8 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

the levelling of original terraces in the eighties to facilitate agricultural mechanization. The plot under study resulted from this type of transformation. As for the spatial variability of trees within the plot, individualized canopy projected area values for each tree were obtained (see section 2.4.2 for more details). The average value was 2.82 m[2] , with a range between 0.62 m[2] and 5.50 m[2] , and a Coefficient of Variation (CV) close to 21%, which can be considered a lowto-moderate variability level for fruit orchards. 

## _2.2. Systematic sampling of the orchard_ 

A regular sampling grid of 15x15 m was defined in 2016 to sample the plot systematically (Fig. 1). The trees coinciding with the grid nodes were taken as sampling points. Grid size was previously defined by variographic analysis of the apparent electrical conductivity (ECa) data provided by a Veris 3100 soil sensor (Veris Technologies, Inc., Salinas, KS, USA) from an onthe-go survey of the plot. Once a strong autocorrelation of the ECa data was verified, half of the variogram range (ArcGIS 10.4.1 software) was taken as the optimum distance between sampling points (Kerry et al. 2010). On the other hand, to avoid border effect, no sample sites were positioned in a buffer zone of 15 meters from the limits that separated other plots (short sides of the rectangular shape of the plot). However, this buffer zone was not applied on the sides alongside with other fields because the cultivated peach variety and the canopy training system were the same in these adjacent plots. 

In total, 104 trees (sampling points) were defined (Fig. 1), and the number of fruits was counted manually in each tree four weeks before harvest. As proposed by Miranda and Royo (2003), yield in fruit orchards is usually measured in terms of fruit load (number of fruits per tree). As 

9 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

yield (kg/tree) basically depends on fruit load, the latter was the variable used in this work. Covering the entire plot, these 104 trees were taken as a reference population on which to compare two sampling methods. 

## _2.3. Basics of the sampling methods_ 

## 2.3.1. Simple random sampling (SRS) 

The size of the sample was initially set at _N_ = 12 trees or sampling points. Randomly selected without replacement, each of the twelve measured fruit load values could be considered representative of the population (or parcel under study), and with identical probability of choice. Therefore, the mean of the sample allowed the average number of fruits per tree to be estimated without bias. However, there was a possibility that such a mean did not provide a truly representative picture of the orchard mean (Wolfe 2010). 

## 2.3.2. Ranked set sampling (RSS) 

Ranked set sampling is not a new method. Initially developed by McIntyre (1952), the method was proved to be effective in improving the efficiency of pasture sampling. In this work, making use of adequate ancillary information (necessary for the ranking mechanism as it has been previously mentioned), the method was updated to evaluate its use in fruit growing. 

Briefly, the method is based on an iterative sampling process (Wolfe, 2010). Following the procedure for a sample size _N_ = 12, a first sample of size _k_ = 12 was taken randomly without 

10 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

replacement from the 104 trees initially marked within the plot, and then the 12 selected trees were arranged according to some attribute (ranking mechanism). This process of sorting the sampled trees allowed a ranking to be established, usually from the lowest to the highest presence of the selected attribute. In our case, the attribute used in the ranking mechanism was an ancillary variable (or secondary variable) that, being related to the number of fruits per tree (as a relevant component of yield), should also be easy to measure and at an affordable cost. The individual (tree) with the lowest value in this ranking was finally included as the first item in the ranked set sample, and the property of interest (fruit load) was formally considered only for this unit and denoted by 𝑌[?]. The remaining _k_ -1 observations were discarded in this without replacement strategy first sampling step. 

In a second iteration, another sample of _k_ = 12 observations was again selected without replacement and ranked following the same procedure as before. The individual (tree) ranked as the second smallest attending the attribute (ancillary variable) was now chosen, providing a second number of fruits value 𝑌[@] that was added to the sample. The process was repeated until obtaining _N_ = 12 measured observations 𝑌[?], 𝑌[@], ⋯, 𝑌[B] that constitutes a balanced ranked set sample of size _N_ . 

The mean of the _N_ values (ranked set sample mean) is, like SRS, an unbiased estimate of the population mean (Takahasi and Wakimoto 1968). However, having applied a ranking mechanism, each of the individual sample items in a balanced RSS represented a very distinctly different portion of the underlying population. Figure 2 represents this situation. The histogram represents the actual distribution of the number of fruits per tree (fruit load) in the plot under study (approximately, normal). Obtaining a sample through SRS involves sampling within that 

11 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

normal population (red curve in Fig. 2), and non-representative sample values may be drawn. Instead, using a perfect ranking mechanism (since the ancillary variable that provides the attribute is well correlated with the fruit load), each of the observations included in the RSS behave like mutually independent order statistics, with densities that can be represented by the individual marginal density curves in Figure 2 (in this case, _k_ = 6). Therefore, because of this extra structure provided by the judgment ranking (Wolfe 2004), RSS observations were much more likely to represent the full range of variation to estimate the population mean in a more effective way. This procedure is probably better than or equivalent to stratifying according to the probability distribution of the ancillary variable (stratified sampling based on the distribution of the percentiles). Adopting the previous notation for a sample size _N_ = 12, the mean was calculated using (1), 

**==> picture [458 x 19] intentionally omitted <==**

12 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Fig 2** Distribution of the fruit load (histogram of the 104 trees sampled), normal density curve 

(in red) and the individual marginal densities of six order statistics 𝑌[?], 𝑌[@], 𝑌[G], 𝑌[H], 𝑌[I], 𝑌[J] (solid curves, in order of peaks, from the minimum, 𝑌[?], on the left to the maximum, 𝑌[J], on the right) for a random sample of size 6 from the normal distribution. Figure adapted from Wolfe’s (2010). 

Regarding the variance, Wolfe (2010) provided the formula (2): 

**==> picture [458 x 20] intentionally omitted <==**

where 𝜇[%]∗ = 𝐸"𝑌[%]', for 𝑗= 1, … , 𝑁. Since ∑B%F?"𝜇[%]∗ −𝜇'@ ≥0, it follows from Eq. (2) that the variance of the RSS mean (𝑌CDD[) is, at most, equal to the variance of the SRS mean (][𝑌] DCD[). ] 

13 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Therefore, the RSS mean is, theoretically, a more precise estimator of the population mean 𝜇 than the SRS mean based on the same number of measured observations. The reliability of the ∗ judgment ranking process in separating order statistic expectations 𝜇[%] is a key in improving 

the efficiency of the RSS compared to the SRS, providing the ancillary variable is highly correlated with the fruit load. 

## _2.4. Ancillary variables in the ranking mechanism_ 

In this section, the most relevant characteristics of the ancillary variables used to rank sampled trees are shown. Both terrestrial and remote sensors, whether used or recently introduced in the framework of precision agriculture, were considered to provide these data. Table 1 shows the platforms and sensors tested with additional indication of the ancillary information provided as well as a first assessment of the technical difficulty to obtain and process the data. 

14 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Table 1** Sensors and ancillary information that were evaluated for the ranking of sampled trees in the RSS method. 

|**Acquisition**|**Sensor**|**View of the**|**Ancillary**|**Geometry-**|**Reflectance-**|**Obtaining**|
|---|---|---|---|---|---|---|
|**platform**||**canopy**|**information**|**based**|**based**|**process**|
|ATV|Veris 3100|Soil sensor|(B) shallow ECa|||ME|
||||(C) deep ECa|||ME|
|ATV|OptRx|Lateral view|(D) NDRE||X|ME|
||||(E) NDVI||X|ME|
|UAV|RGB|Nadir|(F) Tree canopy|X||ME|
||camera||perimeter||||
||||(G) Tree canopy|X||ME|
||||projected area||||
|Airplane|DMSC|Nadir|(H) NDVI||X|ME|
||||(I) NDVIC|X|X|HG|
||RGB||(J) Tree canopy|X||ME|
||camera||perimeter||||
||||(K) Tree canopy|X||ME|
||||projected area||||
|Terrestrial|MTLS|Lateral view|(L) Canopy impacts|X||HG|
|platform|||(M) Canopy volume|X||HG|
||||(N) Canopy volume|X||HG|
||||(O) Canopy volume|X||HG|



ATV (All-Terrain Vehicle); UAV (Unmanned Aerial Vehicle); DMSC (Digital MultiSpectral Camera); MTLS (Mobile Terrestrial Laser Scanner); ECa (apparent electrical conductivity); NDRE (Normalized Difference Red Edge); NDVI (Normalized Difference Vegetation Index); NDVIC (corrected value of the NDVI); ME (moderately easy); HG (hard to get) 

15 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## 2.4.1. Apparent electrical conductivity (ECa) 

Soil apparent electrical conductivity (ECa) was measured using a Veris 3100 (Veris Technologies, Inc., Salina, KS, USA). The soil survey was conducted on March 1st, 2016, when the soil had moisture content close to field capacity. Passing through all the alleyways within the plot, two simultaneous measurements of ECa were recorded: shallow ECa (0-30 cm) and deep ECa (0-90 cm). ECa measurements were georeferenced using a Trimble AgGPS332 GPS with SBAS differential correction (EGNOS system). An acquisition frequency of 1Hz was used giving approximately 750 sampling points per hectare. 

Two ECa raster maps (shallow and deep) were then obtained by ordinary kriging interpolation on a 1 m grid. By superimposing the layer of 104 polygons corresponding to the 104 trees within the plot, the respective values of shallow ECa (variable B, Table 1) and deep ECa (variable C, Table 1) were extracted. The mean ECa value was calculated for each tree at each surveying depth. 

## 2.4.2. Tree canopy projected area and tree canopy perimeter 

Tree canopy projected area and tree canopy perimeter were obtained by processing two images acquired from two different platforms: airplane and unmanned aerial vehicle (UAV). Both images were acquired on May 16, 2016, approximately at mid-day and under clear sky conditions. 

Each platform had its own camera. For the UAV, images were grabbed with a 16 MP Panasonic 

16 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

GX 7 camera (Panasonic Corporation, Osaka, Japan) with a 20 mm “pancake” lens coupled on a Mikrokopter Oktokopter 6S12 XL eight rotor UAV (HiSystems GmbH, Moomerland, Germany). The UAV was handled in manual configuration at constant speed of 18 km·h[-1] and constant altitude up to 100 m. Pitch and roll movements were minimized using MK HiSight SLR2 gimbal support equipped with two servo motors. The camera was configured to take an image every two seconds during the flight, being the autofocus activated and the exposure fixed. Nadir images were pre-selected to obtain an orthomosaic image with a spatial resolution of 2 cm per pixel using Agisoft Photoscan Professional software (Agisoft LLC, St. Petersburg, Russia). 

Regarding the airplane image, a 4-band digital multispectral camera (DMSC) was used allowing images centred at 450 nm (blue), 550 nm (green), 675 nm (red) and 780 nm (near infrared) to be acquired. The images were pre-processed by SpecTerra (SpecTerra Services Pty Ltd, Leederville, Western Australia) to correct lens aberration, and adjust scene brightness by the bidirectional reflectance distribution function (BRDF). At the moment of photographing the plot, the airplane was flying at an altitude of 2000 m. The spatial resolution of the pre-processed image was 25 cm per pixel. The aircraft used was a CESSNA 1725 Sky Hawk operated by RS (RS Servicios de Teledetección SL, Lleida, Spain). 

In both cases, images were processed by manually delimiting each of the 104 individual trees sampled within the plot. The polygons used to delimit the projected canopies to the ground allowed the area and the perimeter of each tree canopy to be calculated. Table 1 shows the four variables (symbolized with a capital letter) that were used as ancillary information on the canopy's geometry: airplane-based canopy perimeter (J), airplane-based canopy projected area 

17 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## (K), UAV-based canopy perimeter (F), and UAV-based canopy projected area (G). 

## 2.4.3. Tree canopy reflectance 

The aerial image provided by the multispectral camera (NDVI image, Rouse Jr et al. 1974) was post-processed according to the following procedure. First, and having eliminated the NDVI pixels with values lower than 0.45 to discard other land covers (i.e. bare soil) that were not tree canopy, all the trees (or canopies) within the plot were then easily delimited by using automatically defined polygons. Specifically, 1816 trees were individualized this way. Then, in a second step, NDVI pixels within each polygon (or canopy) were extracted by overlapping the NDVI image and the polygon layer. The average value of NDVI was then calculated and assigned to the centroid of each polygon. The third step consisted in creating a continuous map (or surface map) by interpolation (ordinary kriging) of the average NDVI values of the centroids. By superimposing this new NDVI map (1 m pixel resolution) with the polygons corresponding to the 104 trees, an average value of NDVI for each tree was obtained. This ancillary information was denoted with the letter H (Table 1). As with the previous maps for the other sensors, ArcMap 10.4.1 (ESRI, Redlands, CA, USA) performed spatial data analysis. 

On the other hand, it is worth mentioning that the single information of the NDVI could be inconsistent with the expected fruit load of a tree. The bigger the canopy, the higher the expected fruit load (Mann et al. 2011). However, average NDVI could take similar values in trees of different sizes. With this in mind, formula (3) was used to correct values of the NDVI to be obtained for each tree (variable I, Table 1), 

18 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**==> picture [458 x 21] intentionally omitted <==**

where NDVI and NDVIC were the initial value and the corrected value of the NDVI, respectively, TCA was the tree canopy projected area obtained from the airplane image, and TCAmax was the largest tree canopy projected area within the plot. 

Apart from the remote sensor, a terrestrial OptRx sensor (Ag Leader Technology, Ames, IA, USA) was also used to acquire canopy reflectance data using an all-terrain vehicle (ATV) as a platform. Since the readings were taken sideways passing through the alleyways of the orchard, data referred to the lateral reflectance of the canopy. Specifically, the sensor was maintained at a distance of approximately 1 m from the canopy and moved at a constant speed of 5 km·h[-1] . With the OptRx, only one side of each row was measured. Three different wavelengths were acquired every second (1 Hz) in the ranges of red (670 nm), red edge (728 nm), and near infrared (775 nm). So, the Normalized Difference Vegetation Index (NDVI) and the Normalized Difference Red Edge (NDRE) were finally obtained and georeferenced by also acquiring the position using a Trimble AgGPS332 GPS with SBAS differential correction (EGNOS system). An average of 169 data per row was obtained. Then, following the same procedure as before, the NDVI and NDRE data were interpolated by ordinary kriging to obtain two surface maps with a final resolution (grid) of 1 m for each vegetation index. By superimposing the surface maps with the layer of 104 polygons, the average values of NDVI and NDRE were obtained and denoted as variables E and D, respectively (Table 1). The date of the terrestrial sensor measurements was May 17th, 2016. 

19 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## 2.4.4. Tree volume 

The use of a MTLS allowed four different ancillary variables to be obtained. The sensor used was a UTM30-LX-EW time-of-flight LiDAR (HOKUYO, Osaka, Japan) that could perform 40 scans per second (40 Hz). In addition to this 2D LiDAR sensor, the MTLS integrated a GPS1200+ (Leica Geosystems AG, Heerbrugg, Switzerland) RTK-GNSS system (a real-time kinematics global navigation satellite system receiving GPS and Glonass constellation signals). So, after processing all data, the MTLS provided measurements of the position of the impact points produced between the laser beam and the canopy. These georeferenced impacts formed a point cloud that was then analyzed to calculate the canopy volume. A more detailed description of features, components for acquisition and field use methodology can be found in Escolà et al. (2017). 

Like the OptRx sensor, the MTLS laterally scanned the canopies of all the rows within the plot, but in this case, each row was measured from both sides to obtain a point cloud representative of the entire canopy. Point cloud visualization and specific computations were performed with CloudCompare (CloudCompare [GPL software] v2.6.1 2015). In short, the 3D point cloud was first classified into canopy and ground points. Points located at a height less than 0.4 m above the ground were discarded to eliminate weeds and ridges. The remaining points were then processed to individualize each tree trying to eliminate possible impacts (outliers) that were clearly outside the canopy (presenting positions more than 2.5 standard deviations away from 6 neighboring points). 

20 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Once the cloud of impact points for each tree was delimited (in our case, 104-point clouds), the first variable that was obtained was the number of canopy impacts (variable L, Table 1). CloudCompare ‘octree’ allowed the cubical initial volume including the entire canopy for each tree to be recursively divided into smaller cubes until visually adjusting the actual volume of the canopy. Adding the unit volume of each adjusted cube or voxel (VOlumetric piXEL), the final volume of the canopy in m[3] was obtained. Depending on either how the voxel size was set, manually or automatically, two different volumes could be obtained. The variable M (Table 1) referred to manually adjusted voxels, while the variable N (Table 1) estimated volume by adjusting a voxel size given by default parameters of the software. 

The last volume (variable O, Table 1) was calculated using the '2.5D Volume' tool in the CloudCompare software. Having projected the point cloud for a specific tree on the XY plane (Z-axis projection direction), this tool allowed the volume between the 2D rasterized cloud and the ground surface (taken as arbitrary plane) to be computed. As multiple points of the canopy could fall inside each cell, the maximum height was taken for calculation. 

Obviously, other methods could have been used to calculate the volume from LiDAR point clouds (Escolà et al. 2017). However, the special structure of the 'Catalan' vessel training system, open with branches in different directions and large gaps inside the canopy, could make it more convenient to use the voxelization procedure as proposed by Underwood et al. (2016) in almond. The readings with MTLS system were made on May 17th, 2016. 

21 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## _2.5. Evaluating the efficiency of sampling methods_ 

To compare the SRS versus the RSS, _B_ ( _B_ = 1000) realizations of selecting a sample with size _N_ , with _N_ ranging from 4 to 12 were resampled each time and for each method, with the sampling population being the 104 trees systematically sampled within the plot. By calculating the sample mean (average number of fruits per tree) for realization _i_ , 𝑌<[, the variance of the ] distribution of means for the SRS scheme was computed according to Nane and Kooijman (2018) using expression (4), 

**==> picture [458 x 21] intentionally omitted <==**

where _B_ = 1000 was the number of realizations in the resampling method, 𝑌<[ was the sample ] mean of the fruit load, and 𝑌[.] was the average fruit load for the 104 trees previously sampled covering the entire area of the plot (𝑌[.] = 144.7 fruits per tree). The latter was considered the representative value of the plot (or best estimator of the population mean), and it was practically coincident in all the resampling processes with the average of the 1000 means (data not shown). The finite population correction factor was given by 1 −𝑓, with 𝑓= 𝑁104⁄ defining the sampling fraction. 

22 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

The variance of the mean (𝑌CDD[) of a ranked set sample from a finite population was obtained ] by the formula (5) (Kowalczyk, 2004), 

**==> picture [458 x 22] intentionally omitted <==**

where _N_ and 𝑌[.] had the same meaning as before, and 𝑆[@] was the known variance of the total trees (104) sampled within the plot. To estimate each of the expected values, 𝐸"𝑌[%]', the mean over _B_ = 1000 bootstrap realizations for each of the corresponding ranked yield values _j_ (𝑗= 1, … , 𝑁) was applied. 

Both sampling methods (SRS and RSS) provided an unbiased estimate of the population mean (in this case, of the average of the 104 trees used as a representative measure of the plot mean). So, in both cases, the mean squared error ( _MSE_ ) equals the variance. The inverse of the variance is a measure of the precision, thus for a given sample size _N_ the two sampling methods were compared using the so-called relative efficiency, _RE_ (6), 

**==> picture [458 x 25] intentionally omitted <==**

once obtained 𝑣𝑎𝑟"𝑌DCD['][ and ][𝑣𝑎𝑟"𝑌] CDD['][ by (][4][)][and][(][5][). ] _[RE]_[ values greater than 1 would be ] expected (Chen, Bai and Sinha 2004), showing that RSS would be more precise (or more efficient) than SRS. At worst (Webster and Lark 2013), 𝑅𝐸= 1 when the ranking process is completely imperfect, that is, there is no correlation between the fruit load and the ancillary variable used to rank the realizations. Also, as Wolfe (2010) points out, good concomitant 

23 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

information is necessary to avoid error-prone ranking. 

Two additional efficiency indicators were computed. First, a predicted Coefficient of Error ( _CE_ ) for each method was obtained using equation (7), 

**==> picture [458 x 30] intentionally omitted <==**

being ), the standard deviation of the mean. Having formulated the sampling error of p𝑣𝑎𝑟(𝑌 *+,[-+.][*] one realization as 𝜀"𝑌<[' =] +[.] × 100, being 𝑌<[ the mean of the realization and ][𝑌.][ the ] aforementioned reference mean for the plot, the last indicator allowed the number of realizations of a given sampling design and sample size _N_ with sampling error greater than 10%, 𝑛_𝜀"𝑌<[' > 10%`][, to be computed in percentage terms over the total of the 1000 realizations ] (8), 

**==> picture [458 x 22] intentionally omitted <==**

Note that this procedure was also used to test the optimal ancillary information to run the RSS. For this, the resampling of _B_ = 1000 realizations of size _N_ = 12 using each auxiliary variable shown in Table 1 was used. Indices defined by equations (7) and (8) were used to compare the different auxiliary variables used in the ranking mechanism to provide an estimate of the fruit load. In all cases, resampling was performed by programming in R software, version 3.3.2. 

24 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## **3. Results and discussion** 

## _3.1. Relationship between fruit load and the acquired ancillary variables_ 

Figure 3 shows the scatter plot defined by the first two factors of a principal component analysis (PCA) showing the correlation between the ancillary variables altogether and fruit load. By the two factors, 65.9% of variability is explained. In summary, many of the ancillary variables were well summarized by the two first components of the PCA allowing two sets of variables to be discriminated. 

The variables with the highest correlation to the first component, apart from the fruit load (variable A), were those obtained using remote sensing (UAV and airplane using RGB and multispectral cameras) and MTLS. So, the first component was basically related to the geometry and vigor of the trees. The soil apparent electrical conductivity (shallow and deep values) was correlated to component 2 instead of component 1. In short, component 2 should be interpreted as related to soil variability. Finally, NDVI and NDRE vegetation indices obtained from the OptRx proximal sensor were not clearly included in any of the previous groups (therefore, they showed a weak correlation with both components). As has been mentioned before, "Catalan" vessel is the adopted training system which favours open canopies to improve solar exposure in detriment of the lateral side. In short, a vegetation wall is not easily measurable from the lateral side of the canopy. Because of that, the field of view of the canopy varies between sensors (lateral from terrestrial platform and nadir from aerial platform), and NDVI readings are surely affected. Probably, the best correlation with nadir vision is due to better cover the full size of the canopy. 

25 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Fig 3** Scatterplot showing the correlation between the ancillary variables and fruit load (variable A) with respect to the two principal components of PCA. 

Relevant information about the relationship between fruit load and all other variables was contrasted visually by the scatterplot of a PCA (Fig. 3). The surprising weak correlation between the number of fruits (variable A) and component 2 made it unwise to use the Veris sensor and the ECa as ancillary information in RSS schemes. This weak correlation was not expected when systematic sampling was designed, according to the findings of other authors in fruit growing (Käthner and Zude-Sasse 2015). In spite of this, variability at plot scale was also captured by covering the whole area of the orchard. The weak correlation could be due to drip fertigation allowing roots to grow in a controlled environment with little final soil influence (taking ECa readings in the alleyways outside the wet bulb) on canopy and fruit load (Uribeetxebarria et al. 2018). There being little correlation between ECa and fruit load, the 

ranking process may not be optimal to obtain a sample with the additional information needed for a more efficient estimation of the mean. Figure 3 also shows a nearly zero relationship between fruit load and variables D and E obtained by the OptRx sensor. For this reason, its use 

26 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

in RSS was rejected. However, the variables correlated to component 1 could be of interest. In short, the options for ancillary data to be used were limited to three data sources, i) RGB cameras mounted on remote acquisition platforms (UAV and airplane, variables F, G, J and K), ii) airplane images supplied by DMSC (variables H and I), and iii) MTLS point clouds (variables L, M, N and O). The close spatial arrangement within component 1 (Fig. 3), including fruit load, helped in this interpretation. 

Going into detail (Fig. 3), variable H (airplane-based NDVI) was the ancillary information with apparently the weakest correlation to fruit load among the variables of component 1. While variable H was only based on reflectance, the other variables were mainly based on geometric parameters. Even so, all the variables that were grouped as mostly correlated with component 1 were selected in order to analyze their convenience as ancillary variables in the next section. With respect to the volume of the canopy, only the data calculated with the tool 'Volume 2.5D' (variable O) were considered to avoid redundant information 

## _3.2. Ancillary information to be used in RSS to improve fruit load estimates_ 

Table 2 shows the results of linear correlation between the number of fruits per tree (variable A) and the most relevant ancillary variables within component 1. As expected, the best correlation was obtained using the UAV-based canopy projected area (variable G) with a value of the linear correlation coefficient of 0.85. The worst result (coefficient of 0.21) corresponded to the airplane NDVI (variable H). The rest of the variables ranging between these two extreme values (Table 2). 

27 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Table 2** Assessment of RSS efficiency according to the ancillary variables used in the ranking mechanism. Variables are ordered according to their correlation with fruit load. 

||**R**|𝑴𝑺𝑬"𝒀<br>'|𝑴𝑺𝑬"𝒀<br>'|𝑪𝑬"𝒀<br>'|𝑪𝑬"𝒀<br>'|**_PR_**|
|---|---|---|---|---|---|---|
|UAV-based canopy projected area (G)|0.85|69.10||5.74||10.1|
|LiDAR-based canopy volume (O)|0.68|92.62||6.65||16.4|
|LiDAR-based canopy impacts (L)|0.60|120.04||7.57||21.3|
|Airplane-based canopy projected area|0.55|130.59||7.89||21.1|
|(K)|||||||
|Airplane-based canopy perimeter (J)|0.54|131.51||7.92||22.8|
|Airplane NDVIC(I)|0.52|133.56||7.98||17.3|
|UAV-based canopy perimeter (F)|0.49|140.97||8.20||22.1|
|Airplane NDVI (H)|0.21|167.23||8.93||26.9|



R - Pearson’s linear correlation coefficient _MSE_ – Mean squared error (or mean variance) _CE_ – Coefficient of error _PR_ – Percentage of realizations exceeding the error threshold of 10% 

As expected, Table 2 shows that _MSE_ values follow exactly the same order as the correlation coefficient showing that the higher the correlation, the lower the error in fruit load prediction with the RSS. The trend of the Coefficient of Error (𝐶𝐸) was similar, going from 5.74% when the ancillary variable was the UAV-based canopy projected area to 8.93% using the airplane NDVI to rank items within the samples. Since a _CE_ of 10% may be acceptable in the fruit production sector, any of the ancillary variables could be candidates to be used in RSS schemes. However, it is also true that the sample size used in the comparison ( _N_ = 12) is not usual in practice, and has undoubtedly contributed to improve the efficiency in fruit load estimates above what is expected. Hence, it is necessary to check how the efficiency varies by reducing the sample size closer to the usual sizes used by fruit growers. 

Table 2 also shows the percentage of times the sampling error exceeded the 10% threshold considering 1000 realizations with a sample size _N_ = 12. This probability is a way of knowing 

28 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

the risk assumed by fruit growers since they usually perform a single sampling. Values ranged from 10.1% (variable G) to 26.9% (variable H), and corroborate the results of _MSE_ and linear correlation. The maximum difference between ancillary variables was 166% for this parameter ( _PR_ ), being 55% for the _CE_ . 

On the other hand, the results shown in Table 2 were in accordance with what was noticed by Nahhas et al. (2002) and Stokes (2007) when applying RSS. The better the correlation between the variable to be estimated (number of fruits per tree, in our case) and the concomitant variable (or ancillary variable) used in the ranking process, the better the sampling efficiency. 

Apart from good efficiency results, the ancillary variable to be used must be easily measurable. RGB cameras embedded in UAV meet this requirement. The use of UAV in precision agriculture is a booming and low-cost technology as suggested by Lelong et al. (2008). For this reason, the UAV-based canopy projected area (variable G, Tables 1 and 2) was finally chosen as the optimal ancillary variable to use in RSS schemes in fruit growing. The advantage of this variable is the high resolution of the images compared to other remote data sources. 

## _3.3. Resolution of ancillary variables in RSS: the key factor_ 

In peach orchards, fruit production and quality are clearly influenced by canopy lighting conditions (Tang et al. 2015; Minas et al. 2018). Seeking to enhance floral induction and fruit growth, fruit growers adopt canopy open-center training systems (such as the typical 'Catalan' peach vessel) to maximize exposure to solar radiation. In this way, peach trees with larger canopy projected area usually have a greater number of larger fruits (Marini 2002). In addition, 

29 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

the incidence of unproductive interior branches is lower, avoiding what usually happens in canopies formed into traditional or spherical vessels (Marini et al. 1995). In RSS, an ancillary information system that manages to individualize the canopy of trees in a precise manner will be essential, i) to ensure an optimal and accurate ranking process of the auxiliary variable, and ii) to cover all the variability of the objective variable (number of fruits) (Fig 2). 

Continuing the thread of the previous paragraphs, variables that best meet previously mentioned characteristics are those based on geometrical properties of the canopy (Table 2). UAV-based canopy projected area (variable G) was the best rated ancillary variable. In contrast, LiDARbased canopy volume (O) or impacts (L) and airplane-based canopy projected area (K) obtained less satisfactory sampling efficiency results. What could be the reason for this difference? Probably, the lack of resolution (57528 impacts per tree) is not the main reason for a lower correlation of LiDAR derived variables with fruit load. The lowest correlation comes from the different orientation of each sensor. While the RGB camera mounted on UAV (variable G) provides a top view of the canopy, MTLS provides a lateral view of the trees. The top view allows the area exposed to sunshine to be more precisely delimited. The efficiency when intercepting the sunrays is the key factor for transpiration and photosynthesis, therefore it is strongly related to the fruit load (Da Silva et al. 2014). 

Figure 4A shows the canopy of a peach tree as it is captured with an aerial image from airplane (0.25 m per pixel), and the same canopy when it was captured using UAV and resolution of 0.02 m (Fig. 4B). The difference is obvious. While the delimitation of the canopy projected area was more difficult using the airplane image, the UAV-based canopy projected area allowed the actual canopy projected area to be better defined. This would explain why the use of higher 

30 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

resolution images should lead to more accurate tree ranking processes and more efficient fruit load estimates. To provide an explanatory example, 45 pixels were needed on average to characterize the canopy projected area using the airplane image instead of the 6500 pixels for the UAV image. In other words, the average area of 2.60 m[2] per tree using the higher resolution image became an area of 2.81 m[2] when a larger pixel size was used. The difference was therefore 8%, although large deviations for some trees could be obtained (maximum differences of up to 53% between UAV and airplane were found). Because of that, the use of images of poor resolution can alter the ranking process. In fact, ranking of individuals varied (data not shown) according to the resolution of the ancillary variable that was used (for example, G or K). The moderate Spearman correlation coefficient (0.71) between both variables allowed this property to be concluded. 

**Fig 4** Comparison of tree canopy projected area delimited for the same peach tree, A) using an airplane-based image of 0.25 m per pixel (top view), B) using an UAV-based image of 0.02 m per pixel (top view), C) 3D reproduction of the same canopy using an MTLS (side view). 

31 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

MTLS are another different technology that allows canopy of trees to be characterized with high operative resolution. Figure 4C shows the point cloud obtained from a lateral LiDARbased scan of the same tree. Then, by 3D processing of all the data, a canopy volume expression can be obtained (variable O, Table 2). However, this parameter did not provide results as good as those obtained using the simplest UAV-based tree canopy projected area (variable G). Finding an explanation is not easy. Probably, sunlight penetration is optimal in trees with more open canopy resulting in a larger projected area. Conversely, bulky trees with smaller projected areas could have grown in height instead of laterally and more openly. This could hinder the interior lighting of the canopy and negatively affect the amount of viable fruits and yield. 

Figure 5 helps to understand this phenomenon. While the two trees shown (number 104 and number 45) have similar canopy volume (3.91 m[3] and 3.83 m[3] , respectively), the canopy projected area (3.92 m[2] and 2.40 m[2] ) and fruit load (201 fruits and 124 fruits) are very different. In fact, the correlation between canopy projected area (variable G) and fruit load is higher (R = 0.85) than the correlation between canopy volume (variable O) and fruit load (R = 0.68). 

**Fig 5** Aerial projection of tree 104 (left) and 45 (right) obtained from the LiDAR-based MTLS 

system. 

32 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

The use of NDVI showed acceptable results when adjusting the value of the vegetation index according to the tree canopy projected area. However, the exclusive use of the airplane NDVI (variable H, Table 2) was the least recommended option. The resolution of the airplane images was lower than that of UAV images or MTLS point clouds and, in addition, the reflectance alone does not account for any geometrical parameters of the canopy. In any case, the weak correlation between fruit load and NDVI is also noted in other sampling studies (Arnó et al. 2017; Miranda et al. 2018). 

Concluding, resolution of acquired ancillary data was the main constraint in reliably delimiting canopy of trees (Fig. 4). UAV-based RGB images offered high resolution at competitive costs, and good correlation with the fruit load (Table 2). Therefore, RSS was only tested with UAVbased tree canopy projected area as the ancillary information. Comparison of sampling efficiency against SRS is addressed in the next section. The pending issue is to test the method in other orchards trained under systems that are more intensive forming a fruiting wall structure. Probably in this case, sections of wall vegetation rather than individualized trees should be delimited using an appropriate algorithm and a more automated method. 

## _3.4. RSS versus SRS: sampling efficiency and sample size_ 

Table 3 shows the mean squared error ( _MSE_ ), and the relative efficiency ( _RE_ ) of RSS versus SRS for different sample sizes (4 to 12 points or trees sampled within the plot). A resampling of 1000 realizations allowed such statistics to be calculated in order to compare the sampling methods. RSS was run in all cases using the UAV-based tree canopy projected area as ancillary variable to drive the ranking mechanism. 

33 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

**Table 3** Mean squared error ( _MSE_ ) and relative efficiency ( _RE_ ) of the sampling methods for different sample sizes. 

|SRS<br>RSS|Mean squared error (_MSE_)|
|---|---|
||_N_= 4<br>_N_= 5<br>_N_= 6<br>_N_= 7<br>_N_= 8<br>_N_= 9<br>_N_= 10<br>_N_= 11<br>_N_= 12|
||472.54<br>310.49<br>283.20<br>269.30<br>225.88<br>204.38<br>177.65<br>159.76<br>148.38<br>305.32<br>178.20<br>168.90<br>132.53<br>111.21<br>104.61<br>97.87<br>81.24<br>69.10|
|RSS vs. SRS|Relative efficiency(𝑅𝐸= 𝑣𝑎𝑟"𝑌<br>DCD' 𝑣𝑎𝑟"𝑌<br>CDD'<br>}|
||_N_= 4<br>_N_= 5<br>_N_= 6<br>_N_= 7<br>_N_= 8<br>_N_= 9<br>_N_= 10<br>_N_= 11<br>_N_= 12|
||1.55<br>1.74<br>1.68<br>2.03<br>2.03<br>1.95<br>1.82<br>1.97<br>2.15|



SRS (Simple random sampling), RSS (Ranked set sampling) 

In both cases, SRS and RSS, the _MSE_ decreased, as the sample size increased. As expected, the sampling methods became more efficient with an increasing sample size. However, comparatively, RSS always showed lower variance of the mean (lower _MSE_ ) than SRS. In short, RSS was more efficient than SRS for any of the sample sizes evaluated. Hence the _RE_ was higher than one (Table 3), ranging from 1.55 ( _N_ = 4) to 2.15 ( _N_ = 12). The fact of obtaining higher values of _RE_ for the larger sample sizes was possibly due to the RSS procedure. Takahashi and Wakimoto (1968) reported a loss of efficiency by decreasing the number of individuals checked in the ranking process for the same final sample size. This would explain why the _RE_ of the RSS increases with increasing sample size because a higher number of trees are ranked. Thus, by increasing the sample size ( _N_ = 7, 8 ... 12), RSS required progressively increasing the number of trees to rank to obtain the final sample. For example, a sample of size _N_ = 9 would suppose choosing 81 trees within the plot instead of the 25 (5[2] ) needed for _N_ = 5. In this way, additional information on fruit load structure was more easily achievable by having 

34 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

to select and assess a larger number of trees than the one obtained in small samples. As a result, the _RE_ of RSS increased compared to SRS strategy. 

Considering the UAV-based canopy projected area as ancillary information, RSS allowed more accurate fruit load estimates to be obtained. The extent to which this precision was improved was quantified by the _CE_ (Eq. 7) as shown graphically in Fig. 6. Additionally, Figure 6 shows the effect of the sample size on the _PR_ indicator for both sampling schemes. Both measures are important for fruit growers because they complement each other. Farmers collect samples at specific times during the life of the crop. Therefore, knowing the probability of exceeding the threshold and the average _CE_ for each sample size is important. Both curves ( _CE_ and _PR_ , Fig. 6) show a similar nonlinear trend. For all sample sizes, RSS has a lower _CE_ than SRS. Specifically, while in SRS the _CE_ ranged from 15.4% ( _N_ = 4) to 8.4% ( _N_ = 12), in RSS errors ranged from 12.1% ( _N_ = 4) to 5.7% ( _N_ = 12). From a practical point of view, SRS should be based on minimum sizes of _N_ = 10 while RSS can reduce sample sizes up to _N_ = 5 so as not to exceed a _CE_ threshold of 10% (Fig. 6). This meant that, using sample sizes _N_ = 10 in SRS or _N_ = 5 in RSS, a sampling error of less than 10% could be expected in practically 70% of the samplings ( _PR_ close to 30% in both cases, Fig. 6). Assuming normality, 68.3% of the samplings should provide errors of less than 10% (as it has been obtained approximately), although the RSS strategy only needed to sample 5 trees compared to the 10 trees needed in SRS. Likewise, SRS schemes exceed the error threshold of 10% with a higher percentage ( _PR_ , Fig. 6) compared to RSS for all the sample sizes that were analyzed. While for SRS, _PR_ values ranged from 53.5% ( _N_ = 4) to 25.5% ( _N_ = 12), in RSS the same parameter reached significantly lower scores, varying between 44.4% ( _N_ = 4) and 10.1% ( _N_ = 12). Therefore, using SRS practically doubles (for sample sizes greater than _N_ = 8) the probability of obtaining errors of estimation above the 

35 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

10% threshold than using RSS. However, for smaller sample sizes ( _N_ = 4), the difference between SRS and RSS was not so obvious. 

**Fig 6** Comparison of the Coefficient of Error and the percentage of times the sampling error threshold of 10% is exceeded according to the sample size for two sampling methods: SRS and RSS. 

SRS (simple random sampling). RSS (ranked set sampling). Resampling of 1000 realizations for each of the sample sizes was made, using the UAV-based tree canopy projected area as ancillary variable in the RSS. 

As mentioned before, if a _CE_ of no more than 10% was assumed, RSS allowed the sample size to be reduced to _N_ = 5 while the SRS required twice the sample ( _N_ = 10) (Fig. 6). Moreover, a sample size _N_ = 4 in RSS could even be justified by reaching an error around 12%. Undoubtedly, being able to reduce the sampling requirements, RSS could report favorable operative as well as economic consequences in fruit sampling as those obtained by Carrillo et al. (2016) in vineyard. Although RSS requires random sampling in each iteration to generate the final ranked sample, subjectivity (and, therefore, biased decisions) should not be applied during the ranking mechanism favoring a more automated (without farmers rating) and reliable sampling process. On the other hand, the ancillary variable being available, the method is even 

36 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

applicable in small plots like fruit orchards (Zude-Sasse et al., 2016), avoiding to perform a stratified sampling scheme. 

Looking for the reasons that make the RSS a strategy more adapted to non-homogeneous orchards, it was verified (data not shown) that, in average, the within-sample variability (measured as Coefficient of Variation) in the RSS realizations was always higher than that found in SRS of the same size. This would explain why the RSS manages to capture the heterogeneity of the orchards more reliably providing greater precision in yield estimates. 

Finally, it is necessary to point out that these values obtained for this orchard assume that the sampling variance on estimating mean fruit per tree due to a (in effect) selection of 104 trees as the first step can be considered negligible. In addition, these recommended sample sizes apply to this particular orchard with its spatial variability of fruit. They provide a starting point for considering sample sizes, and being prepared to be more conservative for orchards that are more heterogeneous. 

## **4. Conclusions** 

Ranked set sampling (RSS) is an interesting method to improve sampling in fruit growing. Improvements in the efficiency of peach fruit load estimates were proven by applying RSS compared to simple random sampling (SRS), at least for sample sizes from _N_ = 4 to _N_ = 12. However, to be optimal, RSS requires a relevant auxiliary variable, these data being the key factor in the procedure. Among different data sources currently available in agriculture, either commercialized or under development (such as MTLS), the UAV-based tree canopy projected 

37 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

area was identified in this study of a peach orchard as the best option to use in the ranking mechanism aiming at estimate fruit number in peach production. This information can be obtained from RGB cameras that providing high-resolution images allowing the projected area of the canopy (geometric parameter) to be accurately delimited. The close correlation between this area and the fruit load per tree made this the best choice as an auxiliary variable in RSS schemes for the particular management by the producer (open vessel training systems). 

In terms of the Coefficient of Error of the estimated mean, RSS using samples of size _N_ = 5 trees allows acceptable errors below 10% to be achieved with about 70% probability. In contrast, SRS requires practically doubling the sample needed for a similar error. Finally, it should be noted that the work has been carried out only on one plot, although it provides relevant information as the ancillary variable to be used in RSS for future research on a larger spatial scale. In fact, UAV-based tree canopy projected area is an interesting (cheap and easy to get) ancillary information. However, since the values of the variable are obtained manually, future research is required to automatically obtain this information by developing the appropriate algorithm. 

**Acknowledgments:** The Spanish Ministry of Economy and Competitiveness through the AgVANCE Project (AGL2013-48297-C2-2-R) funded this work. We are also grateful to Frutas Hermanos Espax SL for the possibility to carry out the research in their farm. 

38 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

## **References** 

- Aggelopoulou, K., Castrignano, A., Gemtos, T., Benedetto, D., 2013. Delineation of management zones in an apple orchard in Greece using a multivariate approach. Comput. Electron. Agric. 90, 119-130. 

Aggelopoulou, K.D., Wulfsohn, D., Fountas, S., Gemtos, T.A., Nanos, G.D., Blackmore, S., 2010. Spatial variation in yield and quality in a small apple orchard. Precis. Agric. 11, 538-556. 

- Araya-Alman, M., Acevedo-Opazo, C., Guillaume, S., Valdés-Gómez, H., Verdugo-Vásquez, 

   - N., Moreno, Y., Tisseyre, B., 2017. Using ancillary yield data to improve sampling and grape yield estimation of the current season. In: J. A. Taylor, D. Cammarano, A. Prashar, A. Hamilton (Ed.) Precision Agriculture’17, Papers presented at the 11th European Conference on Precision Agriculture, Adv. Anim. Biosci. 8 (2), 515-519. 

Arnó, J., Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A., Rosell-Polo, J.R., 2017. Comparing efficiency of different sampling schemes to estimate yield and quality parameters in fruit orchards. In: J. A. Taylor, D. Cammarano, A. Prashar, A. Hamilton (Ed.) Precision Agriculture’17, Papers presented at the 11th European Conference on Precision Agriculture, Adv. Anim. Biosci. 8 (2), 471-476. 

Arnó, J., Rosell, J.R., Blanco, R., Ramos, M.C., Martínez-Casasnovas, J.A., 2012. Spatial variability in grape yield and quality influenced by soil and crop nutrition characteristics. Precis. Agric. 13 (3), 393–410. 

39 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Berman, M.E., De Jong, T.M., 1996. Water stress and crop load effects on fruit fresh and dry weights in peach ( _Prunus persica_ ). Tree Physiol. 16, 859-864. 

- Carrillo, E., Matese, A., Rousseau, J., Tisseyre, B., 2016. Use of multi-spectral airborne imagery to improve yield sampling in viticulture. Precis. Agric. 17, 74-92. 

Chen, Z., Bai, Z., Sinha, B.K., 2004. Ranked Set Sampling. Theory and Applications. SpringerVerlag, New York, pp. 224. 

CloudCompare [GPL software] v2.6.1., (2015). http://www.cloudcompare.org. Accessed on July 25, 2017. 

- Cochran, W.G., 1977. Sampling Techniques. John Wiley & Sons, Inc, New York, NY, USA, pp.  428. 

- Da Silva, D., Han, L., Costes, E., 2014. Light interception efficiency of apple trees: a multiscale computational study based on MappleT. Ecol. Model. 290, 45-53. 

Escolà, A., Martínez-Casasnovas, J.A., Rufat, J., Arnó, J., Arbonés, A., Sebé, F., Pascual, M., Gregorio, E., Rosell-Polo, J.R., 2017. Mobile terrestrial laser scanner applications in precision fruticulture/horticulture and tools to extract information from canopy point clouds. Precis. Agric. 18, 111–132. 

Fountas, S., Aggelopoulou, K., Bouloulis, C., Nanos, G.D., Wulfsohn, D., Gemtos, T.A., 2011. Site-specific management in an olive tree plantation. Precis. Agric. 12, 179-195. 

ISPA Newsletter 7 (7) July 2019. (https://ispag.org/site/newsletter/?id=90). 29/07/2019. 

Käthner, J., Zude-Sasse, M., 2015. Interaction of 3D soil electrical conductivity and generative 

growth in _Prunus domestica_ L. Eur. J. Hortic. Sci _**.**_ 80 (5), 231-239. 

Kerry, R., Oliver, M.A., Frogbrook, Z.L., 2010. Sampling in Precision Agriculture. In M. A. Oliver (Ed.), Geostatistical Applications for _Precision Agriculture_ . Springer, New York, pp. 36-63. 

40 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Kowalczyk, B., 2004. Ranked set sampling and its applications in finite population studies. Statistics in Transition. 6 (7), 1031-1046. 

Lelong, C.C.D., Burger, P., Jubelin, G., Roux, B., Labbé, S., Baret, F., 2008. Assessment of unmanned aerial vehicles imagery for quantitative monitoring of wheat crop in small plots. Sensors. 8 (5), 3557–3585. 

Mann, K.K., Schumann, A.W., Obreza, T.A., 2011. Delineating productivity zones in a citrus grove using citrus production, tree growth and temporally stable soil data. Precis. Agric. 12, 457-472. 

Marini, R.P., Sowers, D.S., Marini, M.C., 1995. Tree form and heading height at planting affect peach tree yield and crop value. HortScience. 30 (6), 1196–1201. 

- Marini, R.P., 2002. Heading fruiting shoots before bloom is equally effective as blossom removal in peach crop load management. HortScience. 37 (4), 642–646. 

- Martinez Vega, M.V., Clemmensen, L., Wulfsohn, D., Toldam-Andersen, T.B., 2013. Using multilevel systematic sampling to study apple fruit ( _Malus domestica_ Borkh.) quality and its variability at the orchard scale. Sci. Hortic. 161, 58-64. 

- McIntyre, G.A., 1952. A method for unbiased selective sampling, using ranked sets. Aust. J. Agric. Res. 3, 385-390. (Reprinted in Am. Stat. 2005 _._ 59 (3), 230-232). 

Meyers, J.M., Vanden Heuvel, J.E., 2014. Research Note. Use of Normalized Difference Vegetation Index Images to Optimize Vineyard Sampling Protocols. Am. J. Enol. Viticult. 65, 250-253. 

Minas, I.S., Tanou, G., Molassiotis, A., 2018. Environmental and orchard bases of peach fruit quality. Sci. Hortic. 235, 307-322. 

41 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Miranda, C., Santesteban, L.G., Urrestarazu, J., Loidi, M., Royo, J.B., 2018. Sampling stratification using aerial imagery to estimate fruit load in peach tree orchards. Agriculture. 8 (6), 78. 

Miranda, C., Urretavizcaya, I., Santesteban, L.G., Royo, J.B., 2015. Sampling stratification using aerial imagery to estimate fruit load and hail damage in nectarine trees. In: J. V. Stafford (Ed.) Precision Agriculture’15, Proceedings of the 10th European Conference on Precision Agriculture: Wageningen Academic Publishers, Wageningen, The Netherlands, pp. 541-546. 

Miranda, C., Royo, J.B., 2003. A statistical model to estimate potential yields in peach before bloom. J. Amer. Soc. Hort. Sci. 128, 297–301. 

Monestiez, P., Audergon, J.M., Habib, R., 1990. Spatial dependences and sampling in a fruit tree: a geostatistical approach. Institut National de la Recherche Agronomique. Technical Report No. 163, pp. 30. 

Nahhas, R.W., Wolfe, D.A., Chen, H., 2002. Ranked set sampling: cost and optimal set size. Biometrics _._ 58, 964–971. 

Nane, T., Kooijman, K., 2018. A bootstrap analysis for finite populations. Cornell University. arXiv:1804.05274 [stat.AP]. 

Pearce, S.C., 1944. Sampling methods for the measurement of fruit crops. J. R. Stat. Soc. 107 (2), 117-126. 

Rosell, J.R., Llorens, J., Sanz, R., Arnó, J., Ribes-Dasi, M., Masip, J., Escolà, A., Camp, F., Solanelles, F., Gràcia, F., Gil, E., Val, L., Planas, S., Palacín, J., 2009. Obtaining the three-dimensional structure of tree orchards from remote 2D terrestrial LIDAR scanning. Agric. For. Meteorol. 149, 1505–1515. 

42 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Rouse Jr, J.W., Haas, R.H., Deering, D.W., Schell, J.A., Harlan, J.C., 1974. Monitoring the Vernal Advancement and Retrogradation (GreenWave Effect) of Natural Vegetation. Greenbelt, MD, USA, NASA/GSFC Type III Final Report, pp. 371. 

- Stokes, S.L., 2007. Ranked set sampling with concomitant variables. Commun. Stat. Theory. Methods. 6, 1207-1211. 

- Takahasi, K., Wakimoto, K., 1968. On unbiased estimates of the population mean based on the sample stratified by means of ordering. Ann. Inst. Stat. Math. 20, 1-31. 

- Tang, L., Hou, C., Huang, H., Chen, C., Zou, J., Lin, D., 2015. Light interception efficiency analysis based on three-dimensional peach canopy models. Ecol. Inform. 30, 60-67. 

- Taylor, J., Tisseyre, B., Bramley, R., Reid, A., 2005. A comparison of the spatial variability of vineyard yield in European and Australian production systems. In: J. V. Stafford (Ed.) Precision Agriculture’05, Proceedings of the 5th European Conference on Precision Agriculture: Wageningen Academic Publishers, Wageningen, The Netherlands, pp. 907915. 

- Ulzii-Orshikh, D., Lee, M., Sang-seok, Y., 2017. An yield estimation in citrus orchards via fruit detection and counting using image processing. Comput. Electron. Agric. 140, 103-112. 

- Underwood, J.P., Hung, C., Whelan, B., Sukkarieh, S., 2016. Mapping almond orchard canopy volume, flowers, fruit and yield using lidar and vision sensors. Comput. Electron. Agric. 130, 83-96. 

- Uribeetxebarria, A., Daniele, E., Escolà, A., Arnó, J., Martínez-Casasnovas, J.A., 2018. Spatial variability in orchards after land transformation: Consequences for precision agriculture practices. Sci. Total. Environ. 635, 343–352. 

- Webster, R., Lark, R.M., 2013. Field sampling for environmental science and management. Routledge, London and New York, pp. 192. 

43 

POSTPRINT  of  the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A., Tisseyre, B., Guillaume, S., Escolà, A., Rosell-Polo, J.R., Arnó, J. 2019. Assessing ranked set sampling and ancillary data to improve fruit load estimates in peach orchards. _Comput. Electron. Agric._ DOI: https://doi.org/10.1016/j.compag.2019.104931 

Wolfe, D.A., 2004. Ranked Set Sampling: An Approach to More Efficient Data Collection. Stat. Sci _._ 19 (4), 636-643. 

Wolfe, D.A., 2010. Ranked set sampling _._ Wiley. Interdiscip. Rev. Comput. Stat. 2 (4), 460- 

466. 

Wulfsohn, D., Aravena Zamora, F., Potin Téllez, C., Zamora Lagos, I., García-Fiñana, M., 2012. Multilevel systematic sampling to estimate total fruit number for yield forecasts. Precis. Agric. 13, 256–275. 

Zude-Sasse, M., Fountas, S., Gemtos, T.A., Abu-Khalaf, N., 2016. Applications of precision 

agriculture in horticultural crops. Eur. J. Hortic. Sci **.** 81, 78-90. 

44 

