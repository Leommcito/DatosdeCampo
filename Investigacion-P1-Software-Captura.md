# Investigación — Pregunta 1: Software de Captura y Bloqueo de Sensores

## Fuentes consultadas

- **Elicit**: 16 papers (CSV: `Elicit - Agricultural Outdoor CV Capture Toolchain Papers.csv`)
- **Semantic Scholar**: Búsqueda web complementaria (este documento)
- **Búsqueda web directa**: Documentación técnica, reviews, GitHub

---

## Lo que dice la literatura (papers)

### Papers de Elicit que documentan configuración de captura

| Paper | Dispositivo | Configuración documentada | Lo que reporta |
|---|---|---|---|
| Janowski et al. (2021) — Manzanas | Smartphone + GNSS | Solo menciona "smartphones with required image-acquisition accuracy" | No da settings |
| Vélez et al. (2024) — EscaYard Viñedos | iPhone X, Xiaomi Poco X3 Pro | "High-resolution images of individual plants; geotagged data" | Sin detalles de app ni configuración |
| Zhao et al. (2023) — Fenotipado manzanas | Multi-camera smartphone | "paired smartphone cameras; virtual focal method" | Método de calibración, no app |
| Jaramillo et al. (2025) — Viñedos | Smartphone | "Videos of the ground under vine rows on a sunny day" | Captura simple, sin settings |
| Zhou et al. (2020) — Kiwi | HUAWEI P20 + KiwiDetector | "100 field images at 3968×2976 pixels; 8-bit quantization" | App propia (KiwiDetector), no comercial |

**Conclusión de Elicit:** Ningún paper agrícola documenta apps de captura comerciales (Open Camera, Filmic Pro, etc.) ni justifica la elección de configuración.

### Papers de Semantic Scholar que complementan

#### Paper 1: Medición de humedad en arroz con smartphone (Sensors, 2021) — [P55]

- **Dispositivo:** iPhone 8
- **Configuración:** ISO=25 fijo, shutter=1/400s, f/1.8, distancia=27.5cm
- **Formato:** JPEG, 4032×3024px, aspect ratio 4:3
- **Condiciones:** Sin luz solar directa. Usaron tabla de calibración de color (Spyder Checkr 24)
- **Dato clave:** "To minimize lighting-related factors, the smartphone camera parameters were fixed" — justificación explícita de por qué fijar parámetros
- **Relevancia:** Alta. Paper que demuestra la necesidad de fijar parámetros en campo.
- **ID en Tabla Maestra:** [P55]
- **Enlace:** PDF en resultados Semantic Scholar (rice GMC measurement)

#### Paper 2: Monitoreo de café con smartphone + sensores inerciales (Sensors, 2020)

- **Dispositivo:** Samsung Galaxy S5 SM-G900M
- **Configuración:** Full-HD 1920×1080, 30fps, flash off, WB e ISO en AUTO, EV=0
- **Holder:** Sostén con botones para enfoque + botón start/stop. Ángulo 11.3°.
- **Distancia rama:** 80-150mm (8-15 cm)
- **Dato clave:** Usaron sensores inerciales para detectar movimiento y medir blur. Desarrollaron app Android propia.
- **Relevancia:** Alta. Paper que integra IMU + cámara para control de calidad de captura.
- **Limitación:** Usaron modo automático (no fijaron parámetros) — justo lo que tu tesis busca mejorar.

#### Paper 3: Detección de manzanas con YOLO en smartphone (2024)

- **Dispositivo:** Redmi Note 7
- **Distancia:** 0.3-1.5m
- **Condiciones de luz:** Directa, lateral, difusa, contraluz, baja luz — 5 condiciones probadas
- **App:** Android app con YOLOv8n desplegada localmente
- **Resolución:** Imágenes comprimidas a 640×640px
- **Relevancia:** Alta. Distancia 0.3-1.5m es el rango que usaron para detección de frutos.

#### Paper 4: Dataset de cacao con 5 smartphones (Data, 2023)

- **Dispositivos:** Samsung Galaxy A01, Samsung Galaxy Note 10, iPhone SE 2020, Motorola G9 plus, LG G5
- **Horario:** 8:00-16:00
- **Trayectoria:** Zigzag entre árboles
- **Aspect ratio:** 1:1 (cuadrado), resize a 3000×3000px
- **Ángulos:** 1-4 fotos por fruto desde diferentes ángulos
- **Relevancia:** Alta. Muestra trayectoria zigzag y uso de múltiples dispositivos.

#### Paper 5: DHN-YOLO para fresas (2025)

- **Dispositivo:** Smartphone cámara trasera
- **Distancia:** 50-80cm de la superficie
- **Ángulo:** ~45° respecto a la superficie (simulando robot)
- **Relevancia:** Media. Ángulo 45° y distancia cercana.

#### Paper 6: Stabilization self-calibration esférica con giroscopio (Information, 2021) — [P56]

- **Método:** Estabilización basada en giroscopio + auto-calibración de radio esférico
- **Resultados:** Mejora PSNR, SSIM, cropping ratio, distortion score, stability score
- **Comparación:** Supera a métodos con matriz de parámetros intrínsecos
- **Dato clave:** Método basado en giroscopio no necesita calibración de cámara
- **Relevancia:** Alta. Respalda el uso de giroscopio para estabilización en vez de métodos ópticos.
- **ID en Tabla Maestra:** [P56]

---

## Nueva evidencia encontrada — Búsqueda en Semantic Scholar (2025)

Resultados de búsqueda específica para justificar el uso de controles manuales vs automático en captura agrícola.

### Paper 7: LEDs + exposición fija (Computers and Electronics in Agriculture, 2021) — [P57] 🔴 Crítico

| Hallazgo | Valor |
|---|---|
| **Reducción variación HSV** | **85% menos** con LED fijo vs auto-exposición |
| **Error motion blur** | 7mm → **1mm** a 7km/h con flash sincronizado |
| **Fallo de auto-exposición** | Catastrófico cuando el sol está frontal a la cámara |
| **Conclusión** | Parámetros fijos + iluminación controlada eliminan casi toda la variabilidad |

**Relevancia:** Respalda directamente fijar ISO y shutter speed en la captura.

---

### Paper 8: Phenotyping — Manual vs Auto (Plant Methods, 2018) — [P58] 🔴 Crítico

| Hallazgo | Valor |
|---|---|
| **Error cuadrático medio** | **1.57 (manual) vs 4.26 (auto)** |
| **Conclusión** | Exposición manual es **2.7x más consistente** que automática |

**Relevancia:** Comparación directa manual vs auto en condiciones de campo. Respalda AE Lock.

---

### Paper 9: Illumination-Invariant Camera System (arXiv, 2021) — [P59] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Reducción datos necesarios** | Redes entrenadas con imágenes consistentes requieren **4x menos datos** |
| **AP en luz extrema** | 0.71 (iluminación controlada) vs **casi 0** (luz natural) |
| **Conclusión** | Consistencia en captura reduce drásticamente la cantidad de datos necesarios |

**Relevancia:** Fijar parámetros = menos imágenes necesarias para entrenar.

---

### Paper 10: Stanford — CNN + Exposure Bias (Google Research, 2018) — [P60] 🟡 Media

| Hallazgo | Valor |
|---|---|
| **Impacto en CNN** | Redes entrenadas con exposición fija no generalizan bien a diferentes exposiciones. Asimetría: sub-exposición se maneja mejor que sobre-exposición. |
| **Conclusión** | Exposición inconsistente degrada la precisión de detección |

⚠️ **Nota**: La cifra exacta de "~20% caída de precisión" no pudo ser verificada en el paper original encontrado ("Optimizing Image Acquisition Systems for Autonomous Driving", Blasinski et al., Stanford, 2018). El paper SÍ demuestra que exposiciones subóptimas degradan CNNs, pero el valor cuantitativo exacto requiere verificación. Se ha reducido la importancia a 🟡 Media.

**Relevancia:** Evidencia de que AE Lock mejora la detección, aunque el valor cuantitativo exacto requiere verificación.

---

### Paper 11: Focus Hunting (CVPR, 2025) — [P61] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Focus hunting** | El lente oscila repetitivamente creando inestabilidad en el video |
| **Efectos** | Reduce nitidez, cambia el campo de visión (FoV) |
| **Reducción** | 18% menos FH con método DRL propuesto |

**Relevancia:** Documenta que el focus hunting es un problema real. Respalda AF Lock.

---

### Paper 12: Camera2 API para investigación (Frontiers in Digital Health, 2023) — [P62] 🔴 Crítico

| Hallazgo | Valor |
|---|---|
| **Tone mapping automático** | Aplica transformaciones **no lineales irreversibles**. "Cannot be reversed in post processing" |
| **Camera2 API** | Permite configurar tone mapping lineal (CONTRAST_CURVE con puntos de control). **74% menor MAE** vs default automático |
| **Conclusión** | Camera2 API es necesaria para investigación científica con smartphone. iOS no ofrece control equivalente de tone mapping |

✅ **Corregido**: La fuente correcta es *Frontiers in Digital Health* (2023, PMC10705321), no Nature/PMC. DOI: 10.3389/fdgth.2023.1301019. Importancia elevada a 🔴 Crítico por la evidencia cuantitativa del 74% de mejora.

**Relevancia:** Valida que Camera2 API es el estándar para captura científica con control de tone mapping lineal. Respalda usar Open Camera con Camera2 API.

---

### Paper 13: Kiwifruit Detection + Glare (arXiv, 2020) — [P63] 🟡 Media

| Hallazgo | Valor |
|---|---|
| **F1-score sin glare** | **0.82** en imágenes normales |
| **F1-score con glare** | **0.13** en imágenes con luz no controlada |
| **Conclusión** | Luz no controlada destruye la detección |

**Relevancia:** Demuestra que condiciones de luz adversas degradan severamente la detección.

---

### Tabla de evidencia cuantitativa — Paso 1

| Problema | Evidencia | Fuente | ID |
|---|---|---|---|
| Auto-exposure causa inconsistencia | 85% más variación HSV | LEDs paper (2021) | [P57] |
| Auto-exposure falla en alto rango dinámico | Primer plano oscuro al exponer para cielo | LEDs paper (2021) | [P57] |
| Manual supera a auto | MSE 1.57 vs 4.26 | Phenotyping (2018) | [P58] |
| Parámetros fijos reducen datos necesarios | 4x menos datos de entrenamiento | Illumination-Invariant (2021) | [P59] |
| Exposición inconsistente degrada CNN | Redes no generalizan con exposición variable | Stanford (2018) | [P60] ⚠️ |
| Focus hunting degrada calidad | Lente oscila, FoV cambia | CVPR (2025) | [P61] |
| Camera2 API necesario para control científico | Tone mapping irreversible. 74% menor MAE con lineal | Frontiers Digit. Health (2023) | [P62] |
| Luz no controlada destruye detección | F1 0.82 → 0.13 con glare | Kiwifruit (2020) | [P63] |
| ISP automático degrada detección YOLO | Contraste/gamma/saturación causan falsos negativos | ISP Tuning (2023) | [P95] |
| Parámetros auto causan fluctuación | 13-14% fluctuación en detección en escenas estáticas | ECCV (2022) | [P96] |
| ISP pipeline pierde información útil | 7.1% más precisión entrenando en RAW vs ISP-processed | ISP-less CV (2022) | [P97] |
| ISP default es sub-óptimo para detección | 28% mejora con AdaptiveISP vs ISP default | NeurIPS (2024) | [P98] |

---

## Tabla resumen cruzada Elicit + Semantic Scholar

| Aspecto | Elicit | Semantic Scholar | Gap |
|---|---|---|---|
| Apps de cámara nombradas | ❌ Ninguna | ⚠️ 1 paper (PMC12057810) nombra **Open Camera v1.52** | **Solo 1 paper en toda la literatura — sigue siendo extremadamente raro** |
| Parámetros de cámara (ISO, shutter, etc.) | ❌ No reportados | ⚠️ 1 paper (arroz) sí los reporta | Solo 1 paper en toda la literatura |
| Justificación de por qué fijar parámetros | ❌ No existe | ⚠️ 1 paper dice "to minimize lighting factors" | Justificación débil |
| Distancia al objetivo | ❌ No reportada | ✅ Varios papers: 0.3-1.5m, 8-15cm, 27.5cm | Hay datos pero no comparativos |
| Holder/soporte físico | ❌ No reportado | ✅ 1 paper (café) con holder + botones | Solo 1 paper |
| Integración IMU + cámara | ❌ No reportada | ✅ 1 paper (café) con IMU para blur detection | Solo 1 paper |
| Dispositivos específicos | ⚠️ Algunos (iPhone X, Xiaomi, Huawei) | ✅ Varios (iPhone 8, Galaxy S5, Redmi Note 7, etc.) | Complementario |
| Open Camera / Filmic Pro / MCPro24fps | ❌ No existen en papers agrícolas | ⚠️ 1 paper (PMC12057810) nombra **Open Camera v1.52** en fenotipado de hojas | **Solo 1 paper documenta Open Camera. Ningún paper documenta MCPro24fps o Filmic Pro en agricultura** |

---

## Lo que la búsqueda web (no papers) aportó

Además de papers, se investigó documentación técnica:

### Open Camera — justificación técnica

| Característica | Documentado en | Relevancia |
|---|---|---|
| AF Lock, AE Lock, WB Lock | [Help oficial](https://opencamera.sourceforge.io/help.html) | Bloqueo de los 3 parámetros críticos |
| ISO manual + Shutter manual | Documentación oficial | Control total de exposición |
| Bitrate configurable | Documentación oficial | Calidad constante en todo el video |
| Camera2 API requerido | Documentación oficial | No todos los dispositivos lo soportan |
| Gratis + open-source | SourceForge | Reproducible, sin barrera económica |
| Sin perfiles Log | Comparativas | No necesario para detección de objetos |
| Sin control directo de gimbal | Comparativas vs Filmic Pro | Limitación menor |

### Comparativa apps profesionales (vía reviews técnicas)

| App | Precio | AF Lock | AE Lock | WB Lock | ISO man. | Shutter man. | Log | Gimbal | Bitrate |
|---|---|---|---|---|---|---|---|---|---|
| **Open Camera** | **Gratis** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Filmic Pro | $5/semana | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ V-Log | ✅ DJI/Zhiyun | 100 Mbps |
| MCPro24fps | ~$20 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Múltiples | ❌ | Hasta 500 Mbps |
| Blackmagic Cam | Gratis | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | Alto |

**Decisión:** Open Camera es la mejor opción para tu tesis por:
1. **Costo $0** — reproduce cualquier investigador
2. **Control manual completo** via Camera2 API
3. **Open-source** — puedes citar el código
4. **Sin subscription** — a diferencia de Filmic Pro (subió a ~$5/semana en 2022)

### Gyroflow — justificación técnica (GitHub, 8.9k stars)

- Estabilización usando datos IMU reales (no warp la imagen como EIS)
- Corrección de rolling shutter
- Corrección de distorsión de lente
- Compatible con Sensor Logger como fuente IMU
- Plugin para DaVinci Resolve y Adobe Premiere
- **Open-source (GPLv3)**

---

## Gap confirmado para la tesis

> **Solo 1 paper en toda la literatura (PMC12057810, fenotipado de hojas) documenta Open Camera v1.52 con configuración detallada. Ningún paper documenta el flujo completo (app + configuración + IMU + pipeline) para detección de frutos en video.**

Papers actuales:
- Usan smartphones pero **no dicen qué app**
- Configuran la cámara pero **no justifican los valores**
- No comparan **auto vs manual** con métricas de detección
- No documentan **app de logging IMU** ni método de sincronización

### Nueva evidencia encontrada (2025)

Ahora contamos con **7 papers nuevos** que respaldan el Paso 1:

| ID | Evidencia | Lo que demuestra |
|---|---|---|
| [P57] | LEDs paper | 85% menos variación con exposición fija |
| [P58] | Phenotyping | Manual 2.7x más consistente que auto |
| [P59] | Illumination-Invariant | 4x menos datos con imágenes consistentes |
| [P60] | Stanford CNN | Exposición variable degrada CNNs (⚠️ claim ~20% no verificado) |
| [P61] | CVPR 2025 | Focus hunting es un problema real |
| [P62] | Camera2 API (Frontiers Digital Health) | Tone mapping irreversible. 74% menor MAE con lineal |
| [P63] | Kiwifruit glare | F1 cae de 0.82 a 0.13 con luz no controlada |

### Nueva evidencia adicional encontrada (2023-2026)

Una investigación bibliográfica complementaria (Junio 2026) encontró evidencia adicional que **FORTALECE** la posición del Paso 1:

| ID | Evidencia | Lo que demuestra |
|---|---|---|
| [P95] | ISP Tuning (MDPI J. Imaging, 2023) | Contraste, gamma y saturación del ISP automático degradan significativamente YOLOv5/v8, Faster R-CNN y RT-DETR. Los objetos pequeños son los más afectados. |
| [P96] | ECCV 2022 - "Unintentional Adversary" | La cámara con parámetros automáticos causa 13-14% fluctuación en detección en escenas estáticas. 5.4x falsos track-IDs. |
| [P97] | RAW > ISP-processed (ISP-less CV, 2022) | 7.1% más precisión entrenando en dominio RAW vs RGB procesado por ISP. El ISP pierde información útil para detección. |
| [P98] | AdaptiveISP (NeurIPS 2024) | El pipeline ISP por defecto es sub-óptimo para detección. AdaptiveISP logra 28% mejor mAP optimizando el ISP para la tarea. |

**Gap que persiste:** Solo 1 paper en toda la literatura (PMC12057810, fenotipado de hojas) documenta Open Camera con configuración detallada. Ningún paper documenta el **flujo completo** app + configuración + IMU + procesamiento para detección de frutos en video.

**Tu contribución original:** Documentar y justificar todo el pipeline de captura (app + configuración + IMU + procesamiento) con métricas cuantitativas de impacto en YOLO. El experimento A/B (Protocolo vs Cámara Nativa) medirá si el control de captura sigue siendo relevante frente a detectores modernos robustos a iluminación.

---

## 🆕 Actualización post-investigación (Junio 2026)

Tras una investigación bibliográfica adicional con 6 búsquedas paralelas en Semantic Scholar, web y GitHub, se encontró nueva evidencia que **FORTALECE** la posición del Paso 1, así como correcciones a referencias citadas.

### Nueva evidencia que fortalece el Paso 1

#### 1. El pipeline ISP automático degrada la detección YOLO [P95]

El paper "Impact of ISP Tuning on Object Detection" (MDPI J. Imaging, 2023) demuestra que:
- Contraste, gamma y saturación (componentes del ISP automático) causan **degradación significativa** en YOLOv5/v8, Faster R-CNN y RT-DETR
- La variación de ISP afecta **desproporcionadamente a objetos pequeños** — crítico para mandarinas en huerto denso
- La mayoría de errores introducidos son **falsos negativos** (objetos no detectados)

**Implicación**: El procesamiento automático que hace la cámara (tone mapping, gamma, saturación) no solo es "no reversible" [P62], sino que **activamente perjudica** la detección.

#### 2. La cámara actúa como "unintentional adversary" de la detección [P96]

El paper de ECCV 2022 "Why is the video analytics accuracy fluctuating" demuestra que:
- **13-14% de fluctuación** en conteo de detecciones sobre escenas **estáticas** (sin movimiento)
- La causa raíz son los cambios automáticos de parámetros de cámara
- Transfer-learning redujo errores de tracking en **~40%**
- Modelo original creó **157 track-IDs** para solo 29 objetos reales (5.4x falsos)

**Implicación**: El simple hecho de usar modo automático introduce **ruido en la medición** que no existe en modo manual. Esto justifica directamente el bloqueo de AE/AF/WB.

#### 3. La detección en RAW supera a RGB procesado por ISP [P97]

Múltiples papers (2022-2026) muestran que entrenar modelos en dominio RAW:
- **7.1% más precisión** que con imágenes procesadas por ISP (ISP-less CV, 2022)
- "Freedom from the nonlinear distortions introduced by the ISP pipeline" (RAWild, 2026)
- Aprendizaje de gamma correction en RAW supera baseline RGB

**Implicación**: El ISP automático **pierde información** útil para detección. Al usar Camera2 API con tone mapping lineal [P62], nos acercamos más al dominio RAW.

#### 4. El ISP por defecto NO es óptimo para detección [P98]

AdaptiveISP (NeurIPS 2024) demuestra que el pipeline ISP puede optimizarse específicamente para detección, logrando **28% mejor mAP** (71.4 vs 55.6). Solo algunas etapas ISP son útiles — el pipeline default es sub-óptimo.

**Implicación**: Incluso si el ISP automático produce imágenes "bonitas" para el ojo humano, no están optimizadas para YOLO. El control manual via Camera2 API permite evitar este problema.

### Correcciones a referencias citadas

#### [P60] — Stanford CNN + Exposure Bias

⚠️ **Nota**: La cifra exacta de "~20% caída de precisión" no pudo ser verificada en el paper original encontrado ("Optimizing Image Acquisition Systems for Autonomous Driving", Blasinski et al., Stanford, 2018). El paper SÍ demuestra que exposiciones subóptimas degradan significativamente CNNs (asimetría sub/sobre-exposición, falta de generalización), pero el valor exacto requiere verificación. La importancia de P60 se ha reducido a 🟡 Media hasta verificar el claim exacto.

#### [P62] — Camera2 API para investigación

✅ **Corregido**: El paper citado como "Nature/PMC" es en realidad:
- **Título**: "A calibration method for smartphone camera photoplethysmography"
- **Publicación**: *Frontiers in Digital Health* (2023)
- **PMID**: PMC10705321
- **DOI**: 10.3389/fdgth.2023.1301019
- **Hallazgo clave**: Tone mapping lineal vía Camera2 API logra **74% menor MAE** vs default automático. "The adaptive control causes nonlinear effects that cannot be reversed in post processing."

La importancia de P62 se ha elevado a 🔴 **Crítico** por la solidez del hallazgo (74% de mejora cuantificada).

### Open Camera documentada en investigación previa [P99]

Se encontró el paper PMC12057810 (2024) que **documenta explícitamente Open Camera v1.52** con configuración detallada:
- ISO=200 fijo, shutter=1/100s
- AF deshabilitado, compensación de exposición deshabilitada
- Razón explícita: "to ensure uniformity across images"

Esto **matiza** el claim de que "ningún paper documenta apps de cámara". La afirmación correcta es:

> "Es **extremadamente raro** que papers agrícolas documenten qué app de cámara usaron. Solo se encontró **un paper** (en fenotipado de hojas, no en detección de frutos) que nombra Open Camera con configuración detallada. **Ningún paper** documenta el flujo completo (app + configuración + IMU + pipeline) para detección de frutos en video."

### Discusión: Nuevo paradigma de detección robusta (2024-2026)

Es importante reconocer que entre 2024-2026 han surgido detectores (Orchard-YOLO 2026, YOLO-PBGM 2025) que logran **>94% mAP** incluso con variaciones de iluminación de ±50%, mediante técnicas como:
- Data augmentation con exposición randomizada
- Mecanismos de atención (GAM, CBAM)
- Aprendizaje de features illumination-invariant (YOLA, NeurIPS 2024)

**Sin embargo, esto NO invalida el Paso 1** por las siguientes razones:

1. **Ambos paradigmas son complementarios**: Controlar la captura + entrenar modelos robustos debería dar el mejor resultado
2. **No hay experimento que compare**: Precisamente, el experimento A/B de esta tesis (Protocolo vs Cámara Nativa) es lo que falta en la literatura
3. **Escenario extremo**: El huerto denso de mandarinas (frutos pequeños, alta oclusión, follaje denso) es más desafiante que los escenarios donde se probaron esos modelos
4. **El ISP sigue siendo un problema**: Aunque el detector sea robusto a iluminación, el tone mapping, gamma y saturación del ISP automático siguen degradando la información [P95][P96][P97]

Por lo tanto, el Paso 1 se mantiene como **válido y necesario**, con la salvedad de que su impacto debe evaluarse en el contexto del experimento A/B planificado (Protocolo vs Cámara Nativa con métricas YOLO).**
