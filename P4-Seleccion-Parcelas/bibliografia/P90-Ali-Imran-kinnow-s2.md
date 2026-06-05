                                         Remote Sensing Applications: Society and Environment 26 (2022) 100719


                                                          Contents lists available at ScienceDirect

                                     Remote Sensing Applications: Society and
                                                  Environment
                                                 journal homepage: www.elsevier.com/locate/rsase




Evaluating Sentinel-2 red edge through hyperspectral profiles for
monitoring LAI & chlorophyll content of Kinnow
Mandarin orchards
Ansar Ali a, Muhammad Imran a, *, Amjad Ali b, Muhammad Azam Khan c
a
  Institute of Geoinformation Science & Earth Observation (IGEO), PMAS Arid Agriculture University, Rawalpindi, Pakistan
b
  Pakistan Space Agency, Islamabad, Pakistan
c
  Department of Horticulture, PMAS Arid Agriculture University, Rawalpindi, Pakistan




A R T I C L E I N F O                                    A B S T R A C T

Keywords:                                                Leaf area index (LAI) and chlorophyll content are efficient plant health and nutrition indicators.
Sentinel-2 red edge position                             However, retrieving these traits is challenging for the multilayered canopy of evergreen fruit trees
Spectral validation                                      like Citrus. The spectral reflectance’s Red Edge Position (REP) is a surrogate measure of LAI and
Kinnow LAI & Chl                                         chlorophyll content. Sentinel-2 (20 m) estimates REP at a much higher spatial resolution than
Fruit orchards                                           before. However, retrieval of the traits in the dense canopy structure of orchards requires proper
Large spatial scales
                                                         validation of the Sentinel-2 REP (S2REP) through the hyperspectral profiles of plants. The
                                                         objective here is to evaluate the potential of S2REP to retrieve the LAI and chlorophyll of kinnow
                                                         mandarin fruit orchards and validate the results with REP extracted from the hyperspectral
                                                         profiles and ground measurements of these traits. For this, we first tested several algorithms to
                                                         enumerate the REP range from hyperspectral data that corresponds well to the kinnow manda­
                                                         rin’s LAI and Chl content. Next, we used the S2REP to estimate these traits at sampled locations.
                                                         Hence, we calibrated the regression models of LAI and chlorophyll content with the Sentinel-2
                                                         REP as an explanatory variable and traits ground measurements as response variables. The pre­
                                                         diction accuracy was tested through an independent validation data set. The results show that the
                                                         kinnow mandarin trees demonstrated significant spectral response in the 695–725 nm S2REP
                                                         range of the electromagnetic spectrum similar to the spectral profiles from ground-based
                                                         hyperspectral data. With this S2REP range, LAI and chlorophyll content models outperformed
                                                         to predict these traits for the orchards, with adjusted-R2 0.86 and 0.80 and RMSE 3.7 and 53.3%,
                                                         respectively. We conclude that the S2REP can effectively evaluate kinnow mandarin’s LAI and
                                                         Chlorophyll over large areas. The plants’ LAI and chlorophyll content are best represented by the
                                                         REP derived from the hyperspectral profiles through Polynomial fitting and Linear Extrapolation.
                                                         Such spectrally-validated Sentinel-2 REP for kinnow orchards can calibrate the LAI and chloro­
                                                         phyll models more accurately over large scales. Our methods can be extrapolated to other fruit
                                                         traits to enable the real-time monitoring of orchards’ health and nutritional status.




1. Introduction
    The biophysical and biochemical traits of fruit orchards are efficient indicators of plant health status. Quantitative retrieval of these


    * Corresponding author.
    E-mail address: imran.igeo@uaar.edu.pk (M. Imran).


https://doi.org/10.1016/j.rsase.2022.100719
Received 8 November 2021; Received in revised form 14 February 2022; Accepted 2 March 2022
Available online 9 March 2022
2352-9385/© 2022 Elsevier B.V. All rights reserved.
A. Ali et al.                                                                   Remote Sensing Applications: Society and Environment 26 (2022) 100719


traits helps cope with changing environmental conditions and select the best cultivars for a specific region. The leaf area index (LAI) is
an important canopy architectural parameter. It optimizes the interception of photosynthetically active radiation (Poblete-Echeverría
et al., 2015). Thus, it controls the plant’s microclimate, water balance, gas exchange, and physiological processes. Significant cor­
relations exist between LAI and canopy development, biomass, ecosystem productivity, fruit quality, and yield (Stanley, 2016).
Therefore, LAI has been widely applied in precision agriculture, a crucial morphological index for monitoring plant growth and fruit
yield estimation. Chlorophyll (Chl) content is another essential biochemical parameter that plays a critical role in photosynthetic
processes and provides a means to determine plant health and stress response. The use of Chl as a surrogate measure of solar radiation
absorption is crucial in assessing fruit productivity and its quality (Ramírez et al., 2014). These traits directly control the fruit plant
physiology at the leaf, canopy, and orchard levels. However, it remains challenging to systematically monitor these traits at large
spatial scales for timely and effectively scheduling precise and proper inputs to improve Citrus production.
    Remote sensing is widely applied to quantify vegetation LAI and Chl content by spectral reflectance in visible and near-infrared
(NIR) bands. However, several peripheral factors alter the canopy spectral reflectance of fruit plants (García-Rodríguez et al.,
2020). These factors include leaf angle distribution and optical properties, underlying soil, variable solar illumination, and sensor
observation angles. Similarly, the traits at different plant parts can vary enormously within and across a fruit orchard due to several
biotic and abiotic factors. Therefore, the spectral reflectances may fluctuate mainly due to the sizeable thick canopy structure of
evergreen trees like Citrus (Toselli et al., 2020). Thus, to capture the spatial variability caused by these external factors, remote sensing
data are transformed to spectral vegetation indices (VIs) (e.g., a combination of Red and NIR spectral reflectance). They correlate well
with vegetation traits such as cover matrices, the fraction of photosynthetically active radiation (PAR), net primary productivity (NPP),
and within-field LAI & chlorophyll content (Anderegg et al., 2020). However, most of these VIs become sensitive to soil background,
canopy architecture, and leaf angle distribution factors, mainly in fruit plants where the values of these traits are generally in high
ranges. For instance, the logarithmic correlation between VARI (visible atmospherically resistant index) and LAI becomes weaker and
saturate at intermediate to high values due to the red spectra strongly absorbed by Chl content (Junges et al., 2019). Some studies
adjusted spectral VIs to overcome soil and other interferences such as Soil-Adjusted VI (SAVI), the Optimized Soil-Adjusted VI (OSAVI),
the Modified Soil-adjusted VI (MSAVI), and the Wide Dynamic Range VI (WDRVI). These VIs further raised several issues in providing
reliable LAI estimates from reflectance data, particularly fruit orchards. Moreover, their performance in estimating the chlorophyll
content largely depends on fruit canopies’ crop phenology and structural attributes.
    Red Edge Position (REP) is the point of maximum slope in the plants’ reflectance spectra arising at a wavelength between 680–740
nm. The REP represents the combined effects of heavy assimilation of Chl content in red wavebands and leaf internal scattering in the
NIR spectral region. It is relatively insensitive to the changes caused by external factors, for instance, soil cover percentage, leaf, and
canopy architectural properties, bidirectional and sensor angle effects (Chen et al., 2018). Further, it is less sensitive to the impact of
varied biotic and abiotic factors. Therefore, this spectral index can effectively monitor the health and function of vegetation. The
position of the red edge stretch towards longer wavelengths in the reflectance spectra of healthy plants and remains at shorter
wavebands for stressed and unhealthy plants (Raper and Varco, 2015). It also shifts its position with changes in the concentration of
leaf chlorophyll content, LAI, biomass, water content, age, and seasonal patterns. REP response is highly significant against the
moderate to dense plantations. Therefore, it remains promising for retrieval of LAI and Chl content in many plants such as citrus (Ali
and Imran, 2020), apple (Li et al., 2018), coniferous trees (Xu et al., 2019), winter wheat and maize (Sun et al., 2019), and potato crop
(Zheng et al., 2018). However, linking the REP to multispectral remote sensing is challenging to estimate LAI and Chl content at a large
spatial scale of kinnow mandarin fruit orchards.
    The REP derived through hyperspectral data is commonly used to quantify LAI and Chl content at the field scale (i.e., tree level).
However, multispectral sensors like Sentinel-2 can determine REP at a higher spatial resolution (20 m) for larger areas. Estevez et al.
(2020) showed that spectral bands in the Sentinel-2 REP (S2REP) region represent permeated absorption of Chl content and minimized
saturation nuisance even at higher values of architectural traits. Thus, these bands depict enhanced sensitivity to canopy LAI.
Furthermore, they are less affected by crop phenological and structural attributes to render reliable estimates of Chl content without
the strenuous process of re-calibration (Padalia et al., 2020). As a result, the use of S2REP recently emerged to retrieve fruit orchards’
traits quantitatively. Initial studies using simulated S2 data highlighted its advantages for improved LAI and chlorophyll content
(Frampton et al., 2013). The studies using the real-time Sentinel-2 imagery also calibrated their products for LAI and Chl content
retrieval for some field crops, e.g., potato (Clevers et al., 2017), cereal grains (Caporaso et al., 2018), and forest trees (Sandino et al.,
2018).
    Nonetheless, Citrus orchards are different from field crops and forest plantations in diverse canopy characteristics such as the
compact ceiling of leaves penetrated by varying solar illumination and complicated leaf geometry that can alter the spectral features of
canopy reflectance data. Citrus is a perennial fruit crop for which a profound increase in certain traits (e.g., LAI and Chl content)
appears at the onset of the growing season; that degenerate as phenological stages apropos the fall (Ladanyia and Ladaniya, 2010). The
spectral characteristics of Sentinel-2 reflectance also vary among fruit cultivars. Further, acquiring ground truth data of canopy traits is
critical for calibrating and validating the S2REP response to ensure a real-time estimation of these traits of dense canopy structured
fruit orchards spreading at a large spatial scale.
    Despite the maximum potential of the REP index, the studies on assessment and validation of spectral response of Sentinel-2 REP for
retrieval of canopy traits of mandarin fruit orchards are missing to our best knowledge. Therefore, the present study aimed to evaluate
the potential of Sentinel-2 REP for quantifying the LAI and chlorophyll content of kinnow mandarin (Citrus reticulata) fruit orchards. To
do so, we extracted the REP from spectral profiles measured by ASD FieldSpec 4 high-resolution spectroradiometer. Moreover, we
obtained the ground measurements of the LAI and Chl traits from individual trees. By doing this, we developed and tested multiple
linear regression models for LAI and Chl with REP as an explanatory variable. Finally, the estimated models were applied on the

                                                                     2
A. Ali et al.                                                                        Remote Sensing Applications: Society and Environment 26 (2022) 100719


Sentinel-2 REP to predict LAI and chlorophyll at unobserved locations. Our developed methodology can help quantify the structural
properties of mandarin plants through monitoring orchards’ health and nutrient status.

2. Materials and methods
    Fig. 1 shows the flowchart for all methods applied in this study.

2.1. Study area
    The study was carried out in the widespread orchards of kinnow mandarin in two tehsils of district Sargodha, i.e., Kot Momin
(32◦ 13′ N; 73◦ 00′ E) and Bhalwal (32◦ 15′ N; 72◦ 54′ E), Punjab province of Pakistan (Fig. 2). This area belongs to the steppe climate, i.e.,
semi-arid in the warm and temperate zone of the eastern monsoon, which is significantly characterized by high temperatures, humid
and rainy summers, and pretty mild winters. The nutrient-rich silt-loam soils of the study area favor the growth and production of
mandarins (Ramesh et al., 2019). Kinnow mandarin fruit orchards extending to about 70% agricultural land in the district are major
economic zones of Pakistan. The annual fruit yield in the area ranges from 12.8 to 14.7 tons per hectare.
    Randomly distributed fruit orchards comprised the sampled pixels in the study sampling scheme. For this purpose, 20 m × 20 m
Fishnet was generated on the Sentinel-2 images based on which 55 sample orchards of kinnow mandarin were selected. We overlay the
Sentinel-2 pixels of 20 m × 20 m on 55 sampling points, and the trees in corresponding pixels were used for spectral and non-spectral
measurements (Richter et al., 2010). The orchard trees budding on rough lemon (Citrus Jambheri) rootstock are planted at 6.09 m ×
6.09 m (20 ft × 20 ft) and row-to-row distance with about 9–10 trees per pixel and 109 per acre. The kinnow trees in the sampled
orchards were almost 8.5 years, 3.1 m tall, and 2.9 m wide on average. We assumed the higher range of plant conditions to better
correlate with satellite-derived reflectance data and allow mapping within-orchard variations of biophysical and biochemical traits.
However, within the pixel itself, we targeted a homogeneous plant condition to make the overlaying pixels independent of background
effects. We obtained the ground measurements during 28 August − 01 September 2018 concurrently with cloud-free images of the
Sentinel-2 satellite on 29 August 2018.

2.2. Data collection and pre-processing
2.2.1. Ground measurements
    Three in-field measurements were made in each predetermined pixel in the study area. The reflectance spectra from the tree canopy
were recorded through ASD FieldSpec 4 Hi-Res Spectroradiometer (Malvern Panalytical, Longmont, CO, USA) via 1 m fiber optics. The
Spectroradiometer detects light consistently over the visible to short wave infra-red wavebands across 2151 bands. The red edge bands
in the range of 670–780 nm with 3 m spectral resolution and 1.4 m sampling interval to ensure detection of even subtle spectral
features comprise the desired zone of our study. Spectral measurements were made for each of the 9 to 10 trees within each pixel. For
each tree, we obtained three spectral measurements positioning the sensor head of fiber optics exactly 1 m above the tree canopy




                                                  Fig. 1. Flowchart for the research methodology.


                                                                        3
A. Ali et al.                                                                               Remote Sensing Applications: Society and Environment 26 (2022) 100719




                                            Fig. 2. Study area and sampling points illustrated on Sentinel-2 images.




Fig. 3. Measuring spectral reflectance of each tree in sampled pixels (a) Chlorophyll content (b), and below-canopy (c) above-canopy (d) Leaf area index (LAI)
(adopted from Ali and Imran (2020)).


                                                                               4
A. Ali et al.                                                                                Remote Sensing Applications: Society and Environment 26 (2022) 100719


(Fig. 3(a)) and later averaged to account for illumination and canopy structural differences as well as bidirectional effects. The
measurements were made between 10:00 and 14:00 Pakistan Standard (UTC+5) under a clear and cloudless sky to record the
reflectance spectra in solar elevation angel > 45◦ . These time and solar zenith angle arrangements help reduce the illumination
changes errors. Before each spectral measurement, the instrument was calibrated using a Spectralon white reference panel (LabSphere,
North Sutton, NH, USA) to account for any ambient radiation changes and convert the measured radiance to reflectance.
    The relative chlorophyll content of the same trees was recorded using a chlorophyll concentration meter (MC-100) (Apogee In­
struments, Inc., Logan, UT, USA). The meter determines the chlorophyll concentration by measuring light absorbance at 653 nm (red
wavelength) and 931 nm (NIR wavelength). The instrument directly measures and displays chlorophyll concentration (μmol) from
intact leaf samples by calculating the ratio between transmissions of radiation at 653 nm and 931 nm wavebands. The meter was
calibrated to record three chlorophyll readings from each leaf and give their average as an output measurement. Accordingly, an
average value of chlorophyll content per tree was obtained from three fully-expanded sun-lit leaves with the meter’s sensor placed
midway between the leaf’s margin and the middle rib (Fig. 3(b)). Utmost care was taken to watch for leaves with bruising, insect
excretion, or condensate water droplets for measurements. The average value of Chl content measured for all trees within a pixel was
used for further analysis.
    LAI of the same trees were gauged using Plant Canopy Analyzer (LAI-2200C; LI-COR, Inc., Lincoln, NE, USA). The instrument uses a
non-destructive method to efficiently and accurately measure LAI. Radiation measurements made above and below the tree canopy
with a fisheye optical sensor (148◦ field of view) are used to determine canopy light interception at five zenith angles. Simultaneously,
LAI is computed by simulating the radiative transfer model. Following the instrument instructions to avoid errors caused by direct
sunlight, the measurements were recorded between 06.30 and 10:00 and 16:30 to 18:15 Pakistan Standard (UTC+5). From each tree, a
minimum of five below the canopy and five above canopy measurements were recorded (Fig. 3(c)), with the resultant measurement
being the average of these readings. Following the validated manufacturer recommendations (Chianucci et al., 2015), care was taken
to record measurements with accurate operator position, i.e., opposite to the sun circumventing sunlight directly on the instrument
(aka effect of view caps). Thus, uniform sky-illumination conditions were ensured, eluding the scattering effect under direct sunlight.
Each trait was measured 3–5 times a tree, providing statistical means of spectral reflectance, LAI, and Chl content values per pixel.

2.2.2. Sentinel-2 data
    We acquired the study area images of Sentinel-2 satellite from the scientific data hub provided by European space agency (Hub,
2017). The images in the form of tiles of 100 × 100 km2 with UTM/WGS84 projections comprised 13 visible to SWIR spectral region
bands at spatial resolutions of 10, 20, and 60 m. Strategically placed red edge bands centered at wavebands 705, 740, and 783 nm with
a spatial resolution of 20 m and bandwidth of 15 nm were used in this study to evaluate the predictive accuracy of Sentinel-2 red edge
position. Sen2cor 2.5.5 Freeware was used to process the top-of-atmospheric (ToA) reflectance (level 1C product) into top-of-canopy
(ToC) reflectance (level 2A product), and all the bands were resampled to 20 m spatial resolution (Main-Knorn et al., 2017).
    We acquired three tiles, i.e., SBR, SCR, and SCS, fully covering the central position coordinates of the study area. We considered the
minimal possible cloudiness level and full area coverage. The following files were downloaded for the study:
1. S2A_MSIL1C_20180829T054641_N0206_R048_T43SBR_20180829T095805.SAFE
2. S2A_MSIL1C_20180829T054641_N0206_R048_T43SCR_20180829T095805.SAFE
3. S2A_MSIL1C_20180829T054641_N0206_R048_T43SCS_20180829T095805.SAFE




                Fig. 4. Pattern of kinnow mandarin plantation on high resolution image (a), and weighted average measurements in sampled pixels (b).


                                                                                 5
A. Ali et al.                                                                               Remote Sensing Applications: Society and Environment 26 (2022) 100719


2.2.3. Pre-processing hyperspectral and multispectral data for REP calculation
   We obtained the ground-based hyperspectral reflectance data using ASD FieldSpec 4 high-resolution Spectroradiometer. Linear
extrapolation and polynomial fitting were applied to compute REPs from the hyperspectral profiles of kinnow trees. These two al­
gorithms have already proved outstanding to estimate LAI and chlorophyll of kinnow trees (Ali and Imran, 2020), used as reference
models in this study. For each pixel, one representative REP value was obtained by averaging the values of 9–10 kinnow trees. The
average REP values derived from each pixel were then regressed with ground measured LAI x Chl content to show how the correlation
should theoretically look. The S2REP was calculated using Sentinel-2 ToC values (see 1), all resampled to 20 m spatial resolution using
the following formula in SNAP 5.0:
                                 B7+B4
                                       −B5
         S2REP = 705 + 35 ∗        2
                                                                                                                                                             (1)
                                  B6 − B5

where bands B4 (665 nm), B5 (705 nm), B6 (740 nm), and B7 (783 nm).
    Taking the ground spectral reflectances 1m above the tree’s canopy, the ASD Spectroradiometer captures the pure spectral
reflectance from each tree’s canopy. However, although the expanded tops of fruit trees cover most of the ground area (90–95%)
within each pixel, the variability in the spectral response of multispectral sensor may be caused by the reflectance from mixed
vegetation or bare land between the tree plants (Isbaex and Coelho, 2021). It could be the limitation of the Sentinel-2 MSI sensor,
particularly for dense canopy structured fruit orchards. For this, we computed a weighted average of Sentinel-2 measurements. First,
we delineated the cover area of individual trees and the bare land of each pixel through high spatial resolution images (Google Earth)
and field observations (see Fig. 4). Next, the Sentinel-2 measurements were weighted through the following method proposed by Jin
et al. (2018). It takes into account the weight of tree canopies in the ratio of the bare area between the plants, as
             ∑
                 x i wi
        Wa = ∑                                                                                                                     (2)
                  wi

where Wa is weighted average of Sentinel-2 measurements for individual trees and the bare land for a pixel, xi is ith observation, and wi
is weight of the ith observation.

2.2.4. LAI and Chl estimation and prediction models
   We used the weighted averaged S2REP values for each pixel to model their correlation with ground measured LAI and chlorophyll
of mandarin canopies. For this, the REPs from polynomial fitting and linear extrapolation models were used as reference ground
measurements (Ali and Imran, 2020). The field observation data were randomly split into training and validation subsets (42 readings:
70% of the total samples and 13 readings: 30% of the total samples, respectively). The multiple linear regression (MLR) estimated the
LAI and chlorophyll (response variables) with the S2REP values (explanatory variable). We evaluated the resulting LAI and Chl content
models based on the coefficient of determination (adjusted-R2) between the measured and observed values. These estimated models
with the REP values derived from Sentinel-2 imagery were used to predict LAI and Chl values for the kinnow orchards at unobserved
locations in the study area. The prediction accuracies were measured using root mean square error (RMSE) and mean absolute error
(MAE) with the independent validation data set (Cressie, 1993). The entire analyses were performed in an R environment.

3. Results
3.1. Variations of ground-measured traits
    Table 1 shows descriptive statistics of the in-situ measured LAI, Chl content, and REPs derived from the hyperspectral reflectance of
the sampled pixels in the study area. They indicate high spatial variations of the sampled variables across the 55 pixels of Sentinal-2
imagery covering the study area. The ground observations of LAI traversed between 2.02 m2 m− 2 and 6.34 m2 m− 2 with mean of 4.18
m2 m− 2, whereas field-measured chlorophyll content fluctuated between 54.10 μmol m− 2 and 175 μmol m− 2 with mean of 114.55
μmol m− 2 in the sampled pixels of study area. The results of this study verified our previous findings (Ali and Imran, 2020) that kinnow
mandarin’s LAI and chlorophyll are best represented by polynomial fitting and linear extrapolation REPs (nm), respectively. The REP
values derived through polynomial fitting and linear extrapolation models stand between 698 nm and 725 nm by an average of 710 nm
and 713 nm, respectively. Expository analysis of field observations showed an upward trend in the LAI and chlorophyll content values
with thick and mature canopies reflecting strong variability in these traits: however, with no significant inter-correlation between the
two. Similarly, an increasing trend in REP values extracted from hyperspectral algorithms was observed from pixels with higher values
of these traits and vice versa.


Table 1
Descriptive statistics of the in-situ measured variables. Leaf area index (LAI), chlorophyll content and Red-Esge Position (REP) of ground-measured hyperspectral
profiles of kinnow mandarin trees.

  Measured variables                              Min                       Mean                      Max                      StDev                    Range
          2     − 2
  LAI (m m )                                      2.02                      4.18                      6.34                     1.13                     4.32
  Chl content (μmol m− 2)                         54.10                     114.55                    175                      31.32                    120.9
  Polynomial fitting REPs (nm)                    698                       710                       722                      3.16                     24
  Linear Extrapol REPs (nm)                       701                       713                       725                      3.15                     24


                                                                               6
A. Ali et al.                                                                                Remote Sensing Applications: Society and Environment 26 (2022) 100719


3.2. Spectral response of Sentinel-2 spectral reflectance
   Fig. 5(a and b) show the spectral profile of Kinnow mandarin trees from three random pixels in the spectral region of red-edge from
ground-based reflectance and 16-bit digital number image of Sentinel-2 (b). Both the cases observed a remarkable spectral response in
the 695–725 nm S2REP range of the electromagnetic spectrum. The field measurements of LAI and chlorophyll content of these pixels
vary from 2.25 m2 m− 2 & 85.1 μmol m− 2, 5.43 m2 m− 2 & 85.1 μmol m− 2 to 4.68 (m2 m− 2) & 80.8 μmol m− 2, respectively. S2REP
exhibited the same spectral response as to REP from hyperspectral algorithms; shifts towards longer wavelengths with increasing LAI
and chlorophyll values in the pixels. Moreover, it also demonstrated imposing reflectance in the NIR spectral region with higher leaf
area index values.


3.3. Distribution features of Sentinel-2 red edge position
   Fig. 6 shows the distribution features of S2REPs with training and test points of ground values of kinnow mandarin’s LAI and
chlorophyll content. The distribution spread for S2REP values (695 − 725 nm) is quite comparable to those derived from spectral
profiles (on the ground) through two calibrated models, i.e., polynomial fitting (698 − 722 nm) and linear extrapolation (701 − 725
nm). Therefore, the S2REP range well predicted the LAI and chlorophyll content of kinnow orchards with adjusted-R2 0.93 and 0.90
and RMSE 0.156% and 10.1%, respectively. A more concise studying of the S2REP map showed that most of the map areas (greater
than 90%) exhibited by yellow color range indicated REP values between 705–725 nm, while only 10% of the study area shown by
purple color range indicated REP values from 695–704 nm.


3.4. Modeling LAI and chlorophyll with Sentinel-2 red edge position
    Table 2 shows the estimated Multiple Linear Regression models (i.e., LAI-MLR and Chl-MLR) applied to predict LAI and chlorophyll
of the kinnow mandarin orchards using the S2REP values, respectively. Both models show strong relationships between the S2REP of
the pixels and the corresponding sampled LAI and Chl content on the ground, with adjusted-R2 0.86 for LAI-MLR and 0.80 for Chl-MLR,
both significant at the p < 0.001 level.
    Fig. 7 shows several diagnostic plots to check the validity of LAI-MLR model (a-c) and Chl-MLR model (d-f) assumptions. Fig. 7(a
and d) indicate homoscedasticity of the LAI-MLR and Chl-MLR models, respectively, i.e., residuals variance is independent of the fitted
values. The linear patterns of residuals indicate relationships of LAI and chlorophyll with the S2REP as linear because a non-linear
pattern may be due to a non-linear relationship between explanatory variables and an independent variable, which a linear model
does not fully capture. Fig. 7(b and e) show the Q-Q plot of theoretical (x-axes) versus sampled quartile (y-axes) of MLR models re­
siduals. The plots indicate the overall normal distribution of model residuals. It was further confirmed by examining the spatial de­
pendency of the models’ residuals. The Moran’s I values 0.1161 and 0.0113 for these models, respectively, are close to zero at the
significance level p < 0.001. It indicates no spatial autocorrelation in model residuals exists, i.e., independence of model error terms. It
also shows that the models are not required to improve further through spatial models. Finally, Fig. 7(c and f) indicate that outliers are
influential in LAI-MLR and Chl-MLR models, respectively.


3.5. Predicting LAI and chlorophyll with the S2REP model
    Fig. 8(a and b) shows the predicted LAI map (a) and Chl map (b) for the kinnow mandarin orchards in the study area using the REP
derived from Sentinel-2 (20 m) and the estimated LAI-MLR and Chl-MLR models, respectively. The spread of distribution of LAI and
Chl content predicted from Sentinel-2 imagery (0 − 10 and 0 − 200 μmol m− 2) is quite comparable with ground measured values of
these traits i.e., 2.02–6.34 m2 m− 2 and 54.10 μmol m− 2 to 175 μmol m− 2 recorded using plant canopy analyzer and chlorophyll meter
respectively in the sampled pixels. Moreover, using the independent validation data, both models show high prediction accuracy with
a root mean square error (RMSE) of prediction of 0.36 (equals 10.1% of the mean LAI) and 0.062 μmol m− 2 (equals 12.3% of the mean
Chl content) respectively. It is further confirmed with the graphs in Fig. 9(a and b), which show strong correlations between ground
measured traits (LAI & Chl) and S2REP derived from Sentinel-2 imagery for the experimental orchards.




Fig. 5. Spectral response of Kinnow mandarin trees from three random pixels in the Red-edge region of ground-based reflectance (a) and 16-bit digital number image
of Sentinel-2 (b). (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)


                                                                                7
A. Ali et al.                                                                                    Remote Sensing Applications: Society and Environment 26 (2022) 100719




Fig. 6. Distribution of the red edge position derived from Sentinel-2 (S2REP) in the study area. (For interpretation of the references to color in this figure legend, the
reader is referred to the Web version of this article.)



Table 2
Multiple Linear Regression (MLR) Leaf Area Index (LAI) and Chl content models (i.e., LAI-MLR and Chl-MLR), where LAI and chlorophyll content are estimated with the
Sentinel-2 derived Red Edge Position (S2REP) values extracted through the polynomial fitting and linear extrapolation, respectively. Standard errors are hetero­
scedasticity robust. ***p < 0.001; **p < 0.01; *p < 0.05.The LAI-MLR and Chl-MLR model are used to predict the LAI and chlorophyll content of the Kinnow Mandarin
(Citrus reticulata) orchards using the S2REP values at unobserved locations.

                                                                LAI-MLR                                                                    Chl-MLR

    (Intercept)                                                 4.65 ***                                                                   103.34 ***
                                                                95.00% CIΨ [4.50, 4.81]                                                    95.00% CI [98.80, 107.87]
    S2REP                                                       1.22 ***                                                                   28.04 ***
                                                                95.00% CIΨ [1.10, 1.33]                                                    95.00% CI [23.94, 32.13]
    N                                                           42                                                                         42
    Adjusted-R2                                                 0.86                                                                       0.80
Ψ
    95% Confidence Interval. All continuous predictors are mean-centered and scaled by 1 standard deviation.


4. Discussions
    Quantitative retrieval of biophysical and biochemical traits using multispectral satellite imagery remained challenging, especially
for dense canopies of fruit orchards. Therefore, very few studies are found in the literature on the applicability of REP derived from the
Sentinel-2 imagery (S2REP) to estimate kinnow fruit orchards’ LAI & chlorophyll content. The study aimed to investigate the potential
of S2REP to predict kinnow mandarin’s traits at the scale of fruit orchards and validate the results with algorithms derived from
hyperspectral data and detailed ground observations. The research demonstrates S2REP, a practical index for the real-time estimation
of LAI and chlorophyll content of kinnow orchards for precision agriculture.
    High spatial variations demonstrated by ground-observed LAI, chlorophyll content, and REPs derived from canopy spectral
reflectance of kinnow mandarin often result from varying canopy structures and volumes of tree plants. For instance, Yuan et al. (2013)
reported that dense, structured tree plants would have higher LAI ranges than the plants with more uniform leaf area distribution that
characterizes the tree growth. The LAI and volume increment for both individual trees and stand canopies are also reported to increase
with height, trunk diameter, and other crown characteristics (Kitajima et al., 2005). Similarly, the chlorophyll concentration in leaves


                                                                                    8
A. Ali et al.                                                                              Remote Sensing Applications: Society and Environment 26 (2022) 100719




                                   Fig. 7. Diagnostic plots for the validity of LAI-MLR model (a–c) and Chl-MLR model (d–f).




Fig. 8. The predicted LAI map (a) and Chl map (b) for the kinnow orchards in the study area using the REP derived from Sentinel-2 and the estimated LAI-MLR and
Chl-MLR models, respectively. (The coordinate system is UTM Zone 43N with datum WGS84).


and canopies varies with various pigments, protein complexes, photosystems, and composition and activities of chemosynthesis en­
zymes (Sumanta et al., 2014). Besides the leaf properties, the orientation of tree leaves also determines the light regime within a
canopy by altering the characteristics of canopy reflectance. Moreover, the spectral reflectance in the visible and mid-infrared regions
is affected by leaf area, crown health attributes, soil brightness level, and diverse canopy architectural parameters (Ferreira et al.,
2018).
    In this study, we keenly observed spectral curves of the kinnow mandarin trees in the selected Sentinel-2 pixels. Our observations
reveal that the red edge slope instigated from the band-5 (705 nm) of the red edge spectral region exhibits sharp reflectance peaks in
the band-6 (740 nm) and then sustains in the band-7 (783 nm). With this, we can demonstrate the importance of these two bands in the

                                                                              9
A. Ali et al.                                                                            Remote Sensing Applications: Society and Environment 26 (2022) 100719




Fig. 9. Correlations between ground measured traits and S2REP derived from Sentinel-2 imagery of the experimental orchards, (a) S2REP and LAI, (b) S2REP and
Chl content.


context of leaf and canopy architectural traits of kinnow fruit plants. Some other researchers also observed similar reflective spectra in
the red edge of S2REP to associate with LAI and chlorophyll concentration (Padalia et al., 2020). Likewise, Li et al. (2018) estimated
the canopy chlorophyll content in apple trees based on the Sentinel-2A sensor. He observed that the significant reflectance peak in the
700–740 nm shifts towards longer wavelengths with the increase in LAI x Chl contents. He concludes that the S2REP spectral region is
the best option for estimating the plant traits. Martínez and Luis (2017) revealed that the reflectance peak of S2REP strongly correlates
with leaf Chl content and depends on the amount of chlorophyll seen by the sensor. Therefore, he declared S2REP a sensitive indicator
and surrogate measure of vegetation stress. Moreover, our results are reconcilable with (Delloye et al., 2018) that the red-edge spectral
response of the MSI sensor is highly sensitive to chlorophyll and other physiological traits of vegetation. The authors added that the
spectral response is highly variable among different cultivars of the same crop.
    A wider spread of S2REP (695 − 725 nm) observed in the study area depicts the canopy structural heterogeneity present in the
kinnow mandarin fruit orchards. This diversity may be caused by canopy shape and size, tree height, position, density, and background
reflectance. Some studies also observed a similar S2REP spread. For instance, Li et al. (2018) have observed the spectral slope of apple
trees canopy reflectance between 680–740 nm. Rahimzadeh-Bajgiran et al. (2020) confirmed that the S2REP spectral range between
690–730 nm is more promising for measuring varied biophysical and biochemical parameters of vegetation. Our results are also
supported by Hallik et al. (2019) that S2REP produced a straight red edge inflection point shifting between 700 and 730 nm; showing
peak jumps between fixed locations around 717 nm and 727 nm for tree canopies. Li et al. (2021) demonstrated that S2REP distri­
bution near 700 nm is associated with low LAI and leaf chlorophyll concentration, while its values near 725 nm refer to high LAI and
chlorophyll concentration. Along with these studies, we illustrated the importance of S2REP spread of 695–725 nm to quantify these
traits for kinnow mandarin fruit orchards.
    The estimation of LAI and Chl content through S2REP should incorporate certain uncertainties caused by the spatial variation of
these structural traits. The sensitivity of S2REP to LAI and Chl content demonstrated through diverse environments reported minimal
uncertainty. Djamai et al. (2019) observed that LAI and chlorophyll content dynamically determine the slope of S2REP. The transition
in the canopy reflectance in the red edge is mainly resulting from the multiple scattering between the leaf layers. Estevez et al. (2020)
showed a good correlation of S2REP with LAI, least influenced by spectral noise from soil background and atmospheric effects. Ustin
and Jacquemoud (2020) identified the higher response of S2REP through changing foliar traits of different crops. These responses were
due to the transition from solid photosynthetic pigments strongly absorbed in the red wavebands to scattering longer wavelengths in
the NIR spectral range. Thus, it permits the detection of leaf functional properties. We observed no spatial autocorrelation of residuals
from the MLR models of our desired traits. It indicates that S2REP captures the spatial heterogeneity caused by the plant structural
characteristics. Therefore, our findings are in line with the earlier studies that the S2REP can improve the accuracy of LAI (Kamenova
and Dimitrov, 2021), chlorophyll concentration (Delloye et al., 2018), and biomass estimation (Li et al., 2021).
    We developed LAI and Chlorophyll estimation models with Sentinel-2 REP as an explanatory variable to predict the kinnow traits at
unobserved locations. The LAI and Chl maps thus obtained very well captured the spatial variation of the canopy traits across the study
area. These maps indicated that the predicted LAI data in the dense kinnow orchards is higher than that of the sparse to moderately
dense orchards. The canopy chlorophyll content is related to crop productivity. It varies with other physiological parameters such as
leaf fraction exposed to light, fraction of incoming solar radiation absorbed by the plant, fractional cover, and energy absorption
capacity of tree’s canopy (Delloye et al., 2018). Overall, accuracy statistics show that the maps of the LAI and Chl traits derived from
Sentinel-2 imagery accurately incorporate their spatial and temporal distributions across dense and closed canopy structures of the
kinnow orchards. These results are well in agreement with findings of similar studies or other fruit orchards (Tanioka et al., 2020).
Hence, the maps of LAI and Chl content in this study can help farmers and policymakers in real-time monitoring of kinnow mandarin
health and nutrition status and overcome the declining fruit productivity. Moreover, these maps can be used to monitor the ongoing
cropping season continuously and for early detection of crop growth anomalies connected to potential damage and yield loss

                                                                            10
A. Ali et al.                                                                                       Remote Sensing Applications: Society and Environment 26 (2022) 100719


(Kamenova and Dimitrov, 2021). Other studies applied the LAI and Chl maps to understanding plant functioning and modeling the
earth’s biogeochemical systems.

5. Conclusion
    The potential of S2REP was evaluated successfully in this study for accurate and real-time monitoring of the health and nutrition
status of kinnow mandarin (Citrus reticulata) fruit orchards. We developed and tested the Sentinel-2 Red Edge Position (S2REP)
models to estimate and predict sampled orchards’ LAI and chlorophyll content. The algorithms derived from ground-based hyper­
spectral data and detailed ground observations of desired traits enabled us to calibrate and validate the LAI and Chl models for kinnow
orchards over large spatial scales.
    The REP distribution spread for the Sentinel-2 imagery (695 − 725 nm) is quite comparable to those derived from ground spectral
profiles through polynomial fitting (698 − 722 nm) and linear extrapolation (701 − 725 nm). These models proved outstanding to
estimate kinnow mandarin’s LAI and chlorophyll content, with adjusted-R2 (0.93 and 0.90) and RMSE (0.156% and 10.1%). Spectral
profiles of kinnow mandarin orchards derived from Sentinel-2 pixels demonstrated a remarkable spectral response in the 695–725 nm
S2REP range of the electromagnetic spectrum similar to the spectral profiles from ground-based hyperspectral data. The shift of S2REP
towards longer wavelengths in the red edge region with increasing LAI and chlorophyll content proves it an effective tool to estimate
these traits for kinnow mandarin fruit orchards. Multiple linear regression established a strong relationship between S2REP and the LAI
and chlorophyll content with adjusted-R2 0.86 and 0.80, respectively, at the 5% confidence level. The developed mechanism would
help farmers and policymakers overcome declining fruit productivity in precision agriculture.

Data availability statement
    Data generated at a central, large-scale facility, available upon request.


Declaration of competing interest
    The authors declare that they have no known competing financial interests or personal relationships that could have appeared to
influence the work reported in this paper.


Acknowledgment
    The authors would like to thank Mr. Shoukat Ullah Khan (DG SUPARCO) and Dr. Hassan Munir Bajwa (UAF) for providing the field
instruments. Thanks also to Syed Masroor-ul- Hassan for technical assistance, Mr. Razzaq for helping with logistics and Ishtiaq and
Majid for support in the field measurements.


References
Ali, A., Imran, M., 2020. Evaluating the potential of red edge position (rep) of hyperspectral remote sensing data for real time estimation of LAI & chlorophyll content
     of kinnow Mandarin (citrus reticulata) fruit orchards. Sci. Hortic. 267, 109326.
Anderegg, J., Yu, K., Aasen, H., Walter, A., Liebisch, F., Hund, A., 2020. Spectral vegetation indices to track senescence dynamics in diverse wheat germplasm. Front.
     Plant Sci. 10, 1749.
Caporaso, N., Whitworth, M.B., Fisk, I.D., 2018. Near-infrared spectroscopy and hyperspectral imaging for non-destructive quality assessment of cereal grains. Appl.
     Spectrosc. Rev. 53 (8), 667–687.
Chen, H., Huang, W., Li, W., Niu, Z., Zhang, L., Xing, S., 2018. Estimation of lai in winter wheat from multi-angular hyperspectral vnir data: effects of view angles and
     plant architecture. Rem. Sens. 10 (10), 1630.
Chianucci, F., Macfarlane, C., Pisek, J., Cutini, A., Casa, R., 2015. Estimation of foliage clumping from the lai-2000 plant canopy analyzer. Trees 29 (2), 355–366.
Clevers, J., Kooistra, L., Brande, M.V.D., 2017. Using Sentinel-2 data for retrieving LAI and leaf and canopy chlorophyll content of a potato crop. Rem. Sens. 9 (5), 405.
Cressie, N., 1993. Statistics for spatial data. Terra. Nova 4 (5), 613–617.
Delloye, C., Weiss, M., Defourny, P., 2018. Retrieval of the canopy chlorophyll content from sentinel-2 spectral bands to estimate nitrogen uptake in intensive winter
     wheat cropping systems. Rem. Sens. Environ. 216, 245–261.
Djamai, N., Zhong, D., Fernandes, R., Zhou, F., 2019. Evaluation of vegetation biophysical variables time series derived from synthetic sentinel-2 images. Rem. Sens.
     11 (13), 1547.
Estevez, J., Vicent, J., Rivera-Caicedo, J.P., Morcillo-Pallarés, P., Vuolo, F., Sabater, N., Camps-Valls, G., Moreno, J., Verrelst, J., 2020. Gaussian processes retrieval of
     LAI from Sentinel-2 top-of-atmosphere radiance data. ISPRS J. Photogrammetry Remote Sens. 167, 289–304.
Ferreira, M.P., Féret, J.B., Grau, E., Gastellu-Etchegorry, J.P., Amaral, D.H.C., Shimabukuro, Y.E., de Souza Filho, C.R., 2018. Retrieving structural and chemical
     properties of individual tree crowns in a highly diverse tropical forest with 3d radiative transfer modeling and imaging spectroscopy. Rem. Sens. Environ. 211,
     276–291.
Frampton, W.J., Dash, J., Watmough, G., Milton, E.J., 2013. Evaluating the capabilities of Sentinel-2 for quantitative estimation of biophysical variables in vegetation.
     ISPRS J. Photogrammetry Remote Sens. 82, 83–92.
García-Rodríguez, A., García-Rodríguez, S., Díez-Mediavilla, M., Alonso-Tristán, C., 2020. Photosynthetic active radiation, solar irradiance and the cie standard sky
     classification. Appl. Sci. 10 (22), 8007.
Hallik, L., Kuusk, A., Lang, M., Kuusk, J., 2019. Reflectance properties of hemiboreal mixed forest canopies with focus on red edge and near infrared spectral regions.
     Rem. Sens. 11 (14), 1717.
Hub, S.S.D., 2017. Us Geological Survey Distribution of European Space Agency’s Sentinel-2 Data. US Geological Survey. Technical report.
Isbaex, C., Coelho, A.M., 2021. The Potential of Sentinel-2 Satellite Images for Land-Cover/Land-Use and Forest Biomass Estimation: A Review. Forest Biomass-From
     Trees to Energy.
Jin, Y., Ge, Y., Wang, J., Heuvelink, G., Wang, L., 2018. Geographically weighted area-to-point regression kriging for spatial downscaling in remote sensing. Rem.
     Sens. 10 (4), 579.
Junges, A.H., Fontana, D.C., Lampugnani, C.S., 2019. Relationship between the normalized difference vegetation index and leaf area in vineyards. Bragantia 78 (2),
     297–305.


                                                                                      11
A. Ali et al.                                                                                      Remote Sensing Applications: Society and Environment 26 (2022) 100719

Kamenova, I., Dimitrov, P., 2021. Evaluation of sentinel-2 vegetation indices for prediction of lai, fapar and fcover of winter wheat in Bulgaria. Eur. J. Rem. Sens. 54,
     89–108.
Kitajima, K., Mulkey, S.S., Wright, S.J., 2005. Variation in crown light utilization characteristics among tropical canopy trees. Ann. Bot. 95 (3), 535–547.
Ladanyia, M., Ladaniya, M., 2010. Citrus Fruit: Biology, Technology and Evaluation. Academic press.
Li, C., Zhou, L., Xu, W., 2021. Estimating aboveground biomass using sentinel-2 msi data and ensemble algorithms for grassland in the shengjin lake wetland, China.
     Rem. Sens. 13 (8), 1595.
Li, C., Zhu, X., Wei, Y., Cao, S., Guo, X., Yu, X., Chang, C., 2018. Estimating apple tree canopy chlorophyll content based on sentinel-2a remote sensing imaging. Sci.
     Rep. 8 (1), 1–10.
Main-Knorn, M., Pflug, B., Louis, J., Debaecker, V., Müller-Wilm, U., Gascon, F., 2017. Sen2cor for sentinel-2. In: Image and Signal Processing for Remote Sensing
     XXIII, vol. 10427. International Society for Optics and Photonics, 1042704.
Martínez, M., Luis, J., 2017. Relationship between crop nutritional status, spectral measurements and sentinel 2 images. Agron. Colomb. 35 (2), 205–215.
Padalia, H., Sinha, S.K., Bhave, V., Trivedi, N.K., Kumar, A.S., 2020. Estimating canopy LAI and chlorophyll of tropical forest plantation (North India) using Sentinel-2
     data. Adv. Space Res. 65 (1), 458–469.
Poblete-Echeverría, C., Fuentes, S., Ortega-Farias, S., Gonzalez-Talice, J., Yuri, J.A., 2015. Digital cover photography for estimating leaf area index (lai) in apple trees
     using a variable light extinction coefficient. Sensors 15 (2), 2860–2872.
Rahimzadeh-Bajgiran, P., Hennigar, C., Weiskittel, A., Lamb, S., 2020. Forest potential productivity mapping by linking remote-sensing-derived metrics to site
     variables. Rem. Sens. 12 (12), 2056.
Ramesh, T., Bolan, N.S., Kirkham, M.B., Wijesekara, H., Kanchikerimath, M., Rao, C.S., Sandeep, S., Rinklebe, J., Ok, Y.S., Choudhury, B.U., Wang, H., 2019. Soil
     organic carbon dynamics: impact of land use changes and management practices: a review. Adv. Agron. 156, 1–107.
Ramírez, D.A., Yactayo, W., Gutiérrez, R., Mares, V., De Mendiburu, F., Posadas, A., Quiroz, R., 2014. Chlorophyll concentration in leaves is an indicator of potato
     tuber yield in water-shortage conditions. Sci. Hortic. 168, 202–209.
Raper, T.B., Varco, J.J., 2015. Canopy-scale wavelength and vegetative index sensitivities to cotton growth parameters and nitrogen status. Precis. Agric. 16 (1),
     62–76.
Richter, K., Atzberger, C., Vuolo, F., D’Urso, G., 2010. Evaluation of sentinel-2 spectral sampling for radiative transfer model based lai estimation of wheat, sugar beet,
     and maize. IEEE J. Sel. Top. Appl. Earth Obs. Rem. Sens. 4 (2), 458–464.
Sandino, J., Pegg, G., Gonzalez, F., Smith, G., 2018. Aerial mapping of forests affected by pathogens using uavs, hyperspectral sensors, and artificial intelligence.
     Sensors 18 (4), 944.
Stanley, J., 2016. Factors affecting fruit set and fruit quality along branch units of different apricot cultivars. N. Z. J. Crop Hortic. Sci. 44 (3), 171–191.
Sumanta, N., Haque, C.I., Nishika, J., Suprakash, R., 2014. Spectrophotometric analysis of chlorophylls and carotenoids from commonly grown fern species by using
     various extracting solvents. Res. J. Chem. Sci. 2231, 606X.
Sun, Y., Qin, Q., Ren, H., Zhang, T., Chen, S., 2019. Red-edge band vegetation indices for leaf area index estimation from sentinel-2/msi imagery. IEEE Trans. Geosci.
     Rem. Sens. 58 (2), 826–840.
Tanioka, Y., Cai, Y., Ida, H., Hirota, M., 2020. A spatial relationship between canopy and understory leaf area index in an old-growth cool-temperate deciduous forest.
     Forests 11 (10), 1037.
Toselli, M., Baldi, E., Cavani, L., Sorrenti, G., 2020. Nutrient management in fruit crops: an organic way. In: Fruit Crops. Elsevier, pp. 379–392.
Ustin, S.L., Jacquemoud, S., 2020. How the optical properties of leaves modify the absorption and scattering of energy and enhance leaf functionality. In: Remote
     Sensing of Plant Biodiversity. Springer, Cham, pp. 349–384.
Xu, N., Tian, J., Tian, Q., Xu, K., Tang, S., 2019. Analysis of vegetation red edge with different illuminated/shaded canopy proportions and to construct normalized
     difference canopy shadow index. Rem. Sens. 11 (10), 1192.
Yuan, Y., Wang, X., Yin, F., Zhan, J., 2013. Examination of the quantitative relationship between vegetation canopy height and lai. Adv. Meteorol. 1–6, 2013.
Zheng, H., Cheng, T., Li, D., Yao, X., Tian, Y., Cao, W., Zhu, Y., 2018. Combining unmanned aerial vehicle (uav)-based multispectral imagery and ground-based
     hyperspectral data for plant nitrogen concentration estimation in rice. Front. Plant Sci. 9, 936.




                                                                                    12
