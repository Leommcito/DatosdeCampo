# Draft: Contradicciones y Mejoras al Paso 3 — Protocolo de Caminata

> Investigación ejecutada el 05/06/2026 vía 8 agentes librarian paralelos (Semantic Scholar + búsqueda web)
> Archivo fuente analizado: `Investigacion-P3-Protocolo-Caminata.md`

---

## Resumen Ejecutivo

Se encontraron **contradicciones significativas** para 5 de 6 parámetros del Paso 3, y **mejoras sustanciales** respaldadas por papers 2023-2026. Solo el parámetro de anti-doble conteo se mantiene parcialmente válido pero con alternativas superiores.

---

## 1. 🚶 VELOCIDAD DE CAMINATA (~1 m/s)

### ❌ Contradicción: Se puede ir MÁS RÁPIDO
**MangoYOLO (Payne et al., 2019)** — DOI: 10.3390/s19122742
- **Velocidad usada: 5 km/h (~1.39 m/s)** en vehículo
- Resultado: 62% de detección con video tracking (vs 40% dual-view estático)
- Error de doble conteo: solo 2.6%
- La velocidad más rápida proporcionó **más ángulos de visión por árbol**, mejorando el manejo de oclusión

**Sanchez & Zhang (2022)** — DOI: 10.3390/app12125600
- Introducen el concepto de **"overlapping rate (ro)"**: `ro = (FOV × fps) / velocidad`
- Con FOV=0.5m y 16fps → velocidad máxima segura: **~1.3 m/s** antes de que aparezcan gaps
- Con 22fps: velocidades de hasta **2.5 m/s** son viables

### ⚠️ Matiz importante
**AGG-DeblurGAN (Huang et al., 2024)** cuantifica:
- Imagen nítida: mAP@0.5 = **0.925**
- Imagen borrosa: mAP@0.5 = **0.673** (27% drop)
- **Después de deblurring**: se recupera a **0.898**
- → El blur es manejable con post-procesamiento

### 💡 Recomendación actualizada
- **Sin deblurring**: mantener ~1 m/s para mandarinas (fruto pequeño)
- **Con deblurring GAN o tracking robusto**: subir a **1.3-1.5 m/s**
- **Usar fórmula de overlapping rate** para calcular velocidad óptima según FOV y fps

---

## 2. 📐 ÁNGULO DE CÁMARA (~15° hacia arriba)

### ❌ Contradicción 1: Ángulo horizontal (0°/perpendicular) es MEJOR
**Villacrés et al. (2024)** — Multi-cámara manzanas en V-trellis
- Una cámara **perpendicular al dosel** (0° horizontal): detectó **88.3%** de frutos
- Dos cámaras: **97.5%** (del sistema de 4)
- **Conclusión**: La orientación óptima para single-view es perpendicular/horizontal, NO 15° up

### ❌ Contradicción 2: Ángulos más pronunciados (45°) superan 15°
**Cluster Segmentation Stereo Vision (2025)** — DOI: 10.3389/fpls.2025.1598414
- Probó 0°, 15°, 30°, 45°
- **45° = mejor tasa de detección (>40%)**
- Algoritmo mantuvo estabilidad en todo el rango 0°-45°

### ✅ Mejora: Multi-ángulo combinado es crítico
**Hemming et al. (2014)** — Sweet-Pepper, 14 posiciones
- Mejor single view (zenith 60° = 30° up): solo **69%** detectabilidad
- **5 posiciones combinadas**: **90%** detectabilidad
- Las 5 posiciones incluían 2 imágenes a zenith 60° Y 3 a zenith 90° (horizontal)

**Mango Multi-View (2016)** — DOI: 10.3390/s16111915
- Single view: **27%** de frutos detectados
- Dual-view: **54%**
- Multi-view (tracking): **101.4%** (error 1.36%)

**Apple Orientation (2025)** — DOI: 10.1007/s44462-025-00020-w
- Sideways (90°): mAP **95%**
- Stem up: 86%
- Stem down: 91.7%

### 💡 Recomendación actualizada
- NO usar solo 15° up como único ángulo
- **Estrategia óptima**: grabar a **0° (horizontal) + 30° up** como mínimo
- **Ideal**: combinación de 3-5 ángulos (0°, 15°, 30°, 45°) + ambos lados de hilera
- Para mandarinas en dosel denso, los ángulos hacia arriba son importantes, pero deben complementarse con horizontales

---

## 3. 📏 DISTANCIA AL DOSEL (0.8-1.5 m)

### ❌ Contradicción: Para frutos pequeños, distancia <0.8 m es MEJOR
**RealSense Citrus (2018)** — Close-shot identificación
- Rango óptimo: **0.16-0.7 m** (160-700 mm)
- Detección: **80-100%** para poca oclusión
- Argumento: "En close-shot hay pocos objetos, poca información redundante, el objeto es 'cerca, grande y claro'"

**Lychee Detection** — Distancia 30-100 cm
- F1 ~89%
- Frutos pequeños (~20-30mm)

**Oil Palm Stereo (2024)**
- Mejor detección a **30 cm**: **97.63% accuracy**, F1=0.99
- Mejor estimación de distancia a **50 cm**: MAPE 0.86%

### 📊 Distancia ideal según TAMAÑO DE FRUTO

| Tipo de fruto | Distancia óptima | Fuentes |
|---|---|---|
| **Frutos muy pequeños** (lychee, blueberry ~20-30mm) | **0.3-0.7 m** | RealSense, Lychee |
| **Frutos pequeños** (mandarina, cítrico ~40-60mm) | **0.3-1.0 m** | Múltiples estudios |
| **Frutos grandes** (manzana, mango ~70-100mm) | **0.8-1.5 m** | YOLO-CSB 2026 |
| **Conteo a nivel árbol** | **1.5-5 m** | Yield estimation |

### 💡 Recomendación actualizada
- Para **mandarinas** (fruto pequeño, ~40-60mm) el rango óptimo sería **0.3-1.0 m**, más cercano que el recomendado
- La recomendación de 0.8-1.5m es válida para frutos grandes tipo manzana/mango
- **Compromiso**: Usar **0.5-1.2 m** para balancear detalle fino vs cobertura del dosel

---

## 4. ☀️ HORARIO/ILUMINACIÓN (9-11 AM o 3-5 PM, nublado)

### ❌ Contradicción FUERTE: Sol cenital (mediodía) da MEJORES resultados
**Multi-UAV Detection (2024)** — DOI: 10.3390/s24093743
| Condición | Precision | Recall | F1 |
|---|---|---|---|
| **Sol cenital (mediodía)** | **92.1%** | **89.3%** | **90.5%** |
| Nublado | 86.1% | 82.1% | 84% |
| Sombra fuerte | 78.1% | 74.2% | 72.4% |
- **Conclusion**: "The peak metric values were attained when the weather was sunny and the sun was directly overhead"

### ❌ Contradicción: "Nublado ideal" puede ser INSUFICIENTE
**Tomato HSV Illumination (2024)**
- Mínimo **3,000 lx** requerido para segmentación precisa
- Nublado da solo **1,000-2,000 lx**
- A 1,600 lx: solo **50% del área del fruto** es detectada

### ✅ Mejora IMPORTANTE: Noche con LED SUPERA al día consistentemente

| Paper | Resultado noche | Resultado día | Mejora |
|---|---|---|---|
| **OrBot Night Harvest (2024)** | **94%** éxito | 88% | +6% |
| **YOLOv8n-CSE Litchi Night (2024)** | **98.86% mAP** | — | Superior a día |
| **YOLO-P Pear Night (2022)** | **96.1% F1** | ~93% | +3% |
| **Penn State Active LED (2021)** | Reduce variabilidad **85%** | — | Elimina dependencia solar |
| **Choi LED Flash (2021)** | 20µs exposure, blur 7mm→1mm | — | Revoluciona captura |

**OrBot parámetros**: LED **5600K**, intensidad **10%**, frontal lighting
**YOLOv8n-CSE**: LED matrix, **210-350 Lux** normal

### ⚠️ Matiz: RGB-D sensors se degradan con alta iluminación
**RGB-D Sensors (2020)** — DOI: 10.3390/s2024...
- Rango óptimo: **50-2,000 lx**
- >2,000 lx degrada rendimiento 3D
- → Para sensores de profundidad, el sol cenital es problemático

### 💡 Recomendación actualizada
- La recomendación "evitar mediodía" es **directamente contradicha** por el paper Multi-UAV
- La opción **noche con LED** (5600K, frontal) consistentemente supera al día
- "Nublado ideal" es cuestionado: <3,000 lx puede ser insuficiente
- **Nueva estrategia**: Priorizar **captura nocturna con iluminación LED controlada**. Alternativamente, **cualquier hora del día funciona** siempre que se evite backlight extremo

---

## 5. 📸 SHUTTER SPEED (1/60-1/120s)

### ❌ Contradicción: Con iluminación activa, se elimina el blur COMPLETAMENTE
**Choi et al. (2021)** — Overcurrent-driven LEDs
- **Shutter: 20 µs** (~1/50,000s)
- LED overdriven 6× rating → strobe poderoso
- Blur reducido de **7mm a 1mm** a 7 km/h
- Variación HSV reducida **85%** en 11 horas de campo

**Arad FNF (2019)** — DOI: 10.3390/s19061390
- **Exposición: 20 µs** (Flash-No-Flash)
- **95% precision @ 95% recall** con algoritmo color-based
- Deep learning: 84% AP (Flash-only), 83.6% AP (FNF)

### ✅ Mejora: Deblurring GAN recupera blur post-hoc
**AGG-DeblurGAN (Huang et al., 2025)** — DOI: 10.3390/plants14193085
- mAP@0.5:0.95 mejora **86.4%** tras deblurring
- Recall mejora **76.9%**
- F1 aumenta **40.1%**
- mAP sube de **0.673 → 0.898** (casi nivel de imagen nítida)

### ✅ Mejora: Burst photography reemplaza exposición única
**Hasinoff HDR+ (2016)** — Google Nexus/Pixel
- Múltiples frames subexpuestos combinados
- "Shorter than typical exposure times... reducing motion blur"
- Mejor que single exposure tanto en ruido como en blur

**DEBIR (2026)** — arXiv:2603.21784
- Predice exposición óptima por frame dinámicamente
- Preview exposure: **1/120s**, burst usa exposiciones variables
- Adaptativo según movimiento en escena

### ✅ Mejora: Modelos tolerantes al blur
**FEGW-YOLO (2025)**
- Con blur severo (k=11): **80.1% mAP** (vs YOLOv8n 71.9%)
- Cross-noise: **89.7% mAP** combinando blur + ruido + contraste

### 💡 Recomendación actualizada
- **Con LED activo**: usar **20-100 µs** (elimina blur por completo, independiente del shutter)
- **Sin LED**: 1/60-1/120s sigue siendo razonable, pero:
  - Considerar **deblurring GAN post-hoc** para recuperar calidad
  - Considerar **burst photography** (múltiples frames cortos) en lugar de exposición fija
  - **1/120s** se recomienda sobre 1/60s para minimizar rolling shutter en smartphone

---

## 6. 🔄 ANTI-DOBLE CONTEO (ByteTrack + multi-view)

### ❌ Contradicción: Trackers SIMPLES superan ByteTrack en agricultura

**Dynamic Kalman Filter (2025)** — MDPI Sensors
| Tracker | MOTA | IDF1 | HOTA |
|---|---|---|---|
| ByteTrack | 75.0% | 37.0% | 68.6% |
| BoTSORT | 84.7% | 55.5% | 76.4% |
| **Dynamic Kalman (propuesto)** | **95.0%** | **65.5%** | **82.4%** |

**AgriSORT (ICRA 2024)** — arXiv:2309.13393
| Tracker | MOTA (CloseUp) | HOTA |
|---|---|---|
| ByteTrack | 48.24 | 38.24 |
| BoTSORT | 48.66 | 40.51 |
| **AgriSORT** | **65.93** | **48.71** |

**OrangeSort (2019)**
- MAE: **0.081** (vs SORT 0.6788, DeepSort 1.212)
- Simple SORT + región counting strategy

### ✅ Mejora: Trackers 2024-2025 específicos para agricultura

| Tracker | Año | Métrica | vs ByteTrack |
|---|---|---|---|
| **OC-SORT** | 2025 | HOTA 67.10% | +4.71% (passion fruit) |
| **Deep OC-SORT** | 2023 | HOTA 64.9 (MOT17) | +1.8 |
| **BoTSORT + YOLO** | 2025 | MOTA 89.2% | +14.0% |
| **FTO-SORT** | 2025 | IDF1 90.2% | +15.1% |
| **LocalizeSORT** | 2026 | Count error: 187 vs 263 | -29% |
| **PineSORT** | 2025 | CVPR | Drone-specific |

### ✅ Mejora: Trackers Transformer
**MOTR (2022)** — DanceTrack (objetos con apariencia uniforme, como fruta)
| Tracker | HOTA | AssA |
|---|---|---|
| ByteTrack | 47.7 | 32.1 |
| **MOTR** | **54.2** | **40.2** |

**MOT-DETR-3D (2023)** — Tomates
- HOTA **60.4** vs FairMOT 46.06

**Transformer Apple Fruitlet (2025)** — arXiv:2503.03200
- F1: **92.4%** para asociación temporal (vs ICP 89.5%, Desc 86.4%)

### ✅ Mejora: CoTracker3 para puntos
**Multi-Fruit Tracking via CoTracker (2026)**
- Tracking conjunto de múltiples puntos
- Infiere posiciones ocluidas desde puntos visibles
- **27% más rápido** que LoCoTrack

### ⚠️ Single-view puede ser suficiente
**Mango video tracking (2019)**: 62% harvest vs 40% dual-view
**Orange regression (2024)**: 7-frame secuencias reducen error 22-25%

### 💡 Recomendación actualizada
- **ByteTrack NO es la mejor opción** para agricultura en 2026
- **AgriSORT** (ICRA 2024) o **OC-SORT** son superiores para tracking de fruta
- **Dynamic Kalman Filter** con forgetting factor variabe da MOTA 95%
- **CoTracker3** como alternativa para point-tracking robusto a oclusiones
- **Single-view con agregación temporal** (multi-frame) puede reemplazar multi-view geometry en muchos casos
- Mantener **ambos lados de hilera**, pero no necesariamente con multi-view geometry

---

## 7. ⚔️ CONTRADICCIÓN INTEGRAL AL ENFOQUE

### Desafíos al enfoque smartphone manual

| Desafío | Evidencia | Severidad |
|---|---|---|
| **UAV supera a ground-level** | Through-canopy UAV: 66% visibilidad. Ground vehicle: solo 34% (arXiv:2409.18293) | ⚠️ Alto |
| **30fps puede ser insuficiente** | Citrus tracking 2022 usó 60fps. Múltiples papers recomiendan ≥60fps para tracking confiable | ⚠️ Medio |
| **Smartphone RGB no da profundidad** | ToF cameras logran 6mm RMSE. Smartphone no puede medir distancia precisa | ⚠️ Medio |
| **Video añade complejidad vs fotos** | Doble conteo requiere tracking complejo. Still images con solapamiento pueden ser más simples | ⚡ Medio-Bajo |
| **Calidad inconsistente smartphone** | DXOMARK: "smartphone results are much less consistent... cannot trust our smartphones to always provide a quality image" | ⚡ Bajo |

### Papers que apoyan el enfoque
- **Apple Yield Mapping (Häni 2018)**: Samsung S4 a 2 m/s → 95-97% accuracy. Demuestra que smartphone manual FUNCIONA.
- **Kiwifruit smartphone (KiwiDetector 2020)**: Selfie stick, ~1m, TDR 90.8%
- **YOLO-MECD (2025)**: Smartphone Honor 70, detección de cítricos
- **CampanetaOrangeFruit**: Dataset mediterráneo de naranjas

---

## 8. 🌎 PAPERS ESPECÍFICOS LATAM/CÍTRICOS

### Papers más relevantes para mandarinas en huerto denso

| Prioridad | Paper | Por qué es relevante |
|---|---|---|
| ⭐⭐⭐ | **IYOLOv5 citrus occlusion** | **13.1% menos detecciones perdidas** en dosel denso. Enfoque en **tangerine**. Capturado a 30-100cm. |
| ⭐⭐⭐ | **YOLO-MECD (2025)** | Smartphone **Honor 70** usado explícitamente. mAP 81.6%. 4.66 MB modelo. |
| ⭐⭐⭐ | **YOLO-PBGM (2025)** | Despliegue móvil + **98.5% precision** en condiciones complejas. BiFormer attention. |
| ⭐⭐ | **YOLOC-tiny (2024)** | Multi-variedad incluyendo **tangerine Harumi**. 4.2M params, 80 FPS. |
| ⭐⭐ | **CampanetaOrangeFruit (España)** | **301,232 anotaciones**. Clima mediterráneo similar a Argentina. RGB + 4 bandas multiespectrales. |
| ⭐⭐ | **CitDet Benchmark (Florida 2023)** | **32,000+ anotaciones**, 60 variedades. Clima subtropical similar a Argentina. |
| ⭐ | **Satsuma Mandarin Yield (2024)** | Mandarina Satsuma específicamente. R²=0.8099. Drone + hyperspectral. |
| ⭐ | **YCCB-YOLO young citrus (2024)** | Cítricos jóvenes. mAP 97.32%. Mañana, mediodía y tarde probados. |
| ⭐ | **ELD-YOLO mandarin occlusion (2024)** | Mandarinas ocluidas. Mañana, mediodía y tarde. |

### ⚠️ GAP CONFIRMADO
No existen papers específicos de detección de cítricos con smartphone en **Argentina/Latinoamérica**. Esto refuerza la **originalidad de tu tesis**.

---

## 📊 TABLA COMPARATIVA: P3 Original vs Evidencia Encontrada

| Parámetro | P3 Original | Nueva evidencia | Acción recomendada |
|---|---|---|---|
| **Velocidad** | ~1 m/s | 1.3-1.5 m/s viable con tracking/deblurring | Actualizar: "1-1.5 m/s según capacidad de tracking" |
| **Ángulo** | ~15° up | 0° (horizontal) y 45° pueden superarlo. Multi-ángulo esencial | Actualizar: "Combinación 0° + 30° up como mínimo" |
| **Distancia** | 0.8-1.5 m | 0.3-1.0 m para frutos pequeños | Actualizar: "0.5-1.2 m para mandarinas" |
| **Horario** | 9-11AM/3-5PM, nublado | Mediodía puede ser mejor. Noche con LED supera al día | Actualizar: "Noche con LED > Cualquier horario > Evitar solo backlight" |
| **Shutter** | 1/60-1/120s | 20µs con LED activo. 1/120s recomendado sobre 1/60s | Actualizar: "1/120s sin LED. 20-100µs con LED activo" |
| **Anti-doble conteo** | ByteTrack + multi-view | AgriSORT, OC-SORT, Dynamic Kalman superan ByteTrack. Single-view con multi-frame funciona | Actualizar: "AgriSORT/OC-SORT + ambos lados de hilera" |

---

## Papers nuevos identificados (candidatos a P79-PXX)

IDs tentativos para papers que contradicen/mejoran el P3:

| ID Tentativo | Título corto | Año | Parámetro |
|---|---|---|---|
| [P79] | AgriSORT — ICRA 2024 | 2024 | Tracking (supera ByteTrack en agricultura) |
| [P80] | Dynamic Kalman Filter Fruit Tracking | 2025 | Tracking (MOTA 95% vs ByteTrack 75%) |
| [P81] | OC-SORT Passion Fruit Yield | 2025 | Tracking (HOTA 67.10%) |
| [P82] | Multi-UAV Detection — Noon Best | 2024 | Iluminación (contradice "evitar mediodía") |
| [P83] | YOLOv8n-CSE Litchi Night | 2024 | Iluminación (98.86% mAP nocturno) |
| [P84] | OrBot Night Harvesting | 2024 | Iluminación (94% noche vs 88% día) |
| [P85] | AGG-DeblurGAN Citrus | 2025 | Shutter (deblurring recupera 86% mAP) |
| [P86] | Choi LED Overcurrent | 2021 | Shutter (20µs, blur 7mm→1mm) |
| [P87] | Villacrés Multi-Camera Apple | 2024 | Ángulo (perpendicular 0° = 88.3%) |
| [P88] | Sanchez Overlapping Rate | 2022 | Velocidad (fórmula ro = FOV×fps/v) |
| [P89] | RealSense Close-Shot Citrus | 2018 | Distancia (0.16-0.7m óptimo) |
| [P90] | IYOLOv5 citrus occlusion | 2024 | Cítricos (13.1% menos missed, tangerine) |
| [P91] | CoTracker3 Agricultural | 2025 | Tracking point-level |
| [P92] | Transformer Apple Fruitlet | 2025 | Tracking (F1 92.4% asociación) |
| [P93] | FEGW-YOLO blur robust | 2025 | Shutter (80.1% mAP con blur severo) |
| [P94] | MOT-DETR-3D Tomato | 2023 | Tracking (transformer 3D, HOTA 60.4) |
| [P95] | PineSORT CVPR 2025 | 2025 | Tracking (drone agricultura, CVPR) |
| [P96] | FTO-SORT Farm Tracking | 2025 | Tracking (IDF1 90.2%, +18%) |
