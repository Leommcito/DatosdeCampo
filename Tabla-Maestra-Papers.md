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
| **P60** | Optimizing Image Acquisition Systems for Autonomous Driving (CNN + Exposure) | — | 2018 | *Stanford / Google Research* | **~20% caída de precisión** en CNN cuando hay sesgo de exposición. Cámaras con parámetros inconsistentes degradan generalización de redes. | P1 — Evidencia de que exposición inconsistente degrada CNN. Respalda AE Lock. | 🟠 Alta | Etapa 1 — App de Cámara (AE Lock) | Búsqueda P1 | Stanford |
| **P61** | Stabilizing and Accelerating Autofocus with Expert Trajectory Regularized Deep RL | — | 2025 | *CVPR* | Focus hunting (FH) causa que el lente oscile repetidamente creando **inestabilidad en video**. FH reduce nitidez y cambia el FoV. | P1 — Documenta que el focus hunting es un problema real. Respalda AF Lock. | 🟠 Alta | Etapa 1 — App de Cámara (AF Lock) | Búsqueda P1 | CVPR 2025 |
| **P62** | A Calibration Method for Smartphone Camera Photoplethysmography (Camera2 API) | — | 2023 | *Nature / PMC* | Tone mapping automático aplica **transformaciones no lineales irreversibles**. Camera2 API permite desactivarlo. WB lock esencial para color consistente. | P1 — Valida Camera2 API para control manual en investigación. Respalda uso de Camera2 API + WB Lock. | 🟠 Alta | Etapa 1 — App de Cámara (Camera2 API, WB Lock) | Búsqueda P1 | PMC |
| **P63** | Kiwifruit Detection in Orchard Conditions Using a FCN with Preprocessing | — | 2020 | *arXiv* | Sin preprocesamiento: **F1 0.82** en imágenes normales vs **0.13** en imágenes con glare. Luz no controlada destruye detección. | P1 — Demuestra que condiciones de luz adversas degradan severamente la detección. | 🟡 Media | Etapa 1 — Condiciones de captura | Búsqueda P1 | arXiv:2006.11729 |
| **P64** | DeepOIS: Gyroscope-Guided Deep Optical Image Stabilizer Compensation | — | 2021 | *arXiv* | **OIS interfiere con estabilización por giroscopio.** Error alineación: 0.688 (sin OIS) vs 1.038 (con OIS) — **50% peor**. "OIS terminates the possibility of image registration by gyros." | P2 — Evidencia directa de que OIS interfiere con Gyroflow. Justifica regla OIS OFF. | 🔴 Crítico | Etapa 2 — Regla OIS OFF | Búsqueda P2 | arXiv:2101.11183 |
| **P65** | Image Stabilization Influence on Photogrammetric Accuracy | — | 2022 | *ISPRS* | **IS debe desactivarse** para modelado 3D. Incertidumbre en parámetros **hasta 300% mayor** con IS activado. Error de reproyección **4x mayor**. | P2 — Respalda desactivar OIS desde fotogrametría. Corrobora regla OIS OFF. | 🟠 Alta | Etapa 2 — Regla OIS OFF | Búsqueda P2 | ISPRS |
| **P66** | Mango Fruit Load Estimation Using Video Based MangoYOLO-Kalman Filter-Hungarian Algorithm | — | 2019 | *Sensors* | Video detection: **62.3%** del conteo real vs **40.2%** con foto estática. **+22% mejora** usando video en movimiento. Error doble conteo 9.9%. | P2 — Demuestra que video estabilizado supera a fotos estáticas para conteo de frutos. | 🟠 Alta | Etapa 2 — Video estabilizado para detección | Búsqueda P2 | 10.3390/s19122742 |
| **P67** | Crop Row Video Stabilization for Agricultural Field Robotics | — | — | *MDPI Sensors* | Desplazamiento lateral suprimido: **66%** del espacio entre hileras. Desviación: ~20px (desde 93px inicial). | P2 — Justifica estabilización en agricultura con métricas cuantitativas. | 🟠 Alta | Etapa 2 — Estabilización en agricultura | Búsqueda P2 | MDPI Sensors |
| **P68** | Lightweight GAN for Restoring Blurred Images to Enhance Citrus Detection | — | 2025 | *MDPI* | **mAP@0.5:0.95 +86.4%** tras restaurar imágenes borrosas. Recall **+76.9%**. F1 **+40.1%**. FN rate **-63.9%**. | P2 — Motion blur degrada severamente detección YOLO. Respalda necesidad de estabilización. | 🟠 Alta | Etapa 2 — Motion blur vs YOLO | Búsqueda P2 | MDPI 2025 |

---

## Papers de documentación técnica (no académicos)

| ID | Nombre | Tipo | Contexto | Importancia | Justifica a | Link |
|---|---|---|---|---|---|---|
| D1 | Open Camera Help | Documentación oficial | Justificación de controles manuales (AF Lock, AE Lock, WB Lock, ISO, shutter, bitrate) | ⚪ Informativa | Etapa 1 — App de Cámara | https://opencamera.sourceforge.io/help.html |
| D2 | Gyroflow Documentation | Documentación oficial | Estabilización IMU-based, compatibilidad con Sensor Logger, sincronización | ⚪ Informativa | Etapa 2 — Estabilización, Etapa 6 — Pre-procesamiento | https://docs.gyroflow.xyz/ |
| D3 | Sensor Logger Official Site | App documentation | Validación de la app, sensores soportados, formatos de exportación | ⚪ Informativa | Etapa 3 — Logging IMU | https://www.tszheichoi.com/sensorlogger |
| D4 | OpenCamera Sensors (GitHub) | Repositorio open-source | Fork con sincronización video-IMU nativa | ⚪ Informativa | Etapa 4 — Sincronización Video-IMU | https://github.com/prime-slam/opencamera-sensors |
| D5 | Gyroflow GitHub | Repositorio open-source | 8.9k stars, 40+ contribuidores, 24 releases | ⚪ Informativa | Etapa 2 — Estabilización, Etapa 6 — Pre-procesamiento | https://github.com/gyroflow/gyroflow |
| D6 | Object recognition + IMU (GitHub) | Repositorio open-source | Kalman Filter + IoU con IMU para post-procesar detecciones YOLO | ⚪ Informativa | Pipeline MOT (post-procesamiento) | https://github.com/zhouzypaul/object-recognition-imu |

---

## Resumen por fuente

| Fuente | Cantidad de papers |
|---|---|
| **Elicit P1** (Software) | 16 |
| **Elicit P2** (IMU) | 12 |
| **Semantic Scholar / Web Search** (adicionales) | 26 |
| **Documentación técnica** | 6 |
| **Total** | **74** |

---

## Distribución por Nivel de Importancia

| Nivel | Cantidad | IDs |
|---|---|---|
| **🔴 Crítico** | 16 | P11, P13, P22, P23, P25, P27, P28, P31, P37, P40, P43, P57, P58, P64 |
| **🟠 Alta** | 21 | P10, P12, P18, P24, P26, P34, P35, P41, P42, P47, P49, P51, P55, P59, P60, P61, P62, P65, P66, P67, P68 |
| **🟡 Media** | 18 | P03, P29, P30, P32, P33, P36, P38, P39, P44, P45, P46, P48, P50, P53, P54, P56, P63 |
| **🟢 Baja** | 13 | P01, P02, P04, P05, P06, P07, P08, P09, P14, P15, P16, P17, P19, P20, P21, P52 |
| **⚪ Informativa** | 6 | D1, D2, D3, D4, D5, D6 |

---

## Papers más citados en el proyecto

| ID | Paper | Veces referenciado | En |
|---|---|---|---|
| P25 | Fan et al. (2025) — Sampling rate IMU | 3 archivos | P2, Pipeline, Metodologia |
| P28 | Kuznetsova et al. (2020) — Apple distances | 2 archivos | Pipeline, Metodologia |
| P27 | Ramos Giraldo et al. (2017) — Coffee + IMU | 2 archivos | P1, Metodologia |
| P43 | Gašparović — Gimbal stability | 2 archivos | Pipeline, Metodologia |
| P22 | Arslan et al. (2024) — IMU deblurring | 2 archivos | P2, Pipeline |
| P13 | Li et al. (2025) — Visual-Inertial 47.8% SSIM | 2 archivos | P2, Pipeline |

---

## Trazabilidad: Etapas del Pipeline ↔ Papers que las Justifican

### Etapa 1 — App de Cámara (P1)
| ID | Paper | Importancia |
|---|---|---|
| P40 | Kurtser et al. — FNF exposición fija | 🔴 Crítico |
| P57 | LEDs — 85% menos variación HSV con exposición fija | 🔴 Crítico |
| P58 | Phenotyping — Manual MSE 1.57 vs Auto 4.26 | 🔴 Crítico |
| P41 | ICNet — Compensación de iluminación | 🟠 Alta |
| P49 | Rançon et al. — Flash xenon + obturador 250µs | 🟠 Alta |
| P55 | Rice GMC — ISO=25 fijo, shutter=1/400s | 🟠 Alta |
| P59 | Illumination-Invariant — 4x menos datos con imágenes consistentes | 🟠 Alta |
| P60 | Stanford CNN — ~20% caída precisión con sesgo exposición | 🟠 Alta |
| P61 | CVPR 2025 — Focus hunting documentado | 🟠 Alta |
| P62 | Camera2 API — Tone mapping irreversible en auto | 🟠 Alta |
| P63 | Kiwifruit glare — F1 0.82→0.13 con luz no controlada | 🟡 Media |
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
| D2  | Gyroflow Documentation | ⚪ Informativa |
| D5  | Gyroflow GitHub | ⚪ Informativa |

### Regla OIS OFF (sub-sección crítica de Etapa 2)
| ID | Paper | Importancia |
|---|---|---|
| P64 | DeepOIS — OIS interfiere 50% peor alineación | 🔴 Crítico |
| P65 | ISPRS — IS 300% peor incertidumbre, 4x reproyección | 🟠 Alta |
| D2  | Gyroflow Docs — OIS debe estar OFF | ⚪ Informativa |

### Etapa 3 — Logging IMU
| ID | Paper | Importancia |
|---|---|---|
| P25 | Fan et al. — Sampling rate 100Hz | 🔴 Crítico |
| P23 | Choi — Sensor Logger | 🔴 Crítico |
| D3  | Sensor Logger Official Site | ⚪ Informativa |

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

### Etapa 6 — Pre-procesamiento (Deblurring + Frame Selection)
| ID | Paper | Importancia |
|---|---|---|
| P22 | Arslan et al. — IMU deblurring 5% PSNR | 🔴 Crítico |
| P26 | Bell et al. — Gyroflow foundation | 🟠 Alta |
| P49 | Rançon et al. — Iluminación controlada | 🟠 Alta |
| D2  | Gyroflow Documentation | ⚪ Informativa |
| D5  | Gyroflow GitHub | ⚪ Informativa |

### Etapa 7 — Pipeline de Datos (YOLO + MOT)
| ID | Paper | Importancia |
|---|---|---|
| P28 | Kuznetsova — Distancias 0.2-2.0m | 🔴 Crítico |
| P31 | OrangeYolo — Velocidad 2 m/s | 🔴 Crítico |
| P37 | Apple Redmi Note 7 — Distancia 0.3-1.5m | 🔴 Crítico |
| P47 | Wang et al. — FruitSize distancia/ángulo | 🟠 Alta |
| P34 | Dynamic Kalman — MOTA 95% | 🟠 Alta |
| P35 | AgriSORT — Tracking agricultura | 🟠 Alta |
| P54 | Parico & Ahamed — Pear YOLOv4+DeepSORT | 🟡 Media |
| D6  | Object recognition + IMU | ⚪ Informativa |

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

### Investigación P3 — Protocolo Caminata (contexto general)
| ID | Paper | Importancia |
|---|---|---|
| P28-P39, P44-P45 | Papers distancia/velocidad/ángulo | 🟡 Media a 🔴 Crítico |

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
