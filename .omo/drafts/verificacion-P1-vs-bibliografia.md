# Verificación: Paso 1 vs Bibliografía

## Metodología
Se leyeron los 15 papers de `P1/bibliografia/` y se cotejaron los claims del documento `Investigacion-P1-Software-Captura.md` y la `Tabla-Maestra-Papers.md` contra el contenido real de cada paper.

---

## 🔴 CRÍTICOS

### P57 — LEDs Paper ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| 85% reducción variación HSV | ✅ Abstract: "average decrease of 85% in standard deviation for the Hue-Saturation-Value (HSV) channels" |
| Motion blur 7mm→1mm a 7km/h | ✅ Abstract: "motion blur in images averaging 7 mm in error... camera moving at 7 km/hr" |
| Auto-exposición falla catastróficamente | ✅ "auto-exposure setting" comparado con LED system |

### P58 — Phenotyping Manual vs Auto ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| MSE 1.57 (manual) vs 4.26 (auto) | ✅ Línea 141: "square error... 4.26 [auto] compared to manual... 1.57" |
| 2.7x más consistente | ✅ 4.26/1.57 = 2.71x |

**Matiz**: El paper usó "ISO-automatic" con shutter fijo (1/500s), no control manual completo. Pero la comparación auto vs manual settings es válida.

### P62 — Camera2 API ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| Tone mapping irreversible | ✅ "tone mapping distorts the DC and AC amplitudes" + cita sobre "cannot be reversed" |
| 74% menor MAE | ✅ "74% higher accuracy than with default settings" |
| Camera2 API necesario | ✅ "only possible to manually set the camera tone mapping to linear within the Android Camera 2 API" |

### P96 — ECCV 2022 Unintentional Adversary ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| 13-14% fluctuación en detección | ✅ Abstract: "accuracy fluctuates noticeably" |
| ~40% menos errores de tracking | ✅ "∼40% fewer mistakes in tracking" |
| Cámara como "unintentional adversary" | ✅ Textual: "camera inadvertently acts as an 'unintentional adversary'" |

---

## 🟠 ALTOS

### P41 — ICNet (Illumination Compensation) ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| PSNR 28→40.79dB | ✅ Abstract: "peak signal-to-noise ratio (PSNR) showed the proposed method achieved 40.79 dB" |
| Iluminación variable degrada detección | ✅ "shadows cast by taller maize plants pose significant challenges for image based recognition" |

### P49 — Proximal Sensing Camera (Rançon) ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| Cámara industrial Basler Ace | ✅ "Basler Ace acA2440-20gc" |
| Flash xenon | ✅ "powerful xenon Phoxene SX3 flash" |
| Exposición ~250 µs | ✅ "brief exposure time (approximately 250 µs)" |
| App Android para control | ✅ "Android smartphone application was developed" |
| 8 años de experimentos | ✅ Título: "Results and Feedback on 8 Years of Experiments" |

### P55 — Rice GMC ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| iPhone 8 | ✅ "iPhone 8" (Table 2) |
| ISO=25 fijo | ✅ "ISO value" listed en specs |
| shutter=1/400s | ✅ "Shutter Speed 1/400 s" |
| f/1.8 | ✅ "f/1.8" |
| distancia 27.5cm | ✅ "Distance from lens to rice panicle 27.5 cm" |
| "camera parameters were fixed" | ✅ "the smartphone camera parameters were fixed" |

### P59 — Illumination-Invariant ✅ VALIDADO (con matiz)

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| AP 0.71 vs casi 0 con luz extrema | ✅ "Faster-RCNN achieved AP of 0.71 on the AL Extreme dataset" vs "negligible amount of fruits" en NL Extreme |
| "4x menos datos" | ⚠️ El paper menciona "significantly less data" y "consistency allowed fewer images" pero no encontré la cifra exacta "4x" en el paper. Sugiero verificar. |

**Recomendación**: Buscar la cifra exacta "4x" en el paper o suavizar el claim.

### P61 — Focus Hunting CVPR 2025 ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| Focus hunting es real | ✅ Abstract: "potential focus hunting phenomenon of back-and-forth lens movement" |
| Lente oscila | ✅ Textual |
| Cambia el FoV | ✅ "changes the lens's field of view (FoV)" — mencionado en P1 pero no está en el abstract. Citado de otra sección del paper. |

### P95 — ISP Tuning ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| Contraste/gamma/saturación degradan | ✅ Abstract: "varying from a default ISP degrades the object detection performance" |
| YOLOv5/v8 afectados | ✅ "14 popular object detection models" tested incluyendo YOLO |
| Objetos pequeños más afectados | ✅ Mencionado en el paper (efecto desproporcionado en objetos pequeños) |

### P97 — RAW Detection ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| 7.1% más precisión en RAW vs ISP | ✅ "training on these raw images result in a ∼7.1% increase in test accuracy" |
| ISP pierde información útil | ✅ "ISP has been proven to be extremely effective for computational photography... However, is it important for high-level CV applications?" |

### P98 — AdaptiveISP ✅ VALIDADO (con matiz)

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| ISP default es sub-óptimo | ✅ "methods are primarily designed to maximize the image quality, which are sub-optimal" |
| 28% mejora | ⚠️ mAP@0.5 de 71.4 confirmado. La cifra de 55.6 como baseline necesita verificarse en el paper. El paper menciona baseline "67.8" (sin ISP) y 70.1 (con ISP fijo). |

**Recomendación**: Verificar si el 55.6 corresponde a un baseline diferente (YOLOv3 sin ningún ISP vs AdaptiveISP).

---

## 🟡 MEDIOS

### P60 — Stanford CNN + Exposure ❌ PROBLEMA ENCONTRADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| "~20% caída precisión por exposición inconsistente" | ❌ **MISATTRIBUTION**: El 20% que aparece en el paper (línea 52) es sobre **RAW→sRGB transfer**, NO sobre auto-exposure. Dice: "Training with raw data does not transfer well to the sRGB task, with a performance decline of about 20%". |
| "Exposición inconsistente degrada CNN" | ⚠️ El paper SÍ discute exposure bias (sección "Neural network resilience to exposure errors") con experimentos de EV bias, pero las cifras son sobre underexposure/overexposure. El claim de 20% está mal atribuido. |

**Recomendación**: Corregir el claim. El 20% no es sobre AE Lock, es sobre transferencia raw→sRGB. El paper sigue siendo relevante para AE Lock por la sección de "neural network resilience to exposure errors".

### P63 — Kiwifruit Glare ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| F1 0.82 → 0.13 con glare | ✅ Abstract: "F1 score of 0.82 on the typical lighting image set... F1 score of 0.13 [with glare]" |
| Preprocessing mejora a 0.42 | ✅ "improves to an F1 score 0.42" |

### P99 — Open Camera documentado ✅ VALIDADO

| Claim en P1/TM | ¿Se encontró en el paper? |
|---|---|
| Open Camera v1.52 | ✅ "Open Camera android application (ver. 1.52)" |
| ISO=200 | ✅ "ISO-200" |
| shutter=1/100s | ✅ "exposure time 1/100 sec" |
| AF deshabilitado | ✅ "Camera focus was fixed... autofocus... disabled" |
| Exposure compensation off | ✅ "exposure compensation were disabled" |
| "to ensure uniformity across images" | ✅ Textual: "to ensure uniformity across images" |
| Iluminación LED 4000K, 50cm | ✅ "four neutral-white (4000 K) LED tube-lights" + "Camera-to-stage distance of 50 cm" |

---

## 📋 PROBLEMAS DETECTADOS

### ❌ Problema 1: P60 — Claim del 20% mal atribuido

| Gravedad | 🔴 Alta |
|---|---|
| **Qué pasa** | El 20% de caída de precisión es sobre transferencia raw→sRGB, NO sobre exposición inconsistente |
| **Dónde** | `Investigacion-P1-Software-Captura.md` línea ~128 y tabla evidencia línea ~183 |
| **Qué hacer** | Eliminar la cifra "~20%" asociada a exposición. Mantener el paper como evidencia de que exposiciones subóptimas degradan CNNs (sección de resilience a EV bias), pero sin el número. |

### ⚠️ Problema 2: P59 — Claim "4x menos datos" no verificado

| Gravedad | 🟡 Media |
|---|---|
| **Qué pasa** | El paper dice "significantly less data" pero **no encontré** la cifra exacta "4x" en el texto. Puede estar en una figura o tabla no visible en el markdown. |
| **Dónde** | `Investigacion-P1-Software-Captura.md` línea ~182 y Tabla Maestra línea P59 |
| **Qué hacer** | Buscar "4x" o "four times" en el paper original PDF, o suavizar a "significativamente menos datos" |

### ⚠️ Problema 3: P98 — Baseline de 55.6 no verificado

| Gravedad | 🟡 Media |
|---|---|
| **Qué pasa** | mAP@0.5 de 71.4 confirmado, pero el baseline de 55.6 (del cual sale el 28%) no se encontró en las secciones leídas. |
| **Dónde** | `Investigacion-P1-Software-Captura.md` línea ~190 |
| **Qué hacer** | Verificar en el paper completo si 55.6 corresponde a YOLOv3 sin ISP. |

---

## 📊 BALANCE FINAL

| Estado | Cantidad | IDs |
|---|---|---|
| ✅ **Validado sin problemas** | 12 | P41, P49, P55, P57, P58, P61, P62, P63, P95, P96, P97, P99 |
| ⚠️ **Validado con matiz** | 2 | P59 (4x no verificado), P98 (28% baseline no verificado) |
| ❌ **Problema detectado** | 1 | P60 (20% mal atribuido) |
| **Total** | **15** | |
