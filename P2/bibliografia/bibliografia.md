# Bibliografía del Paso 2 — Registro de Telemetría IMU

Referencias utilizadas en [Investigacion-P2-IMU-Telemetria.md](../Investigacion-P2-IMU-Telemetria.md), organizadas por nivel de impacto al pipeline.

---

## 🔴 Grupo 1 — Decisiones críticas del pipeline

Justifican reglas que afectan directamente la configuración de captura y post-procesamiento.

| ID | Título | Autores | Año | Publicación | Resumen | Contexto en P2 | Importancia | Justifica a | Link / DOI |
|---|---|---|---|---|---|---|---|---|---|
| **P25** | Influence of Sampling Rate on IMU Orientation Estimation for Human Movement | Fan, B. et al. | 2025 | *Sensors* | **100 Hz suficiente para walking.** 200 Hz para running. Acelerómetro >100 Hz degrada precisión. Testeado 10-1600 Hz, 17 sujetos, ground truth mocap óptico. | Resuelve la frecuencia de muestreo IMU óptima (100 Hz). | 🔴 Crítico | Etapa 3 — Logging IMU (100 Hz) | 10.3390/s25071976 |
| **P64** | DeepOIS: Gyroscope-Guided Deep Optical Image Stabilizer Compensation | — | 2021 | *arXiv* (2101.11183) | OIS mueve el lente independientemente del cuerpo. **Error alineación: 0.688 (sin OIS) vs 1.038 (con OIS) — 50% peor.** "OIS terminates the possibility of image registration by gyros." | Evidencia directa de que OIS interfiere con Gyroflow. Justifica regla OIS OFF. | 🔴 Crítico | Etapa 2 — Regla OIS OFF | arXiv:2101.11183 |
| **P43** | Gimbal influence on exterior orientation parameters (UAV) | Gašparović, M.; Jurjević, L. | — | *Sensors* | **Gimbal mejora 6x estabilidad.** Roll/pitch 69.9° sin gimbal → 2.56° con gimbal. | Respaldo cuantitativo del uso de gimbal para estabilización. | 🔴 Crítico | Etapa 2 — Estabilización (Gimbal) | Semantic Scholar |
| **P11** | Video Stabilization for Camera Shoot in Mobile Devices via Inertial-Visual State Tracking | Han, F.; Xie, L.; Yin, Y.; Zhang, H.; Chen, G.; Lu, S. | 2021 | *IEEE Trans. Mobile Computing* | Fusión IMU + visión para estabilización. **32% mejor que SOTA.** 32.6ms latencia. Probado en walking, climbing, riding. | Principal respaldo de que estabilización IMU supera a óptica en caminata. | 🔴 Crítico | Etapa 2 — Estabilización (IMU) | IEEE |
| **P13** | Towards Visual-Inertial Integration: Multi-Modal Collaboration-based Video Stabilization | Li, C.; Bu, Y.; Xie, L. | 2025 | *IEEE ICDCS 2025* | Gyroscope + clustering + relative-depth. **47.8% SSIM mejora**, 37% más rápido. | Respaldo cuantitativo más alto (47.8% SSIM). | 🔴 Crítico | Etapa 2 — Estabilización (IMU) | 10.1109/ICDCS63083.2025.00107 |
| **P22** | IMU-aided adaptive mesh-grid based video motion deblurring | Arslan, A.; Gultekin, G.K.; Saranli, A. | 2024 | *PeerJ Computer Science* | IMU-informed adaptive mesh. **5% PSNR gain, 19% menos cómputo.** | Mejor métrica cuantitativa de deblurring con IMU. | 🔴 Crítico | Etapa 6 — Pre-procesamiento (Deblurring) | 10.7717/peerj-cs.2540 |

---

## 🟠 Grupo 2 — Respaldo técnico con evidencia cuantitativa

Apoyan las decisiones del pipeline con métricas y evidencia experimental.

| ID | Título | Autores | Año | Publicación | Resumen | Contexto en P2 | Importancia | Justifica a | Link / DOI |
|---|---|---|---|---|---|---|---|---|---|
| **P26** | Non-Linear Filter for Video Stabilization + Rolling Shutter on Mobile Devices | Bell, S.; Troccoli, A.; Pulli, K. | 2014 | *ECCV* (NVIDIA) | Gyroscope-based stabilization + RS correction. Real-time (~160μs filter time). Supera feature-based. **Fundamento de Gyroflow.** | Paper clásico, fundamento teórico de la estabilización IMU. Cita obligada. | 🟠 Alta | Etapa 2 — Estabilización (Gyroflow) | NVIDIA Research |
| **P12** | Deep Online Video Stabilization Using IMU Sensors | Li, C.; Song, L.; Chen, S.; Xie, R.; Zhang, W. | 2023 | *IEEE Trans. Multimedia* | Sensor-driven online stabilization. **25fps en 1080p.** Euler angles + acceleration de IMU. | Respaldo de IMU para estabilización en tiempo real. | 🟠 Alta | Etapa 2 — Estabilización (IMU) | 10.1109/TMM.2022.3142429 |
| **P18** | Point feature correction based rolling shutter modeling for EKF-based VIO | Zhang, K.; Zhang, M. | 2023 | *Measurement Science and Technology* | High-frequency IMU + Android phone. **Supera SOTA en precisión y costo computacional.** Online self-calibration. | Rolling shutter en Android con IMU. | 🟠 Alta | Etapa 2 — Estabilización (Gyroflow RS) | 10.1088/1361-6501/ad044e |
| **P65** | Image Stabilization Influence on Photogrammetric Accuracy | — | 2022 | *ISPRS* | **IS debe desactivarse** para modelado 3D. Incertidumbre parámetros **hasta 300% mayor** con IS activado. Error reproyección **4x mayor.** | Respalda desactivar OIS desde fotogrametría. | 🟠 Alta | Etapa 2 — Regla OIS OFF | ISPRS |
| **P66** | Mango Fruit Load Estimation Using Video Based MangoYOLO-Kalman Filter-Hungarian Algorithm | — | 2019 | *Sensors* (10.3390/s19122742) | Video detection: **62.3%** conteo real vs **40.2%** foto estática. **+22% mejora.** ⚠️ Mejora es por tracking multi-vista, no estabilización. | Video supera a fotos para conteo, pero la mejora no es por estabilización. | 🟠 Alta | Etapa 2 — Video vs fotos | 10.3390/s19122742 |
| **P67** | Crop Row Video Stabilization for Agricultural Field Robotics | — | — | *MDPI Sensors* | Desplazamiento lateral suprimido: **66%** del espacio entre hileras. Desviación: ~20px (desde 93px inicial). | Justifica estabilización en agricultura con métricas cuantitativas. | 🟠 Alta | Etapa 2 — Estabilización agrícola | MDPI Sensors |
| **P68** | Lightweight GAN for Restoring Blurred Images to Enhance Citrus Detection | — | 2025 | *MDPI* | **mAP@0.5:0.95 +86.4%** tras restaurar. Recall **+76.9%**. ⚠️ El 86.4% es mejora relativa. Degradación real: 48.6% (0.630 → 0.324). | Motion blur degrada severamente detección YOLO. | 🟠 Alta | Etapa 2 — Motion blur vs YOLO | MDPI 2025 |
| **P100** | Combined Electronic Image Stabilization and Optical Image Stabilization (Qualcomm Patent) | — | 2024 (granted) | *US Patent US20200412954A1* | OIS+EIS combinados con sensores Hall. EIS filter se ajusta según posición OIS. | **Contradice** OIS OFF para sistemas con Hall sensor. Confirma regla para sensores externos. | 🟠 Alta | Etapa 2 — OIS OFF (matiz) | US Patent |
| **P103** | FEGW-YOLO: Feature-Complexity-Guided Lightweight Framework | — | 2026 | *PMC* (PMC12944136) | YOLOv8n retiene **71.9% mAP@0.5** a blur severo (k=11). Degradación ~21.4% vs 86.4% reportado. | **Contradice magnitud** de 86.4%. Degradación real ≤50%. | 🟠 Alta | Etapa 2 — Motion blur (matiz) | PMC12944136 |
| **P105** | A Novel Knowledge Distillation Framework for Small Object Detection in Blurry Environments | — | 2024 | *Springer* | Al 100% velocidad de motion, YOLOv8 pierde solo **4.6% mAP@0.5**. Con KD: solo **2.5% drop**. | **Contradice fuertemente** degradación extrema. | 🟠 Alta | Etapa 2 — Motion blur (evidencia) | 10.1007/s40747-024-01676-w |
| **P106** | Delving into YOLO Object Detection Models: Insights into Adversarial Robustness | — | 2025 | *MDPI Electronics* | YOLOv4 tiene **MEJOR robustez a blur** que YOLOv7/v9/v11. YOLOv4 ~15%, YOLOv11 ~25%. | **Contradice** que YOLO moderno sea más robusto. | 🟠 Alta | Etapa 2 — Motion blur, Etapa 7 — YOLO | 10.3390/electronics14081624 |
| **P107** | Deep Online Fused Video Stabilization | Shi, Z.; Shi, F.; Lai, W.; Liang, C.; Liang, Y. | 2022 | *WACV 2022* | **Primer híbrido IMU+DL.** Gyro-only: Stability 0.846. Fused: **0.853**. FOV 0.906 vs 0.827. | **Contradice** superioridad de IMU puro. Respalda Gyroflow (híbrido). | 🟠 Alta | Etapa 2 — Estabilización (híbrido) | arXiv:2102.01279 |
| **P108** | RStab: 3D Multi-frame Fusion for Video Stabilization | Peng, Z. et al. | 2024 | *CVPR 2024* | **SOTA.** Cropping Ratio=1.00. Stability **0.92** vs gyro-only ~0.83. | **Contradice** "IMU supera a óptica". Deep learning es SOTA. | 🟠 Alta | Etapa 2 — Estabilización (contexto SOTA) | 10.1109/CVPR52733.2024.00710 |
| **P109** | Let's Roll: A Synthetic and Real Dataset for Pedestrian Detection Across Different Shutter Types | — | 2024 | *arXiv* (2309.08136) | **RS correction NO necesaria** para detección a IoU≥0.5. A IoU≥0.5:0.95 discrepancia 24% (posición, no detección). | **Contradice** necesidad de RS correction para detección. | 🟠 Alta | Etapa 2 — RS correction (matiz) | arXiv:2309.08136 |

---

## 🟡 Grupo 3 — Contexto y matices

Información complementaria, contexto metodológico, o contradicciones que no afectan directamente las reglas del pipeline.

| ID | Título | Autores | Año | Publicación | Resumen | Contexto en P2 | Importancia | Justifica a | Link / DOI |
|---|---|---|---|---|---|---|---|---|---|
| **P14** | Dual-Modality Cross-Interaction-Based Hybrid Full-frame Video Stabilization | Jang, J.S.; Ban, Y.; Lee, K. | 2024 | *Applied Sciences* | IMU motion compensation + optical flow + neural rendering. **18% Stability score**, 3% Distortion. | Estabilización híbrida IMU+visión para full-frame. | 🟢 Baja | Contexto P2 | 10.3390/app14104290 |
| **P15** | A Hybrid Motion Estimation for Video Stabilization Based on an IMU Sensor | Auysakul, J.; Xu, H.; Pooneeth, V. | 2018 | *Sensors* | KLT tracker + IMU-aided motion estimator. Switching según rotación. Kalman filter. | Híbrido KLT/IMU para estabilización. | 🟢 Baja | Contexto P2 | 10.3390/s18082708 |
| **P17** | IMU-Assisted Learning of Single-View Rolling Shutter Correction | Mo, J.; Islam, M.; Sattar, J. | 2020 | — | Deep network + IMU pose refinement. Mejora downstream DSO. >95% dirección correcta. | Rolling shutter correction con IMU. | 🟢 Baja | Etapa 2 — RS correction | Semantic Scholar |
| **P19** | Simultaneous Video Stabilization and Rolling Shutter Removal | Wu, H.; Xiao, L.; Wei, Z. | 2021 | *IEEE Trans. Image Processing* | Joint modeling de jitter + rolling shutter. **Superior a SOTA.** | Tratamiento conjunto de estabilización + RS. | 🟢 Baja | Contexto P2 | 10.1109/TIP.2021.3073865 |
| **P20** | Robust Single Image Deblurring Using Gyroscope Sensor | Ji, S.W.; Hong, J.P.; Lee, J.; Baek, S.; Ko, S.J. | 2021 | *IEEE Access* | Gyroscope guidance para deblurring. Mejora visual + feature detectors. Sin métrica YOLO. | Deblurring guiado por giroscopio. | 🟢 Baja | Contexto P2 | 10.1109/ACCESS.2021.3084968 |
| **P21** | Inertial-aided Motion Deblurring with Deep Networks | Mustaniemi, J.; Kannala, J.; Särkkä, S.; Matas, J.; Heikkilä, J. | 2018 | — | Gyroscope + CNN. Tiempo real. Maneja blur no-uniforme. Pionero. | Pionero en deblurring con IMU. | 🟢 Baja | Contexto P2 | Semantic Scholar |
| **P101** | HyperOIS: Advanced OIS and OIS-EIS Cooperation in Smartphone Cameras | — | 2024 | *IEEE Trans. Consumer Electronics* | OIS avanzado integrado. SR -34.37dB a -26.90dB. Xiaomi 14 blur 39.17μm en 4K. | **Contradice parcialmente** OIS OFF. OIS moderno puede coexistir. | 🟡 Media | Etapa 2 — OIS OFF (contexto) | 10.1109/TCE.2024.3369029 |
| **P102** | In-Shoe System for Gait Monitoring — Effects of Sampling Rate | Torun et al. | 2021 | *Sensors* | **100 Hz inadecuado** para parámetros espaciales. Useful gait hasta 120 Hz. Óptimo: **250 Hz.** | **Contradice** suficiencia de 100 Hz. No aplica a tesis. | 🟡 Media | Etapa 3 — Logging IMU (límite) | 10.3390/s21082869 |
| **P104** | Quantization Robustness to Input Degradations for Object Detection | — | 2025 | *arXiv* (2508.19600) | Medium blur: solo **11-15% mAP drop** en YOLOv12. Modelos INT8 más robustos. | **Contradice** degradación severa. Degradación moderada. | 🟡 Media | Etapa 2 — Motion blur (contexto) | arXiv:2508.19600 |

---

## Documentación técnica

| ID | Nombre | Tipo | Contexto | Link |
|---|---|---|---|---|
| D2 | Gyroflow Documentation | Documentación oficial | Estabilización IMU-based, compatibilidad Sensor Logger, sincronización ±200ms, regla OIS OFF | https://docs.gyroflow.xyz/ |
| D5 | Gyroflow GitHub | Repositorio open-source | 8.9k stars, 40+ contribuidores, 24 releases | https://github.com/gyroflow/gyroflow |
| D7 | Gyroflow Plugins (GitHub) | Repositorio open-source | Plugins OpenFX (DaVinci Resolve), Adobe, frei0r | https://github.com/gyroflow/gyroflow-plugins |
| D4 | OpenCamera Sensors (GitHub) | Repositorio open-source | Fork con sincronización video-IMU nativa (mismo clock) | https://github.com/prime-slam/opencamera-sensors |
| D6 | Object recognition + IMU (GitHub) | Repositorio open-source | Kalman Filter + IoU con IMU para post-procesar YOLO. Brown University Paradiso Lab. | https://github.com/zhouzypaul/object-recognition-imu |
