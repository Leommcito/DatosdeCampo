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

| # | Título | Autores | Año | Publicación | Resumen | Contexto en el proyecto | Referenciado en | Link / DOI |
|---|---|---|---|---|---|---|---|---|
| **1** | Detecting Apples in the Wild: Potential for Harvest Quantity Estimation | Janowski, A.; Kazmierczak, R.; Kowalczyk, C.; Szulwic, J. | 2021 | *Sustainability* | Usaron smartphones + GNSS para conteo de manzanas. Recomiendan YOLO sobre Viola-Jones. No documentan app de captura. | P1 — Evidencia de que papers agrícolas NO documentan software de captura. | Investigacion-P1, Pipeline | 10.3390/SU13148054 |
| **2** | EscaYard: Precision viticulture multimodal dataset | Vélez, S.; Ariza-Sentís, M.; Valente, J. | 2024 | *Data in Brief* | Dataset de viñedos con iPhone X, Xiaomi Poco X3 Pro, UAV. Geotagged. | P1 — Mismos hallazgos: no documentan app ni configuración. | Investigacion-P1 | 10.1016/j.dib.2024.110497 |
| **3** | Phenotyping of individual apple tree with smartphone-based heterogeneous binocular vision | Zhao, G.; Yang, R.; Jing, X.; et al. | 2023 | *Computers and Electronics in Agriculture* | Usan cámara multi-lente de smartphone + método virtual focal para fenotipado. Mencionan calibración. | P1 — Único paper que detalla método de calibración de cámara en smartphone. | Investigacion-P1, Pipeline | 10.1016/j.compag.2023.107814 |
| **4** | Toward Estimating the Crop Coefficient of Vineyards Using a Smartphone Camera | Jaramillo, J.; Vanden Heuvel, J.; Petersen, K.H. | 2025 | *American Journal of Enology and Viticulture* | Video de suelo bajo hileras de vid con smartphone. Protocolo simple: video en día soleado, segmentación + SfM. | P1 — Protocolo simple pero explícito. Sin configuración de cámara. | Investigacion-P1 | 10.5344/ajev.2025.24068 |
| **5** | Real-time kiwifruit detection using deep learning on Android smartphones | Zhou, Z.; Song, Z.; Fu, L.; et al. | 2020 | *Computers and Electronics in Agriculture* | App Android (KiwiDetector) en Huawei P20. SSD + MobileNetV2. 8-bit quantization. | P1 — App propia, no comercial. Dataset de 100 imágenes. | Investigacion-P1 | 10.1016/j.compag.2020.105856 |
| **6** | Framework for smartphone-based grape detection using UAV-trained AI | Vélez, S.; Ariza-Sentís, M.; Triviño, M.; et al. | 2025 | *Heliyon* | Framework con UAV + smartphone para detección de uva. MobileNetV2 cuantizado. TDR 90.8%. | P1 — Aplicación Android para detección en campo. | Investigacion-P1 | 10.1016/j.heliyon.2025.e42525 |
| **7** | High-Throughput Image Analysis Framework for Fruit Detection from Video Streams | Huang, Y.H.; Lin, T.T. | 2019 | *ASABE* | YOLOv2 + tracking + optical flow + denoising para video de frutos en invernadero. | P1 — Pipeline de video post-captura. | Investigacion-P1 | 10.13031/aim.201900487 |
| **8** | Correction of distortions in image analysis for phenotyping of tomato fruit | Rabelo, N.G.; Faria, S.E.S.; Matos, D.V.; et al. | 2026 | *Acta Scientiarum Agronomía* | Corrección de distorsión en imágenes de tomate con smartphone usando regresión. | P1 — Calibración de lente con smartphone para fenotipado. | Investigacion-P1 | 10.4025/actasciagron.v48i1.75604 |
| **9** | High Throughput Image Analytics Using Hough Transformation for Wheat Phenotyping | Kim, J.Y.; Shin, M.N.; Lee, J.H.; et al. | 2022 | *Applied Engineering in Agriculture* | Smartphone + Hough transformation para rectificación de imágenes de trigo. Open-source stitching. | P1 — Pipeline de pre-procesamiento con smartphone. | Investigacion-P1 | 10.13031/aea.14956 |
| **10** | A real-time fisheye video correction method based on Android smartphone GPU | Peng, Z.; Zhu, X.; Wu, J.; Qin, Z. | 2020 | *Optik* | Corrección de video fisheye en GPU Android a 25fps. RMSE ~0.67 píxeles. | P1 — Calibración de lente para smartphone, útil para lente gran angular en huerto. | Investigacion-P1, Pipeline | 10.1016/j.ijleo.2020.165108 |
| **11** | Video Stabilization for Camera Shoot in Mobile Devices via Inertial-Visual State Tracking | Han, F.; Xie, L.; Yin, Y.; Zhang, H.; Chen, G.; Lu, S. | 2021 | *IEEE Trans. Mobile Computing* | Fusión IMU + visión para estabilización. 32% mejor que SOTA. 32.6ms latencia. Probado en walking, climbing, riding. | P2 — Principal respaldo de que estabilización IMU supera a óptica en caminata. | Investigacion-P2, Pipeline | IEEE |
| **12** | Deep Online Video Stabilization Using IMU Sensors | Li, C.; Song, L.; Chen, S.; Xie, R.; Zhang, W. | 2023 | *IEEE Trans. Multimedia* | Sensor-driven online stabilization. 25fps en 1080p. Euler angles + acceleration de IMU. | P2 — Respaldo de IMU para estabilización en tiempo real. | Investigacion-P2, Pipeline | 10.1109/TMM.2022.3142429 |
| **13** | Towards Visual-Inertial Integration: Multi-Modal Collaboration-based Video Stabilization | Li, C.; Bu, Y.; Xie, L. | 2025 | *IEEE ICDCS 2025* | Gyroscope + clustering + relative-depth. 47.8% SSIM mejora, 37% más rápido. | P2 — Respaldo cuantitativo más alto (47.8% SSIM). | Investigacion-P2, Pipeline | 10.1109/ICDCS63083.2025.00107 |
| **14** | Dual-Modality Cross-Interaction-Based Hybrid Full-frame Video Stabilization | Jang, J.S.; Ban, Y.; Lee, K. | 2024 | *Applied Sciences* | IMU motion compensation + optical flow + neural rendering. 18% Stability score. | P2 — Estabilización híbrida IMU+visión para full-frame. | Investigacion-P2 | 10.3390/app14104290 |
| **15** | A Hybrid Motion Estimation for Video Stabilization Based on an IMU Sensor | Auysakul, J.; Xu, H.; Pooneeth, V. | 2018 | *Sensors* | KLT tracker + IMU-aided motion estimator. Switching según rotación. Kalman filter. | P2 — Híbrido KLT/IMU para estabilización. | Investigacion-P2 | 10.3390/s18082708 |
| **16** | Gyroscope-Based Video Stabilization for Electro-Optical Long-Range Surveillance | Milanović, P.D.; Popadic, I.V.; Kovacevic, B.D. | 2021 | *Sensors* | Gyroscope-only stabilization. Menor complejidad computacional. Cortó ruido de movimiento a la mitad. | P2 — Respaldo de giroscopio como método eficiente vs feature-based. | Investigacion-P2 | 10.3390/s21186219 |
| **17** | IMU-Assisted Learning of Single-View Rolling Shutter Correction | Mo, J.; Islam, M.; Sattar, J. | 2020 | — | Deep network + IMU pose refinement para rolling shutter. Mejora downstream DSO. | P2 — Rolling shutter correction con IMU. | Investigacion-P2, Pipeline | Semantic Scholar |
| **18** | Point feature correction based rolling shutter modeling for EKF-based VIO | Zhang, K.; Zhang, M. | 2023 | *Measurement Science and Technology* | High-frequency IMU + Android phone. Supera SOTA en precisión y costo computacional. Online self-calibration. | P2 — Rolling shutter en Android con IMU. | Investigacion-P2, Pipeline | 10.1088/1361-6501/ad044e |
| **19** | Simultaneous Video Stabilization and Rolling Shutter Removal | Wu, H.; Xiao, L.; Wei, Z. | 2021 | *IEEE Trans. Image Processing* | Joint modeling de jitter + rolling shutter. Superior a SOTA. | P2 — Tratamiento conjunto de estabilización + RS. | Investigacion-P2 | 10.1109/TIP.2021.3073865 |
| **20** | Robust Single Image Deblurring Using Gyroscope Sensor | Ji, S.W.; Hong, J.P.; Lee, J.; Baek, S.; Ko, S.J. | 2021 | *IEEE Access* | Gyroscope guidance para deblurring. Mejora feature detectors/descriptors. | P2 — Deblurring guiado por giroscopio. | Investigacion-P2 | 10.1109/ACCESS.2021.3084968 |
| **21** | Inertial-aided Motion Deblurring with Deep Networks | Mustaniemi, J.; Kannala, J.; Särkkä, S.; Matas, J.; Heikkilä, J. | 2018 | — | Gyroscope + CNN. Tiempo real. Maneja blur no-uniforme mejor que baselines. | P2 — Pionero en deblurring con IMU. | Investigacion-P2 | Semantic Scholar |
| **22** | IMU-aided adaptive mesh-grid based video motion deblurring | Arslan, A.; Gultekin, G.K.; Saranli, A. | 2024 | *PeerJ Computer Science* | IMU-informed adaptive mesh. **5% PSNR gain, 19% menos cómputo.** | P2 — Mejor métrica cuantitativa de deblurring con IMU. | Investigacion-P2, Pipeline | 10.7717/peerj-cs.2540 |
| **23** | Sensor Logger: A Framework for Smartphone-based Sensor Data Collection | Choi, K.T.H. | 2024 | *CEUR Workshop* | Paper que valida Sensor Logger para investigación científica. App multi-plataforma con exportación CSV/JSON. | P2 — Valida la app Sensor Logger como herramienta de investigación. | Investigacion-P1, Pipeline | CEUR-WS |
| **24** | Mobile AR Sensor (MARS) Logger | — | 2020 | *arXiv* | Logger para SLAM. Sincronización Camera2 API + SensorEvent. Offsets <5ms. | P2 — Fundamento técnico de sincronización video-IMU en Android. | Pipeline | arXiv:2001.00470 |
| **25** | Influence of Sampling Rate on IMU Orientation Estimation for Human Movement | Fan, B. et al. | 2025 | *Sensors* | **100 Hz suficiente para walking.** 200 Hz para running. Acelerómetro >100 Hz degrada precisión. | P2 — Resuelve la pregunta de frecuencia de muestreo IMU óptima. | Investigacion-P2, Pipeline, Metodologia | 10.3390/s25071976 |
| **26** | Non-Linear Filter for Video Stabilization + Rolling Shutter on Mobile Devices | Bell; Troccoli; Pulli | 2014 | *ECCV* | Gyroscope-based stabilization + RS correction. Real-time. Supera feature-based. Fundamento de Gyroflow. | P2 — Paper clásico, cita obligada para justificar estabilización IMU. | Pipeline | NVIDIA Research |
| **27** | Sensor Fusion of a Mobile Device to Acquire Videos of Coffee Branches | Ramos Giraldo, P.J.; Guerrero Aguirre, A.; Muñoz, C.M.; Prieto, F.A.; Oliveros, C.E. | 2017 | *Sensors* | Samsung Galaxy S5, 1080p 30fps, AUTO (ISO/WB), IMU para blur detection. Velocidad 3 cm/s. Holder con botones. Ángulo 11.3°. | P1+P3+M — Metodología más parecida a la nuestra. Usan AUTO + IMU correctivo vs nuestro preventivo. | Investigacion-P1, Metodologia | 10.3390/s17040786 |
| **28** | Using YOLOv3 Algorithm with Pre- and Post-Processing for Apple Detection | Kuznetsova, A.; Maleva, T.; Soloviev, V. | 2020 | *Agronomy* | Nikon D3500. **Compara 4 distancias: 0.2, 0.5, 1.0, 2.0m.** 4 condiciones de luz. Varias resoluciones. Pre/post-processing. | P3 — Único paper que compara distancias con métricas. Crítico para justificar distancia 0.5-1.5m. | Pipeline, Metodologia | 10.3390/agronomy10071016 |
| **29** | YOLOv5s-FP: Pear Detection with Transformer Encoder | Li, L. et al. | 2023 | *Sensors* | Cámaras CCD en trípode + UAV DJI Phantom 4. 4 horarios (7-8AM, 10-11AM, 2-3PM, 6-7PM). Velocidad UAV 1 m/s. Ángulo 20°-80°. | P3 — Metodología multi-horario para cubrir condiciones de luz variables. | Metodologia | 10.3390/s23010030 |
| **30** | RipSetCocoaCNCH12: Dataset for Ripeness Stage Detection | Restrepo-Arias, J.F.; Salinas-Agudelo, M.I.; Hernandez-Pérez, M.I.; et al. | 2023 | *Data* | 5 smartphones. 8AM-4PM. Trayectoria zigzag. 1:1 aspect ratio, 3000×3000px. Anotación CVAT. | P3+M — Metodología multi-dispositivo, zigzag. Respalda horarios 8AM-4PM. | Investigacion-P1, Metodologia | 10.3390/data8070112 |
| **31** | Deep-learning-based orange counting via video sequences (OrangeYolo + OrangeSort) | — | 2024 | *Computers and Electronics in Agriculture* | Rover + DJI Osmo Action. **2 m/s uniforme.** Cámara perpendicular. 60fps 1080p. FOV 145°. MAE = 0.081. | P3 — Velocidad de captura para tracking. Estrategia anti-doble conteo (OrangeSort). | Pipeline, Metodologia | GitHub: I3-Laboratory/orange-dataset |
| **32** | Strawberry longitudinal dataset (LabFruits) | Kirk, R. et al. | 2020 | *University of Lincoln* | 3 cámaras a 45°. Plataforma robótica Thorvald. 3 veces/día, 3 veces/semana, 2 meses. 1920×1080. Datos climáticos. | M — Metodología longitudinal con múltiples vistas y datos ambientales. | Metodologia | GitHub: RaymondKirk/labfruits_dataset |
| **33** | Fruits hidden by green: YCCB-YOLO for young citrus | Ang, G.; Zhiwei, T.; Wei, M.; et al. | 2024 | *Frontiers in Plant Science* | **Redmi K60 Ultra.** Fotos + video con keyframes. 3 períodos (mañana, mediodía, tarde). 1400 imágenes. LabelImg. | M — Metodología más cercana a nuestro cultivo (cítricos). Usan video + keyframes. | Metodologia | 10.3389/fpls.2024.1375118 |
| **34** | A Dynamic Kalman Filtering for Multi-Object Fruit Tracking | Zhai, Y.; Zhang, L.; Hu, X.; Yang, F.; Huang, Y. | 2025 | *Sensors* | YOLOv8n + Kalman dinámico + camera motion compensation. **MOTA 95.0%, HOTA 82.4%.** R² = 0.85. | P2+M — Tracking con compensación de movimiento de cámara. Útil para pipeline MOT. | Metodologia | 10.3390/s25134138 |
| **35** | AgriSORT: Online Real-time Tracking-by-Detection for Agriculture | — | 2023 | *arXiv* | Tracking con Kalman Filter adaptado a agricultura. Compensación de movimiento de cámara con optical flow. | P2+M — Algoritmo de tracking específico para agricultura con cámara en movimiento. | Metodologia | arXiv:2309.13393 |
| **36** | Coffee cherry counting with YOLOv8 + farmers | — | 2024 | *Precision Agriculture* | **Farmers con sus smartphones.** 3 ramas/árbol. 6AM-6PM. Sin sol directo. Res: 768×768 a 1024×1024. 2,968 árboles. | M — Protocolo masivo simplificado. Demuestra que farmers pueden capturar con smartphones sin entrenamiento. | Metodologia | Semantic Scholar |
| **37** | Apple detection Redmi Note 7 + YOLOv8n | — | 2025 | *Plants* | Redmi Note 7. **Distancia 0.3-1.5m.** 5 condiciones de luz. Android app desplegada. Distancia entre hileras 4m. | P3 — Distancia 0.3-1.5m y 5 condiciones de luz validadas para detección. | Pipeline, Metodologia | Semantic Scholar (PDF) |
| **38** | DHN-YOLO: strawberry detection ridge-type | — | 2025 | — | Smartphone cámara trasera. **50-80cm, ángulo 45°.** 2066 imágenes. Res: 1024×768. Aumentación a 5018. | P3 — Distancia y ángulo para fresas en ridge-planting. | Metodologia | Semantic Scholar |
| **39** | Hawthorn detection with Huawei Nova 7 | — | 2025 | *Sensors* | **Huawei Nova 7.** Distancia 0.1-1.0m. 3 ángulos (overhead, level, upward). 3 condiciones de luz (backlight, front, normal). | P3 — Múltiples ángulos y distancias con smartphone. | Metodologia | Semantic Scholar |
| **40** | Flash-No-Flash controlled illumination for fruit detection | Kurtser, P. et al. | — | — | Exposición fija a 20µs (mínima) para eliminar efectos de iluminación. FNF mejora detección: Precision 95% a Recall 95%. | P1 — Respalda que estabilizar condiciones de captura mejora detección. | Pipeline | Semantic Scholar |
| **41** | ICNet: Illumination Compensation for Intercropping | — | 2025 | — | Compensación de iluminación mejora PSNR de 28dB a 40.79dB. Demuestra que iluminación variable degrada detección. | P1 — Evidencia de que iluminación no controlada afecta detección. | Pipeline | Semantic Scholar |
| **42** | DCNet: Low-visibility fruit detection | — | 2025 | — | Detección en baja visibilidad. 86.5% mAP. Demuestra que condiciones adversas degradan significativamente la detección. | P1 — Apoya la necesidad de controlar condiciones de captura. | Pipeline | Semantic Scholar |
| **43** | Gimbal influence on exterior orientation parameters (UAV) | Gašparović, M.; Jurjević, L. | — | *Sensors* | **Gimbal mejora 6x estabilidad.** Roll/pitch 69.9° sin gimbal → 2.56° con gimbal. | H — Respaldo cuantitativo del uso de gimbal para estabilización. | Pipeline | Semantic Scholar |
| **44** | EMA-YOLO: yellow peach detection | — | — | — | Smartphone a diferentes distancias. Compara corta, media y larga distancia. Muestra que distancia afecta detección. | P3 — Evidencia de que distancia impacta mAP. | Pipeline | Semantic Scholar |
| **45** | Apple fruit recognition with MSX thermal imaging | Feng, J.; Zeng, L.; He, L. | 2019 | *Sensors* | Cámara térmica FLIR. Distancia 1-1.5m. Ángulo óptimo -16°. Imágenes 9AM. | P3 — Ángulo de cámara óptimo documentado. | Metodologia | 10.3390/s19040927 |

---

## Papers de documentación técnica (no académicos)

| # | Nombre | Tipo | Contexto | Link |
|---|---|---|---|---|
| D1 | Open Camera Help | Documentación oficial | Justificación de controles manuales (AF Lock, AE Lock, WB Lock, ISO, shutter, bitrate) | https://opencamera.sourceforge.io/help.html |
| D2 | Gyroflow Documentation | Documentación oficial | Estabilización IMU-based, compatibilidad con Sensor Logger, sincronización | https://docs.gyroflow.xyz/ |
| D3 | Sensor Logger Official Site | App documentation | Validación de la app, sensores soportados, formatos de exportación | https://www.tszheichoi.com/sensorlogger |
| D4 | OpenCamera Sensors (GitHub) | Repositorio open-source | Fork con sincronización video-IMU nativa | https://github.com/prime-slam/opencamera-sensors |
| D5 | Gyroflow GitHub | Repositorio open-source | 8.9k stars, 40+ contribuidores, 24 releases | https://github.com/gyroflow/gyroflow |
| D6 | Object recognition + IMU (GitHub) | Repositorio open-source | Kalman Filter + IoU con IMU para post-procesar detecciones YOLO | https://github.com/zhouzypaul/object-recognition-imu |

---

## Resumen por fuente

| Fuente | Cantidad de papers |
|---|---|
| **Elicit P1** (Software) | 16 |
| **Elicit P2** (IMU) | 12 |
| **Semantic Scholar** (adicionales) | 17 |
| **Documentación técnica** | 6 |
| **Total** | **45** |

---

## Papers más citados en el proyecto

| # | Veces referenciado | En |
|---|---|---|
| Fan et al. (2025) — Sampling rate IMU | 3 archivos | P2, Pipeline, Metodologia |
| Kuznetsova et al. (2020) — Apple distances | 2 archivos | Pipeline, Metodologia |
| Ramos Giraldo et al. (2017) — Coffee + IMU | 2 archivos | P1, Metodologia |
| Gašparović — Gimbal stability | 2 archivos | Pipeline, Metodologia |
| Arslan et al. (2024) — IMU deblurring | 2 archivos | P2, Pipeline |
| Li et al. (2025) — Visual-Inertial 47.8% SSIM | 2 archivos | P2, Pipeline |
