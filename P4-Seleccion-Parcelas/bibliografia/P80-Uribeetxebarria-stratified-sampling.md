Document downloaded from: 

http://hdl.handle.net/10459.1/66090 

The final publication is available at: 

https://doi.org/10.1007/s11119-018-9619-9 

Copyright 

(c) Springer Science+Business Media, 2018 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

- 1 **Stratified sampling in fruit orchards using cluster-based ancillary information maps: a** 2 **comparative analysis to improve yield and quality estimates** 

- 3 

- 4 **Asier Uribeetxebarria[1] · José A. Martínez-Casasnovas[2] · Alexandre Escolà[1] · Joan R.** 5 **Rosell-Polo[1] · Jaume Arnó[1]** 

- 6 

- 7 Asier Uribeetxebarria (  ) 8 Uribeetxebarria.asier@gmail.com 

- 9 

- 10 1 Research Group in AgroICT & Precision Agriculture, Department of Agricultural and Forest 11 Engineering, University of Lleida - Agrotecnio Centre, Rovira Roure, 191, Lleida, 25198, Catalonia, 12 Spain 

- 13 

- 14 2 Research Group in AgroICT & Precision Agriculture, Department of Environmental and Soil 15 Sciences, University of Lleida - Agrotecnio Centre, Rovira Roure, 191, Lleida, 25198, Catalonia, 16 Spain 

- 17 

- 18 

- 19 

- 20 

- 21 **Abstract** Estimation of yield or other fruit quality parameter is of great interest to farmers to 22 decide on management actions just before harvesting and, in any case, to anticipate and plan 23 harvesting operations. Making accurate and reliable estimates often requires systematic 24 sampling that, when covering the whole plot, can result in the use of a large number of 25 samples and a significant effort in time and cost for fruit growers. Faced with this whole area 26 sampling strategy, simple random sampling (SRS) using reduced sample sizes is currently a 27 widely used technique despite the less precise estimates that it provides. In this work, 28 different stratified sampling schemes have been tested to estimate yield (kg/tree), fruit 29 firmness (kg/cm[2] ) and the refractometric index (ºBaumé) in a peach orchard located in 30 Gimenells (Lleida, Catalonia, Spain). In contrast to SRS, the use of ancillary information 31 (NDVI and apparent electrical conductivity, ECa) allowed sampling units or trees to be 32 stratified according to two or three classes (strata) within the plot. The classes or 33 homogeneous stratification zones were delimited by cluster analysis using, either separately 34 or in combination, a multispectral airborne image (NDVI) and a ECa survey map acquired by 35 means of a soil resistivity sensor (Veris 3100). Sampling schemes were then compared in 36 terms of efficiency. In general, stratified sampling showed better results than SRS. Regarding 37 yield estimates, stratified sampling according to two strata of NDVI allowed the sample size 38 to be reduced by 17% compared to the SRS for the same precision. On the other hand, quality 39 parameters may require different stratification strategies concerning the number of strata to be 40 used. While ºBaumé was better-estimated using also stratified samples based on two strata of 41 NDVI, fruit firmness showed better results when stratifying by three classes or strata of 42 NDVI. In any case, neither the ECa nor the combined use of NDVI + ECa have improved 43 sampling efficiency when used as ancillary maps for stratification. 

- 44 

- 45 **Keywords** Sampling efficiency · Fruit yield and quality · Peach · NDVI · Apparent electrical 46 conductivity 

- 47 

- 48 

49 

1 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

- 50 **Introduction** 

- 51 

- 52 Sampling to estimate yield and/or fruit quality at harvest time is of great interest in fruit 53 growing. However, reliable prediction of these parameters is not easy, especially when 54 systematic sampling is usually replaced by a less complex simple random sampling (SRS) to 55 reduce time and cost. In other occasions, random sampling raises doubts to both growers and 56 advisors about how many trees should be sampled and, above all, which specific ones should 57 be sampled within a plot. Facing this situation, there is a need to develop new and more 58 precise methods with acceptable costs to guide fruit growers during field sampling. SRS is a 59 widely used design, because it is relatively simple to implement by random selection of 60 sampling units (trees) within the plot. However, SRS is inefficient when estimating 61 parameters that show spatial autocorrelation within the plots (Webster and Lark 2013). Taylor 62 et al. (2005) and Kazmierski et al. (2011) showed that vineyards are spatially variable and that 63 grape yield usually follows well-defined and consistent spatial patterns over time. This same 64 situation can be expected in fruit orchards and, for this reason, sampling methods that take 65 into account the different areas within the plot with different expected yield values would be 66 preferable to optimally locate sampling trees to obtain better yield estimates. 

- 67 

- 68 On the other hand, fruit growers can hire service companies that provide crop vigour and/or 69 soil apparent electrical conductivity (ECa) maps obtained with suitable sensors (proximal and 70 remote sensing). Normalized difference vegetation index (NDVI) derived from airborne 71 images were used by Meyers and Vanden Heuvel (2014) to optimize sampling protocols in 72 vineyard and reduce sample sizes. Applying a heuristic optimization algorithm (Tabu Search 73 Algorithm) to NDVI images, specific samples to conform the spatial distribution of NDVI 74 within the plot can be established (Meyers and Vanden Heuvel 2014). As NDVI is related to 75 vine vigour, the method is a way for distributing sampling units by covering the areas of 76 different vigour to capture vineyard canopy variability within the plot. This idea is also 77 behind the method proposed by Carrillo et al. (2016) to improve grape yield estimates. The 78 authors concluded with the need to consider a two-step sampling method combining NDVI79 based samples with random vine samples to predict specific components of the productive 

- 80 potential in a vineyard. Regarding apparent electrical conductivity (ECa), there are several 81 studies that address the use of ECa classified maps for site-specific management practices 82 (Moral et al. 2010; Peralta and Costa 2013). The suitability of this information in fruit- 

- 83 growing sampling is a pending issue, although soil characteristics are expected to impact yield 84 and/or quality parameters. 

- 85 

- 86 There are few studies on sampling in fruit orchards. Monestiez et al. (1990) proposed a 87 geostatistical approach to assess spatial dependence between fruits to choose the most 88 appropriate sampling designs inside the tree structure. Multilevel systematic sampling can 

- 89 also be an interesting option to estimate the number of fruits for yield forecasts (Wulfsohn et 

- 90 al. 2012), obtaining error coefficients of only 10%. More recently, sampling stratification 

- 91 using NDVI-based aerial images allowed different areas to be better delimited for sampling in 92 nectarine orchards (Miranda et al. 2015), with a significant reduction in sample size (20-35%) 

- 93 compared to random sampling (Miranda et al. 2018). As is known, SRS can produce local 94 clusters of trees and leave unrepresented areas within a plot (Webster and Lark 2013 95 Alternatively, farmers can consider using NDVI or ECa data to stratify samples, assuming 96 that yield and quality parameters in orchards often present spatial autocorrelation and, what is 97 more important, possible spatial cross-correlation with ancillary variables supplied by 

2 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

98 proximal and remote sensors of increasingly common use in agriculture. Cross-correlogram is 99 a powerful tool to test the spatial correlation between two variables, and checking this spatial 100 correlation may be the key factor before stratifying the samples. 

- 101 

102 The aim of this study was to investigate how the use of ancillary data (NDVI and ECa) in 103 stratified sampling schemes can improve sampling efficiency compared to a SRS of equal size 104 for the whole of a plot. Efforts in time and cost could be reduced with this new sampling 105 strategy by optimizing sample sizes through the application of technological advances in the 106 framework of precision agriculture. Sampling in orchards is then proposed as a design-based 107 sampling strategy, making use of classical sampling theory (that is, assuming normality and 108 independence of observations). This may be a limitation in plots with spatial autocorrelation. 109 However, the use of geostatistical methods is beyond the scope of this paper. 

- 110 

- 111 

## **Materials and methods** 

- 112 

- 113 

## _Study plot_ 

- 114 

115 The research was conducted in a peach orchard ( _Prunus persica_ cv. ‘Platycarpa’) located at 116 the IRTA Experimental Station (41° 39’ 19” N, 0° 23’ 36” E, ETRS89) in Gimenells (Lleida, 117 Catalonia, Spain). The plot covered an area of 0.65 ha, and was planted in 2011 according to a 118 5 x 2.80 m pattern (Fig. 1). Soil was classified as Petrocalcic Calcixerept (Soil Survey Staff 119 2014), and it was a well-drained soil without salinity problems. The presence of a petrocalcic 120 horizon at a variable depth (0.4-0.8 m) and high CaCO3 content were the main soil limiting 121 factors. The horizon may be at shallow depth due to successive earth movements and tillage 122 operations that, over time and since 1946, have contributed to modify in shape and size of the 123 parcelling in the farm. The climate is typical of hot semi-arid areas, with strong seasonal 124 temperature variations (cold winters and hot summers). Annual precipitation is frequently 125 below 400 mm, and basically distributed from September to May. 

125 126 

127 z00'w ooo" Pa 400°E 0°2327°E 0°2330"E 0°2333"E 0°23'36"E 128 **Fig. 1** Location of the study area (left), and orthophoto of the peach orchard plot in 2015 129 (right). 

130 

131 

132 _Sample size and stratification_ 

133 

134 Three production and quality variables were sampled within the plot: yield (kg/tree), fruit 135 firmness (kg/cm[2] ) and refractometric index (ºBaumé). To determine the sample size, an aerial 136 multi-spectral image was taken on June 9[th] , 2015. The image resolution was 0.25 m/pixel. 137 Once the canopies were individually delimited on the basis of this image (ESRI® ArcMap[TM] 

3 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

138 10.4.1) to obtain a map of georeferenced trees within the plot (statistical population), a 139 weighted average value of NDVI according to the area of the canopy was assigned to each 140 tree. These tree-averaged NDVI values were then used as base data for determining the 141 sample size for a SRS without replacement using Eq. 1: 142 

143 

**==> picture [18 x 12] intentionally omitted <==**

144 

145 where _n_ is the sample size (number of trees) assuming sample independence, _ζ_ α/2 (1.96) is the 146 value of the standard normal variate for a 95% confidence (α = 0.05), _CV_ is the Coefficient of 147 Variation (17.5% in the present case), and _ER_ is the relative error assumed (10%). The result 148 of Eq. 1 was 12 sampling trees that were first randomly distributed within the plot (sampling 149 scheme A, Fig. 2). Apart from being a usual index for detecting spatial variability in tree 150 crops (Kazmierski et al. 2011), the use of NDVI for this approach was justified because 151 previous successful applications in fruit sampling were known (Miranda et al. 2015, 2018). 152 

153 154 **Fig. 2** Sampling units (trees) corresponding to seven different sampling schemes. 155 156 

157 Additional schemes were tested in which new sampling trees (twelve in each case) were first 158 obtained by stratified random sampling according to two and three classes of NDVI. 159 Specifically, NDVI classified maps were built by clustering interpolated NDVI values (NDVI 160 raster map) using the unsupervised classification algorithm ISODATA (Jensen 1996). The 161 process on which this algorithm is based is well known. Assigning an arbitrary mean to each 162 class, pixels were then successively reassigned minimizing the Euclidean distance from each 

4 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

163 pixel to the mean value of the class. Each iteration, class means were recalculated and pixels 164 were reallocated until the last iteration is reached, or the number of pixels that change from 165 one class to another does not exceed a certain threshold (Guastaferro et al. 2010). The same 166 strategy (stratified sampling based on clustered maps) was repeated using the information 167 provided by a Veris 3100 ECa surveyor. As a widely used sensor for soil characterization 168 (Sudduth et al. 2005), the information provided may be very useful in sampling given the soil169 tree interaction. This sensor measured the ECa at two soil depths: shallow (0-0.3 m) and deep 170 (0-0.9 m). Both ECa value layers were interpolated by ordinary kriging, and ECa classes were 171 established based on the cluster analysis of the two maps (shallow and deep) simultaneously. 172 Finally, the same procedure was repeated again by taking all three ancillary layers (NDVI, 173 shallow ECa and deep ECa). In short, seven sampling schemes (including scheme A) were 174 compared to each other based on a total number of 84 sampled trees (7x12) within the plot 175 (Fig. 2). Figure 3 shows five of the proposed sampling schemes, (i) SRS (scheme A), (ii) 176 stratified sampling based on two classes of NDVI (scheme B1), (iii) stratified sampling based 177 on three classes of NDVI (scheme B2), (iv) stratified sampling based on two classes of ECa 178 (scheme C1), and (v) stratified sampling based on three classes of ECa (scheme C2). Schemes 179 that use both information layers (schemes D1 and D2) are not shown. In each case, sampling 180 trees within each stratum were randomly sampled without replacement. 181 

182 183 **Fig. 3** Sampling schemes: (i) simple random sampling, (ii) stratified sampling by NDVI (two 184 strata), (iii) stratified sampling by NDVI (three strata), (iv) stratified sampling by ECa (two 185 strata), (v) stratified sampling by ECa (three strata). 186 187 188 

5 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

189 _Estimation in stratified sampling schemes_ 

- 190 

191 In a SRS approach, the sample mean ([)][ has proven to be an unbiased estimator of the ] 192 population mean ( ), with a variance that can be estimated by  ([)  ] (   ) 193 where is the sample variance, and is the finite population ( ) 194 correction or fpc, where _n_ is the sample size and _N_ the size of the population (459 trees in the 195 plot under study). As the interest was to work with small size samples, confidence limits for 196 the mean can be formulated as ⁄ √ √ , where[ is the sample mean, ] 197 √ √ is the standard error of the mean, and ⁄[ is the Student’s ] _[t]_[ value corresponding to ] 198 _n_ -1 degrees of freedom for a 95% confidence. 

199 

200 In order to sample more efficiently, other sampling schemes were used by stratifying the 12 201 sampling trees according to two strata (6 trees per stratum) or three strata (4 trees per 202 stratum). As a reminder, strata corresponded to the classes obtained after classification of the 203 plot according to NDVI, ECa or both auxiliary data layers. The different stratifications 204 produced classes that were not equal in area (therefore, with different number of trees per 205 stratum), and so the plot mean ( ) was then estimated for _K_ classes (strata) within the plot 206 using a weighted average as suggested by Cochran (1977), and more recently by Webster and 207 Lark (2013) in what is called regional classification techniques: 

208 

209[ ∑] (2) 

210 211 where[ is the sample mean of the ] _[k]_[th class, and ][ allowed the number of individuals ] 212 (trees) of the _k_ th class to be weighted using Eq. 3, 

213 

214 (3) 

215 

216 where _Nk_ is the number of trees within stratum _k_ , and _N_ is the total number within the plot. 

217 

- 218 As in SRS, confidence limits were obtained using the standard error of the mean, in this case, 219 the square root of the estimated variance (Cochran, 1977): 

220 221 ([)  ∑] ( ) (4) 

222 223 where is the within-class sample variance of the _k_ th stratum, is the sampling trees 224 within the stratum (6 or 4), and is the fpc for the _k_ th stratum calculated as 225 ~~.~~ Finally, the value ⁄[ was adjusted for each stratified sampling scheme according to ] 226 an effective number of degrees of freedom as established by Cochran (1977) in these cases. 

227 

228 The above confidence intervals were obtained assuming normality of observations. Since this 229 hypothesis was not tested (for example, using Shapiro-Wilk test), additional intervals were 230 calculated by applying a bootstrap estimation with the aim of contrasting the results. 231 Bootstrap is a method of resampling to obtain approximately the precision of an estimator 232 without hypothesizing about its distribution. Thus, for each set of 12 sampling trees 

6 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

233 corresponding to the different sampling schemes (which are now the statistical population), 234 sampling is done with replacement until obtaining 1000 sample arrangements each of equal 235 size 12. By averaging the 12 values in each new sample, it is known that 1-α level confidence 236 intervals can be obtained from the distribution of the 1000 calculated mean values through the 237 use of the percentile method (Efron 1982). Specifically, confidence limits were established 238 excluding the values located at the extreme positions of the distribution (α = 0.05). 239 In all cases, sample arrangement generation was performed by programming in R software, 240 version 3.3.2. 

- 241 

- 242 _Sampling efficiency_ 

- 243 

244 The most interesting sampling scheme is that which provides, on average, the least mean 245 squared error ( _MSE_ ). Since the seven sample means were unbiased estimators of the plot 246 mean, _MSE_ can be used as a measure of accuracy. Coinciding _MSE_ with the variance (Eq. 5), 247 efficiency to estimate the plot or population mean ( ) can be established as the inverse of the 248 estimated variance of the sample mean. 249 250 ( ~~)~~ [    ( ~~)~~ ] ( ~~)~~ ( ~~)~~ (5) 

- 251 

252 To compare any of the stratified sampling schemes ([)][ with respect to the simple random ] 253 sampling design ([)][, the relative efficiency (] _[RE]_[) was obtained as shown in Eq. ][6][: ] 254 

255 

**==> picture [426 x 23] intentionally omitted <==**

256 

257 where ([)][ was in each case the variance of the stratified sample mean, and ][ (][)][ or ] 258 variance of a random sample mean of the same size (taken as reference) was best estimated by 259 applying the method suggested by Cochran (1977). Specifically, given the results of a 260 stratified random sample, an unbiased estimator of the variance of the mean for a simple 261 random sample from the same population is (Eq. 7), 262 (   ) 263 ([)  ] ∑ ∑ ([)] 

**==> picture [461 x 23] intentionally omitted <==**

264 

265 where were the values sampled at trees within stratum _k_ . The other parameters are those 266 stated in previous paragraphs. By averaging the six previously calculated variances (one for 267 each stratified sample) with the variance previously obtained for scheme A (SRS), the 268 resulting variance, ([)][, was the one used in the calculation of the ] _[RE]_[. The reason for ] 269 using Eq. 7 was the use of non-proportional allocation of sampling trees, that is, the same 270 number of sampling units (6 or 4) was assigned regardless of the size (number of trees) of 271 each stratum. 272 273 Both the _MSE_ and the _RE_ were the statistics that served for the comparison of the different 274 sampling schemes and, above all, for the verification of the possible gain due to stratification. 275 Knowing the _RE_ allowed the necessary sample size for the same precision to be compared 276 between sampling schemes. Low _MSE_ values and values of _RE_ greater than 1 are those sought 277 for stratified sampling schemes. 278 279 

7 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

280 _An estimate of the population mean_ 

281 282 

282 Considering the spatial distribution of the 84 sampling trees resulting from the seven 283 sampling schemes (7x12) (Fig. 2), it is important to emphasize that only 5% of the plot area 284 resulted in a weak sampling density, i. e. with sampling units separated from each other by a 285 distance larger than 9.78 m (range of the NDVI exponential variogram, not shown). So, the 286 sampled information contained in these 84 trees was finally considered to estimate the mean 287 of the plot as accurately as possible by calculating a weighted average of the means of the 288 samples. The most accurate linear combination of the seven independent sample means was 289 obtained by assigning proportionally greater weighting to the more precise (Eq. 8), 

290 291 

## [ ∑ ] 

**==> picture [14 x 11] intentionally omitted <==**

292 

293 where[ is the weighted average for the plot, ][ are][ the sample means calculated for each of ] 294 the seven sampling schemes, and are the relative weights calculated using the inverse of the 295 variance of the sample means (Eq. 9): 296 

297 

**==> picture [429 x 23] intentionally omitted <==**

298 

299 _Goodness of stratification_ 

300 301 Finally, and as already mentioned, stratified sampling schemes were based on a previous 302 classification of the plot. A more accurate and efficient estimation of the mean was linked to 303 the ability of the NDVI and/or ECa auxiliary layers to discriminate different mean values 304 between classes, while the values within the classes have lower intra-class variability 305 compared to the total variability of the plot. A parameter that served to judge the goodness of 306 these classifications was the relative variance ( ⁄ ), where was the pooled or 307 average within-class variance, and was the total variance in the sample (Webster and Lark 308 2013). Used in the form of its complement (Eq. 10), 309 310 ( ⁄ ) (10) 

311 

312 it allowed values close to 1 to be obtained for those more effective sampling schemes. Values 313 close to 0 or even negative corresponded to non-effective stratifications. 

314 

- 315 _Spatial cross-correlation_ 

- 316 

317 To check stratified sampling results using ancillary variables, bivariate Moran's coefficient 318 was also calculated to assess the spatial cross-correlation between ancillary information layers 319 (NDVI and ECa) and the sampled yield and quality variables (GeoDa 1.12 software, Anselin 320 et al. 2010). Hypothetically, the most efficient stratified sampling schemes would be those 321 with significant spatial correlation with the variables to be sampled. Having verified 322 significant spatial autocorrelation for the three variables of interest (Moran's _I_ coefficient on 323 the total of 84 sampled trees, data not shown), assessing spatial cross-correlation between 324 ancillary variables and sampled variables could report information (even if a posteriori) on 325 what ancillary information was most convenient in each case. However, it must be said that 326 the use of geostatistical methods was beyond the scope of this paper. So, classical sampling 

8 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

327 theory was prevalent to assess stratified methods in this work under what is called design328 based sampling strategies (Brus & de Gruijter 1997). 

- 329 

- 330 **Results and discussion** 

- 331 

- 332 Table 1 shows the mean squared error ( _MSE_ ) and the relative efficiency ( _RE_ ) for the different 333 sampling schemes tested. For each of the variables (yield, fruit firmness and refractometric 334 index), confidence intervals (CIs) for the population mean ( ) are also shown. Two types of 335 confidence intervals were built for each sampling scheme as a result of using, i) the standard 336 error of the corresponding sample mean (parametric approach) or ii) the non-parametric 337 bootstrap approach. In the same Table 1, the weighted average of the plot[ for each field ] 338 variable is added next to the sample means. By completing this table of results, each sampling 339 scheme is valued according to the goodness of stratification using the value 1 minus the 340 relative variance. 

- 341 

- 342 Concerning the confidence intervals for the mean, bootstrap CIs were always slightly 343 narrower compared to CIs based on the normality of the sample means. This may be due to 344 the asymptotic approximation of the bootstrap method and, in any case, could prove the non345 normality of the distributions. However, and for comparison purposes, relative efficiency ( _RE,_ 346 Table 1) based on the estimated variances of the sample means (Eq. 6) was the statistic taken 347 as a reference instead of the CIs. As general results, stratified sampling seemed to improve 348 efficiency ( _RE_ ) compared to SRS, mostly for the quality variables (fruit firmness and 349 refractometric index). The improvement in yield estimation efficiency using stratified 350 sampling was lower than for quality variables, and it was only evident in very particular cases 351 of stratification. To aid interpretation, a more detailed analysis of the results in Table 1 352 addressed in the following sections. 

- 353 

- 354 _Sampling to estimate yield_ 

- 355 

- 356 Compared to the other sampling schemes, stratified sampling based on two classes of NDVI 357 (scheme B1) was the one that showed the best results in estimating yield, with an expected 358 average error (√   ) of 2.71 kg/tree (Table 1). Surprisingly, when stratifying the sample in 359 three NDVI classes (scheme B2), the method failed to improve the efficiency or precision 360 compared to SRS. This result could be explained by the poor effectiveness of the stratification 361 (negative value of ). In fact, negative values of the goodness of the stratification have 362 always been obtained in those inefficient schemes with _RE_ less than 1. 

- 363 

- 364 Concerning the use of ECa as ancillary information, stratifying the sample according to three 365 classes (strata) of soil conductivity (scheme C2) has also shown better efficiency results than 366 SRS. However, the error ( _MSE_ ) and relative efficiency ( _RE_ ) are not as good as in scheme B1 367 (stratification according to two classes of NDVI). Again and unexpectedly, the stratified 368 sampling has shown better efficiency than SRS despite the poor result of the goodness of the 369 stratification (positive but very low value of , and very far from the optimal values 370 close to 1). 

- 371 

- 372 The choice between using scheme B1 (stratifying by using the NDVI) and scheme C2 373 (stratifying by using the ECa) is not easy. An analysis of the special characteristics of the plot 374 can help to understand the sampling results for later decision-making. In the plot under study, 

9 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

375 affected by the presence of a petrocalcic horizon and high CaCO3 content, some advantage 376 was expected by stratifying the sample using a classified map of the ECa. In fact, significant 377 inverse spatial cross-correlation was obtained between yield and ECa using the bivariate 378 Moran’s _IB_ statistic (Table 2). As high CaCO3 content is a limiting factor of yield, with high 379 ECa values usually associated with low yields (Martínez-Casasnovas et al. 2012; Ortega-Blue 380 and Molina-Roco 2016; Uribeetxebarria et al. 2018), the spatial variation of ECa could make 381 it advisable to stratify on the basis of this information layer instead of using an NDVI map. 382 However, given the also significant spatial correlation between NDVI and yield (Table 2), the 383 best efficiency results, and the simplicity in managing the stratification in only two strata, the 384 B1 scheme is the option to recommend. In fact, NDVI has been used successfully to guide 385 sampling for yield forecasting tasks in many crops (Fortes et al. 2015; Miranda and Royo 386 2003; Taylor et al. 2010). 387 388 **Table 1** Efficiency parameters for the sampling schemes tested. 

|Sampling<br>scheme|Mean (|<br>)|(_MSE_)1/2|CIL|CIU|CILB|CIUB|_RE_||
|---|---|---|---|---|---|---|---|---|---|
|Yield (kg/tree)||||||||||
|Weighted average of the plot|24.49|||||||||
|A|26.36||2.32|21.26|31.47|22.41|30.73||0.00|
|B1|24.33||2.71|17.93|30.73|19.65|30.09|1.20|0.04|
|B2|24.29||3.65|15.37|33.21|18.28|30.58|0.66|-0.10|
|C1|23.57||3.70|14.83|32.31|16.90|29.43|0.64|-0.09|
|C2|24.58||2.82|17.90|31.26|19.11|30.20|1.10|0.07|
|D1|22.09||3.30|14.29|29.89|16.32|27.00|0.81|-0.08|
|D2|24.21||2.87|16.23|32.20|18.84|29.18|1.06|0.08|
|Fruit firmness (kg/cm2)||||||||||
|Weighted average of the plot|4.33|||||||||
|A|4.10||0.30|3.44|4.76|3.51|4.60||0.00|
|B1|4.31||0.22|3.82|4.81|3.87|4.76|1.80|0.13|
|B2|4.26||0.17|3.88|4.65|3.89|4.67|3.09|0.28|
|C1|4.27||0.35|3.45|5.08|3.56|4.79|0.69|-0.08|
|C2|4.75||0.27|4.13|5.37|4.28|5.22|1.18|-0.19|
|D1|4.40||0.33|3.66|5.14|3.40|4.92|0.80|0.19|
|D2|4.28||0.29|3.36|5.21|3.71|4.83|1.01|0.12|
|Refractometric index (ºBaumé)||||||||||
|Weighted average of the plot|6.86|||||||||
|A|7.02||0.14|6.71|7.32|6.80|7.31||0.00|
|B1|6.55||0.10|6.32|6.78|6.34|6.74|3.77|0.10|
|B2|6.63||0.19|6.10|7.16|5.90|7.09|1.09|0.54|
|C1|7.22||0.17|6.81|7.63|6.99|7.54|1.40|-0.09|
|C2|6.88||0.10|6.64|7.12|6.70|7.12|4.04|0.21|
|D1|6.80||0.32|5.99|7.61|6.37|7.32|0.39|-0.05|
|D2|7.31||0.17|6.86|7.76|6.88|7.66|1.29|0.38|



389 A (Simple random sampling); B1 and B2 (NDVI stratified sampling, 2 and 3 classes); C1 and C2 (ECa stratified 390 sampling, 2 and 3 classes); D1 and D2 (combined NDVI + ECa stratified sampling, 2 and 3 classes). _MSE_ (Mean 391 Squared Error), CIL and CIU (lower and upper confidence interval considering normality), CILB and CIUB (lower 392 and upper CI using bootstrap), _RE_ (relative efficiency), (relative variance). 393 394 395 From a practical point of view, as scheme B1 was more efficient ( _RE_ out of 1.20, Table 1), a 396 similar efficiency for the SRS (scheme A) could be reached using a smaller sample size, 397 theoretically equal to _n_ (SRS)/ _RE_ (12/1.20). In short, stratified sampling according to two 398 strata of NDVI allowed the sample size to be reduced by 17% compared to the SRS for the 399 same precision. 

10 

400 401 **Table 2** Spatial cross-correlation between NDVI and ECa ancillary information layers and the 402 sampled yield and quality variables 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

|Ancillary information|Sampled fruit variable|Bivariate Moran’s_IB_|Pseudo p-value**|
|---|---|---|---|
|||coefficient*||
|NDVI|Yield|-0.147|0.011|
|NDVI|Fruit firmness|0.199|0.004|
|NDVI|Refractometric index|-0.215|0.002|
|ECa|Yield|-0.315|0.001|
|ECa|Fruit firmness|-0.059|0.173|
|ECa|Refractometric index|0.029|0.306|



403 *Global spatial statistic to estimate the spatial cross-correlation between ancillary and sampled variables. 404 Correlation calculated based on 84 sampling trees using GeoDa 1.12 software (Anselin et al. 2010). 405 **Significance test was based on 999 permutations to generate the reference distribution under the null 406 hypothesis of spatial randomness. The observed statistic was then compared to this distribution to calculate a so407 called pseudo p-value (0.001 is the most extreme pseudo p-value under this scenario). 408 409 410 _Sampling to estimate fruit quality parameters_ 

411 412 Stratified sampling schemes worked differently when estimating fruit quality parameters. 413 Regarding fruit firmness (Table 1), scheme B2 was clearly better in both _MSE_ and efficiency 414 ( _RE_ greater than the other sampling schemes). A significant spatial cross-correlation between 415 NDVI and firmness (the greater the NDVI, the greater the firmness) could explain this result 416 (Table 2). Likewise, stratifying sampling trees based on three strata of NDVI allowed spatial 417 classification in fruit firmness to be more effective ( = 0.28). Concerning the sugar 418 content of the fruit (refractomeric index), the results were somewhat difficult to interpret. 419 Again, NDVI correlated spatially in a significant way (Table 2), showing an inverse 420 relationship. However, among the two proposed schemes (B1 and B2), it was the B1 scheme 421 (stratification through 2 strata) that achieved the best efficiency ( _RE_ value of 3.77). On the 422 other hand, this result was somewhat inconsistent with the effectiveness of the stratification. 423 Sampling trees were optimally classified using three classes of NDVI as suggested by the 424 goodness of stratification ( in Table 1). Therefore, there was a discrepancy in the 425 efficiency scores between schemes B1 and B2, and reasonable doubts arise as to whether to 426 use two or three strata to stratify the samples. This situation can occur because the sampling 427 trees can be well segmented (reducing the average within-class variance) and, however, 428 presenting a variance of the sample mean too high (poor value of the _RE_ ). Since the 429 fundamental criterion sought is to increase the _RE_ , the B1 scheme would be the recommended 430 option in this case by making compatible the values of _RE_ (Table 1) and spatial correlation 431 (Table 2). 432 

433 The relationship between NDVI and some quality parameters has been shown in other studies 434 (Zude-Sasse et al. 2016; Martínez-Casasnovas et al. 2012). Many times, fruits achieve lower 435 sugar content (ºBaumé) in the areas with the highest NDVI values. Inversely, vigorous 436 canopies with high amount of leaves (and higher NDVI values) can shade the fruits affecting 437 fruit ripening and, as happens in viticulture (Vanden Heuvel et al. 2002), producing greener 438 fruits with higher firmness values. This would explain the significant spatial relationship 439 between NDVI, fruit firmness and ºBaumé within the plot (Table 2). 440 

11 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

441 Regarding the use of ECa as ancillary information to stratify the quality, specifically ºBaumé 442 in fruit, the results have been contradictory. While sampling scheme C2 (three strata of ECa) 443 has shown the highest relative efficiency ( _RE_ of 4.04) together with good goodness of 444 stratification, spatial cross-correlation between both parameters (ECa and ºBaumé) was not 445 significant (Table 2). Since spatial correlation is an essential requirement to justify the 446 suitability of stratification, the use of ECa was not a priori an interesting option to stratify the 447 sampling. Nevertheless, as already said before, there could be an opportunity to use it to 448 efficiently estimate yield in this plot. 

- 449 

- 450 _Lessons learned for future research_ 

- 451 

452 Estimated variance of the mean in stratified sampling (StRS) is usually expected to be less 453 than the variance of a simple random sample (SRS) of the same size (Cochran 1977). Once 454 the sample size is decided (in our case, 12 sampling units), variance for StRS is finally 455 influenced by the particular allocation of the sampling units between the strata. Two or three 456 strata were delimited in this work using auxiliary information maps (NDVI or ECa), to then 457 allocate the same number of sampling units (trees) for all strata (6 or 4 trees per stratum if two 458 or three strata were used, respectively). This procedure probably resulted in a non-optimal 459 allocation of the sampled trees and, as a consequence, in a possible greater uncertainty (or less 460 precision) of the estimates. Cochran (1977) managed to evaluate, for a fixed sample size _n_ 461 the effect of the deviation from an optimal allocation of sampling units in stratified samples. 462 According to this approach, no significant increase in the variance (or significant loss of 463 efficiency) was expected due to having used the same number of trees per stratum (data not 464 shown). The use of identical allocation in each stratum was for reasons of simplifying the 465 whole process for the farmer. However, it would be advisable in future works to opt for the 466 proportional allocation of sampling trees according to the size of the strata to possibly 467 minimize the variance of the stratified means. Moving away from the optimal allocation of 468 sampling trees should be especially sensitive in yield estimation. This would explain why the 469 variance of the mean in the stratified sampling according to three strata of NDVI was 470 unexpectedly greater than the variance of the SRS. Interesting results comparing proportional 471 and optimum allocation can be found in Brus (1994). 472 

473 Finally, being in agreement with other studies (Meyers et al. 2011), sample stratification 474 making use of ancillary information is a possibility to take into account in fruit growing. 475 Cluster analysis has been the option used in this work for the construction of strata. A pending 476 issue for future work is to check other methods to optimize strata such as, for example, the 477 well-known rule of the cumulative root of the frequency function (see Cochran 1977 478 Although both SRS and stratified sampling provide unbiased estimates of the population 479 mean, stratifying the sample (Lark and Marchant 2009) is a way to (i) get more precise 480 estimates (or estimates with less uncertainty), or (ii) reduce the sample size for a certain 481 precision or efficiency. However, there is a major limiting factor as it is necessary for the 482 ancillary information to be spatially correlated with the variable to be sampled. If this 483 requirement is met, sample estimates can improve in precision. Ultimately, fruit growers and 484 technical advisors can benefit from positive impacts on operating time and cost. 485 486 487 488 

12 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

489 **Conclusions** 

- 490 

491 The use of ancillary data such as NDVI in stratified sampling schemes allows yield and 492 quality parameters in a peach orchard to be estimated with greater precision (or greater 493 efficiency). For fruit firmness, the stratification in three strata (scheme B2) is the most 494 recommendable option, achieving almost triple the efficiency compared to simple random 495 sampling (SRS). This means being able to reduce the sample size by almost 67% for the same 496 precision of the estimates. On the other hand, refractometric index may require a simpler 497 stratification scheme using only two NDVI classes (scheme B1). In terms of yield estimation, 498 the 20% higher efficiency of also stratified sampling according to two strata of NDVI 499 (scheme B1) allowed the sample size to be reduced by 17% compared to SRS. In no case the 500 ECa or the combined use of NDVI and ECa have provided substantial advantages compared 501 to the use of NDVI as a single layer of ancillary information. So, the recommendation is to 502 use NDVI as ancillary information to more efficiently estimate yield and quality variables in 503 peach. However, and especially for yield estimates, caution must be taken at the time of 504 allocating sampling trees by strata. 

- 505 

- 506 **Acknowledgements** 

- 507 

- 508 This work was funded by the Spanish Ministry of Economy and Competitiveness through the 509 project AgVANCE (AGL2013-48297-C2-2-R). The authors also thank the IRTA 510 Experimental Station in Gimenells (Lleida, Spain) for the possibility of carrying out this 511 sampling study on a peach orchard. 

- 512 

- 513 **References** 

- 514 

- 515 Anselin, L., Syabri, I., & Kho, Y. (2010). GeoDa: An Introduction to Spatial Data Analysis. 516 In: M. M. Fischer, A. Getis (Ed.) Handbook of Applied Spatial Analysis, Berlin, 517 Germany: Springer, pp. 73-89. 

- 518 Brus, D. J. (1994). Improving design-based estimation of spatial means by soil map 519 stratification. A case study of phosphate saturation. _Geoderma, 62_ , 233-246. 

- 520 Brus, D. J., & de Gruijter, J. J. (1997). Random sampling or geostatistical modelling? 521 Choosing between design-based and model-based sampling strategies for soil (with 522 Discussion). _Geoderma, 80_ , 1-44. 

- 523 Carrillo, E., Matese, A., Rousseau, J., & Tisseyre, B. (2016). Use of multi-spectral airborne 524 imagery to improve yield sampling in viticulture. _Precision Agriculture, 17_ , 74-92. 

- 525 Cochran, W. G. (1977). _Sampling Techniques_ . New York, NY, USA: John Wiley & Sons, 526 Inc. 428 pp. 

- 527 Efron, B. (1982). _The Jackknife, the Bootstrap and Other Resampling Plans_ . CBMS-NSF 528 Regional Conference Series in Applied Mathematics, Philadelphia, PA, USA: Society 529 for Industrial and Applied Mathematics. 85 pp. 

- 530 Fortes, R., Prieto, M. H., García-Martín, A., Córdoba, A., Martínez, L., & Campillo, C. 531 (2015). Using NDVI and guided sampling to develop yield prediction maps of 532 processing tomato crop. _Spanish Journal of Agricultural Research, 13(1)_ , e02-004, 9 533 pages. 534 Guastaferro, F., Castrignanò, A., De Benedetto, D., Sollitto, D., Troccoli, A., & Cafarelli, B. 535 (2010). A comparison of different algorithms for the delineation of management zones. 536 _Precision Agriculture, 11_ , 600-620. 

13 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

537 Jensen, J. R. (1996). _Introductory Digital Image Processing: A Remote Sensing Perspective_ . 538 Englewood Cliffs, NJ, USA: Prentice Hall. 316 pp. 539 Kazmierski, M., Glemas, P., Rousseau, J., & Tisseyre, B. (2011). Temporal stability of 540 within-field patterns of NDVI in non-irrigated Mediterranean vineyards. _Journal_ 541 _International des Sciences de la Vigne et du Vin, 45(2)_ , 61–73. 542 Lark, R. M., & Marchant, B. P. (2009). Using advanced methods to reduce the cost of soil 543 sampling; ideas for the future. R&D Conference ‘Precision in arable farming: current 544 practice and future potential’, Grantham, Lincolnshire, UK, 28[th] -29[th] October 2009. pp. 545 18–25 ref.6. https://www.cabdirect.org/cabdirect/FullTextPDF/2010/20103068758.pdf 546 Martínez-Casasnovas, J.A., Agelet-Fernandez, J., Arnó, J., & Ramos, M.C. (2012). Analysis 547 of vineyard differential management zones and relation to vine development, grape 548 maturity and quality. _Spanish Journal of Agricultural Research, 10(2)_ , 326–337. 549 Meyers, J. M., & Vanden Heuvel, J. E. (2014). Research Note. Use of Normalized Difference 550 Vegetation Index Images to Optimize Vineyard Sampling Protocols. _American Journal_ 551 _of Enology and Viticulture, 65(2)_ , 250-253. 552 Meyers, J. M., Sacks, G. L., van Es, H. M., & Vanden Heuvel, J. E. (2011). Improving 553 vineyard sampling efficiency via dynamic spatially explicit optimisation. _Australian_ 554 _Journal of Grape and Wine Research, 17,_ 306-315. 555 Miranda, C., & Royo, J. B. (2003). A statistical model to estimate potential yields in peach 556 before bloom. _Journal of the American Society for Horticultural Science, 128_ , 297-301. 557 Miranda, C., Urretavizcaya, I., Santesteban, L. G., & Royo, J. B. (2015). Sampling 558 stratification using aerial imagery to estimate fruit load and hail damage in nectarine 559 trees. In: J. V. Stafford (Ed.) Precision Agriculture’15, Proceedings of the 10th 560 European Conference on Precision Agriculture, Wageningen, The Netherlands: 561 Wageningen Academic Publishers, pp. 541-546. 562 Miranda, C., Santesteban, L. G., Urrestarazu, J., Loidi, M., & Royo, J. B. (2018). Sampling 563 stratification using aerial imagery to estimate fruit load in peach tree orchards. 564 _Agriculture, 8_ (6), 78; https://doi.org/10.3390/agriculture8060078. 565 Monestiez, P., Audergon, J. M., & Habib, R. (1990). Spatial dependences and sampling in a 566 fruit tree: a geostatistical approach. _Institut National de la Recherche Agronomique_ , 567 Technical Report No. 163, 30 pp. 568 Moral, F. J., Terrón, J. M., & Marques da Silva, J. R. (2010). Delineation of management 569 zones using mobile measurements of soil apparent electrical conductivity and 570 multivariate geostatistical techniques. _Soil & Tillage Research, 106_ , 335–343. 571 Ortega-Blu, R., & Molina-Roco, M. (2016). Evaluation of vegetation indices and apparent 572 soil electrical conductivity for site-specific vineyard management in Chile. _Precision_ 573 _Agriculture, 17_ , 434-450. 

- 574 Peralta, N. R., & Costa, J. L. (2013). Delineation of management zones with soil apparent 575 electrical conductivity to improve nutrient management. _Computers and Electronics in_ 576 _Agriculture, 99_ , 218-226. 

- 577 Soil Survey Staff. (2014). _Keys to Soil Taxonomy, 12th ed_ . Washington, USA: USDA-Natural 578 Resources Conservation Service. 

- 579 Sudduth, K. A., Kitchen, N. R., Wiebold, W. J., Batchelor, W. D., Bollero, G. A., Bullock, D. 580 G., et al. (2005). Relating apparent electrical conductivity to soil properties across the 581 north-central USA. _Computers and Electronics in Agriculture_ , 46, 263-283. 

- 582 Taylor, J., Tisseyre, B., Bramley, R., & Reid, A. (2005). A comparison of the spatial 583 variability of vineyard yield in European and Australian production systems. In: J. V. 584 Stafford (Ed.) Precision Agriculture’05, Proceedings of the 5th European Conference on 

14 

POSTPRINT of the article: Uribeetxebarria, A., Martínez-Casasnovas, J.A, Escolà, A., Rosell-Polo, J.R., Arnó, J.2018. Stratified sampling in fruit orchards using cluster-based ancillary information maps: a comparative analysis to improve yield and quality estimates. _Precis.Agric._ DOI: https://doi.org/10.1007/s11119-018-9619-9 

- 585 Precision Agriculture, Wageningen, The Netherlands: Wageningen Academic 586 Publishers, pp. 907–914. 

- 587 Taylor, J., Acevedo-Opazo, C., Ojeda, H., & Tisseyre, B. (2010). Identification and 588 significance of sources of spatial variability in grapevine water status. _Australian_ 589 _Journal of Grape and Wine Research, 16_ , 218–226. 

- 590 Uribeetxebarria, A., Arnó, J., Escolà, A., & Martínez-Casasnovas, J.A. (2018). Apparent 591 electrical conductivity and multivariate analysis of soil properties to assess soil 592 constraints in orchards affected by previous parcelling. _Geoderma, 319_ , 185–193. 

- 593 Vanden Heuvel, J. E., Leonardos, E. D., Proctor, J. T. A., Fisher, K. H., & Sullivan, J. A. 594 (2002). Translocation and partitioning patterns of 14C photoassimilate from light- and 595 shade- adapted shoots in greenhouse-grown ‘Chardonnay’ grapevines (Vitis vinifera 596 L.). _Journal of the American Society for Horticultural Science, 127,_ 912–918. 

- 597 Webster, R., & Lark, R. M. (2013). _Field sampling for environmental science and_ 598 _management_ . London and New York: Routledge, 192 pp. 

- 599 Wulfsohn, D., Aravena Zamora, F., Potin Téllez, C., Zamora Lagos, I., & García-Fiñana, M. 600 (2012). Multilevel systematic sampling to estimate total fruit number for yield forecasts. 601 _Precision Agriculture, 13_ , 256-275. 

- 602 Zude-Sasse, M., Fountas, S., Gemtos, T. A., Abu-Khalaf, N. (2016). Applications of precision 603 agriculture in horticultural crops. _European Journal of Horticultural Science, 81(2)_ , 78604 90. 

15 

