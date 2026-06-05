Computers and Electronics in Agriculture 222 (2024) 109098 

Contents lists available at ScienceDirect 

## Computers and Electronics in Agriculture 

journal homepage: www.elsevier.com/locate/compag 

## Original papers 

## Delineating citrus management zones using spatial interpolation and UAV-based multispectral approaches 

Giuseppe Longo-Minnolo[a] , Simona Consoli[a] , Daniela Vanella[a][,][*] , Salvatore Pappalardo[a] , Serena Guarrera[b] , Giuseppe Manetto[a] , Emanuele Cerruto[a ] 

ab _Dipartimento di Agricoltura, Alimentazione e Ambiente (Di3A), Universit Agricultural, Food and Environmental Science, Di3A, University of Catania, Catania, 95124, Italy   a degli Studi di Catania, Via S. Sofia, 100, Catania 95123, Italy_ ` 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_<br>Precision irrigation<br>Proximal sensing<br>Soil-plant system<br>Crop water status monitoring|The ability to delineate site-specific management zones is a key feature for precision agriculture applications. In<br>this study, a novel methodological protocol for mapping the water status, i.e. the stem water potential (SWP), of<br>citrus orchards was developed. Specifically, observed stem water potential (SWPobs) values and unmanned aerial<br>vehicle multispectral information (i.e., vegetation indices, VIs, and spectral bands, SBs) were integrated to<br>implement a twofold approach based on: (i) the spatial interpolation (SWPint) of the SWPobs, and (ii) the stepwise|
||regression models (SWPproxy) between the SWPobsand the VIs (scenario 1) or between the SWPobsand the SBs|
||(scenario 2). Then, the derived crop water status maps (SWPintand SWPproxy) were customized by applying an<br>absolute (scientific-driven), a relative (quantile-driven), and an automated clustering (K-means) classification|
||method.|
||The accuracy of the proposed approach, evaluated by comparing SWPintand SWPproxywith SWPobsusing linear|
||regression models, showed reliable results, with average mean absolute error and root mean square error values|
||ranging from 0.13 to 0.19 MPa and from 0.19 to 0.24 MPa, respectively. These results provide practical insights|
||for identifying the spatial-temporal variability of the SWP of the citrus orchard under study. Additionally, the<br>study highlights the importance of using a scientific-driven classification to support the adoption of precision|
||irrigation criteria and decision-making process by non-expert users, as indicated by the assessment of the|
||Silhouette index.|



## **1. Introduction** 

The agricultural sector, and specifically irrigation, is the largest consumer of freshwater worldwide. In this context, precision agriculture, which includes a set of different management strategies and technologies, could play a fundamental role in supporting decisions and actions aimed at increasing the efficiency, productivity, and sustainability of agricultural processes (Ohana-Levi et al., 2021a). The assessment of crop water status and the delineation of irrigation management zones are fundamental because water deficit is one of the primary limiting factors, especially in Mediterranean agro-ecosystems, where long and persistent dry seasons occur (Jiang et al., 2011; Rossini et al., 2013; Rallo et al., 2014). 

Traditionally, a management zone is defined as a sub-region of a field characterized by a homogeneous combination of yield-limiting factors (e.g., crop potential productivity, nutrient use efficiency and 

environmental characteristics), which can be managed with a single set of agronomic inputs, including irrigation doses (Doerge, 1999). Several techniques have been proposed for delineating optimal management zones for precision irrigation purposes under different cropping systems (by applying multivariate geo-statistics and/or classification techniques Inman et al., 2008; Jiang et al., 2011; Cordoba et al., 2016; Oldoni ´ & Bassoi, 2016; Ohana-Levi et al., 2019; Leo et al., 2023;). However, a common goal of the zoning approaches is to minimize the number of homogeneous areas based on the input data (Zhang et al., 2002). In this sense, different sources of information have been used to implement irrigation management zones, varying from crop parameters (Leo et al., 2023) to soil properties (Jiang et al., 2011). 

Generally, data-sources referring to the soil-plant system are divided into two separate groups based on the data acquisition modality: (i) point-based ground data; and (ii) spatially distributed information. Point-based ground data refer to local measurements acquired at soil 

* Corresponding author. 

_E-mail address:_ daniela.vanella@unict.it (D. Vanella). 

https://doi.org/10.1016/j.compag.2024.109098 Received 20 July 2023; Received in revised form 23 May 2024; Accepted 26 May 2024 

Available online 30 May 2024 

0168-1699/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/bync-nd/4.0/). 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 1.** Overview of the citrus orchard (a) and the monitoring tools applied at the study area: stem water potential measurements by a pressure chamber (b), and multispectral imagery acquired by unmanned aerial vehicle (c). The sample trees are indicated as red circles. 

and plant level, whereas spatially distributed information is usually derived from multispectral images acquired by satellite and/or unmanned aerial vehicle (UAV) techniques, as well as soil mapping instruments. Typically, crop point-based data involve traditional methods for measuring crop water status. In this context, stem water potential (SWP), usually measured by pressure chambers, has been widely considered a useful indicator due to its reliability and effectiveness. Nevertheless, the main limitation associated to this data is its confined spatial distribution. In addition, SWP measurements are time-consuming and labour-intensive, requiring many samples, and are expensive and not standardized because they are influenced by the observer’s expertise (e.g., Motisi et al., 2012; Romero et al., 2018; Pampuri et al., 2021; Tang et al., 2022; Maran˜on et al., 2023´ ). However, some of these shortcomings can be overcome using spatial interpolation methods based on deterministic or stochastics algorithms (Longo-Minnolo et al., 2022). 

The other group of data-source derived from satellite or UAV-based techniques commonly includes information referring to the visiblenear infrared (VNIR) and thermal infrared (TIR) portions of the electromagnetic spectrum at high spatial resolution. 

Nowadays, precision irrigation management and crop water status monitoring have greatly benefited from current technological advances in UAV systems, both in terms of on-board sensors (e.g., improved spatial, spectral, and radiometric resolutions) and UAV platforms (e.g., smaller dimensions, greater payload capacity, and increased autonomy). In particular, the use of UAV technologies offers significant advantages by enabling the fast and easy acquisition of useful field data for defining homogeneous irrigation zoning, representing a reliable and costeffective tool. 

In the recent years, spectral reflectance data, specifically vegetation indices (VIs) calculated by combining different spectral bands (SBs), have been used due to the connection between the spectral properties of vegetation and its biochemical and biophysical attributes, including water content (Song et al., 2009). Although in the visible spectral domain water is transparent (with a finite absorption coefficient with a minimum in the blue-green), a high correlation between the most common VIs in this region and crop water status has been detected in several studies because of the role of water deficit in the photosynthesis process (Romero et al., 2018). For instance, some authors have successfully used VIs as proxy of crop water status, detecting crop water stress at the canopy level in maize, barley, olive groves, and vineyards (Baluja et al., 2012; Behmann et al., 2014; Rallo et al., 2014; Poças et al., ˆ 

2015 Tang et al., 2022). 

However, the response to water stress is crop-specific and varies with different VIs used (Lin et al., 2020). In this context, a limited number of studies have investigated the performance of multispectral images for detecting water stress conditions in citrus orchards. Additionally, none of these studies have applied any approach for the delineation of management zones on the final crop water status maps. 

The general aim of this research was to identify a simple and innovative protocol for the spatial assessment of citrus water status (CWS) and the delineation of management zones. Specifically, it aimed to: (i) assess the use of interpolation methods to derive spatially distributed estimates of SWP; (ii) predict SWP by evaluating the suitability of the SBs and the most common VIs, computed with VNIR UAV-based information, and assess the best SBs and VIs combination through statistical methods; and (iii) define different approaches for delineating management zones of the CWS. 

## **2. Materials and methods** 

## _2.1. Study area_ 

The study was conducted in a blood orange orchard ( _Citrus sinensis_ (L.) Osbeck, Tarocco Sciara grafted on Carrizo citrange Poncirus trifoliata (L.) Raf. × C. sinensis (L.) Osbeck), located in Eastern Sicily, Italy (37[◦] 20′12.65″N, 14[◦] 53′33.04″E, WGS84) (Fig. 1a), during the period September 2021 to July 2022. During this period, 6 monitoring campaigns were carried out, considering 3 different citrus phenological phases: 01/09/2021 (phase II - fruit rapid growth, FRG), 18/11/2021 (phase III - fruit maturation, FM), 12/04/2022 and 12/05/2022 (phase I - fruit cellular division, FCD), 28/06/2022 and 19/07/2022 (FRG). 

The citrus orchard was planted in 2011 with a spacing of 6 m between the tree rows and 4 m within the trees (with NW-SE orientation), totaling 300 plants (approximately 1 ha). Additional details on irrigation and fertilization amounts applied at the study site are reported in Consoli et al. (2014) and Saitta et al. (2021). 

The climate in the study area is semi-arid Mediterranean, characterised by warm and dry summers. The annual average values (2002–2022) of air temperature, precipitation, and reference evapotranspiration (ET0) were approximately 18.3[◦] C, 577 mm, and 1264 mm, respectively. The soil texture is sandy loam, with soil water content values at the field capacity (0.03 MPa) and at the wilting point (1.5 MPa) 

2 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 2.** Flow chart of the methodological protocol applied at the study area for assessing citrus water status (CWS) and defining management zones. 

of 0.28 m[3] m[−][3 ] and 0.14 m[3] m[−][3] , respectively (Consoli et al., 2017). 

(McCluney, 2014). 

## _2.2. Citrus water status assessment_ 

## _2.2.1. Data sources_ 

The data inputs of interest were gathered from 6 monitoring campaigns conducted _in situ_ during the years 2021–2022. Specifically, the observed SWP values (SWPobs) dataset was acquired using a portable Scholander pressure chamber apparatus (Model 3115, Soilmoisture equipment corp., Santa Barbara, CA, USA) (Fig. 1b). Measurements were conducted at solar midday on 2 fully exposed sunlit mature leaves per tree, totaling 24 trees for each field campaign (Turner, 1981; Corell et al., 2020). The selection of the tree samples in Fig. 1 was based on the experimental factors described in Pappalardo et al. (2023). Leaves were covered with aluminum foil for at least one hour prior to the measurements, and once cut, they were immediately placed into the pressure chamber with the petiole exposed and pressurized with nitrogen. 

Multispectral images were collected simultaneously with the SWPobs measurements using a multi-spectral camera mounted on board of a UAV platform (DJI P4 Multispectral) (Fig. 1c). The camera, comprised of 6 sensors (CMOS 1/2.9″ with 2 MPixel each), with a field-of-view and a focal length of 62.7[◦] and 5.74 mm, respectively, captured the surface reflective characteristics within the following SBs (wavelengths in brackets): blue (B, 450 nm ± 16 nm); green (G, 560 nm ± 16 nm); red (R, 650 nm ± 16 nm); red-edge (RE, 730 nm ± 16 nm); near-infrared (NIR, 840 nm ± 26 nm). The ground sample resolution at a flight elevation of 37 m of was approximately 1.9 cm/pixel. The UAV system was integrated with a global navigation satellite system and global positioning system real time kinematic module (Galileo and GLONASS). The mosaic of the tiles was generated using the Mosaic Editor tool implemented in the PIX4Dmapper software (v.4.8.4). Additionally, radiometric correction of the single reflectance maps was performed to improve the radiometric quality of the data. This correction step took into account the sensor settings and properties, as well as the scene conditions (e.g., sun irradiance and sun angle) during the flight 

## _2.2.2. Methodological approach_ 

Fig. 2 depicts a flow chart of the protocol applied to assess the CWS and define the management zones in the study area. For this purpose, two different data sources were used: (i) point-based ground data, namely SWPobs values, comprising a total of 144 observations, and (ii) spatially distributed data, specifically 6 UAV-based multispectral imagery datasets. 

Data sources were used to develop two strategies aimed at estimating the SWP: a spatial interpolation approach and a UAV-based multispectral approach. In both cases, the overall SWPobs dataset was split into two subsets, 67 % of SWPobs (n = 96) was randomly selected as training subset and the remaining 37 % (n = 48) as validation subset for evaluating the accuracy of the applied methods. Each processing step was executed with 5 different configurations (C1–C5), with variation in the random selection of subsets (i.e., training and validation subsets) each time. 

The training subset was utilized to obtain spatially distributed SWP maps (SWPint) for each of the 6 UAV image acquisition dates, as reported in Section 2.2.3. With the UAV-based multispectral approach, SWP was estimated from VIs and SBs (SWPproxy). Specifically, to evaluate the suitability of VIs (scenario 1) or SBs (scenario 2) for sensing the CWS, a correlation analysis was performed with respect to SWPobs, followed by a stepwise linear regression, as detailed in Section 2.2.4. Finally, the CWS management zones were delineated on the obtained maps using an absolute, a relative, and an automated clustering algorithm (K-means) approach, as detailed in Section 2.3. Statistical analyses and graphical representations were performed by using R ver. 4.1.1 (R Core Team, 2021) and RStudio (Posit team, 2023). Note that all the plots showed in the Result section were drawn using the “lattice” (Sarkar, 2008) and “latticeExtra” (Sarkar and Andrews, 2022) packages. 

## _2.2.3. Spatial interpolation approach_ 

To determine SWPint, the inverse distance weighting (IDW) 

3 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Table 1** Vegetation indices, with standard equations and relative references, calculated in the study. _B_ , _G_ , _R_ , _RE_ and _NIR_ refer to the blue, green, red, red-edge and near-infrared SBs, respectively, whereas _L_ is the canopy background adjustment factor (set as 0.5). 

|<br>SBs, respectively, whereas_L_is the canopy background adjustment factor (set as 0.5).|<br>|
|---|---|
|Vegetation Index<br>Acronym|Equation<br>Reference|
|Atmospherically Resistant Vegetation Index<br>ARVI<br>Enhanced Vegetation Index<br>EVI<br>Green Index<br>GI<br>Green Leaf Index<br>GLI<br>Modifed Soil Adjusted Vegetation Index<br>MSAVI<br>Normalized Difference Greenness Vegetation Index<br>NDGI<br>Normalized Difference Red Edge Index<br>NDRE<br>Normalized Difference Vegetation Index<br>NDVI<br>Optimal Soil Adjusted Vegetation Index<br>OSAVI<br>Red Green Ratio Index<br>RGRI<br>Renormalized Difference Vegetation Index<br>RDVI<br>Simple Ratio Index<br>SR<br>Soil Adjusted Vegetation Index<br>SAVI<br>Visible Atmospherically Resistant Index<br>VARI|_NIR_−2(_R_−_B_)<br>_NIR_+2(_R_−_B_)<br>Kaufman and Tanre (1992)<br>2_._5(_NIR_−_R_)<br>(_NIR_+6_R_−7_._5_B_) +1<br>Huete et al. (2002)<br>_G_<br>_R_<br>Chamard et al. (1991)<br>2_G_−_R_−_B_<br>2_G_+_R_+_B_<br>Gobron et al. (2000)<br>2_NIR_+1−<br>̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅**̅**<br>(2_NIR_+1)2 −8(_NIR_−_R_)<br>√<br>2<br>Qi et al. (1994)<br>_NIR_−_G_<br>_NIR_+_G_<br>Gamon&Surfus (1999)<br>_NIR_−_RE_<br>_NIR_+_RE_<br>Barnes et al. (2000)<br>_NIR_−_R_<br>_NIR_+_R_<br>Rouse et al. (1974)<br>_NIR_−_R_<br>_NIR_+_R_+0_._16<br>Rondeaux et al. (1996)<br>_R_<br>_G_<br>Gamon&Surfus (1999)<br>_NIR_−_R_<br>~~̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅~~<br>_NIR_+_R_<br>~~√~~<br>Roujean and Breon (1995)<br>_NIR_<br>_R_<br>Birth&McVey (1968)<br>(1+_L_)(_NIR_−_R_)<br>_NIR_+_R_+_L_<br>Huete (1988)<br>_G_−_R_<br>_G_+_R_−_B_<br>Gitelson et al. (2002)|



algorithm was applied using the processing tools implemented in QGIS software (QGIS, v. 3.16.7-Hannover). The choice of adopting the IDW algorithm in this study is justified by the size of the available SWP observations, as suggested by Acevedo-Opazo et al. (2013). In general, IDW is a deterministic method that utilizes a weighted average of the observations, where the weight assigned to each observation is function of the inverse distance between that observation and the point to be estimated (Shepard, 1968). Specifically, the general equation of IDW is the following: 

**==> picture [257 x 20] intentionally omitted <==**

where _z_ ( _x_ ) is the interpolated value of a point, _zi_ ( _xi_ ) are the neighbouring observations and _λi_ ( _x_ ) are the weights, defined as: 

**==> picture [257 x 20] intentionally omitted <==**

with _d_ ( _x, xi_ ) the distance between the point to be estimated and the observations, and α the power of the reciprocal distance function. 

In the current study, the parameter α was varied from 0.5 to 2, with a step of 0.5, and the model with the best performance was chosen, as detailed in Section 2.2.5. 

From the preliminary inspection of scatterplots between SWPobs and SBs, and between SWPobs and VIs values for each phenological stage, a roughly linear trend was observed in the majority of the cases, even though with low (but statistically significant) correlation coefficients. Therefore, a linear regression approach was chosen to be carried-out. Specifically, a stepwise linear regression was applied, considering SWPobs as dependent variable and the VIs (scenario 1) or the SBs (scenario 2) as independent variables. 

The stepwise regression is a method applied when numerous potential explanatory variables are present (Efroymson, 1960). This method iteratively examines the statistical significance of each variable in a linear regression model, selecting a subset of predictive variables for building the final model. In this study, a backward elimination approach was used. The significance level ( _p_ -value) to remove variables from the model was set at 0.05 for each step. Thus, the variable with the highest _p_ - value was eliminated from the model at each step. In addition, multicollinearity among independent variables was analyzed using the Variance Inflation Factor (VIF) test, employing the “car” package (Fox and Weisberg, 2019). Note that the smallest possible value of VIF is 1, indicating an absence of collinearity. As a rule of thumb, a VIF value exceeding 5 or 10 suggests a problematic amount of collinearity (James et al., 2013). In this study, all variables with VIF greater than 5 were removed from the model. 

## _2.2.4. UAV-based multispectral approach_ 

The most common VIs were calculated in QGIS by combining the available SBs into the raster calculator according to the equations reported in Table 1. For defining the best predictor of CWS, a preliminary correlation analysis between SWPobs, and VIs, and between SWPobs and SBs was carried out. To visualize the correlation matrix, the “corrplot” package (Wei and Simko, 2021) was utilized. 

The VIs and SBs values were extracted at canopy level using a fixed circular buffer area (diameter equal to 1.0 m) in the QGIS environment (v. 3.16.7-Hannover). This fixed buffer area was generated and adjusted to identify the tree canopies for each UAV image using the relative true colour image (RGB) as a reference. The diameter of the buffer area was chosen as the minimum value of the canopy diameters to avoid pixel contamination from the soil. 

## _2.2.5. Statistical performance_ 

Preliminarily, significant differences between SWP or spectral band reflectance values as a function of the monitoring campaign were assessed by applying the Kruskal-Wallis test, utilizing the “agricolae” package (de Mendiburu, 2023). 

The performance of the spatial interpolation approach (i.e. IDW, varying the α parameter) was evaluated using a linear regression to compare the SWPint estimated from the interpolation subset with the SWPobs from the validation subset. Specifically, the slope of regression and the residual standard error (RSE, MPa; Eq. (1)) were evaluated by forcing the intercept to 0 to analyze how well the models fit the observed data. In addition, the following statistical metrics were adopted to quantitatively describe the accuracy of the applied approaches: mean 

4 

_G. Longo-Minnolo et al._ 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

**Fig. 3.** Trend and variability of observed stem water potential (SWPobs) during the experimental trials (mean separation by Kruskal–Wallis test at _p_ -level = 0.05), together with irrigation, precipitation, air temperature and relative humidity (RH) data. 

absolute error (MAE, MPa; Eq. (2)); root mean square error (RMSE, MPa; Eq. (3)), and percent bias (PBIAS, %; Eq. (4)). 

**==> picture [44 x 2] intentionally omitted <==**

**==> picture [257 x 120] intentionally omitted <==**

where _Pi_ and _Oi_ are the predicted and the observed values, respectively, _df_ are the degrees of freedom, _n_ is the number of observations. The 

significance level was assessed in terms of _p_ -value (≤0.05). Consequently, the model with the best performance was chosen based on the above mentioned statistical indicators. 

The correlation between the multispectral images in terms of VIs and SBs, and the SWPobs, was assessed using the Pearson coefficient of correlation and the significance was evaluated using p-value ≤ 0.05, ≤0.01, and ≤0.001. 

The stepwise linear regression models, constructed with SWPobs as dependent variable and the VIs (scenario 1) or the SBs (scenario 2) as independent variables, and including the phenological stage (PS) as covariate, were initially calibrated on the training subset. The calibration was assessed in terms of coefficient of determination (R[2] ), adjusted R[2 ] for the number of predictors (R[2] -Adj), RSE, RMSE, and MAE. Their accuracy was then evaluated by comparing the SWPproxy with the SWPobs from the validation subset. As for the spatial interpolation approach, the same statistical indicators were utilized, i.e., slope, RSE, MAE, RMSE and PBIAS. The significance level was determined based on 

5 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 4.** Trend and variability of spectral band reflectance profiles during the experimental trials (mean separation by Kruskal–Wallis test at _p_ -level = 0.05). 

**Table 2** 

Main statistical indicators of the interpolation method applied at the study area for determining the stem water potential spatial distribution (SWPint) by varying the power (α) of the inverse distance function for each configuration (C1–C5) of the validation subset. 

|||Configuration|Slope|RSE (MPa)|MAE (MPa)|RMSE (MPa)|PBIAS (%)|
|---|---|---|---|---|---|---|---|
|α=0.5|0.5|C1|1.000|0.194|0.136|0.192|−1.059|
|||C2|1.000|0.185|0.130|0.183|0.573|
|||C3|0.970|0.182|0.138|0.186|3.101|
|||C4|0.970|0.210|0.145|0.211|2.049|
|||C5|0.970|0.184|0.142|0.187|3.580|
|α=1.0|1.0|C1|1.000|0.188|0.124|0.186|−0.731|
|||C2|0.990|0.176|0.125|0.174|1.041|
|||C3|0.970|0.175|0.129|0.179|3.131|
|||C4|0.980|0.205|0.138|0.206|1.651|
|||C5|0.970|0.172|0.132|0.178|4.043|
|α=1.5|1.5|C1|1.000|0.190|0.126|0.188|−0.611|
|||C2|0.980|0.173|0.125|0.173|1.704|
|||C3|0.970|0.177|0.127|0.181|3.131|
|||C4|0.980|0.208|0.138|0.208|1.269|
|||C5|0.960|0.172|0.132|0.179|4.336|
|α=2.0|2.0|C1|1.000|0.200|0.133|0.198|−0.626|
|||C2|0.980|0.176|0.128|0.177|2.142|
|||C3|0.970|0.187|0.131|0.191|3.208|
|||C4|0.980|0.217|0.145|0.217|0.917|
|||C5|0.960|0.183|0.142|0.191|4.522|



the _p_ -value (≤0.05). 

## _2.3. Definition of the citrus water status management zones_ 

Site-specific CWS management zones were delineated by implementing different methods, i.e., an absolute (or scientific-driven) approach, a relative approach, and an automated clustering algorithm (K-means). 

The absolute approach was founded on the utilization of fixed SWP thresholds recommended by an extensive literature review analysis (Ballester et al., 2013; P´erez-P´erez et al., 2014; Robles et al., 2016; Martínez-Gimeno et al., 2018, Saitta et al., 2021) and adjusted for the − 0.80 site-specific conditions. In particular, a SWP range of values from to − 1.40 MPa indicated a “no water stress” condition. At the study site, the “no water stress” condition was met after intense rain events occurred in the days leading up to the SWP monitoring campaign on 18/ 11/2021, during which the median observed SWP value was − 1.10 MPa. This value was used as threshold for defining the first CWS zone (CSW_abs 1, SWP _>_ − 1.10 MPa). By incrementing this observed SWP threshold by 25 % and 40 %, corresponding to a moderate and severe water deficit condition, respectively (Consoli et al., 2017; Saitta et al., 2021; Vanella et al., 2021), three additional CWS zones were obtained (i. e., CWS_abs 2: with SWP interval values ranging from − 1.10 MPa to 

− 1.34 MPa; CWS_abs 3: from − 1.34 MPa to − 1.54 MPa; and CWS_abs 4, SWP ≤− 1.54 MPa). 

The adopted relative approach relied on the quantile classification method. This method distributes attribute (SWP) values into equally sized classes, ensuring that each class contains the same number of observations (Brewer, 1994). Specifically, SWPint and SWPproxy ranges were distributed for each date into 4 groups (i.e., CWS_rel 1, CWS_rel 2, CWS_rel 3 and CWS_rel 4) containing an equal number of values. The decision to select 4 zones was driven by the number of zones chosen for the absolute approach, allowing for a direct comparison between these approaches. Both absolute and relative classification methods were implemented in QGIS software. 

In this study, an automated clustering algorithm named K-means (MacQueen, 1967) was also employed in this study. The K-means approach partitions observations into k clusters, with each observation belonging to the cluster with the nearest mean. Generally, K-means algorithm is affected by initialization and needs to be provided with the number of cluster a priori (Sinaga & Yang, 2020). To determine the cluster number and assess the homogeneity of the resulting clusters, the Silhouette index (SI, Rousseeuw, 1987) was calculated. The SI is a validity index which measures how similar an observation is to its own − cluster, compared to other clusters. Its values range from 1 to 1, where positive and negative high values indicate that the observation is well or 

6 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 5.** Correlation matrix between all measured (spectral reflectance bands and stem water potential values) or computed (vegetation indices) variables (significance level: * _p_ -value ≤ 0.05; ** _p_ -value ≤ 0.01; *** _p_ -value ≤ 0.001). 

poorly clustered, respectively. SI values around 0 suggest that observations are not clearly discriminated between clusters. Additionally, to validate the success of cluster delineation by applying the absolute and the relative approach, the SI was used as well. Both the K-means algorithm and SI were implemented using the “factoextra” (Kassambara & Mundt, 2017) and “cluster” (Maechler, 2019) packages. 

## **3. Results** 

## _3.1. Stem water potential and reflectance values_ 

Fig. 3 shows the trend and the variability of measured SWP values during the experimental trials, along with data on precipitation, irrigation, air temperature and relative humidity. Table A1 shows the values of these parameters on the monitoring campaign dates. The mean SWP values ranged from − 1.87 MPa (01/09/2021) to − 1.09 MPa (18/ 11/21); SWP variability, expressed in terms of coefficient of variation (CV), ranged from 9.6 % (12/05/2022) to 16.2 % (28/06/2022). The Kruskal-Wallis test indicated significant differences between measurement dates: SWP values were lower in September 2021 and June 2022, intermediate in July 2022, and higher on the remaining dates. Generally, SWP values were lowest during the FRG phenological stage (− 1.65 − MPa), intermediate during the FCD phenological stage ( 1.14 MPa), and highest during the FM phenological stage (− 1.09 MPa). 

Fig. 4 shows the reflectance temporal profiles at the study area for each band. For all SBs, reflectance values were highest during the FRG phenological stage, intermediate during the FCD phenological stage, and lowest during the FM phenological stage. Additionally, the reflectance values of the SBs were inversely related to the SWP values. 

## _3.2. Interpolated stem water potential maps_ 

Table 2 shows the statistical performances of the spatial interpolation methods (i.e., IDW, with α ranging from 0.5 to 2.0, in steps of 0.5) applied at the study area for determining maps of SWPint during the reference period. The scatterplots of SWPobs _versus_ SWPint, obtained by varying α, are reported in Fig. A1 (Supplementary material) for each –C5 of the validation subset. configuration C1 

In general, the best performance was observed when α was equal to 1.0, with average b and RSE values of 0.982 and 0.183 MPa, respectively, and average MAE, RMSE and PBIAS values of 0.130 MPa, 0.185 MPa and 1.827 %, respectively. For α = 0.5, average values for MAE, RMSE and PBIAS were 0.138 MPa, 0.192 MPa and 1.649 %, respectively; for α = 1.5 they were 0.123 MPa, 0.186 MPa, and 1.966 % and, finally, when α = 2.0 they were 0.136 MPa, 0.195 MPa and 2.033 %. Therefore, the percentage of bias showed an increasing trend as α increased from 0.5 to 2.0. In all cases, the significance level of the regressions, in terms of the _p_ -value, was lower than 0.001. Thus, the final SWPint maps were generated applying IDW with α = 1.0. 

## _3.3. Spatially distributed estimates of citrus water status_ 

## _3.3.1. Relationships between UAV-based multispectral imagery and stem water potential_ 

Fig. 5 shows the correlation matrix between all the variables considered in the study (i.e., SBs, VIs and SWPobs). The SWPobs was significantly correlated with all variables, except for red-edge, ARVI, SR, and NDVI. However, the correlation coefficients were quite low, ranging from − 0.37 to 0.24. 

7 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

were considered. The results are reported as follows: 

## **Table 3** 

Models based on vegetation indices to predict the stem water potential (SWPproxy) for each configuration C1–C5 of the training subset. 

**==> picture [256 x 87] intentionally omitted <==**

|Config.|Models|R2|R2-|RSE|RMSE|MAE|
|---|---|---|---|---|---|---|
||||Adj|(MPa)|(MPa)|(MPa)|
|C1|SWP ~ PS+GLI+|0.60|0.58|0.237|0.230|0.180|
||ARVI+ MSAVI||||||
|C2|SWP ~ PS+GLI+|0.59|0.57|0.224|0.217|0.170|
||ARVI+ MSAVI||||||
|C3|SWP ~ PS+GLI+|0.61|0.59|0.233|0.225|0.176|
||ARVI+ MSAVI||||||
|C4|SWP ~ PS+GLI+|0.66|0.65|0.214|0.207|0.159|
||ARVI+ MSAVI||||||
|C5|SWP ~ PS+GLI+|0.61|0.59|0.223|0.216|0.168|
||ARVI+ MSAVI||||||



− The intercept was lowest during the FRG period ( 1.249 MPa), in− termediate during the FCD period ( 0.792 MPa), and highest during the − FM period ( 0.651 MPa). In addition, the model showed a direct correlation with the GLI index and an inverse correlation with the ARVI and MSAVI indices. Testing the model on the validation subset, the median value for the correlation coefficient between predicted and observed values was 0.755, for MAE 0.186 MPa, for RMSE 0.237 MPa, and for 

## **Table 4** 

Statistical performances of the model based on vegetation indices applied to the – validation subset for each configuration C1 C5 (model without intercept). 

|Config.|Models||Slope|RSE|MAE|RMSE|PBIAS|PBIAS|**Table 5**|**Table 5**||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C1|SWPobs~||1.035|(MPa)<br>0.223|(MPa)<br>0.182|(MPa)<br>0.226|(%)<br>−4.24||Models based on spectral bands to predict the stem water potential (SWP<br>for each configuration C1–C5 of the training subset.|||||Models based on spectral bands to predict the stem water potential (SWP<br>C5 of the training subset.|Models based on spectral bands to predict the stem water potential (SWPproxy|
|C2|SWPproxy−<br>SWPobs~<br>SWPproxy−|1<br>1|0.982|0.245|0.189|0.244||2.26|Config.|Config.<br>Models|R2|R2-<br>Adj|RSE<br>(MPa)|RMSE<br>(MPa)|MAE<br>(MPa)|
|C3|SWPobs~||0.969|0.230|0.178|0.232||2.72|C1|M1: SWP ~ PS|0.59|0.57|0.240|0.240<br>0.234|0.184|
||SWPproxy−|1||||||||+ G+NIR||||||
|C4|SWPobs~||0.976|0.265|0.208|0.264||1.48|C2|M2: SWP ~ PS|0.58|0.56|0.225|0.225<br>0.219|0.170|
||SWPproxy−|1||||||||+ G+NIR||||||
|C5|SWPobs~||0.966|0.243|0.195|0.246||3.81|C3|M3: SWP ~ PS|0.59|0.57|0.236|0.236<br>0.230|0.177|
||SWPproxy−|1||||||||+ G+NIR||||||
||||||||||C4|M4: SWP ~ PS|0.65|0.63|0.218|0.218<br>0.212|0.164|
|||||||||||+ G+NIR||||||
|_3.3.2. Stem water potential prediction based on vegetation indices_<br>Due to the significant effect of measurement date on SWP and the|||||_Stem water potential prediction based on vegetation indices_<br>Due to the significant effect of measurement date on SWP and the|||_Stem water potential prediction based on vegetation indices_<br>Due to the significant effect of measurement date on SWP and the|C5|M5: SWP ~ PS<br>+ G+NIR|0.59|0.58|0.227|0.227<br>0.221|0.169|



Models based on spectral bands to predict the stem water potential (SWPproxy) – for each configuration C1 C5 of the training subset. 

_3.3.2. Stem water potential prediction based on vegetation indices_ 

Due to the significant effect of measurement date on SWP and the UAV information (Fig. 3 and Fig. 4), phenological stage (PS) was included as a covariate in the multiple linear regression model. The stepwise backward regression and the VIF test for each testing configuration produced the results summarized in Table 3. The same model was obtained for all the configurations, with independent variables being PS, GLI, ARVI, and MSAVI. The average values between the five configurations for R[2] , adjusted R[2] , RMSE and MAE were 0.61, 0.60, 0.219 MPa, 0.171 MPa, respectively. 

## **Table 6** 

Statistical performances of the model based on spectral bands applied to the – validation subset for each configuration C1 C5 (model without intercept). 

|Config.|Models||Slope|RSE<br>(MPa)|MAE<br>(MPa)|RMSE<br>(MPa)|PBIAS<br>(%)|
|---|---|---|---|---|---|---|---|
|C1|SWPobs~||1.031|0.227|0.186|0.229|–3.89|
||SWPproxy−|1||||||
|C2|SWPobs~||0.983|0.252|0.196|0.250|2.17|
|C3|SWPproxy−<br>SWPobs~<br>SWPproxy−|1<br>1|0.963|0.230|0.180|0.234|3.48|
|C4<br>C5|SWPobs~<br>SWPproxy−<br>SWPobs~<br>SWPproxy−|1<br>1|0.970<br>0.964|0.265<br>0.246|0.209<br>0.198|0.265<br>0.249|2.16<br>4.02|



The performances of the model applied to the validation subset are summarized in Table 4 and depicted in Fig. 6. The average values between the five configurations for MAE, RMSE and PBIAS were 0.190 MPa, 0.242 MPa, and 1.206 %, respectively. MAE and RMSE were about 11 % higher than those obtained with the training subset. 

To obtain unique coefficients, independent of the configuration, the model SWP ~ PS + GLI + ARVI + MSAVI was tested on 1000 random configurations (67 % testing and 33 % validation) and median values 

**Fig. 6.** Scatterplots of observed (SWPobs) vs predicted (SWPproxy) stem water potential using the vegetation indices for each configuration C1–C5 of the validation subset. 

8 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 7.** Scatterplots of observed (SWPobs) vs predicted (SWPproxy) stem water potential using the multispectral bands (SBs) for each configuration C1–C5 of the validation subset. 

**Table 7** 

Comparison among the spatial interpolation (IDW) and the stepwise linear regression models, based on the use of vegetation indices (VIs) or single spectral bands (SBs). 

|regression models, based on the use of vegetation indices (VIs) or single spectral<br>bands (SBs).|regression models, based on the use of vegetation indices (VIs) or single spectral|regression models, based on the use of vegetation indices (VIs) or single spectral|regression models, based on the use of vegetation indices (VIs) or single spectral|
|---|---|---|---|
|Statistical indicators|Spatial interpolation|UAV-based multispectral approach|UAV-based multispectral approach|
||IDW|VIs|SBs|
|MAE (MPa)|0.130|0.186|0.186|
|RMSE (MPa)|0.185|0.237|0.238|
|PBIAS (%)|1.827|–0.260|–0.130|
|R2||0.570|0.561|



## PBIAS − 0.26 %. 

_3.3.3. Stem water potential prediction based on spectral bands_ 

The relationships between SWPobs and SBs were studied by applying the same procedure as for VIs, i.e., including the PS as covariate in the independent variables. The stepwise backward regression and the VIF test for each testing configuration produced the results summarized in Table 5 . All models retained as significant independent variables the PS and the G and NIR bands. The average values between the five configurations for R[2] , adjusted R[2] , RMSE and MAE were 0.60, 0.58, 0.223 MPa, 0.173 MPa, respectively, very similar to those obtained when VIs were considered. 

The performances of the model applied to the validation subset are summarized in Table 6 and depicted in Fig. 7. The average values between the five configurations for MAE, RMSE and PBIAS were 0.194 MPa, 0.245 MPa, and 1.588 %, respectively. MAE was about 12 % and RMSE about 10 % higher than those obtained with the training subset. Comparing the two approaches, the performances of the model based on SBs were slightly: 0.194 vs 0.190 MPa for MAE, 0.245 vs 0.242 MPa for RMSE and 1.588 % vs 1.206 % for PBIAS. 

To obtain unique coefficients, the model was tested on 1000 random configurations (67 % testing and 33 % validation) and median values were considered, resulting as follows: 

SWPproxy = − 1 _._ 091 +14 _._ 393 G − 3 _._ 684 NIR (at FCD phenological stage) 

**==> picture [23 x 7] intentionally omitted <==**

## **Table 8** 

Stem water potential (SWP) thresholds used for mapping the citrus water status (CWS) management zones (i.e., CWS_rel 1, CWS_rel 2, CWS_rel 3 and CWS_rel 4) by applying the relative approach. IDW, SBs and VIs refer to the applied spatial interpolation and the UAV-based multispectral models, respectively. 

|Model|Date|SWP thresholds (MPa)|SWP thresholds (MPa)|||
|---|---|---|---|---|---|
|||CWS_rel|CWS_rel 2|CWS_rel 3|CWS_rel|
|||1|||4|
|IDW|01/09/|_>_–1.823|–1.823,|–1.901,|≤–1.927|
||2021||–1.901|–1.927||
||18/11/|_>_–1.087|–1.087,|–1.095,|≤–1.102|
||2021||–1.095|–1.102||
||12/04/|_>_–1.148|–1.148,|–1.154,|≤–1.168|
||2022||–1.154|–1.168||
||12/05/|_>_–1.108|–1.108,|–1.116,|≤–1.140|
||2022||–1.116|–1.140||
||28/06/|_>_–1.699|–1.699,|–1.728,|≤–1.742|
||2022||–1.728|–1.742||
|VIs|19/07/<br>2022<br>01/09/<br>2021|_>_–1.299<br>_>_–1.736|–1.299,<br>–1.362<br>–1.736,<br>–1.763|–1.362,<br>–1.406<br>–1.763,<br>–1.786|≤–1.406<br>≤–1.786|
||18/11/|_>_–1.118|–1.118,|–1.143,|≤–1.164|
||2021||–1.143|–1.164||
||12/04/|_>_–1.190|–1.190,|–1.226,|≤–1.263|
||2022||–1.226|–1.263||
||12/05/<br>2022|_>_–1.094|–1.094,<br>–1.121|–1.121,<br>–1.148|≤–1.148|
|SBs|28/06/<br>2022<br>19/07/<br>2022<br>01/09/<br>2021|_>_–1.585<br>_>_–1.565<br>_>_–1.694|–1.585,<br>–1.607<br>–1.565,<br>–1.602<br>–1.694,<br>–1.719|–1.607,<br>–1.628<br>–1.602,<br>–1.635<br>–1.719,<br>–1.741|≤–1.628<br>≤–1.635<br>≤–1.741|
||18/11/|_>_–1.104|–1.104,|–1.126,|≤–1.147|
||2021||–1.126|–1.147||
||12/04/<br>2022<br>12/05/|_>_–1.136<br>_>_–1.122|–1.136,<br>–1.159<br>–1.122,|–1.159,<br>–1.178<br>–1.145,|≤–1.178<br>≤–1.165|
||2022||–1.145|–1.165||
||28/06/|_>_–1.558|–1.558,|–1.581,|≤–1.602|
||2022||–1.581|–1.602||
||19/07/|_>_–1.553|–1.553,|–1.588,|≤–1.619|
||2022||–1.588|–1.619||



SWPproxy = − 1 _._ 574 +14 _._ 393 G − 3 _._ 684 NIR (at FRG phenological stage) 

**==> picture [23 x 8] intentionally omitted <==**

SWPproxy = − 0 _._ 957 +14 _._ 393 G − 3 _._ 684 NIR (at FM phenological stage) 

(12) 

The trend of the intercept was the same as in the previous approach: − lowest during the FRG period ( 1.574 MPa), intermediate during the 

FCD period (− 1.091 MPa), and highest during the FM period (− 0.957 MPa). In addition, the model showed a direct correlation with green reflectance and an inverse one with the NIR reflectance values. Testing the model on the validation subset, the median value for the correlation coefficient between predicted and observed values was of 0.749, for MAE 0.186 MPa, for RMSE 0.238 MPa, and for PBIAS − 0.13 %. All values were substantially the same as the model based on VIs, except PBIAS, which was better (− 0.130 % vs − 0.260 %). 

9 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**==> picture [225 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ah.<br>Wit @ o.<br>**----- End of picture text -----**<br>


**Fig. 8.** Citrus water status management zones obtained by the spatial interpolation (SWPint) and the UAV-based multispectral models (SWPproxy_VIs and SWPproxy_SBs) applying the absolute approach. 

_3.4. Comparison among the spatial interpolation and the UAV-based multispectral models_ 

The overall performances of the different modelling approaches proposed in this study, i.e. the spatial interpolation of SWPobs (IDW) and the stepwise linear regression model, based on the use of VIs or single SBs, are summarized in Table 7. 

## _3.5. Citrus water status management zones_ 

Table 8 shows the SWP threshold values used for mapping the 4 CWS management zones at the study site using the relative approach. 

The generated maps obtained applying the absolute, relative and the automated clustering algorithm K-means approaches are reported in Figs. 8–10. Note that CWS values, even if spatialized at the orchard level, refer only to the tree canopies, thus excluding soil interference. 

10 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 9.** Citrus water status management zones obtained by the spatial interpolation (SWPint) and the UAV-based multispectral models (SWPproxy_VIs and SWPproxy_SBs) by applying the relative approach. 

Tables 8–10 report the performance, in terms of Silhouette Index (SI), in delineating the CWS management zones at the study area by applying the absolute, relative, and the K-means approach, respectively. Note that Table 10 also includes the resulting SWP thresholds (center, minimum and maximum values) of each CWS management zone obtained by applying the K-means. An overall comparison among the applied approaches is reported in Table 11. In general, more powerful CWS management zones were obtained by the absolute approach, with average SI 

values of 0.65, 0.68 and 0.63, respectively, for the spatial interpolation and the VIs and SBs based-models. An intermediate performance was observed for the K-means, with average SI values of 0.57, 0.54 and 0.54, respectively, for the spatial interpolation and the VIs and SBs basedmodels. A lower performance was observed instead for the relative approach, with average SI values of 0.39, 0.45 and 0.44, respectively, for the spatial interpolation and the VIs and SBs based-models. 

11 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

**Fig. 10.** Citrus water status management zones obtained by the spatial interpolation (SWPint) and the UAV-based multispectral models (SWPproxy_VIs and SWPproxy_SBs) by applying the K-means approach. 

## **4. Discussion** 

Nowadays, determining spatial variability within agricultural fields is feasible using novel approaches and multiple data sources to outline management zone for precision agricultural purposes (Ohana-Levi et al., 2021b). In general, the quality of homogenous management zones depends on the quality of the data collection phase, which requires a high number of representative and robust measurements of specific 

characteristics with a fair temporal resolution (Arrouays et al., 2020). In this study, a protocol was developed to assess CWS and delineate management zones in a citrus orchard. Multiple data sources were used for this purpose, including point-based ground data (e.g., SWP) and spatially distributed UAV-based information (e.g., VIs and SBs). Specifically, two different approaches were proposed: the spatial interpolation of SWPobs and the stepwise linear regression model based on the use of VIs or single SBs. The performances of these approaches are 

12 

_G. Longo-Minnolo et al.                                                                                                                                                                                                                       Computers and Electronics in Agriculture 222 (2024) 109098_ 

## **Table 9** 

Performance of the absolute and relative approaches in delineating the citrus water status (CWS) management zones. The Silhouette Index (SI) and the number of trees (n.) included in each zone are also reported. IDW, SBs and VIs refer to the applied spatial interpolation and the UAV-based multispectral models, respectively. 

|Date<br>CWS management zone|Absolute approach||SBs<br>_SI_<br>_n._|Relative approach||SBs<br>_SI_<br>_n._|
|---|---|---|---|---|---|---|
||IDW<br>_SI_<br>_n._|VIs<br>_SI_<br>_n._||IDW<br>_SI_<br>_n._|VIs<br>_SI_<br>_n._||
|01/09/2021<br>1<br>2<br>3<br>4<br>18/11/2021<br>1<br>2<br>3<br>4<br>12/04/2022<br>1<br>2<br>3<br>4<br>12/05/2022<br>1<br>2<br>3<br>4<br>28/06/2022<br>1<br>2<br>3<br>4<br>19/07/2022<br>1<br>2<br>3<br>4|–<br>–<br>–<br>–<br>0.54<br>2<br>0.77<br>298<br>0.36<br>208<br>0.58<br>92<br>–<br>–<br>–<br>–<br>0.74<br>16<br>0.63<br>283<br>0.85<br>1<br>–<br>–<br>0.64<br>40<br>0.43<br>259<br>0.98<br>1<br>–<br>–<br>–<br>–<br>0.68<br>2<br>0.65<br>4<br>0.77<br>294<br>0.93<br>1<br>0.64<br>109<br>0.55<br>188<br>0.91<br>2|–<br>–<br>–<br>–<br>–<br>–<br>0.80<br>300<br>0.63<br>34<br>0.57<br>266<br>–<br>–<br>–<br>–<br>0.84<br>6<br>0.41<br>294<br>–<br>–<br>–<br>–<br>0.63<br>62<br>0.45<br>238<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>0.84<br>4<br>0.52<br>296<br>–<br>–<br>–<br>–<br>0.60<br>12<br>0.54<br>288|–<br>–<br>–<br>–<br>–<br>–<br>0.79<br>300<br>0.64<br>64<br>0.51<br>236<br>–<br>–<br>–<br>–<br>0.69<br>35<br>0.59<br>265<br>–<br>–<br>–<br>–<br>0.68<br>20<br>0.54<br>280<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>0.68<br>22<br>0.53<br>278<br>–<br>–<br>–<br>–<br>0.51<br>18<br>0.58<br>282|0.41<br>81<br>0.44<br>73<br>0.86<br>74<br>0.09<br>72<br>−0.01<br>78<br>0.66<br>74<br>0.69<br>75<br>0.05<br>73<br>0.02<br>74<br>0.81<br>78<br>0.30<br>75<br>0.10<br>73<br>0.03<br>74<br>0.83<br>75<br>0.33<br>80<br>0.33<br>71<br>0.04<br>72<br>0.43<br>76<br>0.74<br>80<br>0.00<br>72<br>0.61<br>68<br>0.47<br>71<br>0.65<br>75<br>0.53<br>86|0.18<br>40<br>0.58<br>64<br>0.60<br>70<br>0.40<br>126<br>0.20<br>64<br>0.58<br>72<br>0.62<br>83<br>0.38<br>81<br>0.33<br>95<br>0.61<br>74<br>0.58<br>50<br>0.30<br>81<br>0.30<br>53<br>0.60<br>108<br>0.60<br>89<br>0.29<br>50<br>0.34<br>80<br>0.58<br>84<br>0.60<br>88<br>0.35<br>48<br>0.19<br>38<br>0.59<br>68<br>0.61<br>96<br>0.34<br>98|0.20<br>39<br>0.58<br>46<br>0.60<br>63<br>0.41<br>152<br>0.27<br>73<br>0.59<br>55<br>0.59<br>76<br>0.39<br>96<br>0.18<br>64<br>0.59<br>62<br>0.62<br>89<br>0.30<br>85<br>0.23<br>59<br>0.59<br>78<br>0.61<br>113<br>0.36<br>50<br>0.24<br>60<br>0.59<br>76<br>0.60<br>84<br>0.35<br>80<br>0.06<br>34<br>0.58<br>66<br>0.60<br>91<br>0.42<br>109|



summarized in Table 7. 

Overall, the performance of the proposed approaches was quite similar, with slightly more accurate IDW values in terms of MAE and RMSE than the regression models, but not in terms of PBIAS. Therefore, the SBs-based regression model showed the best results (Table 8). For this reason, using the above metrics, it is difficult to establish the most reliable approach. However, some practical considerations can be deduced. 

In particular, the spatial interpolation approach is simpler than implementing stepwise linear regression models with multispectral imagery, requiring easier data processing. On the other hand, while it solves the problem of spatial distribution of point-based ground data, it requires in all cases the _in situ_ measurements of SWP using pressure chambers. Therefore, this approach might not be easily recommended, especially over large areas, as it would necessitate a very extensive SWP field campaign. 

In this sense, remote sensing techniques offer non-destructive and fast methodologies. In particular, the use of UAV-based imaging could provide valuable opportunities to map the water status of crops in a costeffective way (van der Merwe et al., 2020; Tang et al., 2022; Wiederstein et al., 2022). 

The VIs calculated from VNIR regions have been shown to be effective in detecting the crop water status (Rossini et al., 2013). In this study, our methodological approach allowed us to infer the dynamics of crop water status under specific temporal conditions, even when referring to a specific cultivar on a single plot. However, the climate regime under study may be considered representative of Mediterranean areas, where citrus groves are typically cultivated. In addition, the explored timesteps describe the phenological dynamics occurring under these evergreen groves. 

Several authors have found quite good correlations between VIs (e. g., NDVI, NDRE, NDGI, OSAVI) and water status in different crops (Baluja et al., 2012; Rallo et al., 2014; Poças et al., 2015ˆ ). For citrus orchards, Waldo & Schumann (2009) observed a significant correlation between SWP and NDVI (R[2 ] of 0.31). In our study, none of the analyzed SBs and VIs showed a strong correlation with SWP, with the highest coefficients of correlation observed for red-edge (− 0.37) and MSAVI 

(− 0.32), respectively (Fig. 5). 

However, when stepwise linear regression was applied, combing the available information (i.e., VIs in scenario 1 and SBs in scenario 2), better results were observed (Tables 4 and 6). The models, built with ARVI, GLI and MSAVI in scenario 1, and with G and NIR bands in scenario 2, estimated SWP with coefficients of correlation of 0.76 and 0.75, respectively. This selection of multispectral information in the models as the best predictors of CWS, may be attributed to the fact that G, NIR and R (the main bands in the VIs mentioned above) are commonly associated Kazmierski et al., 2011; Rossini et al., 2013; Gamon et al., 2015; Pwith physiological modifications of the crop (Zygielbaum et al., 2009; oças ˆ et al., 2015). 

Similarly, Romero et al. (2018) improved vineyard SWP estimates by applying artificial neural networks on several VIs. In some cases, multispectral information on VNIR is not sufficient to fully detect the crop water status, while temperature-based approaches have proven to be more reliable for capturing abiotic and biotic stress conditions (RamírezCuesta et al., 2022). However, the ability of thermal methods to determine plant stress using proximal and/or remote sensing data may be limited by latency issues and the pixel resolution of thermal infrared sensors (Consoli and Vanella, 2014; Knipper et al., 2019). 

The methodology proposed in this study for mapping the water status of citrus groves can contribute to the definition of management zones, thereby supporting decisions made by local farmers regarding the release of agronomic inputs such as irrigation, nutrients, plant protection products. Several studies have evaluated the impacts related to the adoption of zoning approaches for precision irrigation, highlighting the benefits in terms of water/energy savings and increased yield (e.g., Fontanet et al., 2020; Souza & Rodrigues, 2022). However, care must be taken to correctly interpret zoning maps by non-expert users (Arrouays et al., 2020). 

In this research, the management zones of the CWS have been defined by applying a scientifically based approach (absolute), a relative one and an automated clustering algorithm. Specifically, Figs. 8–10 and Tables 9–10 show different zoning areas obtained by applying these approaches, starting from the same dataset inputs. Generally, more powerful CWS management zones were obtained by applying the 

13 

_G. Longo-Minnolo et al.                                                                                                                                                                                                                       Computers and Electronics in Agriculture 222 (2024) 109098_ 

## **Table 10** 

Performance of the K-means in delineating the citrus water status (CWS) management zones. The stem water potential (SWP) thresholds (center, minimum and maximum values), the Silhouette Index (SI) and the number of trees (n.) included in each zone are also reported. IDW, SBs and VIs refer to the applied spatial interpolation and the UAV-based multispectral models, respectively. 

|Date|Model|CWS management zone|SWP center (MPa)|SWP min (MPa)|SWP max (MPa)|SI|n.|
|---|---|---|---|---|---|---|---|
|01/09/2021|IDW|1|−1.800|−1.867|−1.327|0.57|127|
|||2|−1.930|−2.232|−1.867|0.68|173|
||SBs|1|−1.670|−1.704|−1.371|0.48|58|
|||2|−1.740|−1.860|−1.704|0.61|242|
||VIs|1|−1.710|−1.746|−1.449|0.48|59|
|||2|−1.780|−1.905|−1.746|0.61|241|
|18/11/2021|IDW|1|−1.050|−1.070|−0.968|0.46|137|
|||2|−1.090|−1.096|−1.070|0.56|25|
|||3|−1.110|−1.227|−1.096|0.49|138|
||SBs|1|−1.090|−1.121|−0.895|0.52|185|
|||2|−1.150|−1.234|−1.121|0.58|115|
||VIs|1|−1.100|−1.129|−0.863|0.49|199|
|||2|−1.160|−1.266|−1.129|0.60|101|
|12/04/2022|IDW|1|−1.100|−1.128|−0.973|0.58|41|
|||2|−1.160|−1.177|−1.128|0.69|53|
|||3|−1.200|−1.431|−1.177|0.45|206|
||SBs|1|−1.120|−1.146|−0.700|0.48|178|
|||2|−1.170|−1.300|−1.146|0.58|122|
||VIs|1|−1.190|−1.232|−0.925|0.55|119|
|||2|−1.280|−1.644|−1.232|0.53|181|
|12/05/2022|IDW|1|−1.080|−1.098|−0.976|0.48|40|
|||2|−1.110|−1.133|−1.098|0.64|100|
|||3|−1.150|−1.349|−1.133|0.53|160|
||SBs|1|−1.110|−1.136|−0.886|0.50|209|
|||2|−1.160|−1.303|−1.136|0.58|91|
||VIs|1|−1.090|−1.122|−0.899|0.55|204|
|||2|−1.160|−1.445|−1.122|0.53|96|
|28/06/2022|IDW|1|−1.610|−1.672|−1.114|0.73|42|
|||2|−1.730|−2.046|−1.672|0.42|258|
||SBs|1|−1.540|−1.573|−1.356|0.57|179|
|||2|−1.600|−1.717|−1.573|0.50|121|
||VIs|1|−1.580|−1.604|−1.418|0.54|151|
|||2|−1.630|−1.759|−1.604|0.56|149|
|19/07/2022|IDW|1|−1.290|−1.349|−1.060|0.60|125|
|||2|−1.400|−1.577|−1.349|0.64|175|
||SBs|1|−1.500|−1.555|−0.866|0.43|249|
|||2|−1.610|−1.783|−1.555|0.62|51|
||VIs|1|−1.540|−1.585|−1.176|0.49|228|
|||2|−1.630|−2.113|−1.585|0.58|72|



## **Table 11** 

Comparison in terms of average Silhouette Index (SI) values among the applied approaches (i.e. absolute, relative, and K-means approaches) for delineating the citrus water status (CWS) management zones at the study site. IDW, SBs and VIs refer to the applied spatial interpolation and the UAV-based multispectral models, respectively. 

|<br>respectively.||||
|---|---|---|---|
|Date|Absolute approach<br>_IDW_<br>_SBs_<br>_VIs_|Relative approach<br>_IDW_<br>_SBs_<br>_VIs_|K-means<br>_IDW_<br>_SBs_<br>_VIs_|
|01/09/2021<br>18/11/2021<br>12/04/2022<br>12/05/2022<br>28/06/2022<br>19/07/2022<br>Overall|0.44<br>0.80<br>0.85<br>0.47<br>0.58<br>0.60<br>0.74<br>0.64<br>0.68<br>0.68<br>0.61<br>0.64<br>0.70<br>0.61<br>0.68<br>0.76<br>0.60<br>0.64<br>0.65<br>0.63<br>0.68|0.45<br>0.45<br>0.44<br>0.35<br>0.46<br>0.45<br>0.31<br>0.42<br>0.46<br>0.38<br>0.45<br>0.45<br>0.30<br>0.45<br>0.47<br>0.57<br>0.42<br>0.43<br>0.39<br>0.44<br>0.45|0.63<br>0.55<br>0.55<br>0.50<br>0.55<br>0.55<br>0.57<br>0.53<br>0.54<br>0.55<br>0.54<br>0.54<br>0.58<br>0.54<br>0.55<br>0.62<br>0.53<br>0.54<br>0.57<br>0.54<br>0.54|



absolute approach for all methods (i.e. spatial interpolation and SBs and VIs based models) (Table 11). Thus, the conducted application suggests that the setting of zoning classes plays a critical role in the identification of reliable homogeneous areas. 

In fact, the relative approach, based on the distribution by quantile of data commonly used by most UAV agricultural service providers, could lead to incorrect interpretations of the maps (i.e., unrealistic scattered zones in terms of SWP thresholds). Note that the interval derived from the quantile approach classification is too small (0.01–0.02 MPa) to describe relevant differences among the CWS classes (Table 8 and Fig. 9). Additionally, classes may vary over time, presenting a challenge in identifying the optimal moment to perform zoning. 

To overcome this shortcoming, further research is needed, primarily focused on defining the optimal number of zoning classes based on the variations of single variables over time (e.g., needs to provide sitespecific SWP thresholds). Alternatively, a temporal approach could be applied. Determining a composite map where each pixel receives the main statistical values from multiple acquisitions over different phenological stages could be a compromise for the end-users who wish to maintain static CWS management zones during the growing season. 

Moreover, these outputs provide practical insights for the management of the orchard under study. Specifically, the spatial patterns obtained in Figs. 8–10 depict areas of the plot characterized by different sensitivities or response to the water stress (Fernandez, 2014; Gonzalez- ´ 

14 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

_G. Longo-Minnolo et al._ 

Dugo et al., 2021). This information serves as a basis for adopting precision irrigation criteria. For example, it can support farmers in selecting locations for installing point-based sensors to monitor crop and soil water conditions in the field or making other management decisions, such as applying different irrigation volumes depending on the agronomic objectives they wish to achieve. 

## **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Data availability** 

## **5. Conclusions** 

Data will be made available on request. 

In this study, a methodological protocol was developed to determine the CWS and delineate management zones using different alternatives: (i) point-based ground data (e.g., SWP) and; (ii) UAV-based spatially distributed information (i.e. multispectral imaging). The main conclusions of the study can be summarized as follows: 

- IDW is an easy-to-use spatial interpolation method for obtaining accurate estimates of CWS. However, its use is not recommended for large areas due to the extensive SWP measurement campaigns required. 

- None of the analyzed SBs and VIs, calculated with VNIR information acquired from UAVs, showed strong correlation with SWP. 

- The combination of SBs and VIs, using stepwise linear regression models provided reliable estimates of CWS. Compared to IDW, this method is quicker and more cost-effective for mapping CWS, but requires more detailed data processing. 

- Caution should be exercised in interpreting CWS maps. Setting zoning classes with a relative approach can lead to erroneous interpretations. A scientific-driven approach, based on fixed thresholds suggested by the literature, could be more reliable. K-means clustering algorithm showed intermediate performance. 

## **Acknowledgements** 

This work was carried out within the framework of: (i) the project “Miglioramento delle produzioni agroalimentari mediterranee in condizioni di carenza di risorse idriche - WATER4AGRIFOOD” (Cod. progetto: ARS01_00825; cod. CUP: B64I20000160005, “PON “RICERCA E INNOVAZIONE” 2014-2020, Azione II - Obiettivo Specifico 1b), (ii) the project PRIMA 2020 HANDYWATER “Handy tools for sustainable irrigation management in Mediterranean crops” (PCI2021-121940),(iii) the project Agritech National Research Center receiving funding from the European Union Next-GenerationEU (PIANO NAZIONALE DI RIPRESA E RESILIENZA (PNRR)—MISSIONE 4 COMPONENTE 2, INVESTIMENTO 1.4—D.D. 1032 17 June 2022, CN00000022), (iv) the project “IRRIAP” receiving funding from “Mis. 16.1 del PSR-Sicilia 2014/2022”, and (v) the Research Project of National Relevance (PRIN 2022) entitled “Smart Technologies and Remote Sensing methods to support the sustainable Agriculture WAter Management of Mediterranean woody Crops - ” SWAM4Crops . 

## **Appendix A. Supplementary material** 

The methodological protocol developed in this study could represent a powerful tool for identifying the temporal and spatial variability of CWS characteristics, supporting the adoption of precision agriculture criteria. Specifically, it could be used for preliminary field investigations, necessary for the installation of point-based sensors to monitor the crop and/or soil water status, or for applying different irrigation volumes to the crops. 

However, some limitations should be considered and further investigated. This study explored a single plot within a specific time period, limiting the generalizability of the findings to other crops or different environmental conditions. Therefore, the site-specific nature of the proposed spatial and temporal application could be improved by testing the protocol on other crops and in various climate conditions. As a result, the use of fixed SWP thresholds could lead to inaccuracies, since the response to water stress is crop-specific. Further analyses could define thresholds based on others parameters rather than SWP. 

Additionally, multispectral information from VNIR is not sufficient to fully detect water stress conditions. Thus, incorporating TIR information could provide a more reliable assessment of crop water status. Finally, applying the proposed approach over large areas using satellite images, could be evaluated to obtain a broader spatial assessment of crop water status, enhancing water resources management in agriculture. 

## **CRediT authorship contribution statement** 

**Giuseppe Longo-Minnolo:** Writing – review & editing, Investigation. **Simona Consoli:** Writing – review & editing, Supervision, Investigation, Funding acquisition, Conceptualization. **Daniela Vanella:** Writing – review & editing, Supervision, Methodology, Investigation, Conceptualization. **Salvatore Pappalardo:** Investigation. **Serena Guarrera:** Investigation, Data curation. **Giuseppe Manetto:** Investigation, Writing – review & editing. **Emanuele Cerruto:** Writing – review & editing, Visualization, Supervision, Software, Methodology, Investigation. 

Supplementary data to this article can be found online at https://doi. org/10.1016/j.compag.2024.109098. 

## **References** 

Acevedo-Opazo, C., Vald´es-Gomez, H., Taylor, J.A., Avalo, A., Verdugo-V´ asquez, N., ´ Araya, M., Jara-Rojas, F., Tisseyre, B., 2013. Assessment of an empirical spatial prediction model of vine water status for irrigation management in a grapevine field. Agric. Water Manag. 124, 58–68. 

Arrouays, D., McBratney, A., Bouma, J., Libohova, Z., Richer-de-Forges, A.C., Morgan, C. L., Roudier, P., Poggio, L., Mulder, V.L., 2020. Impressions of digital soil maps: The good, the not so good, and making them ever better. Geoderma Reg. 20, e00255. ISO 690. 

Ballester, C., Castel, J., Intrigliolo, D.S., Castel, J.R., 2013. Response of Navel Lane Late citrus trees to regulated deficit irrigation: yield components and fruit composition. Irrig. Sci. 31, 333–341. 

Baluja, J., Diago, M.P., Balda, P., Zorer, R., Meggio, F., Morales, F., Tardaguila, J., 2012. Assessment of vineyard water status variability by thermal and multispectral imagery using an unmanned aerial vehicle (UAV). Irrig. Sci. 30, 511–522. 

- Barnes, E.M., Clarke, T.R., Richards, S.E., Colaizzi, P.D., Haberland, J., Kostrzewski, M., Waller, P., Choi, C., Riley, E., Thompson, T., Lascano, R.J., Li, H., Moran, M.S., 2000. Coincident detection of crop water stress, nitrogen status and canopy density using ground based multispectral data. In: Proceedings of the Fifth International Conference on Precision Agriculture, Bloomington, MN, USA, Vol. 1619, p. 6. 

- Behmann, J., Steinrücken, J., Plümer, L., 2014. Detection of early plant stress responses in hyperspectral images. ISPRS J. Photogramm. Remote Sens. 93, 98–111. 

- Birth, G.S., McVey, G.R., 1968. Measuring the color of growing turf with a reflectance spectrophotometer 1. Agron. J. 60 (6), 640–643. 

- Brewer, C.A., 1994. Cartography: thematic map design. Cartogr. Perspect. 17, 26–27. ISO 690 (pp. 138-160). 

- Chamard, P., Courel, M.F., Docousso, M., Gu´en´egou, M.C., LeRhun, J., Levasseur, J., Togola, M., 1991. Utilisation des bandes spectrales du vert et du rouge pour une meilleure ´evaluation des formations v´eg´etales actives In T´el´ed´etection et Cartographie; AUPELF–UREF: Sherbrooke, QC, Canada, pp. 203–209. 

- Consoli, S., Stagno, F., Roccuzzo, G., Cirelli, G.L., Intrigliolo, F., 2014. Sustainable management of limited water resources in a young orange orchard. Agric. Water Manag. 132, 60–68. 

- Consoli, S., Stagno, F., Vanella, D., Boaga, J., Cassiani, G., Roccuzzo, G., 2017. Partial root–zone drying irrigation in orange orchards: effects on water use and crop production characteristics. Eur. J. Agron. 82, 190–202. 

- Consoli, S., Vanella, D., 2014. Comparisons of satellite-based models for estimating evapotranspiration fluxes. J. Hydrol. 513, 475–489. 

15 

_G. Longo-Minnolo et al.                                                                                                                                                                                                                       Computers and Electronics in Agriculture 222 (2024) 109098_ 

Cordoba, M.A., Bruno, C.I., Costa, J.L., Peralta, N.R., Balzarini, M.G., 2016. Protocol for ´ multivariate homogeneous zone delineation in precision agriculture. Biosyst. Eng. 143, 95–107. 

- Corell, M., Martín-Palomo, M.J., Giron, I., Andreu, L., Galindo, A., Centeno, A., P´ ´erezLopez, D., Moriana, A., 2020. Stem water potential´ –based regulated deficit irrigation scheduling for olive table trees. Agric. Water Manag. 242, 106418. 

- de Mendiburu, F., 2023. agricolae: Statistical Procedures for Agricultural Research. R package version 1.3-6. https://CRAN.R-project.org/package=agricolae. 

Doerge, T., 1999. Defining management zones for precision farming. Crop Insights 8, 1–5. 

Efroymson, M.A., 1960. Multiple regression analysis. Math. Methods Dig. Comput. 191–203. 

- Fernandez, J.E., 2014. Plant-based sensing to monitor water stress: applicability to ´ commercial orchards. Agric. Water Manag. 142, 99–109. 

- Fontanet, M., Scudiero, E., Skaggs, T.H., Fern`andez-Garcia, D., Ferrer, F., Rodrigo, G., Bellvert, J., 2020. Dynamic management zones for irrigation scheduling. Agric. Water Manag. 238, 106207. 

- Fox, J., Weisberg, S., 2019. An R Companion to Applied Regression, Third edition. Sage, Thousand Oaks CA. 

- Gamon, J.A., Surfus, J.S., 1999. Assessing leaf pigment content and activity with a reflectometer. New Phytol. 143 (1), 105–117. 

- Gamon, J.A., Kovalchuck, O., Wong, C.Y.S., Harris, A., Garrity, S.R., 2015. Monitoring seasonal and diurnal changes in photosynthetic pigments with automated PRI and NDVI sensors. Biogeosciences 12 (13), 4149–4159. 

- Gitelson, A.A., Kaufman, Y.J., Stark, R., Rundquist, D., 2002. Novel algorithms for remote estimation of vegetation fraction. Remote Sens. Environ. 80 (1), 76–87. 

- Gobron, N., Pinty, B., Verstraete, M.M., Widlowski, J.L., 2000. Advanced vegetation indices optimized for up–coming sensors: design, performance, and applications. IEEE Trans. Geosci. Remote Sens. 38 (6), 2489–2505. 

Gonzalez-Dugo, V., Zarco-Tejada, P.J., Intrigliolo, D.S., Ramírez-Cuesta, J.M., 2021. Normalization of the crop water stress index to assess the within-field spatial variability of water stress sensitivity. Precis. Agric. 22, 964–983. 

- Huete, A.R., 1988. A soil–adjusted vegetation index (SAVI). Remote Sens. Environ. 25 (3), 295–309. 

Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sens. Environ. 83 (1–2), 195–213. 

- Inman, D., Khosla, R., Reich, R., Westfall, D.G., 2008. Normalized difference vegetation index and soil color-based management zones in irrigated maize. Agron. J. 100 (1), 60–66. 

- James, G., Witten, D., Hastie, T., Tibshirani, R., 2013. An Introduction to Statistical Learning Vol. 112, 18. 

- Jiang, Q., Fu, Q., Wang, Z., 2011. Delineating site-specific irrigation management zones. Irrig. Drain. 60 (4), 464–472. 

- Kassambara, A., Mundt, F., 2017. Package ‘factoextra’. Extract and Visualize the Results of Multivariate Data Analyses. 

- Kaufman, Y.J., Tanre, D., 1992. Atmospherically resistant vegetation index (ARVI) for EOS–MODIS. IEEE Trans. Geosci. Remote Sens. 30 (2), 261–270. 

Kazmierski, M., Gl´emas, P., Rousseau, J., Tisseyre, B., 2011. Temporal stability of within–field patterns of NDVI in non irrigated Mediterranean vineyards. Oeno One 45 (2), 61–73. 

- Knipper, K.R., Kustas, W.P., Anderson, M.C., Alfieri, J.G., Prueger, J.H., Hain, C.R., Gao, F., Yang, Y., McKee, L.G., Nieto, H., Hipps, L.E., Alsina, M.M., Sanchez, L., 2019. Evapotranspiration estimates derived using thermal-based satellite remote sensing and data fusion for irrigation management in California vineyards. Irrig. Sci. 37, 431–449. 

Leo, S., Migliorati, M.D.A., Nguyen, T.H., Grace, P.R., 2023. Combining remote 

- sensing–derived management zones and an auto–calibrated crop simulation model to determine optimal nitrogen fertilizer rates. Agr. Syst. 205, 103559. 

Lin, Y., Zhu, Z., Guo, W., Sun, Y., Yang, X., Kovalskyy, V., 2020. Continuous monitoring of cotton stem water potential using sentinel-2 imagery. Remote Sens. (Basel) 12 (7), 1176. 

Longo-Minnolo, G., Vanella, D., Consoli, S., Pappalardo, S., Ramírez-Cuesta, J.M., 2022. 

- Assessing the use of ERA5–Land reanalysis and spatial interpolation methods for retrieving precipitation estimates at basin scale. Atmos. Res. 271, 106131. 

- MacQueen, J., 1967, June. Some methods for classification and analysis of multivariate observations. In: Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1, No. 14, pp. 281–297. 

- Maechler, M., 2019. Finding groups in data: Cluster analysis extended Rousseeuw et al. R package version, 2(0), pp. 242–248. 

Maran˜on, M., Fern´ ´andez-Novales, J., Tardaguila, J., Guti´errez, S., Diago, M.P., 2023. NIR attribute selection for the development of vineyard water status predictive models. Biosyst. Eng. 229, 167–178. 

Martínez-Gimeno, M.A., Bonet, L., Provenzano, G., Badal, E., Intrigliolo, D.S., Ballester, C., 2018. Assessment of yield and water productivity of clementine trees under surface and subsurface drip irrigation. Agric. Water Manag. 206, 209–216. McCluney, W.R., 2014. Introduction to Radiometry and Photometry. Artech House. 

- Motisi, A., Rossi, F., Consoli, S., Papa, R., Minacapilli, M., Rallo, G., Cammalleri, C., D’Urso, G., 2012. Eddy covariance and sap flow measurement of energy and mass exchanges of woody crops in a Mediterranean environment. Acta Hortic. 951, 121–127. https://doi.org/10.17660/ActaHortic.2012.951.14. 

Ohana-Levi, N., Bahat, I., Peeters, A., Shtein, A., Netzer, Y., Cohen, Y., Ben-Gal, A., 2019. A weighted multivariate spatial clustering model to determine irrigation management zones. Comput. Electron. Agric. 162, 719–731. 

- Ohana-Levi, N., Gao, F., Knipper, K., Kustas, W.P., Anderson, M.C., del Mar Alsina, M., Sanchez, L.A., Karnieli, A., 2021a. Time–series clustering of remote sensing retrievals for defining management zones in a vineyard. Irrig. Sci. 1–15. 

- Ohana-Levi, N., Ben-Gal, A., Peeters, A., Termin, D., Linker, R., Baram, S., Raveh, E., PazKagan, T., 2021b. A comparison between spatial clustering models for determining N–fertilization management zones in orchards. Precis. Agric. 22, 99–123. 

- Oldoni, H., Bassoi, L.H., 2016. Delineation of irrigation management zones in a Quartzipsamment of the Brazilian semiarid region. Pesq. Agrop. Brasileira 51, 1283–1294. 

Pampuri, A., Tugnolo, A., Bianchi, D., Giovenzana, V., Beghi, R., Fontes, N., Oliveira, H. M., Casson, A., Brancadoro, L., Guidetti, R., 2021. Optical specifications for a proximal sensing approach to monitor the vine water status in a distributed and autonomous fashion. Biosyst. Eng. 212, 388–398. 

- Pappalardo, S., Consoli, S., Longo-Minnolo, G., Vanella, D., Longo, D., Guarrera, S., D’Emilio, A., Ramírez-Cuesta, J.M., 2023. Performance evaluation of a low-cost 

- P´erez-Pthermal camera for citrus water status estimation. Agric. Water Manag. 288, 108489fruit growth stages on ‘Star Ruby´erez, J.G., Robles, J.M., Botía, P., 2014. Effects of deficit irrigation in different ’grapefruit trees in semi–arid conditions. Agric. . Water Manag. 133, 44–54. 

- Poças, I., Rodrigues, A., Gonçalves, S., Costa, P.M., Gonçalves, I., Pereira, L.S., Cunha, M., ˆ 2015. Predicting grapevine water status based on hyperspectral reflectance vegetation indices. Remote Sens. (Basel) 7 (12), 16460–16479. 

- Posit team, 2023. RStudio: Integrated Development for R, Version 2023.3. 0.386. Posit Software, PBC. https://posit.co/. 

- Qi, J., Chehbouni, A., Huete, A.R., Kerr, Y.H., Sorooshian, S., 1994. A modified soil adjusted vegetation index. Remote Sens. Environ. 48 (2), 119–126. 

- R Core Team, 2021. R: A Language and Environment for Statistical Computing; R Foundation for Statistical Computing: Vienna, Austria. Available online: https: //www.R-project.org (accessed on 11 April 2022). 

Rallo, G., Minacapilli, M., Ciraolo, G., Provenzano, G., 2014. Detecting crop water status in mature olive groves using vegetation spectral measurements. Biosyst. Eng. 128, 52–68. 

- Ramírez-Cuesta, J.M., Consoli, S., Longo, D., Longo-Minnolo, G., Intrigliolo, D.S., Vanella, D., 2022. Influence of short-term surface temperature dynamics on tree 

- Robles, J.M., Botía, P., Porchards energy balance fluxes. Precis. Agric. 23 (4), 1394´erez-P´erez, J.G., 2016. Subsurface drip irrigation affects trunk –1412. diameter fluctuations in lemon trees, in comparison with surface drip irrigation. Agric. Water Manag. 165, 11–21. 

Romero, M., Luo, Y., Su, B., Fuentes, S., 2018. Vineyard water status estimation using multispectral imagery from an UAV platform and machine learning algorithms for irrigation scheduling management. Comput. Electron. Agric. 147, 109–117. 

- Rondeaux, G., Steven, M., Baret, F., 1996. Optimization of soil–adjusted vegetation indices. Remote Sens. Environ. 55 (2), 95–107. 

Rossini, M., Fava, F., Cogliati, S., Meroni, M., Marchesi, A., Panigada, C., Giardino, C., Busetto, L., Migliavacca, M., Amaducci, S., Colombo, R., 2013. Assessing canopy PRI from airborne imagery to map water stress in maize. ISPRS J. Photogramm. Remote Sens. 86, 168–177. 

Roujean, J.L., Breon, F.M., 1995. Estimating PAR absorbed by vegetation from bidirectional reflectance measurements. Remote Sens. Environ. 51 (3), 375–384. Rouse, J.W., Haas, R.H., Schell, J.A., Deering, D.W., 1974. Monitoring vegetation systems in the Great Plains with ERTS. NASA Spec. Publ. 351 (1), 309. 

Rousseeuw, P.J., 1987. Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. J. Comput. Appl. Math. 20, 53–65. 

Saitta, D., Consoli, S., Ferlito, F., Torrisi, B., Allegra, M., Longo-Minnolo, G., RamírezCuesta, J.M., Vanella, D., 2021. Adaptation of citrus orchards to deficit irrigation strategies. Agric. Water Manag. 247, 106734. 

Sarkar, D., Andrews, F., 2022. latticeExtra: Extra Graphical Utilities Based on Lattice. R package version 0.6-30, https://CRAN.R-project.org/package=latticeExtra. 

Sarkar, D., 2008. Lattice: Multivariate Data Visualization with R. Springer, New York. ISBN 978-0-387-75968-5, http://lmdvr.r-forge.r-project.org. 

Shepard, D., 1968. A two–dimensional interpolation function for irregularly–spaced data. In: In Proceedings of the 1968 23[Rd ] ACM National Conference, pp. 517–524. Sinaga, K.P., Yang, M.S., 2020. Unsupervised K-means clustering algorithm. IEEE Access 8, 80716–80727. 

Song, X., Wang, J., Huang, W., Liu, L., Yan, G., Pu, R., 2009. The delineation of agricultural management zones with high resolution remotely sensed data. Precis. Agric. 10, 471–487. 

Souza, S.A., Rodrigues, L.N., 2022. Irrigation management zone strategies impact assessment on potential crop yield, water and energy savings. Comput. Electron. Agric. 201, 107349. 

16 

Tang, Z., Jin, Y., Alsina, M.M., McElrone, A.J., Bambach, N., Kustas, W.P., 2022. Vine water status mapping with multispectral UAV imagery and machine learning. Irrig. Sci. 40 (4–5), 715–730. 

Turner, N.C., 1981. Techniques and experimental approaches for the measurement of plant water status. Plant Soil 58 (1–3), 339–366. 

- van der Merwe, D., Burchfield, D.R., Witt, T.D., Price, K.P., Sharda, A., 2020. Drones in agriculture. Adv. Agron. 162, 1–30. ISO 690. 

Vanella, D., Ferlito, F., Torrisi, B., Giuffrida, A., Pappalardo, S., Saitta, D., LongoMinnolo, G., Consoli, S., 2021. Long-term monitoring of deficit irrigation regimes on citrus orchards in Sicily. J. Agric. Eng. 52 (4). 

_Computers and Electronics in Agriculture 222 (2024) 109098_ 

Wei, T., Simko, V., 2021. R package ’corrplot’: Visualization of a Correlation Matrix (Version 0.92). Available from https://github.com/taiyun/corrplot. Wiederstein, T., Sharda, V., Aguilar, J., Hefley, T., Ciampitti, I.A., Sharda, A., Igwe, K., 2022. Evaluating spatial and temporal variations in sub-field level crop water demands. Front. Agron. 4, 983244. 

   - Zhang, N., Wang, M., Wang, N., 2002. Precision agriculture—a worldwide overview. Comput. Electron. Agric. 36 (2–3), 113–132. 

   - Zygielbaum, A.I., Gitelson, A.A., Arkebauer, T.J., Rundquist, D.C., 2009. Non-destructive detection of water stress and estimation of relative water content in maize. Geophys. Res. Lett. 36 (12). 

- Waldo, L.J., Schumann, A.W., 2009, December. Alternative methods for determining crop water status for irrigation of citrus groves. In: Proceedings of the Florida State Horticultural Society, Vol. 122, pp. 63–71. 

17 

