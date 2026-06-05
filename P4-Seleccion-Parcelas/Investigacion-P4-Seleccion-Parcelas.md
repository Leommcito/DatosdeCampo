# Selección de Parcelas para Muestreo en Campo en Huerto de Mandarinas

## 1. Introducción

La presente investigación forma parte de una tesis cuyo objetivo es establecer un protocolo de captura manual con smartphone en huertos densos de mandarinas, optimizado para modelos de detección YOLO y seguimiento MOT (Multiple Object Tracking). El diseño experimental incluye una comparación A/B entre el protocolo propuesto y la captura con cámara nativa en modo automático, evaluando métricas de detección (mAP) y seguimiento (MOTA, IDF1). La validez externa de los resultados de este experimento depende críticamente de que las parcelas seleccionadas para la captura sean representativas de la variabilidad de vigor presente en el huerto.

En huertos frutales, la variabilidad espacial del vigor vegetativo es una fuente importante de heterogeneidad que afecta la densidad de follaje, la iluminación del dosel y, en consecuencia, la calidad de las imágenes capturadas y el rendimiento de los algoritmos de visión por computadora. Si las parcelas seleccionadas para el experimento A/B presentan vigores similares, los resultados no serán generalizables a condiciones de bajo o alto vigor, limitando la utilidad del protocolo propuesto.

El objetivo específico de este capítulo es seleccionar las parcelas y las hileras dentro de ellas que serán objeto de captura de video en campo, justificando cada decisión metodológica con el nivel de respaldo bibliográfico correspondiente. La estructura del documento es la siguiente: la Sección 2 describe el área de estudio y los datos disponibles; la Sección 3 presenta el estado del arte sobre métodos de muestreo en huertos frutales; la Sección 4 detalla la metodología propuesta; la Sección 5 discute las decisiones tomadas y sus limitaciones; y la Sección 6 resume las conclusiones.

## 2. Área de Estudio y Datos Disponibles

### 2.1 Caracterización de las Parcelas

El área de estudio comprende **4 parcelas** de mandarina variedad **Murcott** de **4 años de edad**, ubicadas en un huerto comercial. Cada parcela tiene una superficie de **0.5 ha** (aproximadamente 70 × 70 m), configuración cuadrada, y contiene **13 hileras** de árboles. Las parcelas comparten el mismo marco de plantación, están alejadas de bordes del huerto y han sido manejadas con prácticas agronómicas homogéneas (riego, fertilización y poda), lo que minimiza fuentes de variabilidad no asociadas al vigor vegetativo.

La variedad Murcott (también conocida como Afourer o Delite) es una mandarina híbrida de maduración tardía, ampliamente cultivada en regiones mediterráneas y subtropicales. A los 4 años de edad, los árboles se encuentran en la fase de entrada a producción comercial, con un porte y desarrollo de copa que permite la aplicación de técnicas de visión por computadora, pero con una densidad de follaje suficiente para representar el desafío de captura en huertos densos que motiva esta investigación.

### 2.2 Datos de Teledetección

Se dispone de imágenes del satélite **Sentinel-2** con los siguientes índices de vegetación:

| Índice | Banda / Resolución | Píxeles por parcela (70 × 70 m) | ¿Resuelve hileras individuales? | ¿Apto para selección de parcelas? |
|---|---|---|---|---|
| **NDVI** | Banda 4 (R) + Banda 8 (NIR), 10 m | ~7 × 7 = **49 píxeles** | No. Cada píxel cubre ~2 hileras (~5.4 m cada una) | **Sí** — 49 píxeles proporcionan una media robusta por parcela |
| **MSAVI2** | Banda 4 (R) + Banda 8 (NIR), 10 m | ~7 × 7 = **49 píxeles** | No | Sí |
| **NDRE** | Banda 5 (Red Edge 1) + Banda 6 (Red Edge 2), 20 m | ~3.5 × 3.5 = **12 píxeles** | No. Cada píxel cubre ~4 hileras | **Limitado** — resolución insuficiente para selección, útil como descriptor complementario |

La resolución espacial de Sentinel-2 no permite discriminar hileras individuales, dado que cada hilera ocupa aproximadamente 5.4 m de ancho, mientras que un píxel NDVI (10 m) cubre aproximadamente el equivalente a 2 hileras, y un píxel NDRE (20 m) cubre aproximadamente 4 hileras. Sin embargo, **sí permite caracterizar y comparar parcelas enteras entre sí**, ya que el número de píxeles por parcela (49 para NDVI y MSAVI2; 12 para NDRE) es estadísticamente suficiente para estimar una media representativa del vigor de cada unidad experimental.

## 3. Estado del Arte

### 3.1 Muestreo Aleatorio Simple (MAS / SRS)

El Muestreo Aleatorio Simple (MAS, o Simple Random Sampling, SRS) es el diseño de muestreo más fundamental en estadística, en el cual cada unidad de la población tiene la misma probabilidad de ser seleccionada. Su fundamento teórico está establecido en la obra clásica de [P79] (Miranda et al., 2018) y [P80] (Uribeetxebarria et al., 2018), quienes lo utilizaron como línea base para comparar la eficiencia de métodos de muestreo más complejos en huertos frutales. La principal ventaja del MAS es su simplicidad y su sólido respaldo teórico, derivado de la teoría de muestreo de (Cochran, 1977).

No obstante, en el presente estudio, el MAS presenta una limitación crítica: con solo 4 parcelas disponibles, la selección aleatoria de 2 parcelas podría resultar en la elección de 2 unidades con vigor muy similar (por ejemplo, ambas de vigor medio), perdiendo la representatividad de los extremos de la distribución de vigor del huerto. Esta limitación motiva la búsqueda de un método de selección que maximice la variabilidad capturada con el número limitado de parcelas disponibles.

### 3.2 Muestreo Estratificado con NDVI de Alta Resolución

El muestreo estratificado utiliza una variable auxiliar para dividir la población en estratos homogéneos internamente y heterogéneos entre sí, permitiendo una representación más eficiente de la variabilidad total. En el contexto de huertos frutales, el Índice de Vegetación de Diferencia Normalizada (NDVI) ha sido ampliamente utilizado como variable de estratificación.

[P79] (Miranda et al., 2018) y [P80] (Uribeetxebarria et al., 2018) aplicaron muestreo estratificado con NDVI en huertos de durazno utilizando imágenes aéreas de muy alta resolución espacial (0.25 m), logrando reducciones del tamaño de muestra necesario entre el 17 % y el 35 %, manteniendo la misma precisión en la estimación de variables productivas. Es importante señalar que [P79] (Miranda et al., 2018) empleó el Índice de Vegetación de Razón (RVI, Ratio Vegetation Index) como variable de estratificación, no el NDVI, aunque ambos índices capturan dimensiones similares del vigor vegetativo.

**Aplicabilidad al presente caso:** Este método no aplica directamente porque requiere resolución submétrica (0.25 m) para discriminar árboles individuales y construir estratos intra-parcela. Sentinel-2, con su resolución de 10 m, no permite este nivel de detalle. Sin embargo, el principio general de estratificación por índices vegetativos sí es aplicable a escala de parcela completa, como se desarrolla en la siguiente sección.

### 3.3 Muestreo Estratificado con NDVI Satelital — Método Seleccionado para Parcelas

El método seleccionado para la selección de parcelas consiste en utilizar el NDVI medio derivado de imágenes satelitales para ordenar las parcelas por nivel de vigor y seleccionar los extremos (bajo y alto), maximizando así la representatividad de la muestra con solo 2 unidades. Esta decisión se sustenta en una cadena de evidencia bibliográfica que valida cada eslabón del razonamiento metodológico:

**Principio general de selección por cuantiles NDVI satelital.** [P82] (Meyers et al., 2020) desarrollaron el método NDVI3, que utiliza el NDVI de Landsat (resolución 30 m) para seleccionar puntos de muestreo en viñedos ubicados en los cuantiles de la distribución del índice (cola baja, media y alta). Los autores demostraron que 3 píxeles seleccionados estratégicamente alcanzan la misma representatividad que 20 puntos seleccionados aleatoriamente, estableciendo el principio de que la selección por cuantiles de NDVI satelital es estadísticamente eficiente.

**Validación del sensor Sentinel-2.** [P84] (Ortuani et al., 2024) compararon el rendimiento de Sentinel-2 (10 m) frente a imágenes de vehículo aéreo no tripulado (UAV) de resolución 3–4 cm para la delineación de zonas de manejo en viñedos. Los autores concluyeron que Sentinel-2 captura las principales zonas de vigor a nivel de parcela de manera comparable a UAV, validando que la resolución de 10 m es suficiente para caracterizar y estratificar unidades del tamaño de las parcelas de este estudio (0.5 ha).

**Aplicación a cultivos de cítricos.** [P85] (Moussaid et al., 2022) utilizaron el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de cítricos (mandarina Afourer) en Marruecos, demostrando que el índice captura de manera robusta la variabilidad de vigor entre parcelas de este cultivo. Este estudio proporciona respaldo directo para el uso del NDVI medio de Sentinel-2 en parcelas de mandarina.

**Eficiencia de la estratificación frente al azar.** [P91] (Arnó et al., 2017) demostraron que el muestreo estratificado por NDVI es significativamente más eficiente que el muestreo aleatorio simple en huertos frutales. Un hallazgo clave de su trabajo es que con solo 2 estratos se captura la mayor parte de la variabilidad entre parcelas, lo que respalda directamente la decisión de seleccionar solo 2 parcelas (una de cada extremo) en lugar de 3 o más.

**Delineación de zonas de manejo en cítricos.** [P92] (Longo-Minnolo et al., 2023) delinearon zonas de manejo en huertos de cítricos mediante NDVI utilizando el algoritmo K-means, con el objetivo de gestionar el estrés hídrico de manera diferenciada. Los autores confirmaron que las zonas de diferente vigor, definidas por niveles de NDVI, presentan diferencias estadísticamente significativas entre sí, validando que la división por niveles de vigor es metodológicamente sólida en cítricos.

**Predicción de rendimiento en mandarina con Sentinel-2.** [P90] (Ali & Imran, 2022) predijeron el rendimiento y los atributos bioquímicos de mandarina Kinnow (variedad genéticamente cercana a Murcott) utilizando índices de Sentinel-2, incluyendo el Sentinel-2 Red Edge Position (S2REP). Los autores reportaron coeficientes de determinación de R² = 0.86 para el área foliar (LAI) y R² = 0.80 para la clorofila, confirmando que Sentinel-2 captura la variabilidad intra-huerto en mandarinos y respaldando el uso de imágenes satelitales para estratificar parcelas de este cultivo.

### 3.4 Muestreo Sistemático Uniforme (SUR) — Método Seleccionado para Hileras

Para la selección de hileras dentro de cada parcela seleccionada, se adoptó el Muestreo Sistemático Uniforme (SUR, o Systematic Uniform Sampling). Este método consiste en seleccionar cada k-ésima unidad a partir de un arranque aleatorio, siendo particularmente adecuado para poblaciones con autocorrelación espacial, como las hileras de un huerto, donde unidades cercanas tienden a ser similares.

(Wulfsohn, 2010) estableció teóricamente que el SUR es superior al muestreo aleatorio simple para poblaciones con autocorrelación espacial positiva, ya que garantiza una distribución espacial uniforme de las unidades seleccionadas, cubriendo de manera más representativa el área total de la parcela. [P88] (Wulfsohn et al., 2012) validaron empíricamente este método en 14 huertos comerciales de kiwi, manzana y uva, reportando errores de estimación inferiores al 10 % en 11 de los 14 huertos evaluados. [P80] (Uribeetxebarria et al., 2018) citan este mismo resultado como respaldo para el uso de SUR en huertos frutales.

**Aplicación al presente caso:** Dentro de cada una de las 2 parcelas seleccionadas, se eligieron 3 hileras mediante SUR con arranque aleatorio = 3 e intervalo = 4, resultando en las hileras 3, 7 y 11 de un total de 13. Esta configuración asegura una distribución espacial equilibrada: la hilera 3 está cercana al borde de la parcela, la hilera 7 es central, y la hilera 11 está cercana al borde opuesto, capturando así la variabilidad potencial asociada a efectos de borde y a la heterogeneidad interna de la parcela.

### 3.5 Otros Métodos Considerados

Además de los métodos seleccionados, se evaluaron otras alternativas documentadas en la literatura, que fueron descartadas por no ajustarse a las condiciones y recursos disponibles en este estudio:

- **Ranked Set Sampling (RSS) con UAV.** [P81] (Martínez-Casasnovas et al., 2019) demostraron que el RSS con imágenes de UAV reduce el tamaño de muestra en un 50 %, pero este método requiere disponibilidad de un vehículo aéreo no tripulado y de imágenes de muy alta resolución, recursos no disponibles para esta investigación.
- **Análisis de costos del NDVI3.** [P83] (Meyers & Vanden Heuvel, 2024) cuantificaron la eficiencia económica del método NDVI3, demostrando una reducción del 90 % en el recorrido de muestreo respecto al muestreo aleatorio. Aunque este resultado refuerza la eficiencia del método, no aplica directamente al diseño del presente estudio, que prioriza la representatividad sobre la reducción de costos de tránsito.
- **Selección por criterios agronómicos.** [P89] (Mediterranean orchard assessment, 2024) propusieron seleccionar parcelas por criterios complementarios como edad, variedad y manejo. En el presente estudio, estas variables están controladas (4 parcelas de la misma variedad, edad y manejo), por lo que la estratificación por vigor mediante NDVI es la única fuente de variabilidad relevante para la selección.

## 4. Metodología

La metodología de selección de parcelas y hileras para el experimento A/B se estructura en 4 pasos secuenciales, cada uno justificado por el respaldo bibliográfico presentado en el estado del arte.

### Paso 1: Selección de Parcelas por NDVI Medio de Sentinel-2

Se extrajo el valor medio de NDVI de cada una de las 4 parcelas a partir de imágenes Sentinel-2 (banda 10 m, ~49 píxeles por parcela). Los valores de NDVI medio se ordenaron de menor a mayor, representando un gradiente de vigor vegetativo. Se seleccionaron 2 parcelas: una ubicada en el extremo inferior de la distribución (menor NDVI, menor vigor) y una en el extremo superior (mayor NDVI, mayor vigor).

Esta decisión sigue el principio de selección por cuantiles NDVI satelital validado por [P82] (Meyers et al., 2020), quienes demostraron que la selección de puntos en las colas de la distribución del índice alcanza la misma representatividad que un número considerablemente mayor de puntos aleatorios. El uso de Sentinel-2 a 10 m está respaldado por [P84] (Ortuani et al., 2024), quienes confirmaron que este sensor captura las principales zonas de vigor a nivel de parcela. La aplicación específica a parcelas de cítricos está validada por [P85] (Moussaid et al., 2022), quienes emplearon el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de mandarina.

La eficiencia de la estratificación por NDVI frente al muestreo aleatorio simple está respaldada por [P91] (Arnó et al., 2017), quienes demostraron que con solo 2 estratos se captura la mayor parte de la variabilidad del huerto. En cítricos específicamente, [P92] (Longo-Minnolo et al., 2023) validaron que la división por niveles de NDVI genera zonas de manejo con diferencias estadísticamente significativas entre sí. Adicionalmente, [P90] (Ali & Imran, 2022) confirmaron que Sentinel-2 captura la variabilidad intra-huerto en mandarina Kinnow con alta correlación (R² = 0.86 para LAI), respaldando el uso de imágenes satelitales para estratificar parcelas de mandarinos.

### Paso 2: Selección de Hileras mediante SUR Sistemático

Dentro de cada una de las 2 parcelas seleccionadas, se eligieron 3 hileras mediante muestreo sistemático uniforme (SUR) con arranque aleatorio. El arranque se fijó en la hilera 3 y el intervalo de selección en 4 hileras, resultando en las hileras 3, 7 y 11 de un total de 13.

Este método fue validado empíricamente por [P88] (Wulfsohn et al., 2012), quienes reportaron errores de estimación inferiores al 10 % en 11 de 14 huertos comerciales evaluados. (Wulfsohn, 2010) demostró teóricamente que el SUR es superior al muestreo aleatorio simple para poblaciones con autocorrelación espacial, característica presente en las hileras de un huerto, donde la proximidad espacial implica similitud en condiciones de vigor. La distribución resultante (hilera 3 cercana al borde, hilera 7 central, hilera 11 cercana al borde opuesto) asegura una cobertura espacial equilibrada de cada parcela.

### Paso 3: Caracterización de Parcelas con NDVI y NDRE

Las 2 parcelas seleccionadas se caracterizaron mediante los valores medios de NDVI y NDRE derivados de Sentinel-2, con el objetivo de documentar sus niveles de vigor y proporcionar contexto para la interpretación de los resultados del experimento A/B.

El **NDVI (10 m)** se utilizó como índice primario de caracterización, siguiendo la metodología de [P85] (Moussaid et al., 2022), quienes emplearon el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de cítricos. El **NDRE (20 m)** se incluyó como descriptor complementario, siguiendo la recomendación de [P90] (Ali & Imran, 2022), quienes demostraron que los índices de Red Edge son superiores al NDVI para estimar LAI (R² = 0.86) y clorofila (R² = 0.80) en mandarinos Kinnow.

Es fundamental destacar que **estos índices se utilizan exclusivamente para describir el vigor de las parcelas seleccionadas, no para su selección**. La selección se realizó sobre la base del NDVI (10 m, 49 píxeles por parcela), mientras que la resolución de 20 m del NDRE (12 píxeles por parcela) es insuficiente para una estratificación robusta entre parcelas.

### Paso 4: Captura de Video

La captura de video en las 6 unidades de muestreo (2 parcelas × 3 hileras) se realizó siguiendo el protocolo establecido en la fase P3 de esta investigación: velocidad de desplazamiento de aproximadamente 1 m/s, distancia al dosel de 0.8–1.5 m, ángulo de inclinación de la cámara de 15–30° hacia arriba, y bloqueo de autofoco (AF), autoexposición (AE) y balance de blancos (WB).

## 5. Discusión

### 5.1 Elección de NDVI sobre NDRE para la Selección de Parcelas

La decisión de utilizar NDVI en lugar de NDRE como variable de selección de parcelas se fundamenta en cuatro argumentos:

**Resolución espacial.** El NDVI de Sentinel-2 tiene una resolución de 10 m, lo que proporciona aproximadamente 49 píxeles por parcela de 0.5 ha. En contraste, el NDRE tiene una resolución de 20 m, resultando en solo 12 píxeles por parcela. Para una unidad de 0.5 ha, 49 píxeles proporcionan una estimación de la media del índice significativamente más robusta y con menor error estándar que 12 píxeles, reduciendo la incertidumbre asociada a la variabilidad intra-parcela del índice.

**Respaldo bibliográfico directo.** El principio de selección por cuantiles de NDVI satelital está validado específicamente por [P82] (Meyers et al., 2020), quienes demostraron la eficiencia de este enfoque en viñedos con Landsat. No existe en la literatura revisada un estudio equivalente que valide la selección de parcelas por cuantiles de NDRE satelital. Además, [P91] (Arnó et al., 2017) y [P92] (Longo-Minnolo et al., 2023) respaldan específicamente la estratificación por NDVI en huertos frutales y cítricos, respectivamente, no por NDRE.

**Tradición metodológica.** La literatura de muestreo estratificado con índices vegetativos en huertos frutales ha empleado consistentemente el NDVI como variable auxiliar. [P79] (Miranda et al., 2018), [P80] (Uribeetxebarria et al., 2018), [P82] (Meyers et al., 2020) y [P91] (Arnó et al., 2017) utilizaron NDVI (o RVI, en el caso de [P79]) para la estratificación, estableciendo una tradición metodológica que respalda la comparabilidad y la reproducibilidad del presente estudio.

**Correlación con vigor en cítricos.** [P93] (Ampatzidis & Partel, 2019) demostraron que el NDVI correlaciona significativamente con el tamaño de copa y la sanidad en cítricos, utilizando técnicas de aprendizaje profundo con redes neuronales convolucionales (DL-CNN) para el fenotipado de árboles. Este hallazgo refuerza la idoneidad del NDVI como proxy de vigor en el cultivo objeto de estudio.

### 5.2 Limitaciones de la Metodología

La metodología propuesta presenta las siguientes limitaciones, que deben considerarse al interpretar los resultados del experimento A/B:

**Número reducido de parcelas.** El hecho de contar con solo 4 parcelas disponibles constituye una restricción importante del tamaño de muestra a nivel de parcela. Sin embargo, esta limitación se mitiga mediante la estratificación por NDVI, que maximiza la variabilidad capturada con solo 2 unidades seleccionadas. [P91] (Arnó et al., 2017) demostraron que 2 estratos capturan la mayor parte de la variabilidad, lo que justifica metodológicamente que 2 parcelas extremas sean más informativas que 2 parcelas aleatorias.

**Imposibilidad de resolver hileras con Sentinel-2.** La resolución espacial de Sentinel-2 (10 m para NDVI, 20 m para NDRE) no permite discriminar hileras individuales (~5.4 m de ancho). Esta limitación física del sensor impide una estratificación directa a nivel de hilera y motiva el uso del SUR como método alternativo para la selección intra-parcela. [P88] (Wulfsohn et al., 2012) proporcionan respaldo empírico sólido para esta alternativa.

**Selección de solo 2 parcelas.** La decisión de capturar solo 2 parcelas (una de bajo vigor y una de alto vigor) sacrifica la cobertura espacial del huerto en favor de la representatividad de los extremos de la distribución de vigor. Si el objetivo fuera caracterizar la producción promedio del huerto, 3 parcelas (baja, media, alta) serían preferibles. Sin embargo, para el objetivo específico de esta investigación —evaluar la robustez del protocolo de captura en condiciones extremas de vigor—, la selección de 2 parcelas extremas es metodológicamente adecuada y más eficiente en términos de tiempo de campo (~30 min vs. ~45 min).

**Variedad única.** Las 4 parcelas disponibles corresponden a una única variedad (Murcott), por lo que los resultados del experimento A/B no son directamente generalizables a otras variedades de mandarina o cítricos. No obstante, [P90] (Ali & Imran, 2022) trabajaron con mandarina Kinnow, una variedad genéticamente cercana, lo que proporciona cierto respaldo para la extrapolación a mandarinas en general.

## 6. Conclusión

La selección de parcelas y hileras para el experimento A/B de captura de video en huerto de mandarinas se realizó mediante una metodología de muestreo estratificado por NDVI satelital a nivel de parcela y muestreo sistemático uniforme (SUR) a nivel de hilera, ambos respaldados por evidencia bibliográfica específica en huertos frutales y cultivos de cítricos.

La decisión final se resume en la siguiente tabla:

| Elemento | Decisión | Método | Respaldo Bibliográfico |
|---|---|---|---|
| **Selección de parcelas** | 2 parcelas: una de menor NDVI + una de mayor NDVI | Estratificación por NDVI medio de Sentinel-2 (extremos) | [P82] (Meyers et al., 2020) — selección por cuantiles NDVI satelital; [P84] (Ortuani et al., 2024) — S2 captura vigor a nivel parcela; [P85] (Moussaid et al., 2022) — NDVI medio S2 en cítricos; [P91] (Arnó et al., 2017) — estratificación > aleatorio en huertos; [P92] (Longo-Minnolo et al., 2023) — zonas de manejo cítricos con NDVI; [P90] (Ali & Imran, 2022) — variabilidad mandarina con S2 |
| **Selección de hileras** | 3 hileras por parcela: 3, 7, 11 | SUR sistemático con arranque aleatorio | (Wulfsohn, 2010) — SUR superior a SRS para autocorrelación espacial; [P88] (Wulfsohn et al., 2012) — error < 10 % en 11/14 huertos |
| **Caracterización de parcelas** | NDVI medio (primario) + NDRE medio (complementario) | Índices de Sentinel-2 | [P85] (Moussaid et al., 2022) — NDVI en cítricos; [P90] (Ali & Imran, 2022) — NDRE superior para LAI/clorofila en mandarinos |
| **Total de videos** | 6 videos | 2 parcelas × 3 hileras | — |
| **Tiempo estimado de captura** | ~30 minutos | — | — |

El resultado final del proceso de selección es un conjunto de **6 videos** (2 parcelas × 3 hileras), con un tiempo estimado de captura en campo de aproximadamente **30 minutos**. Esta muestra, aunque reducida en número de parcelas, maximiza la representatividad de la variabilidad de vigor del huerto mediante la estratificación por NDVI y asegura una cobertura espacial equilibrada dentro de cada parcela mediante el SUR. La metodología descrita es reproducible y está completamente trazable a la literatura científica, cumpliendo con los principios de rigor metodológico establecidos en esta investigación.

## 7. Referencias

Ali, A., Imran, M., Ali, A. & Khan, M.A. (2022). Evaluating Sentinel-2 red edge through hyperspectral profiles for monitoring LAI & chlorophyll content of Kinnow Mandarin orchards. *Remote Sensing Applications: Society and Environment*, 26, 100719. https://doi.org/10.1016/j.rsase.2022.100719 [P90]

Ampatzidis, Y. & Partel, V. (2019). UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence. *Remote Sensing*, 11(4), 410. https://doi.org/10.3390/rs11040410 [P93]

Arnó, J., Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A. & Rosell-Polo, J.R. (2017). Comparing efficiency of different sampling schemes to estimate yield and quality parameters in fruit orchards. *Advances in Animal Biosciences*, 8(2), 471-476. https://doi.org/10.1017/S2040470017000978 [P91]

Cochran, W.G. (1977). *Sampling Techniques* (3rd ed.). John Wiley & Sons.

Longo-Minnolo, G., Consoli, S., Vanella, D., Pappalardo, S., Guarrera, S., Manetto, G. & Cerruto, E. (2023). Delineating Citrus Management Zones Using Spatial Interpolation and UAV-Based Multispectral Approaches. *Precision Agriculture*, 24(5), 1570-1592. [P92]

Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A., Arnó, J. & Rosell-Polo, J.R. (2019). Assessing Ranked Set Sampling and Ancillary Data to Improve Fruit Load Estimates in Peach Orchards. *Computers and Electronics in Agriculture*. https://doi.org/10.1016/j.compag.2019.104931 [P81]

Meyers, J.M., Dokoozlian, N., Ryan, C., Bioni, C. & Vanden Heuvel, J.E. (2020). A New, Satellite NDVI-Based Sampling Protocol for Grape Maturation Monitoring. *Remote Sensing*, 12(7), 1159. https://doi.org/10.3390/rs12071159 [P82]

Meyers, J.M. & Vanden Heuvel, J.E. (2024). Spatial Sampling of Fruit Maturity Reduces Sampling Costs for Winegrapes in California and New York. *American Journal of Enology and Viticulture*. https://doi.org/10.5344/ajev.2024.23067 [P83]

Miranda, C., Santesteban, L.G., Urrestarazu, J., Loidi, M. & Royo, J.B. (2018). Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards. *Agriculture*, 8(6), 78. https://doi.org/10.3390/agriculture8060078 [P79]

Moussaid, A., El Fkihi, S., Zennayi, Y., Lahlou, O., Kassou, I., Bourzeix, F., El Mansouri, L. & Imani, Y. (2022). Machine Learning Applied to Tree Crop Yield Prediction Using Field Data and Satellite Imagery: A Case Study in a Citrus Orchard. *Informatics*, 9(3), 80. https://doi.org/10.3390/informatics9040080 [P85]

Ortuani, B., Mayer, A., Bianchi, D., Sona, G., Crema, A., Modina, D., Bolognini, M., Brancadoro, L., Boschetti, M. & Facchi, A. (2024). Effectiveness of Management Zones Delineated from UAV and Sentinel-2 Data for Precision Viticulture Applications. *Remote Sensing*, 16(4), 635. https://doi.org/10.3390/rs16040635 [P84]

Uribeetxebarria, A., Martínez-Casasnovas, J.A., Escolà, A., Rosell-Polo, J.R. & Arnó, J. (2018). Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps: A Comparative Analysis to Improve Yield and Quality Estimates. *Precision Agriculture*, 19, 1031-1050. https://doi.org/10.1007/s11119-018-9619-9 [P80]

Wulfsohn, D. (2010). Sampling Techniques for Plants and Soil. *Landbauforschung Völkenrode, Special Issue 340*, 3-30.

Wulfsohn, D., Aravena, F., Potin, C., Zamora, I. & García-Fiñana, M. (2012). Multilevel Systematic Sampling to Estimate Total Fruit Number. *Precision Agriculture* (Springer). [P88]
