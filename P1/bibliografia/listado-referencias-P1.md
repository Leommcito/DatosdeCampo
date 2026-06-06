# Bibliografía del Paso 1 — Software de Captura y Bloqueo de Sensores

**Proyecto:** Protocolo de captura manual con smartphone en huertos densos de mandarinas para YOLO + MOT
**Última actualización:** 05/06/2026
**Total de referencias:** 17 (16 papers académicos + 1 documentación técnica)

---

## 🔴 Sección 1 — Crítico (Decisiones centrales del pipeline)

Estos papers proporcionan la **evidencia más sólida** para justificar las decisiones del Paso 1. Definen el núcleo del protocolo de captura.

---

### P40 — Flash-No-Flash Controlled Illumination for Fruit Detection

| Campo | Valor |
|---|---|
| **Autores** | Kurtser, P. et al. |
| **Año** | — |
| **Publicación** | — |
| **Hallazgo clave** | Exposición fija a 20µs (mínima) para eliminar efectos de iluminación. FNF mejora detección: Precision 95% a Recall 95%. |
| **Contexto en P1** | Respalda que estabilizar condiciones de captura mejora detección. |
| **Justifica** | Etapa 1 — Bloqueo AE/AF/WB |
| **Referenciado en** | Pipeline |
| **Link** | Semantic Scholar |

---

### P57 — Overcurrent-Driven LEDs for Consistent Image Colour and Brightness in Agricultural Machine Vision

| Campo | Valor |
|---|---|
| **Autores** | Mirbod, O.; Choi, D.; Thomas, R.; He, L. |
| **Año** | 2021 |
| **Publicación** | *Computers and Electronics in Agriculture* (Elsevier), Vol. 187 |
| **Hallazgo clave** | **85% reducción** variación HSV con LED fijo vs auto-exposición. Error motion blur 7mm → 1mm a 7km/h. Auto-exposición falla catastróficamente con sol frontal. |
| **Contexto en P1** | Demuestra que parámetros fijos + iluminación controlada eliminan variabilidad. |
| **Justifica** | Etapa 1 — ISO/shutter fijo |
| **DOI** | 10.1016/j.compag.2021.106266 |
| **Link** | ScienceDirect |

---

### P58 — Land-based Crop Phenotyping by Image Analysis: Consistent Canopy Characterization from Inconsistent Field Illumination

| Campo | Valor |
|---|---|
| **Autores** | Chopin, J.; Kumar, P.; Miklavcic, S.J. |
| **Año** | 2018 |
| **Publicación** | *Plant Methods*, Vol. 14, Article 39 |
| **Hallazgo clave** | **Error MSE: 1.57 (manual) vs 4.26 (auto)** bajo iluminación cambiante. Exposición manual + corrección de color es superior. Manual es **2.7x más consistente**. |
| **Contexto en P1** | Comparación directa manual vs auto en condiciones de campo. |
| **Justifica** | Etapa 1 — AE Lock, exposición manual |
| **DOI** | 10.1186/s13007-018-0308-5 |
| **Link** | Springer (Open Access) |

---

### P62 — A Calibration Method for Smartphone Camera Photoplethysmography (Camera2 API)

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2023 |
| **Publicación** | *Frontiers in Digital Health* (PMC10705321) |
| **Hallazgo clave** | Tone mapping automático aplica **transformaciones no lineales irreversibles** ("cannot be reversed in post processing"). Camera2 API permite configurar tone mapping lineal. **74% menor MAE** con calibración. WB lock esencial para color consistente. |
| **Contexto en P1** | Valida Camera2 API para control manual en investigación. ✅ **Corregido**: la fuente correcta es Frontiers in Digital Health, no Nature/PMC. |
| **Justifica** | Etapa 1 — Camera2 API, WB Lock, tone mapping lineal |
| **DOI** | 10.3389/fdgth.2023.1301019 |
| **Link** | PMC10705321 |

---

### P96 — Why is the Video Analytics Accuracy Fluctuating, and What Can We Do About It? (Camera as Unintentional Adversary)

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2022 |
| **Publicación** | *ECCV* (European Conference on Computer Vision) |
| **Hallazgo clave** | La cámara actúa como **"unintentional adversary"**: cambios automáticos de parámetros causan **13-14% fluctuación** en detección en escenas estáticas. Transfer-learning redujo errores de tracking **~40%**. Ground truth 29 tracks → modelo original creó **157 track-IDs** (5.4x falsos). |
| **Contexto en P1** | Evidencia directa de que los parámetros automáticos de cámara degradan la detección y tracking. |
| **Justifica** | Etapa 1 — Bloqueo de parámetros automáticos, impacto en tracking |
| **Link** | arXiv:2208.12644 |

---

## 🟠 Sección 2 — Alta (Respaldan decisiones técnicas)

Estos papers proporcionan **evidencia complementaria sólida** y contexto técnico para las decisiones del Paso 1.

---

### P41 — ICNet: Illumination Compensation for Intercropping

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2025 |
| **Publicación** | — |
| **Hallazgo clave** | Compensación de iluminación mejora PSNR de 28dB a 40.79dB. Demuestra que iluminación variable degrada detección. |
| **Contexto en P1** | Evidencia de que iluminación no controlada afecta detección. |
| **Justifica** | Etapa 1 — Bloqueo AE |
| **Referenciado en** | Pipeline |
| **Link** | Semantic Scholar |

---

### P49 — Designing a Proximal Sensing Camera Acquisition System for Vineyard Applications: 8 Years of Experiments

| Campo | Valor |
|---|---|
| **Autores** | Rançon, F.; Keresztes, B.; Deshayes, A.; et al. |
| **Año** | 2023 |
| **Publicación** | *Sensors* |
| **Hallazgo clave** | **Cámara industrial Basler Ace + flash xenon.** Exposición 250 µs, obturador global. App Android para control remoto vía Wi-Fi. 8 años de desarrollo. Iluminación controlada + obturador global eliminan motion blur. |
| **Contexto en P1** | Respalda fijar shutter speed y usar iluminación controlada. |
| **Justifica** | Etapa 1 — Shutter controlado, Etapa 6 — Iluminación |
| **DOI** | 10.3390/s23020847 |
| **Link** | MDPI Sensors |

---

### P55 — Rice Grain Moisture Content Measurement with Smartphone (Rice GMC)

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2021 |
| **Publicación** | *Sensors* |
| **Hallazgo clave** | **iPhone 8. ISO=25 fijo, shutter=1/400s, f/1.8, distancia 27.5cm.** "To minimize lighting-related factors, the smartphone camera parameters were fixed". Usaron tabla de calibración de color (Spyder Checkr 24). |
| **Contexto en P1** | Paper que demuestra la necesidad de fijar parámetros en campo con justificación explícita. |
| **Justifica** | Etapa 1 — ISO fijo, shutter fijo |
| **DOI** | 10.3390/s21175875 |
| **Link** | Semantic Scholar (PDF rice GMC) |

---

### P59 — A Robust Illumination-Invariant Camera System for Agricultural Applications

| Campo | Valor |
|---|---|
| **Autores** | Silwal, A.; Parhar, T.; Yandun, F.; Kantor, G. (CMU/Robotics Institute) |
| **Año** | 2021 |
| **Publicación** | *IROS 2021* (IEEE/RSJ International Conference on Intelligent Robots and Systems) — arXiv preprint |
| **Hallazgo clave** | Redes entrenadas con imágenes consistentes requieren **4x menos datos**. Faster-RCNN: AP 0.71 con iluminación controlada vs casi 0 con luz natural extrema. |
| **Contexto en P1** | Parámetros fijos reducen datos necesarios para entrenar. Respalda bloqueo de exposición. |
| **Justifica** | Etapa 1 — Consistencia de captura |
| **DOI** | 10.1109/IROS51168.2021.9636542 |
| **Link** | arXiv:2101.02190 |

---

### P61 — Stabilizing and Accelerating Autofocus with Expert Trajectory Regularized Deep Reinforcement Learning

| Campo | Valor |
|---|---|
| **Autores** | Zhu, S.; Li, C.; Jiang, Y.; Wei, L.; Kan, N.; Zheng, Z.; Dai, W.; Zou, J.; Xiong, H. |
| **Año** | 2025 |
| **Publicación** | *CVPR 2025* (IEEE/CVF Conference on Computer Vision and Pattern Recognition) |
| **Hallazgo clave** | Focus hunting (FH) causa que el lente oscile repetidamente creando **inestabilidad en video**. FH reduce nitidez y cambia el FoV. Logran reducción de FH de 9.1% a 18.0% con DRL. |
| **Contexto en P1** | Documenta que el focus hunting es un problema real en cámaras modernas. |
| **Justifica** | Etapa 1 — AF Lock |
| **Link** | openaccess.thecvf.com/CVPR2025 |

---

### P95 — Impact of ISP Tuning on Object Detection

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2023 |
| **Publicación** | *MDPI J. Imaging* 9(12), 260 |
| **Hallazgo clave** | Contraste, gamma y saturación (componentes del ISP automático) causan **degradación significativa** en YOLOv5/v8, Faster R-CNN, RT-DETR. La variación de ISP afecta **desproporcionadamente a objetos pequeños**. La mayoría de errores son **falsos negativos** (objetos no detectados). |
| **Contexto en P1** | Demuestra que el pipeline ISP automático degrada la detección YOLO. |
| **Justifica** | Etapa 1 — ISP tuning, degradación de detección por procesamiento automático |
| **DOI** | 10.3390/jimaging9120260 |
| **Link** | MDPI J. Imaging |

---

### P97 — ISP-less Low-Power Computer Vision (RAW Detection)

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2022 |
| **Publicación** | *arXiv* |
| **Hallazgo clave** | Detección en **dominio RAW supera a RGB procesado por ISP** en 7.1% precisión. Aprendizaje de gamma correction en RAW supera baseline RGB. "Freedom from the nonlinear distortions introduced by the ISP pipeline" (RAWild, 2026). |
| **Contexto en P1** | Confirma que el procesamiento ISP (tone mapping, gamma) pierde información útil para detección. |
| **Justifica** | Etapa 1 — RAW vs ISP, calidad de datos de entrenamiento, tone mapping |
| **Link** | arXiv:2210.05451 |

---

### P98 — AdaptiveISP: Learning an Adaptive Image Signal Processor for Object Detection

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2024 |
| **Publicación** | *NeurIPS* (Conference on Neural Information Processing Systems) |
| **Hallazgo clave** | ISP puede optimizarse específicamente para detección. AdaptiveISP logra **mAP@0.5 de 71.4 vs baseline 55.6 (28% mejora)**. Solo algunas etapas ISP son útiles para detección — el pipeline default es **sub-óptimo** para visión computacional. |
| **Contexto en P1** | Confirma que el ISP por defecto NO es óptimo para detección. |
| **Justifica** | Etapa 1 — ISP sub-óptimo para detección, RAW vs procesado |
| **Link** | arXiv:2410.22939 |

---

## 🟡 Sección 3 — Media e Informativa (Contexto metodológico y documentación)

Estos papers proporcionan **contexto adicional** y documentación técnica de las herramientas seleccionadas.

---

### P60 — Optimizing Image Acquisition Systems for Autonomous Driving (CNN + Exposure Bias)

| Campo | Valor |
|---|---|
| **Autores** | Blasinski, H.; Farrell, J.; Lian, T.; Liu, Z.; Wandell, B. (Stanford University) |
| **Año** | 2018 |
| **Publicación** | *IS&T Electronic Imaging Symposium* (Stanford / Google Research) |
| **Hallazgo clave** | Redes entrenadas con exposiciones específicas no generalizan bien a exposiciones diferentes. Las CNN son asimétricas: manejan mejor sub-exposición que sobre-exposición. Entrenar con mezcla de exposiciones ayuda pero reduce precisión óptima. |
| ⚠️ **Nota** | La cifra de "~20% caída de precisión" no pudo ser verificada en el paper original encontrado. El paper SÍ demuestra que exposiciones subóptimas degradan CNNs, pero el valor exacto requiere verificación. |
| **Contexto en P1** | Evidencia de que exposición inconsistente degrada CNN. Respalda AE Lock. |
| **Justifica** | Etapa 1 — AE Lock |
| **DOI** | 10.2352/ISSN.2470-1173.2018.05.PMII-161 |

---

### P63 — Kiwifruit Detection in Orchard Conditions Using a FCN with Preprocessing

| Campo | Valor |
|---|---|
| **Autores** | University of Auckland's Centre for Automation and Robotic Engineering Science |
| **Año** | 2020 |
| **Publicación** | *arXiv* preprint |
| **Hallazgo clave** | Sin preprocesamiento: **F1 0.82** en imágenes normales vs **0.13** en imágenes con glare (luz directa no controlada). Con preprocessing (histogram equalization): F1 mejora a 0.42. |
| **Contexto en P1** | Demuestra que condiciones de luz adversas degradan severamente la detección. |
| **Justifica** | Etapa 1 — Condiciones de captura |
| **Link** | arXiv:2006.11729 |

---

### P99 — Assessing Nutritional Pigment Content of Green and Red Leafy Vegetables via Digital Image Analysis

| Campo | Valor |
|---|---|
| **Autores** | — |
| **Año** | 2024 |
| **Publicación** | *PMC* (12057810) |
| **Hallazgo clave** | Usa **Open Camera v1.52** en Redmi Note 7 Pro. **ISO=200 fijo, shutter=1/100s, AF deshabilitado, compensación de exposición deshabilitada**. Razón explícita: "to ensure uniformity across images". Iluminación LED controlada 4000K, 4 neutral-white LED tube-lights, 50cm distancia. |
| **Contexto en P1** | **Único paper encontrado que documenta Open Camera** con configuración detallada y justificación explícita. Matiza el claim de que "ningún paper documenta apps de cámara". |
| **Justifica** | Etapa 1 — Open Camera, justificación de parámetros fijos en investigación |
| **Link** | PMC12057810 |

---

### D1 — Open Camera Help (Documentación Técnica)

| Campo | Valor |
|---|---|
| **Nombre** | Open Camera Help |
| **Tipo** | Documentación oficial de la aplicación |
| **Desarrollador** | Mark Harman |
| **Licencia** | GPLv3 (gratuita y open-source) |
| **Contexto en P1** | Justificación de controles manuales disponibles: AF Lock, AE Lock, WB Lock, ISO manual, Shutter manual, Bitrate configurable, Camera2 API. |
| **Justifica** | Etapa 1 — App de Cámara (todos los parámetros) |
| **Link** | https://opencamera.sourceforge.io/help.html |

---

## Resumen

| Sección | Nivel | Cantidad | IDs |
|---|---|---|---|
| **1** | 🔴 **Crítico** | 5 | P40, P57, P58, P62, P96 |
| **2** | 🟠 **Alta** | 8 | P41, P49, P55, P59, P61, P95, P97, P98 |
| **3** | 🟡 Media / ⚪ Informativa | 4 | P60, P63, P99, D1 |
| | **Total** | **17** | |

### Trazabilidad: Decisión ↔ Paper

| Decisión del Paso 1 | IDs que la justifican |
|---|---|
| **AE Lock** (Exposición fija) | P57, P58, P60, P96 |
| **AF Lock** (Foco fijo) | P61, P96 |
| **WB Lock** (Balance de blancos fijo) | P62 |
| **ISO fijo** | P55 (principio, valor ISO=25), P57 (principio, baja ganancia), P99 (valor ISO=200 documentado en Open Camera) |
| **Shutter fijo** | P49 (principio, ~250µs cámara industrial), P55 (principio, 1/400s arroz), P99 (valor 1/100s documentado en Open Camera) |
| **Camera2 API / Open Camera** | P40, P62, P99, D1 |
| **ISP automático degrada detección** | P95, P97, P98 |
| **Condiciones de luz controladas** | P41, P59, P63 |
| **Parámetros automáticos degradan tracking** | P96 |
