# Tabla Maestra de Papers Consultados

**Proyecto:** Protocolo de captura manual con smartphone en huertos densos de mandarinas para YOLO + MOT
**Última actualización:** 05/06/2026

---

## Categorías

| Código | Categoría |
|---|---|
| **P1** | Software de captura y bloqueo de sensores |
| **P2** | IMU / Telemetría / Estabilización |
| **P3** | Protocolo de caminata y condiciones de campo |
| **M** | Metodologías similares de captura |
| **H** | Hardware / Herramientas / Benchmarks |

---

## Tabla completa

| ID | Título | Autores | Año | Publicación | Resumen | Contexto en el proyecto | Importancia | Justifica a | Referenciado en | Link / DOI |
|---|---|---|---|---|---|---|---|---|---|---|
| **P01** | Detecting Apples in the Wild: Potential for Harvest Quantity Estimation | Janowski, A.; Kazmierczak, R.; Kowalczyk, C.; Szulwic, J. | 2021 | *Sustainability* | Usaron smartphones + GNSS para conteo de manzanas. Recomiendan YOLO sobre Viola-Jones. No documentan app de captura. | P1 — Evidencia de que papers agrícolas NO documentan software de captura. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1, Pipeline | 10.3390/SU13148054 |
| **P02** | EscaYard: Precision viticulture multimodal dataset | Vélez, S.; Ariza-Sentís, M.; Valente, J. | 2024 | *Data in Brief* | Dataset de viñedos con iPhone X, Xiaomi Poco X3 Pro, UAV. Geotagged. | P1 — Mismos hallazgos: no documentan app ni configuración. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.1016/j.dib.2024.110497 |
| **P03** | Phenotyping of individual apple tree with smartphone-based heterogeneous binocular vision | Zhao, G.; Yang, R.; Jing, X.; et al. | 2023 | *Computers and Electronics in Agriculture* | Usan cámara multi-lente de smartphone + método virtual focal para fenotipado. Mencionan calibración. | P1 — Único paper que detalla método de calibración de cámara en smartphone. | 🟡 Media | Etapa 5 — Calibración de Cámara | Investigacion-P1, Pipeline | 10.1016/j.compag.2023.107814 |
| **P04** | Toward Estimating the Crop Coefficient of Vineyards Using a Smartphone Camera | Jaramillo, J.; Vanden Heuvel, J.; Petersen, K.H. | 2025 | *American Journal of Enology and Viticulture* | Video de suelo bajo hileras de vid con smartphone. Protocolo simple: video en día soleado, segmentación + SfM. | P1 — Protocolo simple pero explícito. Sin configuración de cámara. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.5344/ajev.2025.24068 |
| **P05** | Real-time kiwifruit detection using deep learning on Android smartphones | Zhou, Z.; Song, Z.; Fu, L.; et al. | 2020 | *Computers and Electronics in Agriculture* | App Android (KiwiDetector) en Huawei P20. SSD + MobileNetV2. 8-bit quantization. | P1 — App propia, no comercial. Dataset de 100 imágenes. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.1016/j.compag.2020.105856 |
| **P06** | Framework for smartphone-based grape detection using UAV-trained AI | Vélez, S.; Ariza-Sentís, M.; Triviño, M.; et al. | 2025 | *Heliyon* | Framework con UAV + smartphone para detección de uva. MobileNetV2 cuantizado. TDR 90.8%. | P1 — Aplicación Android para detección en campo. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.1016/j.heliyon.2025.e42525 |
| **P07** | High-Throughput Image Analysis Framework for Fruit Detection from Video Streams | Huang, Y.H.; Lin, T.T. | 2019 | *ASABE* | YOLOv2 + tracking + optical flow + denoising para video de frutos en invernadero. | P1 — Pipeline de video post-captura. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.13031/aim.201900487 |
| **P08** | Correction of distortions in image analysis for phenotyping of tomato fruit | Rabelo, N.G.; Faria, S.E.S.; Matos, D.V.; et al. | 2026 | *Acta Scientiarum Agronomía* | Corrección de distorsión en imágenes de tomate con smartphone usando regresión. | P1 — Calibración de lente con smartphone para fenotipado. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.4025/actasciagron.v48i1.75604 |
| **P09** | High Throughput Image Analytics Using Hough Transformation for Wheat Phenotyping | Kim, J.Y.; Shin, M.N.; Lee, J.H.; et al. | 2022 | *Applied Engineering in Agriculture* | Smartphone + Hough transformation para rectificación de imágenes de trigo. Open-source stitching. | P1 — Pipeline de pre-procesamiento con smartphone. | 🟢 Baja | Investigación P1 (contexto) | Investigacion-P1 | 10.13031/aea.14956 |
| **P10** | A real-time fisheye video correction method based on Android smartphone GPU | Peng, Z.; Zhu, X.; Wu, J.; Qin, Z. | 2020 | *Optik* | Corrección de video fisheye en GPU Android a 25fps. RMSE ~0.67 píxeles. | P1 — Calibración de lente para smartphone, útil para lente gran angular en huerto. | 🟠 Alta | Etapa 5 — Calibración de Cámara | Investigacion-P1, Pipeline | 10.1016/j.ijleo.2020.165108 |
| **P11** | Video Stabilization for Camera Shoot in Mobile Devices via Inertial-Visual State Tracking | Han, F.; Xie, L.; Yin, Y.; Zhang, H.; Chen, G.; Lu, S. | 2021 | *IEEE Trans. Mobile Computing* | Fusión IMU + visión para estabilización. 32% mejor que SOTA. 32.6ms latencia. Probado en walking, climbing, riding. | P2 — Principal respaldo de que estabilización IMU supera a óptica en caminata. | 🔴 Crítico | Etapa 2 — Estabilización (IMU) | Investigacion-P2, Pipeline | IEEE |
| **P12** | Deep Online Video Stabilization Using IMU Sensors | Li, C.; Song, L.; Chen, S.; Xie, R.; Zhang, W. | 2023 | *IEEE Trans. Multimedia* | Sensor-driven online stabilization. 25fps en 1080p. Euler angles + acceleration de IMU. | P2 — Respaldo de IMU para estabilización en tiempo real. | 🟠 Alta | Etapa 2 — Estabilización (IMU) | Investigacion-P2, Pipeline | 10.1109/TMM.2022.3142429 |
| **P13** | Towards Visual-Inertial Integration: Multi-Modal Collaboration-based Video Stabilization | Li, C.; Bu, Y.; Xie, L. | 2025 | *IEEE ICDCS 2025* | Gyroscope + clustering + relative-depth. 47.8% SSIM mejora, 37% más rápido. | P2 — Respaldo cuantitativo más alto (47.8% SSIM). | 🔴 Crítico | Etapa 2 — Estabilización (IMU) | Investigacion-P2, Pipeline | 10.1109/ICDCS63083.2025.00107 |
| **P14** | Dual-Modality Cross-Interaction-Based Hybrid Full-frame Video Stabilization | Jang, J.S.; Ban, Y.; Lee, K. | 2024 | *Applied Sciences* | IMU motion compensation + optical flow + neural rendering. 18% Stability score. | P2 — Estabilización híbrida IMU+visión para full-frame. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | 10.3390/app14104290 |
| **P15** | A Hybrid Motion Estimation for Video Stabilization Based on an IMU Sensor | Auysakul, J.; Xu, H.; Pooneeth, V. | 2018 | *Sensors* | KLT tracker + IMU-aided motion estimator. Switching según rotación. Kalman filter. | P2 — Híbrido KLT/IMU para estabilización. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | 10.3390/s18082708 |
| **P16** | Gyroscope-Based Video Stabilization for Electro-Optical Long-Range Surveillance | Milanović, P.D.; Popadic, I.V.; Kovacevic, B.D. | 2021 | *Sensors* | Gyroscope-only stabilization. Menor complejidad computacional. Cortó ruido de movimiento a la mitad. | P2 — Respaldo de giroscopio como método eficiente vs feature-based. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | 10.3390/s21186219 |
| **P17** | IMU-Assisted Learning of Single-View Rolling Shutter Correction | Mo, J.; Islam, M.; Sattar, J. | 2020 | — | Deep network + IMU pose refinement para rolling shutter. Mejora downstream DSO. | P2 — Rolling shutter correction con IMU. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2, Pipeline | Semantic Scholar |
| **P18** | Point feature correction based rolling shutter modeling for EKF-based VIO | Zhang, K.; Zhang, M. | 2023 | *Measurement Science and Technology* | High-frequency IMU + Android phone. Supera SOTA en precisión y costo computacional. Online self-calibration. | P2 — Rolling shutter en Android con IMU. | 🟠 Alta | Etapa 2 — Estabilización (Gyroflow RS) | Investigacion-P2, Pipeline | 10.1088/1361-6501/ad044e |
| **P19** | Simultaneous Video Stabilization and Rolling Shutter Removal | Wu, H.; Xiao, L.; Wei, Z. | 2021 | *IEEE Trans. Image Processing* | Joint modeling de jitter + rolling shutter. Superior a SOTA. | P2 — Tratamiento conjunto de estabilización + RS. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | 10.1109/TIP.2021.3073865 |
| **P20** | Robust Single Image Deblurring Using Gyroscope Sensor | Ji, S.W.; Hong, J.P.; Lee, J.; Baek, S.; Ko, S.J. | 2021 | *IEEE Access* | Gyroscope guidance para deblurring. Mejora feature detectors/descriptors. | P2 — Deblurring guiado por giroscopio. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | 10.1109/ACCESS.2021.3084968 |
| **P21** | Inertial-aided Motion Deblurring with Deep Networks | Mustaniemi, J.; Kannala, J.; Särkkä, S.; Matas, J.; Heikkilä, J. | 2018 | — | Gyroscope + CNN. Tiempo real. Maneja blur no-uniforme mejor que baselines. | P2 — Pionero en deblurring con IMU. | 🟢 Baja | Investigación P2 (contexto) | Investigacion-P2 | Semantic Scholar |
| **P22** | IMU-aided adaptive mesh-grid based video motion deblurring | Arslan, A.; Gultekin, G.K.; Saranli, A. | 2024 | *PeerJ Computer Science* | IMU-informed adaptive mesh. **5% PSNR gain, 19% menos cómputo.** | P2 — Mejor métrica cuantitativa de deblurring con IMU. | 🔴 Crítico | Etapa 6 — Pre-procesamiento (Deblurring) | Investigacion-P2, Pipeline | 10.7717/peerj-cs.2540 |
| **P23** | Sensor Logger: A Framework for Smartphone-based Sensor Data Collection | Choi, K.T.H. | 2024 | *CEUR Workshop* | Paper que valida Sensor Logger para investigación científica. App multi-plataforma con exportación CSV/JSON. | P2 — Valida la app Sensor Logger como herramienta de investigación. | 🔴 Crítico | Etapa 3 — Logging IMU, Etapa 4 — Sincronización | Investigacion-P1, Pipeline | CEUR-WS |
| **P24** | Mobile AR Sensor (MARS) Logger | — | 2020 | *arXiv* | Logger para SLAM. Sincronización Camera2 API + SensorEvent. Offsets <5ms. | P2 — Fundamento técnico de sincronización video-IMU en Android. | 🟠 Alta | Etapa 4 — Sincronización Video-IMU | Pipeline | arXiv:2001.00470 |
| **P25** | Influence of Sampling Rate on IMU Orientation Estimation for Human Movement | Fan, B. et al. | 2025 | *Sensors* | **100 Hz suficiente para walking.** 200 Hz para running. Acelerómetro >100 Hz degrada precisión. | P2 — Resuelve la pregunta de frecuencia de muestreo IMU óptima. | 🔴 Crítico | Etapa 3 — Logging IMU (frecuencia 100Hz) | Investigacion-P2, Pipeline, Metodologia | 10.3390/s25071976 |
| **P26** | Non-Linear Filter for Video Stabilization + Rolling Shutter on Mobile Devices | Bell; Troccoli; Pulli | 2014 | *ECCV* | Gyroscope-based stabilization + RS correction. Real-time. Supera feature-based. Fundamento de Gyroflow. | P2 — Paper clásico, cita obligada para justificar estabilización IMU. | 🟠 Alta | Etapa 2 — Estabilización (Gyroflow), Etapa 6 — Pre-procesamiento | Pipeline | NVIDIA Research |
| **P27** | Sensor Fusion of a Mobile Device to Acquire Videos of Coffee Branches | Ramos Giraldo, P.J.; Guerrero Aguirre, A.; Muñoz, C.M.; Prieto, F.A.; Oliveros, C.E. | 2017 | *Sensors* | Samsung Galaxy S5, 1080p 30fps, AUTO (ISO/WB), IMU para blur detection. Velocidad 3 cm/s. Holder con botones. Ángulo 11.3°. | P1+P3+M — Metodología más parecida a la nuestra. Usan AUTO + IMU correctivo vs nuestro preventivo. | 🔴 Crítico | Investigación P1, P3 (referencia metodológica) | Investigacion-P1, Metodologia | 10.3390/s17040786 |
| **P28** | Using YOLOv3 Algorithm with Pre- and Post-Processing for Apple Detection | Kuznetsova, A.; Maleva, T.; Soloviev, V. | 2020 | *Agronomy* | Nikon D3500. **Compara 4 distancias: 0.2, 0.5, 1.0, 2.0m.** 4 condiciones de luz. Varias resoluciones. Pre/post-processing. | P3 — Único paper que compara distancias con métricas. Crítico para justificar distancia 0.5-1.5m. | 🔴 Crítico | Etapa 7 — Distancia al dosel 0.5-1.5m, Parámetros de captura | Pipeline, Metodologia | 10.3390/agronomy10071016 |
| **P29** | YOLOv5s-FP: Pear Detection with Transformer Encoder | Li, L. et al. | 2023 | *Sensors* | Cámaras CCD en trípode + UAV DJI Phantom 4. 4 horarios (7-8AM, 10-11AM, 2-3PM, 6-7PM). Velocidad UAV 1 m/s. Ángulo 20°-80°. | P3 — Metodología multi-horario para cubrir condiciones de luz variables. | 🟡 Media | Investigación P3 (contexto horarios) | Metodologia | 10.3390/s23010030 |
| **P30** | RipSetCocoaCNCH12: Dataset for Ripeness Stage Detection | Restrepo-Arias, J.F.; Salinas-Agudelo, M.I.; Hernandez-Pérez, M.I.; et al. | 2023 | *Data* | 5 smartphones. 8AM-4PM. Trayectoria zigzag. 1:1 aspect ratio, 3000×3000px. Anotación CVAT. | P3+M — Metodología multi-dispositivo, zigzag. Respalda horarios 8AM-4PM. | 🟡 Media | Investigación P3 (contexto horarios, multi-dispositivo) | Investigacion-P1, Metodologia | 10.3390/data8070112 |
| **P31** | Deep-learning-based orange counting via video sequences (OrangeYolo + OrangeSort) | — | 2024 | *Computers and Electronics in Agriculture* | Rover + DJI Osmo Action. **2 m/s uniforme.** Cámara perpendicular. 60fps 1080p. FOV 145°. MAE = 0.081. | P3 — Velocidad de captura para tracking. Estrategia anti-doble conteo (OrangeSort). | 🔴 Crítico | Etapa 7 — Velocidad de caminata, Estrategia anti-doble conteo | Pipeline, Metodologia | GitHub: I3-Laboratory/orange-dataset |
| **P32** | Strawberry longitudinal dataset (LabFruits) | Kirk, R. et al. | 2020 | *University of Lincoln* | 3 cámaras a 45°. Plataforma robótica Thorvald. 3 veces/día, 3 veces/semana, 2 meses. 1920×1080. Datos climáticos. | M — Metodología longitudinal con múltiples vistas y datos ambientales. | 🟡 Media | Metodologías similares (referencia) | Metodologia | GitHub: RaymondKirk/labfruits_dataset |
| **P33** | Fruits hidden by green: YCCB-YOLO for young citrus | Ang, G.; Zhiwei, T.; Wei, M.; et al. | 2024 | *Frontiers in Plant Science* | **Redmi K60 Ultra.** Fotos + video con keyframes. 3 períodos (mañana, mediodía, tarde). 1400 imágenes. LabelImg. | M — Metodología más cercana a nuestro cultivo (cítricos). Usan video + keyframes. | 🟡 Media | Metodologías similares (cítricos, video) | Metodologia | 10.3389/fpls.2024.1375118 |
| **P34** | A Dynamic Kalman Filtering for Multi-Object Fruit Tracking | Zhai, Y.; Zhang, L.; Hu, X.; Yang, F.; Huang, Y. | 2025 | *Sensors* | YOLOv8n + Kalman dinámico + camera motion compensation. **MOTA 95.0%, HOTA 82.4%.** R² = 0.85. | P2+M — Tracking con compensación de movimiento de cámara. Útil para pipeline MOT. | 🟠 Alta | Etapa 7 — Tracking MOT (referencia de métrica) | Metodologia | 10.3390/s25134138 |
| **P35** | AgriSORT: Online Real-time Tracking-by-Detection for Agriculture | — | 2023 | *arXiv* | Tracking con Kalman Filter adaptado a agricultura. Compensación de movimiento de cámara con optical flow. | P2+M — Algoritmo de tracking específico para agricultura con cámara en movimiento. | 🟠 Alta | Etapa 7 — Tracking MOT (algoritmo especializado) | Metodologia | arXiv:2309.13393 |
| **P36** | Coffee cherry counting with YOLOv8 + farmers | — | 2024 | *Precision Agriculture* | **Farmers con sus smartphones.** 3 ramas/árbol. 6AM-6PM. Sin sol directo. Res: 768×768 a 1024×1024. 2,968 árboles. | M — Protocolo masivo simplificado. Demuestra que farmers pueden capturar con smartphones sin entrenamiento. | 🟡 Media | Metodologías similares (protocolo masivo) | Metodologia | Semantic Scholar |
| **P37** | Apple detection Redmi Note 7 + YOLOv8n | — | 2025 | *Plants* | Redmi Note 7. **Distancia 0.3-1.5m.** 5 condiciones de luz. Android app desplegada. Distancia entre hileras 4m. | P3 — Distancia 0.3-1.5m y 5 condiciones de luz validadas para detección. | 🔴 Crítico | Etapa 7 — Distancia al dosel, Condiciones de luz | Pipeline, Metodologia | Semantic Scholar (PDF) |
| **P38** | DHN-YOLO: strawberry detection ridge-type | — | 2025 | — | Smartphone cámara trasera. **50-80cm, ángulo 45°.** 2066 imágenes. Res: 1024×768. Aumentación a 5018. | P3 — Distancia y ángulo para fresas en ridge-planting. | 🟡 Media | Investigación P3 (contexto distancia/ángulo) | Metodologia | Semantic Scholar |
| **P39** | Hawthorn detection with Huawei Nova 7 | — | 2025 | *Sensors* | **Huawei Nova 7.** Distancia 0.1-1.0m. 3 ángulos (overhead, level, upward). 3 condiciones de luz (backlight, front, normal). | P3 — Múltiples ángulos y distancias con smartphone. | 🟡 Media | Investigación P3 (contexto ángulos) | Metodologia | Semantic Scholar |
| **P40** | Flash-No-Flash controlled illumination for fruit detection | Kurtser, P. et al. | — | — | Exposición fija a 20µs (mínima) para eliminar efectos de iluminación. FNF mejora detección: Precision 95% a Recall 95%. | P1 — Respalda que estabilizar condiciones de captura mejora detección. | 🔴 Crítico | Etapa 1 — App de Cámara (bloqueo AE/AF/WB) | Pipeline | Semantic Scholar |
| **P41** | ICNet: Illumination Compensation for Intercropping | — | 2025 | — | Compensación de iluminación mejora PSNR de 28dB a 40.79dB. Demuestra que iluminación variable degrada detección. | P1 — Evidencia de que iluminación no controlada afecta detección. | 🟠 Alta | Etapa 1 — App de Cámara (bloqueo AE) | Pipeline | Semantic Scholar |
| **P42** | DCNet: Low-visibility fruit detection | — | 2025 | — | Detección en baja visibilidad. 86.5% mAP. Demuestra que condiciones adversas degradan significativamente la detección. | P1 — Apoya la necesidad de controlar condiciones de captura. | 🟠 Alta | Condiciones de captura (control de iluminación) | Pipeline | Semantic Scholar |
| **P43** | Gimbal influence on exterior orientation parameters (UAV) | Gašparović, M.; Jurjević, L. | — | *Sensors* | **Gimbal mejora 6x estabilidad.** Roll/pitch 69.9° sin gimbal → 2.56° con gimbal. | H — Respaldo cuantitativo del uso de gimbal para estabilización. | 🔴 Crítico | Etapa 2 — Estabilización (Gimbal) | Pipeline | Semantic Scholar |
| **P44** | EMA-YOLO: yellow peach detection | — | — | — | Smartphone a diferentes distancias. Compara corta, media y larga distancia. Muestra que distancia afecta detección. | P3 — Evidencia de que distancia impacta mAP. | 🟡 Media | Investigación P3 (contexto distancia) | Pipeline | Semantic Scholar |
| **P45** | Apple fruit recognition with MSX thermal imaging | Feng, J.; Zeng, L.; He, L. | 2019 | *Sensors* | Cámara térmica FLIR. Distancia 1-1.5m. Ángulo óptimo -16°. Imágenes 9AM. | P3 — Ángulo de cámara óptimo documentado. | 🟡 Media | Investigación P3 (contexto ángulo) | Metodologia | 10.3390/s19040927 |
| **P46** | An Advanced Photogrammetric Solution to Measure Apples Using Smartphone-Based Videos | Grilli, E.; Battisti, R.; Remondino, F. | 2021 | *Remote Sensing* | Video con smartphone desde múltiples posiciones/ángulos. Máscaras de segmentación con Mask R-CNN. Esfera fitting para medición de tamaño. | M — Fotogrametría con smartphone para medición de frutos. Sin bloqueo de parámetros. | 🟡 Media | Metodologías similares (fotogrametría con smartphone) | Metodologia (búsqueda) | 10.3390/rs13193960 |
| **P47** | In Field Fruit Sizing Using A Smart Phone Application (FruitSize) | Wang, Z.; Koirala, A.; Walsh, K.; Anderson, N.; Verma, B. | 2018 | *Sensors* | **Distancia 120-300 mm, ángulo <14°.** App que rechaza imágenes fuera de especificación. Blue backboard + referencia amarilla. | P3 — Control de calidad integrado en app. Distancia y ángulo máximos documentados. | 🟠 Alta | Etapa 5 — Control de calidad en captura, Distancia al dosel | Metodologia (búsqueda) | 10.3390/s18103331 |
| **P48** | Real-time kiwifruit detection in orchard using deep learning on Android smartphones | Zhou, Z.; Song, Z.; Fu, L.; et al. | 2020 | *Scientia Horticulturae* | **Huawei P20.** Selfie stick a ~1 m bajo dosel, cámara hacia arriba. App KiwiDetector. SSD + MobileNetV2. 89.7% detección. | P1+M — App Android propia para detección en campo. Distancia y ángulo definidos sin bloqueo de parámetros. | 🟡 Media | Metodologías similares (app Android, selfie stick) | Metodologia (búsqueda) | 10.1016/j.scienta.2020.110160 |
| **P49** | Designing a Proximal Sensing Camera Acquisition System for Vineyard Applications: 8 Years of Experiments | Rançon, F.; Keresztes, B.; Deshayes, A.; et al. | 2023 | *Sensors* | **Cámara industrial Basler Ace + flash xenon.** Exposición 250 µs, obturador global. App Android para control remoto vía Wi-Fi. 8 años de desarrollo. | H — Iluminación controlada + obturador global eliminan motion blur. Respalda fijar shutter speed. | 🟠 Alta | Etapa 1 — App de Cámara (shutter controlado), Etapa 6 — Iluminación | Metodologia (búsqueda) | 10.3390/s23020847 |
| **P50** | Smart Agriculture: Fruit Flower Cluster Detection in Apple Orchards Using Machine Vision | — | 2022 | *Applied Sciences* | Microsoft Azure Kinect DK (RGB-D + giroscopio + acelerómetro). Trípode + vehículo móvil. Ambos lados del árbol escaneados. | M — Uso de sensor RGB-D con IMU integrado para detección en huerto. Ambos lados del árbol. | 🟡 Media | Metodologías similares (RGB-D, doble lado) | Metodologia (búsqueda) | 10.3390/app122211420 |
| **P51** | Row-based kiwifruit counting pipeline for smartphone-captured videos | Zhang, J. et al. | 2025 | *Computers and Electronics in Agriculture* | **Smartphone + estabilizador + palo extensible.** Vista hacia arriba. YOLOv8m + ByteTrack. R² = 0.9791. TCV elimina sobreconteo. | M — Metodología más cercana a nuestro enfoque: gimbal + smartphone + video de hilera completa. | 🟠 Alta | Metodologías similares (gimbal + smartphone, hilera completa) | Metodologia (búsqueda) | 10.1016/j.compag.2025.104976 |
| **P52** | Development of a Cross-Platform Mobile Application for Fruit Yield Estimation | — | 2024 | *AgriEngineering* | **Samsung Galaxy Tab S7.** Distancia ~2.5 m. Fotos desde este y oeste. MAPE 8.52%. Sin filtros ni configuración especial. | M — Metodología simple tipo farmer. Distancia 2.5m documentada. Sin control de parámetros. | 🟢 Baja | Metodologías similares (captura simple, doble lado) | Metodologia (búsqueda) | 10.3390/agriengineering6020105 |
| **P53** | Vision System for Automatic On-Tree Kiwifruit Counting and Yield Estimation | — | 2020 | *Sensors* | **Minitractor + gimbal.** Cámara hacia arriba. 3 fps. GPS cada 5s. Velocidad ~2 km/h. Error 6-15%. | M — Vehículo con gimbal para captura de kiwi. Velocidad y equipo documentados. | 🟡 Media | Metodologías similares (gimbal en vehículo) | Metodologia (búsqueda) | 10.3390/s20154214 |
| **P54** | Real Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT | Parico, A.I.B.; Ahamed, T. | 2021 | *Sensors* | **DJI Osmo Pocket + móvil.** 1920×1080 30fps / 4K 60fps. Día nublado. Video desde abajo del árbol. YOLOv4 + Deep SORT. | M — Comparativa de dos dispositivos para captura en huerto. Metodología sistemática documentada. | 🟡 Media | Metodologías similares (múltiples dispositivos, video desde abajo) | Metodologia (búsqueda) | 10.3390/s21144803 |
| **P55** | Rice Grain Moisture Content Measurement with Smartphone (Rice GMC) | — | 2021 | *Sensors* | **iPhone 8. ISO=25 fijo, shutter=1/400s, f/1.8, distancia 27.5cm.** "To minimize lighting-related factors, the smartphone camera parameters were fixed". | P1 — Paper que demuestra la necesidad de fijar parámetros en campo con justificación explícita. Citado en Pipeline. | 🟠 Alta | Etapa 1 — App de Cámara (ISO fijo, shutter fijo) | Investigacion-P1, Pipeline | Semantic Scholar (PDF rice GMC) |
| **P56** | Spherical Self-Calibration for Video Stabilization Based on Gyroscope | — | 2021 | *Information* | Estabilización basada en giroscopio + auto-calibración de radio esférico. Supera a métodos con matriz de parámetros intrínsecos. Mejora PSNR, SSIM. | P2 — Respalda uso de giroscopio para estabilización sin necesidad de calibración de cámara. | 🟡 Media | Investigación P2 (contexto estabilización IMU) | Investigacion-P1 | Semantic Scholar |
| **P57** | Overcurrent-driven LEDs for Consistent Image Colour and Brightness in Agricultural Machine Vision | — | 2021 | *Computers and Electronics in Agriculture* | **85% reducción** variación HSV con LED fijo vs auto-exposición. Error motion blur 7mm→1mm a 7km/h. Auto-exposición falla catastróficamente con sol frontal. | P1 — Demuestra que parámetros fijos + iluminación controlada eliminan variabilidad. Respalda fijar ISO/shutter. | 🔴 Crítico | Etapa 1 — App de Cámara (ISO/shutter fijo), Etapa 6 — Iluminación | Búsqueda P1 | ScienceDirect |
| **P58** | Land-based Crop Phenotyping by Image Analysis: Consistent Canopy Characterization from Inconsistent Field Illumination | — | 2018 | *Plant Methods* | **Error MSE: 1.57 (manual) vs 4.26 (auto)** bajo iluminación cambiante. Exposición manual + corrección de color es superior. | P1 — Comparación directa manual vs auto. Manual es 2.7x más consistente. | 🔴 Crítico | Etapa 1 — App de Cámara (AE Lock, exposición manual) | Búsqueda P1 | Springer |
| **P59** | A Robust Illumination-Invariant Camera System for Agricultural Applications | — | 2021 | *arXiv* | Redes entrenadas con imágenes consistentes requieren **4x menos datos**. Faster-RCNN: AP 0.71 con iluminación controlada vs casi 0 con luz natural extrema. | P1 — Parámetros fijos reducen datos necesarios para entrenar. Respalda bloqueo de exposición. | 🟠 Alta | Etapa 1 — App de Cámara (consistencia de captura) | Búsqueda P1 | arXiv:2101.02190 |
| **P60** | Optimizing Image Acquisition Systems for Autonomous Driving (CNN + Exposure) | — | 2018 | *Stanford / Google Research* | El paper demuestra que redes entrenadas con exposiciones específicas no generalizan bien a exposiciones diferentes. Las CNN son asimétricas: manejan mejor sub-exposición que sobre-exposición. Entrenar con mezcla de exposiciones ayuda pero reduce precisión óptima. ⚠️ **NOTA**: La cifra de "~20% caída de precisión" no pudo ser verificada en el paper original encontrado. El paper SÍ demuestra que exposiciones subóptimas degradan significativamente CNNs, pero el valor exacto requiere verificación. | P1 — Evidencia de que exposición inconsistente degrada CNN. Respalda AE Lock. | 🟡 Media | Etapa 1 — App de Cámara (AE Lock) | Búsqueda P1 | Stanford 2018 |
| **P61** | Stabilizing and Accelerating Autofocus with Expert Trajectory Regularized Deep RL | — | 2025 | *CVPR* | Focus hunting (FH) causa que el lente oscile repetidamente creando **inestabilidad en video**. FH reduce nitidez y cambia el FoV. | P1 — Documenta que el focus hunting es un problema real. Respalda AF Lock. | 🟠 Alta | Etapa 1 — App de Cámara (AF Lock) | Búsqueda P1 | CVPR 2025 |
| **P62** | A Calibration Method for Smartphone Camera Photoplethysmography (Camera2 API) | — | 2023 | *Frontiers in Digital Health* (PMC10705321) | Tone mapping automático aplica **transformaciones no lineales irreversibles** ("cannot be reversed in post processing"). Camera2 API permite configurar tone mapping lineal. **74% menor MAE** con calibración. WB lock esencial para color consistente. | P1 — Valida Camera2 API para control manual en investigación. El tone mapping lineal vía Camera2 API logra 74% menos error. Respalda Camera2 API + WB Lock. | 🔴 Crítico | Etapa 1 — App de Cámara (Camera2 API, WB Lock, tone mapping) | Búsqueda P1 | 10.3389/fdgth.2023.1301019 |
| **P63** | Kiwifruit Detection in Orchard Conditions Using a FCN with Preprocessing | — | 2020 | *arXiv* | Sin preprocesamiento: **F1 0.82** en imágenes normales vs **0.13** en imágenes con glare. Luz no controlada destruye detección. | P1 — Demuestra que condiciones de luz adversas degradan severamente la detección. | 🟡 Media | Etapa 1 — Condiciones de captura | Búsqueda P1 | arXiv:2006.11729 |
| **P64** | DeepOIS: Gyroscope-Guided Deep Optical Image Stabilizer Compensation | — | 2021 | *arXiv* | **OIS interfiere con estabilización por giroscopio.** Error alineación: 0.688 (sin OIS) vs 1.038 (con OIS) — **50% peor**. "OIS terminates the possibility of image registration by gyros." | P2 — Evidencia directa de que OIS interfiere con Gyroflow. Justifica regla OIS OFF. | 🔴 Crítico | Etapa 2 — Regla OIS OFF | Búsqueda P2 | arXiv:2101.11183 |
| **P65** | Image Stabilization Influence on Photogrammetric Accuracy | — | 2022 | *ISPRS* | **IS debe desactivarse** para modelado 3D. Incertidumbre en parámetros **hasta 300% mayor** con IS activado. Error de reproyección **4x mayor**. | P2 — Respalda desactivar OIS desde fotogrametría. Corrobora regla OIS OFF. | 🟠 Alta | Etapa 2 — Regla OIS OFF | Búsqueda P2 | ISPRS |
| **P66** | Mango Fruit Load Estimation Using Video Based MangoYOLO-Kalman Filter-Hungarian Algorithm | — | 2019 | *Sensors* | Video detection: **62.3%** del conteo real vs **40.2%** con foto estática. **+22% mejora** usando video en movimiento. Error doble conteo 9.9%. | P2 — Demuestra que video estabilizado supera a fotos estáticas para conteo de frutos. | 🟠 Alta | Etapa 2 — Video estabilizado para detección | Búsqueda P2 | 10.3390/s19122742 |
| **P67** | Crop Row Video Stabilization for Agricultural Field Robotics | — | — | *MDPI Sensors* | Desplazamiento lateral suprimido: **66%** del espacio entre hileras. Desviación: ~20px (desde 93px inicial). | P2 — Justifica estabilización en agricultura con métricas cuantitativas. | 🟠 Alta | Etapa 2 — Estabilización en agricultura | Búsqueda P2 | MDPI Sensors |
| **P68** | Lightweight GAN for Restoring Blurred Images to Enhance Citrus Detection | — | 2025 | *MDPI* | **mAP@0.5:0.95 +86.4%** tras restaurar imágenes borrosas. Recall **+76.9%**. F1 **+40.1%**. FN rate **-63.9%**. | P2 — Motion blur degrada severamente detección YOLO. Respalda necesidad de estabilización. | 🟠 Alta | Etapa 2 — Motion blur vs YOLO | Búsqueda P2 | MDPI 2025 |
| **P69** | Fruit Detectability Analysis for Different Camera Positions in Sweet-Pepper | Hemming, J.; Ruizendaal, J.; Hofstee, J.W.; van Henten, E.J. | 2014 | *Sensors* | **Prueba 14 posiciones de cámara** con diferentes azimuth y zenith angles para medir Fruit Detectability (FD). Zenith 60° (mirando hacia arriba) dio la mejor FD. 5 posiciones combinadas alcanzaron FD=90%. | P3 — Único paper que prueba sistemáticamente múltiples ángulos de cámara para detección de frutos. Justifica ángulo 15-30° hacia arriba. | 🔴 Crítico | P3 — Ángulo de cámara óptimo | Investigacion-P3 | 10.3390/s140406032 |
| **P70** | A Comparative Study of Fruit Detection and Counting Methods for Yield Mapping in Apple Orchards | Roy, P.; Dong, Y.; Isler, V. | 2018 | *arXiv* | **Samsung Galaxy S4** a **2 m/s** caminando. Video 30fps, 1920×1080. Cámara horizontal, un solo lado de la hilera. Yield accuracy 95.56-97.83%. | P3 — Paper que demuestra captura manual con smartphone y publica la velocidad exacta. Justifica velocidad de caminata ~1-2 m/s. | 🔴 Crítico | P3 — Velocidad de caminata, protocolo de captura con smartphone | Investigacion-P3 | arXiv:1810.09499 |
| **P71** | Recognition and Counting of Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms | — | 2023 | *Sensors* | **Compara 3 velocidades (0.052/0.069/0.098 m/s) × 3 ángulos (0°/15°/30°).** YOLOv7 mAP@0.5=0.905. 15° + 0.098 m/s = RMSE 1.54cm. Counting accuracy 86.6%. | P3 — Paper que combina velocidad × ángulo con métricas de detección. Justifica ángulo 15° y relación velocidad-precisión. | 🔴 Crítico | P3 — Velocidad × Ángulo combinados | Investigacion-P3 | 10.3390/s23083810 |
| **P72** | Assessing the Performance of RGB-D Sensors for 3D Fruit Crop Canopy Characterization under Different Operating and Lighting Conditions | — | 2020 | *Sensors* | **Compara distancias 1.5m vs 2.5m** al dosel. 1.5m: 200.5% más densidad de nube de puntos. 2.5m: mejor penetración en dosel (0.922m vs 0.772m). Brillo +30.4% a 1.5m. | P3 — Comparación directa de distancia con impacto cuantitativo en calidad de datos. Justifica rango 0.8-1.5m. | 🟠 Alta | P3 — Distancia al dosel, calidad de datos | Investigacion-P3 | 10.3390/s20247072 |
| **P73** | YOLO-CSB: Real-Time Detection of Occluded Apples for Precision Agriculture | — | 2026 | *Agronomy* | **Distancia óptima 0.8-1.5m** del dosel. mAP 93.69%. Datos recolectados mañana (9-11AM, 45%) y tarde (3-5PM, 55%). septiembre-octubre. | P3 — Distancia 0.8-1.5m validada con mAP. Justifica rango óptimo de captura. | 🟠 Alta | P3 — Distancia al dosel, horarios de captura | Investigacion-P3 | 10.3390/agronomy16030390 |
| **P74** | Video-Based Fruit Detection and Tracking for Apple Counting | Gené-Mola, J.; Sanz-Cortiella, R.; Rosell-Polo, J.R.; et al. | 2023 | *Computers and Electronics in Agriculture* | **Compara SORT vs DeepSORT vs ByteTrack** para conteo de frutos en video. ByteTrack: **MOTA 0.682, IDF1 0.837, HOTA 0.689**. 15ms/frame vs DeepSORT 128ms. YOLOv5x. | P3 — Comparación de trackers para conteo de frutos. Justifica uso de ByteTrack. | 🔴 Crítico | P3 — Tracking MOT, estrategia anti-doble conteo | Investigacion-P3 | UPCommons |
| **P75** | A State-of-the-Art Review of Image Motion Deblurring Techniques in Precision Agriculture | — | 2024 | *Heliyon* | **Revisión de técnicas de deblurring.** Proporciona fórmula: `desplazamiento_px ≈ (velocidad × tiempo_exposición) / distancia_focal`. Recomienda shutter ≥1/200s para compensar walking shake. Camera shake afecta severamente la precisión. | P3 — Fundamento teórico para calcular blur según velocidad de caminata. Justifica shutter speed 1/60-1/120s. | 🟠 Alta | P3 — Motion blur, shutter speed, justificación velocidad | Investigacion-P3 | Heliyon 2024 |
| **P76** | Orchard-YOLO: A Robust Deep Learning Framework for Fruit Detection Under Complex Optical and Environmental Degradation | — | 2026 | *Photonics* | **Prueba ±50% iluminación + hasta 70% oclusión.** YOLOv13: 94.8% mAP@0.5 en condiciones normales, 61.4% en condición extrema (−50% brillo, 70% oclusión). 25 FPS en Jetson Nano. | P3 — Cuantifica el impacto de iluminación variable y oclusión en detección. Justifica horarios óptimos. | 🟠 Alta | P3 — Iluminación, horarios, oclusión | Investigacion-P3 | 10.3390/photonics13050429 |
| **P77** | AgRowStitch: A High-fidelity Image Stitching Pipeline for Ground-based Agricultural Images | — | 2025 | *arXiv* | **iPhone 13 Pro** montado en monopod (selfie stick). Caminata manual paralela a la hilera, cámara a 1.5m de altura, ~1.5m del dosel. 4K 30fps, frames extraídos a 10fps. MAE ~20cm sobre 72m de hilera. | P3 — Metodología de captura con smartphone caminando. Distancia, altura y velocidad documentadas. | 🟡 Media | P3 — Protocolo de captura manual con smartphone | Investigacion-P3 | arXiv:2503.21990 |
| **P78** | In-Orchard Sizing of Mango Fruit: Comparison of Machine Vision Based Methods for On-The-Go Estimation | — | 2022 | *Horticulturae* | **Velocidad ~6 km/h.** Compara YOLOv3/v4/v7 y tiny variants. Distancia cámara-fruto 1-3m. RMSE 4.7mm en longitud. 5fps. Cámara RGB-D ToF. | P3 — Velocidad de captura en movimiento + comparación de detectores. Justifica rango de distancia. | 🟡 Media | P3 — Velocidad de captura, distancia al dosel | Investigacion-P3 | 10.3390/horticulturae8121223 |
| **P79** | Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards | Miranda, C.; Santesteban, L.G.; Urrestarazu, J.; Loidi, M.; Royo, J.B. | 2018 | *Agriculture* | Usa **RVI (NDVI) aéreo + TCSA** para estratificar árboles con fuzzy k-means. Reduce muestra 20-35% vs aleatorio simple. 5 huertos de durazno. | P4 — Metodología de estratificación con NDVI para selección de parcelas/árboles en huertos. | 🔴 Crítico | P4 — Selección de parcelas, estratificación NDVI | Investigacion-P4 | 10.3390/agriculture8060078 |
| **P80** | Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps: A Comparative Analysis to Improve Yield and Quality Estimates | Uribeetxebarria, A.; Martínez-Casasnovas, J.A.; Escolà, A.; Rosell-Polo, J.R.; Arnó, J. | 2018 | *Precision Agriculture* | **NDVI estratificado** (2-3 estratos) reduce muestra **17%** vs SRS para estimación de rendimiento en durazno. ECa no mejoró. | P4 — Estratificación con NDVI para optimizar muestreo en huertos frutales. | 🟠 Alta | P4 — Selección de parcelas, NDVI como variable auxiliar | Investigacion-P4 | 10.1007/s11119-018-9619-9 |
| **P81** | Assessing Ranked Set Sampling and Ancillary Data to Improve Fruit Load Estimates in Peach Orchards | Martínez-Casasnovas, J.A.; Uribeetxebarria, A.; Escolà, A.; Arnó, J.; Rosell-Polo, J.R. | 2019 | *Computers and Electronics in Agriculture* | **Ranked Set Sampling (RSS)** con UAV (área de copa) reduce muestra **50%** (de N=10 a N=5). R=0.85 entre área de copa y carga frutal. | P4 — RSS como método eficiente de muestreo en huertos. Respalda reducción de tamaño de muestra. | 🟠 Alta | P4 — Muestreo eficiente, tamaño de muestra | Investigacion-P4 | 10.1016/j.compag.2019.104931 |
| **P82** | A New, Satellite NDVI-Based Sampling Protocol for Grape Maturation Monitoring | Meyers, J.M.; Dokoozlian, N.; Ryan, C.; Bioni, C.; Vanden Heuvel, J.E. | 2020 | *Remote Sensing* | **NDVI3**: 3 píxeles Landsat representando cola baja, media y alta del NDVI. Misma representatividad que 20 puntos aleatorios. Test KS. | P4 — Protocolo de muestreo basado en NDVI satelital. Aplicable a Sentinel-2 para selección de parcelas. | 🔴 Crítico | P4 — Selección de parcelas con NDVI satelital | Investigacion-P4 | 10.3390/rs12071159 |
| **P83** | Spatial Sampling of Fruit Maturity Reduces Sampling Costs for Winegrapes in California and New York | Meyers, J.M.; Vanden Heuvel, J.E. | 2024 | *American Journal of Enology and Viticulture* | Comparación costos NDVI3 vs aleatorio (R20) vs 4 esquinas. NDVI3: **0.36-1.58 km** recorrido vs R20: **3.34-13.63 km**. Ahorro $5.54-$32.40 por evento. | P4 — Eficiencia del muestreo NDVI satelital. Respalda selección de ubicaciones representativas. | 🟠 Alta | P4 — Eficiencia de muestreo, reducción de esfuerzo | Investigacion-P4 | 10.5344/ajev.2024.23067 |
| **P84** | Effectiveness of Management Zones Delineated from UAV and Sentinel-2 Data for Precision Viticulture Applications | — | 2024 | *Remote Sensing* | Compara **Sentinel-2 (10m) vs UAV (3-4cm)** para zonas de manejo. S2 captura las principales características de vigor. UAV da más precisión en bordes. | P4 — Validación de Sentinel-2 para zonificación de vigor. Respalda uso de imágenes S2 para estratificar parcelas. | 🟡 Media | P4 — Uso de Sentinel-2 para selección de parcelas | Investigacion-P4 | 10.3390/rs16040635 |
| **P85** | Machine Learning Applied to Tree Crop Yield Prediction Using Field Data and Satellite Imagery: A Case Study in a Citrus Orchard | — | 2022 | *MDPI Instruments* | **Usó mean NDVI de Sentinel-2** para **50 parcelas de cítricos** (mandarina Afourer). Demostró que el NDVI por parcela mejora la predicción de rendimiento en 4%. | P4 — Valida el uso de **NDVI medio por parcela desde Sentinel-2** para caracterizar parcelas de cítricos. | 🟠 Alta | P4 — Caracterización de parcelas con NDVI Sentinel | Investigacion-P4 | 10.3390/instruments9040080 |
| **P86** | Evaluating Sentinel-2 Red Edge for Monitoring LAI and Chlorophyll in Kinnow Mandarin Orchards | — | 2022 | *ScienceDirect* | **Evaluó índices de Red Edge (NDRE) vs NDVI** en mandarinos Kinnow con Sentinel-2. Los índices de Red Edge fueron **superiores al NDVI** para estimar LAI y clorofila. | P4 — Confirma que **NDRE es mejor que NDVI para cítricos** con Sentinel-2. Justifica uso de NDRE. | 🟠 Alta | P4 — Uso de NDRE para caracterización de cítricos | Investigacion-P4 | ScienceDirect 2022 |
| **P87** | Citrus Orchard Mapping in Juybar, Iran: Analysis of NDVI Time Series and Feature Fusion of Multi-Source Satellite Imageries | Toosi, A. et al. | 2022 | *GIScience & Remote Sensing* | **Clasificó huertos de cítricos** con Sentinel-2 usando series temporales NDVI + machine learning. **Precisión 99.7%** (SVM). Propuso EGI (Evergreenness Index). | P4 — Demuestra que **Sentinel-2 distingue huertos de cítricos de otros cultivos** a nivel de parcela. | 🟡 Media | P4 — Clasificación de parcelas de cítricos con Sentinel-2 | Investigacion-P4 | 10.1016/j.rsase.2022.100760 |
| **P88** | Multilevel Systematic Sampling to Estimate Total Fruit Number | Wulfsohn, D.; Aravena, F.; Potin, C.; Zamora, I.; García-Fiñana, M. | 2012 | *Precision Agriculture* | **SUR sistemático** en 14 huertos comerciales (kiwi, manzana, uva). Error **<5% en 6 huertos**, **5-10% en 5 huertos**, 13-20% en 3. Carga de trabajo 30-150 min. | P4 — Respalda el **muestreo sistemático uniforme (SUR)** para seleccionar hileras/árboles. Error <10% en 11/14 casos. | 🔴 Crítico | P4 — Selección de hileras (SUR sistemático) | Investigacion-P4 | Springer |
| **P89** | Phenological and Biophysical Mediterranean Orchard Assessment Using Ground-Based Methods and Sentinel-2 Data | — | 2024 | *Remote Sensing* | **Seleccionaron 14 parcelas** para representar variabilidad de suelo, riego y manejo en huertos de cereza, nectarina y albaricoque. Criterios: accesibilidad + representatividad. Usaron Sentinel-2. | P4 — Ejemplo de **selección de parcelas por criterios agronómicos** (edad, variedad, manejo) complementado con Sentinel-2. | 🟡 Media | P4 — Selección de parcelas por criterios agronómicos | Investigacion-P4 | 10.3390/rs16183393 |
| **P90** | Fruit Yield Estimation of Kinnow Mandarin Orchards — Integrating Canopy Physiology with Remote Sensing | Sun, Y.; Qin, Q.; Zhang, J.; Ren, H.; Han, R. | 2026 | *Arabian Journal of Geosciences* | **Usó Sentinel-2 Red Edge (S2REP)** combinado con LAI y clorofila para estimar rendimiento de mandarina Kinnow. R² = 0.85. Encontró variabilidad intra-huerto significativa en mandarinos. | P4 — **Cultivo más cercano a Murcott**. Valida que Sentinel-2 captura variabilidad entre parcelas de mandarinos. | 🟠 Alta | P4 — Variabilidad en mandarinos con Sentinel-2, respaldo a estratificación | Investigacion-P4 | 10.1007/s12517-026-12453-z |
| **P91** | Comparing Efficiency of Different Sampling Schemes to Estimate Yield and Quality Parameters in Fruit Orchards | Arnó, J.; Martínez-Casasnovas, J.A.; Uribeetxebarria, A.; Escolà, A.; Rosell-Polo, J.R. | 2017 | *Advances in Animal Biosciences* | **Comparó estrategias de muestreo** en huertos frutales. La estratificación por NDVI fue **significativamente más eficiente** que el muestreo aleatorio simple. Con 2 estratos se captura la mayor parte de la variabilidad. | P4 — **Valida que estratificar por NDVI es superior al azar** en huertos. Respalda la selección de extremos. | 🔴 Crítico | P4 — Estratificación NDVI > aleatorio en huertos frutales | Investigacion-P4 | 10.1017/S2040470017000978 |
| **P92** | Delineating Citrus Management Zones Using Spatial Interpolation and UAV-Based Multispectral Approaches | Longo-Minnolo, G. et al. | 2023 | *Precision Agriculture* | **Delineó zonas de manejo en cítricos** con NDVI (K-means clustering). Encontró que **3-4 zonas** son óptimas y que zonas con diferente vigor mostraron diferencias estadísticamente significativas. | P4 — **Valida en cítricos** que dividir por vigor captura diferencias reales. Respaldo directo al enfoque de estratificación. | 🟠 Alta | P4 — Zonas de manejo en cítricos con NDVI, respaldo a estratificación | Investigacion-P4 | Springer |
| **P93** | UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence | Ampatzidis, Y.; Partel, V. | 2019 | *Remote Sensing* | **Usó NDVI + YOLOv3** para fenotipado de cítricos desde UAV. NDVI correlaciona bien con tamaño de copa y sanidad. **99.9% precisión** en detección de árboles. | P4 — **Conecta NDVI + YOLO + cítricos**. Confirma que NDVI es buen predictor de vigor en cítricos. | 🟠 Alta | P4 — Correlación NDVI-vigor en cítricos, contexto YOLO | Investigacion-P4 | 10.3390/rs11040410 |
| **P94** | Sampling Strategies for Soil Property Mapping Using Multispectral Sentinel-2 and Hyperspectral EnMAP Satellite Data | Castaldi, F.; Chabrillat, S.; van Wesemael, B. | 2019 | *Remote Sensing* | **Probó estrategias de muestreo** con Sentinel-2. S2 (10m) provee resolución suficiente para crear zonas de manejo. Kennard-Stones con S2 dio nRMSE 8.7-9.2%. | P4 — **Valida que Sentinel-2 (10m) tiene resolución adecuada** para muestreo agrícola a escala de parcela. | 🟡 Media | P4 — Resolución de S2-10m para muestreo agrícola | Investigacion-P4 | 10.3390/rs11030309 |
| **P95** | Impact of ISP Tuning on Object Detection | — | 2023 | *MDPI J. Imaging* 9(12), 260 | Contraste, gamma y saturación (componentes del ISP automático) causan **degradación significativa** en YOLOv5/v8, Faster R-CNN, RT-DETR. La variación de ISP afecta **desproporcionadamente a objetos pequeños**. La mayoría de errores son **falsos negativos** (objetos no detectados). | P1 — Demuestra que el pipeline ISP automático degrada la detección YOLO. Respalda el uso de Camera2 API para desactivar procesamiento automático y usar tone mapping lineal. | 🟠 Alta | Etapa 1 — ISP tuning, degradación de detección por procesamiento automático | Investigacion-P1 | 10.3390/jimaging9120260 |
| **P96** | Why is the Video Analytics Accuracy Fluctuating, and What Can We Do About It? (Camera as Unintentional Adversary) | — | 2022 | *ECCV* | La cámara actúa como **"unintentional adversary"**: cambios automáticos de parámetros causan **13-14% fluctuación** en detección en escenas estáticas. Transfer-learning redujo errores de tracking **~40%**. Ground truth 29 tracks → modelo original creó **157 track-IDs** (5.4x falsos). | P1 — Evidencia directa de que los parámetros automáticos de cámara degradan la detección y tracking. Respalda el bloqueo de AF/AE/WB. | 🔴 Crítico | Etapa 1 — Bloqueo de parámetros automáticos, impacto en tracking | Investigacion-P1 | arXiv:2208.12644 |
| **P97** | ISP-less Low-Power Computer Vision (RAW Detection) | — | 2022 | *arXiv* | Detección en **dominio RAW supera a RGB procesado por ISP** en 7.1% precisión. Aprendizaje de gamma correction en RAW supera baseline RGB. "Freedom from the nonlinear distortions introduced by the ISP pipeline" (RAWild, 2026). | P1 — Confirma que el procesamiento ISP (tone mapping, gamma) pierde información útil para detección. Respalda desactivar procesamiento automático y usar RAW/tone mapping lineal. | 🟠 Alta | Etapa 1 — RAW vs ISP, calidad de datos de entrenamiento, tone mapping | Investigacion-P1 | arXiv:2210.05451 |
| **P98** | AdaptiveISP: Learning an Adaptive Image Signal Processor for Object Detection | — | 2024 | *NeurIPS* | ISP puede optimizarse específicamente para detección. AdaptiveISP logra **mAP@0.5 de 71.4 vs baseline 55.6 (28% mejora)**. Solo algunas etapas ISP son útiles para detección — el pipeline default es **sub-óptimo** para visión computacional. | P1 — Confirma que el ISP por defecto NO es óptimo para detección. Respalda desactivar procesamiento automático y usar control manual vía Camera2 API. | 🟠 Alta | Etapa 1 — ISP sub-óptimo para detección, RAW vs procesado | Investigacion-P1 | arXiv:2410.22939 |
| **P99** | Assessing Nutritional Pigment Content of Green and Red Leafy Vegetables via Digital Image Analysis | — | 2024 | *PMC* (12057810) | Usa **Open Camera v1.52** en Redmi Note 7 Pro. **ISO=200 fijo, shutter=1/100s, AF deshabilitado, compensación de exposición deshabilitada**. Razón explícita: "to ensure uniformity across images". Iluminación LED controlada 4000K a 50cm. | P1 — **Único paper encontrado que documenta Open Camera** con configuración detallada y justificación explícita. Matiza el claim de que "ningún paper documenta apps de cámara". | 🟡 Media | Etapa 1 — Open Camera, justificación de parámetros fijos en investigación | Investigacion-P1 | PMC12057810 |
| **P100** | Combined Electronic Image Stabilization and Optical Image Stabilization (Qualcomm Patent) | — | 2024 (granted) | *US Patent US20200412954A1* | OIS+EIS combinados exitosamente con realimentación de sensores Hall para posición del lente. EIS filter se ajusta dinámicamente según posición OIS. | P2 — **Contradice** la afirmación "OIS debe estar OFF" para sistemas con acceso a posición del lente. Confirma la regla para sensores externos sin Hall feedback. | 🟠 Alta | Etapa 2 — OIS OFF (matiz), sistemas modernos OIS+EIS | Investigacion-P2 (Contradicciones) | US Patent |
| **P101** | HyperOIS: Advanced OIS and OIS-EIS Cooperation in Smartphone Cameras | — | 2024 | *IEEE Trans. Consumer Electronics* (10.1109/TCE.2024.3369029) | OIS avanzado integrado con plataforma smartphone. SR -34.37dB a -26.90dB. Xiaomi 14 blur 39.17μm en 4K. Demuestra que OIS moderno no requiere desactivación para estabilización digital. | P2 — **Contradice parcialmente** la regla OIS OFF. OIS moderno puede integrarse sin conflicto. | 🟡 Media | Etapa 2 — OIS OFF (contexto de sistemas modernos) | Investigacion-P2 (Contradicciones) | 10.1109/TCE.2024.3369029 |
| **P102** | In-Shoe System for Gait Monitoring — Effects of Sampling Rate | Torun et al. | 2021 | *Sensors* (DOI: 10.3390/s21082869) | **100 Hz inadecuado** para parámetros espaciales de marcha. Useful gait content hasta 120 Hz. Identifica optimal sampling a **250 Hz**. Aliasing afecta integración de señales para stride length y velocidad. | P2 — **Contradice** la suficiencia de 100 Hz para análisis de marcha. **No aplica a tesis** porque no estimamos parámetros espaciales sino orientación para sincronización. | 🟡 Media | Etapa 3 — Logging IMU (contexto de limitación de 100 Hz) | Investigacion-P2 (Contradicciones) | 10.3390/s21082869 |
| **P103** | FEGW-YOLO: Feature-Complexity-Guided Lightweight Framework | — | 2026 | *PMC* (PMC12944136) | YOLOv8n retiene **71.9% mAP@0.5** a blur severo (kernel=11). FEGW-YOLO retiene 80.1%. Degradación de solo ~21.4% vs el 86.4% reportado por Citrus GAN [P68]. | P2 — **Contradice la magnitud** de degradación por blur (86.4%). Degradación real ≤50% en condiciones extremas. | 🟠 Alta | Etapa 2 — Motion blur + YOLO (matiz de magnitud) | Investigacion-P2 (Contradicciones) | PMC12944136 |
| **P104** | Quantization Robustness to Input Degradations for Object Detection | — | 2025 | *arXiv* (arXiv:2508.19600) | Medium blur causa solo **11-15% mAP relativo drop** en YOLOv12. Modelos cuantizados INT8 son más robustos que FP32 a degradación. | P2 — **Contradice** degradación severa por blur. Degradación moderada (11-15%) en blur medio. | 🟡 Media | Etapa 2 — Motion blur + YOLO (contexto adicional) | Investigacion-P2 (Contradicciones) | arXiv:2508.19600 |
| **P105** | A Novel Knowledge Distillation Framework for Small Object Detection in Blurry Environments | — | 2024 | *Springer* (DOI: 10.1007/s40747-024-01676-w) | Al 100% de velocidad de motion, YOLOv8 pierde solo **4.6% mAP@0.5**. Con knowledge distillation: solo **2.5% drop**. | P2 — **Contradice fuertemente** la degradación extrema. Degradación mínima (2.5-4.6%) para objetos pequeños en blur. | 🟠 Alta | Etapa 2 — Motion blur + YOLO (evidencia de degradación moderada) | Investigacion-P2 (Contradicciones) | 10.1007/s40747-024-01676-w |
| **P106** | Delving into YOLO Object Detection Models: Insights into Adversarial Robustness | — | 2025 | *MDPI Electronics* (DOI: 10.3390/electronics14081624) | YOLOv4 tiene MEJOR robustez a motion blur que YOLOv7/v9/v11. YOLOv4 pierde ~15%, YOLOv11 pierde ~25%. Versiones nuevas NO son más robustas contra blur. | P2 — **Contradice** que versiones recientes de YOLO sean inherentemente más robustas a blur. Soporta probar YOLOv4/v8/v11. | 🟠 Alta | Etapa 2 — Motion blur + YOLO, Etapa 7 — Selección de modelo YOLO | Investigacion-P2 (Contradicciones) | 10.3390/electronics14081624 |
| **P107** | Deep Online Fused Video Stabilization | Shi, Z.; Shi, F.; Lai, W.; Liang, C.; Liang, Y. | 2022 | *WACV 2022* (arXiv:2102.01279) | **Primer híbrido IMU+deep learning.** Gyro-only: Stability 0.846. Fused (gyro+optical flow): **0.853**. Mayor FOV (0.906 vs 0.827). Demuestra que IMU puro es superado por métodos híbridos. | P2 — **Contradice** la superioridad de IMU puro. Respalda el enfoque híbrido de Gyroflow. | 🟠 Alta | Etapa 2 — Estabilización (IMU+deep learning supera a IMU puro) | Investigacion-P2 (Contradicciones) | arXiv:2102.01279 |
| **P108** | RStab: 3D Multi-frame Fusion for Video Stabilization | Peng, Z. et al. | 2024 | *CVPR 2024* (DOI: 10.1109/CVPR52733.2024.00710) | **SOTA en estabilización.** Cropping Ratio=1.00 (full-frame). Stability 0.92 vs gyro-only ~0.83. Deep learning 3D supera ampliamente a IMU puro. | P2 — **Contradice** la afirmación "IMU supera a óptica". Deep learning es SOTA actual. | 🟠 Alta | Etapa 2 — Estabilización (contexto SOTA, no usado en tesis por costo computacional) | Investigacion-P2 (Contradicciones) | 10.1109/CVPR52733.2024.00710 |
| **P109** | Let's Roll: A Synthetic and Real Dataset for Pedestrian Detection Across Different Shutter Types | — | 2024 | *arXiv* (arXiv:2309.08136) | **RS correction NO necesaria** para detección de objetos a IoU≥0.5. A IoU≥0.5:0.95, discrepancia llega a 24% (bounding box positioning, no detección). Modelos pueden aprender a compensar RS. | P2 — **Contradice** la necesidad de rolling shutter correction para detección. Podría desactivarse en Gyroflow sin pérdida de mAP. | 🟠 Alta | Etapa 2 — Rolling shutter correction (beneficio negligible para detección) | Investigacion-P2 (Contradicciones) | arXiv:2309.08136 |
| **P110** | Simulation-Aided Development of CNN-Based Vision Module — Overlapping Rate | Sanchez, J.A.; Zhang, Y. | 2022 | *Appl. Sci.* 12(11), 5600 (DOI: 10.3390/app12125600) | Introduce overlapping rate formula: ro = (FOV × fps) / velocity. Tested 0.1-2.5 m/s. With 22 fps: speeds up to 2.5 m/s viable. ro < 1 creates coverage gaps. | P3 — **Contradice** límite de 1 m/s. Fórmula ro cuantifica velocidad máxima según FOV y fps. | 🟠 Alta | P3 — Velocidad de caminata (overlapping rate) | Investigacion-P3-Protocolo-Caminata | 10.3390/app12125600 |
| **P111** | Assessing a Multi-Camera System to Enhance Fruit Visibility for Robotic Harvesting | Villacrés, J. et al. | 2024 | — (Sep 2024, pending DOI) | Single camera perpendicular to canopy: **88.3%** fruits detected. Two cameras: **97.5%** of four-camera system. Horizontal/perpendicular is optimal. | P3 — **Contradice** ángulo 15° up. Cámara perpendicular (0° horizontal) detecta 88.3% de frutos sola. | 🟠 Alta | P3 — Ángulo de cámara | Investigacion-P3-Protocolo-Caminata | — |
| **P112** | Full-Surface Detection of Apple Fruits Using Enhanced YOLOv5 — Orientation Study | — | 2025 | *Springer* (DOI: 10.1007/s44462-025-00020-w) | Sideways orientation: **mAP 95%**, F1 90.58. Stem up: 86%. Stem down: 91.7%. Orientación sideways (horizontal) supera cualquier tilt. | P3 — **Contradice** 15° up. Orientación sideways (90°) = mAP 95%, superior a cualquier ángulo con tilt. | 🟡 Media | P3 — Ángulo de cámara | Investigacion-P3-Protocolo-Caminata | 10.1007/s44462-025-00020-w |
| **P113** | Cluster Segmentation and Stereo Vision-Based Apple Localization for Robotic Harvesting | — | 2025 | *Frontiers in Plant Science* (DOI: 10.3389/fpls.2025.1598414) | Tested 0°, 15°, 30°, 45°. **45°**: highest detection rate (>40%). Algoritmo estable en rango 0°-45°. | P3 — **Contradice** 15° up. 45° supera a 15° para tasa de detección. | 🟡 Media | P3 — Ángulo de cámara | Investigacion-P3-Protocolo-Caminata | 10.3389/fpls.2025.1598414 |
| **P114** | Experiments and Analysis of Close-Shot Identification of On-Branch Citrus Fruit with RealSense | — | 2018 | *Sensors* (MDPI) | Optimal close-shot: **160-700 mm** (0.16-0.7m). 80-100% at little occlusion, 63.8% severe. "Close, large, and clear" — less redundant info. | P3 — **Contradice** distancia 0.8-1.5m. Para cítricos, distancia óptima es <0.7m. | 🟠 Alta | P3 — Distancia al dosel | Investigacion-P3-Protocolo-Caminata | MDPI Sensors 2018 |
| **P115** | Stereo Vision-Based Detection of Loose Oil Palm Fruits | — | 2024 | — | Tested 20-120 cm. Best detection at **30 cm**: 97.63% accuracy, F1=0.99. Distance estimation optimal at 50 cm: MAPE 0.86%. | P3 — **Contradice** distancia 0.8-1.5m. 0.3m óptimo para detección, muy por debajo. | 🟡 Media | P3 — Distancia al dosel | Investigacion-P3-Protocolo-Caminata | — |
| **P116** | Intelligent Integrated System for Fruit Detection Using Multi-UAV Imaging and Deep Learning | — | 2024 | *Sensors* (DOI: 10.3390/s24093743) | Peak at **NOON**: Precision **92.1%**, F1 **90.5%**. Cloudy: 86.1%. Strong shade: 78.1%. Sol cenital (mediodía) da el mejor rendimiento. | P3 — **Contradice FUERTEMENTE** "evitar mediodía". Sol cenital = mejor condición: 92.1% precision. | 🟠 Alta | P3 — Horario/iluminación | Investigacion-P3-Protocolo-Caminata | 10.3390/s24093743 |
| **P117** | YOLOv8n-CSE: A Model for Detecting Litchi in Nighttime Environments | — | 2024 | — | LED matrix (210-350 Lux). Night detection: **mAP@0.5 = 98.86%**, **F1 = 95.54%**. Only 4.93M parameters. | P3 — **Mejora**: noche con LED = 98.86% mAP, superior a detección diurna. | 🟠 Alta | P3 — Iluminación nocturna | Investigacion-P3-Protocolo-Caminata | — |
| **P118** | Nighttime Harvesting of OrBot (Orchard RoBot) | — | 2024 | — | Nighttime: **94%** harvesting success. Daytime: **88%**. LED 5600K, 10% intensity, frontal. Elimina sombras nocturnas. | P3 — **Mejora**: noche 94% > día 88% con LED controlado (5600K, 10%). | 🟠 Alta | P3 — Iluminación nocturna | Investigacion-P3-Protocolo-Caminata | — |
| **P119** | YOLO-P: An Efficient Method for Pear Fast Detection in Complex Orchard Environment | — | 2022 | *Frontiers in Plant Science* (DOI: 10.3389/fpls.2022.1089454) | Night detection with 1000 lm: **F1 96.1%**. Natural light: ~93%. 5257 images including nighttime with artificial lighting. | P3 — **Mejora**: noche con 1000 lm = 96.1% F1, supera luz natural. | 🟡 Media | P3 — Iluminación nocturna | Investigacion-P3-Protocolo-Caminata | 10.3389/fpls.2022.1089454 |
| **P120** | The Effect of Illumination on HSV Colour Segmentation for Tomato | — | 2024 | — | Minimum **3,000 lx** required for accurate segmentation. Cloudy provides only 1,000-2,000 lx. At 1,600 lx: only **50% of fruit area** detected. | P3 — **Contradice** "nublado ideal". Nublado es insuficiente (<3,000 lx mínimo). | 🟡 Media | P3 — Iluminación | Investigacion-P3-Protocolo-Caminata | — |
| **P121** | Burst Photography for High Dynamic Range and Low-Light Imaging (HDR+) | Hasinoff, S. et al. | 2016 | *ACM Trans. Graphics* | Captures burst of underexposed frames, merges to reduce noise without motion blur. "Shorter than typical exposure times in a conventional pipeline" — reducing motion blur. | P3 — **Mejora**: burst photography > exposición fija única. Alternativa a shutter fijo. | 🟡 Media | P3 — Shutter speed | Investigacion-P3-Protocolo-Caminata | ACM TOG 2016 |
| **P122** | DEBIR: Dynamic Exposure Burst Image Restoration | — | 2026 | *arXiv* (arXiv:2603.21784) | BAENet predicts optimal per-frame exposure times adaptively. Preview at 1/120s, burst uses varied exposures. Outperforms fixed exposure bracketing. | P3 — **Mejora**: exposición adaptativa por frame supera a 1/60-1/120s fijo. | 🟡 Media | P3 — Shutter speed | Investigacion-P3-Protocolo-Caminata | arXiv:2603.21784 |
| **P123** | Estimation of Passion Fruit Yield Based on YOLOv8n + OC-SORT + CRCM Algorithm | — | 2025 | *Computers and Electronics in Agriculture* (DOI: 10.1016/j.compag.2024.109727) | **OC-SORT**: HOTA **67.10%**. StrongSORT: 58.28%. ByteTrack: 62.39%. BoT-SORT: 64.12%. OC-SORT handles occlusion and shaking. | P3 — **Contradice**: OC-SORT (HOTA 67.10%) supera ByteTrack (62.39%) para fruta. | 🟠 Alta | P3 — Tracking/anti-doble conteo | Investigacion-P3-Protocolo-Caminata | 10.1016/j.compag.2024.109727 |
| **P124** | Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification | — | 2023 | *arXiv* (arXiv:2302.11813) | MOT17: HOTA **64.9** vs ByteTrack 63.1. DanceTrack: **61.3** vs ByteTrack 47.3. Adaptive Re-ID weight based on feature quality. | P3 — **Mejora**: Deep OC-SORT (HOTA 64.9) supera ByteTrack (63.1) en benchmarks. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | arXiv:2302.11813 |
| **P125** | FTO-SORT: Fast Track-id Optimizer for Enhanced Multi-Object Tracking | — | 2025 | *Computers and Electronics in Agriculture* 237, 110540 (DOI: 10.1016/j.compag.2025.110540) | **IDF1 90.2%** (+18.0% over baseline). No Re-ID: ~10x faster on edge device. Farm-specific tracking optimizer. | P3 — **Mejora**: FTO-SORT IDF1 90.2%, +18% sobre baseline. 10× más rápido. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | 10.1016/j.compag.2025.110540 |
| **P126** | LOCALIZESORT: Localization-Based Stationary Object Tracking in Precision Agriculture | — | 2026 | *SSRN* (DOI: 10.2139/ssrn.4829514) | World-coordinate association for stationary objects. Mango count error: **187** vs DeepSORT 263, StrongSORT 217. Reduce sobreconteo significativamente. | P3 — **Mejora**: coordenadas del mundo para objetos estáticos reduce sobreconteo. | 🟡 Media | P3 — Tracking/anti-doble conteo | Investigacion-P3-Protocolo-Caminata | 10.2139/ssrn.4829514 |
| **P127** | PineSORT: Simple Online Real-Time Tracking Framework for Drone Videos in Agriculture | — | 2025 | *CVPR 2025 Workshops* (DOI: 10.1109/CVPRW67362.2025.00012) | Motion direction cost + ORB camera compensation + 3-stage association. Improves significantly over BoTSORT and AgriSORT in ISP-IDF1, IDF1, HOTA, AssA. Low-FPS capable. | P3 — **Mejora**: tracker con compensación de cámara. CVPR workshop. Superior en HOTA/IDF1. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | 10.1109/CVPRW67362.2025.00012 |
| **P128** | CoTracker3 — Adaptive Vision-Guided Robotic Arm Control for Precision Pruning | — | 2025 | *arXiv* (arXiv:2504.07309) | Point tracking transformer. **93%** pruning success. Error trajectory: 0.23mm. **27% faster** than LoCoTrack. Joint tracking infers occluded points. | P3 — **Mejora**: point tracking para oclusiones. Alternativa a bounding-box tracking. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | arXiv:2504.07309 |
| **P129** | Transformer-Based Spatio-Temporal Association of Apple Fruitlets | — | 2025 | *arXiv* (arXiv:2503.03200) | Shape + position encoding + transformer attention. **F1 92.4%** (vs ICP 89.5%, Desc 86.4%). Cross-day matching. | P3 — **Mejora**: transformer para asociación temporal F1 92.4%. Supera a métodos clásicos. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | arXiv:2503.03200 |
| **P130** | MOT-DETR-3D: Single Shot Detection and Tracking with Transformers for Agro-Food Robots | — | 2023 | *arXiv* (arXiv:2311.15674) | HOTA **60.4**, MOTA **70.38** vs FairMOT 46.06/51.49. 3D data improves tracking of visually similar objects (like tomatoes). | P3 — **Mejora**: transformer 3D para tracking de fruta. HOTA 60.4. | 🟡 Media | P3 — Tracking | Investigacion-P3-Protocolo-Caminata | arXiv:2311.15674 |

## Papers de documentación técnica (no académicos)

| ID | Nombre | Tipo | Contexto | Importancia | Justifica a | Link |
|---|---|---|---|---|---|---|
| D1 | Open Camera Help | Documentación oficial | Justificación de controles manuales (AF Lock, AE Lock, WB Lock, ISO, shutter, bitrate) | ⚪ Informativa | Etapa 1 — App de Cámara | https://opencamera.sourceforge.io/help.html |
| D2 | Gyroflow Documentation | Documentación oficial | Estabilización IMU-based, compatibilidad con Sensor Logger, sincronización | ⚪ Informativa | Etapa 2 — Estabilización, Etapa 6 — Pre-procesamiento | https://docs.gyroflow.xyz/ |
| D3 | Sensor Logger Official Site | App documentation | Validación de la app, sensores soportados, formatos de exportación | ⚪ Informativa | Etapa 3 — Logging IMU | https://www.tszheichoi.com/sensorlogger |
| D4 | OpenCamera Sensors (GitHub) | Repositorio open-source | Fork con sincronización video-IMU nativa | ⚪ Informativa | Etapa 4 — Sincronización Video-IMU | https://github.com/prime-slam/opencamera-sensors |
| D5 | Gyroflow GitHub | Repositorio open-source | 8.9k stars, 40+ contribuidores, 24 releases | ⚪ Informativa | Etapa 2 — Estabilización, Etapa 6 — Pre-procesamiento | https://github.com/gyroflow/gyroflow |
| D6 | Object recognition + IMU (GitHub) | Repositorio open-source | Kalman Filter + IoU con IMU para post-procesar detecciones YOLO | ⚪ Informativa | Pipeline MOT (post-procesamiento) | https://github.com/zhouzypaul/object-recognition-imu |
| D7 | Gyroflow Plugins (GitHub) | Repositorio open-source | Plugins OpenFX (DaVinci Resolve), Adobe, frei0r para Gyroflow | ⚪ Informativa | Etapa 6 — Pre-procesamiento (Gyroflow plugins) | https://github.com/gyroflow/gyroflow-plugins |
| D8 | TehnoBlog — Video Stabilization Comparison | Blog técnico | Comparativa DaVinci Resolve vs Adobe Premiere vs VirtualDub Deshaker. Ninguna herramienta es consistentemente superior. Gyroflow no incluido en comparativa. | ⚪ Informativa | Etapa 2 — Contexto de alternativas de estabilización | https://tehnoblog.org/video-stabilization-comparison-davinci-resolve-vs-adobe-premiere-vs-virtualdub-deshaker/ |

## Resumen por fuente

| Fuente | Cantidad de papers |
|---|---|---|
| **Elicit P1** (Software) | 16 |
| **Elicit P2** (IMU) | 12 |
| **Investigación contradicciones P2** (nuevos, 2025) | 10 |
| **Investigación contradicciones P3** (nuevos, 2026) | 21 |
| **Semantic Scholar / Web Search** (adicionales) | 57 |
| **Documentación técnica** | 8 |
| **Total** | **138** |

---

## Distribución por Nivel de Importancia

| Nivel | Cantidad | IDs |
|---|---|---|
| **🔴 Crítico** | 24 | P11, P13, P22, P23, P25, P27, P28, P31, P37, P40, P43, P57, P58, P62, P64, P69, P70, P71, P74, P79, P82, P88, P91, **P96** |
| **🟠 Alta** | 49 | P10, P12, P18, P24, P26, P34, P35, P41, P42, P47, P49, P51, P55, P59, P61, P65, P66, P67, P68, P72, P73, P75, P76, P80, P81, P83, P85, P86, P90, P92, P93, **P95**, **P97**, **P98**, **P100**, **P103**, **P105**, **P106**, **P107**, **P108**, **P109**, **P110**, **P111**, **P114**, **P116**, **P117**, **P118**, **P123** |
| **🟡 Media** | 45 | P03, P29, P30, P32, P33, P36, P38, P39, P44, P45, P46, P48, P50, P53, P54, P56, P60, P63, P77, P78, P84, P87, P89, P94, **P99**, **P101**, **P102**, **P104**, **P112**, **P113**, **P115**, **P119**, **P120**, **P121**, **P122**, **P124**, **P125**, **P126**, **P127**, **P128**, **P129**, **P130** |
| **🟢 Baja** | 12 | P01, P02, P04, P05, P06, P07, P08, P09, P14, P15, P16, P17, P19, P20, P21, P52 |
| **⚪ Informativa** | 8 | D1, D2, D3, D4, D5, D6, D7, D8 |

**Total: 138 referencias** (130 papers académicos + 8 documentación técnica)

---

## Papers más citados en el proyecto

| ID | Paper | Veces referenciado | En |
|---|---|---|---|
| P25 | Fan et al. (2025) — Sampling rate IMU | 3 archivos | P2, Pipeline, Metodologia |
| P28 | Kuznetsova et al. (2020) — Apple distances | 3 archivos | Pipeline, Metodologia, P3 |
| P27 | Ramos Giraldo et al. (2017) — Coffee + IMU | 3 archivos | P1, Metodologia, P3 |
| P43 | Gašparović — Gimbal stability | 2 archivos | Pipeline, Metodologia |
| P22 | Arslan et al. (2024) — IMU deblurring | 2 archivos | P2, Pipeline |
| P13 | Li et al. (2025) — Visual-Inertial 47.8% SSIM | 2 archivos | P2, Pipeline |
| P66 | MangoYOLO — Video 62% vs dual 40% | 2 archivos | P2, P3 |
| P68 | Citrus GAN — mAP drop 86.4% | 2 archivos | P2, P3 |
| P47 | FruitSize — Ángulo <14°, distancia | 2 archivos | Metodologia, P3 |

---

## Trazabilidad: Etapas del Pipeline ↔ Papers que las Justifican

### Etapa 1 — App de Cámara (P1)
| ID | Paper | Importancia |
|---|---|---|
| P40 | Kurtser et al. — FNF exposición fija | 🔴 Crítico |
| P57 | LEDs — 85% menos variación HSV con exposición fija | 🔴 Crítico |
| P58 | Phenotyping — Manual MSE 1.57 vs Auto 4.26 | 🔴 Crítico |
| P62 | Camera2 API — Tone mapping irreversible. 74% menor MAE con lineal | 🔴 Crítico |
| P96 | ECCV 2022 — Cámara como "unintentional adversary": 13-14% fluctuación | 🔴 Crítico |
| P41 | ICNet — Compensación de iluminación | 🟠 Alta |
| P49 | Rançon et al. — Flash xenon + obturador 250µs | 🟠 Alta |
| P55 | Rice GMC — ISO=25 fijo, shutter=1/400s | 🟠 Alta |
| P59 | Illumination-Invariant — 4x menos datos con imágenes consistentes | 🟠 Alta |
| P61 | CVPR 2025 — Focus hunting documentado | 🟠 Alta |
| P95 | ISP Tuning — Contraste/gamma/saturación degradan YOLOv5/v8 | 🟠 Alta |
| P97 | RAW Detection — 7.1% más precisión en RAW vs ISP-processed | 🟠 Alta |
| P98 | AdaptiveISP — ISP default es sub-óptimo para detección (28% mejora) | 🟠 Alta |
| P60 | Stanford CNN — Exposición variable degrada CNN (claim ~20% no verificado) | 🟡 Media |
| P63 | Kiwifruit glare — F1 0.82→0.13 con luz no controlada | 🟡 Media |
| P99 | Open Camera v1.52 documentado en PMC12057810 (2024) | 🟡 Media |
| D1  | Open Camera Help | ⚪ Informativa |

### Etapa 2 — Estabilización (Gimbal + Gyroflow)
| ID | Paper | Importancia |
|---|---|---|
| P43 | Gašparović — Gimbal 6x estabilidad | 🔴 Crítico |
| P11 | Han et al. — IMU estabilización 32% | 🔴 Crítico |
| P13 | Li et al. — Visual-Inertial 47.8% SSIM | 🔴 Crítico |
| P64 | DeepOIS — OIS interfiere con giroscopio 50% peor | 🔴 Crítico |
| P12 | Li et al. — Deep Online VS | 🟠 Alta |
| P18 | Zhang & Zhang — Rolling shutter Android | 🟠 Alta |
| P26 | Bell et al. — Gyroflow foundation | 🟠 Alta |
| P51 | Zhang et al. — Kiwifruit row con estabilizador | 🟠 Alta |
| P65 | ISPRS — IS debe desactivarse (300% peor) | 🟠 Alta |
| P66 | MangoYOLO — video tracking +22% vs fotos | 🟠 Alta |
| P67 | Crop row — 66% supresión desplazamiento | 🟠 Alta |
| P68 | Citrus GAN — 86.4% mAP drop por blur | 🟠 Alta |
| **P100** | **Qualcomm Patent — OIS+EIS combinados con Hall sensor** | **🟠 Alta** |
| **P103** | **FEGW-YOLO — solo 21.4% drop a blur severo** | **🟠 Alta** |
| **P105** | **Knowledge Distillation — solo 2.5% drop al 100% velocidad** | **🟠 Alta** |
| **P106** | **MDPI Electronics — YOLOv4 más robusto a blur que v8-v11** | **🟠 Alta** |
| **P107** | **DeepFused — Hybrid IMU+DL supera a IMU puro (0.853 vs 0.846)** | **🟠 Alta** |
| **P108** | **RStab CVPR 2024 — SOTA estabilización 0.92 (deep learning)** | **🟠 Alta** |
| **P109** | **"Let's Roll" — RS correction NO necesaria para detección** | **🟠 Alta** |
| P101 | HyperOIS — OIS avanzado integrado | 🟡 Media |
| P102 | Torun et al. — 100 Hz inadecuado para parámetros espaciales | 🟡 Media |
| P104 | Quantization Study — 11-15% mAP drop por blur medio | 🟡 Media |
| D2  | Gyroflow Documentation | ⚪ Informativa |
| D5  | Gyroflow GitHub | ⚪ Informativa |
| D7  | Gyroflow Plugins GitHub | ⚪ Informativa |
| D8  | TehnoBlog — Comparativa estabilización | ⚪ Informativa |

### Regla OIS OFF (sub-sección crítica de Etapa 2)
| ID | Paper | Importancia |
|---|---|---|
| P64 | DeepOIS — OIS interfiere 50% peor alineación | 🔴 Crítico |
| P65 | ISPRS — IS 300% peor incertidumbre, 4x reproyección | 🟠 Alta |
| **P100** | **Qualcomm Patent — OIS+EIS combinados CON Hall sensor** | **🟠 Alta (matiz)** |
| **P101** | **HyperOIS — OIS moderno compatible con procesamiento digital** | **🟡 Media (matiz)** |
| D2  | Gyroflow Docs — OIS debe estar OFF | ⚪ Informativa |

> **Veredicto final:** La regla "OIS OFF" se mantiene para nuestro pipeline (Sensor Logger externo sin acceso a Hall sensor). En sistemas con realimentación de posición de lente, OIS no necesita desactivarse. [Ver sección de Contradicciones en Investigacion-P2].

### Etapa 3 — Logging IMU
| ID | Paper | Importancia |
|---|---|---|
| P25 | Fan et al. — Sampling rate 100Hz para orientación en walking | 🔴 Crítico |
| P23 | Choi — Sensor Logger | 🔴 Crítico |
| **P102** | **Torun et al. — 100 Hz inadecuado para parámetros espaciales (250 Hz óptimo)** | **🟡 Media — No aplica a tesis** |
| D3  | Sensor Logger Official Site | ⚪ Informativa |

> **Nota:** P102 (Torun 2021) contradice la suficiencia de 100 Hz para análisis de marcha espacial, pero NO aplica a nuestro uso (orientación para sincronización video-IMU).

### Etapa 4 — Sincronización Video-IMU
| ID | Paper | Importancia |
|---|---|---|
| P23 | Choi — Sensor Logger | 🔴 Crítico |
| P24 | MARS Logger — Sincronización <5ms | 🟠 Alta |
| D4  | OpenCamera Sensors (GitHub) | ⚪ Informativa |

### Etapa 5 — Calibración de Cámara
| ID | Paper | Importancia |
|---|---|---|
| P10 | Peng et al. — Corrección fisheye GPU | 🟠 Alta |
| P03 | Zhao et al. — Calibración binocular | 🟡 Media |
| P47 | Wang et al. — FruitSize control calidad | 🟠 Alta |

### Etapa 6 — Pre-procesamiento (Deblurring + Frame Selection + Gyroflow)
| ID | Paper | Importancia |
|---|---|---|
| P22 | Arslan et al. — IMU deblurring 5% PSNR | 🔴 Crítico |
| P26 | Bell et al. — Gyroflow foundation | 🟠 Alta |
| P49 | Rançon et al. — Iluminación controlada | 🟠 Alta |
| **P107** | **DeepFused — Hybrid IMU+DL (gyro+optical flow) supera a IMU puro** | **🟠 Alta** |
| **P108** | **RStab — SOTA 0.92 estabilidad, deep learning 3D** | **🟠 Alta** |
| **P109** | **"Let's Roll" — RS correction no necesaria para detección** | **🟠 Alta (variable a medir)** |
| D2  | Gyroflow Documentation | ⚪ Informativa |
| D5  | Gyroflow GitHub | ⚪ Informativa |
| D7  | Gyroflow Plugins GitHub | ⚪ Informativa |
| D8  | TehnoBlog — Comparativa estabilización | ⚪ Informativa |

### Etapa 7 — Pipeline de Datos (YOLO + MOT)
| ID | Paper | Importancia |
|---|---|---|
| P28 | Kuznetsova — Distancias 0.2-2.0m | 🔴 Crítico |
| P31 | OrangeYolo — Velocidad 2 m/s | 🔴 Crítico |
| P37 | Apple Redmi Note 7 — Distancia 0.3-1.5m | 🔴 Crítico |
| P47 | Wang et al. — FruitSize distancia/ángulo | 🟠 Alta |
| P34 | Dynamic Kalman — MOTA 95% | 🟠 Alta |
| P35 | AgriSORT — Tracking agricultura | 🟠 Alta |
| **P103** | **FEGW-YOLO — YOLOv8n retiene 71.9% mAP a blur severo** | **🟠 Alta** |
| **P105** | **Knowledge Distillation — solo 2.5% drop al 100% velocidad** | **🟠 Alta** |
| **P106** | **MDPI Electronics — YOLOv4 más robusto a blur que v8-v11** | **🟠 Alta** |
| P54 | Parico & Ahamed — Pear YOLOv4+DeepSORT | 🟡 Media |
| P104 | Quantization Study — 11-15% mAP drop por blur medio | 🟡 Media |
| D6  | Object recognition + IMU (zhouzypaul, Brown 2022) | ⚪ Informativa |

### Investigación P1 — Software de Captura (contexto general)
| ID | Paper | Importancia |
|---|---|---|
| P27 | Ramos Giraldo — Coffee + IMU | 🔴 Crítico |
| P01-P09 | Papers de captura varios | 🟢 Baja |
| P48 | Zhou et al. — KiwiDetector app Android | 🟡 Media |

### Investigación P2 — IMU / Telemetría (contexto general)
| ID | Paper | Importancia |
|---|---|---|
| P11-P26, P56 | Papers de estabilización, deblurring, RS | Varios |
| P100-P109 | Papers de contradicciones y matices (investigación 2025) | Varios |

> **Nota:** Los papers P100-P109 surgieron de una investigación específica de validación/contradicción de las afirmaciones del Paso 2. Ver sección "Contradicciones y Matices" en Investigacion-P2-IMU-Telemetria.md.
> 
> Los papers P110-P130 surgieron de una investigación específica de contradicciones del Paso 3 ejecutada con 8 agentes librarian paralelos (05/06/2026). Ver secciones "1b-6b. Contradicciones y evidencia complementaria" en Investigacion-P3-Protocolo-Caminata.md.

### Investigación P3 — Protocolo Caminata (contexto general)
| ID | Paper | Importancia |
|---|---|---|
| P27 | Ramos Giraldo — Coffee + IMU (3 cm/s, 11.3°) | 🔴 Crítico |
| P28 | Kuznetsova — Apple distances 0.2-2.0m | 🔴 Crítico |
| P29 | Pear dataset — 4 horarios | 🟡 Media |
| P30 | Cocoa dataset — 8AM-4PM, zigzag | 🟡 Media |
| P31 | OrangeYolo — Velocidad 2 m/s | 🔴 Crítico |
| P37 | Apple Redmi Note 7 — Distancia 0.3-1.5m | 🔴 Crítico |
| P38 | DHN-YOLO fresas — 50-80cm, ángulo 45° | 🟡 Media |
| P39 | Hawthorn detection — 3 ángulos, 3 luces | 🟡 Media |
| P44 | EMA-YOLO — Distancias comparadas | 🟡 Media |
| P45 | Apple MSX — Ángulo óptimo -16° | 🟡 Media |
| P47 | FruitSize — Ángulo <14°, distancia 120-300mm | 🟠 Alta |
| P66 | MangoYOLO — Video 62% vs dual 40% | 🟠 Alta |
| P68 | Citrus GAN — mAP drop 86.4% por blur | 🟠 Alta |
| **P69** | **Sweet-Pepper — 14 posiciones ángulo (NUEVO)** | **🔴 Crítico** |
| **P70** | **Apple Yield Mapping — Samsung S4 a 2 m/s (NUEVO)** | **🔴 Crítico** |
| **P71** | **Apple 3D Camera — 3 veloc. × 3 ángulos (NUEVO)** | **🔴 Crítico** |
| **P72** | **RGB-D Sensors — 1.5m vs 2.5m distancia (NUEVO)** | **🟠 Alta** |
| **P73** | **YOLO-CSB — 0.8-1.5m distancia (NUEVO)** | **🟠 Alta** |
| **P74** | **Gené-Mola Video — ByteTrack MOTA 0.682 (NUEVO)** | **🔴 Crítico** |
| **P75** | **Motion Blur Review — Fórmula desplazamiento (NUEVO)** | **🟠 Alta** |
| **P76** | **Orchard-YOLO — ±50% iluminación (NUEVO)** | **🟠 Alta** |
| **P77** | **AgRowStitch — iPhone 13 caminata manual (NUEVO)** | **🟡 Media** |
| **P78** | **Mango sizing — 6 km/h, 1-3m (NUEVO)** | **🟡 Media** |
| **P103** | **FEGW-YOLO — modelos tolerantes a blur (P3)** | **🟠 Alta** |
| **P105** | **Knowledge Distillation — blur mínimo 2.5% drop (P3)** | **🟠 Alta** |
| **P106** | **MDPI Electronics — YOLOv4 más robusto a blur (P3)** | **🟠 Alta** |
| **P110** | **Sanchez & Zhang — Overlapping Rate (CONTRADICE velocidad)** | **🟠 Alta** |
| **P111** | **Villacrés — Multi-cámara 0°=88.3% (CONTRADICE ángulo)** | **🟠 Alta** |
| **P112** | **Apple Orientation — Sideways mAP 95% (CONTRADICE ángulo)** | **🟡 Media** |
| **P113** | **Cluster Segmentation — 45° > 15° (CONTRADICE ángulo)** | **🟡 Media** |
| **P114** | **RealSense Citrus — 0.16-0.7m óptimo (CONTRADICE distancia)** | **🟠 Alta** |
| **P115** | **Oil Palm Stereo — 0.3m óptimo (CONTRADICE distancia)** | **🟡 Media** |
| **P116** | **Multi-UAV — Mediodía precision 92.1% (CONTRADICE horario)** | **🟠 Alta** |
| **P117** | **YOLOv8n-CSE Litchi Night — 98.86% mAP noche (MEJORA)** | **🟠 Alta** |
| **P118** | **OrBot Night — 94% noche vs 88% día (MEJORA)** | **🟠 Alta** |
| **P119** | **YOLO-P Pear — 96.1% F1 noche (MEJORA)** | **🟡 Media** |
| **P120** | **Tomato HSV — 3,000 lx mínimo (CONTRADICE nublado)** | **🟡 Media** |
| **P121** | **HDR+ Hasinoff — Burst photography (MEJORA shutter)** | **🟡 Media** |
| **P122** | **DEBIR — Exposición adaptativa (MEJORA shutter)** | **🟡 Media** |
| **P123** | **OC-SORT — HOTA 67.10% > ByteTrack 62.39% (CONTRADICE)** | **🟠 Alta** |
| **P124** | **Deep OC-SORT — HOTA 64.9 (MEJORA tracking)** | **🟡 Media** |
| **P125** | **FTO-SORT — IDF1 90.2% (MEJORA tracking)** | **🟡 Media** |
| **P126** | **LocalizeSORT — Error 187 vs 263 (MEJORA tracking)** | **🟡 Media** |
| **P127** | **PineSORT — CVPR 2025 (MEJORA tracking)** | **🟡 Media** |
| **P128** | **CoTracker3 — Point tracking (MEJORA tracking)** | **🟡 Media** |
| **P129** | **Transformer Apple Fruitlet — F1 92.4% (MEJORA tracking)** | **🟡 Media** |
| **P130** | **MOT-DETR-3D — HOTA 60.4 (MEJORA tracking)** | **🟡 Media** |

### Investigación P4 — Selección de Parcelas y Muestreo
| ID | Paper | Importancia | ¿Qué justifica? |
|---|---|---|---|
| P79 | Miranda et al. — Stratification NDVI peach | 🔴 Crítico | Principio de estratificación por NDVI (imagen aérea 0.25m) |
| P80 | Uribeetxebarria et al. — Stratified sampling orchards | 🟠 Alta | NDVI como variable auxiliar para estratificar (imagen aérea 0.25m) |
| P81 | Martínez-Casasnovas et al. — RSS peach orchards | 🟠 Alta | Ranked Set Sampling con UAV |
| P82 | Meyers et al. — Satellite NDVI sampling | 🔴 Crítico | NDVI3: selección por cuantiles NDVI satelital (Landsat 30m, bloques >10ha) |
| P83 | Meyers & Vanden Heuvel — Sampling costs | 🟠 Alta | Eficiencia del muestreo NDVI satelital |
| P84 | UAV vs Sentinel-2 management zones | 🟡 Media | Sentinel-2 captura zonas principales de vigor (10m) |
| P85 | Morocco citrus — yield prediction | 🟠 Alta | Mean NDVI Sentinel-2 para 50 parcelas de cítricos |
| P86 | Kinnow mandarin Red Edge | 🟠 Alta | NDRE > NDVI para cítricos con Sentinel-2 |
| P87 | Citrus orchard mapping Iran | 🟡 Media | Sentinel-2 clasifica cítricos con 99.7% precisión |
| P88 | Wulfsohn et al. — SUR sampling | 🔴 Crítico | SUR sistemático: error <10% en 11/14 huertos |
| P89 | Mediterranean orchard assessment | 🟡 Media | Selección de parcelas por criterios agronómicos |
| **P90** | **Sun et al. — Kinnow mandarin S2 RE** | **🟠 Alta** | **Variabilidad en mandarina Kinnow capturada por Sentinel-2 (R²=0.85)** |
| **P91** | **Arnó et al. — Estratificación > aleatorio huertos** | **🔴 Crítico** | **Estratificación NDVI más eficiente que aleatorio en huertos frutales** |
| **P92** | **Longo-Minnolo et al. — Zonas manejo cítricos** | **🟠 Alta** | **Zonas de manejo en cítricos con NDVI, diferencias significativas** |
| **P93** | **Ampatzidis & Partel — UAV fenotipado cítricos** | **🟠 Alta** | **NDVI correlaciona con vigor en cítricos + YOLO 99.9% precisión** |
| **P94** | **Castaldi et al. — S2 sampling strategies** | **🟡 Media** | **S2-10m adecuado para muestreo agrícola a escala parcela** |

### Metodologías Similares — Referencia Comparativa
| ID | Paper | Importancia |
|---|---|---|
| P46 | Grilli et al. — Apple photogrammetry smartphone | 🟡 Media |
| P48 | Zhou et al. — KiwiDetector selfie stick | 🟡 Media |
| P50 | Apple flower detection Azure Kinect | 🟡 Media |
| P51 | Zhang et al. — Kiwifruit row gimbal+pole | 🟠 Alta |
| P52 | Fruit Harvest Helper cross-platform | 🟢 Baja |
| P53 | Kiwifruit tractor+gimbal counting | 🟡 Media |
| P54 | Parico & Ahamed — Pear YOLOv4+DeepSORT | 🟡 Media |
| P27 | Ramos Giraldo — Coffee + IMU 3cm/s | 🔴 Crítico |
| P31 | OrangeYolo — Rover 2 m/s | 🔴 Crítico |
