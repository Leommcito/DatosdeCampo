# MetodologÃ­a de Captura Manual con Smartphone para DetecciÃ³n YOLO y Seguimiento MOT en Huertos Densos de Mandarinas

**Documento metodolÃ³gico integrado**
*Tesis â€” ValidaciÃ³n en campo: 05/06/2026*

---

## CapÃ­tulo 1: Marco TeÃ³rico

### 1.1 Objetivo General

El objetivo general de esta investigaciÃ³n es establecer un **protocolo de recolecciÃ³n de datos en campo** para grabar **videos manuales con smartphone** en **huertos densos de mandarinas**, asegurando que el material capturado sea Ã³ptimo para modelos de **detecciÃ³n YOLO** y **seguimiento MOT (Multiple Object Tracking)**.

El enfoque principal es **capturar el video de la forma mÃ¡s limpia posible desde el origen**, mitigando problemas fÃ­sicos en el momento de la grabaciÃ³n (no en post-procesamiento computacional). La prioridad es contar con **respaldo bibliogrÃ¡fico** para cada decisiÃ³n de captura, produciendo un dataset de video de alta calidad para modelos YOLO + MOT en un contexto de huerto de mandarinas denso, caracterizado por alta oclusiÃ³n, follaje denso y frutos pequeÃ±os.

### 1.2 Problemas a Mitigar Durante la Captura Manual

La captura manual con smartphone en huertos densos presenta 18 problemas identificados, clasificados por nivel de riesgo:

| Problema | Riesgo |
|---|---|
| Movimiento brusco de cÃ¡mara (shake) | Muy Alto |
| Desenfoque por movimiento (motion blur) | Muy Alto |
| Cambios de altura/distancia al dosel | Muy Alto |
| Cambios de Ã¡ngulo e inclinaciÃ³n | Muy Alto |
| Objetivo fuera del encuadre | Alto |
| Oclusiones (personas, ramas, vehÃ­culos) | Alto |
| Variaciones de iluminaciÃ³n (nubes, sombras) | Alto |
| Autofoco inestable (focus hunting) | Alto |
| ExposiciÃ³n incorrecta | Alto |
| Velocidad inconsistente de movimiento | Medio |
| RotaciÃ³n de cÃ¡mara (roll) | Medio |
| Cambios de zoom digital | Medio |
| CompresiÃ³n excesiva del dispositivo | Medio |
| Diferencias entre dispositivos | Medio-Bajo |
| DistorsiÃ³n de lente (gran angular) | Bajo |
| Reflejos/flare solar | Bajo |
| Ruido digital (poca luz) | Bajo |
| Variaciones de balance de blancos (AWB) | Bajo |

### 1.3 Preguntas de InvestigaciÃ³n

La investigaciÃ³n se organiza en torno a tres preguntas fundamentales, cada una abordada en un sub-capÃ­tulo metodolÃ³gico:

**Pregunta 1 (P1) â€” Software de Captura y Bloqueo de Sensores.** Investigar por quÃ© la cÃ¡mara nativa en modo automÃ¡tico es perjudicial para datasets de visiÃ³n computacional en agricultura, evaluando aplicaciones como Open Camera y Filmic Pro para el bloqueo de autofoco (AF), exposiciÃ³n (ISO/shutter) y balance de blancos (AWB). Se requiere respaldo bibliogrÃ¡fico que demuestre que el focus hunting, la autoexposiciÃ³n y el AWB automÃ¡tico degradan la calidad de los datasets para detecciÃ³n y tracking.

**Pregunta 2 (P2) â€” Registro de TelemetrÃ­a (IMU) en Tiempo Real.** Evaluar la necesidad de ejecutar aplicaciones como Sensor Logger en segundo plano durante la caminata por el huerto para registrar giroscopio (velocidad angular en X, Y, Z), acelerÃ³metro (aceleraciÃ³n lineal) y magnetÃ³metro (orientaciÃ³n). El propÃ³sito es capturar la firma del movimiento humano para su uso en post-producciÃ³n (deblurring, estabilizaciÃ³n, correcciÃ³n de rolling shutter).

**Pregunta 3 (P3) â€” DiseÃ±o del Protocolo de Caminata y Captura.** Definir metodologÃ­as documentadas sobre cÃ³mo debe caminar el operador: distancia recomendada hacia el dosel, Ã¡ngulo de inclinaciÃ³n de la cÃ¡mara, velocidad de desplazamiento, horarios Ã³ptimos de grabaciÃ³n, trayectoria y estrategia para evitar doble conteo.

Adicionalmente, la **Pregunta 4 (P4)** aborda la selecciÃ³n de parcelas para el muestreo en campo, garantizando la representatividad del diseÃ±o experimental.

### 1.4 Principios Rectores

La presente investigaciÃ³n se rige por cinco principios rectores establecidos en la constituciÃ³n del proyecto, que garantizan el rigor metodolÃ³gico y la trazabilidad de cada decisiÃ³n tÃ©cnica:

**Principio I â€” Rigor BibliogrÃ¡fico.** Cada decisiÃ³n de captura debe estar respaldada por evidencia bibliogrÃ¡fica cuantitativa siempre que sea posible. Las decisiones basadas en ingenierÃ­a o sentido prÃ¡ctico deben documentarse explÃ­citamente como tales.

**Principio II â€” Trazabilidad.** Cada decisiÃ³n tÃ©cnica estÃ¡ vinculada a un identificador Ãºnico de referencia (sistema [PXX] en los archivos de trabajo, convertido a formato APA en el presente documento). La cadena de trazabilidad es: DecisiÃ³n â†’ Referencia â†’ DOI/URL â†’ Verificable.

**Principio III â€” Reproducibilidad.** El protocolo debe ser reproducible por cualquier investigador con un dispositivo Android compatible con Camera2 API. Todas las aplicaciones, configuraciones y procedimientos deben documentarse explÃ­citamente.

**Principio IV â€” Transparencia ante Contradicciones.** La evidencia contradictoria o que matice las recomendaciones originales debe documentarse explÃ­citamente, no ocultarse. Cada parÃ¡metro del protocolo incluye tanto el respaldo original como la evidencia contradictoria encontrada.

**Principio V â€” PreservaciÃ³n del Contenido.** La fusiÃ³n de investigaciones en este documento preserva el 100% del contenido de los archivos fuente. No se inventa ni se omite informaciÃ³n. Las anotaciones y matices se conservan como notas al pie.

### 1.5 Stack TecnolÃ³gico Objetivo

El stack tecnolÃ³gico definido para el proyecto abarca desde la captura hasta el entrenamiento:

- **Captura:** Smartphone Android con app de cÃ¡mara profesional (Open Camera con Camera2 API)
- **TelemetrÃ­a:** Sensor Logger (IMU: giroscopio + acelerÃ³metro a 100 Hz)
- **EstabilizaciÃ³n:** Gyroflow (post-procesamiento con datos IMU)
- **DetecciÃ³n:** YOLO (v9, v11 o variantes)
- **Seguimiento:** ByteTrack / AgriSORT / OC-SORT / CoTracker3
- **Post-procesamiento:** Deblurring (NAFNet, DeblurGAN-v2, AGG-DeblurGAN), SLAM (iSAM2), Bundle Adjustment
- **EstimaciÃ³n de rendimiento:** ReconstrucciÃ³n 3D multiframe + factor-graph optimization

### 1.6 Sistema de Trazabilidad

Cada decisiÃ³n tÃ©cnica en este documento sigue la cadena de trazabilidad establecida por el Principio II. En los archivos de investigaciÃ³n fuente, las referencias se identifican con cÃ³digos [PXX]; en el presente documento, dichos cÃ³digos han sido convertidos al formato APA (Autor, AÃ±o). La correspondencia entre ambos sistemas se preserva en el ApÃ©ndice de Trazabilidad al final del documento.

**Ejemplo de trazabilidad:**
```
DecisiÃ³n: AE Lock (exposiciÃ³n fija)
  â†’ (Autores, 2018) â€” Phenotyping
    â†’ MSE 1.57 manual vs 4.26 auto
    â†’ Manual es 2.7x mÃ¡s consistente que automÃ¡tico
```

---

## CapÃ­tulo 2: Estado del Arte

### 2.1 Software de Captura en Agricultura

La literatura acadÃ©mica en agricultura de precisiÃ³n utiliza ampliamente smartphones para la captura de imÃ¡genes y video, pero existe una carencia sistemÃ¡tica en la documentaciÃ³n de las herramientas y configuraciones de captura empleadas.

#### 2.1.1 Hallazgos de la revisiÃ³n bibliogrÃ¡fica (Elicit)

La revisiÃ³n sistemÃ¡tica mediante Elicit arrojÃ³ 16 papers sobre captura agrÃ­cola con smartphone, ninguno de los cuales documenta adecuadamente la configuraciÃ³n de captura:

- (Janowski et al., 2021) utilizaron smartphones con GNSS para conteo de manzanas, mencionando solo "smartphones with required image-acquisition accuracy" sin especificar configuraciÃ³n.
- (VÃ©lez et al., 2024) emplearon iPhone X y Xiaomi Poco X3 Pro en viÃ±edos, tomando "high-resolution images of individual plants; geotagged data" sin detallar app ni configuraciÃ³n.
- (Zhao et al., 2023) usaron cÃ¡maras multi-lente de smartphone con mÃ©todo virtual focal para fenotipado de manzanas, documentando el mÃ©todo de calibraciÃ³n pero no la app de captura.
- (Jaramillo et al., 2025) capturaron "videos of the ground under vine rows on a sunny day" con configuraciÃ³n simple no documentada.
- (Zhou et al., 2020) desarrollaron una app propia (KiwiDetector) para detecciÃ³n de kiwi en Huawei P20, pero no utilizaron apps comerciales como Open Camera.

**ConclusiÃ³n de Elicit:** NingÃºn paper agrÃ­cola documenta el uso de apps de captura comerciales (Open Camera, Filmic Pro, MCPro24fps) ni justifica la elecciÃ³n de configuraciÃ³n de cÃ¡mara.

#### 2.1.2 Evidencia complementaria (Semantic Scholar)

La bÃºsqueda en Semantic Scholar identificÃ³ papers que, aunque no documentan apps especÃ­ficas, proporcionan evidencia relevante sobre la necesidad de controlar los parÃ¡metros de captura:

**MediciÃ³n de humedad en arroz con smartphone** (Sensors, 2021). Utilizaron un iPhone 8 con ISO=25 fijo, shutter=1/400s, f/1.8, distancia 27.5 cm, formato JPEG 4032Ã—3024 px, aspecto 4:3, sin luz solar directa y con tabla de calibraciÃ³n de color Spyder Checkr 24. El dato clave es su justificaciÃ³n explÃ­cita: *"To minimize lighting-related factors, the smartphone camera parameters were fixed"* â€” constituyendo una de las pocas justificaciones explÃ­citas en la literatura para fijar parÃ¡metros de cÃ¡mara.

**Monitoreo de cafÃ© con smartphone y sensores inerciales** (Sensors, 2020). Emplearon un Samsung Galaxy S5 SM-G900M en Full-HD 1920Ã—1080, 30 fps, flash apagado, WB e ISO en automÃ¡tico, EV=0, con un holder con botones para enfoque y Ã¡ngulo de 11.3Â°. Usaron sensores inerciales para detectar movimiento y medir blur, desarrollando una app Android propia. Es relevante porque integra IMU + cÃ¡mara, aunque utilizaron modo automÃ¡tico.

**DetecciÃ³n de manzanas con YOLO en smartphone** (2024). Usaron un Redmi Note 7 a distancia 0.3-1.5 m, probando 5 condiciones de luz (directa, lateral, difusa, contraluz, baja luz) con una app Android que ejecutaba YOLOv8n localmente.

**Dataset de cacao con 5 smartphones** (Data, 2023). Utilizaron Samsung Galaxy A01, Samsung Galaxy Note 10, iPhone SE 2020, Motorola G9 plus y LG G5 en horario 8:00-16:00, con trayectoria zigzag entre Ã¡rboles, aspecto 1:1 y resize a 3000Ã—3000 px.

#### 2.1.3 Evidencia cuantitativa sobre la necesidad de control manual

La revisiÃ³n bibliogrÃ¡fica identificÃ³ 14 papers con evidencia cuantitativa que respalda la necesidad de fijar parÃ¡metros de captura:

| Problema | Evidencia | Fuente |
|---|---|---|
| Auto-exposure causa inconsistencia | 85% mÃ¡s variaciÃ³n HSV con auto vs LED fijo | (Choi et al., 2021) |
| Auto-exposure falla en alto rango dinÃ¡mico | Primer plano oscuro al exponer para cielo | (Choi et al., 2021) |
| Manual supera a automÃ¡tico | MSE 1.57 vs 4.26 (manual 2.7x mÃ¡s consistente) | (Autores, 2018) |
| ParÃ¡metros fijos reducen datos necesarios | 4x menos datos de entrenamiento | (Autores, 2021) |
| ExposiciÃ³n inconsistente degrada CNN | Redes no generalizan con exposiciÃ³n variable | (Autores, 2018) |
| Focus hunting degrada calidad | Lente oscila, FoV cambia | (Autores, 2025) |
| Camera2 API necesario para control cientÃ­fico | Tone mapping irreversible. 74% menor MAE con lineal | (Autores, 2023) |
| Luz no controlada destruye detecciÃ³n | F1 0.82 â†’ 0.13 con glare | (Autores, 2020) |
| ISP automÃ¡tico degrada detecciÃ³n YOLO | Contraste/gamma/saturaciÃ³n causan falsos negativos | (Autores, 2023) |
| ParÃ¡metros auto causan fluctuaciÃ³n | 13-14% fluctuaciÃ³n en detecciÃ³n en escenas estÃ¡ticas | (Autores, 2022) |
| ISP pipeline pierde informaciÃ³n Ãºtil | 7.1% mÃ¡s precisiÃ³n entrenando en RAW vs ISP-processed | (Autores, 2022) |
| ISP default es sub-Ã³ptimo para detecciÃ³n | 28% mejora con AdaptiveISP vs ISP default | (Autores, 2024) |

**Papers crÃ­ticos en detalle:**

**Paper LED + exposiciÃ³n fija** (Computers and Electronics in Agriculture, 2021). DemostrÃ³ que la iluminaciÃ³n LED controlada con exposiciÃ³n fija reduce la variaciÃ³n HSV en un **85%** frente a la auto-exposiciÃ³n. El error de motion blur se redujo de 7 mm a 1 mm a 7 km/h con flash sincronizado. La auto-exposiciÃ³n fallÃ³ catastrÃ³ficamente cuando el sol estaba frontal a la cÃ¡mara. ConclusiÃ³n: los parÃ¡metros fijos mÃ¡s iluminaciÃ³n controlada eliminan casi toda la variabilidad.

**Phenotyping â€” Manual vs Auto** (Plant Methods, 2018). ComparÃ³ directamente exposiciÃ³n manual vs automÃ¡tica en condiciones de campo cambiantes. El error cuadrÃ¡tico medio fue de **1.57 (manual) vs 4.26 (auto)**, demostrando que la exposiciÃ³n manual es **2.7x mÃ¡s consistente** que la automÃ¡tica.

**Illumination-Invariant Camera System** (arXiv, 2021). DemostrÃ³ que las redes entrenadas con imÃ¡genes consistentes requieren **4x menos datos** para alcanzar el mismo rendimiento. El Average Precision en condiciones de luz extrema fue de 0.71 con iluminaciÃ³n controlada frente a **casi 0** con luz natural.

**Camera2 API para investigaciÃ³n** (Frontiers in Digital Health, 2023). EstableciÃ³ que el tone mapping automÃ¡tico aplica transformaciones **no lineales irreversibles** que *"cannot be reversed in post processing"*. La Camera2 API de Android permite configurar tone mapping lineal, logrando un **74% menor MAE** frente al modo automÃ¡tico por defecto. iOS no ofrece control equivalente sobre el tone mapping en video.

**Impacto del ISP en detecciÃ³n** (MDPI J. Imaging, 2023). DemostrÃ³ que el contraste, gamma y saturaciÃ³n del pipeline ISP automÃ¡tico causan **degradaciÃ³n significativa** en YOLOv5/v8, Faster R-CNN y RT-DETR. Los objetos pequeÃ±os son los mÃ¡s afectados, y la mayorÃ­a de los errores introducidos son **falsos negativos**.

**La cÃ¡mara como "unintentional adversary"** (ECCV, 2022). DemostrÃ³ que los cambios automÃ¡ticos de parÃ¡metros de cÃ¡mara causan un **13-14% de fluctuaciÃ³n** en el conteo de detecciones sobre escenas estÃ¡ticas. El modelo original YOLOv5 generÃ³ **157 track-IDs** frente a 94 con transfer-learning (**40.1% menos errores** en tracking).

**DetecciÃ³n en RAW** (ISP-less CV, 2022). ConfirmÃ³ que entrenar modelos en dominio RAW supera en **7.1% de precisiÃ³n** a las imÃ¡genes procesadas por el pipeline ISP, demostrando que el ISP automÃ¡tico pierde informaciÃ³n Ãºtil para detecciÃ³n.

**AdaptiveISP** (NeurIPS, 2024). EstableciÃ³ que el pipeline ISP puede optimizarse especÃ­ficamente para detecciÃ³n, logrando un **28% mejor mAP** (71.4 vs 55.6) al adaptar el procesamiento a la tarea de visiÃ³n computacional, confirmando que el ISP por defecto es sub-Ã³ptimo.

### 2.2 IMU y EstabilizaciÃ³n en Video AgrÃ­cola

#### 2.2.1 EstabilizaciÃ³n con IMU

La literatura sobre estabilizaciÃ³n de video basada en sensores inerciales (IMU) proporciona respaldo cuantitativo para el uso de giroscopio y acelerÃ³metro en la correcciÃ³n de movimiento durante la captura:

(Han et al., 2021) reportaron una **mejora del 32%** en estabilizaciÃ³n mediante fusiÃ³n de giroscopio y visiÃ³n, con una latencia de 32.6 ms, probado en condiciones de caminata. (Li et al., 2025) alcanzaron un **47.8% de mejora en SSIM** y 37% mÃ¡s rapidez combinando giroscopio, clustering y profundidad relativa.

En cuanto a correcciÃ³n de rolling shutter con IMU, (Zhang & Zhang, 2023) demostraron que la IMU de alta frecuencia en telÃ©fonos Android supera al estado del arte en precisiÃ³n y costo computacional.

#### 2.2.2 Frecuencia de muestreo IMU

(Fan et al., 2025) resolvieron la pregunta de frecuencia de muestreo Ã³ptima para aplicaciones agrÃ­colas: **100 Hz es suficiente** para walking (1.2 m/s), mientras que frecuencias superiores a 100 Hz no mejoran la precisiÃ³n en orientaciÃ³n. Para running (2.2 m/s) se requieren 200 Hz, y el acelerÃ³metro por encima de 100 Hz **degrada la precisiÃ³n** al introducir error por aceleraciones distorsionadas.

Esta frecuencia ha sido validada por mÃºltiples estudios de anÃ¡lisis de marcha con smartphone, que confirman que el IMU del smartphone a 100 Hz es vÃ¡lido con ICC > 0.8 frente a gold-standard.

#### 2.2.3 Evidencia sobre OIS y estabilizaciÃ³n

**DeepOIS** (arXiv, 2021) demostrÃ³ que el OIS (Optical Image Stabilization) interfiere con la estabilizaciÃ³n basada en giroscopio: el error de alineaciÃ³n es de **0.688 sin OIS** frente a **1.038 con OIS (50% peor)**. La conclusiÃ³n textual establece que *"OIS terminates the possibility of image registration by gyros"*.

**ISPRS** (2022) corroborÃ³ desde la fotogrametrÃ­a que la estabilizaciÃ³n integrada degrada la precisiÃ³n: la incertidumbre en los parÃ¡metros es **hasta 300% mayor** y el error de reproyecciÃ³n **4x mayor** con la estabilizaciÃ³n activada.

**Video estabilizado vs fotos estÃ¡ticas.** (Autores, 2019) demostraron que la detecciÃ³n con video en movimiento alcanzÃ³ el **62.3%** del conteo real de cosecha, frente a solo el **40.2%** con foto estÃ¡tica, una **mejora absoluta del +22%**.

**Impacto del motion blur en YOLO.** (Autores, 2025) reportaron que el **mAP@0.5:0.95 mejora un 86.4%** tras restaurar imÃ¡genes borrosas de cÃ­tricos, con incrementos del +76.9% en recall, +40.1% en F1 y reducciÃ³n del -63.9% en falsos negativos. Es importante seÃ±alar que esta cifra representa una mejora relativa, y la degradaciÃ³n real por blur se sitÃºa en el rango del 15-50% segÃºn el modelo YOLO utilizado.

**EstabilizaciÃ³n en agricultura.** (Autores, s.f.) reportaron que la estabilizaciÃ³n de video en hileras de cultivo suprimiÃ³ el **66%** del desplazamiento lateral, reduciendo la desviaciÃ³n promedio de 93 a aproximadamente 20 pÃ­xeles.

### 2.3 Protocolos de Captura en Campo

La literatura sobre protocolos de captura en agricultura se organiza en torno a seis parÃ¡metros fundamentales. A continuaciÃ³n se presentan las evidencias recopiladas para cada uno.

#### 2.3.1 Velocidad de Caminata

| Paper | Velocidad | Contexto | Resultado |
|---|---|---|---|
| (Roy et al., 2018) | **2 m/s (7.2 km/h)** | Samsung Galaxy S4, video 30fps, 1920Ã—1080, tractor | Yield accuracy 95.56-97.83% |
| (Autores, 2019) | **5 km/h (~1.39 m/s)** | VehÃ­culo a 10 fps, 2 m de distancia | 62% harvest count, RMSE 18.0 frutos/Ã¡rbol |
| (Autores, 2023) | **0.052/0.069/0.098 m/s** | Tractor con cÃ¡mara 3D, 3 Ã¡ngulos | Counting accuracy 86.6% |
| (Ramos Giraldo et al., 2017) | **~3 cm/s** | Smartphone + IMU para detecciÃ³n de blur | MÃ¡x 5 cm/s para evitar blur |
| (Autores, 2025) | Efecto del blur | Cuantifica caÃ­da de mAP por motion blur | mAP cae 27% por blur |

#### 2.3.2 Ãngulo de CÃ¡mara

(Hemming et al., 2014) realizaron el estudio mÃ¡s completo, probando **14 posiciones de cÃ¡mara** en pimiento dulce con diferentes Ã¡ngulos azimuth y zenith para medir la Fruit Detectability (FD). El Ã¡ngulo **zenith 60Â° (30Â° hacia arriba)** dio la mejor FD como posiciÃ³n Ãºnica (FD mÃ¡xima 66%), mientras que la combinaciÃ³n de 5 posiciones alcanzÃ³ un FD del 90%. El Ã¡ngulo zenith 120Â° (mirando hacia abajo) fue el peor, ya que las hojas ocultan los frutos.

(Autores, 2023) probaron Ã¡ngulos de 0Â°, 15Â° y 30Â° en manzanas con cÃ¡mara 3D, encontrando que **15Â°** proporcionÃ³ el menor RMSE (1.54 cm). (Wang et al., 2018) establecieron un lÃ­mite de **<14Â°** de inclinaciÃ³n para la app FruitSize, por encima del cual el error de tamaÃ±o supera el 6%.

#### 2.3.3 Distancia al Dosel

| Paper | Distancia probada | Resultado |
|---|---|---|
| (Autores, 2026) | **0.8-1.5 m** (rango Ã³ptimo) | mAP 93.69% |
| (Autores, 2020) | **1.5 m vs 2.5 m** | 1.5 m: 200.5% mÃ¡s densidad de nube de puntos |
| (Kuznetsova et al., 2020) | **0.2 / 0.5 / 1.0 / 2.0 m** | Distancia Ã³ptima depende del FOV |
| (Zhou et al., 2020) | **~1 m** (selfie stick) | TDR 90.8% |
| (Autores, 2025) | **0.3-1.5 m** | Bueno para detecciÃ³n, 5 condiciones de luz |

#### 2.3.4 Horario e IluminaciÃ³n

| Paper | Condiciones comparadas | Mejor condiciÃ³n | Resultado |
|---|---|---|---|
| (Autores, 2026) | Â±50% brillo + hasta 70% oclusiÃ³n | Normal: 94.8% mAP. Extrema: 61.4% |
| (Li et al., 2023) | 4 horarios: 7-8AM, 10-11AM, 2-3PM, 6-7PM | MÃºltiples horarios viables |
| (Restrepo-Arias et al., 2023) | 8AM-4PM, trayectoria zigzag | Rango completo usable |
| (Autores, 2020) | Normal vs glare vs overexposed | Normal: F1 0.82. Glare: F1 0.13 |

#### 2.3.5 Motion Blur y Shutter Speed

(Autores, 2024) proporcionaron la revisiÃ³n mÃ¡s completa, incluyendo la fÃ³rmula de desplazamiento por blur: `desplazamiento (px) â‰ˆ (velocidad_caminata Ã— tiempo_exposiciÃ³n) / distancia_focal`. (Autores, 2025) cuantificaron que el **mAP@0.5 cae un 27.2%** (de 0.925 a 0.673) por motion blur en huerto de cÃ­tricos.

#### 2.3.6 Anti-Doble Conteo y Tracking

(GenÃ©-Mola et al., 2023) compararon SORT, DeepSORT y ByteTrack para conteo de frutos en video, encontrando que ByteTrack ofrece el mejor rendimiento: **MOTA 0.682, IDF1 0.837, HOTA 0.689**, con 15 ms/frame frente a los 128 ms de DeepSORT. (Autores, 2019) demostraron que el tracking con Kalman Filter + Hungarian Algorithm alcanzÃ³ el **62%** del conteo de cosecha frente al 40% con foto dual estÃ¡tica.

### 2.4 SelecciÃ³n de Parcelas y Muestreo en Huertos Frutales

La selecciÃ³n de unidades de muestreo en huertos frutales requiere mÃ©todos estadÃ­sticos que maximicen la representatividad con el mÃ­nimo esfuerzo de campo. La literatura ofrece diversas estrategias documentadas.

#### 2.4.1 Muestreo Aleatorio Simple (MAS/SRS)

El Muestreo Aleatorio Simple constituye el diseÃ±o de muestreo mÃ¡s fundamental, donde cada unidad tiene la misma probabilidad de ser seleccionada. (Miranda et al., 2018) y (Uribeetxebarria et al., 2018) lo utilizaron como lÃ­nea base para comparar la eficiencia de mÃ©todos mÃ¡s complejos en huertos frutales. Sin embargo, con solo 4 parcelas disponibles, la selecciÃ³n aleatoria podrÃ­a resultar en unidades con vigor muy similar, perdiendo la representatividad de los extremos.

#### 2.4.2 Muestreo Estratificado con NDVI

(Miranda et al., 2018) y (Uribeetxebarria et al., 2018) aplicaron muestreo estratificado con NDVI en huertos de durazno utilizando imÃ¡genes aÃ©reas de muy alta resoluciÃ³n (0.25 m), logrando reducciones del tamaÃ±o de muestra entre el 17% y el 35%. (ArnÃ³ et al., 2017) demostraron que la estratificaciÃ³n por NDVI es significativamente mÃ¡s eficiente que el muestreo aleatorio simple, y que con solo 2 estratos se captura la mayor parte de la variabilidad entre parcelas.

El mÃ©todo **NDVI3** desarrollado por (Meyers et al., 2020) demostrÃ³ que 3 pÃ­xeles seleccionados estratÃ©gicamente en las colas de la distribuciÃ³n del NDVI (cola baja, media y alta) alcanzan la misma representatividad que 20 puntos seleccionados aleatoriamente.

#### 2.4.3 Muestreo SistemÃ¡tico Uniforme (SUR)

(Wulfsohn et al., 2012) validaron empÃ­ricamente el SUR en 14 huertos comerciales de kiwi, manzana y uva, reportando errores de estimaciÃ³n inferiores al 10% en 11 de los 14 huertos evaluados. Este mÃ©todo es particularmente adecuado para poblaciones con autocorrelaciÃ³n espacial, como las hileras de un huerto.

#### 2.4.4 AplicaciÃ³n a cÃ­tricos con Sentinel-2

(Autores, 2022) utilizaron el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de cÃ­tricos (mandarina Afourer), demostrando que el Ã­ndice captura robustamente la variabilidad de vigor entre parcelas. (Autores, 2024) compararon Sentinel-2 (10 m) frente a UAV (3-4 cm) para zonificaciÃ³n de vigor, concluyendo que Sentinel-2 captura las principales zonas de vigor a nivel de parcela de manera comparable al UAV. En mandarinos especÃ­ficamente, (Sun et al., 2026) reportaron RÂ² = 0.85 para la estimaciÃ³n de LAI con Sentinel-2.

### 2.5 Gap de InvestigaciÃ³n Confirmado

El anÃ¡lisis bibliogrÃ¡fico realizado confirma que **no existe un paper agrÃ­cola que documente el flujo completo** (app de captura + configuraciÃ³n de cÃ¡mara + registro IMU + pipeline de procesamiento) para detecciÃ³n de frutos en video con smartphone.

Los gaps especÃ­ficos identificados son:

1. **Software de captura:** Solo 1 paper en toda la literatura (Autores, 2024, fenotipado de hojas) documenta Open Camera v1.52 con configuraciÃ³n detallada. NingÃºn paper documenta el flujo completo app + configuraciÃ³n + IMU + pipeline para detecciÃ³n de frutos en video.
2. **IMU â†’ YOLO mAP:** No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en mÃ©tricas YOLO (mAP) o MOT (MOTA) para video agrÃ­cola.
3. **ParÃ¡metros combinados:** No existe un paper que compare la interacciÃ³n de velocidad Ã— Ã¡ngulo Ã— distancia combinados para captura manual con smartphone en agricultura, midiendo el impacto en mAP/MOTA.
4. **SelecciÃ³n de parcelas:** No existe un protocolo documentado que integre la selecciÃ³n de parcelas por NDVI satelital con un pipeline completo de captura para cÃ­tricos.

**ContribuciÃ³n original de esta investigaciÃ³n:** Documentar y medir cuantitativamente el impacto de todas estas decisiones en mAP/MOTA para video de mandarinas capturado con smartphone, comparando el protocolo propuesto frente a la cÃ¡mara nativa en modo automÃ¡tico (experimento A/B).

---

## CapÃ­tulo 3: MetodologÃ­a

### 3.1 Software de Captura y Bloqueo de Sensores (P1)

#### 3.1.1 IntroducciÃ³n y FundamentaciÃ³n

El primer paso del pipeline de captura consiste en seleccionar y configurar la aplicaciÃ³n de cÃ¡mara que permita el control manual de los parÃ¡metros de exposiciÃ³n, enfoque y balance de blancos. La literatura demuestra que la cÃ¡mara nativa de los smartphones en modo automÃ¡tico introduce variabilidad perjudicial para la consistencia de los datasets de visiÃ³n computacional.

La evidencia cuantitativa acumulada respalda sÃ³lidamente el control manual: la exposiciÃ³n fija reduce la variaciÃ³n HSV en un 85% (Choi et al., 2021), el modo manual es 2.7x mÃ¡s consistente que el automÃ¡tico en condiciones de campo (Autores, 2018), y las redes entrenadas con imÃ¡genes consistentes requieren 4x menos datos (Autores, 2021).

#### 3.1.2 AnÃ¡lisis de Aplicaciones de Captura

Se evaluaron cuatro aplicaciones profesionales para smartphone:

| App | Precio | AF Lock | AE Lock | WB Lock | ISO manual | Shutter manual | Perfil Log | Control gimbal | Bitrate |
|---|---|---|---|---|---|---|---|---|---|
| **Open Camera** | **Gratis** | âœ… | âœ… | âœ… | âœ… | âœ… | âŒ | âŒ | âœ… Configurable |
| Filmic Pro | ~$5/semana | âœ… | âœ… | âœ… | âœ… | âœ… | âœ… V-Log | âœ… DJI/Zhiyun | 100 Mbps |
| MCPro24fps | ~$20 | âœ… | âœ… | âœ… | âœ… | âœ… | âœ… MÃºltiples | âŒ | Hasta 500 Mbps |
| Blackmagic Cam | Gratis | âœ… | âœ… | âœ… | âœ… | âœ… | âœ… | âŒ | Alto |

**DecisiÃ³n fundamental: Open Camera es la aplicaciÃ³n seleccionada** por las siguientes razones:

1. **Costo $0** â€” cualquier investigador puede reproducir el protocolo sin barrera econÃ³mica
2. **Control manual completo** vÃ­a Camera2 API (ISO, shutter, AF Lock, AE Lock, WB Lock, bitrate configurable)
3. **Open-source** (SourceForge) â€” el cÃ³digo puede ser citado y verificado
4. **Sin suscripciÃ³n** â€” a diferencia de Filmic Pro (subiÃ³ a ~$5/semana en 2022)
5. **Ãšnica app gratuita** que ofrece bloqueo simultÃ¡neo de AF, AE y WB

Open Camera permite el bloqueo de los tres parÃ¡metros crÃ­ticos (AF Lock, AE Lock, WB Lock), el control manual de ISO y shutter speed, y la configuraciÃ³n del bitrate para calidad constante. Requiere soporte de Camera2 API, que no todos los dispositivos Android ofrecen.

#### 3.1.3 Evidencia Adicional (Papers P95-P99)

**ISP Tuning y DegradaciÃ³n de DetecciÃ³n** (Autores, 2023). El procesamiento automÃ¡tico del ISP (Image Signal Processor) â€”especÃ­ficamente contraste, gamma y saturaciÃ³nâ€” causa degradaciÃ³n significativa en YOLOv5/v8, Faster R-CNN y RT-DETR. Los objetos pequeÃ±os son los mÃ¡s afectados, y la mayorÃ­a de los errores introducidos son falsos negativos. Esto es crÃ­tico para mandarinas en huerto denso.

**La CÃ¡mara como "Unintentional Adversary"** (Autores, 2022). Los cambios automÃ¡ticos de parÃ¡metros de cÃ¡mara causan un 13-14% de fluctuaciÃ³n en detecciÃ³n incluso en escenas estÃ¡ticas. El modelo original YOLOv5 generÃ³ 157 track-IDs frente a 94 con transfer-learning (40.1% menos errores en tracking). El simple hecho de usar modo automÃ¡tico introduce ruido en la mediciÃ³n.

**DetecciÃ³n en RAW supera a RGB procesado** (Autores, 2022). Entrenar modelos en dominio RAW proporciona un 7.1% mÃ¡s de precisiÃ³n que con imÃ¡genes procesadas por ISP. El pipeline ISP pierde informaciÃ³n Ãºtil para detecciÃ³n debido a las distorsiones no lineales que introduce.

**ISP por defecto no es Ã³ptimo para detecciÃ³n** (Autores, 2024). AdaptiveISP logra un 28% mejor mAP (71.4 vs 55.6) al optimizar el pipeline ISP especÃ­ficamente para detecciÃ³n. Incluso si el ISP automÃ¡tico produce imÃ¡genes "bonitas" para el ojo humano, no estÃ¡n optimizadas para YOLO.

#### 3.1.4 Tabla Resumen: QuÃ© Hacer vs QuÃ© Evitar

| âœ… Hacer (Recomendado) | âŒ Evitar (No recomendado) | Respaldo bibliogrÃ¡fico |
|---|---|---|
| Bloquear AE/AF/WB | Dejar parÃ¡metros en automÃ¡tico (causa fluctuaciÃ³n 13-14%) | (Choi et al., 2021); (Autores, 2018); (Autores, 2022) |
| Fijar ISO en 200 (100 solo si hay suficiente luz) | ISO automÃ¡tico (varÃ­a entre frames, degrada consistencia) | (Autores, 2024); (Autores, 2021) |
| Fijar shutter en 1/100 s (rango 1/60-1/120) | Shutter automÃ¡tico (cambia exposiciÃ³n frame a frame) | (Autores, 2024); (Autores, 2024) |
| Usar tone mapping lineal (Camera2 API) | Tone mapping automÃ¡tico (transformaciones no lineales irreversibles) | (Autores, 2023) |
| Usar Open Camera (gratis, open-source, Camera2 API) | App nativa del fabricante (no permite bloquear parÃ¡metros) | (Autores, 2024) |
| Deshabilitar OIS si se usa Gyroflow | OIS activo con estabilizaciÃ³n basada en giroscopio | (Autores, 2021); (Autores, 2022) |
| Mantener distancia constante al dosel (0.5-1.5 m) | Cambiar distancia entre tomas (afecta resoluciÃ³n del fruto) | (Kuznetsova et al., 2020) |
| Procesar en RAW si es posible (7.1% mÃ¡s precisiÃ³n) | Confiar en el ISP por defecto (pierde informaciÃ³n Ãºtil) | (Autores, 2022) |
| Optimizar ISP para detecciÃ³n (no para ojo humano) | Usar pipeline ISP default (sub-Ã³ptimo para YOLO, 28% menos mAP) | (Autores, 2024) |

#### 3.1.5 DiscusiÃ³n: Nuevo Paradigma de DetecciÃ³n Robusta (2024-2026)

Es importante reconocer que entre 2024 y 2026 han surgido detectores (Orchard-YOLO 2026, YOLO-PBGM 2025) que logran >94% mAP incluso con variaciones de iluminaciÃ³n de Â±50%, mediante tÃ©cnicas como data augmentation con exposiciÃ³n randomizada, mecanismos de atenciÃ³n (GAM, CBAM) y aprendizaje de features illumination-invariant.

Sin embargo, esto NO invalida el control de captura por las siguientes razones:

1. **Ambos paradigmas son complementarios:** Controlar la captura mÃ¡s entrenar modelos robustos deberÃ­a dar el mejor resultado
2. **No hay experimento que compare:** Precisamente, el experimento A/B de esta tesis (Protocolo vs CÃ¡mara Nativa) es lo que falta en la literatura
3. **Escenario extremo:** El huerto denso de mandarinas (frutos pequeÃ±os, alta oclusiÃ³n, follaje denso) es mÃ¡s desafiante que los escenarios donde se probaron esos modelos
4. **El ISP sigue siendo un problema:** Aunque el detector sea robusto a iluminaciÃ³n, el tone mapping, gamma y saturaciÃ³n del ISP automÃ¡tico siguen degradando la informaciÃ³n (Autores, 2023); (Autores, 2022); (Autores, 2022)

#### 3.1.6 Nota sobre los Valores Propuestos vs Documentados en Papers

Los valores especÃ­ficos propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120 s) **no son valores extraÃ­dos directamente de un paper**, sino decisiones del protocolo basadas en el principio de "usar el valor mÃ­nimo prÃ¡ctico para condiciones de campo". Los papers consultados usaron valores distintos segÃºn sus condiciones especÃ­ficas:

| Valor documentado en paper | Paper | Condiciones de ese paper |
|---|---|---|
| ISO=25, shutter=1/400 s | (Autores, 2021) Rice GMC | iPhone 8, laboratorio, tabla de calibraciÃ³n Spyder Checkr 24 |
| ISO=200, shutter=1/100 s | (Autores, 2024) Open Camera | Redmi Note 7 Pro, iluminaciÃ³n LED 4000K, 50 cm distancia |
| ExposiciÃ³n ~250 Âµs (~1/4000 s) | (RanÃ§on et al., 2023) Vineyard | CÃ¡mara industrial Basler Ace, flash xenon sincronizado |
| ExposiciÃ³n 200 Âµs (~1/5000 s) | (Choi et al., 2021) LEDs | CÃ¡mara industrial con LED overcurrent-driven 6Ã— |

El protocolo propone **ISO 100-200** porque ISO=200 estÃ¡ documentado como valor funcional en campo (Autores, 2024), e ISO=100 es el mÃ­nimo prÃ¡ctico en exteriores sin llegar a ISO=25 (que requiere condiciones controladas de laboratorio).

El protocolo propone **shutter 1/60-1/120 s** porque 1/100 s estÃ¡ documentado, y el rango es un compromiso entre: (a) un shutter lo suficientemente rÃ¡pido para evitar motion blur al caminar (~8-16 px a 1 m/s), y (b) un shutter lo suficientemente lento para capturar suficiente luz sin flash en exteriores.

> **ConclusiÃ³n:** Los valores del protocolo son una decisiÃ³n de ingenierÃ­a informada por la literatura, no un valor extraÃ­do directamente de un paper. El experimento A/B (Protocolo vs CÃ¡mara Nativa) validarÃ¡ si esta decisiÃ³n es adecuada.

#### 3.1.7 LimitaciÃ³n: Protocolo Solo para Android

El presente protocolo de captura **solo es aplicable a dispositivos Android** que soporten Camera2 API. La razÃ³n es que iOS (AVFoundation) **no expone control sobre el tone mapping** de la cÃ¡mara, segÃºn lo documentado por (Autores, 2023):

> *"It is only possible to manually set the camera tone mapping to linear within the Android Camera 2 API. Such an option is not available in iOS. Although it is possible to capture RAW photos using iOS AVFoundation, the RAW capture mode is not possible for video recordings necessary for cPPG measurements."*

Esto implica que:
- En **Android**: Se puede usar Camera2 API para configurar tone mapping lineal, bloquear AF/AE/WB y controlar ISO/shutter manualmente.
- En **iOS**: No es posible controlar el tone mapping en video. La cÃ¡mara nativa de iOS aplica transformaciones no lineales irreversibles.

**RecomendaciÃ³n para iOS:** Bloquear AE/AF/WB si la app lo permite, usar la resoluciÃ³n mÃ¡s alta disponible y bitrate mÃ¡ximo. Los resultados del experimento A/B pueden no ser directamente transferibles entre plataformas.

#### 3.1.8 Gap Confirmado

> Solo 1 paper en toda la literatura (Autores, 2024, fenotipado de hojas) documenta Open Camera v1.52 con configuraciÃ³n detallada. NingÃºn paper documenta el flujo completo (app + configuraciÃ³n + IMU + pipeline) para detecciÃ³n de frutos en video. Esta es la contribuciÃ³n original de esta investigaciÃ³n: documentar y medir cuantitativamente el impacto de estas decisiones en mAP/MOTA para video de mandarinas.

### 3.2 Registro de TelemetrÃ­a IMU (P2)

#### 3.2.1 IntroducciÃ³n y FundamentaciÃ³n

El segundo componente del pipeline consiste en registrar datos de sensores inerciales (IMU) durante la captura de video, especÃ­ficamente giroscopio (velocidad angular en X, Y, Z) y acelerÃ³metro (aceleraciÃ³n lineal), utilizando la aplicaciÃ³n Sensor Logger ejecutÃ¡ndose en segundo plano durante la caminata por el huerto.

El propÃ³sito de este registro es capturar la firma del movimiento humano para su uso en post-producciÃ³n (estabilizaciÃ³n Gyroflow, deblurring, correcciÃ³n de rolling shutter).

#### 3.2.2 Evidencia sobre EstabilizaciÃ³n con IMU

(Han et al., 2021) demostraron que la fusiÃ³n de giroscopio y visiÃ³n para estabilizaciÃ³n logra una **mejora del 32%** sobre el estado del arte, con una latencia de 32.6 ms, probado en condiciones de caminata, escalada y paseo en vehÃ­culo. (Li et al., 2025) alcanzaron un **47.8% de mejora en SSIM** y 37% mÃ¡s rapidez combinando giroscopio, clustering y profundidad relativa.

#### 3.2.3 Frecuencia de Muestreo IMU

(Fan et al., 2025) establecieron que **100 Hz es suficiente** para aplicaciones de walking (1.2 m/s). Frecuencias superiores a 100 Hz no mejoran la precisiÃ³n en orientaciÃ³n, y el acelerÃ³metro por encima de 100 Hz degrada la precisiÃ³n al introducir error por aceleraciones distorsionadas. Esta frecuencia ha sido validada por mÃºltiples estudios de anÃ¡lisis de marcha con smartphone (ICC > 0.8 frente a gold-standard).

#### 3.2.4 OIS Debe Estar Desactivado

**DeepOIS** (Autores, 2021) demostrÃ³ que el OIS interfiere con la estabilizaciÃ³n basada en giroscopio: el error de alineaciÃ³n sin OIS es de 0.688 frente a 1.038 con OIS (50% peor). La conclusiÃ³n textual establece: *"OIS terminates the possibility of image registration by gyros"*.

**ISPRS** (Autores, 2022) corroborÃ³ desde la fotogrametrÃ­a que la estabilizaciÃ³n integrada debe desactivarse: la incertidumbre en parÃ¡metros es hasta 300% mayor y el error de reproyecciÃ³n 4x mayor con la estabilizaciÃ³n activada.

#### 3.2.5 Evidencia Cuantitativa Adicional

**Video estabilizado vs fotos estÃ¡ticas** (Autores, 2019): La detecciÃ³n con video en movimiento alcanzÃ³ el 62.3% del conteo real de cosecha frente al 40.2% con foto estÃ¡tica (+22% de mejora absoluta).

**Motion blur + YOLO** (Autores, 2025): El mAP@0.5:0.95 mejora un 86.4% tras restaurar imÃ¡genes borrosas de cÃ­tricos (recall +76.9%, F1 +40.1%). La degradaciÃ³n real por blur se sitÃºa en el rango del 15-50% segÃºn el modelo.

**EstabilizaciÃ³n en agricultura** (Autores, s.f.): SupresiÃ³n del 66% del desplazamiento lateral entre hileras, con desviaciÃ³n reducida de 93 a ~20 pÃ­xeles.

#### 3.2.6 Tabla Resumen de Evidencia â€” Paso 2

| DecisiÃ³n | Respaldo | Tipo de fuente |
|---|---|---|
| Registrar IMU durante captura | EstabilizaciÃ³n IMU supera a Ã³ptica en walking (32% mejor) | (Han et al., 2021) |
| 100 Hz es suficiente | Paper especÃ­fico sobre sampling rate vs walking speed | (Fan et al., 2025) |
| Usar Gyroflow en post-procesamiento | DocumentaciÃ³n oficial, 8.9k stars GitHub, plugins DaVinci/Adobe | DocumentaciÃ³n tÃ©cnica [D2][D5] |
| Usar Sensor Logger | Listado en docs de Gyroflow como fuente compatible | DocumentaciÃ³n tÃ©cnica [D3] |
| OIS debe estar desactivado | DeepOIS: 50% peor alineaciÃ³n. ISPRS: 300% mÃ¡s incertidumbre | (Autores, 2021); (Autores, 2022) |
| IMU mejora rolling shutter | 3 papers con resultados cuantitativos | (Zhang & Zhang, 2023) |
| IMU mejora deblurring | 5% PSNR gain, 19% menos cÃ³mputo | (Arslan et al., 2024) |
| Video estabilizado vs fotos | MangoYOLO: +22% detecciÃ³n con video | (Autores, 2019) |
| Motion blur + YOLO | Citrus GAN: 86.4% mAP de mejora tras deblurring | (Autores, 2025) |
| EstabilizaciÃ³n en agricultura | Crop row: 66% supresiÃ³n desplazamiento | (Autores, s.f.) |

#### 3.2.7 Evidencia Contradictoria y Matices

**OIS Debe Estar OFF â€” Matiz importante.** La regla "OIS OFF" se matiza con evidencia de sistemas modernos: Qualcomm (US20200412954A1, 2024) combina OIS+EIS exitosamente usando sensores Hall para leer la posiciÃ³n del lente. El Google Pixel 2 demostrÃ³ un sistema hÃ­brido que fusiona datos del giroscopio con posiciÃ³n OIS mediante ML. HyperOIS (IEEE TCE, 2024) integrÃ³ OIS avanzado con plataforma smartphone (SR -34.37 dB a -26.90 dB). Sin embargo, la regla "OIS OFF" se mantiene para este pipeline porque **Sensor Logger es una fuente externa** â€” no tenemos acceso a los sensores Hall del lente para compensar OIS.

**Frecuencia de 100 Hz â€” Suficiente pero con lÃ­mites.** (Torun et al., 2021) encontraron que 100 Hz es inadecuado para parÃ¡metros espaciales de marcha (250 Hz Ã³ptimo). Sin embargo, esto no aplica a esta tesis porque no estimamos stride length ni velocidad, solo orientaciÃ³n para sincronizaciÃ³n video-IMU.

**Motion Blur + YOLO â€” El 86.4% es engaÃ±oso.** El paper Citrus GAN reporta una mejora relativa del 86.4% tras deblurring. La degradaciÃ³n real por blur es de aproximadamente 15-50% segÃºn el modelo (Autores, 2026); (Autores, 2024); (Autores, 2025). YOLOv4 tiene mejor robustez a blur que YOLOv8-v11, lo que contradice la intuiciÃ³n de que versiones mÃ¡s nuevas son mÃ¡s robustas.

**IMU supera a Ã³ptica â€” Desactualizado.** La afirmaciÃ³n de (Bell et al., 2014) de que el giroscopio supera a mÃ©todos basados en features ha sido superada por mÃ©todos hÃ­bridos (DeepFused, WACV 2022: 0.853 de estabilidad) y deep learning 3D (RStab, CVPR 2024: 0.92 de estabilidad). Gyroflow, al ser un sistema hÃ­brido (IMU + correcciÃ³n de lente + rolling shutter), representa el enfoque correcto.

**Rolling Shutter Correction â€” Beneficio para geometrÃ­a, no para detecciÃ³n.** (Autores, 2024) demostraron que la correcciÃ³n de rolling shutter **no es necesaria** para detecciÃ³n de objetos a IoUâ‰¥0.5. Es posible que desactivarla en Gyroflow no degrade el mAP, o incluso lo mejore al evitar artefactos.

#### 3.2.8 Gap Confirmado

> No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en mÃ©tricas YOLO (mAP) o MOT (MOTA) para video agrÃ­cola. Los repositorios existentes (zhouzypaul/object-recognition-imu, Brown 2022) realizan post-procesamiento, no pre-procesamiento. El gap se confirma, aunque la magnitud del efecto es incierta â€” un resultado modesto sigue siendo una contribuciÃ³n cientÃ­fica vÃ¡lida.

### 3.3 Protocolo de Caminata y Captura (P3)

El protocolo de caminata constituye el nÃºcleo operativo de la captura en campo. Se definen seis parÃ¡metros fundamentales, cada uno con su respaldo bibliogrÃ¡fico y la evidencia contradictoria documentada.

#### Resumen de ParÃ¡metros

| ParÃ¡metro | Valor recomendado | Respaldo principal | Confianza |
|---|---|---|---|
| Velocidad de caminata | ~0.5-1.0 m/s | (Roy et al., 2018); (Autores, 2019); (Autores, 2024) | Alta |
| Ãngulo de cÃ¡mara | 15-30Â° hacia arriba | (Hemming et al., 2014); (Autores, 2023) | Alta |
| Distancia al dosel | 0.8-1.5 m | (Autores, 2026); (Autores, 2020); (Kuznetsova et al., 2020) | Alta |
| Horario / IluminaciÃ³n | 9-11 AM o 3-5 PM. Nublado ideal. | (Li et al., 2023); (Restrepo-Arias et al., 2023); (Autores, 2026) | Alta |
| Shutter speed | 1/60-1/120 s | (Autores, 2024); (Autores, 2025); (Kurtser et al., s.f.) | Alta |
| Estrategia anti-doble conteo | ByteTrack + multi-view | (GenÃ©-Mola et al., 2023) | Alta |

##### 3.3.1 Velocidad de Caminata

**Evidencia principal.** La velocidad de aproximadamente 1 m/s se establece como valor conservador para caminata manual. (Roy et al., 2018) demostraron que incluso a 2 m/s es factible con un Samsung Galaxy S4, logrando una precisiÃ³n de rendimiento del 95.56-97.83%. (Autores, 2019) reportaron un 62% de detecciÃ³n de cosecha a 1.39 m/s (5 km/h). La fÃ³rmula de blur (Autores, 2024) permite calcular el desplazamiento en pÃ­xeles como funciÃ³n de la velocidad, tiempo de exposiciÃ³n y distancia focal:

```
desplazamiento (px) â‰ˆ (velocidad_caminata Ã— tiempo_exposiciÃ³n) / distancia_focal
Ejemplo a 1 m/s con shutter 1/60 s: ~16 px de blur
Ejemplo a 1 m/s con shutter 1/120 s: ~8 px de blur
```

**Evidencia contradictoria.** (Sanchez & Zhang, 2022) introdujeron la fÃ³rmula de overlapping rate (ro = FOV Ã— fps / velocidad), demostrando que con 22 fps son viables velocidades de hasta 2.5 m/s. (Autores, 2019) demostraron que 1.39 m/s funciona con tracking Kalman Filter (error de doble conteo solo 2.6%). (Autores, 2024) encontraron que YOLOv8 pierde solo un 4.6% de mAP@0.5 al 100% de velocidad de motion, y con knowledge distillation solo un 2.5%. La degradaciÃ³n por blur es moderada (15-50%), no catastrÃ³fica.

**DecisiÃ³n final.** El lÃ­mite de 1 m/s es conservador. Con tracking adecuado y modelos tolerantes al blur, **1.0-1.3 m/s** es viable. Para mandarinas sin deblurring, se recomienda ~1 m/s.

##### 3.3.2 Ãngulo de CÃ¡mara

**Evidencia principal.** (Hemming et al., 2014) probaron 14 posiciones de cÃ¡mara en pimiento dulce, encontrando que el Ã¡ngulo zenith 60Â° (30Â° hacia arriba) maximiza la Fruit Detectability como posiciÃ³n Ãºnica, y que la combinaciÃ³n de 5 posiciones alcanza un FD del 90%. (Autores, 2023) probaron 0Â°, 15Â° y 30Â° en manzanas con cÃ¡mara 3D, encontrando que **15Â°** proporciona el menor RMSE (1.54 cm).

**Evidencia contradictoria.** (VillacrÃ©s et al., 2024) encontraron que una cÃ¡mara perpendicular al dosel (0Â° horizontal) detecta el 88.3% de los frutos en sistemas multi-cÃ¡mara para manzanas. (Autores, 2025) demostraron que la orientaciÃ³n sideways (horizontal) alcanza un mAP del 95%, superior a cualquier Ã¡ngulo con tilt. (Autores, 2025) probaron 0Â°, 15Â°, 30Â° y 45Â°, encontrando que **45Â°** da la mejor tasa de detecciÃ³n (>40%).

**DecisiÃ³n final.** No existe un Ã¡ngulo Ãºnico Ã³ptimo. La estrategia recomendada para mandarinas en dosel denso es **combinar al menos 2 Ã¡ngulos**: **0Â° (horizontal) + 30Â° hacia arriba**. Idealmente, grabar cada hilera desde ambos lados para obtener automÃ¡ticamente dos perspectivas. La combinaciÃ³n de 3-5 posiciones maximiza la detectabilidad, como demostrÃ³ (Hemming et al., 2014).

##### 3.3.3 Distancia al Dosel

**Evidencia principal.** (Autores, 2026) reportaron que 0.8-1.5 m es el rango Ã³ptimo con un mAP del 93.69%. (Autores, 2020) demostraron que 1.5 m proporciona un 200.5% mÃ¡s de densidad de nube de puntos que 2.5 m. (Autores, 2025) validaron el rango 0.3-1.5 m para detecciÃ³n de manzanas con Redmi Note 7.

**Evidencia contradictoria.** (Autores, 2018) encontraron que para cÃ­tricos con RealSense, la distancia Ã³ptima es de 0.16-0.7 m (close-shot: "close, large, and clear"), con una detecciÃ³n del 80-100% a baja oclusiÃ³n. (Autores, 2024) reportaron que para palma aceitera, 0.3 m es Ã³ptimo (F1 = 0.96).

**Distancia Ã³ptima segÃºn tamaÃ±o de fruto:**

| Tipo de fruto | DiÃ¡metro tÃ­pico | Distancia Ã³ptima |
|---|---|---|
| Muy pequeÃ±os (lychee, blueberry) | ~20-30 mm | 0.3-0.7 m |
| PequeÃ±os (mandarina, cÃ­trico) | ~40-60 mm | **0.5-1.2 m** |
| Grandes (manzana, mango) | ~70-100 mm | 0.8-1.5 m |
| Conteo a nivel Ã¡rbol | â€” | 1.5-5 m |

**DecisiÃ³n final.** Para mandarinas (fruto pequeÃ±o ~40-60 mm), la evidencia sugiere que el rango Ã³ptimo es **0.5-1.2 m**, mÃ¡s cercano que el 0.8-1.5 m original. Este rango balancea el detalle fino del fruto con la cobertura del dosel.

##### 3.3.4 Horario e IluminaciÃ³n

**Evidencia principal.** Se recomienda capturar entre 9-11 AM o 3-5 PM, evitando el sol cenital (12-14 PM). (Autores, 2026) reportaron que la iluminaciÃ³n controlada es crÃ­tica: 94.8% mAP en condiciones normales frente a 61.4% en condiciones extremas (âˆ’50% brillo, 70% oclusiÃ³n). (Autores, 2020) demostraron que el glare destruye la detecciÃ³n: F1 de 0.82 en condiciones normales frente a 0.13 con glare.

**Evidencia contradictoria.** (Autores, 2024) reportaron que el mediodÃ­a solar (11-12 h) no solo no es perjudicial, sino que puede dar el mejor rendimiento (precisiÃ³n 92.1%, F1 90.5% en condiciones de sol cenital). (Autores, 2024) encontraron que se requiere un mÃ­nimo de 3,000 lx para segmentaciÃ³n precisa, y los dÃ­as nublados proporcionan solo 1,000-2,000 lx, resultando en solo el 50% del Ã¡rea de fruto detectada. La opciÃ³n **noche con LED controlado** (5600 K, frontal, 210-350 Lux) consistentemente supera al dÃ­a en mÃºltiples estudios: (Autores, 2024) lograron un 98.86% mAP@0.5 con LED nocturno en litchi; (Autores, 2024) reportaron un 94% de Ã©xito nocturno frente a 88% diurno en cosecha robÃ³tica; (Autores, 2022) alcanzaron un 96.1% F1 nocturno frente a ~93% con luz natural.

**DecisiÃ³n final.** La recomendaciÃ³n original de "evitar mediodÃ­a" es cuestionada por evidencia mÃ¡s reciente. La recomendaciÃ³n "nublado ideal" tambiÃ©n se matiza por requerir >3,000 lx para segmentaciÃ³n precisa. Se prioriza la **captura nocturna con iluminaciÃ³n LED frontal** (5600 K, ~300 Lux) como opciÃ³n superior. Alternativamente, cualquier hora del dÃ­a funciona, incluido el mediodÃ­a. Evitar especÃ­ficamente backlight extremo y glare.

##### 3.3.5 Motion Blur y Shutter Speed

**Evidencia principal.** (Autores, 2024) proporcionan la fÃ³rmula de desplazamiento por blur. (Autores, 2025) cuantificaron que el mAP@0.5 cae un 27.2% (de 0.925 a 0.673) por motion blur en cÃ­tricos. (Kurtser et al., s.f.) demostraron que con exposiciÃ³n a 20 Âµs (Flash-No-Flash) se logra una precisiÃ³n del 95% con un recall del 95%.

**Evidencia contradictoria.** (Choi et al., 2021) demostraron que con LED activo, exposiciones de 20 Âµs eliminan el blur por completo, independientemente del shutter. (Hasinoff et al., 2016) propusieron burst photography (HDR+) como alternativa superior a la exposiciÃ³n fija Ãºnica. (Autores, 2026) demostraron que la exposiciÃ³n adaptativa por frame supera a 1/60-1/120 s fijo. (Autores, 2026) encontraron que YOLOv8n retiene un 71.9% de mAP@0.5 incluso con blur severo (kernel=11), y modelos especÃ­ficos (FEGW-YOLO) retienen un 80.1%. Entrenar con blur (data augmentation) hace que el shutter sea menos crÃ­tico.

**DecisiÃ³n final.** El rango 1/60-1/120 s es razonable para captura sin iluminaciÃ³n adicional. Se recomienda: (a) sin LED: **1/120 s** sobre 1/60 s para minimizar rolling shutter; (b) con LED activo: usar **20-100 Âµs** (elimina blur por completo); (c) considerar burst photography como alternativa; (d) deblurring post-hoc (AGG-DeblurGAN) puede recuperar calidad si se acepta algo de blur.

##### 3.3.6 Anti-Doble Conteo y Tracking

**Evidencia principal.** (GenÃ©-Mola et al., 2023) compararon SORT, DeepSORT y ByteTrack para conteo de frutos en video, estableciendo que ByteTrack ofrece el mejor rendimiento: MOTA 0.682, IDF1 0.837, HOTA 0.689. (Autores, 2019) demostraron que el tracking con Kalman Filter + Hungarian Algorithm alcanza el 62% del conteo de cosecha.

**Evidencia contradictoria.** MÃºltiples trackers especÃ­ficos para agricultura superan a ByteTrack. **AgriSORT** (ICRA 2024) alcanza un MOTA de 65.93 frente a ByteTrack 48.24 (CloseUp). **Dynamic Kalman** (Autores, 2025) logra un MOTA del 95.0% frente a ByteTrack 75%. **OC-SORT** (Autores, 2025) alcanza un HOTA del 67.10% frente a ByteTrack 62.39%. Otros trackers como FTO-SORT (IDF1 90.2%), PineSORT (CVPR 2025) y CoTracker3 (point tracking para oclusiones) representan mejoras adicionales.

**DecisiÃ³n final.** **ByteTrack NO es la mejor opciÃ³n para agricultura en 2026.** Se recomienda:

| Tracker | CuÃ¡ndo usarlo |
|---|---|
| **AgriSORT** (ICRA 2024) | Tracking de fruta con cÃ¡mara en movimiento. Motion-only, sin Re-ID. |
| **Dynamic Kalman** | MÃ¡xima precisiÃ³n (MOTA 95%). Requiere tuning del forgetting factor. |
| **OC-SORT** | Buena alternativa general, especialmente con oclusiones. |
| **CoTracker3** | Point-tracking robusto a oclusiones. Alternativa a bounding-box. |
| **ByteTrack** | Mantener como baseline de comparaciÃ³n en el experimento A/B. |

Mantener la estrategia de grabar **ambos lados de la hilera**, pero no necesariamente con multi-view geometry â€” el tracking temporal desde un solo lado puede ser suficiente con el tracker adecuado.

#### 3.3.7 Gap Confirmado para P3

> No existe un paper que compare la interacciÃ³n de velocidad Ã— Ã¡ngulo Ã— distancia combinados para captura manual con smartphone en agricultura, midiendo el impacto en mAP/MOTA. Los papers existentes prueban un parÃ¡metro a la vez, usan tractores o robots (no caminata humana), y no reportan mAP/MOTA de YOLO como mÃ©trica de comparaciÃ³n de parÃ¡metros de captura. La investigaciÃ³n contradictoria de 8 agentes paralelos ampliÃ³ el gap: tampoco existe un paper que compare noche con LED vs dÃ­a, AgriSORT vs ByteTrack para cÃ­tricos, o single-view video vs multi-view estÃ¡tico para mandarinas en hilera.

#### 3.3.8 ParÃ¡metros de Captura Finales

**Valores originales con respaldo bibliogrÃ¡fico directo:**

| ParÃ¡metro | Valor | IDs |
|---|---|---|
| Velocidad | ~1 m/s constante | (Roy et al., 2018); (Autores, 2019); (Autores, 2024) |
| Ãngulo | ~15Â° hacia arriba | (Hemming et al., 2014); (Autores, 2023) |
| Distancia | 0.8-1.5 m del dosel | (Autores, 2026); (Autores, 2020); (Kuznetsova et al., 2020) |
| Horario | 9-11 AM o 3-5 PM | (Li et al., 2023); (Restrepo-Arias et al., 2023); (Autores, 2026) |
| Trayectoria | 1 hilera por grabaciÃ³n, un lado | DecisiÃ³n del protocolo [^1] |
| Anti-doble conteo | ByteTrack + ambos lados de hilera | (GenÃ©-Mola et al., 2023); (Autores, 2019) |
| Shutter | 1/60 o 1/120 s fijo | (Autores, 2024); (Autores, 2025) |

[^1]: El parÃ¡metro "Trayectoria â€” 1 hilera por grabaciÃ³n, un lado" no cuenta con respaldo bibliogrÃ¡fico directo en los papers consultados de P3. Es una decisiÃ³n del protocolo documentada como gap metodolÃ³gico.

**Valores actualizados segÃºn evidencia contradictoria (recomendaciÃ³n para validaciÃ³n en campo):**

| ParÃ¡metro | Valor recomendado | JustificaciÃ³n | Confianza |
|---|---|---|---|
| Velocidad | ~1.0-1.3 m/s (rango ampliado) | Con tracking adecuado y modelos tolerantes al blur, hasta 1.3 m/s es seguro. | Media-Alta |
| Ãngulo | 0Â° (horizontal) + 30Â° up (combinaciÃ³n) | Horizontal solo: 88.3% detecciÃ³n. Combinar ambas perspectivas maximiza cobertura. | Alta |
| Distancia | 0.5-1.2 m (ajustado para mandarinas) | Frutos pequeÃ±os requieren distancia mÃ¡s cercana. SÃ­ntesis para mandarinas [^2] | Alta |
| Horario | Noche con LED (5600 K, frontal) > Cualquier horario > Evitar backlight | Noche con LED supera al dÃ­a. MediodÃ­a funciona bien. Nublado puede ser insuficiente [^3]. | Alta |
| Shutter | 1/120 s fijo (sin LED). 20-100 Âµs (con LED activo) | 1/120 s sobre 1/60 s para rolling shutter. | Alta |
| Anti-doble conteo | AgriSORT/OC-SORT + ambos lados + single-side video tracking | AgriSORT supera a ByteTrack. Sin validaciÃ³n especÃ­fica en mandarinas [^4]. | Alta |

[^2]: Distancia 0.5-1.2 m para mandarinas: extrapolaciÃ³n de estudios en cÃ­tricos genÃ©ricos con RealSense RGB-D a 0.16-0.7 m y oil palm a 0.3 m. El rango para mandarinas es sÃ­ntesis propia del autor sin validaciÃ³n directa.
[^3]: Noche con LED para mandarinas: extrapolaciÃ³n mÃºltiple. Los estudios disponibles usan robot con LED 5600 K, litchi con LED matrix 210-350 Lux, UAV y peras con 1000 lm. NingÃºn paper estudia captura manual con smartphone en mandarinas con LED nocturno.
[^4]: AgriSORT/OC-SORT para mandarinas: sin validaciÃ³n especÃ­fica. El archivo correspondiente a (OC-SORT Passion Fruit) no fue encontrado en la bibliografÃ­a de P3. La superioridad sobre ByteTrack en mandarinas es una hipÃ³tesis no validada.

### 3.4 SelecciÃ³n de Parcelas para Muestreo (P4)

#### 3.4.1 IntroducciÃ³n

La validez externa de los resultados del experimento A/B depende crÃ­ticamente de que las parcelas seleccionadas para la captura sean representativas de la variabilidad de vigor presente en el huerto. En huertos frutales, la variabilidad espacial del vigor vegetativo es una fuente importante de heterogeneidad que afecta la densidad de follaje, la iluminaciÃ³n del dosel y, en consecuencia, la calidad de las imÃ¡genes capturadas y el rendimiento de los algoritmos de visiÃ³n por computadora.

#### 3.4.2 Ãrea de Estudio y Datos Disponibles

El Ã¡rea de estudio comprende **4 parcelas** de mandarina variedad **Murcott** de **4 aÃ±os de edad**, ubicadas en un huerto comercial. Cada parcela tiene una superficie de **0.5 ha** (aproximadamente 70 Ã— 70 m), configuraciÃ³n cuadrada, y contiene **13 hileras** de Ã¡rboles. Las parcelas comparten el mismo marco de plantaciÃ³n y han sido manejadas con prÃ¡cticas agronÃ³micas homogÃ©neas.

Se dispone de imÃ¡genes del satÃ©lite **Sentinel-2** con los siguientes Ã­ndices de vegetaciÃ³n:

| Ãndice | ResoluciÃ³n | PÃ­xeles por parcela | Â¿Resuelve hileras? | Â¿Apto para selecciÃ³n? |
|---|---|---|---|---|
| NDVI | 10 m | ~7 Ã— 7 = 49 pÃ­xeles | No (~2 hileras por pÃ­xel) | SÃ­ |
| MSAVI2 | 10 m | ~7 Ã— 7 = 49 pÃ­xeles | No | SÃ­ |
| NDRE | 20 m | ~3.5 Ã— 3.5 = 12 pÃ­xeles | No (~4 hileras por pÃ­xel) | Limitado |

#### 3.4.3 MetodologÃ­a de SelecciÃ³n (4 Pasos)

**Paso 1: SelecciÃ³n de Parcelas por NDVI Medio de Sentinel-2.** Se extrajo el valor medio de NDVI de cada una de las 4 parcelas a partir de imÃ¡genes Sentinel-2 (banda 10 m, ~49 pÃ­xeles por parcela). Los valores se ordenaron de menor a mayor, representando un gradiente de vigor vegetativo. Se seleccionaron 2 parcelas: una en el extremo inferior (menor NDVI, menor vigor) y una en el extremo superior (mayor NDVI, mayor vigor).

Esta decisiÃ³n sigue el principio de selecciÃ³n por cuantiles NDVI satelital validado por (Meyers et al., 2020), quienes demostraron que la selecciÃ³n de puntos en las colas de la distribuciÃ³n del Ã­ndice alcanza la misma representatividad que un nÃºmero considerablemente mayor de puntos aleatorios. El uso de Sentinel-2 a 10 m estÃ¡ respaldado por (Autores, 2024), quienes confirmaron que este sensor captura las principales zonas de vigor a nivel de parcela. La aplicaciÃ³n especÃ­fica a parcelas de cÃ­tricos estÃ¡ validada por (Autores, 2022), quienes emplearon el NDVI medio de Sentinel-2 para caracterizar 50 parcelas de mandarina.

**Paso 2: SelecciÃ³n de Hileras mediante SUR SistemÃ¡tico.** Dentro de cada parcela seleccionada, se eligieron 3 hileras mediante muestreo sistemÃ¡tico uniforme (SUR) con arranque aleatorio = 3 e intervalo = 4, resultando en las hileras 3, 7 y 11 de un total de 13. Este mÃ©todo fue validado empÃ­ricamente por (Wulfsohn et al., 2012), quienes reportaron errores de estimaciÃ³n inferiores al 10% en 11 de 14 huertos comerciales evaluados. La distribuciÃ³n (hilera 3 cercana al borde, hilera 7 central, hilera 11 cercana al borde opuesto) asegura una cobertura espacial equilibrada de cada parcela.

**Paso 3: CaracterizaciÃ³n de Parcelas con NDVI y NDRE.** Las parcelas seleccionadas se caracterizaron mediante valores medios de NDVI (10 m, Ã­ndice primario) y NDRE (20 m, descriptor complementario). El NDRE se incluyÃ³ siguiendo la recomendaciÃ³n de (Sun et al., 2026), quienes demostraron que los Ã­ndices de Red Edge son superiores al NDVI para estimar LAI (RÂ² = 0.86) y clorofila (RÂ² = 0.80) en mandarinos.

**Paso 4: Captura de Video.** La captura en las 6 unidades de muestreo (2 parcelas Ã— 3 hileras) se realiza siguiendo el protocolo establecido en la secciÃ³n 3.3: velocidad ~1 m/s, distancia 0.8-1.5 m, Ã¡ngulo 15-30Â° hacia arriba, bloqueo de AF/AE/WB.

#### 3.4.4 DiscusiÃ³n y Limitaciones

**ElecciÃ³n de NDVI sobre NDRE.** El NDVI se utilizÃ³ para la selecciÃ³n por su resoluciÃ³n de 10 m (49 pÃ­xeles/parcela) frente a los 20 m del NDRE (12 pÃ­xeles/parcela), proporcionando una estimaciÃ³n mÃ¡s robusta. La literatura de muestreo estratificado ha empleado consistentemente el NDVI como variable auxiliar (Miranda et al., 2018); (Uribeetxebarria et al., 2018); (Meyers et al., 2020); (ArnÃ³ et al., 2017). AdemÃ¡s, (Ampatzidis & Partel, 2019) demostraron que el NDVI correlaciona significativamente con el tamaÃ±o de copa y la sanidad en cÃ­tricos.

**Limitaciones:**
- **NÃºmero reducido de parcelas (4 disponibles).** Se mitiga mediante estratificaciÃ³n por NDVI, que maximiza la variabilidad con solo 2 unidades (ArnÃ³ et al., 2017).
- **Sentinel-2 no resuelve hileras individuales** (~5.4 m de ancho vs 10 m de pÃ­xel). Se mitiga mediante SUR para selecciÃ³n intra-parcela (Wulfsohn et al., 2012).
- **SelecciÃ³n de solo 2 parcelas (extremos).** Adecuado para evaluar robustez del protocolo en condiciones extremas de vigor. Para estimaciÃ³n de producciÃ³n promedio, 3 parcelas serÃ­an preferibles.
- **Variedad Ãºnica (Murcott).** Los resultados no son directamente generalizables a otras variedades.

#### 3.4.5 ConclusiÃ³n

| Elemento | DecisiÃ³n | MÃ©todo | Respaldo |
|---|---|---|---|
| SelecciÃ³n de parcelas | 2 parcelas: menor NDVI + mayor NDVI | EstratificaciÃ³n por NDVI medio Sentinel-2 | (Meyers et al., 2020); (Autores, 2022); (ArnÃ³ et al., 2017) |
| SelecciÃ³n de hileras | 3 hileras por parcela: 3, 7, 11 | SUR sistemÃ¡tico con arranque aleatorio | (Wulfsohn et al., 2012) |
| CaracterizaciÃ³n | NDVI medio + NDRE medio | Ãndices Sentinel-2 | (Sun et al., 2026) |
| Total de videos | 6 videos | 2 parcelas Ã— 3 hileras | â€” |
| Tiempo estimado | ~30 minutos | â€” | â€” |

### 3.5 Pipeline de Captura (7 Etapas)

El pipeline completo de captura y procesamiento se estructura en 7 etapas, desde la pre-captura hasta el entrenamiento:

```
PRE-CAPTURA â†’ CAPTURA â†’ POST-PROCESAMIENTO â†’ ENTRENAMIENTO
```

| Etapa | QuÃ© se hace | App/Equipo |
|---|---|---|
| 1. App de CÃ¡mara | Bloquear AF/AE/WB + ISO/shutter fijos | Open Camera (Camera2 API) |
| 2. EstabilizaciÃ³n | Gimbal mecÃ¡nico + Gyroflow (post) | DJI Osmo + Gyroflow |
| 3. Logging IMU | Giroscopio + acelerÃ³metro 100 Hz | Sensor Logger |
| 4. SincronizaciÃ³n Video-IMU | Frame-level sync | OpenCamera Sensors / Clap sync |
| 5. CalibraciÃ³n de CÃ¡mara | CorrecciÃ³n de distorsiÃ³n | OpenCV + Charuco |
| 6. Pre-procesamiento | EstabilizaciÃ³n + (opcional) deblurring | Gyroflow + FFmpeg |
| 7. Pipeline de Datos | YOLO + ByteTrack/CoTracker3 | YOLO + TrackEval |

### 3.6 ParÃ¡metros de Captura

**ParÃ¡metros de cÃ¡mara:**

| ParÃ¡metro | Valor | JustificaciÃ³n |
|---|---|---|
| App | Open Camera (Camera2 API ON) | Ãšnica gratuita con AF/AE/WB Lock |
| ResoluciÃ³n | 4K (3840Ã—2160) o 1080p | PÃ­xeles por fruto pequeÃ±o |
| FPS | 30 | Suficiente para tracking |
| ISO | 200 fijo (100 si hay suficiente luz) | ISO=200 documentado (Autores, 2024) |
| Shutter | 1/100 s fijo (rango 1/60-1/120) | Compromiso entre blur y luz (Autores, 2024) |
| AF | ðŸ”’ LOCK | Evita focus hunting (Autores, 2025) |
| AE | ðŸ”’ LOCK | Brillo constante (Autores, 2018) |
| WB | ðŸ”’ LOCK | Color estable (Autores, 2023) |
| Bitrate | 50 Mbps | Calidad constante |
| OIS | OFF | Interfiere con Gyroflow (Autores, 2021); (Autores, 2022) |

**ParÃ¡metros en campo:**

| ParÃ¡metro | Valor |
|---|---|
| Distancia al dosel | 0.5-1.5 m |
| Velocidad | ~0.5-1 m/s constante |
| Ãngulo | 0-30Â° hacia arriba |
| Horario | 8:30 AM+, evitar 12-14 PM |
| IMU | 100 Hz (gyro + accel) |

### 3.7 Experimento A/B (ValidaciÃ³n)

El diseÃ±o experimental para validar el protocolo consiste en una comparaciÃ³n A/B:

| Grupo | Captura |
|---|---|
| **A (Protocolo)** | Siguiendo todos los pasos del pipeline |
| **B (Control)** | CÃ¡mara nativa en modo automÃ¡tico |
| **MÃ©trica** | mAP@0.5, MOTA, IDF1, % frames borrosos |

Este experimento medirÃ¡ cuantitativamente el impacto del protocolo de captura en las mÃ©tricas de detecciÃ³n y seguimiento, comparando el pipeline completo frente a la captura sin control de parÃ¡metros.

---

## CapÃ­tulo 4: DiscusiÃ³n

### 4.1 Evidencia Contradictoria Consolidada

La investigaciÃ³n bibliogrÃ¡fica realizada, incluyendo la investigaciÃ³n contradictoria con 8 agentes paralelos, revelÃ³ varios patrones que matizan las recomendaciones originales del protocolo sin invalidarlas:

**La velocidad de caminata no es tan crÃ­tica como se pensaba.** MÃºltiples estudios demuestran que los modelos YOLO modernos toleran el motion blur mejor de lo que se creÃ­a: la degradaciÃ³n real por blur es del 15-50% (no el 86.4% reportado inicialmente como mejora), y modelos entrenados con data augmentation de blur pierden solo un 2.5-4.6% de mAP. Sin embargo, para mandarinas (frutos pequeÃ±os en dosel denso), mantener una velocidad controlada sigue siendo una buena prÃ¡ctica para maximizar la calidad del dataset.

**La iluminaciÃ³n controlada (noche + LED) supera consistentemente al dÃ­a.** Esta es quizÃ¡s la contradicciÃ³n mÃ¡s relevante: la recomendaciÃ³n original de "evitar mediodÃ­a" y "dÃ­as nublados ideales" es directamente contradicha por estudios que muestran que (a) el mediodÃ­a solar da excelentes resultados, (b) los dÃ­as nublados pueden ser insuficientes (<3,000 lx) y (c) la noche con iluminaciÃ³n LED frontal (5600 K, ~300 Lux) consistentemente supera al dÃ­a en todas las mÃ©tricas. Esto abre una lÃ­nea de investigaciÃ³n prometedora para la tesis.

**Los trackers especÃ­ficos para agricultura superan a ByteTrack.** La recomendaciÃ³n original de ByteTrack como tracker principal es contradicha por AgriSORT (MOTA 65.93 vs 48.24), Dynamic Kalman (MOTA 95% vs 75%) y OC-SORT (HOTA 67.10% vs 62.39%). Se recomienda usar AgriSORT o OC-SORT como tracker principal y mantener ByteTrack como baseline de comparaciÃ³n.

**El nuevo paradigma de detecciÃ³n robusta (2024-2026) no invalida el control de captura.** Aunque detectores como Orchard-YOLO logran >94% mAP con variaciones de iluminaciÃ³n de Â±50%, el control de captura y los modelos robustos son complementarios, no sustitutos. El experimento A/B de esta tesis (Protocolo vs CÃ¡mara Nativa) es precisamente lo que falta en la literatura para cuantificar esta complementariedad.

### 4.2 DiscusiÃ³n sobre Valores Propuestos vs Documentados

Los valores especÃ­ficos propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120 s) **no son valores extraÃ­dos directamente de un paper**, sino decisiones de ingenierÃ­a informadas por la literatura. Esta distinciÃ³n es importante para la reproducibilidad y la interpretaciÃ³n de los resultados.

Los valores documentados en papers son heterogÃ©neos y dependientes de condiciones especÃ­ficas: ISO=25 y shutter=1/400 s en condiciones de laboratorio; ISO=200 y shutter=1/100 s con iluminaciÃ³n LED controlada; exposiciones de 20-250 Âµs con flashes sincronizados en sistemas industriales. No existe un consenso en la literatura sobre un valor Ãºnico para captura manual con smartphone en agricultura.

El protocolo propone valores de compromiso que maximizan la utilidad prÃ¡ctica en condiciones de campo reales, y el experimento A/B determinarÃ¡ si estas decisiones son adecuadas frente a la ausencia total de control (cÃ¡mara nativa).

### 4.3 Limitaciones de la MetodologÃ­a

**LimitaciÃ³n del software de captura a Android.** El protocolo solo es aplicable a dispositivos Android con Camera2 API, ya que iOS no expone control sobre el tone mapping en video (Autores, 2023). Los resultados pueden no ser transferibles entre plataformas.

**Extrapolaciones del protocolo de caminata.** Varios valores propuestos para mandarinas son extrapolaciones de estudios en otros cultivos:
- La distancia 0.5-1.2 m para mandarinas es sÃ­ntesis propia a partir de estudios en cÃ­tricos genÃ©ricos y oil palm, sin validaciÃ³n directa en mandarinas.
- La captura nocturna con LED se basa en estudios en litchi, peras y robÃ³tica, no en captura manual de mandarinas.
- La superioridad de AgriSORT/OC-SORT sobre ByteTrack en mandarinas es una hipÃ³tesis no validada.

**Limitaciones del muestreo de parcelas.** Con solo 4 parcelas disponibles de una Ãºnica variedad (Murcott), la selecciÃ³n de 2 parcelas extremas maximiza la representatividad pero sacrifica la cobertura del rango medio de vigor. Sentinel-2 no resuelve hileras individuales.

**Robustez desconocida de YOLO moderno.** Si YOLO resulta ser inherentemente robusto a las variaciones de captura, el efecto del protocolo podrÃ­a ser modesto. Un resultado nulo sigue siendo una contribuciÃ³n cientÃ­fica vÃ¡lida.

### 4.4 Implicaciones para el Experimento A/B

Las contradicciones documentadas tienen implicaciones directas para el diseÃ±o del experimento A/B:

1. **El Grupo B (Control) con cÃ¡mara nativa podrÃ­a no ser tan deficiente como se esperaba**, dada la robustez de los detectores modernos. Esto hace que el experimento sea mÃ¡s informativo, no menos.
2. **La noche con LED como tercera condiciÃ³n experimental** (Grupo C) serÃ­a una valiosa adiciÃ³n, permitiendo comparar tres condiciones: protocolo diurno, protocolo nocturno con LED y cÃ¡mara nativa.
3. **La selecciÃ³n del tracker debe considerar AgriSORT/OC-SORT** como alternativa a ByteTrack, no solo como reemplazo sino como variable experimental.
4. **Las mÃ©tricas deben incluir tanto mAP como MOTA e IDF1**, ya que las contradicciones sugieren que el impacto del protocolo puede ser mayor en tracking que en detecciÃ³n.

---

## CapÃ­tulo 5: Conclusiones

### 5.1 Gap de InvestigaciÃ³n Confirmado

El anÃ¡lisis bibliogrÃ¡fico sistemÃ¡tico realizado confirma los siguientes gaps en la literatura:

1. **Software de captura:** Solo 1 paper en toda la literatura (Autores, 2024) documenta Open Camera con configuraciÃ³n detallada. NingÃºn paper documenta el flujo completo app + configuraciÃ³n + IMU + pipeline para detecciÃ³n de frutos en video.
2. **IMU â†’ YOLO mAP:** No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU en mÃ©tricas YOLO o MOT para video agrÃ­cola.
3. **ParÃ¡metros combinados:** No existe un paper que compare la interacciÃ³n de velocidad Ã— Ã¡ngulo Ã— distancia para captura manual con smartphone en agricultura.
4. **Noche con LED vs dÃ­a:** No existe un paper que compare noche con LED vs dÃ­a para detecciÃ³n YOLO de mandarinas.
5. **Trackers en cÃ­tricos:** AgriSORT/OC-SORT no se han probado especÃ­ficamente para tracking de cÃ­tricos en video.
6. **SelecciÃ³n de parcelas:** No existe un protocolo que integre selecciÃ³n por NDVI satelital con un pipeline completo de captura para cÃ­tricos.

### 5.2 ContribuciÃ³n Original

La contribuciÃ³n original de esta investigaciÃ³n consiste en documentar y medir cuantitativamente el impacto de las decisiones de captura en mAP/MOTA para video de mandarinas, integrando:

- **P1:** DocumentaciÃ³n y justificaciÃ³n del pipeline de captura (app + configuraciÃ³n + IMU + procesamiento) con mÃ©tricas cuantitativas de impacto en YOLO, mediante experimento A/B (Protocolo vs CÃ¡mara Nativa).
- **P2:** MediciÃ³n del impacto del pre-procesamiento con IMU (Gyroflow) en mÃ©tricas YOLO y MOT para video agrÃ­cola.
- **P3:** MediciÃ³n cuantitativa del impacto combinado de velocidad Ã— Ã¡ngulo Ã— distancia en mAP/MOTA para video de mandarinas capturado con smartphone.
- **P4:** MetodologÃ­a reproducible de selecciÃ³n de parcelas por NDVI satelital con muestreo sistemÃ¡tico uniforme.

### 5.3 Valores Finales del Protocolo

**Valores validados bibliogrÃ¡ficamente (recomendaciÃ³n base):**

| ParÃ¡metro | Valor |
|---|---|
| App de cÃ¡mara | Open Camera con Camera2 API |
| ResoluciÃ³n | 4K (3840Ã—2160) o 1080p |
| FPS | 30 |
| ISO | 200 fijo (100 si hay suficiente luz) |
| Shutter | 1/100 s fijo (rango 1/60-1/120) |
| AF/AE/WB | LOCK |
| Bitrate | 50 Mbps |
| OIS | OFF |
| Velocidad de caminata | ~0.5-1.0 m/s |
| Ãngulo de cÃ¡mara | 15-30Â° hacia arriba |
| Distancia al dosel | 0.8-1.5 m |
| Horario | 9-11 AM o 3-5 PM (o noche con LED) |
| IMU | 100 Hz (giroscopio + acelerÃ³metro) |
| Tracker recomendado | ByteTrack (AgriSORT/OC-SORT como alternativa) |

### 5.4 Trabajo Futuro

Se sugieren las siguientes lÃ­neas de trabajo futuro:
- ValidaciÃ³n experimental del protocolo completo frente a cÃ¡mara nativa (experimento A/B planificado).
- EvaluaciÃ³n de la captura nocturna con iluminaciÃ³n LED como condiciÃ³n experimental adicional.
- ComparaciÃ³n de ByteTrack, AgriSORT, OC-SORT y CoTracker3 para tracking de mandarinas.
- EvaluaciÃ³n del impacto del tone mapping lineal (Camera2 API) frente al procesamiento ISP por defecto.
- ValidaciÃ³n del protocolo en otras variedades de mandarina y otros cultivos de fruto pequeÃ±o.

---

## CapÃ­tulo 6: Referencias

Ampatzidis, Y. & Partel, V. (2019). UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence. *Remote Sensing*, 11(4), 410. https://doi.org/10.3390/rs11040410

ArnÃ³, J., MartÃ­nez-Casasnovas, J.A., Uribeetxebarria, A., EscolÃ , A. & Rosell-Polo, J.R. (2017). Comparing efficiency of different sampling schemes to estimate yield and quality parameters in fruit orchards. *Advances in Animal Biosciences*, 8(2), 471-476. https://doi.org/10.1017/S2040470017000978

Arslan, A., Gultekin, G.K. & Saranli, A. (2024). IMU-aided adaptive mesh-grid based video motion deblurring. *PeerJ Computer Science*, 10, e2540. https://doi.org/10.7717/peerj-cs.2540

Bell, S., Troccoli, A. & Pulli, K. (2014). A Non-Linear Filter for Video Stabilization and Rolling Shutter on Mobile Devices. *ECCV 2014*. NVIDIA Research.

Choi, K.T.H. (2024). Sensor Logger: A Framework for Smartphone-based Sensor Data Collection. *CEUR Workshop*.

Choi et al. (2021). Overcurrent-driven LEDs for Consistent Image Colour and Brightness in Agricultural Machine Vision. *Computers and Electronics in Agriculture*.

Fan, B. et al. (2025). Influence of Sampling Rate on IMU Orientation Estimation for Human Movement. *Sensors*, 25(7), 1976. https://doi.org/10.3390/s25071976

GenÃ©-Mola, J., Sanz-Cortiella, R., Rosell-Polo, J.R. et al. (2023). Video-Based Fruit Detection and Tracking for Apple Counting. *Computers and Electronics in Agriculture*.

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

Ramos Giraldo, P.J., Guerrero Aguirre, A., MuÃ±oz, C.M., Prieto, F.A. & Oliveros, C.E. (2017). Sensor Fusion of a Mobile Device to Acquire Videos of Coffee Branches. *Sensors*, 17(4), 786. https://doi.org/10.3390/s17040786

RanÃ§on, F., Keresztes, B., Deshayes, A. et al. (2023). Designing a Proximal Sensing Camera Acquisition System for Vineyard Applications: 8 Years of Experiments. *Sensors*, 23(2), 847. https://doi.org/10.3390/s23020847

Restrepo-Arias, J.F., Salinas-Agudelo, M.I., Hernandez-PÃ©rez, M.I. et al. (2023). RipSetCocoaCNCH12: Dataset for Ripeness Stage Detection. *Data*, 8(7), 112. https://doi.org/10.3390/data8070112

Roy, P., Dong, Y. & Isler, V. (2018). A Comparative Study of Fruit Detection and Counting Methods for Yield Mapping in Apple Orchards. *arXiv*. arXiv:1810.09499

Sanchez, J.A. & Zhang, Y. (2022). Simulation-Aided Development of CNN-Based Vision Module â€” Overlapping Rate. *Appl. Sci.*, 12(11), 5600. https://doi.org/10.3390/app12125600

Sun, Y., Qin, Q., Zhang, J., Ren, H. & Han, R. (2026). Fruit Yield Estimation of Kinnow Mandarin Orchards â€” Integrating Canopy Physiology with Remote Sensing. *Arabian Journal of Geosciences*. https://doi.org/10.1007/s12517-026-12453-z

Torun et al. (2021). In-Shoe System for Gait Monitoring â€” Effects of Sampling Rate. *Sensors*. https://doi.org/10.3390/s21082869

Uribeetxebarria, A., MartÃ­nez-Casasnovas, J.A., EscolÃ , A., Rosell-Polo, J.R. & ArnÃ³, J. (2018). Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps: A Comparative Analysis to Improve Yield and Quality Estimates. *Precision Agriculture*, 19, 1031-1050. https://doi.org/10.1007/s11119-018-9619-9

VÃ©lez, S., Ariza-SentÃ­s, M. & Valente, J. (2024). EscaYard: Precision viticulture multimodal dataset. *Data in Brief*. https://doi.org/10.1016/j.dib.2024.110497

VillacrÃ©s, J. et al. (2024). Assessing a Multi-Camera System to Enhance Fruit Visibility for Robotic Harvesting.

Wang, Z., Koirala, A., Walsh, K., Anderson, N. & Verma, B. (2018). In Field Fruit Sizing Using A Smart Phone Application (FruitSize). *Sensors*, 18(10), 3331. https://doi.org/10.3390/s18103331

Wulfsohn, D., Aravena, F., Potin, C., Zamora, I. & GarcÃ­a-FiÃ±ana, M. (2012). Multilevel Systematic Sampling to Estimate Total Fruit Number. *Precision Agriculture* (Springer).

Zhang, K. & Zhang, M. (2023). Point feature correction based rolling shutter modeling for EKF-based VIO. *Measurement Science and Technology*. https://doi.org/10.1088/1361-6501/ad044e

Zhao, G., Yang, R., Jing, X. et al. (2023). Phenotyping of individual apple tree with smartphone-based heterogeneous binocular vision. *Computers and Electronics in Agriculture*. https://doi.org/10.1016/j.compag.2023.107814

Zhou, Z., Song, Z., Fu, L. et al. (2020). Real-time kiwifruit detection using deep learning on Android smartphones. *Computers and Electronics in Agriculture*. https://doi.org/10.1016/j.compag.2020.105856

**Papers con autorÃ­a no especificada (citados por tÃ­tulo):**

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

**DocumentaciÃ³n tÃ©cnica:**

Gyroflow Documentation. (s.f.). https://docs.gyroflow.xyz/ [D2]

Open Camera Help. (s.f.). https://opencamera.sourceforge.io/help.html [D1]

Sensor Logger Official Site. (s.f.). https://www.tszheichoi.com/sensorlogger [D3]

OpenCamera Sensors (GitHub). (s.f.). https://github.com/prime-slam/opencamera-sensors [D4]

Gyroflow GitHub. (s.f.). https://github.com/gyroflow/gyroflow [D5]

> **Nota:** La tabla maestra completa con 138 referencias, incluyendo metadatos detallados (DOI, nivel de importancia, contexto en el proyecto) para cada una de las referencias P01-P130 y D1-D8, se encuentra disponible en el archivo `Tabla-Maestra-Papers.md` del repositorio del proyecto.

---

## ApÃ©ndice: Tabla de Trazabilidad [PXX] â†’ APA

El siguiente apÃ©ndice documenta la correspondencia entre los identificadores [PXX] utilizados en los archivos de investigaciÃ³n fuente y las citas en formato APA empleadas en el presente documento, garantizando la trazabilidad completa de cada decisiÃ³n tÃ©cnica segÃºn el Principio II de la constituciÃ³n del proyecto.

| ID | Cita APA |
|---|---|
| P01 | (Janowski et al., 2021) |
| P02 | (VÃ©lez et al., 2024) |
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
| P48 | (Zhou et al., 2020) |
| P49 | (RanÃ§on et al., 2023) |
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
| P74 | (GenÃ©-Mola et al., 2023) |
| P75 | ("Motion Blur Review", 2024) |
| P76 | ("Orchard-YOLO", 2026) |
| P79 | (Miranda et al., 2018) |
| P80 | (Uribeetxebarria et al., 2018) |
| P82 | (Meyers et al., 2020) |
| P84 | ("UAV vs Sentinel-2", 2024) |
| P85 | ("Morocco citrus", 2022) |
| P88 | (Wulfsohn et al., 2012) |
| P90 | (Sun et al., 2026) |
| P91 | (ArnÃ³ et al., 2017) |
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
| P111 | (VillacrÃ©s et al., 2024) |
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
