Landbauforschung Völkenrode, Special Issue 340, 2010

**2** **Sampling** **Techniques** **for** **Plants** **and** **Soil**

> *D.* *Wulfsohn*
>
> Department of Agriculture and Ecology, Faculty of Life Sciences,
> University of Copenhagen, Højbakkegaard Allé 9, 2630 Taastrup,
> Denmark, dw@life.ku.dk

**2.1** **Introduction**

The practical implementation of precision farming requires that the
spatial and temporal variability of soils and crops be measured and
understood. It is usually insurmountable and expensive to measure
everything, but it is also almost always unnecessary to do so. Survey
sampling and stereology provide mathematically valid techniques to make
reliable inferences about spatial populations based on small

samples. Stereology provides a stochastic approach to measurement of
geometrical parameters of a given structure such as volume, surface
area, curve length, or ‘particle’1 number (Baddeley and Jensen, 2004).

Soil surveys in many countries have traditionally been based on
‘purposive sampling’ at points or along transects, in which the surveyor
chooses sample locations based on knowledge of the survey area with some
restriction to ensure a balanced sample. Another approach that has been
used in surveys of small, heterogeneous populations has been for the
surveyor to inspect the population and select a small sample of
‘typical’ units that appear to be ‘close to the average’. Many soil
surveys deliberately exclude areas of a field that are known to be
considerably different from the rest of the field and which could
produce inaccurate treatment maps such as for variable rate
fertilization (Francis and Schepers, 1997). Although under the right
conditions such non-probability sampling methods can give useful
results, there is no guarantee that a method that works well under one
set of circumstances (which can only be determined for a situation in
which the results are known) will do so under another (Cochran, 1977).
The need for random sampling procedures for soil surveys has been
recognized (Roels and Jonker, 1983; Abbitt, 2002).

When strong correlations exist between population parameters of interest
and ancillary variables that are more readily measured, then ancillary
data can be used to design efficient unbiased protocols for estimation
and for prediction by interpolation (Sections 2.3.1.1, 2.3.2, 2.3.5,
2.4). The increasing resolution, availability and affordability of
remote sensing images has made it feasible to collect timely information
on soil and crop variability by examining multispectral, near infrared
or thermal infrared images (Basso et al., 2001; Best and Zamora, 2008).
The normalized difference vegetation index (NDVI) (Tucker, 1979) is
correlated with canopy vigor, density, and size and with fruit quality
(Price, 1992; Carlson and Ripley, 1997; Zaman et al., 2004; Fletcher et
al., 2004; Best et al., 2008; Best and Zamora, 2008; Bramley et al.,
2003; Lamb et al., 2004). NDVI may indirectly indicate variability of
soil parameters causing variability in tree growth (Taylor, 2004; Zaman
and Schuman, 2006). Soil color obtained from aerial images can be an
indication of organic matter content and other soil properties (Francis
and Schepers, 1997; Kerry and Oliver, 2003). Apparent soil electrical
conductivity (EC)

1 Any discrete physical object contained in a 3-D object, e.g. grains or
aggregates of soil, cells, fruit, leaves

> 3

measured intensely using electromagnetic induction sensors and
elevations measured using GPS may be correlated with a number of other
soil parameters (Taylor, 2004; Friedman, 2005; Johnson et al., 2005).

Both survey sampling and stereology have many potential errors of
methodology into which

researchers may easily fall (Baddeley and Jensen, 2004). Statistically
valid inferences about the population can be made if: 1) samples are
selected randomly2 with positive (non-zero) probability, and

2\) the sample size is sufficiently large to reflect the variability of
soil or crop characteristics. Limiting sampling to regions that are
readily accessible (e.g. lower branches of a tree to estimate nutrient
content for the entire tree) violates the requirement for a non-zero
probability and may introduce bias in the estimator unless the variation
across the tree branches is spatially homogeneous, see Section 2.2.

**2.2** **Design-based** **and** **model-based** **approaches**

Two approaches to statistical inference from a sample have developed:
design-based and model-based (Thompson, 1992).

Design-based approaches provide unbiased estimators of the parameters of
interest by using a well defined random selection procedure, and require
no statistical model of the structure such as object shape, stationarity
or isotropy. Design-based methods are valuable for the study of highly
organized, heterogeneous structures.

In model-based approaches the random variation is assumed to arise from
intrinsic randomness in the population. The population is regarded as a
single realization of a stationary and/or isotropic stochastic

process and the estimated mean value of a variable does not depend on
the location and shape of the sample windows or probes3. It is therefore
not necessary to randomize sample locations. Researchers

in precision agriculture and soils have mostly relied upon model-based
sampling methods. This has sometimes been under the misconception that
design-based sampling requires independence of samples (see Bruis and de
Gruijter, 1997, and the discussion subsequent to it). A model-based
approach is often preferred when our aim is to formulate models
describing the spatial arrangement of a population. Models of the
population can be of considerable practical advantage when based on
knowledge of the natural phenomena (e.g. climate, dynamics of weed
populations, predators or disease) influencing the distribution of the
population or when models (e.g. regression relations, process based crop
models, soil property functions) are available describing a relationship
between the variable of interest with an auxiliary variable.
Geostatistical interpolation methods (Section 2.4) are model-based. When
a statistical model can be assumed for the population, an adaptive
sampling strategy is often optimal (Thompson and Seber, 1996) (Section
2.5). Model based approaches are the basis of several variance
prediction models used in stereology (Section 2.6).

Model-based designs can be very sensitive to departures from the assumed
model and lead to biased estimators (Baddeley and Jensen, 2004). A less
precise, yet robust, design-based estimator may then

2 The term random is used to mean non-deterministic. It does not mean
that events must be

independently distributed.

3 The term probes in stereology is defined in Section 2.2.

> 4

Landbauforschung Völkenrode, Special Issue 340, 2010

be preferred. When the assumptions underlying an assumed model are
valid, model-based inference can be more precise than design-based
inference (e.g. Särndal, 1978).

**2.3** **Sampling** **concepts**

The concepts reviewed here are taken from survey theory (Cochran, 1977;
Thompson, 1992) and from design-based stereology (Baddeley and Jensen,
2004). Consider the study of a finite ‘population’ of discrete ‘units’
arbitrarily numbered 1, 2, …, *N*, where the population size *N* may be
unknown (depending on the sampling design). Although usually described
with respect to discrete elements (e.g. plants, insects), the theories
are equally applicable to continuous media (e.g. soil) that are divided
up into non-overlapping discrete sub-units. Suppose the population is
the collection of all fruit on a group of trees, then the sampling units
may be plots, trees, branches, fruit clusters or any other division that
is practically convenient. Our aim is to investigate the population by
taking a ‘random sample’ – a randomly selected part of the population –
with the goal of drawing conclusions about the population from
information observed from the sample. Of particular interest are
population totals (e.g. total number of fruit, total canopy surface
area), population means (e.g. mean soil nitrogen content, mean weed
density, mean fruit size) and the spatial-temporal variation of such
quantities (e.g. distribution of fruit size classes, spatial variation
of water content).

A uniform random (UR) ‘sampling design’ is any well defined procedure
for selecting a sample in which all elements of the population are given
an equal probability of being selected. UR sampling (together with
isotropically random direction, i.e. IUR sampling, for length and
surface area estimation) guarantees unbiasedness at the level of
geometric sampling, but does not guarantee adequate precision. There are
many ways to implement UR sampling, including simple random sampling
(SR) and systematic random sampling (SUR, Section 2.3.1). Non-uniform
designs are also possible, e.g. probability proportional to size (PPS)
sampling, and can be very efficient for sampling inhomogeneous or rare
populations (Section 2.3.2).

In simple random sampling without replacement (SR-wor), we use a random
digit generator or a table of random digits to select a fixed number,
*n*, of distinct units with label numbers between 1 and (known) *N*. The
sampling probability for each unit is *n*/*N*. Simple random sampling
with replacement (SR-wr), which generates independent samples, is
generally the most inefficient of sampling designs (followed by SR-wor)
but serves as a reference procedure because it is the only design for
which the mathematical properties are completely known. Three UR
sampling designs for selecting plots from a ‘field’ are illustrated in
Figure 2.1(b)-(d). The Smooth fractionator design (d) is described in
Section 2.3.1.1.

A general estimator of the population total, *Q*, may be written
(Horvitz and Thompson, 1952) as

> ˆ = *n* *qi* (2.1) *i*=1 *i*

where *qi* is the content (the amount of the parameter under study) of
unit *i* in the sample, π*i* is the positive sampling probability of
unit *i*, and *n* is the sample size (number of units). The sampling
probabilities need only be known for the sampled units, but they must be
known exactly to provide unbiased estimates of the population total. A
UR design is a special case of the Horvitz-Thompson

> 5

(HT) estimator (2.1) in which the sampling probability is a constant. SR
and PPS sampling provide unbiased estimators of the population mean.
Multiplying by the sample size provides an unbiased estimator of the
population total, *Q* = *nq* . Systematic sampling and the HT estimator
provide unbiased

estimators of the population total. The corresponding estimator of the
population mean,*q* = *Q*/*n*, is

generally biased for SUR sampling because the denominator *n* is a
random variable. The bias decreases as *n*–1 (e.g. Cochran, 1977). If
the denominator varies little, the bias is negligible.

In stereology several other concepts are introduced: A ‘probe’ is a
geometric entity (3D slice, 2D plane, 1D line, 0D point) used to
penetrate and sample an object. A ‘test system’ is a set of probes used
to obtain stereological estimates, e.g. a regular grid of points for
estimating 2D area (Figure 2.2). (The classic work of Warren Wilson
(1960) and Warren Wilson and Reeve (1959) to estimate LAI and related
parameters using linear probes, and the recent studies by Radtke and
Bolstad (2001) and Wulfsohn et al. (2010) provide examples of this
stereological principle.) The ‘containing space’ is the space in which
the features of interest are entirely contained (the size and extent of
the containing space need not be known exactly). A ‘reference space’, is
a well defined object of known or measurable size, compared to which the
size of the feature of interest can be expressed (Weibel, 1980). An
example is provided by Wulfsohn and Nyengaard (1999). They estimated the
total number of root hairs *N* (the population total) on a plant root
system with a total length *L* (the reference space, estimated using an
unbiased procedure as in Wulfsohn et al., 1999) by the product of the
mean density of root hairs per unit root length (*NL*) and *L*.

**2.3.1** **Systematic** **random** **sampling**

Systematic uniform random sampling often offers an appropriate balance
between the estimator precision and the time spent to obtain samples. It
is easy to execute without mistakes, and in many situations is more
precise than SR for a given sample size. SUR sampling has been shown to
be superior to SR sampling for autocorrelated, stationary populations
when the spatial correlation function decreases with distance between
units (see Cochran, 1977; Cressie, 1993).

In SUR sampling, every *m*-th unit in the population is chosen where *m*
is the ‘sampling period’ and the first unit is selected with ‘random
start’. The random start is obtained by randomly selecting an integer
between 1 and *m*. Each unit of the population appears in the sample
with probability (‘sampling fraction’) 1/*m*. A SUR sample of plots in a
field and a procedure for evenly spacing the plots is presented in
Figure 2.1(c). Sampling on the corners of a regular square grid (‘grid
sampling’ or ‘lattice design’) or, equivalently at fixed intervals along
equally spaced parallel transects (e.g. Flatman and Yfantis, 1984; Mulla
and Bhatti, 1997), is probably the most commonly used SUR design used in
soil and crop surveys. Triangular or hexagonal tessellations of plots
have also been advocated for purposes of semivariogram estimation and
spatial interpolation. A SUR procedure for sampling of branches on a
stem is illustrated in Figure 2.3(a).

> 6

<img src="./1wyjoezh.png" style="width:3.145in;height:2.22in" /><img src="./yls2ceqv.png"
style="width:3.25829in;height:0.46583in" /><img src="./3is5kcm1.png"
style="width:3.25829in;height:0.46583in" /><img src="./b5rywtit.png"
style="width:3.25829in;height:0.46583in" /><img src="./utsnzhxi.png"
style="width:3.25829in;height:0.46583in" /><img src="./adbdrrod.png"
style="width:3.25829in;height:0.46417in" />

Landbauforschung Völkenrode, Special Issue 340, 2010

> <img src="./iszq3elt.png"
> style="width:3.25829in;height:0.46833in" /><img src="./kd4zhuyr.png"
> style="width:3.25829in;height:0.46833in" /><img src="./1lq1wjin.png"
> style="width:3.25829in;height:0.46833in" /><img src="./1dmyupqq.png"
> style="width:3.25829in;height:0.46833in" /><img src="./mdu4pmgp.png"
> style="width:3.25829in;height:0.4675in" /><img src="./hfujns5e.png"
> style="width:3.25829in;height:0.46917in" /><img src="./1ro13yfo.png"
> style="width:3.25829in;height:0.46917in" /><img src="./goheabdl.png"
> style="width:3.25829in;height:0.46917in" /><img src="./wblbrqik.png"
> style="width:3.25829in;height:0.46917in" /><img src="./qyuzp0rn.png"
> style="width:3.25829in;height:0.46583in" /><img src="./i2btpl10.png"
> style="width:2.8275in;height:0.1325in" /><img src="./tehasivh.png" style="width:2.825in;height:0.13in" /><img src="./ed4nyjuk.png" style="width:2.8225in" />(a)
> (b)
>
> \(c\) (d)

**Figure** **2.1:** Three examples of uniform random (UR) sampling
designs for selecting plots in an arbitrarily shaped field, all with the
same sampling fraction: (a) A random point is placed within the unit
tile (white square), which then defines the UR placement of a
tessellation of *N* = 301 sampling units. The tessellation is of extent
to completely contain the field (it defines the containing space).
Providing that the tessellation of plots is positioned randomly, then
all the following designs provide units (and thereby elements of the
population of interest contained within the units) – including edge
plots and empty plots – with equal probability. (b) A simple random
sample (without replacement) of 43 units. (c) A systematic uniformly
random (SUR) sample with sampling fraction 1/*m* = 1/7 and random start
3 (where the top left quadrat has been designated as unit 1, the quadrat
to its right as unit 2, etc.). To avoid aligning samples the position of
the selected units is shifted *k* = round( *m*) = 3 units on consecutive
rows. When *m* is exactly divisible by *k*

then the position of the selected unit is shifted *k* + 1 units on the
first consecutive row and by k units on the remaining rows. The
combination of sampling unit size and sampling period avoids alignment
with tramlines (indicated by dashed lines), a potential cause of
periodicity in the soil or crop. (d) SUR sample with 1/*m* = 1/7
sampling fraction taken from the Smooth arrangement of the units based
on mean plot intensity (‘smooth fractionator’ design). The sampled units
are shown in their smooth order (from top left to right, and then bottom
right to left) in the strip below the map.

> 7

<img src="./tsb1abse.png"
style="width:3.72167in;height:2.68167in" />

**Figure** **2.2:** Point counting. A (0-dimensional) point is defined
as the upper right corner of a cross. The number of intersections, *P*,
between the UR positioned square point grid and the feature of interest
is counted. An unbiased estimator of the feature area is given by *A*
= *apP* , where the grid

constant, *ap*, is the area associated with a single point. A double
grid is illustrated. The fine grid (all points, grid constant *ap*
cm2/point) is used to estimate the area of infected (yellow, 9
intersections) and

diseased (black, 3 intersections) leaf surface while the coarse grid
(circled points, grid constant equal to 9·*ap*) is used to estimate
total surface area (15 intersections). The area fraction of
infected+diseased leaf is 12/(15×9) = 0.089 (Photograph of banana leaf
courtesy of David Collinge, University of Copenhagen).

Systematic sampling behaves very poorly when a sampling period is chosen
that is close to any periodicity in the population variable under study.
Management and cultivation effects such as evenly spaced and aligned
wheel tracks, trees, irrigation furrows, fertilizing bands, or tillage
rows can cause soil or crop conditions to vary systematically
(Wollenhaupt et al., 1997; Mulla and McBratney, 2002). The arrangement
of branching and axillary flowering structures on parent units of a
plant is periodic (phyllotaxy, length of internode). Sequences of
patterns may not be clearly evident at some stages of development and
scales (Guédon et al., 2001). When visible or known, sampling periods
and plot spacing and orientation can be selected so as to not coincide
with these periodicities (e.g. Figure 2.1(c)). To avoid sampling units
from only one side of a plant stem, leaf sampling periods that are
multiples of the phyllotaxic period should be avoided in a systematic
design such as shown in Figure 2.3. An approach that has been
recommended to reduce errors due to periodicity in the landscape is to
take simple randomly positioned samples within systematic random plots,
using ‘unaligned sampling’ (Cochran, 1977; Mulla and McBratney, 2002;
Webster and Oliver, 2007; Wollenhaupt et al., 1994, 1997) or
‘one-per-stratum’ stratified sampling (Breidt, 1995). Breidt (1995)
showed that systematic sampling and one-per-stratum stratified sampling
designs are special cases of ‘Markov chain designs’ in which the *x* and
*y* coordinates of sample points evolve according to Markov chains.

> 8

Landbauforschung Völkenrode, Special Issue 340, 2010

> <img src="./lqbvopvc.png"
> style="width:0.97917in;height:1.06583in" /><img src="./fsblxxdy.png"
> style="width:0.49334in;height:0.37086in" /><img src="./tel3rudi.png"
> style="width:0.24306in;height:0.24913in" /><img src="./c3qb4qso.png"
> style="width:1.22049in;height:0.83226in" /><img src="./ylvjzoxa.png"
> style="width:0.18166in;height:0.47583in" /><img src="./fbabui4i.png"
> style="width:0.26562in;height:0.27257in" /><img src="./i3tuooae.png"
> style="width:0.1826in;height:0.16681in" /><img src="./nxgy53o4.png"
> style="width:0.97834in;height:1.32969in" /><img src="./pymg5z1n.png"
> style="width:0.485in;height:0.37086in" /><img src="./g4xdhedb.png"
> style="width:1.22896in;height:0.83919in" /><img src="./fsdmdizh.png"
> style="width:1.79049in;height:1.4436in" /><img src="./l0xtpirv.png"
> style="width:0.3559in;height:0.24219in" />**11** 13 15 **11**
>
> **10** 11
>
> **8** **9** 12 **8** **7** 10
>
> **6** 6 7 9 **5** **5** 4 8
>
> **4** 3
>
> **3** 5 2
>
> **21** 1 **2**
>
> Stage 1 Stage 2 (a) (b)

**Figure** **2.3:** A two-stage fractionator sampling design applied to
a tree: (a) Primary branches and stem (—) serve as primary sampling
units in the first sampling stage, and (b) higher order branches (----)
are the sampling units in the second stage. Consider sampling the
structure with stage 1 sampling fraction 1/*m*1 = 1/3 and stage 2
fraction 1/*m*2 = 1/4, and uniform random starts equal to 2 and 1,
respectively. (Stage 1): The first stage sample contains all particles
(e.g. fruit) on branches 2, 5, 8 and 11 (circled numbers). (Stage 2):
The final sample (filled circles) contains all fruit on branch segments
1, 5, 9 and 13 within the sampled branches. In practice, data is
collected as the surveyor steps systematically through the structure:
Starting at primary branch 2 we select 2 fruit on branch segment 1. Then
step *m*2 = 4 branch segments as follows: one remaining segment on
branch 2, then jump to branch 5 (2 + *m*1 = 5) to segment number 5 where
we sample 4 fruit, and so on. Empty units (branches with no fruit) have
been ignored. An unbiased estimate of the total number of fruit on the
tree is given by the product of the aggregate sampling period *m* = 12
and the total content of the sample (9 fruit). Figure modified from
Maletti and Wulfsohn (2006).

**2.3.1.1** **Smooth** **fractionator**

The ‘smooth fractionator’ provides a general, straightforward technique
to reduce the estimator variance for SUR sampling of heterogeneous
populations (Gundersen, 2002; Gardi et al., 2006). It aims to increase
estimator precision by increasing within-sample variability and reducing
the variability between samples (Gundersen et al., 1999). The procedure
is as follows: (1) Conceptually or physically divide up the population
into distinct units. (2) Order the units of the population in increasing
size. The size here is that of the parameter of interest or that of any
quantifiable associated variable (e.g. shape,

> 9

<img src="./5rgop0vq.png"
style="width:4.3362in;height:0.88333in" /><img src="./apthktk4.png"
style="width:4.3362in;height:0.8825in" /><img src="./gc01romg.png"
style="width:4.24077in;height:0.26167in" /><img src="./0hhz5zfl.png"
style="width:4.23049in;height:0.26833in" />

texture, spectral intensity, slope, etc.) that is positively correlated
with this parameter. (3) Push out every second unit to produce an
ordering of the units in a monotonically increasing and then decreasing
size. (4) Take a SUR sample of the smooth arrangement. Figure 2.4 shows
examples of smooth arrangements of plants and sub-regions of images.

Figure 2.1(d) shows a sample of plots selected using a smooth
fractionator with the plot mean red-band intensity (between-plot
coefficient of variance, CV = standard deviation/mean = 11%) as the
associated variable. (In this example, assume that the parameter of
interest is perfectly positively correlated with the intensity.) The
coefficient of error (*CE* = *SEM*/mean, where *SEM* = standard error of
the mean) due to taking a sample of plots, *CE*plots, is 1.8% for SR-wr,
1.6% for SR-wor, 3.6% for SURS, and a negligible 0.038% for the Smooth
design. Clearly, when surveying sampling locations at the field scale,
the ease associated with systematic sampling is lost, an increase in
cost which may not justify the gain in precision. The use of GIS and GPS
makes smooth fractionator designs more practical.

> \(a\)
>
> \(b\)

**Figure** **2.4:** The smooth fractionator. (a) A smooth arrangement of
plants, using plant height as an indicator of plant surface area for
estimating total canopy surface area. ‘Rank’ indexes plants by
increasing height, while ‘Smooth’ is the labeling of plants according to
the smooth height arrangement. In this example a sample of plants is
selected with fraction 1/3 with random start 2 from the smooth
arrangement. Figure modified from Wulfsohn et al. (2010). (b) A smooth
ordering can be implemented based on an auxiliary or associated variable
continuously sampled using non-invasive sensors, e.g. the proportion of
red pixels in an image window as an associated variable for (red) apple
number, or the NDVI value at a location in the field as an indicator of
varying crop and soil conditions.

Wulfsohn et al. (2010) examined the efficiency of the smooth
fractionator for estimating the total

surface area, *At*, of a canopy made up of 50 chrysanthemum plants
(between-plant CV(*A*) = 65%). For a sample size of 10 plants and a
precise estimator of leaf area, *CEplants* ( ˆ*t* ) for the Smooth
design was

2% when ordering by plant area (Figure 2.4(a)), 10% when using Smooth
with three plant height

> 10

Landbauforschung Völkenrode, Special Issue 340, 2010

classes as the associated variable and with plants randomly arranged
within height classes before smoothing (introducing a random noise
component), and 21% using SR-wor.

**2.3.2** **Probability** **Proportional** **to** **Size** **(PPS)**
**sampling**

Gardi et al. (2007a) presented a probability proportional to size (PPS)
design called the ‘proportionator’. Image analysis is used to
automatically assign weights to the sampling units, the units are put in
a smooth order based on their weights (an optional step), and then a
sample of specified size *n* is sampled systematically on the ordinate
of the cumulative weight using a sampling period of *Z/n* with random
start (Figure 2.5). The probability of sampling a unit is strictly
proportional to the recorded

weight of the unit and therefore known exactly. An unbiased estimator of
the population total is obtained by applying the HT equation (2.1) with
π*i* = *zi* (*Z* *n*) , where *zi* is the weight of unit *i*

and*Z* = ∑*i*=1*zi* .

Gardi et al. (2007a) compared the performance of SR-wr (i.e.,
independent sampling), SUR, Smooth fractionator and PPS sampling for
estimating the total number of 2500 rectangular ‘particles’ (of one
color intensity but of varying area) and the total and average particle
area (using point counting), from a 2D irregularly shaped region divided
UR into roughly 400 sampling units. The total intensity of a sampling
unit was used as the ancillary variable and weight for Smooth and PPS
sampling, respectively. Simulations were carried out for moderately
inhomogeneous (between-unit *CV* = 67%), intermediary (*CV* = 155%),
clustered (*CV* = 188%) and sparse (*CV* = 293%) particle spatial
distributions. Qualitatively and quantitatively the precision of point
counting for area estimation was almost identical to that for number
estimation. In all cases, SR-wr was the least precise estimator, SURS a
few times more precise than SR, Smooth always more precise than SURS,
and PPS the most precise except for the homogeneous distribution where
Smooth has a slightly smaller *CE*. Increased clustering reduced the
precision, with the effect considerably more pronounced for SR and SURS
than for Smooth and PPS.

> 11

<img src="./yxyey0eu.png"
style="width:4.29158in;height:0.82917in" /><img src="./hev1swlx.png"
style="width:4.29158in;height:0.82917in" /><img src="./4i23f0tw.png"
style="width:4.29158in;height:0.82917in" /><img src="./xcx1ntgm.png"
style="width:4.29158in;height:0.82917in" />

**Figure** **2.5:** Proportionator (PPS) sampling. The complete set of
*N* sampling units is listed in arbitrary order or, as illustrated here,
arranged in a sequence based on the weights as for the smooth
fractionator before SUR sampling. The ordinate shows the accumulated
weight. Sampling on the ordinate is systematic with sampling period
*Z*/*n* and UR start. The probability of sampling a unit is proportional
to the recorded weight of the unit. Sampled units are highlighted (*n* =
6 in this example). Figure based on Gardi et al. (2007a).

Like for the smooth fractionator, the precision of the proportionator is
dependent on having a strong positive correlation between weights and
counts. Any noise in the relationship between weight and count such as
outliers, particles that intersect a sampling unit but are not sampled
by the same unit (see Section 2.7), reduces precision.

**2.3.4** **Multistage** **designs**

A ‘‘level’ is a sampling design in which the measurements are made at a
constant scale. There are several reasons for using multilevel
(multistage, nested) designs. To obtain a sample of seeds from a
vegetable crop, it may be convenient to first take a sample of rows from
a field, then a sample of fruit from plots located along the sampled
rows, and finally take a sample of seeds from the sampled fruit. One may
observe ancillary variables at one scale and make final measurements
much more efficiently at a finer resolution. Indices obtained from
remote sensing images or soil maps might be used to design stratified
(Section 2.3.5), Smooth or PPS designs for field and orchard crops.
Basso et al. (2001) used remote sensing to target sampling of soil and
crop for input to a crop model and combined remote sensing with model
output to identify management zones and to interpret yield maps.

> 12

Landbauforschung Völkenrode, Special Issue 340, 2010

In some cases the variable under study may only be observable at the
object scale or under higher magnification. The physical characteristics
of weeds are similar to those of crops, complicating the detection of
weeds and weed patches in a growing crop (Stafford et al., 1996;
Christensen and Heisel, 1998). Thus, weed maps for patch spraying may
need to be developed by combining manual and automatic measurements at
different scales, such as using aerial imaging (Stafford and Miller,
1993) and vehicle-mounted cameras (Brivot and Marchant, 1995;
Christensen et al., 1997) supplemented by georeferenced observations or
measurements of attributes (e.g. patch shape and size). Handheld
data-logging sampling software can be used to facilitate selection and
recording of samples (Stafford et al., 1996; Gardi et al., 2007b).

Multistage SURS designs are called ‘fractionator’ designs in stereology.
Figure 2.3 illustrates a two-stage fractionator for UR sampling of
particles (fruit, buds, leaves, spurs, etc.) on a tree. This design is
easily applied in practice for a group of trees by treating the union of
branches as a single continuous sequence of sampling units (Wulfsohn et
al., 2006a). Aggelopoulou et al. (2010) used a two-stage (trees,
branches) design to map flowering in an orchard. Data from a SUR sample
of 162 apple trees were collected in one day – a sample size adequate
for semivariogram estimation and for interpolation. Aravena et al.
(2010) used a three-stage design (tree, branch, segment) with systematic
sampling of trees and the design illustrated in Figure 2.3 within trees,
to estimate total yield in several rows of 14 commercial fruit orchards.
Yields at harvest ranged from several thousand bunches for table grapes
to over 40,000 fruit for kiwis and apples. Accuracies of better than 5%
were obtained in six orchards and between 5-10% in five orchards for
workloads of 30-150 minutes, typically less than 90 minutes. Two yield
estimates had absolute errors of about 20%. A variance analysis
indicated that in one of these orchards a precision of 10% could be
obtained for a similar workload by changing the sampling periods for the
three stages.

The smooth fractionator is usually applied in a multistage context.
Steps 1–4 (Section 2.3.1.1) are repeated as many times as desired to the
sampled units obtained in the preceding stage (nesting). Data are
collected only at the last stage. The aggregate sampling fraction is
given by the product of individual sampling fractions, 1/*m* =
1/(*m*1·*m*2·…·*m*k). A nested design leads to dependent observations,
which means that inferences can also be made about macro-micro relations
if data are recorded at relevant stages.

**2.3.5** **Cluster** **sampling**

Cluster sampling is particularly convenient for sampling large or
complex populations. To conduct cluster sampling, divide the population
into a finite number of separate subsets (‘clusters’) in any fashion
that is practically convenient. These clusters are treated as ‘primary
sampling units’. Then select a random sample (e.g. SR, SUR) of clusters.
To uniformly and randomly sample fruit on a tree, take a UR sample of
branches. If all clusters have an equal probability of being selected,
then each unit in the population has equal probability of appearing in
the cluster sample. The fractionator design presented in Figure 2.3 is a
two-stage nested systematic cluster sampling design. The primary
sampling units are primary branches, while the higher order branches
serve as the second stage clusters.

> 13

**2.3.6** **Stratified** **sampling**

Stratified sampling provides a technique for variance reduction. The
population is partitioned into non-overlapping subsets (‘strata’) and
each stratum is treated as a separate population for sampling purposes;
samples are selected independently from each stratum (e.g. requiring a
new random start for each stratum for stratified SURS). Strata can be
physical or conceptual. It may be possible to divide an inhomogeneous
population into subpopulations (which need not be spatially contiguous),
each of which is internally homogeneous. Examples of possible strata are
soil horizons, biogeographical areas, morphological zones within plants
and management zones based on easily measured ancillary variables such
as vegetation indices, yield productivity, soil properties and/or past
field history (Basso et al., 2001; Bramley and Hamilton, 2004; Bramley,
2005; Taylor, 2004; Wulfsohn et al., 2006a; Zaman and Schuman, 2006;
Sciortino et al., 2008; Best and Zamora, 2008). The benefit of
stratification is gained by using different sampling fractions in the
different strata (Figure 2.6). Higher sampling fractions could be used
in strata which have a comparatively high contribution to the population
total to ensure their contributions are estimated more accurately. Very
small (but non-zero probability) sampling fractions could be used in
areas of a field (delineated as strata) known to be odd and likely to
introduce biases when producing management maps for variable rate
application. More intensive sampling could be used in strata where
variation is large, and sparse sampling applied in strata where
properties are more spatially uniform. Seber (2002) reported that large
gains in precision can be obtained if the sampling fraction allocated to
each stratum is proportional to the square root of the population
density in the stratum. Sampling densities for say soil nutrient testing
are selected based on prior knowledge of the spatial scale of
variability of that nutrient or its mobility through the soil profile
(e.g. Francis and Schepers, 1997). McBratney et al. (1999) proposed an
iterative procedure for partitioning a field into strata with
approximately equal variances based upon intensively sampled correlated
ancillary data such as from crop or soil monitors or aerial images.
Gallego (2005) described a method to combine stratified, systematic and
PPS sampling of satellite images.

Figure 2.6 shows a sampling design in which stratified and cluster
sampling have been combined to optimize sampling of fruit from an
orchard, the five trees in a cluster would be treated as a continuous
sequence of branches for further subsampling as in Wulfsohn et al.
(2006a). The purpose of sampling across spatial clusters (blocks) of
trees at each sampling location is to reduce the contribution of local
variability to the total estimator variance, similar to compositing soil
samples obtained from small regions.

**2.3.7** **Directed** **or** **targeted** **sampling**

In sampling programs undertaken for precision farming, an important
objective may be to identify areas of a field that are distinctly
different from the rest of the field to create variable rate application
maps (Mulla, 1993; Francis and Schepers, 1997). A number of studies have
used ‘directed’ or ‘targeted’ sampling designs, in which sampling is
carried out in regions of the field or crop that appear to be visually
different from the rest of the field. A frequent motivation is to make
accurate prescriptions on the basis of relatively few samples.
Christensen et al. (2005) were able to discriminate between N, P and NPK
stress in maize plants using visual-NIR reflectance by sampling specific
leaf growth stages within a plant, but were not successful when
reflectance data for the entire plant were used. Pocknee (2000) showed
that directed soil sampling was more effective for characterizing
vineyard management

> 14

Landbauforschung Völkenrode, Special Issue 340, 2010

<img src="./nmg21rdp.png"
style="width:4.80718in;height:0.56417in" /><img src="./c23wmrly.png"
style="width:4.80718in;height:0.56417in" /><img src="./2sjtpzmh.png"
style="width:4.80718in;height:0.56417in" /><img src="./egnnz01q.png"
style="width:4.80718in;height:0.56417in" /><img src="./hago5tqk.png"
style="width:4.80718in;height:0.56417in" /><img src="./a32xzagt.png"
style="width:4.80718in;height:0.56167in" />zones. For economic
constraints much of the crop and soil property sampling for precision
agriculture has been conducted manually on grids with 100 m spacing or
more (McBratney et al., 1999; Griffin, 1999). A 100 m regular grid is
sometimes excessively coarse to produce accurate prescriptions for site
specific soil management (e.g. Brooker et al., 1995, Brooker and Warren,
1997) while in other cases it may be unnecessarily intensive. Griffin
(1999) and Mulla and McBratney (2002) advocate targeted sampling as a
supplement for a rigorous sampling design, e.g. supplementing samples
taken on a regular systematic grid with a few samples taken at locations
where there is visible evidence of large changes in the measured
property e.g. from aerial photos, electromagnetic induction maps or from
patterns in yield maps observed over several years. Bramley (2003)
demonstrated that vineyard soil surveys could be improved by using high
resolution soil sensing and elevation modeling supplemented by targeted
ground-truthing.

**Figure** **2.6:** A stratified cluster sampling design. (a) Three
management zones (the strata) have been identified in an orchard, e.g.
based on low, medium and high yielding zones from remote sensing images
(highlighted using different colors/tones). (b) In each of the strata, a
nested cluster sampling design is applied, with different sampling
fractions. The first stage sampling units are blocks of five adjacent
trees in a row. In the low yielding (right) zone, a systematic sampling
fraction of 1 in 3 sampling units is used with uniform random start. In
the high yielding (left) stratum a systematic sample of 1 in 9 sampling
units is selected with random start. An intermediate sampling fraction
is used in the medium yielding (middle) stratum. Within each of the
selected sampling units, a systematic sample of fruit might be obtained
using a multistage design such as that shown in Figure 2.3 (perhaps with
different sampling fractions in each zone to obtain a desired total
sample size in each stratum). The estimator of the population total is
the sum of the estimates from the three strata, with proper accounting
for the different sampling fractions.

> 15

**2.4** **Geostatistical** **sampling**

The sampling designs presented in the above sections are design-based.
The population was considered to be fixed while the sampling design
introduced randomness in the sample. When observations are made at
sample locations and the objective is to predict values at non-sampled
locations (spatial prediction) or to determine parameters of a spatial
regression, it is useful to take a

model-based approach. The value of the population parameter at location
***x*** is now considered to be a random variable *z*. Given sampled
values observed at locations **X** = {**x**1,...,**x***n*}, the aim may
be to

predict the value *z*0 at a new location ***x***0. Typically, the values
of the variable of interest at nearby nonsampled locations are not
independent of each other.

Given accurate measurements at sample locations, kriging provides the
interpolation with least bias, and is known as a best linear unbiased
predictor (BLUP). Kriging is an exact interpolator, i.e. it reinstates
the measurement values at the observation locations. Different types of
kriging and geostatistical simulation for interpolation of stationary
and non-stationary data have been described in several textbooks \[e.g.
Matheron, 1963; Journel and Huijbregts, 1978; Isaaks and Srivistava,
1989; Cressie, 1993; Goovaerts, 1997; Lantuéjoul, 2002; Wackernagel,
2003\]. A number of studies have compared kriging and non-parameteric
interpolaton methods such as inverse distance methods, nearest neighbor,
Delauney triangulation and cubic splines (Laslett et al., 1987; Isaaks
and Srivistava, 1989; Wollenhaupt et al., 1994; Gotway et al., 1996).
When intensive sampling is carried out on a regular grid, kriging,
inverse distance, and cubic splines give similar predictions. Kriging is
generally superior when the data to be interpolated have a
well-developed spatial structure, and are sampled at more than 70-80
points with spacings less than the range of the semivariogram in
clusters or at irregular spacings (Laslett et al., 1987; Gotway et al.,
1996; Mulla and McBratney, 2002).

There are two primary concerns when sampling for spatial prediction
using kriging. One is sampling for parameter estimation. Kriging
requires knowledge about the variances of differences between sample
locations (the variogram) or the covariances. The second consideration
is the placement of samples to minimize variances associated with
interpolation. A common dilemma is that geostatistically designed
sampling schemes rely upon knowledge of the semivariogram, yet the
semivariogram is often unknown until the site is sampled. The sampling
needed to determine the semivariogram is often the largest part of the
task (Webster and Burgess, 1984) but sampling designs that are efficient
for parameter estimation are not necessarily efficient for spatial
prediction. A typical compromise is to supplement a systematic grid with
some closely related sample locations (Figure 2.7). Diggle and Lophaven
(2006) found that supplementing a regular grid with a fixed number *k*
of additional points located uniformly randomly within a small radius of
a grid point as in Figure 2.7 yielded more accurate predictions than a
regular grid supplemented by more finely filled grids within *k*
randomly chosen cells of the primary grid. Another approach is to use
transect designs with points separated by decreasing distances along the
transect (Pettitt and McBratney, 1993). Systematically rotated transects
positioned on a systematic grid can be used to investigate anisotropy.
It may be necessary to conduct a preliminary pilot study to establish
the spatial scale. Pettitt and McBratney (1993) reviewed approaches to
design and analysis of soil surveys to investigate the spatial variation
of an attribute where little of no prior knowledge of the scale of the
variation is known. They proposed an approach that was a hybrid of
design- and model-based approaches.

> 16

<img src="./5cxuimd4.png"
style="width:3.12917in;height:1.565in" /><img src="./35ks4ygf.png"
style="width:3.12917in;height:1.565in" />

Landbauforschung Völkenrode, Special Issue 340, 2010

Both the total number of samples and the spacing between samples affect
the accuracy of an experimental semivariogram (Goovaerts, 1997; Webster
and Oliver, 2007). The distance between sample points needs to be just
small enough to resolve the scale of variation at the field level. The
sampling interval for regular grid sampling programs should be from ¼ to
½ the average semivariogram range of the property of interest to
preserve the main patterns of variation (Flatman and Yfantis, 1984).

**Figure** **2.7:** Example of a ‘lattice plus close pairs’ sampling
design (Diggle and Lophaven, 2006), aimed at efficient spatial
prediction when the variogram is also unknown.

Webster and Oliver (1992) recommend 100 to 150 data locations to obtain
a reliable experimental semivariogram for soil attributes using grid
sampling and Matheron’s method of moments. Where variation is
anisotropic even more data may be needed. Kerry and Oliver (2007) found
that an adequate model semivariogram for soil properties in four fields
in the UK could be obtained using 50 locations at an appropriate
distance apart when the residual maximum likelihood (REML) method for
semivariogram estimation was used. The REML approach is parametric and
the data is assumed to follow a multivariate Gaussian distribution
(Patterson and Thompson, 1971; Cressie, 1993; Pardo-Igúzquiza, 1997).
The REML method does not yield an experimental semivariogram. Linear
combinations of the data celled ‘generalized increments’ are used to
simultaneously filter out the trend and estimate the parameters of the
variance-covariance matrix.

When the semivariogram is known, it can be used to evaluate different
sampling designs even before samples are collected. One type of analysis
is to determine optimal spacing and spatial arrangement of grids for
kriging by comparing mean square prediction errors (also called kriging
variances). The kriging variance depends only on the semivariogram (or
covariance function) and the distances between sampled and unsampled
locations, which means it can be computed even when no

> 17

measurements have been made at the potential sampling locations.
McBratney et al. (1981), McBratney and Webster (1981) and Yfantis et al.
(1987) considered the problem of spacing *n* systematic sampling sites
on square, triangular and hexagonal grids to achieve an acceptable value
of the kriging variance over the region of interest. For a given number
of locations per unit area, making observations at the vertices of
equilateral triangles minimizes kriging variance. The gain in precision
is usually so small that square grids are more commonly used (Webster
and Oliver, 2007). Semivariograms of ancillary data can be also used to
guide spacing of sampling grids for correlated properties (Kerry and
Oliver, 2003). The most efficient placement of grid sampling locations
is in the center of each grid cell (Webster and Burgess, 1984).

Kriging variance increases as nugget variance. i.e., the variance due to
sampling and measurement noise, increases. Compositing or bulking of
soil or biomass samples in small regions or accumulating a sample over a
group of plants (treated as a block average) may be used to reduce
short-range fluctuations that add to the noise. The aim is to reduce the
workload of sampling while retaining some of the precision that comes
from having a larger sample size. A model of the semivariogram combined
with the kriging equations can be used to determine the optimum number
of composite samples to collect at sampling locations (Webster and
Burgess, 1984; Oliver et al., 1997). Kriging variances are computed for
different combinations of support (size and shape or area) and
configurations of sampling locations within the blocks. From these, a
combination that meets the tolerance for a given parameter can be
selected. In the absence of tolerance limits, Oliver et al. (1997)
recommended that for soil nutrient mapping 16 cores be bulked from
within a few meters of the sampling location.

Rich data sets may be aggregated into grids of larger cells, where each
cell value represents the average of all points contained within the
cell, to remove unnecessary small-scale detail. Perez-Quezada et al.
(2003) aggregated yield data into 20-m by 20-m cells, using the same
mask coverage from year to year, to compare yields for different years
in the same locations. Bulking and aggregation of samples involves a
‘change of support’ and values are smoothed. Even where average values
are not greatly affected by the smoothing, the observed variability
(e.g. as expressed by the *CV*) can be substantially reduced, especially
where small-scale variability exists.

**2.5** **Adaptive** **sampling**

Surveys and mapping of rare, spatially clustered populations such as
some weed species and insects or early-onset plant diseases or pests may
motivate the use of adaptive sampling designs (Thompson, 1992; Fleischer
et al., 1999). Rather than selecting the sample of units prior to the
survey, the procedure for selecting sites or units may depend on
observed values of the variable of interest during the survey (Thompson,
1992). The goal is to achieve gains in precision or efficiency, compared
to conventional designs with similar sample sizes, or to increase the
number of elements observed for a given sampling effort. A number of
different adaptive sampling strategies exist including ‘sequential
sampling’ (Ghosh et al., 1997) and ‘adaptive cluster sampling’ (Thompson
and Seber, 1996). Chao and Thompson (2001) considered the problem of
optimal selection of new sampling sites to augment a systematic
arrangement of sites.

With ‘sequential estimation’ a fixed number of sampling units are
collected and the population mean or total is estimated along with a
measure of the uncertainty, e.g. confidence interval bounds or the *CE,*
under some assumed spatial pattern of the disease or pest. If the
predicted uncertainty is within a

> 18

<img src="./gkglgm1v.png" style="width:4.00514in;height:0.58in" /><img src="./fwmebg2v.png" style="width:4.00514in;height:0.58in" /><img src="./2z21oclf.png" style="width:4.00514in;height:0.58in" /><img src="./3cbnklqh.png" style="width:4.00514in;height:0.58in" /><img src="./ig1krojp.png"
style="width:4.00514in;height:0.5775in" />

Landbauforschung Völkenrode, Special Issue 340, 2010

desired value sampling ceases, otherwise additional units are added
sequentially until the desired uncertainty is obtained. With sequential
sampling for classification, sampling ends when sufficient numbers of
individuals are collected so that conclusions regarding the population
can be drawn with a desired degree of certainty. Sequential sampling
designs have been used in a number of studies for pest and disease
monitoring in specialty crops (e.g. Allsopp, 1990; Hamilton and
Hepworth, 2004; Turechek and Madden, 1999; Gent et al., 2007).
Sequential sampling can behave very poorly if the sequential sampling
scheme is stopped before the variation in the population is captured
because of having sampled similar units or when the population is
auto-correlated (Robinson and Hamann, 2008).

In ‘adaptive cluster sampling’ the set of primary sampling units is
selected using a probability method, and whenever the observed property
of interest in a primary sampling unit meets a given criterion (e.g.
weeds are detected in a plot) neighboring sampling units are added to
the sample (Figure 2.8). Adaptive cluster sampling will usually provide
an improved indication of the spatial extent of the population of
interest than non-adaptive designs. The selected sample will generally
not provide a design-unbiased estimator of the population mean or total
because inclusion probabilities may not be completely known. Thompson
(1992) describes design-unbiased estimators of the population mean and
total for several adaptive cluster and stratified adaptive cluster
designs.

**Figure** **2.8:** An adaptive cluster sampling design with initial SR
selection of six strip plots. The final sample is highlighted.

**2.6** **The** **accuracy** **of** **an** **estimator**

The accuracy of an estimator can be considered the accumulation of two
important properties: bias (systematic error, the difference between the
expected value of an estimator and the true parameter value) and
precision (random error or noise). We can decompose the mean squared
error (MSE) into a sum of the bias and variance of the estimator:

> 19
>
> MSE = var(*Q*)+bias2(*Q*) (2.2)

Both quantities are important and need to be sufficiently small to
achieve good estimations. Bias cannot be detected from the data (Mandel,
1964). The much desired property of unbiasedness is a consequence of UR
(or IUR) sampling. An important principle in sampling is that variances
are governed largely by sample size rather than by the proportion of the
population included in the sample, except when sampling small
populations (Stuart, 1984; Thompson, 1992). Designing systems to meet
requirements for unbiased sampling makes it possible then to achieve a
desired precision by controlling sample size.

The total variance (MSE) of an unbiased estimator can be written

> MSE(*Q*) = var(*Q*) = var(*Q*)+ var*e*(*Q*) (2.3)

where var(*Q*) is the total (observed) variance, var(*Q*) is the
biological (or natural, intrinsic) variance

(i.e. the true variability between individuals in the population), and
var*e*(*Q*) is the sampling error variance. The biological variance is
the only meaningful variance for management purposes. Equation 2.3 can
also be expressed in terms of the dimensionless squared coefficient of
variance (CV = SD/mean, where SD is the standard deviation) and the
squared coefficient of error (CE = SEM/mean, where SEM is the standard
error of the mean) as

> CV2(*Q*) = CV2(*Q*)+CE2(*Q*) (2.4)

For a multistage nested design, the total estimator variance can be
decomposed into components due to each stage of sampling (Cochran, 1977;
Baddeley and Jensen, 2004). Examples are provided by Wulfsohn et al.
(2010) and Aravena et al. (2010), respectively, for optimizing
estimators of canopy surface area and fruit yield. In many cases it is
sufficient to devise sampling schemes so that the

contribution of sampling error variance to the total observed variance
is small compared to the biological variance. The convention is to aim
for 5 CV2 ≤ CE2 ≤ 2 CV2 to achieve a balance between

precision and cost. Gardi et al. (2007b) describe handheld software that
can be used to assist in collecting data using multistage stereological
designs and obtain estimates of the variance contributions due to each
stage of sampling.

The coefficient of error of any estimator ˆ can be calculated based on
*k* independent realizations of the estimator {*Q*,*Q*,K*Q* } by
applying:

> *k*
>
> (*Qi* −*Q*)2
>
> CE2(*Q*) ≈ ⎜1− *K* ⎟ (*k* −1) *i*=1 (*Q*)2 (2.5)

*k* where *Q* = *Qi*

> *i* =1

and *K* is the number of all possible realizations of ˆ . The variance
components

of a nested design may be estimated by including independent replication
at each level of the sampling

> 20

Landbauforschung Völkenrode, Special Issue 340, 2010

design, e.g. to determine optimal allocation of effort across sampling
stages from a pilot study (Baddeley and Jensen, 2004).

A variation of independent repeated sampling to estimate the total
variance of any complex, multistage design, is provided by the “random
groups” (RG) method (Wolter, 1985). We use *k* repeated samples
according to the design (e.g. *k* systematic samples for a SUR design)
with repetition applied at the primary sampling stage and the sampling
fraction scaled proportionally so as to yield the same final sample
size. Figure 2.9 illustrates the difference between repeated sampling
with independent replication and the RG method for the design shown in
Figure 2.1(c). For the design in Figure 2.3, we may use *k* = 2
replications at the tree level, repeated for say *n* = 8 randomly
selected trees in an orchard, and compute an average *CE*,

> ∧ ∧ 0.5
>
> *CE* ≈ ⎢1 *n* var∧(*Qi* )⎥ (2.6) ⎣ *i*=1 *Qi* ⎦

We distribute the work across trees (which have high biological
variability) rather than attempt to obtain precise estimates for
individual trees. The RG method is generally biased for SUR for which
there is generally dependency between samples. In contrast, an unbiased
(but still imprecise) estimate of the CE of the proportionator (Section
2.2.2) can be obtained at no extra cost by taking *k* = 2 independent
samples each of size *n*/*2* and applying Eq. 2.5. The estimator of the
total now used is the average of the two independent estimates, with
only a small loss in precision compared to using a single sample of size
*n* (Gardi et al., 2007a). Aravena et al. (2010) used repeated
sub-sampling of *sample* *data* at each sampling stage and variance
decomposition to construct a semi-empirical model for the estimator CE.

> 21

<img src="./smcrlpax.png"
style="width:2.9625in;height:1.0475in" /><img src="./d1rygpur.png"
style="width:2.9625in;height:1.04667in" /><img src="./4binc3nc.png"
style="width:2.89294in;height:1.02167in" /><img src="./un3jv1ny.png"
style="width:2.89294in;height:1.02167in" />

> \(a\) (b)

**Figure** **2.9:** Repeated-sampling variance estimation procedures for
an SUR design with sample size *n* and period *m* = 7, cf. Fig. 2.1(c).
An estimate of the population total is obtained by computing the mean of
the estimates obtained from the two samples. (a) Resampling with SUR
period *m* = 7 and

two independent replicates (random-wr starts 1 and 3). The average total
sample size is 2*n*. An estimate of the CE is given by Eq. 2.5 with*Q*
= *Qm*,*i* = *m*∑\[*n*\] *qj* , *k* = 2 and *K* = 7. (b) “Random Groups”

procedure with *k* = 2 replicates each with period *k·m* = 14 (aggregate
period *m* = 7) and random-wor

starts 2 and 6, respectively. The average total sample size is *n*. An
estimate of the CE is given by Eq. 2.5 with*Q* = *Q*2*m*,*i*
= 2*m*∑\[*n*/2\]*qj* , *k* = 2 and *K* = 7.

**2.6.1** **Predicting** **the** **variance** **of** **an**
**estimator** **from** **a** **single** **sample**

In practice, resampling procedures can be prohibitively time consuming
and methods to estimate variances from single sample are desirable.
Devising suitable variance predictors for SUR designs is generally very
difficult because the observations of the sample are not independent.
Single-sample variance predictors are generally biased, with the degree
of bias depending on the extent to which model assumptions are violated
for the population under study. Wolter (1985) discusses the performance
of large number of variance predictors. The Poisson distribution,
according to which CE = 1 *n* (*n* is the sample size), provides a model
for counting noise and is often assumed as a starting

point for a pilot study. Matherons’ transitive approach to modeling the
covariogram is the basis of several single-sample variance predictors
developed for systematic sampling designs in stereology (Matheron, 1971;
Cruz-Orive, 1989). Cruz-Orive (1990, 2004) proposed semi-empirical
models for predicting the sampling error variance of a fractionator
sample. Maletti and Wulfsohn (2006) evaluated the performance of several
models and resampling applied to fractionator sampling of trees. Several
estimators have been proposed motivated by the problem of estimating the
volume of a structure from a systematic sample of area sections (e.g.
Matheron, 1971; Gundersen and Jensen, 1987; Cruz-Orive, 1989; Kiêu,
1997, Gundersen et al., 1999; Garcίa-Fiñana and Cruz-Orive, 2004).
Wulfsohn et al. (2010) showed that similar models could be used to
accurately predict variance components of a

canopy surface area estimator that combined fractionator sampling of
leaves and point counting of leaf area. Point counting (Figure 2.2)
using grids of 1.8 and 4.3 cm2 were found to perform as well as

image analysis and a commercial area meter, respectively, for estimating
the surface area of a chrysanthemum canopy.

> 22

Landbauforschung Völkenrode, Special Issue 340, 2010

**2.7** **Sources** **of** **bias** **and** **unbiased** **counting**
**rules**

The act of sampling a spatial structure by observing it in a bounded
window or plot complicates the estimation of geometric characteristics
by loss of information due to edge effects*.* Baddeley (1999) identified
two main types of edge effects: ‘sampling bias’ where the probability of
observing an object depends on its size and ‘censoring effects’ where
the full extent of the object to be measured cannot be observed within
the window. Sources of non-sampling biases include projection artifacts,
operator effects, and biases arising due to difficulties in defining the
features of interest.

There are two general approaches to dealing with sampling bias:

\(1\) The use of unbiased sampling rules, e.g. the ‘disector’ (Sterio,
1984, Figure 2.10(a)-(b)), the tiling rule (Gundersen, 1978, Fig.
2.10(c)), and the ‘associated point rule’ (Miles, 1978) (Figure
2.10(d)). These generally require some information from outside the
sampling window. We have used the disector counting/sampling rule (a)
within a SUR design to estimate the total yield of seed cucumber grown
as a row crop in farmer fields, achieving precisions of 10% or better
(unpublished report).

\(2\) The use of weighted sampling methods. Usually these are of the
spatial Horvitz-Thomson type, where spatial sampling bias is corrected
by weighting each sampled object by the reciprocal of the sampling
probability, e.g. the domain can be tessellated with copies of the
sampling window and then each sampled object is weighted by the
reciprocal of the number of windows that intersect it.

Observation bias due to occlusions of features observed under
projection, such as in a 2D image, can be substantial. Wulfsohn et al.
(2006b) found occlusion biases in counting of flowers and fruit on small
trees of –18% to –31%. In combination with occlusion errors, biases
(both positive and negative) can arise because of errors in thresholding
and feature recognition. Several studies reporting on algorithms for
automatic recognition of apples using 2D images of trees have achieved
successful recognition rates from 56% to 100% (typically 85-97%). Rates
of false positives were usually less than 5% (Bulanon et al., 2002;
Stajnko et al., 2004; Tabb et al., 2006) but could be as high as +15–83%
(Stajnko et al., 2004). Bulanon et al. (2002) reported biases of –18%
(average of 10 images) under poor lighting conditions. The data of
Stajnko et al. (2004) indicate biases of –13% to +21% for averages from
thermal images of 20 trees obtained at four development stages.

In some situations there can also be considerable error in recording
samples. In surveys of insects in a field it is highly unlikely that
every individual will be captured or detected. When carrying out
observations of hard-to-detect or rare events such as some weed species
or diseases along transects or in plots, the probability of detecting an
object depends in some way on its distance from the observer as well as
on its size. Thompson (1992) presents methods for estimating and
modeling detectability, i.e., the probability that an object in a
selected sampling unit is observed.

> 23

<img src="./sezdytyb.png" style="width:0.57167in" /><img src="./hvxrcvs0.png" style="width:3.605in;height:1.435in" /><img src="./bs3l3bwc.png" style="width:1.56in;height:1.54917in" /><img src="./aq41i2dy.png" style="width:1.56in;height:1.56in" />

> <img src="./qfg40qgi.png"
> style="width:3.64833in;height:1.67083in" />(a)
>
> \(b\)
>
> \(c\) (d)

**Figure** **2.10:** Unbiased counting rules used to select objects with
equal probability in UR positioned finite windows. (a) ‘Disector’ or
‘first-time’ rule (Sterio, 1984). An object is sampled if it overlaps
the strip in question but does not cross the right border of the strip
(i.e. an object is selected by the first strip which intersects it, when
the strips are ordered from right to left). The plant marked (\*) is
sampled by the highlighted strip. (b) Illustration of ‘physical
disector’ sampling rule (Sterio, 1984). Strips narrower than the
horizontal width of any object are used in this example to develop a
fractionator with *h*/*d* = 1/10 sampling fraction for a ‘double
systematic subsampling’ design. The dashed line is called a counting
line while the fulldrawn line is called a lookup line. An object is
sampled by a strip of width *h* if it intersects the counting line but
does not intersect the lookup line. The plant marked with an asterisk is
sampled by the highlighted strip. (c) Associated point rule (Miles,
1978) samples the 7 fruit indicated with asterisks, which all have their
(dimensionless) left tangent point located in the sampling window. (d)
Tiling rule (Gundersen, 1978) applied to sample the 8 fruit indicated
with asterisks, all of which overlap the window and do not cross the
infinite boundary with fulldrawn lines. (Photograph of plants in (a) and
(b) by Hans-Werner Griepentrog, University of Copenhagen).

> 24

Landbauforschung Völkenrode, Special Issue 340, 2010

**2.8** **Remarks**

The proper application of sampling principles is necessary to obtain
design- or model-unbiased estimators of population attributes and their
variability and this is equally true whether variables are measured
manually or automated using non-destructive sensors – a machine moving
through a field or orchard, equipped with sensors to measure crop yield
or structure is performing ‘spatial sampling’ (Wulfsohn et al., 2004).
Equipped with the basic sampling and variance reduction techniques
reviewed in this section there is considerable flexibility to design
practical sampling protocols for precision farming of soils and
specialty crops. Prior knowledge and ancillary information obtained by
remote sensing and non-destructive soil and plant sensors can be used
within a random sampling framework to design protocols that provide an
appropriate balance between statistical precision and cost (time and
technology investment).

**References**

Abbitt PJ (2002) Soil Surveys. In: El-Shaarawi AH, Piegorsch WW (eds),
Encyclopedia of Environmetrics. Wiley: New York, pp. 2027–2029

Aggelopoulou K, Wulfsohn D, Fountas S, Gemtos TA, Nanos GD, Blackmore S
(2010) Spatial variability of quality and yield in a small apple
orchard. Precision Agriculture (DOI 10.1007/s11119-009-9146-9)

Allsopp PG (1990) Sequential sampling plans for nematodes affecting
sugarcane in Queensland. Australian Journal of Agricultural Research 41:
351–358

Aravena Zamora F, Potin Téllez C, Wulfsohn D, Zamora I, García-Fiñana, M
(2010) Performance of a procedure for fruit tree yield estimation. Paper
No. 1009638. St. Joseph, Mich.: ASABE, 16 pp.

Baddeley AJ (1999) Spatial sampling and censoring. In: Barndorff-Nielsen
OE, Kendall WS, van Lieshout MNM (Eds), Stochastic Geometry: Likelihood
and Computation. London: Chapman and Hall, pp. 37–78

Baddeley AJ, Jensen EBV (2004) Stereology for Statisticians. Chapman and
Hall/CRC Boca Raton. Basso B, Ritchie JT, Pierce FJ, Braga RP, Jones JW
(2001) Spatial validation of crop models for

> precision agriculture. Agricultural Systems 68: 97–112

Best S, Salazar F, Bastias R, Leon L (2008) Crop load estimation model
to optimize yield–quality ratio in apple orchards, Malus Domestica
Borkh., var. Royal Gala. Journal of Information

Technology in Agriculture 3: 11–18
(<u>http://www.jitag.org/ojs/index.php/jitag/article/view/40/16</u>)
Best S, Zamora I. (2008) Tecnologías Aplicable en Agricultura de
Precisión. Use de Tecnología de

> Precisión en Evaluación, Diagnóstico y Solución de Problemas
> Productivos. Santiago de Chile: Fundacion para la Innovacion Agraria

Bramley R (2003) Smarter thinking on soil survey. Australian and New
Zealand Wine Industry Journal 18: 88-94

Bramley B, Pearse B, Chamberlain P (2003) Being profitable precisely - A
case study of precision viticulture from Margaret river. The Australian
& New Zealand Grapegrower & Winemaker 473a: 84–87

Bramley RGV, Hamilton RP (2004) Understanding variability in winegrape
production systems. 1. Within vineyard variation in yield over several
vintages. Australian Journal of Grape and Wine Research 10: 32–45

> 25

Bramley RGV (2005) Understanding variability in winegrape production
systems. 2. Within vineyard variation in quality over several vintages.
Australian Journal of Grape and Wine Research 11: 33–42

Breidt FJ (1995) Markov chain designs for one-per-stratum sampling. In:
Proceedings of the section on survey research Mmethods, American
Statistical Association, Vol. 1, pp. 356–361

Brivot R, Marchant JA (1995) Segmentation of plants and weeds using
Infra-red images. IEEE Proceedings – Vision, Image and Signal Processing
143: 118–124

Brooker PI, Warren S (1997) Sampling design for irrigated vineyards in
the Riverland of South Australia. Environmental International 23:
215–219

Brooker PI, Winchester JP, Adams AC (1995) A geostatistical study of
soil data from an irrigated vineyard near Waikerie, South Australia.
Environmental International 21: 699–704

Bruis DJ, de Gruitjer JJ (1997) Random sampling or geostatistical
modelling? Choosing between design-based and model-based sampling
strategies for soil (with discussion). Geoderma 80: 1–59

Bulanon DM, Kataoka T, Ota Y, Hiroma T (2002) A segmentation algorithm
for the automatic recognition of *Fuji* apples at harvest. Biosystems
Engineering 83: 405–412

Carlsen TN, Ripley DA (1997) On the relation between NDVI, fractional
vegetation cover and leaf area index. Remote Sensing of Environment 62:
241–252

Chao CT, Thompson SK (2001) Optimal adaptive selection of sampling
sites. Environmetrics 12: 517– 538

Christensen LK, Upadhyaya SK, Jahn B, Slaughter DC, Tan E, Hills D
(2005) Determining the influence of water deficiency on NPK stress
discrimination in maize using spectral and spatial information.
Precision Agriculture 6: 539–550

Christensen S, Heisel T (1998) Patch spraying using historical, manual
and real-time monitoring of weeds in cereals. Zeitschrift für
Pflanzenkrankheiten und Pflanzenschutz XVI: 257–265

Christensen S, Heisel T, Secher BJM, Jensen A, Haahr V (1997) Spatial
variation of pesticide doses

> adjusted to varying canopy density in cereals. In: Stafford JV (Ed.),
> Precision Agriculture ’97, Proceedings of the 1st European Conference
> on Precision Agriculture. Oxford, UK: BIOS
>
> Scientific Publishers, Vol. 1, pp. 211–218.

Cochran WG (1977) Sampling Techniques, 3rd ed. New York: Wiley

Cressie NAC (1993) Statistics for Spatial Data (revised version). New
York: Wiley

Cruz-Orive LM (1989) On the precision of systematic sampling: A review
of Matheron’s transitive methods. Journal of Microscopy 153: 315–333

Cruz-Orive LM (1990) On the empirical variance of a fractionator
estimate. Journal of Microscopy 160: 89–95

Cruz-Orive LM (2004) Precision of the fractionator from Cavalieri
designs. Journal of Microscopy 213: 205–211

Diggle P, Lophaven S (2006) Bayesian geostatistical design. Scandinavian
Journal of Statistics 33: 53–64

Flatman GT, Yfantis AA (1984) Geostatistical strategy for soil sampling:
The survey and the census. Environmental Monitoring and Assessment 4:
335–349

Fleischer SJ, Blom PE, Weisz R (1999) Sampling in precision IPM: When
the objective is a map. Phytopathology 89: 1112–1118

Fletcher RS, Escobar DE, Skaria M (2004) Evaluating airborne normalized
difference vegetation index imagery for citrus orchard surveys.
HortTechnology 14: 91–94

> 26

Landbauforschung Völkenrode, Special Issue 340, 2010

> Francis DD, Schepers JS (1997) Selective soil sampling for
> site-specific nutrient management. In: Stafford JV (Ed), Precision
> Agriculture ’97, Proceedings of the 1st European Conference on
> Precision Agriculture. Oxford, UK: BIOS Scientific Publishers, Vol. 1,
> pp. 119–126
>
> Friedman SP (2005) Soil properties influencing apparent electrical
> conductivity: A review. Computers and Electronics in Agriculture 46:
> 45–70
>
> Gallego FJ (2005) Stratified sampling of satellite images with a
> systematic grid of points. ISPRS Journal of Photogrammetry and Remote
> Sensing 59: 369–376
>
> García-Fiñana M, Cruz-Orive LM (2004) Improved variance prediction for
> systematic sampling on . Statistics 38: 243–272
>
> Gardi JE, Nyengaard JR, Gundersen HJG (2006) Using biased image
> analysis for improving unbiased stereological number estimation – A
> pilot simulation study of the smooth fractionator. Journal of
> Microscopy 222: 242–250
>
> Gardi JE, Nyengaard JR, Gundersen HJG (2007a) The proportionator:
> Unbiased stereological estimation using biased automatic image
> analysis and non-uniform probability proportional to size sampling.
> Computers in Biology and Medicine (DOI
> 10.1016/j.compbiomed.2007.11.002)
>
> Gardi JE, Wulfsohn D, Nyengaard JR (2007b) A handheld support system
> to facilitate stereological measurements and mapping of branching
> structures. Journal of Microscopy 227: 124–139
>
> Gent DH, Turechek WW, Mahaffee WF (2007) Sequential sampling for
> estimation and classification of the incidence of hop powdery mildew
> I: Leaf sampling. Plant Disease 91: 1002–1012

Ghosh M., Mukhopadhyay N., Sen PK (1997) Sequential Estimation. New
York: Wiley

> Goovaerts P (1997) Geostatistics for Natural Resources Evaluation*.*
> New York: Oxford University Press, 483 pp.
>
> Gotway CA, Ferguson RB, Hergert GW, Peterson TA (1996) Comparison of
> kriging and inverse-distance methods for mapping soil parameters. Soil
> Science Society of America Journal 60: 1237–1247

Griffin SJ (1999) Directed soil sampling as a means of increasing
nutrient map accuracy using

> complementary precision farming data. In: Stafford JV (ed), Precision
> Agriculture ’99, Proceedings of the 2nd European Conference on
> Precision Agriculture. Sheffield, UK: Sheffield Academic Press, Vol.
> 1, pp. 141–150
>
> Guédon Y, Barthélémy D, Caraglio Y, Costes E (2001) Pattern analysis
> in branching and axillary flowering sequences. Journal of Theoretical
> Biology 212: 481–520
>
> Gundersen HJG (1978) Estimators of the number of objects per unit area
> unbiased by edge effects. Microscopica Acta 81: 107–117

Gundersen HJG (2002) The smooth fractionator. Journal of Microscopy 207:
191–210 Gundersen HJG, Jensen EB (1987) The efficiency of systematic
sampling in stereology and its

> prediction. Journal of Microscopy 147: 229–263
>
> Gundersen HJG, Jensen EBV, Kiêu K., Nielsen J (1999) The efficiency of
> systematic sampling in stereology – Reconsidered. Journal of
> Microscopy 193: 199–211

Hamilton AJ, Hepworth G (2004) Accounting for cluster sampling in
constructing enumerative sequential sampling plans. Journal of Economic
Entomology 97: 1132–1136

Horvitz DG, Thompson DJ (1952) A generalization of sampling without
replacement from a finite universe. Journal of the American Statistical
Association 47: 663–685

Isaaks EH, Srivistava RM (1989) An Introduction to Applied
Geostatistics. New York: Oxford University Press

> 27

Johnson CK, Eigenberg RA, Doran JW, Wienhold BJ, Eghball B, Woodbury BL
(2005) Status of soil electrical conductivity studies by central state
researchers. Transactions of the ASAE 48: 979–989

Journel AG, Huijbregts CJ (1978) Mining Geostatistics. London, UK:
Academic Press

Kerry R, Oliver MA (2003) Variograms of ancillary data to aid sampling
for soil surveys. Precision Agriculture 4: 261–278

Kerry R, Oliver MA (2007) Comparing sampling needs for variograms of
soil properties computed by the method of moments and residual maximum
likelihood. Geoderma 140: 383–396

Kiêu K (1997) Three lectures on systematic geometric sampling.
*Memoirs*, Vol. 13. Aarhus, Denmark: Department of Theoretical
Statistics, University of Aarhus

Lamb DW, Weedon MM, Bramley RGV (2004) Using remote sensing to predict
grape phenolics and colour at harvest in a cabernet sauvignon vineyard:
Timing observations against vine phenology and optimising image
resolution. Australian Journal of Grape and Wine Research 10: 46–54

Lantuéjoul C (2002) Geostatistical Simulation. Models and Algorithms.
Berlin/Heidelburg: Springer-Verlag

Laslett GM, McBratney AB, Pahl PJ, Hutchinson MF (1987) Comparison of
several spatial prediction methods for soil pH. Journal of Soil Science
38: 325–341

Maletti GM, Wulfsohn D (2006) Evaluation of variance prediction models
for fractionator sampling of trees. Journal of Microscopy 222: 228–241

Mandel J (1964) The Statistical Analysis of Experimental Data. New York:
Dover Publications Matheron G (1963) Principles of Geostatistics.
Economic Geology 58: 146–166

Matheron G (1971) The Theory of Regionalized Variables and its
Applications. Les Cahiers du Centre de Morphologie Mathématique de
Fointainebleau, No. 5. Paris, France: École Nationale Suipèrieure des
Mines

McBratney AB, Webster R (1981) The design of optimal sampling schemes
for local estimation and mapping of regionalized variables: II, Program
and examples. Computers & Goesciences 7: 335–365

McBratney AB, Webster R, Burgess TM (1981) The design of optimal
sampling schemes for local estimation and mapping of regionalized
variables: I, Theory and method. Computers & Goesciences 7: 331–334

McBratney AB, Whelan BM, Walvoort DJJ, Minasny B (1999) A purposive
sampling scheme for precision agriculture. In: Stafford JV (ed),
Precision Agriculture ’99, Proceedings of the 2nd European Conference on
Precision Agriculture. Sheffield, UK: Sheffield Academic Press, Vol. 1,
pp 101–110

Miles RE (1978) The sampling, by quadrats, of planar aggregates. Journal
of Microscopy 113: 257– 267

Mulla DJ (1993) Mapping and managing spatial patterns in soil fertility
and crop yield. In: Robert PC, Rust RH, Larson WE (eds), Site Specific
Crop Management. Madison, WI: ASA/CSSA/SSSA, pp. 15–26

Mulla DJ, Bhatti AU (1997) An evaluation of indicator properties
affecting spatial patterns in N and P requirements for winter wheat
yield. In: Stafford JV (ed), Precision Agriculture ’97, Proceedings of
the 1st European Conference on Precision Agriculture. Oxford, UK: BIOS
Scientific Publishers, Vol. 1, pp. 145–153

Mulla DJ, McBratney AB (2002) Soil spatial variability. In: Warwick AW
(ed), Soil Physics Companion. Boca Raton: CRC Press, pp. 343–373

> 28

Landbauforschung Völkenrode, Special Issue 340, 2010

Oliver MA, Frogbrook Z, Webster R, Dawson CJ (1997) A rational strategy
for determining the number of cores for bulked sampling of soil. In:
Stafford JV (ed), Precision Agriculture ’97, Proceedings of the 1st
European Conference on Precision Agriculture. Oxford, UK: BIOS
Scientific Publishers, Vol. 1, pp. 155–162

Pardo-Igúzquiza E (1997) MLREML: A computer program for the inference of
spatial covariance parameters by maximum likelihood and restricted
maximum likelihood. Computers & Goesciences 23: 153–162

Patterson HD, Thompson R (1971) Recovery of interblock information when
block sizes are unequal. Biometrika 58: 545–554

Perez-Quezada JF, Pettygrove GS, Plant RE (2003) Spatial–temporal
analysis of yield and soil factors in two four-crop–rotation fields in
the Sacramento Valley, California. Agronomy Journal 95: 676–687

Pettitt AN, McBratney AB (1993) Sampling designs for estimating spatial
variance components. Applied Statistics 42: 185–209

Pocknee S (2000) The management of within-field soil spatial
variability. PhD Dissertation, University of Georgia, USA.

Price JC (1992) Estimating vegetation amount from visible and near
infrared reflectances. Remote Sensing of the Environment 41: 29–34

Radtke PJ, Bolstad PV (2001) Laser point-quadrat sampling for estimating
foliage-height profiles in broad-leaved forests. Canadian Journal of
Forestry Research 31: 410–418

Robinson AP, Hamann JD (2008) Correcting for spatial autocorrelation in
sequential sampling. Journal of Applied Ecology 45: 1221–1227

Roels JM, Jonker PJ (1983) Probability sampling techniques for
estimating soil erosion. Soil Science Society of America Journal 47:
1224–1228

Särndal CE (1978) Design-based and model-based inference in survey
sampling (with discussion).

> Scandinavian Journal of Statistics 5: 27–52

Seber GAF (2002) The Estimation of Animal Abundance and Related
Parameters, 2nd ed. Caldwell, NJ, USA: The Blackburn Press

Sciortino M, Wulfsohn D, Andreassen A, Gianquinto G, Aaslyng JM (2008)
Validation of canopy photosynthesis models for climate control in
greenhouses. Acta Horticulturae 801: 1309–1315

Sterio DC (1984) The unbiased estimation of number and sizes of
arbitrary particles using the disector. Journal of Microscopy 134:
127–136

Stafford JV, Le Bars JM, Ambler B (1996) A hand-held datalogger with
integral GPS for producing weed maps by field walking. Computers and
Electronics in Agriculture 14: 235–247

Stafford JV, Miller PCH (1993) Spatially selective application of
herbicide. Computers and Electronics in Agriculture 11: 23–36

Stajnko D, Lakota M, Hočevar M (2004) Estimation of number and diameter
of apple fruits in an orchard during the growing season by thermal
imaging. Computers and Electronics in

> Agriculture 42: 31–42

Stuart A (1984) The Ideas of Sampling, 3rd ed. New York, NY: MacMillan
Publishing Company

Tabb A, Peterson DL, Park J (2006) Segmentation of apple fruit from
video via background modeling. ASABE Paper No. 063060. St. Joseph,
Michigan, 49085.

Taylor JA (2004) Digital terroirs and precision viticulture:
Investigations into the application of information technology in
Australian vineyards. PhD thesis, The University of Sydney, New South
Wales, Australia.

Thompson SK (1992) Sampling. New York: Wiley

> 29

Thompson SK, Seber GAF (1996) Adaptive Sampling. New York: Wiley

Tucker CJ (1979) Red and photographic infrared linear combinations for
monitoring vegetation. Remote Sensing of Environment 8: 127–150

Turechek WW, Madden LV (1999) Spatial pattern analysis and sequential
sampling for the incidence

of leaf spot on strawberry in Ohio. Plant Disease 83: 992–1000
Wackernagel H (2003) Multivariate Geostatistics, 3rd ed. Berlin:
Springer-Verlag

Warren Wilson J, Reeve JE (1959) Analysis of the spatial distribution of
foliage by two dimensional point quadrats. New Phytologist 58: 92–101

Warren Wilson J (1960) Inclined point quadrats. New Phytologist 59: 1–8.

Webster R, Burgess TM (1984) Sampling and bulking strategies for
estimating soil properties in small regions. European Journal of Soil
Science 35: 127–140

Webster R, Oliver MA (1992) Sample adequately to estimate variograms of
soil properties. Journal of

> Soil Science 43: 177–192

Webster R, Oliver MA (2007) Geostatistics for Environmental Scientists,
2nd ed. New York: Wiley

Weibel ER (1980) Stereological Methods. Vol. 2: Theoretical foundations.
Academic Press, London. Wollenhaupt NC, Mulla DJ, Gotway Crawford CA
(1997) Soil sampling and interpolation techniques for

> mapping spatial variability of soil properties. In: Pierce FJ, Sadler
> EJ (eds). The State of Site-Specific Management for Agriculture.
> Madison, WI: ASA/CSSA/SSSA, pp. 19–53

Wollenhaupt NC, Wolkowski RP, Clayton MK (1994) Mapping soil test
phosphorus and potassium for variable rate fertilizer application.
Journal of Production Agriculture 7: 441-448

Wolter K (1985) Introduction to Variance Estimation. New York:
Springer-Verlag

Wulfsohn D, Nyengaard JR, Gundersen HJG, Jensen EBV (2004) Stereology
for Biosystems Engineering. In: Proceedings of AgEng2004 (CD). Leuven,
Belgium, September 12-16, 2004

Wulfsohn D, Maletti GM, Toldam-Andersen TB (2006a) Unbiased estimator of
the number of flowers on a tree. Acta Horticulturae 707: 245–252

Wulfsohn D, Nørremark M, Nielsen J, Maletti GM, Blackmore BS,
Toldam-Andersen T (2006b) Stereological estimators of the number of
blossoms and fruit on trees using image analysis. Paper No. 063063,
presented at the 2006 Annual Meeting of the American Society of
Agricultural and Biological Engineers, Portland, OR, July 9-12, 2006.
St. Joseph, Mich.: ASABE

Wulfsohn D, Nyengaard JR (1999) Simple stereological procedure to
estimate the number and dimensions of root hairs. Plant & Soil 209:
129–136

Wulfsohn D, Nyengaard JR, Gundersen HJG, Cutler AJ, Squires TM (1999)
Non-destructive, stereological estimation of plant root length,
branching pattern and diameter distribution. Plant & Soil 214: 15–26

Wulfsohn D, Sciortino M, Aaslyng JM, García-Fiñana M (2010)
Non-destructive, stereological estimation of canopy surface area.
Biometrics 66: 159–168

Yfantis EA, Flatman GT, Behar JV (1987) Efficiency of kriging estimation
for square, triangular, and hexagonal grids. Mathematical Geology 19:
183–205

Zaman QU, Schuman AW (2006) Nutrient management zones for citrus based
on variation in soil properties and tree performance. Precision
Agriculture 7: 45–63

Zaman QU, Schumann AW, Miller MW, Buchanon S, Hostler K, Perkins G
(2004) Variable rate nitrogen application in florida citrus based on
ultrasonically-sensed tree size. In: Mulla DJ (Ed), Proceedings of the
7th International Conference on Precision Agriculture (CD). St. Paul,
Minn.: The Precision Agriculture Center, University of Minnesota

> 30
