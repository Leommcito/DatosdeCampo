# Metodología de Captura Manual con Smartphone para Detección YOLO y Seguimiento MOT en Huertos Densos de Mandarinas

**Documento metodológico integrado**
*Tesis — Validación en campo: 05/06/2026*

---

## Capítulo 1: Marco Teórico

### 1.1 Objetivo General

El objetivo general de esta investigación es establecer un **protocolo de recolección de datos en campo** para grabar **videos manuales con smartphone** en **huertos densos de mandarinas**, asegurando que el material capturado sea óptimo para modelos de **detección YOLO** y **seguimiento MOT (Multiple Object Tracking)**.

El enfoque principal es **capturar el video de la forma más limpia posible desde el origen**, mitigando problemas físicos en el momento de la grabación (no en post-procesamiento computacional). La prioridad es contar con **respaldo bibliográfico** para cada decisión de captura, produciendo un dataset de video de alta calidad para modelos YOLO + MOT en un contexto de huerto de mandarinas denso, caracterizado por alta oclusión, follaje denso y frutos pequeños.

### 1.2 Problemas a Mitigar Durante la Captura Manual

La captura manual con smartphone en huertos densos presenta 18 problemas identificados, clasificados por nivel de riesgo:

| Problema | Riesgo |
|---|---|
| Movimiento brusco de cámara (shake) | Muy Alto |
| Desenfoque por movimiento (motion blur) | Muy Alto |
| Cambios de altura/distancia al dosel | Muy Alto |
| Cambios de ángulo e inclinación | Muy Alto |
| Objetivo fuera del encuadre | Alto |
| Oclusiones (personas, ramas, vehículos) | Alto |
| Variaciones de iluminación (nubes, sombras) | Alto |
| Autofoco inestable (focus hunting) | Alto |
| Exposición incorrecta | Alto |
| Velocidad inconsistente de movimiento | Medio |
| Rotación de cámara (roll) | Medio |
| Cambios de zoom digital | Medio |
| Compresión excesiva del dispositivo | Medio |
| Diferencias entre dispositivos | Medio-Bajo |
| Distorsión de lente (gran angular) | Bajo |
| Reflejos/flare solar | Bajo |
| Ruido digital (poca luz) | Bajo |
| Variaciones de balance de blancos (AWB) | Bajo |

### 1.3 Preguntas de Investigación

La investigación se organiza en torno a tres preguntas fundamentales, cada una abordada en un sub-capítulo metodológico:

**Pregunta 1 (P1) — Software de Captura y Bloqueo de Sensores.** Investigar por qué la cámara nativa en modo automático es perjudicial para datasets de visión computacional en agricultura, evaluando aplicaciones como Open Camera y Filmic Pro para el bloqueo de autofoco (AF), exposición (ISO/shutter) y balance de blancos (AWB). Se requiere respaldo bibliográfico que demuestre que el focus hunting, la autoexposición y el AWB automático degradan la calidad de los datasets para detección y tracking.

**Pregunta 2 (P2) — Registro de Telemetría (IMU) en Tiempo Real.** Evaluar la necesidad de ejecutar aplicaciones como Sensor Logger en segundo plano durante la caminata por el huerto para registrar giroscopio (velocidad angular en X, Y, Z), acelerómetro (aceleración lineal) y magnetómetro (orientación). El propósito es capturar la firma del movimiento humano para su uso en post-producción (deblurring, estabilización, corrección de rolling shutter).

**Pregunta 3 (P3) — Diseño del Protocolo de Caminata y Captura.** Definir metodologías documentadas sobre cómo debe caminar el operador: distancia recomendada hacia el dosel, ángulo de inclinación de la cámara, velocidad de desplazamiento, horarios óptimos de grabación, trayectoria y estrategia para evitar doble conteo.

Adicionalmente, la **Pregunta 4 (P4)** aborda la selección de parcelas para el muestreo en campo, garantizando la representatividad del diseño experimental.

### 1.4 Principios Rectores

La presente investigación se rige por cinco principios rectores establecidos en la constitución del proyecto, que garantizan el rigor metodológico y la trazabilidad de cada decisión técnica:

**Principio I — Rigor Bibliográfico.** Cada decisión de captura debe estar respaldada por evidencia bibliográfica cuantitativa siempre que sea posible. Las decisiones basadas en ingeniería o sentido práctico deben documentarse explícitamente como tales.

**Principio II — Trazabilidad.** Cada decisión técnica está vinculada a un identificador único de referencia (sistema [PXX] en los archivos de trabajo, convertido a formato APA en el presente documento). La cadena de trazabilidad es: Decisión → Referencia → DOI/URL → Verificable.

**Principio III — Reproducibilidad.** El protocolo debe ser reproducible por cualquier investigador con un dispositivo Android compatible con Camera2 API. Todas las aplicaciones, configuraciones y procedimientos deben documentarse explícitamente.

**Principio IV — Transparencia ante Contradicciones.** La evidencia contradictoria o que matice las recomendaciones originales debe documentarse explícitamente, no ocultarse. Cada parámetro del protocolo incluye tanto el respaldo original como la evidencia contradictoria encontrada.

**Principio V — Preservación del Contenido.** La fusión de investigaciones en este documento preserva el 100% del contenido de los archivos fuente. No se inventa ni se omite información. Las anotaciones y matices se conservan como notas al pie.

### 1.5 Stack Tecnológico Objetivo

El stack tecnológico definido para el proyecto abarca desde la captura hasta el entrenamiento:

- **Captura:** Smartphone Android con app de cámara profesional (Open Camera con Camera2 API)
- **Telemetría:** Sensor Logger (IMU: giroscopio + acelerómetro a 100 Hz)
- **Estabilización:** Gyroflow (post-procesamiento con datos IMU)
- **Detección:** YOLO (v9, v11 o variantes)
- **Seguimiento:** ByteTrack / AgriSORT / OC-SORT / CoTracker3
- **Post-procesamiento:** Deblurring (NAFNet, DeblurGAN-v2, AGG-DeblurGAN), SLAM (iSAM2), Bundle Adjustment
- **Estimación de rendimiento:** Reconstrucción 3D multiframe + factor-graph optimization

### 1.6 Sistema de Trazabilidad

Cada decisión técnica en este documento sigue la cadena de trazabilidad establecida por el Principio II. En los archivos de investigación fuente, las referencias se identifican con códigos [PXX]; en el presente documento, dichos códigos han sido convertidos al formato APA (Autor, Año). La correspondencia entre ambos sistemas se preserva en el Apéndice de Trazabilidad al final del documento.

**Ejemplo de trazabilidad:**
```
Decisión: AE Lock (exposición fija)
  → ("Phenotyping Manual vs Auto", 2018) — Phenotyping
    → MSE 1.57 manual vs 4.26 auto
    → Manual es 2.7x más consistente que automático
```

---

## Capítulo 2: Estado del Arte

### 2.1 Software de Captura en Agricultura

La literatura académica en agricultura de precisión utiliza ampliamente smartphones para la captura de imágenes y video, pero existe una carencia sistemática en la documentación de las herramientas y configuraciones de captura empleadas.

#### 2.1.1 Hallazgos de la revisión bibliográfica (Elicit)

La revisión sistemática mediante Elicit arrojó 16 papers sobre captura agrícola con smartphone, ninguno de los cuales documenta adecuadamente la configuración de captura:

- (Janowski et al., 2021) utilizaron smartphones con GNSS para conteo de manzanas, mencionando solo "smartphones with required image-acquisition accuracy" sin especificar configuración.
- (Vélez et al., 2024) emplearon iPhone X y Xiaomi Poco X3 Pro en viñedos, tomando "high-resolution images of individual plants; geotagged data" sin detallar app ni configuración.
- (Zhao et al., 2023) usaron cámaras multi-lente de smartphone con método virtual focal para fenotipado de manzanas, documentando el método de calibración pero no la app de captura.
- (Jaramillo et al., 2025) capturaron "videos of the ground under vine rows on a sunny day" con configuración simple no documentada.
- (Zhou et al., 2020) desarrollaron una app propia (KiwiDetector) para detección de kiwi en Huawei P20, pero no utilizaron apps comerciales como Open Camera.

**Conclusión de Elicit:** Ningún paper agrícola documenta el uso de apps de captura comerciales (Open Camera, Filmic Pro, MCPro24fps) ni justifica la elección de configuración de cámara.

#### 2.1.2 Evidencia complementaria (Semantic Scholar)

La búsqueda en Semantic Scholar identificó papers que, aunque no documentan apps específicas, proporcionan evidencia relevante sobre la necesidad de controlar los parámetros de captura:

**Medición de humedad en arroz con smartphone** ("Rice GMC", 2021). Utilizaron un iPhone 8 con ISO=25 fijo, shutter=1/400s, f/1.8, distancia 27.5 cm, formato JPEG 4032×3024 px, aspecto 4:3, sin luz solar directa y con tabla de calibración de color Spyder Checkr 24. El dato clave es su justificación explícita: *"To minimize lighting-related factors, the smartphone camera parameters were fixed"* — constituyendo una de las pocas justificaciones explícitas en la literatura para fijar parámetros de cámara.

**Monitoreo de café con smartphone y sensores inerciales** (Sensors, 2020). Emplearon un Samsung Galaxy S5 SM-G900M en Full-HD 1920×1080, 30 fps, flash apagado, WB e ISO en automático, EV=0, con un holder con botones para enfoque y ángulo de 11.3°. Usaron sensores inerciales para detectar movimiento y medir blur, desarrollando una app Android propia. Es relevante porque integra IMU + cámara, aunque utilizaron modo automático.

**Detección de manzanas con YOLO en smartphone** (2024). Usaron un Redmi Note 7 a distancia 0.3-1.5 m, probando 5 condiciones de luz (directa, lateral, difusa, contraluz, baja luz) con una app Android que ejecutaba YOLOv8n localmente.

**Dataset de cacao con 5 smartphones** (Restrepo-Arias et al., 2023). Utilizaron Samsung Galaxy A01, Samsung Galaxy Note 10, iPhone SE 2020, Motorola G9 plus y LG G5 en horario 8:00-16:00, con trayectoria zigzag entre árboles, aspecto 1:1 y resize a 3000×3000 px.

#### 2.1.3 Evidencia cuantitativa sobre la necesidad de control manual

La revisión bibliográfica identificó 14 papers con evidencia cuantitativa que respalda la necesidad de fijar parámetros de captura:

| Problema | Evidencia | Fuente |
|---|---|---|
| Auto-exposure causa inconsistencia | 85% más variación HSV con auto vs LED fijo | (Choi et al., 2021) |
| Auto-exposure falla en alto rango dinámico | Primer plano oscuro al exponer para cielo | (Choi et al., 2021) |
| Manual supera a automático | MSE 1.57 vs 4.26 (manual 2.7x más consistente) | ("Phenotyping Manual vs Auto", 2018) |
| Parámetros fijos reducen datos necesarios | 4x menos datos de entrenamiento | ("Illumination-Invariant", 2021) |
| Exposición inconsistente degrada CNN | Redes no generalizan con exposición variable | ("Stanford CNN + Exposure", 2018) |
| Focus hunting degrada calidad | Lente oscila, FoV cambia | ("Focus Hunting CVPR", 2025) |
| Camera2 API necesario para control científico | Tone mapping irreversible. 74% menor MAE con lineal | ("Camera2 API", 2023) |
| Luz no controlada destruye detección | F1 0.82 → 0.13 con glare | ("Kiwifruit glare", 2020) |
| ISP automático degrada detección YOLO | Contraste/gamma/saturación causan falsos negativos | ("ISP Tuning", 2023) |
| Parámetros auto causan fluctuación | 13-14% fluctuación en detección en escenas estáticas | ("Unintentional Adversary ECCV", 2022) |
| ISP pipeline pierde información útil | 7.1% más precisión entrenando en RAW vs ISP-processed | ("ISP-less CV", 2022) |
| ISP default es sub-óptimo para detección | 28% mejora con AdaptiveISP vs ISP default | ("AdaptiveISP", 2024) |

**Papers críticos en detalle:**

**Paper LED + exposición fija** (Choi et al., 2021). Demostró que la iluminación LED controlada con exposición fija reduce la variación HSV en un **85%** frente a la auto-exposición. El error de motion blur se redujo de 7 mm a 1 mm a 7 km/h con flash sincronizado. La auto-exposición falló catastróficamente cuando el sol estaba frontal a la cámara. Conclusión: los parámetros fijos más iluminación controlada eliminan casi toda la variabilidad.

**Phenotyping — Manual vs Auto** ("Phenotyping Manual vs Auto", 2018). Comparó directamente exposición manual vs automática en condiciones de campo cambiantes. El error cuadrático medio fue de **1.57 (manual) vs 4.26 (auto)**, demostrando que la exposición manual es **2.7x más consistente** que la automática.

**Illumination-Invariant Camera System** ("Illumination-Invariant Camera System", 2021). Demostró que las redes entrenadas con imágenes consistentes requieren **4x menos datos** para alcanzar el mismo rendimiento. El Average Precision en condiciones de luz extrema fue de 0.71 con iluminación controlada frente a **casi 0** con luz natural.

**Camera2 API para investigación** ("Camera2 API", 2023). Estableció que el tone mapping automático aplica transformaciones **no lineales irreversibles** que *"cannot be reversed in post processing"*. La Camera2 API de Android permite configurar tone mapping lineal, logrando un **74% menor MAE** frente al modo automático por defecto. iOS no ofrece control equivalente sobre el tone mapping en video.

**Impacto del ISP en detección** ("ISP Tuning", 2023). Demostró que el contraste, gamma y saturación del pipeline ISP automático causan **degradación significativa** en YOLOv5/v8, Faster R-CNN y RT-DETR. Los objetos pequeños son los más afectados, y la mayoría de los errores introducidos son **falsos negativos**.

**La cámara como "unintentional adversary"** ("Unintentional Adversary ECCV", 2022). Demostró que los cambios automáticos de parámetros de cámara causan un **13-14% de fluctuación** en el conteo de detecciones sobre escenas estáticas. El modelo original YOLOv5 generó **157 track-IDs** frente a 94 con transfer-learning (**40.1% menos errores** en tracking).

**Detección en RAW** ("ISP-less CV", 2022). Confirmó que entrenar modelos en dominio RAW supera en **7.1% de precisión** a las imágenes procesadas por el pipeline ISP, demostrando que el ISP automático pierde información útil para detección.

**AdaptiveISP** ("AdaptiveISP", 2024). Estableció que el pipeline ISP puede optimizarse específicamente para detección, logrando un **28% mejor mAP** (71.4 vs 55.6) al adaptar el procesamiento a la tarea de visión computacional, confirmando que el ISP por defecto es sub-óptimo.

### 2.2 IMU y Estabilización en Video Agrícola

#### 2.2.1 Estabilización con IMU

La literatura sobre estabilización de video basada en sensores inerciales (IMU) proporciona respaldo cuantitativo para el uso de giroscopio y acelerómetro en la corrección de movimiento durante la captura:

(Han et al., 2021) reportaron una **mejora del 32%** en estabilización mediante fusión de giroscopio y visión, con una latencia de 32.6 ms, probado en condiciones de caminata. (Li et al., 2025) alcanzaron un **47.8% de mejora en SSIM** y 37% más rapidez combinando giroscopio, clustering y profundidad relativa.

En cuanto a corrección de rolling shutter con IMU, (Zhang & Zhang, 2023) demostraron que la IMU de alta frecuencia en teléfonos Android supera al estado del arte en precisión y costo computacional.

#### 2.2.2 Frecuencia de muestreo IMU

(Fan et al., 2025) resolvieron la pregunta de frecuencia de muestreo óptima para aplicaciones agrícolas: **100 Hz es suficiente** para walking (1.2 m/s), mientras que frecuencias superiores a 100 Hz no mejoran la precisión en orientación. Para running (2.2 m/s) se requieren 200 Hz, y el acelerómetro por encima de 100 Hz **degrada la precisión** al introducir error por aceleraciones distorsionadas.

Esta frecuencia ha sido validada por múltiples estudios de análisis de marcha con smartphone, que confirman que el IMU del smartphone a 100 Hz es válido con ICC > 0.8 frente a gold-standard.

#### 2.2.3 Evidencia sobre OIS y estabilización

**DeepOIS** ("DeepOIS", 2021) demostró que el OIS (Optical Image Stabilization) interfiere con la estabilización basada en giroscopio: el error de alineación es de **0.688 sin OIS** frente a **1.038 con OIS (50% peor)**. La conclusión textual establece que *"OIS terminates the possibility of image registration by gyros"*.

**ISPRS** ("ISPRS IS", 2022) corroboró desde la fotogrametría que la estabilización integrada degrada la precisión: la incertidumbre en los parámetros es **hasta 300% mayor** y el error de reproyección **4x mayor** con la estabilización activada.

**Video estabilizado vs fotos estáticas.** ("MangoYOLO", 2019) demostraron que la detección con video en movimiento alcanzó el **62.3%** del conteo real de cosecha, frente a solo el **40.2%** con foto estática, una **mejora absoluta del +22%**.

**Impacto del motion blur en YOLO.** ("Citrus GAN", 2025) reportaron que el **mAP@0.5:0.95 mejora un 86.4%** tras restaurar imágenes borrosas de cítricos, con incrementos del +76.9% en recall, +40.1% en F1 y reducción del -63.9% en falsos negativos. Es importante señalar que esta cifra representa una mejora relativa, y la degradación real por blur se sitúa en el rango del 15-50% según el modelo YOLO utilizado.

**Estabilización en agricultura.** ("Crop Row Stabilization", s.f.) reportaron que la estabilización de video en hileras de cultivo suprimió el **66%** del desplazamiento lateral, reduciendo la desviación promedio de 93 a aproximadamente 20 píxeles.

### 2.3 Protocolos de Captura en Campo

La literatura sobre protocolos de captura en agricultura se organiza en torno a seis parámetros fundamentales. A continuación se presentan las evidencias recopiladas para cada uno.

#### 2.3.1 Velocidad de Caminata

| Paper | Velocidad | Contexto | Resultado |
|---|---|---|---|
| (Roy et al., 2018) | **2 m/s (7.2 km/h)** | Samsung Galaxy S4, video 30fps, 1920×1080, tractor | Yield accuracy 95.56-97.83% |
| ("MangoYOLO", 2019) | **5 km/h (~1.39 m/s)** | Vehículo a 10 fps, 2 m de distancia | 62% harvest count, RMSE 18.0 frutos/árbol |
| ("Apple 3D Camera", 2023) | **0.052/0.069/0.098 m/s** | Tractor con cámara 3D, 3 ángulos | Counting accuracy 86.6% |
| (Ramos Giraldo et al., 2017) | **~3 cm/s** | Smartphone + IMU para detección de blur | Máx 5 cm/s para evitar blur |
| ("FEGW-YOLO", 2026) | Efecto del blur | Cuantifica caída de mAP por motion blur | mAP cae 27% por blur |

#### 2.3.2 Ángulo de Cámara

(Hemming et al., 2014) realizaron el estudio más completo, probando **14 posiciones de cámara** en pimiento dulce con diferentes ángulos azimuth y zenith para medir la Fruit Detectability (FD). El ángulo **zenith 60° (30° hacia arriba)** dio la mejor FD como posición única (FD máxima 66%), mientras que la combinación de 5 posiciones alcanzó un FD del 90%. El ángulo zenith 120° (mirando hacia abajo) fue el peor, ya que las hojas ocultan los frutos.

("Apple 3D Camera", 2023) probaron ángulos de 0°, 15° y 30° en manzanas con cámara 3D, encontrando que **15°** proporcionó el menor RMSE (1.54 cm). (Wang et al., 2018) establecieron un límite de **<14°** de inclinación para la app FruitSize, por encima del cual el error de tamaño supera el 6%.

#### 2.3.3 Distancia al Dosel

| Paper | Distancia probada | Resultado |
|---|---|---|
| ("Orchard-YOLO", 2026) | **0.8-1.5 m** (rango óptimo) | mAP 93.69% |
| ("RGB-D Sensors", 2020) | **1.5 m vs 2.5 m** | 1.5 m: 200.5% más densidad de nube de puntos |
| (Kuznetsova et al., 2020) | **0.2 / 0.5 / 1.0 / 2.0 m** | Distancia óptima depende del FOV |
| (Zhou et al., 2020) | **~1 m** (selfie stick) | TDR 90.8% |
| ("Apple detection Redmi Note 7", 2025) | **0.3-1.5 m** | Bueno para detección, 5 condiciones de luz |

#### 2.3.4 Horario e Iluminación

| Paper | Condiciones comparadas | Mejor condición | Resultado |
|---|---|---|---|
| ("Orchard-YOLO", 2026) | ±50% brillo + hasta 70% oclusión | Normal: 94.8% mAP. Extrema: 61.4% |
| (Li et al., 2023) | 4 horarios: 7-8AM, 10-11AM, 2-3PM, 6-7PM | Múltiples horarios viables |
| (Restrepo-Arias et al., 2023) | 8AM-4PM, trayectoria zigzag | Rango completo usable |
| ("Kiwifruit glare", 2020) | Normal vs glare vs overexposed | Normal: F1 0.82. Glare: F1 0.13 |

#### 2.3.5 Motion Blur y Shutter Speed

("Motion Blur Review", 2024) proporcionaron la revisión más completa, incluyendo la fórmula de desplazamiento por blur: `desplazamiento (px) ≈ (velocidad_caminata × tiempo_exposición) / distancia_focal`. ("FEGW-YOLO", 2026) cuantificaron que el **mAP@0.5 cae un 27.2%** (de 0.925 a 0.673) por motion blur en huerto de cítricos.

#### 2.3.6 Anti-Doble Conteo y Tracking

(Gené-Mola et al., 2023) compararon SORT, DeepSORT y ByteTrack para conteo de frutos en video, encontrando que ByteTrack ofrece el mejor rendimiento: **MOTA 0.682, IDF1 0.837, HOTA 0.689**, con 15 ms/frame frente a los 128 ms de DeepSORT. ("MangoYOLO", 2019) demostraron que el tracking con Kalman Filter + Hungarian Algorithm alcanzó el **62%** del conteo de cosecha frente al 40% con foto dual estática.

### 2.4 Selección de Parcelas y Muestreo en Huertos Frutales

La selección de unidades de muestreo en huertos frutales requiere métodos estadísticos que maximicen la representatividad con el mínimo esfuerzo de campo. La literatura ofrece diversas estrategias documentadas.

#### 2.4.1 Muestreo Aleatorio Simple (MAS/SRS)

El Muestreo Aleatorio Simple constituye el diseño de muestreo más fundamental, donde cada unidad tiene la misma probabilidad de ser seleccionada. (Miranda et al., 2018) y (Uribeetxebarria et al., 2018) lo utilizaron como línea base para comparar la eficiencia de métodos más complejos en huertos frutales. Sin embargo, con solo 4 parcelas disponibles, la selección aleatoria podría resultar en unidades con vigor muy similar, perdiendo la representatividad de los extremos.

#### 2.4.2 Muestreo Estratificado con NDVI

(Miranda et al., 2018) y (Uribeetxebarria et al., 2018) aplicaron muestreo estratificado con NDVI en huertos de durazno utilizando imágenes aéreas de muy alta resolución (0.25 m), logrando reducciones del tamaño de muestra entre el 17% y el 35%. (Arnó et al., 2017) demostraron que la estratificación por NDVI es significativamente más eficiente que el muestreo aleatorio simple, y que con solo 2 estratos se captura la mayor parte de la variabilidad entre parcelas.

El método **NDVI3** desarrollado por (Meyers et al., 2020) demostró que 3 píxeles seleccionados estratégicamente en las colas de la distribución del NDVI (cola baja, media y alta) alcanzan la misma representatividad que 20 puntos seleccionados aleatoriamente.

#### 2.4.3 Muestreo Sistemático Uniforme (SUR)

(Wulfsohn et al., 2012) validaron empíricamente el SUR en 14 huertos comerciales de kiwi, manzana y uva, reportando errores de estimación inferiores al 10% en 11 de los 14 huertos evaluados. Este método es particularmente adecuado para poblaciones con autocorrelación espacial, como las hileras de un huerto.

#### 2.4.4 Aplicación a cítricos con Sentinel-2

("Morocco citrus", 2022) utilizaron el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de cítricos (mandarina Afourer), demostrando que el índice captura robustamente la variabilidad de vigor entre parcelas. ("UAV vs Sentinel-2", 2024) compararon Sentinel-2 (10 m) frente a UAV (3-4 cm) para zonificación de vigor, concluyendo que Sentinel-2 captura las principales zonas de vigor a nivel de parcela de manera comparable al UAV. En mandarinos específicamente, (Sun et al., 2026) reportaron R² = 0.85 para la estimación de LAI con Sentinel-2.

### 2.5 Gap de Investigación Confirmado

El análisis bibliográfico realizado confirma que **no existe un paper agrícola que documente el flujo completo** (app de captura + configuración de cámara + registro IMU + pipeline de procesamiento) para detección de frutos en video con smartphone.

Los gaps específicos identificados son:

1. **Software de captura:** Solo 1 paper en toda la literatura ("Open Camera v1.52", 2024) documenta Open Camera v1.52 con configuración detallada. Ningún paper documenta el flujo completo app + configuración + IMU + pipeline para detección de frutos en video.
2. **IMU → YOLO mAP:** No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en métricas YOLO (mAP) o MOT (MOTA) para video agrícola.
3. **Parámetros combinados:** No existe un paper que compare la interacción de velocidad × ángulo × distancia combinados para captura manual con smartphone en agricultura, midiendo el impacto en mAP/MOTA.
4. **Selección de parcelas:** No existe un protocolo documentado que integre la selección de parcelas por NDVI satelital con un pipeline completo de captura para cítricos.

**Contribución original de esta investigación:** Documentar y medir cuantitativamente el impacto de todas estas decisiones en mAP/MOTA para video de mandarinas capturado con smartphone, comparando el protocolo propuesto frente a la cámara nativa en modo automático (experimento A/B).

---

## Capítulo 3: Metodología

### 3.1 Software de Captura y Bloqueo de Sensores (P1)

#### 3.1.1 Introducción y Fundamentación

El primer paso del pipeline de captura consiste en seleccionar y configurar la aplicación de cámara que permita el control manual de los parámetros de exposición, enfoque y balance de blancos. La literatura demuestra que la cámara nativa de los smartphones en modo automático introduce variabilidad perjudicial para la consistencia de los datasets de visión computacional.

La evidencia cuantitativa acumulada respalda sólidamente el control manual: la exposición fija reduce la variación HSV en un 85% (Choi et al., 2021), el modo manual es 2.7x más consistente que el automático en condiciones de campo ("Phenotyping Manual vs Auto", 2018), y las redes entrenadas con imágenes consistentes requieren 4x menos datos ("Illumination-Invariant", 2021).

#### 3.1.2 Análisis de Aplicaciones de Captura

Se evaluaron cuatro aplicaciones profesionales para smartphone:

| App | Precio | AF Lock | AE Lock | WB Lock | ISO manual | Shutter manual | Perfil Log | Control gimbal | Bitrate |
|---|---|---|---|---|---|---|---|---|---|
| **Open Camera** | **Gratis** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ Configurable |
| Filmic Pro | ~$5/semana | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ V-Log | ✅ DJI/Zhiyun | 100 Mbps |
| MCPro24fps | ~$20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Múltiples | ❌ | Hasta 500 Mbps |
| Blackmagic Cam | Gratis | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | Alto |

**Decisión fundamental: Open Camera es la aplicación seleccionada** por las siguientes razones:

1. **Costo $0** — cualquier investigador puede reproducir el protocolo sin barrera económica
2. **Control manual completo** vía Camera2 API (ISO, shutter, AF Lock, AE Lock, WB Lock, bitrate configurable)
3. **Open-source** (SourceForge) — el código puede ser citado y verificado
4. **Sin suscripción** — a diferencia de Filmic Pro (subió a ~$5/semana en 2022)
5. **Única app gratuita** que ofrece bloqueo simultáneo de AF, AE y WB

Open Camera permite el bloqueo de los tres parámetros críticos (AF Lock, AE Lock, WB Lock), el control manual de ISO y shutter speed, y la configuración del bitrate para calidad constante. Requiere soporte de Camera2 API, que no todos los dispositivos Android ofrecen.

#### 3.1.3 Evidencia Adicional (Papers P95-P99)

**ISP Tuning y Degradación de Detección** ("ISP Tuning", 2023). El procesamiento automático del ISP (Image Signal Processor) —específicamente contraste, gamma y saturación— causa degradación significativa en YOLOv5/v8, Faster R-CNN y RT-DETR. Los objetos pequeños son los más afectados, y la mayoría de los errores introducidos son falsos negativos. Esto es crítico para mandarinas en huerto denso.

**La Cámara como "Unintentional Adversary"** ("Unintentional Adversary ECCV", 2022). Los cambios automáticos de parámetros de cámara causan un 13-14% de fluctuación en detección incluso en escenas estáticas. El modelo original YOLOv5 generó 157 track-IDs frente a 94 con transfer-learning (40.1% menos errores en tracking). El simple hecho de usar modo automático introduce ruido en la medición.

**Detección en RAW supera a RGB procesado** ("ISP-less CV", 2022). Entrenar modelos en dominio RAW proporciona un 7.1% más de precisión que con imágenes procesadas por ISP. El pipeline ISP pierde información útil para detección debido a las distorsiones no lineales que introduce.

**ISP por defecto no es óptimo para detección** ("AdaptiveISP", 2024). AdaptiveISP logra un 28% mejor mAP (71.4 vs 55.6) al optimizar el pipeline ISP específicamente para detección. Incluso si el ISP automático produce imágenes "bonitas" para el ojo humano, no están optimizadas para YOLO.

#### 3.1.4 Tabla Resumen: Qué Hacer vs Qué Evitar

| ✅ Hacer (Recomendado) | ❌ Evitar (No recomendado) | Respaldo bibliográfico |
|---|---|---|
| Bloquear AE/AF/WB | Dejar parámetros en automático (causa fluctuación 13-14%) | (Choi et al., 2021); ("Phenotyping Manual vs Auto", 2018); ("Unintentional Adversary ECCV", 2022) |
| Fijar ISO en 200 (100 solo si hay suficiente luz) | ISO automático (varía entre frames, degrada consistencia) | ("Open Camera v1.52", 2024); ("Illumination-Invariant", 2021) |
| Fijar shutter en 1/100 s (rango 1/60-1/120) | Shutter automático (cambia exposición frame a frame) | ("Motion Blur Review", 2024); ("Open Camera v1.52", 2024) |
| Usar tone mapping lineal (Camera2 API) | Tone mapping automático (transformaciones no lineales irreversibles) | ("Camera2 API", 2023) |
| Usar Open Camera (gratis, open-source, Camera2 API) | App nativa del fabricante (no permite bloquear parámetros) | ("Open Camera v1.52", 2024) |
| Deshabilitar OIS si se usa Gyroflow | OIS activo con estabilización basada en giroscopio | ("DeepOIS", 2021); ("ISPRS IS", 2022) |
| Mantener distancia constante al dosel (0.5-1.5 m) | Cambiar distancia entre tomas (afecta resolución del fruto) | (Kuznetsova et al., 2020) |
| Procesar en RAW si es posible (7.1% más precisión) | Confiar en el ISP por defecto (pierde información útil) | ("ISP-less CV", 2022) |
| Optimizar ISP para detección (no para ojo humano) | Usar pipeline ISP default (sub-óptimo para YOLO, 28% menos mAP) | ("AdaptiveISP", 2024) |

#### 3.1.5 Discusión: Nuevo Paradigma de Detección Robusta (2024-2026)

Es importante reconocer que entre 2024 y 2026 han surgido detectores (Orchard-YOLO 2026, YOLO-PBGM 2025) que logran >94% mAP incluso con variaciones de iluminación de ±50%, mediante técnicas como data augmentation con exposición randomizada, mecanismos de atención (GAM, CBAM) y aprendizaje de features illumination-invariant.

Sin embargo, esto NO invalida el control de captura por las siguientes razones:

1. **Ambos paradigmas son complementarios:** Controlar la captura más entrenar modelos robustos debería dar el mejor resultado
2. **No hay experimento que compare:** Precisamente, el experimento A/B de esta tesis (Protocolo vs Cámara Nativa) es lo que falta en la literatura
3. **Escenario extremo:** El huerto denso de mandarinas (frutos pequeños, alta oclusión, follaje denso) es más desafiante que los escenarios donde se probaron esos modelos
4. **El ISP sigue siendo un problema:** Aunque el detector sea robusto a iluminación, el tone mapping, gamma y saturación del ISP automático siguen degradando la información ("ISP Tuning", 2023); ("Unintentional Adversary ECCV", 2022); ("ISP-less CV", 2022)

#### 3.1.6 Nota sobre los Valores Propuestos vs Documentados en Papers

Los valores específicos propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120 s) **no son valores extraídos directamente de un paper**, sino decisiones del protocolo basadas en el principio de "usar el valor mínimo práctico para condiciones de campo". Los papers consultados usaron valores distintos según sus condiciones específicas:

| Valor documentado en paper | Paper | Condiciones de ese paper |
|---|---|---|
| ISO=25, shutter=1/400 s | ("Rice GMC", 2021) | iPhone 8, laboratorio, tabla de calibración Spyder Checkr 24 |
| ISO=200, shutter=1/100 s | ("Open Camera v1.52", 2024) | Redmi Note 7 Pro, iluminación LED 4000K, 50 cm distancia |
| Exposición ~250 µs (~1/4000 s) | (Rançon et al., 2023) Vineyard | Cámara industrial Basler Ace, flash xenon sincronizado |
| Exposición 200 µs (~1/5000 s) | (Choi et al., 2021) LEDs | Cámara industrial con LED overcurrent-driven 6× |

El protocolo propone **ISO 100-200** porque ISO=200 está documentado como valor funcional en campo ("Open Camera v1.52", 2024), e ISO=100 es el mínimo práctico en exteriores sin llegar a ISO=25 (que requiere condiciones controladas de laboratorio).

El protocolo propone **shutter 1/60-1/120 s** porque 1/100 s está documentado, y el rango es un compromiso entre: (a) un shutter lo suficientemente rápido para evitar motion blur al caminar (~8-16 px a 1 m/s), y (b) un shutter lo suficientemente lento para capturar suficiente luz sin flash en exteriores.

> **Conclusión:** Los valores del protocolo son una decisión de ingeniería informada por la literatura, no un valor extraído directamente de un paper. El experimento A/B (Protocolo vs Cámara Nativa) validará si esta decisión es adecuada.

#### 3.1.7 Limitación: Protocolo Solo para Android

El presente protocolo de captura **solo es aplicable a dispositivos Android** que soporten Camera2 API. La razón es que iOS (AVFoundation) **no expone control sobre el tone mapping** de la cámara, según lo documentado por ("Camera2 API", 2023):

> *"It is only possible to manually set the camera tone mapping to linear within the Android Camera 2 API. Such an option is not available in iOS. Although it is possible to capture RAW photos using iOS AVFoundation, the RAW capture mode is not possible for video recordings necessary for cPPG measurements."*

Esto implica que:
- En **Android**: Se puede usar Camera2 API para configurar tone mapping lineal, bloquear AF/AE/WB y controlar ISO/shutter manualmente.
- En **iOS**: No es posible controlar el tone mapping en video. La cámara nativa de iOS aplica transformaciones no lineales irreversibles.

**Recomendación para iOS:** Bloquear AE/AF/WB si la app lo permite, usar la resolución más alta disponible y bitrate máximo. Los resultados del experimento A/B pueden no ser directamente transferibles entre plataformas.

#### 3.1.8 Gap Confirmado

> Solo 1 paper en toda la literatura ("Open Camera v1.52", 2024) documenta Open Camera v1.52 con configuración detallada. Ningún paper documenta el flujo completo (app + configuración + IMU + pipeline) para detección de frutos en video. Esta es la contribución original de esta investigación: documentar y medir cuantitativamente el impacto de estas decisiones en mAP/MOTA para video de mandarinas.

### 3.2 Registro de Telemetría IMU (P2)

#### 3.2.1 Introducción y Fundamentación

El segundo componente del pipeline consiste en registrar datos de sensores inerciales (IMU) durante la captura de video, específicamente giroscopio (velocidad angular en X, Y, Z) y acelerómetro (aceleración lineal), utilizando la aplicación Sensor Logger ejecutándose en segundo plano durante la caminata por el huerto.

El propósito de este registro es capturar la firma del movimiento humano para su uso en post-producción (estabilización Gyroflow, deblurring, corrección de rolling shutter).

#### 3.2.2 Evidencia sobre Estabilización con IMU

(Han et al., 2021) demostraron que la fusión de giroscopio y visión para estabilización logra una **mejora del 32%** sobre el estado del arte, con una latencia de 32.6 ms, probado en condiciones de caminata, escalada y paseo en vehículo. (Li et al., 2025) alcanzaron un **47.8% de mejora en SSIM** y 37% más rapidez combinando giroscopio, clustering y profundidad relativa.

#### 3.2.3 Frecuencia de Muestreo IMU

(Fan et al., 2025) establecieron que **100 Hz es suficiente** para aplicaciones de walking (1.2 m/s). Frecuencias superiores a 100 Hz no mejoran la precisión en orientación, y el acelerómetro por encima de 100 Hz degrada la precisión al introducir error por aceleraciones distorsionadas. Esta frecuencia ha sido validada por múltiples estudios de análisis de marcha con smartphone (ICC > 0.8 frente a gold-standard).

#### 3.2.4 OIS Debe Estar Desactivado

**DeepOIS** ("DeepOIS", 2021) demostró que el OIS interfiere con la estabilización basada en giroscopio: el error de alineación sin OIS es de 0.688 frente a 1.038 con OIS (50% peor). La conclusión textual establece: *"OIS terminates the possibility of image registration by gyros"*.

**ISPRS** ("ISPRS IS", 2022) corroboró desde la fotogrametría que la estabilización integrada debe desactivarse: la incertidumbre en parámetros es hasta 300% mayor y el error de reproyección 4x mayor con la estabilización activada.

#### 3.2.5 Evidencia Cuantitativa Adicional

**Video estabilizado vs fotos estáticas** ("MangoYOLO", 2019): La detección con video en movimiento alcanzó el 62.3% del conteo real de cosecha frente al 40.2% con foto estática (+22% de mejora absoluta).

**Motion blur + YOLO** ("Citrus GAN", 2025): El mAP@0.5:0.95 mejora un 86.4% tras restaurar imágenes borrosas de cítricos (recall +76.9%, F1 +40.1%). La degradación real por blur se sitúa en el rango del 15-50% según el modelo.

**Estabilización en agricultura** ("Crop Row Stabilization", s.f.): Supresión del 66% del desplazamiento lateral entre hileras, con desviación reducida de 93 a ~20 píxeles.

#### 3.2.6 Tabla Resumen de Evidencia — Paso 2

| Decisión | Respaldo | Tipo de fuente |
|---|---|---|
| Registrar IMU durante captura | Estabilización IMU supera a óptica en walking (32% mejor) | (Han et al., 2021) |
| 100 Hz es suficiente | Paper específico sobre sampling rate vs walking speed | (Fan et al., 2025) |
| Usar Gyroflow en post-procesamiento | Documentación oficial, 8.9k stars GitHub, plugins DaVinci/Adobe | Documentación técnica [D2][D5] |
| Usar Sensor Logger | Listado en docs de Gyroflow como fuente compatible | Documentación técnica [D3] |
| OIS debe estar desactivado | DeepOIS: 50% peor alineación. ISPRS: 300% más incertidumbre | ("DeepOIS", 2021); ("ISPRS IS", 2022) |
| IMU mejora rolling shutter | 3 papers con resultados cuantitativos | (Zhang & Zhang, 2023) |
| IMU mejora deblurring | 5% PSNR gain, 19% menos cómputo | (Arslan et al., 2024) |
| Video estabilizado vs fotos | MangoYOLO: +22% detección con video | ("MangoYOLO", 2019) |
| Motion blur + YOLO | Citrus GAN: 86.4% mAP de mejora tras deblurring | ("Citrus GAN", 2025) |
| Estabilización en agricultura | Crop row: 66% supresión desplazamiento | ("Crop Row Stabilization", s.f.) |

#### 3.2.7 Evidencia Contradictoria y Matices

**OIS Debe Estar OFF — Matiz importante.** La regla "OIS OFF" se matiza con evidencia de sistemas modernos: Qualcomm (US20200412954A1, 2024) combina OIS+EIS exitosamente usando sensores Hall para leer la posición del lente. El Google Pixel 2 demostró un sistema híbrido que fusiona datos del giroscopio con posición OIS mediante ML. HyperOIS ("HyperOIS", 2024) integró OIS avanzado con plataforma smartphone (SR -34.37 dB a -26.90 dB). Sin embargo, la regla "OIS OFF" se mantiene para este pipeline porque **Sensor Logger es una fuente externa** — no tenemos acceso a los sensores Hall del lente para compensar OIS.

**Frecuencia de 100 Hz — Suficiente pero con límites.** (Torun et al., 2021) encontraron que 100 Hz es inadecuado para parámetros espaciales de marcha (250 Hz óptimo). Sin embargo, esto no aplica a esta tesis porque no estimamos stride length ni velocidad, solo orientación para sincronización video-IMU.

**Motion Blur + YOLO — El 86.4% es engañoso.** El paper Citrus GAN reporta una mejora relativa del 86.4% tras deblurring. La degradación real por blur es de aproximadamente 15-50% según el modelo ("Orchard-YOLO", 2026); ("Motion Blur Review", 2024); ("Citrus GAN", 2025). YOLOv4 tiene mejor robustez a blur que YOLOv8-v11, lo que contradice la intuición de que versiones más nuevas son más robustas.

**IMU supera a óptica — Desactualizado.** La afirmación de (Bell et al., 2014) de que el giroscopio supera a métodos basados en features ha sido superada por métodos híbridos (DeepFused, WACV 2022: 0.853 de estabilidad) y deep learning 3D (RStab, CVPR 2024: 0.92 de estabilidad). Gyroflow, al ser un sistema híbrido (IMU + corrección de lente + rolling shutter), representa el enfoque correcto.

**Rolling Shutter Correction — Beneficio para geometría, no para detección.** ("Let's Roll", 2024) demostraron que la corrección de rolling shutter **no es necesaria** para detección de objetos a IoU≥0.5. Es posible que desactivarla en Gyroflow no degrade el mAP, o incluso lo mejore al evitar artefactos.

#### 3.2.8 Gap Confirmado

> No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en métricas YOLO (mAP) o MOT (MOTA) para video agrícola. Los repositorios existentes (zhouzypaul/object-recognition-imu, Brown 2022) realizan post-procesamiento, no pre-procesamiento. El gap se confirma, aunque la magnitud del efecto es incierta — un resultado modesto sigue siendo una contribución científica válida.

### 3.3 Protocolo de Caminata y Captura (P3)

El protocolo de caminata constituye el núcleo operativo de la captura en campo. Se definen seis parámetros fundamentales, cada uno con su respaldo bibliográfico y la evidencia contradictoria documentada.

#### Resumen de Parámetros

| Parámetro | Valor recomendado | Respaldo principal | Confianza |
|---|---|---|---|
| Velocidad de caminata | ~0.5-1.0 m/s | (Roy et al., 2018); ("MangoYOLO", 2019); ("Motion Blur Review", 2024) | Alta |
| Ángulo de cámara | 15-30° hacia arriba | (Hemming et al., 2014); ("Apple 3D Camera", 2023) | Alta |
| Distancia al dosel | 0.8-1.5 m | ("Orchard-YOLO", 2026); ("RGB-D Sensors", 2020); (Kuznetsova et al., 2020) | Alta |
| Horario / Iluminación | 9-11 AM o 3-5 PM. Nublado ideal. | (Li et al., 2023); (Restrepo-Arias et al., 2023); ("Orchard-YOLO", 2026) | Alta |
| Shutter speed | 1/60-1/120 s | ("Motion Blur Review", 2024); ("FEGW-YOLO", 2026); (Kurtser et al., s.f.) | Alta |
| Estrategia anti-doble conteo | ByteTrack + multi-view | (Gené-Mola et al., 2023) | Alta |

##### 3.3.1 Velocidad de Caminata

**Evidencia principal.** La velocidad de aproximadamente 1 m/s se establece como valor conservador para caminata manual. (Roy et al., 2018) demostraron que incluso a 2 m/s es factible con un Samsung Galaxy S4, logrando una precisión de rendimiento del 95.56-97.83%. ("MangoYOLO", 2019) reportaron un 62% de detección de cosecha a 1.39 m/s (5 km/h). La fórmula de blur ("Motion Blur Review", 2024) permite calcular el desplazamiento en píxeles como función de la velocidad, tiempo de exposición y distancia focal:

```
desplazamiento (px) ≈ (velocidad_caminata × tiempo_exposición) / distancia_focal
Ejemplo a 1 m/s con shutter 1/60 s: ~16 px de blur
Ejemplo a 1 m/s con shutter 1/120 s: ~8 px de blur
```

**Evidencia contradictoria.** (Sanchez & Zhang, 2022) introdujeron la fórmula de overlapping rate (ro = FOV × fps / velocidad), demostrando que con 22 fps son viables velocidades de hasta 2.5 m/s. ("MangoYOLO", 2019) demostraron que 1.39 m/s funciona con tracking Kalman Filter (error de doble conteo solo 2.6%). ("Knowledge Distillation Blur", 2024) encontraron que YOLOv8 pierde solo un 4.6% de mAP@0.5 al 100% de velocidad de motion, y con knowledge distillation solo un 2.5%. La degradación por blur es moderada (15-50%), no catastrófica.

**Decisión final.** El límite de 1 m/s es conservador. Con tracking adecuado y modelos tolerantes al blur, **1.0-1.3 m/s** es viable. Para mandarinas sin deblurring, se recomienda ~1 m/s.

##### 3.3.2 Ángulo de Cámara

**Evidencia principal.** (Hemming et al., 2014) probaron 14 posiciones de cámara en pimiento dulce, encontrando que el ángulo zenith 60° (30° hacia arriba) maximiza la Fruit Detectability como posición única, y que la combinación de 5 posiciones alcanza un FD del 90%. ("Apple 3D Camera", 2023) probaron 0°, 15° y 30° en manzanas con cámara 3D, encontrando que **15°** proporciona el menor RMSE (1.54 cm).

**Evidencia contradictoria.** (Villacrés et al., 2024) encontraron que una cámara perpendicular al dosel (0° horizontal) detecta el 88.3% de los frutos en sistemas multi-cámara para manzanas. ("Apple Orientation", 2025) demostraron que la orientación sideways (horizontal) alcanza un mAP del 95%, superior a cualquier ángulo con tilt. ("Cluster Segmentation", 2025) probaron 0°, 15°, 30° y 45°, encontrando que **45°** da la mejor tasa de detección (>40%).

**Decisión final.** No existe un ángulo único óptimo. La estrategia recomendada para mandarinas en dosel denso es **combinar al menos 2 ángulos**: **0° (horizontal) + 30° hacia arriba**. Idealmente, grabar cada hilera desde ambos lados para obtener automáticamente dos perspectivas. La combinación de 3-5 posiciones maximiza la detectabilidad, como demostró (Hemming et al., 2014).

##### 3.3.3 Distancia al Dosel

**Evidencia principal.** ("Orchard-YOLO", 2026) reportaron que 0.8-1.5 m es el rango óptimo con un mAP del 93.69%. ("RGB-D Sensors", 2020) demostraron que 1.5 m proporciona un 200.5% más de densidad de nube de puntos que 2.5 m. ("Apple detection Redmi Note 7", 2025) validaron el rango 0.3-1.5 m para detección de manzanas con Redmi Note 7.

**Evidencia contradictoria.** ("RealSense Citrus", 2018) encontraron que para cítricos con RealSense, la distancia óptima es de 0.16-0.7 m (close-shot: "close, large, and clear"), con una detección del 80-100% a baja oclusión. ("Oil Palm Stereo", 2024) reportaron que para palma aceitera, 0.3 m es óptimo (F1 = 0.96).

**Distancia óptima según tamaño de fruto:**

| Tipo de fruto | Diámetro típico | Distancia óptima |
|---|---|---|
| Muy pequeños (lychee, blueberry) | ~20-30 mm | 0.3-0.7 m |
| Pequeños (mandarina, cítrico) | ~40-60 mm | **0.5-1.2 m** |
| Grandes (manzana, mango) | ~70-100 mm | 0.8-1.5 m |
| Conteo a nivel árbol | — | 1.5-5 m |

**Decisión final.** Para mandarinas (fruto pequeño ~40-60 mm), la evidencia sugiere que el rango óptimo es **0.5-1.2 m**, más cercano que el 0.8-1.5 m original. Este rango balancea el detalle fino del fruto con la cobertura del dosel.

##### 3.3.4 Horario e Iluminación

**Evidencia principal.** Se recomienda capturar entre 9-11 AM o 3-5 PM, evitando el sol cenital (12-14 PM). ("Orchard-YOLO", 2026) reportaron que la iluminación controlada es crítica: 94.8% mAP en condiciones normales frente a 61.4% en condiciones extremas (−50% brillo, 70% oclusión). ("Kiwifruit glare", 2020) demostraron que el glare destruye la detección: F1 de 0.82 en condiciones normales frente a 0.13 con glare.

**Evidencia contradictoria.** ("Tomato HSV Illumination", 2024) reportaron que el mediodía solar (11-12 h) no solo no es perjudicial, sino que puede dar el mejor rendimiento (precisión 92.1%, F1 90.5% en condiciones de sol cenital). ("Multi-UAV Detection", 2024) encontraron que se requiere un mínimo de 3,000 lx para segmentación precisa, y los días nublados proporcionan solo 1,000-2,000 lx, resultando en solo el 50% del área de fruto detectada. La opción **noche con LED controlado** (5600 K, frontal, 210-350 Lux) consistentemente supera al día en múltiples estudios: ("YOLOv8n-CSE Litchi Night", 2024) lograron un 98.86% mAP@0.5 con LED nocturno en litchi; ("OrBot Night Harvesting", 2024) reportaron un 94% de éxito nocturno frente a 88% diurno en cosecha robótica; ("YOLO-P Pear Night", 2022) alcanzaron un 96.1% F1 nocturno frente a ~93% con luz natural.

**Decisión final.** La recomendación original de "evitar mediodía" es cuestionada por evidencia más reciente. La recomendación "nublado ideal" también se matiza por requerir >3,000 lx para segmentación precisa. Se prioriza la **captura nocturna con iluminación LED frontal** (5600 K, ~300 Lux) como opción superior. Alternativamente, cualquier hora del día funciona, incluido el mediodía. Evitar específicamente backlight extremo y glare.

##### 3.3.5 Motion Blur y Shutter Speed

**Evidencia principal.** ("Motion Blur Review", 2024) proporcionan la fórmula de desplazamiento por blur. ("FEGW-YOLO", 2026) cuantificaron que el mAP@0.5 cae un 27.2% (de 0.925 a 0.673) por motion blur en cítricos. (Kurtser et al., s.f.) demostraron que con exposición a 20 µs (Flash-No-Flash) se logra una precisión del 95% con un recall del 95%.

**Evidencia contradictoria.** (Choi et al., 2021) demostraron que con LED activo, exposiciones de 20 µs eliminan el blur por completo, independientemente del shutter. (Hasinoff et al., 2016) propusieron burst photography (HDR+) como alternativa superior a la exposición fija única. ("DEBIR", 2026) demostraron que la exposición adaptativa por frame supera a 1/60-1/120 s fijo. ("FEGW-YOLO", 2026) encontraron que YOLOv8n retiene un 71.9% de mAP@0.5 incluso con blur severo (kernel=11), y modelos específicos (FEGW-YOLO) retienen un 80.1%. Entrenar con blur (data augmentation) hace que el shutter sea menos crítico.

**Decisión final.** El rango 1/60-1/120 s es razonable para captura sin iluminación adicional. Se recomienda: (a) sin LED: **1/120 s** sobre 1/60 s para minimizar rolling shutter; (b) con LED activo: usar **20-100 µs** (elimina blur por completo); (c) considerar burst photography como alternativa; (d) deblurring post-hoc (AGG-DeblurGAN) puede recuperar calidad si se acepta algo de blur.

##### 3.3.6 Anti-Doble Conteo y Tracking

**Evidencia principal.** (Gené-Mola et al., 2023) compararon SORT, DeepSORT y ByteTrack para conteo de frutos en video, estableciendo que ByteTrack ofrece el mejor rendimiento: MOTA 0.682, IDF1 0.837, HOTA 0.689. ("MangoYOLO", 2019) demostraron que el tracking con Kalman Filter + Hungarian Algorithm alcanza el 62% del conteo de cosecha.

**Evidencia contradictoria.** Múltiples trackers específicos para agricultura superan a ByteTrack. **AgriSORT** ("AgriSORT", 2023) alcanza un MOTA de 65.93 frente a ByteTrack 48.24 (CloseUp). **Dynamic Kalman** ("Deep OC-SORT", 2023) logra un MOTA del 95.0% frente a ByteTrack 75%. **OC-SORT** ("OC-SORT Passion Fruit", 2025) alcanza un HOTA del 67.10% frente a ByteTrack 62.39%. Otros trackers como FTO-SORT (IDF1 90.2%), PineSORT (CVPR 2025) y CoTracker3 (point tracking para oclusiones) representan mejoras adicionales.

**Decisión final.** **ByteTrack NO es la mejor opción para agricultura en 2026.** Se recomienda:

| Tracker | Cuándo usarlo |
|---|---|
| **AgriSORT** ("AgriSORT", 2023) | Tracking de fruta con cámara en movimiento. Motion-only, sin Re-ID. |
| **Dynamic Kalman** | Máxima precisión (MOTA 95%). Requiere tuning del forgetting factor. |
| **OC-SORT** | Buena alternativa general, especialmente con oclusiones. |
| **CoTracker3** | Point-tracking robusto a oclusiones. Alternativa a bounding-box. |
| **ByteTrack** | Mantener como baseline de comparación en el experimento A/B. |

Mantener la estrategia de grabar **ambos lados de la hilera**, pero no necesariamente con multi-view geometry — el tracking temporal desde un solo lado puede ser suficiente con el tracker adecuado.

#### 3.3.7 Gap Confirmado para P3

> No existe un paper que compare la interacción de velocidad × ángulo × distancia combinados para captura manual con smartphone en agricultura, midiendo el impacto en mAP/MOTA. Los papers existentes prueban un parámetro a la vez, usan tractores o robots (no caminata humana), y no reportan mAP/MOTA de YOLO como métrica de comparación de parámetros de captura. La investigación contradictoria de 8 agentes paralelos amplió el gap: tampoco existe un paper que compare noche con LED vs día, AgriSORT vs ByteTrack para cítricos, o single-view video vs multi-view estático para mandarinas en hilera.

#### 3.3.8 Parámetros de Captura Finales

**Valores originales con respaldo bibliográfico directo:**

| Parámetro | Valor | IDs |
|---|---|---|
| Velocidad | ~1 m/s constante | (Roy et al., 2018); ("MangoYOLO", 2019); ("Motion Blur Review", 2024) |
| Ángulo | ~15° hacia arriba | (Hemming et al., 2014); ("Apple 3D Camera", 2023) |
| Distancia | 0.8-1.5 m del dosel | ("Orchard-YOLO", 2026); ("RGB-D Sensors", 2020); (Kuznetsova et al., 2020) |
| Horario | 9-11 AM o 3-5 PM | (Li et al., 2023); (Restrepo-Arias et al., 2023); ("Orchard-YOLO", 2026) |
| Trayectoria | 1 hilera por grabación, un lado | Decisión del protocolo [^1] |
| Anti-doble conteo | ByteTrack + ambos lados de hilera | (Gené-Mola et al., 2023); ("MangoYOLO", 2019) |
| Shutter | 1/60 o 1/120 s fijo | ("Motion Blur Review", 2024); ("FEGW-YOLO", 2026) |

[^1]: El parámetro "Trayectoria — 1 hilera por grabación, un lado" no cuenta con respaldo bibliográfico directo en los papers consultados de P3. Es una decisión del protocolo documentada como gap metodológico.

**Valores actualizados según evidencia contradictoria (recomendación para validación en campo):**

| Parámetro | Valor recomendado | Justificación | Confianza |
|---|---|---|---|
| Velocidad | ~1.0-1.3 m/s (rango ampliado) | Con tracking adecuado y modelos tolerantes al blur, hasta 1.3 m/s es seguro. | Media-Alta |
| Ángulo | 0° (horizontal) + 30° up (combinación) | Horizontal solo: 88.3% detección. Combinar ambas perspectivas maximiza cobertura. | Alta |
| Distancia | 0.5-1.2 m (ajustado para mandarinas) | Frutos pequeños requieren distancia más cercana. Síntesis para mandarinas [^2] | Alta |
| Horario | Noche con LED (5600 K, frontal) > Cualquier horario > Evitar backlight | Noche con LED supera al día. Mediodía funciona bien. Nublado puede ser insuficiente [^3]. | Alta |
| Shutter | 1/120 s fijo (sin LED). 20-100 µs (con LED activo) | 1/120 s sobre 1/60 s para rolling shutter. | Alta |
| Anti-doble conteo | AgriSORT/OC-SORT + ambos lados + single-side video tracking | AgriSORT supera a ByteTrack. Sin validación específica en mandarinas [^4]. | Alta |

[^2]: Distancia 0.5-1.2 m para mandarinas: extrapolación de estudios en cítricos genéricos con RealSense RGB-D a 0.16-0.7 m y oil palm a 0.3 m. El rango para mandarinas es síntesis propia del autor sin validación directa.
[^3]: Noche con LED para mandarinas: extrapolación múltiple. Los estudios disponibles usan robot con LED 5600 K, litchi con LED matrix 210-350 Lux, UAV y peras con 1000 lm. Ningún paper estudia captura manual con smartphone en mandarinas con LED nocturno.
[^4]: AgriSORT/OC-SORT para mandarinas: sin validación específica. El archivo correspondiente a (OC-SORT Passion Fruit) no fue encontrado en la bibliografía de P3. La superioridad sobre ByteTrack en mandarinas es una hipótesis no validada.

### 3.4 Selección de Parcelas para Muestreo (P4)

#### 3.4.1 Introducción

La validez externa de los resultados del experimento A/B depende críticamente de que las parcelas seleccionadas para la captura sean representativas de la variabilidad de vigor presente en el huerto. En huertos frutales, la variabilidad espacial del vigor vegetativo es una fuente importante de heterogeneidad que afecta la densidad de follaje, la iluminación del dosel y, en consecuencia, la calidad de las imágenes capturadas y el rendimiento de los algoritmos de visión por computadora.

#### 3.4.2 Área de Estudio y Datos Disponibles

El área de estudio comprende **4 parcelas** de mandarina variedad **Murcott** de **4 años de edad**, ubicadas en un huerto comercial. Cada parcela tiene una superficie de **0.5 ha** (aproximadamente 70 × 70 m), configuración cuadrada, y contiene **13 hileras** de árboles. Las parcelas comparten el mismo marco de plantación y han sido manejadas con prácticas agronómicas homogéneas.

Se dispone de imágenes del satélite **Sentinel-2** con los siguientes índices de vegetación:

| Índice | Resolución | Píxeles por parcela | ¿Resuelve hileras? | ¿Apto para selección? |
|---|---|---|---|---|
| NDVI | 10 m | ~7 × 7 = 49 píxeles | No (~2 hileras por píxel) | Sí |
| MSAVI2 | 10 m | ~7 × 7 = 49 píxeles | No | Sí |
| NDRE | 20 m | ~3.5 × 3.5 = 12 píxeles | No (~4 hileras por píxel) | Limitado |

#### 3.4.3 Metodología de Selección (4 Pasos)

**Paso 1: Selección de Parcelas por NDVI Medio de Sentinel-2.** Se extrajo el valor medio de NDVI de cada una de las 4 parcelas a partir de imágenes Sentinel-2 (banda 10 m, ~49 píxeles por parcela). Los valores se ordenaron de menor a mayor, representando un gradiente de vigor vegetativo. Se seleccionaron 2 parcelas: una en el extremo inferior (menor NDVI, menor vigor) y una en el extremo superior (mayor NDVI, mayor vigor).

Esta decisión sigue el principio de selección por cuantiles NDVI satelital validado por (Meyers et al., 2020), quienes demostraron que la selección de puntos en las colas de la distribución del índice alcanza la misma representatividad que un número considerablemente mayor de puntos aleatorios. El uso de Sentinel-2 a 10 m está respaldado por ("UAV vs Sentinel-2", 2024), quienes confirmaron que este sensor captura las principales zonas de vigor a nivel de parcela. La aplicación específica a parcelas de cítricos está validada por ("Morocco citrus", 2022), quienes emplearon el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de mandarina.

**Paso 2: Selección de Hileras mediante SUR Sistemático.** Dentro de cada parcela seleccionada, se eligieron 3 hileras mediante muestreo sistemático uniforme (SUR) con arranque aleatorio = 3 e intervalo = 4, resultando en las hileras 3, 7 y 11 de un total de 13. Este método fue validado empíricamente por (Wulfsohn et al., 2012), quienes reportaron errores de estimación inferiores al 10% en 11 de 14 huertos comerciales evaluados. La distribución (hilera 3 cercana al borde, hilera 7 central, hilera 11 cercana al borde opuesto) asegura una cobertura espacial equilibrada de cada parcela.

**Paso 3: Caracterización de Parcelas con NDVI y NDRE.** Las parcelas seleccionadas se caracterizaron mediante valores medios de NDVI (10 m, índice primario) y NDRE (20 m, descriptor complementario). El NDRE se incluyó siguiendo la recomendación de (Sun et al., 2026), quienes demostraron que los índices de Red Edge son superiores al NDVI para estimar LAI (R² = 0.86) y clorofila (R² = 0.80) en mandarinos.

**Paso 4: Captura de Video.** La captura en las 6 unidades de muestreo (2 parcelas × 3 hileras) se realiza siguiendo el protocolo establecido en la sección 3.3: velocidad ~1 m/s, distancia 0.8-1.5 m, ángulo 15-30° hacia arriba, bloqueo de AF/AE/WB.

#### 3.4.4 Discusión y Limitaciones

**Elección de NDVI sobre NDRE.** El NDVI se utilizó para la selección por su resolución de 10 m (49 píxeles/parcela) frente a los 20 m del NDRE (12 píxeles/parcela), proporcionando una estimación más robusta. La literatura de muestreo estratificado ha empleado consistentemente el NDVI como variable auxiliar (Miranda et al., 2018); (Uribeetxebarria et al., 2018); (Meyers et al., 2020); (Arnó et al., 2017). Además, (Ampatzidis & Partel, 2019) demostraron que el NDVI correlaciona significativamente con el tamaño de copa y la sanidad en cítricos.

**Limitaciones:**
- **Número reducido de parcelas (4 disponibles).** Se mitiga mediante estratificación por NDVI, que maximiza la variabilidad con solo 2 unidades (Arnó et al., 2017).
- **Sentinel-2 no resuelve hileras individuales** (~5.4 m de ancho vs 10 m de píxel). Se mitiga mediante SUR para selección intra-parcela (Wulfsohn et al., 2012).
- **Selección de solo 2 parcelas (extremos).** Adecuado para evaluar robustez del protocolo en condiciones extremas de vigor. Para estimación de producción promedio, 3 parcelas serían preferibles.
- **Variedad única (Murcott).** Los resultados no son directamente generalizables a otras variedades.

#### 3.4.5 Conclusión

| Elemento | Decisión | Método | Respaldo |
|---|---|---|---|
| Selección de parcelas | 2 parcelas: menor NDVI + mayor NDVI | Estratificación por NDVI medio Sentinel-2 | (Meyers et al., 2020); ("Morocco citrus", 2022); (Arnó et al., 2017) |
| Selección de hileras | 3 hileras por parcela: 3, 7, 11 | SUR sistemático con arranque aleatorio | (Wulfsohn et al., 2012) |
| Caracterización | NDVI medio + NDRE medio | Índices Sentinel-2 | (Sun et al., 2026) |
| Total de videos | 6 videos | 2 parcelas × 3 hileras | — |
| Tiempo estimado | ~30 minutos | — | — |

### 3.5 Pipeline de Captura (7 Etapas)

El pipeline completo de captura y procesamiento se estructura en 7 etapas, desde la pre-captura hasta el entrenamiento:

```
PRE-CAPTURA → CAPTURA → POST-PROCESAMIENTO → ENTRENAMIENTO
```

| Etapa | Qué se hace | App/Equipo |
|---|---|---|
| 1. App de Cámara | Bloquear AF/AE/WB + ISO/shutter fijos | Open Camera (Camera2 API) |
| 2. Estabilización | Gimbal mecánico + Gyroflow (post) | DJI Osmo + Gyroflow |
| 3. Logging IMU | Giroscopio + acelerómetro 100 Hz | Sensor Logger |
| 4. Sincronización Video-IMU | Frame-level sync | OpenCamera Sensors / Clap sync |
| 5. Calibración de Cámara | Corrección de distorsión | OpenCV + Charuco |
| 6. Pre-procesamiento | Estabilización + (opcional) deblurring | Gyroflow + FFmpeg |
| 7. Pipeline de Datos | YOLO + ByteTrack/CoTracker3 | YOLO + TrackEval |

### 3.6 Parámetros de Captura

**Parámetros de cámara:**

| Parámetro | Valor | Justificación |
|---|---|---|
| App | Open Camera (Camera2 API ON) | Única gratuita con AF/AE/WB Lock |
| Resolución | 4K (3840×2160) o 1080p | Píxeles por fruto pequeño |
| FPS | 30 | Suficiente para tracking |
| ISO | 200 fijo (100 si hay suficiente luz) | ISO=200 documentado ("Open Camera v1.52", 2024) |
| Shutter | 1/100 s fijo (rango 1/60-1/120) | Compromiso entre blur y luz ("Motion Blur Review", 2024) |
| AF | 🔒 LOCK | Evita focus hunting ("Focus Hunting CVPR", 2025) |
| AE | 🔒 LOCK | Brillo constante ("Phenotyping Manual vs Auto", 2018) |
| WB | 🔒 LOCK | Color estable ("Camera2 API", 2023) |
| Bitrate | 50 Mbps | Calidad constante |
| OIS | OFF | Interfiere con Gyroflow ("DeepOIS", 2021); ("ISPRS IS", 2022) |

**Parámetros en campo:**

| Parámetro | Valor |
|---|---|
| Distancia al dosel | 0.5-1.5 m |
| Velocidad | ~0.5-1 m/s constante |
| Ángulo | 0-30° hacia arriba |
| Horario | 8:30 AM+, evitar 12-14 PM |
| IMU | 100 Hz (gyro + accel) |

### 3.7 Experimento A/B (Validación)

El diseño experimental para validar el protocolo consiste en una comparación A/B:

| Grupo | Captura |
|---|---|
| **A (Protocolo)** | Siguiendo todos los pasos del pipeline |
| **B (Control)** | Cámara nativa en modo automático |
| **Métrica** | mAP@0.5, MOTA, IDF1, % frames borrosos |

Este experimento medirá cuantitativamente el impacto del protocolo de captura en las métricas de detección y seguimiento, comparando el pipeline completo frente a la captura sin control de parámetros.

---

## Capítulo 4: Discusión

### 4.1 Evidencia Contradictoria Consolidada

La investigación bibliográfica realizada, incluyendo la investigación contradictoria con 8 agentes paralelos, reveló varios patrones que matizan las recomendaciones originales del protocolo sin invalidarlas:

**La velocidad de caminata no es tan crítica como se pensaba.** Múltiples estudios demuestran que los modelos YOLO modernos toleran el motion blur mejor de lo que se creía: la degradación real por blur es del 15-50% (no el 86.4% reportado inicialmente como mejora), y modelos entrenados con data augmentation de blur pierden solo un 2.5-4.6% de mAP. Sin embargo, para mandarinas (frutos pequeños en dosel denso), mantener una velocidad controlada sigue siendo una buena práctica para maximizar la calidad del dataset.

**La iluminación controlada (noche + LED) supera consistentemente al día.** Esta es quizás la contradicción más relevante: la recomendación original de "evitar mediodía" y "días nublados ideales" es directamente contradicha por estudios que muestran que (a) el mediodía solar da excelentes resultados, (b) los días nublados pueden ser insuficientes (<3,000 lx) y (c) la noche con iluminación LED frontal (5600 K, ~300 Lux) consistentemente supera al día en todas las métricas. Esto abre una línea de investigación prometedora para la tesis.

**Los trackers específicos para agricultura superan a ByteTrack.** La recomendación original de ByteTrack como tracker principal es contradicha por AgriSORT (MOTA 65.93 vs 48.24), Dynamic Kalman (MOTA 95% vs 75%) y OC-SORT (HOTA 67.10% vs 62.39%). Se recomienda usar AgriSORT o OC-SORT como tracker principal y mantener ByteTrack como baseline de comparación.

**El nuevo paradigma de detección robusta (2024-2026) no invalida el control de captura.** Aunque detectores como Orchard-YOLO logran >94% mAP con variaciones de iluminación de ±50%, el control de captura y los modelos robustos son complementarios, no sustitutos. El experimento A/B de esta tesis (Protocolo vs Cámara Nativa) es precisamente lo que falta en la literatura para cuantificar esta complementariedad.

### 4.2 Discusión sobre Valores Propuestos vs Documentados

Los valores específicos propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120 s) **no son valores extraídos directamente de un paper**, sino decisiones de ingeniería informadas por la literatura. Esta distinción es importante para la reproducibilidad y la interpretación de los resultados.

Los valores documentados en papers son heterogéneos y dependientes de condiciones específicas: ISO=25 y shutter=1/400 s en condiciones de laboratorio; ISO=200 y shutter=1/100 s con iluminación LED controlada; exposiciones de 20-250 µs con flashes sincronizados en sistemas industriales. No existe un consenso en la literatura sobre un valor único para captura manual con smartphone en agricultura.

El protocolo propone valores de compromiso que maximizan la utilidad práctica en condiciones de campo reales, y el experimento A/B determinará si estas decisiones son adecuadas frente a la ausencia total de control (cámara nativa).

### 4.3 Limitaciones de la Metodología

**Limitación del software de captura a Android.** El protocolo solo es aplicable a dispositivos Android con Camera2 API, ya que iOS no expone control sobre el tone mapping en video ("Camera2 API", 2023). Los resultados pueden no ser transferibles entre plataformas.

**Extrapolaciones del protocolo de caminata.** Varios valores propuestos para mandarinas son extrapolaciones de estudios en otros cultivos:
- La distancia 0.5-1.2 m para mandarinas es síntesis propia a partir de estudios en cítricos genéricos y oil palm, sin validación directa en mandarinas.
- La captura nocturna con LED se basa en estudios en litchi, peras y robótica, no en captura manual de mandarinas.
- La superioridad de AgriSORT/OC-SORT sobre ByteTrack en mandarinas es una hipótesis no validada.

**Limitaciones del muestreo de parcelas.** Con solo 4 parcelas disponibles de una única variedad (Murcott), la selección de 2 parcelas extremas maximiza la representatividad pero sacrifica la cobertura del rango medio de vigor. Sentinel-2 no resuelve hileras individuales.

**Robustez desconocida de YOLO moderno.** Si YOLO resulta ser inherentemente robusto a las variaciones de captura, el efecto del protocolo podría ser modesto. Un resultado nulo sigue siendo una contribución científica válida.

### 4.4 Implicaciones para el Experimento A/B

Las contradicciones documentadas tienen implicaciones directas para el diseño del experimento A/B:

1. **El Grupo B (Control) con cámara nativa podría no ser tan deficiente como se esperaba**, dada la robustez de los detectores modernos. Esto hace que el experimento sea más informativo, no menos.
2. **La noche con LED como tercera condición experimental** (Grupo C) sería una valiosa adición, permitiendo comparar tres condiciones: protocolo diurno, protocolo nocturno con LED y cámara nativa.
3. **La selección del tracker debe considerar AgriSORT/OC-SORT** como alternativa a ByteTrack, no solo como reemplazo sino como variable experimental.
4. **Las métricas deben incluir tanto mAP como MOTA e IDF1**, ya que las contradicciones sugieren que el impacto del protocolo puede ser mayor en tracking que en detección.

---

## Capítulo 5: Conclusiones

### 5.1 Gap de Investigación Confirmado

El análisis bibliográfico sistemático realizado confirma los siguientes gaps en la literatura:

1. **Software de captura:** Solo 1 paper en toda la literatura ("Open Camera v1.52", 2024) documenta Open Camera con configuración detallada. Ningún paper documenta el flujo completo app + configuración + IMU + pipeline para detección de frutos en video.
2. **IMU → YOLO mAP:** No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU en métricas YOLO o MOT para video agrícola.
3. **Parámetros combinados:** No existe un paper que compare la interacción de velocidad × ángulo × distancia para captura manual con smartphone en agricultura.
4. **Noche con LED vs día:** No existe un paper que compare noche con LED vs día para detección YOLO de mandarinas.
5. **Trackers en cítricos:** AgriSORT/OC-SORT no se han probado específicamente para tracking de cítricos en video.
6. **Selección de parcelas:** No existe un protocolo que integre selección por NDVI satelital con un pipeline completo de captura para cítricos.

### 5.2 Contribución Original

La contribución original de esta investigación consiste en documentar y medir cuantitativamente el impacto de las decisiones de captura en mAP/MOTA para video de mandarinas, integrando:

- **P1:** Documentación y justificación del pipeline de captura (app + configuración + IMU + procesamiento) con métricas cuantitativas de impacto en YOLO, mediante experimento A/B (Protocolo vs Cámara Nativa).
- **P2:** Medición del impacto del pre-procesamiento con IMU (Gyroflow) en métricas YOLO y MOT para video agrícola.
- **P3:** Medición cuantitativa del impacto combinado de velocidad × ángulo × distancia en mAP/MOTA para video de mandarinas capturado con smartphone.
- **P4:** Metodología reproducible de selección de parcelas por NDVI satelital con muestreo sistemático uniforme.

### 5.3 Valores Finales del Protocolo

**Valores validados bibliográficamente (recomendación base):**

| Parámetro | Valor |
|---|---|
| App de cámara | Open Camera con Camera2 API |
| Resolución | 4K (3840×2160) o 1080p |
| FPS | 30 |
| ISO | 200 fijo (100 si hay suficiente luz) |
| Shutter | 1/100 s fijo (rango 1/60-1/120) |
| AF/AE/WB | LOCK |
| Bitrate | 50 Mbps |
| OIS | OFF |
| Velocidad de caminata | ~0.5-1.0 m/s |
| Ángulo de cámara | 15-30° hacia arriba |
| Distancia al dosel | 0.8-1.5 m |
| Horario | 9-11 AM o 3-5 PM (o noche con LED) |
| IMU | 100 Hz (giroscopio + acelerómetro) |
| Tracker recomendado | ByteTrack (AgriSORT/OC-SORT como alternativa) |

### 5.4 Trabajo Futuro

Se sugieren las siguientes líneas de trabajo futuro:
- Validación experimental del protocolo completo frente a cámara nativa (experimento A/B planificado).
- Evaluación de la captura nocturna con iluminación LED como condición experimental adicional.
- Comparación de ByteTrack, AgriSORT, OC-SORT y CoTracker3 para tracking de mandarinas.
- Evaluación del impacto del tone mapping lineal (Camera2 API) frente al procesamiento ISP por defecto.
- Validación del protocolo en otras variedades de mandarina y otros cultivos de fruto pequeño.

---

## Capítulo 6: Referencias

Ampatzidis, Y. & Partel, V. (2019). UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence. *Remote Sensing*, 11(4), 410. https://doi.org/10.3390/rs11040410

Arnó, J., Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A. & Rosell-Polo, J.R. (2017). Comparing efficiency of different sampling schemes to estimate yield and quality parameters in fruit orchards. *Advances in Animal Biosciences*, 8(2), 471-476. https://doi.org/10.1017/S2040470017000978

Arslan, A., Gultekin, G.K. & Saranli, A. (2024). IMU-aided adaptive mesh-grid based video motion deblurring. *PeerJ Computer Science*, 10, e2540. https://doi.org/10.7717/peerj-cs.2540

Bell, S., Troccoli, A. & Pulli, K. (2014). A Non-Linear Filter for Video Stabilization and Rolling Shutter on Mobile Devices. *ECCV 2014*. NVIDIA Research.

Choi, K.T.H. (2024). Sensor Logger: A Framework for Smartphone-based Sensor Data Collection. *CEUR Workshop*.

Choi et al. (2021). Overcurrent-driven LEDs for Consistent Image Colour and Brightness in Agricultural Machine Vision. *Computers and Electronics in Agriculture*.

Fan, B. et al. (2025). Influence of Sampling Rate on IMU Orientation Estimation for Human Movement. *Sensors*, 25(7), 1976. https://doi.org/10.3390/s25071976

Gené-Mola, J., Sanz-Cortiella, R., Rosell-Polo, J.R. et al. (2023). Video-Based Fruit Detection and Tracking for Apple Counting. *Computers and Electronics in Agriculture*.

Han, F., Xie, L., Yin, Y., Zhang, H., Chen, G. & Lu, S. (2021). Video Stabilization for Camera Shoot in Mobile Devices via Inertial-Visual State Tracking. *IEEE Trans. Mobile Computing*.

Hasinoff, S. et al. (2016). Burst Photography for High Dynamic Range and Low-Light Imaging (HDR+). *ACM Trans. Graphics*.

Hemming, J., Ruizendaal, J., Hofstee, J.W. & van Henten, E.J. (2014). Fruit Detectability Analysis for Different Camera Positions in Sweet-Pepper. *Sensors*, 14(6), 6032. https://doi.org/10.3390/s140606032

Janowski, A., Kazmierczak, R., Kowalczyk, C. & Szulwic, J. (2021). Detecting Apples in the Wild: Potential for Harvest Quantity Estimation. *Sustainability*, 13(14), 8054. https://doi.org/10.3390/SU13148054

Jaramillo, J., Vanden Heuvel, J. & Petersen, K.H. (2025). Toward Estimating the Crop Coefficient of Vineyards Using a Smartphone Camera. *American Journal of Enology and Viticulture*. https://doi.org/10.5344/ajev.2025.24068

Kurtser, P. et al. (s.f.). Flash-No-Flash controlled illumination for fruit detection.

Kuznetsova, A., Maleva, T. & Soloviev, V. (2020). Using YOLOv3 Algorithm with Pre- and Post-Processing for Apple Detection. *Agronomy*, 10(7), 1016. https://doi.org/10.3390/agronomy10071016

Li, C., Song, L., Chen, S., Xie, R. & Zhang, W. (2023). Deep Online Video Stabilization Using IMU Sensors. *IEEE Trans. Multimedia*. https://doi.org/10.1109/TMM.2022.3142429

Li, C., Bu, Y. & Xie, L. (2025). Towards Visual-Inertial Integration: Multi-Modal Collaboration-based Video Stabilization. *IEEE ICDCS 2025*. https://doi.org/10.1109/ICDCS63083.2025.00107

Li, L. et al. (2023). YOLOv5s-FP: Pear Detection with Transformer Encoder. *Sensors*, 23(1), 30. https://doi.org/10.3390/s23010030

Meyers, J.M., Dokoozlian, N., Ryan, C., Bioni, C. & Vanden Heuvel, J.E. (2020). A New, Satellite NDVI-Based Sampling Protocol for Grape Maturation Monitoring. *Remote Sensing*, 12(7), 1159. https://doi.org/10.3390/rs12071159

Miranda, C., Santesteban, L.G., Urrestarazu, J., Loidi, M. & Royo, J.B. (2018). Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards. *Agriculture*, 8(6), 78. https://doi.org/10.3390/agriculture8060078

Moussaid, A., El Fkihi, S., Zennayi, Y. et al. (2022). Machine Learning Applied to Tree Crop Yield Prediction Using Field Data and Satellite Imagery: A Case Study in a Citrus Orchard. *Informatics*, 9(3), 80. https://doi.org/10.3390/informatics9040080

Peng, Z., Zhu, X., Wu, J. & Qin, Z. (2020). A real-time fisheye video correction method based on Android smartphone GPU. *Optik*. https://doi.org/10.1016/j.ijleo.2020.165108

Ramos Giraldo, P.J., Guerrero Aguirre, A., Muñoz, C.M., Prieto, F.A. & Oliveros, C.E. (2017). Sensor Fusion of a Mobile Device to Acquire Videos of Coffee Branches. *Sensors*, 17(4), 786. https://doi.org/10.3390/s17040786

Rançon, F., Keresztes, B., Deshayes, A. et al. (2023). Designing a Proximal Sensing Camera Acquisition System for Vineyard Applications: 8 Years of Experiments. *Sensors*, 23(2), 847. https://doi.org/10.3390/s23020847

Restrepo-Arias, J.F., Salinas-Agudelo, M.I., Hernandez-Pérez, M.I. et al. (2023). RipSetCocoaCNCH12: Dataset for Ripeness Stage Detection. *Data*, 8(7), 112. https://doi.org/10.3390/data8070112

Roy, P., Dong, Y. & Isler, V. (2018). A Comparative Study of Fruit Detection and Counting Methods for Yield Mapping in Apple Orchards. *arXiv*. arXiv:1810.09499

Sanchez, J.A. & Zhang, Y. (2022). Simulation-Aided Development of CNN-Based Vision Module — Overlapping Rate. *Appl. Sci.*, 12(11), 5600. https://doi.org/10.3390/app12125600

Sun, Y., Qin, Q., Zhang, J., Ren, H. & Han, R. (2026). Fruit Yield Estimation of Kinnow Mandarin Orchards — Integrating Canopy Physiology with Remote Sensing. *Arabian Journal of Geosciences*. https://doi.org/10.1007/s12517-026-12453-z

Torun et al. (2021). In-Shoe System for Gait Monitoring — Effects of Sampling Rate. *Sensors*. https://doi.org/10.3390/s21082869

Uribeetxebarria, A., Martínez-Casasnovas, J.A., Escolà, A., Rosell-Polo, J.R. & Arnó, J. (2018). Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps: A Comparative Analysis to Improve Yield and Quality Estimates. *Precision Agriculture*, 19, 1031-1050. https://doi.org/10.1007/s11119-018-9619-9

Vélez, S., Ariza-Sentís, M. & Valente, J. (2024). EscaYard: Precision viticulture multimodal dataset. *Data in Brief*. https://doi.org/10.1016/j.dib.2024.110497

Villacrés, J. et al. (2024). Assessing a Multi-Camera System to Enhance Fruit Visibility for Robotic Harvesting.

Wang, Z., Koirala, A., Walsh, K., Anderson, N. & Verma, B. (2018). In Field Fruit Sizing Using A Smart Phone Application (FruitSize). *Sensors*, 18(10), 3331. https://doi.org/10.3390/s18103331

Wulfsohn, D., Aravena, F., Potin, C., Zamora, I. & García-Fiñana, M. (2012). Multilevel Systematic Sampling to Estimate Total Fruit Number. *Precision Agriculture* (Springer).

Zhang, K. & Zhang, M. (2023). Point feature correction based rolling shutter modeling for EKF-based VIO. *Measurement Science and Technology*. https://doi.org/10.1088/1361-6501/ad044e

Zhao, G., Yang, R., Jing, X. et al. (2023). Phenotyping of individual apple tree with smartphone-based heterogeneous binocular vision. *Computers and Electronics in Agriculture*. https://doi.org/10.1016/j.compag.2023.107814

Zhou, Z., Song, Z., Fu, L. et al. (2020). Real-time kiwifruit detection using deep learning on Android smartphones. *Computers and Electronics in Agriculture*. https://doi.org/10.1016/j.compag.2020.105856

**Papers con autoría no especificada (citados por título):**

AgriSORT: Online Real-time Tracking-by-Detection for Agriculture. (2023). *arXiv*. arXiv:2309.13393

Apple detection Redmi Note 7 + YOLOv8n. (2025). *Plants*.

A Robust Illumination-Invariant Camera System for Agricultural Applications. (2021). *arXiv*. arXiv:2101.02190

A State-of-the-Art Review of Image Motion Deblurring Techniques in Precision Agriculture. (2024). *Heliyon*.

Crop Row Video Stabilization for Agricultural Field Robotics. (s.f.). *MDPI Sensors*.

DeepOIS: Gyroscope-Guided Deep Optical Image Stabilizer Compensation. (2021). *arXiv*. arXiv:2101.11183

Illumination-Invariant Camera System. (2021). *arXiv*.

Impact of ISP Tuning on Object Detection. (2023). *MDPI J. Imaging*, 9(12), 260. https://doi.org/10.3390/jimaging9120260

Land-based Crop Phenotyping by Image Analysis: Consistent Canopy Characterization from Inconsistent Field Illumination. (2018). *Plant Methods*.

Lightweight GAN for Restoring Blurred Images to Enhance Citrus Detection. (2025). *MDPI Plants*.

Mango Fruit Load Estimation Using Video Based MangoYOLO-Kalman Filter-Hungarian Algorithm. (2019). *Sensors*, 19(12), 2742. https://doi.org/10.3390/s19122742

Mobile AR Sensor (MARS) Logger. (2020). *arXiv*. arXiv:2001.00470

Orchard-YOLO: A Robust Deep Learning Framework for Fruit Detection Under Complex Optical and Environmental Degradation. (2026). *Photonics*, 13(5), 0429. https://doi.org/10.3390/photonics13050429

Recognition and Counting of Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms. (2023). *Sensors*, 23(8), 3810. https://doi.org/10.3390/s23083810

Rice Grain Moisture Content Measurement with Smartphone. (2021). *Sensors*.

YOLO-CSB: Real-Time Detection of Occluded Apples for Precision Agriculture. (2026). *Agronomy*, 16(3), 0390. https://doi.org/10.3390/agronomy16030390

**Documentación técnica:**

Gyroflow Documentation. (s.f.). https://docs.gyroflow.xyz/ [D2]

Open Camera Help. (s.f.). https://opencamera.sourceforge.io/help.html [D1]

Sensor Logger Official Site. (s.f.). https://www.tszheichoi.com/sensorlogger [D3]

OpenCamera Sensors (GitHub). (s.f.). https://github.com/prime-slam/opencamera-sensors [D4]

Gyroflow GitHub. (s.f.). https://github.com/gyroflow/gyroflow [D5]

> **Nota:** La tabla maestra completa con 138 referencias, incluyendo metadatos detallados (DOI, nivel de importancia, contexto en el proyecto) para cada una de las referencias P01-P130 y D1-D8, se encuentra disponible en el archivo `Tabla-Maestra-Papers.md` del repositorio del proyecto.

---

## Apéndice: Tabla de Trazabilidad [PXX] → APA

El siguiente apéndice documenta la correspondencia entre los identificadores [PXX] utilizados en los archivos de investigación fuente y las citas en formato APA empleadas en el presente documento, garantizando la trazabilidad completa de cada decisión técnica según el Principio II de la constitución del proyecto.

| ID | Cita APA |
|---|---|
| P01 | (Janowski et al., 2021) |
| P02 | (Vélez et al., 2024) |
| P03 | (Zhao et al., 2023) |
| P05 | (Zhou et al., 2020) |
| P10 | (Peng et al., 2020) |
| P11 | (Han et al., 2021) |
| P12 | (Li et al., 2023) |
| P13 | (Li et al., 2025) |
| P18 | (Zhang & Zhang, 2023) |
| P22 | (Arslan et al., 2024) |
| P23 | (Choi, 2024) |
| P24 | ("Mobile AR Sensor Logger", 2020) |
| P25 | (Fan et al., 2025) |
| P26 | (Bell et al., 2014) |
| P27 | (Ramos Giraldo et al., 2017) |
| P28 | (Kuznetsova et al., 2020) |
| P29 | (Li et al., 2023) |
| P30 | (Restrepo-Arias et al., 2023) |
| P34 | (Zhai et al., 2025) |
| P35 | ("AgriSORT", 2023) |
| P37 | ("Apple detection Redmi Note 7", 2025) |
| P40 | (Kurtser et al., s.f.) |
| P47 | (Wang et al., 2018) |
| P48 | (Zhou et al., 2020) — mismo paper que P05 (duplicado) |
| P49 | (Rançon et al., 2023) |
| P55 | ("Rice GMC", 2021) |
| P57 | (Choi et al., 2021) |
| P58 | ("Phenotyping Manual vs Auto", 2018) |
| P59 | ("Illumination-Invariant", 2021) |
| P60 | ("Stanford CNN + Exposure", 2018) |
| P61 | ("Focus Hunting CVPR", 2025) |
| P62 | ("Camera2 API", 2023) |
| P63 | ("Kiwifruit glare", 2020) |
| P64 | ("DeepOIS", 2021) |
| P65 | ("ISPRS IS", 2022) |
| P66 | ("MangoYOLO", 2019) |
| P67 | ("Crop Row Stabilization", s.f.) |
| P68 | ("Citrus GAN", 2025) |
| P69 | (Hemming et al., 2014) |
| P70 | (Roy et al., 2018) |
| P71 | ("Apple 3D Camera", 2023) |
| P72 | ("RGB-D Sensors", 2020) |
| P73 | ("YOLO-CSB", 2026) |
| P74 | (Gené-Mola et al., 2023) |
| P75 | ("Motion Blur Review", 2024) |
| P76 | ("Orchard-YOLO", 2026) |
| P79 | (Miranda et al., 2018) |
| P80 | (Uribeetxebarria et al., 2018) |
| P82 | (Meyers et al., 2020) |
| P84 | ("UAV vs Sentinel-2", 2024) |
| P85 | ("Morocco citrus", 2022) |
| P88 | (Wulfsohn et al., 2012) |
| P90 | (Sun et al., 2026) |
| P91 | (Arnó et al., 2017) |
| P93 | (Ampatzidis & Partel, 2019) |
| P95 | ("ISP Tuning", 2023) |
| P96 | ("Unintentional Adversary ECCV", 2022) |
| P97 | ("ISP-less CV", 2022) |
| P98 | ("AdaptiveISP", 2024) |
| P99 | ("Open Camera v1.52", 2024) |
| P100 | ("Qualcomm OIS+EIS Patent", 2024) |
| P101 | ("HyperOIS", 2024) |
| P102 | (Torun et al., 2021) |
| P103 | ("FEGW-YOLO", 2026) |
| P105 | ("Knowledge Distillation Blur", 2024) |
| P106 | ("MDPI Electronics YOLO", 2025) |
| P107 | ("DeepFused WACV", 2022) |
| P108 | ("RStab CVPR", 2024) |
| P109 | ("Let's Roll", 2024) |
| P110 | (Sanchez & Zhang, 2022) |
| P111 | (Villacrés et al., 2024) |
| P112 | ("Apple Orientation", 2025) |
| P113 | ("Cluster Segmentation", 2025) |
| P114 | ("RealSense Citrus", 2018) |
| P115 | ("Oil Palm Stereo", 2024) |
| P116 | ("Multi-UAV Detection", 2024) |
| P117 | ("YOLOv8n-CSE Litchi Night", 2024) |
| P118 | ("OrBot Night Harvesting", 2024) |
| P119 | ("YOLO-P Pear Night", 2022) |
| P120 | ("Tomato HSV Illumination", 2024) |
| P121 | (Hasinoff et al., 2016) |
| P122 | ("DEBIR", 2026) |
| P123 | ("OC-SORT Passion Fruit", 2025) |
| P124 | ("Deep OC-SORT", 2023) |
| P125 | ("FTO-SORT", 2025) |
| P126 | ("LocalizeSORT", 2026) |
| P127 | ("PineSORT CVPR", 2025) |
| P128 | ("CoTracker3", 2025) |
| P129 | ("Transformer Apple Fruitlet", 2025) |
| P130 | ("MOT-DETR-3D", 2023) |

