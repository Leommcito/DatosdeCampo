# Bibliografía del Paso 3 — Protocolo de Caminata y Captura

**Proyecto:** Protocolo de captura manual con smartphone en huertos densos de mandarinas para YOLO + MOT
**Archivo fuente:** `Investigacion-P3-Protocolo-Caminata.md`
**Generado desde:** `Tabla-Maestra-Papers.md`
**Referencias totales en P3:** 52 papers (más 4 con ID [—] no catalogados)
**Fecha:** 05/06/2026

---

## Criterios de clasificación

| Nivel | Criterio | Cantidad |
|---|---|---|
| 🔴 **Nivel 1 — Alto Impacto** | Papers que definen directamente los valores de los parámetros del protocolo P3, o que los contradicen con evidencia cuantitativa fuerte | 18 |
| 🟠 **Nivel 2 — Impacto Medio** | Papers que proporcionan evidencia complementaria importante, soporte para decisiones secundarias, o mejoras a parámetros específicos | 27 |
| 🟡 **Nivel 3 — Impacto Contextual** | Papers que aportan contexto general, metodologías de referencia, o evidencia preliminar sin impacto directo en los valores del protocolo | 7 |

> **Nota:** Un mismo paper puede aparecer referenciado en múltiples parámetros del P3. Esta lista usa la clasificación de mayor impacto para cada paper.

---

## 🔴 NIVEL 1 — ALTO IMPACTO (Justificación Central del P3)

Papers que definen los valores núcleo del protocolo o los contradicen con evidencia cuantitativa robusta.

### Velocidad de Caminata

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P27 "Sensor Fusion of a Mobile Device to Acquire Videos of Coffee Branches"** | Ramos Giraldo, P.J.; Guerrero Aguirre, A.; Muñoz, C.M.; Prieto, F.A.; Oliveros, C.E. | 2017 | *Sensors* | Samsung Galaxy S5, 1080p 30fps, AUTO (ISO/WB), IMU para blur detection. Velocidad 3 cm/s. Holder con botones. Ángulo 11.3°. Metodología más parecida a la nuestra. | 10.3390/s17040786 |
| **P66 "Mango Fruit Load Estimation Using Video Based MangoYOLO-Kalman Filter-Hungarian Algorithm"** | — | 2019 | *Sensors* (10.3390/s19122742) | Video detection: **62.3%** del conteo real vs **40.2%** con foto estática. **+22% mejora** usando video en movimiento. Velocidad **5 km/h (~1.39 m/s)**. Error doble conteo 9.9%. | 10.3390/s19122742 |
| **P70 "A Comparative Study of Fruit Detection and Counting Methods for Yield Mapping in Apple Orchards"** | Roy, P.; Dong, Y.; Isler, V. | 2018 | *arXiv* | **Samsung Galaxy S4** a **2 m/s** caminando. Video 30fps, 1920×1080. Cámara horizontal, un solo lado de hilera. Yield accuracy 95.56-97.83%. | arXiv:1810.09499 |
| **P71 "Recognition and Counting of Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms"** | — | 2023 | *Sensors* | **Compara 3 velocidades (0.052/0.069/0.098 m/s) × 3 ángulos (0°/15°/30°).** YOLOv7 mAP@0.5=0.905. 15° + 0.098 m/s = RMSE 1.54cm. Counting accuracy 86.6%. | 10.3390/s23083810 |
| **P110 "Simulation-Aided Development of CNN-Based Vision Module — Overlapping Rate"** | Sanchez, J.A.; Zhang, Y. | 2022 | *Appl. Sci.* 12(11), 5600 | Introduce **overlapping rate**: `ro = (FOV × fps) / velocity`. Tested 0.1-2.5 m/s. Con 22 fps: **2.5 m/s** viable. ro < 1 = coverage gaps. ❌ **Contradice** límite de 1 m/s. | 10.3390/app12125600 |

### Ángulo de Cámara

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P69 "Fruit Detectability Analysis for Different Camera Positions in Sweet-Pepper"** | Hemming, J.; Ruizendaal, J.; Hofstee, J.W.; van Henten, E.J. | 2014 | *Sensors* | **Prueba 14 posiciones de cámara** con diferentes azimuth y zenith angles. Zenith 60° (mirando hacia arriba) = mejor FD. 5 posiciones combinadas = FD=90%. Single view máximo: 69%. | 10.3390/s140406032 |
| **P111 "Assessing a Multi-Camera System to Enhance Fruit Visibility for Robotic Harvesting"** | Villacrés, J. et al. | 2024 | — (Sep 2024, pending DOI) | Cámara **perpendicular al dosel (0° horizontal)**: detectó **88.3%** de frutos. Dos cámaras: **97.5%**. ❌ **Contradice** ángulo 15° up como único óptimo. | — |

### Distancia al Dosel

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P28 "Using YOLOv3 Algorithm with Pre- and Post-Processing for Apple Detection"** | Kuznetsova, A.; Maleva, T.; Soloviev, V. | 2020 | *Agronomy* | **Compara 4 distancias: 0.2, 0.5, 1.0, 2.0m.** 4 condiciones de luz. Único paper que compara distancias con métricas. | 10.3390/agronomy10071016 |
| **P73 "YOLO-CSB: Real-Time Detection of Occluded Apples for Precision Agriculture"** | — | 2026 | *Agronomy* | **Distancia óptima 0.8-1.5m** del dosel. **mAP 93.69%**. Datos mañana (9-11AM, 45%) y tarde (3-5PM, 55%). | 10.3390/agronomy16030390 |
| **P114 "Experiments and Analysis of Close-Shot Identification of On-Branch Citrus Fruit with RealSense"** | — | 2018 | *Sensors* (MDPI) | Rango óptimo: **160-700 mm (0.16-0.7m)**. 80-100% detección para poca oclusión. ❌ **Contradice** distancia 0.8-1.5m para cítricos. | MDPI Sensors 2018 |

### Horario e Iluminación

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P76 "Orchard-YOLO: A Robust Deep Learning Framework for Fruit Detection Under Complex Optical and Environmental Degradation"** | — | 2026 | *Photonics* | **Prueba ±50% iluminación + hasta 70% oclusión.** YOLOv13: 94.8% mAP@0.5 normal, 61.4% extrema (−50% brillo, 70% oclusión). | 10.3390/photonics13050429 |
| **P116 "Intelligent Integrated System for Fruit Detection Using Multi-UAV Imaging and Deep Learning"** | — | 2024 | *Sensors* | Peak at **NOON**: Precision **92.1%**, F1 **90.5%**. Cloudy: 86.1%. Strong shade: 78.1%. ❌ **Contradice FUERTEMENTE** "evitar mediodía". | 10.3390/s24093743 |

### Shutter Speed / Motion Blur

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P75 "A State-of-the-Art Review of Image Motion Deblurring Techniques in Precision Agriculture"** | — | 2024 | *Heliyon* | Fórmula: `desplazamiento_px ≈ (velocidad × exposición) / focal`. Recomienda shutter ≥1/200s para walking shake. | Heliyon 2024 |
| **P57 "Overcurrent-driven LEDs for Consistent Image Colour and Brightness in Agricultural Machine Vision"** | — | 2021 | *Computers and Electronics in Agriculture* | **85% reducción** variación HSV con LED fijo vs auto-exposición. Motion blur 7mm→1mm a 7km/h. ❌ **Contradice**: shutter de 20 µs con LED elimina blur. | ScienceDirect |
| **P68 "Lightweight GAN for Restoring Blurred Images to Enhance Citrus Detection"** | — | 2025 | *MDPI* | **mAP@0.5:0.95 +86.4%** tras restaurar imágenes borrosas. Recall +76.9%. F1 +40.1%. FN rate -63.9%. Cuantificación central del impacto de blur. | MDPI 2025 |

### Tracking / Anti-Doble Conteo

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P31 "Deep-learning-based orange counting via video sequences (OrangeYolo + OrangeSort)"** | — | 2024 | *Computers and Electronics in Agriculture* | Rover + DJI Osmo Action. **2 m/s uniforme.** Cámara perpendicular. 60fps 1080p. MAE = 0.081 con OrangeSort. | GitHub: I3-Laboratory/orange-dataset |
| **P74 "Video-Based Fruit Detection and Tracking for Apple Counting"** | Gené-Mola, J.; Sanz-Cortiella, R.; Rosell-Polo, J.R.; et al. | 2023 | *Computers and Electronics in Agriculture* | **Compara SORT vs DeepSORT vs ByteTrack.** ByteTrack: **MOTA 0.682, IDF1 0.837, HOTA 0.689**. 15ms/frame vs DeepSORT 128ms. | UPCommons |
| **P123 "Estimation of Passion Fruit Yield Based on YOLOv8n + OC-SORT + CRCM Algorithm"** | — | 2025 | *Computers and Electronics in Agriculture* | **OC-SORT**: HOTA **67.10%** > ByteTrack 62.39%, BoT-SORT 64.12%, StrongSORT 58.28%. ❌ **Contradice**: ByteTrack no es el mejor para agricultura. | 10.1016/j.compag.2024.109727 |

---

## 🟠 NIVEL 2 — IMPACTO MEDIO (Evidencia de Soporte)

Papers que proporcionan evidencia complementaria importante para decisiones del P3.

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P29 "YOLOv5s-FP: Pear Detection with Transformer Encoder"** | Li, L. et al. | 2023 | *Sensors* | 4 horarios (7-8AM, 10-11AM, 2-3PM, 6-7PM). Velocidad UAV 1 m/s. Ángulo 20°-80°. Metodología multi-horario. | 10.3390/s23010030 |
| **P30 "RipSetCocoaCNCH12: Dataset for Ripeness Stage Detection"** | Restrepo-Arias, J.F.; Salinas-Agudelo, M.I.; Hernandez-Pérez, M.I.; et al. | 2023 | *Data* | 5 smartphones. 8AM-4PM. Trayectoria zigzag. 1:1 aspect ratio, 3000×3000px. Respalda horarios 8AM-4PM. | 10.3390/data8070112 |
| **P34 "A Dynamic Kalman Filtering for Multi-Object Fruit Tracking"** | Zhai, Y.; Zhang, L.; Hu, X.; Yang, F.; Huang, Y. | 2025 | *Sensors* | YOLOv8n + Kalman dinámico + camera motion compensation. **MOTA 95.0%, HOTA 82.4%.** R² = 0.85. | 10.3390/s25134138 |
| **P35 "AgriSORT: Online Real-time Tracking-by-Detection for Agriculture"** | — | 2023 | *arXiv* | Kalman Filter adaptado a agricultura con compensación de movimiento de cámara vía optical flow. | arXiv:2309.13393 |
| **P37 "Apple detection Redmi Note 7 + YOLOv8n"** | — | 2025 | *Plants* | Redmi Note 7. **Distancia 0.3-1.5m.** 5 condiciones de luz. Android app desplegada. | Semantic Scholar |
| **P40 "Flash-No-Flash controlled illumination for fruit detection"** | Kurtser, P. et al. | — | — | Exposición fija a **20 µs** (mínima) para eliminar efectos de iluminación. FNF: Precision 95% a Recall 95%. | Semantic Scholar |
| **P47 "In Field Fruit Sizing Using A Smart Phone Application (FruitSize)"** | Wang, Z.; Koirala, A.; Walsh, K.; Anderson, N.; Verma, B. | 2018 | *Sensors* | **Distancia 120-300 mm, ángulo <14°.** App que rechaza imágenes fuera de especificación. Control de calidad integrado. | 10.3390/s18103331 |
| **P48 "Real-time kiwifruit detection in orchard using deep learning on Android smartphones"** | Zhou, Z.; Song, Z.; Fu, L.; et al. | 2020 | *Scientia Horticulturae* | **Huawei P20.** Selfie stick a ~1 m bajo dosel, cámara hacia arriba. App KiwiDetector. TDR 90.8%. | 10.1016/j.scienta.2020.110160 |
| **P72 "Assessing the Performance of RGB-D Sensors for 3D Fruit Crop Canopy Characterization under Different Operating and Lighting Conditions"** | — | 2020 | *Sensors* | **Compara 1.5m vs 2.5m.** 1.5m: 200.5% más densidad de nube de puntos. 2.5m: mejor penetración en dosel. | 10.3390/s20247072 |
| **P77 "AgRowStitch: A High-fidelity Image Stitching Pipeline for Ground-based Agricultural Images"** | — | 2025 | *arXiv* | **iPhone 13 Pro** en monopod. Caminata manual. Cámara a 1.5m altura, ~1.5m del dosel. 4K 30fps, frames a 10fps. | arXiv:2503.21990 |
| **P78 "In-Orchard Sizing of Mango Fruit: Comparison of Machine Vision Based Methods for On-The-Go Estimation"** | — | 2022 | *Horticulturae* | **Velocidad ~6 km/h.** Distancia 1-3m. YOLOv3/v4/v7. RMSE 4.7mm. | 10.3390/horticulturae8121223 |
| **P103 "FEGW-YOLO: Feature-Complexity-Guided Lightweight Framework"** | — | 2026 | *PMC* (PMC12944136) | YOLOv8n retiene **71.9% mAP@0.5** a blur severo (k=11). Degradación solo ~21.4% vs 86.4% de [P68]. ❌ **Matiza** magnitud de degradación por blur. | PMC12944136 |
| **P105 "A Novel Knowledge Distillation Framework for Small Object Detection in Blurry Environments"** | — | 2024 | *Springer* | Al 100% velocidad de motion, YOLOv8 pierde solo **4.6% mAP@0.5**. Con KD: solo **2.5% drop**. ❌ **Contradice** degradación extrema. | 10.1007/s40747-024-01676-w |
| **P106 "Delving into YOLO Object Detection Models: Insights into Adversarial Robustness"** | — | 2025 | *MDPI Electronics* | YOLOv4: ~15% drop por blur. YOLOv11: ~25% drop. Versiones nuevas NO son más robustas. | 10.3390/electronics14081624 |
| **P112 "Full-Surface Detection of Apple Fruits Using Enhanced YOLOv5 — Orientation Study"** | — | 2025 | *Springer* | Sideways orientation: **mAP 95%**, F1 90.58. Stem up: 86%. Stem down: 91.7%. ❌ **Contradice** 15° up como óptimo. | 10.1007/s44462-025-00020-w |
| **P113 "Cluster Segmentation and Stereo Vision-Based Apple Localization for Robotic Harvesting"** | — | 2025 | *Frontiers in Plant Science* | Tested 0°, 15°, 30°, **45°**: mejor tasa >40%. ❌ **Contradice**: 45° supera a 15°. | 10.3389/fpls.2025.1598414 |
| **P115 "Stereo Vision-Based Detection of Loose Oil Palm Fruits"** | — | 2024 | — | 30 cm: 97.63% accuracy, F1=0.99. 50 cm: MAPE 0.86%. ❌ **Contradice** distancia 0.8-1.5m para frutos pequeños. | — |
| **P117 "YOLOv8n-CSE: A Model for Detecting Litchi in Nighttime Environments"** | — | 2024 | — | LED matrix (210-350 Lux). Night: **mAP@0.5 = 98.86%**, F1 = 95.54%. ✅ **Mejora**: noche con LED superior a día. | — |
| **P118 "Nighttime Harvesting of OrBot (Orchard RoBot)"** | — | 2024 | — | Night: **94%** harvesting success. Day: **88%**. LED 5600K, 10% intensity. ✅ **Mejora**: noche > día. | — |
| **P119 "YOLO-P: An Efficient Method for Pear Fast Detection in Complex Orchard Environment"** | — | 2022 | *Frontiers in Plant Science* | Night with 1000 lm: **F1 96.1%**. Natural light: ~93%. ✅ **Mejora**: noche con luz artificial > día. | 10.3389/fpls.2022.1089454 |
| **P120 "The Effect of Illumination on HSV Colour Segmentation for Tomato"** | — | 2024 | — | Mínimo **3,000 lx** requerido. Nublado: 1,000-2,000 lx → insuficiente. ❌ **Contradice** "nublado ideal". | — |
| **P121 "Burst Photography for High Dynamic Range and Low-Light Imaging (HDR+)"** | Hasinoff, S. et al. | 2016 | *ACM Trans. Graphics* | Burst de frames subexpuestos combinados. "Shorter than typical exposure times... reducing motion blur". ✅ **Mejora**: burst > exposición única. | ACM TOG 2016 |
| **P122 "DEBIR: Dynamic Exposure Burst Image Restoration"** | — | 2026 | *arXiv* | BAENet predice exposición por frame adaptativamente. Preview 1/120s, burst con exposiciones variables. ✅ **Mejora**: exposición adaptativa > fija. | arXiv:2603.21784 |
| **P124 "Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification"** | — | 2023 | *arXiv* | MOT17: HOTA **64.9** vs ByteTrack 63.1. DanceTrack: **61.3** vs ByteTrack 47.3. ✅ **Mejora**: Deep OC-SORT supera ByteTrack. | arXiv:2302.11813 |
| **P125 "FTO-SORT: Fast Track-id Optimizer for Enhanced Multi-Object Tracking"** | — | 2025 | *Computers and Electronics in Agriculture* | **IDF1 90.2%** (+18.0% sobre baseline). Sin Re-ID: ~10× más rápido en edge. ✅ **Mejora**: farm-specific tracking optimizer. | 10.1016/j.compag.2025.110540 |
| **P126 "LOCALIZESORT: Localization-Based Stationary Object Tracking in Precision Agriculture"** | — | 2026 | *SSRN* | World-coordinate association. Mango count error: **187** vs DeepSORT 263, StrongSORT 217. ✅ **Mejora**: reduce sobreconteo. | 10.2139/ssrn.4829514 |
| **P127 "PineSORT: Simple Online Real-Time Tracking Framework for Drone Videos in Agriculture"** | — | 2025 | *CVPR 2025 Workshops* | Motion direction cost + ORB camera compensation + 3-stage association. ✅ **Mejora**: tracker CVPR para agricultura. | 10.1109/CVPRW67362.2025.00012 |

---

## 🟡 NIVEL 3 — IMPACTO CONTEXTUAL (Información General)

Papers que aportan contexto general o referencias metodológicas sin impacto directo en valores del protocolo.

| ID | Título | Autores | Año | Publicación | Resumen | Link / DOI |
|---|---|---|---|---|---|---|
| **P39 "Hawthorn detection with Huawei Nova 7"** | — | 2025 | *Sensors* | **Huawei Nova 7.** Distancia 0.1-1.0m. 3 ángulos (overhead, level, upward). 3 condiciones de luz. | Semantic Scholar |
| **P45 "Apple fruit recognition with MSX thermal imaging"** | Feng, J.; Zeng, L.; He, L. | 2019 | *Sensors* | Cámara térmica FLIR. Distancia 1-1.5m. Ángulo óptimo -16°. Imágenes 9AM. Contexto para ángulo de cámara. | 10.3390/s19040927 |
| **P54 "Real Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT"** | Parico, A.I.B.; Ahamed, T. | 2021 | *Sensors* | **DJI Osmo Pocket + móvil.** 1920×1080 30fps / 4K 60fps. Día nublado. Video desde abajo del árbol. | 10.3390/s21144803 |
| **P63 "Kiwifruit Detection in Orchard Conditions Using a FCN with Preprocessing"** | — | 2020 | *arXiv* | Sin preprocesamiento: **F1 0.82** en imágenes normales vs **0.13** con glare. Luz no controlada destruye detección. | arXiv:2006.11729 |
| **P128 "CoTracker3 — Adaptive Vision-Guided Robotic Arm Control for Precision Pruning"** | — | 2025 | *arXiv* | Point tracking transformer. **93%** pruning success. Error: 0.23mm. **27% faster** than LoCoTrack. Joint tracking para oclusiones. | arXiv:2504.07309 |
| **P129 "Transformer-Based Spatio-Temporal Association of Apple Fruitlets"** | — | 2025 | *arXiv* | Shape + position encoding + transformer attention. **F1 92.4%** (vs ICP 89.5%, Desc 86.4%). Cross-day matching. | arXiv:2503.03200 |
| **P130 "MOT-DETR-3D: Single Shot Detection and Tracking with Transformers for Agro-Food Robots"** | — | 2023 | *arXiv* | HOTA **60.4**, MOTA **70.38** vs FairMOT 46.06/51.49. 3D data mejora tracking de objetos similares. | arXiv:2311.15674 |

---

## Papers sin ID asignado [—] referenciados en P3

Papers mencionados en el P3 que no tienen ID en la Tabla Maestra:

| Referencia en P3 | Título / Descripción | Año | Contexto |
|---|---|---|---|
| OrBot nighttime | Nighttime Harvesting of OrBot (Orchard RoBot) | 2024 | Iluminación nocturna con LED (94% noche vs 88% día) |
| Mango multi-view | Image Based Mango Fruit Detection Using Multiple View Geometry | 2016 | Multi-view: error 1.36% en conteo |
| WRA-Net | Deblurring agrícola con WRA-Net | 2024 | Restauración mejora mIOU de 0.63 a 0.74 |
| Motion Blur Wheat | Motion blur wheat detection con YOLOv11 | 2025 | 10.4% más accuracy con método anti-blur |

---

## Resumen de referencias por parámetro del P3

| Parámetro del P3 | Papers Nivel 1 | Papers Nivel 2 | Papers Nivel 3 | Total |
|---|---|---|---|---|
| Velocidad de caminata | P27, P66, P70, P71, P110 | — | — | **5** |
| Ángulo de cámara | P69, P111 | P112, P113 | P39, P45 | **6** |
| Distancia al dosel | P28, P73, P114 | P37, P47, P48, P72, P78, P115 | — | **9** |
| Horario / Iluminación | P76, P116 | P29, P30, P57, P117, P118, P119, P120 | P63 | **10** |
| Shutter speed / Motion Blur | P75 | P40, P68, P103, P105, P106, P121, P122 | — | **8** |
| Tracking / Anti-doble conteo | P31, P74, P123 | P34, P35, P124, P125, P126, P127 | P128, P129, P130 | **12** |

---

*Generado desde `Tabla-Maestra-Papers.md` y `Investigacion-P3-Protocolo-Caminata.md`*
*52 referencias catalogadas + 4 con ID [—]*
*Última actualización: 05/06/2026*
