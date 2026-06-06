# Investigación — Pregunta 2: Registro de Telemetría IMU

## Fuentes consultadas

- **Elicit**: 12 papers (CSV: `Elicit - IMU-assisted video processing papers.csv`)
- **Búsqueda web complementaria**: Documentación de Gyroflow, papers de gait analysis, reviews técnicas

---

## Resultados de Elicit

### Papers sobre estabilización con IMU

| Paper | Método | Resultado cuantitativo | Dispositivo |
|---|---|---|---|
| Han et al. (sin título) [P11] | Fusión giroscopio + visión | **32% mejor estabilización**, 32.6ms latencia | Smartphones, smart glasses |
| Li et al. (2023) — Deep Online VS [P12] | IMU sensor guidance | **25 fps en 1080p** tiempo real | Dispositivos móviles |
| Li et al. (2025) — Multi-Modal VS [P13] | Gyroscope + clustering + depth | **47.8% SSIM mejora**, 37% más rápido | Dispositivos móviles |
| Jang et al. (2024) — Full-frame VS [P14] | IMU + optical flow + neural rendering | **18% Stability score**, 3% Distortion | Dispositivos móviles |
| Auysakul et al. (2018) — Hybrid Motion [P15] | KLT + IMU switching | Tiempo real, multi-threaded | Cámaras handheld |

### Papers sobre rolling shutter con IMU

| Paper | Método | Resultado | Dispositivo |
|---|---|---|---|
| Mo et al. (2020) — IMU RS Correction [P17] | IMU pose refinement | Mejora downstream DSO | Single-view camera |
| Zhang & Zhang (2023) — Point Feature RS [P18] | High-frequency IMU | **Supera SOTA en precisión y costo** | Android phone |
| Wu et al. (2021) — Simultaneous VS+RS [P19] | Joint modeling | Superior a SOTA | CMOS / handheld |

### Papers sobre motion blur con giroscopio

| Paper | Método | Resultado | Nota |
|---|---|---|---|
| Ji et al. (2021) — Gyro-guided deblurring [P20] | Gyroscope guidance | Mejora visual + feature detectors | Sin métrica YOLO |
| Mustaniemi et al. (2018) — Inertial-aided [P21] | Gyroscope + CNN | Tiempo real, mejora visual | Pionero |
| Arslan et al. (2024) — Mesh-grid deblurring [P22] | IMU-informed mesh | **5% PSNR gain**, 19% menos cómputo | Dato más limpio |

### Lo que Elicit NO encontró (gaps)

- ❌ **Ningún paper agrícola** conecta IMU preprocessing → YOLO mAP
- ❌ **Ningún paper documenta** sampling rate IMU específico para caminata en huerto
- ❌ **Ningún paper agrícola** usa Sensor Logger, Gyroflow, OpenCamera Sensors

---

## Resultados de búsqueda web complementaria

### Sampling rate IMU — RESUELTO

**Paper clave:** Fan et al. (2025) — "Influence of Sampling Rate on Wearable IMU Orientation Estimation Accuracy for Human Movement Analysis" — Sensors, MDPI.

| Actividad | Frecuencia suficiente | Observación |
|---|---|---|
| Walking (1.2 m/s) | **100 Hz** | Frecuencias >100Hz no mejoran precisión |
| Running (2.2 m/s) | 200 Hz | — |
| Movimientos cíclicos rápidos (3 Hz) | 400 Hz | — |
| **Acelerómetro >100 Hz** | ❌ **Degrada precisión** | Introduce error por aceleraciones distorsionadas |

**Conclusión:** 100 Hz es suficiente para caminata en huerto (~0.5-1.2 m/s).

### Gait analysis con smartphone IMU — VALIDADO

Múltiples papers confirman que el IMU del smartphone a **100 Hz** es válido para análisis de marcha con ICC > 0.8 contra gold-standard (JMIR 2024, Sensors 2021, Nature SciData 2022).

### Gyroflow — documentación técnica

| Aspecto | Detalle | Fuente |
|---|---|---|
| **Soporte Sensor Logger** | ✅ Compatible como fuente IMU externa | [docs.gyroflow.xyz](https://docs.gyroflow.xyz) |
| **Sync requerida** | Sí, manual para fuentes externas. ±200ms típico. | docs.gyroflow.xyz |
| **OpenCamera Sensors** | Sincronización nativa (mismo clock) | GitHub prime-slam/opencamera-sensors |
| **OIS** | ⚠️ Debe estar desactivado — **ahora respaldado por papers** | docs.gyroflow.xyz, [P64], [P65] |
| **Plugin DaVinci/Adobe** | ✅ OpenFX, Adobe, frei0r | gyroflow/gyroflow-plugins |
| **Corrección rolling shutter** | ✅ Basada en datos IMU | docs.gyroflow.xyz |
| **Corrección de lente** | ✅ Base de datos de perfiles de lente | docs.gyroflow.xyz |

### Nueva evidencia: OIS debe estar desactivado — respaldo académico [P64] [P65]

Anteriormente, la regla "OIS OFF" solo se respaldaba con documentación técnica de Gyroflow. Ahora contamos con papers:

#### DeepOIS (arXiv, 2021) — [P64] 🔴 Crítico

| Hallazgo | Valor |
|---|---|
| **Problema** | OIS mueve el lente independientemente del cuerpo, las lecturas IMU **no corresponden** a la imagen |
| **Error alineación sin OIS** | 0.688 |
| **Error alineación con OIS** | **1.038 (50% peor)** |
| **Conclusión textual** | "OIS terminates the possibility of image registration by gyros" |

**Relevancia:** Respalda directamente por qué OIS debe estar desactivado al usar Gyroflow.

#### ISPRS (2022) — Estabilización debe desactivarse [P65] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Incertidumbre parámetros** | **Hasta 300% mayor** con IS activado |
| **Error de reproyección** | **4x mayor** con IS activado |
| **Conclusión** | "IS must be disabled when photogrammetric 3D modelling is required" |

**Relevancia:** Corrobora desde la fotogrametría que la estabilización integrada degrada la precisión.

---

### Nueva evidencia: Video estabilizado supera a fotos estáticas [P66]

#### MangoYOLO video tracking (Sensors, 2019) — [P66] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Detección con video** | **62.3%** del conteo real de cosecha |
| **Detección con foto estática** | Solo **40.2%** |
| **Mejora absoluta** | **+22%** usando video en movimiento estabilizado |

**Relevancia:** Demuestra que capturar video estabilizado es superior a fotos individuales para conteo de frutos.

---

### Nueva evidencia: Motion blur degrada severamente YOLO [P68]

#### Lightweight GAN para cítricos (MDPI, 2025) — [P68] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **mAP@0.5:0.95** | **+86.4%** tras restaurar imágenes borrosas |
| **Recall** | **+76.9%** |
| **F1 score** | **+40.1%** |
| **False Negative Rate** | **-63.9%** |

**Relevancia:** El motion blur degrada severamente la detección YOLO. Justifica la necesidad de estabilización.

---

### Nueva evidencia: Estabilización en agricultura [P67]

#### Crop Row Video Stabilization (MDPI Sensors) — [P67] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Desplazamiento lateral suprimido** | **66%** del espacio entre hileras |
| **Desviación promedio** | ~20 píxeles (desde 93 píxeles inicial) |
| **Conclusión** | La estabilización de video "está totalmente justificada" en agricultura |

**Relevancia:** Justifica la estabilización en agricultura con métricas cuantitativas.

---

### NVIDIA 2014 — Fundamento teórico [P26]

Bell, Troccoli, Pulli (NVIDIA, ECCV 2014):
- Demostró que estabilización con giroscopio **supera a métodos basados en features**
- Corre en **tiempo real** en dispositivos móviles
- Corrige rolling shutter **per-frame**
- **Cita obligada** en la tesis por ser el fundamento de Gyroflow

### IMU + YOLO directo

**Repositorio GitHub:** zhouzypaul/object-recognition-imu (Paradiso Lab, Brown University)
- Post-procesa detecciones YOLO con Kalman Filter + IoU usando datos IMU
- No es agrícola pero es transferible

---

## Tabla resumen — Evidencia para justificar registro IMU

| Decisión | Respaldo | Tipo de fuente |
|---|---|---|
| **Registrar IMU durante captura** | Estabilización IMU supera a óptica en walking (32% mejor) | Paper [P11] |
| **100 Hz es suficiente** | Paper específico sobre sampling rate vs walking speed | Paper [P25] |
| **Usar Gyroflow en post-procesamiento** | Documentación oficial, 8.9k stars GitHub, plugins DaVinci/Adobe | Documentación técnica |
| **Usar Sensor Logger** | Listado en docs de Gyroflow como fuente compatible | Documentación técnica |
| **OIS debe estar desactivado** | DeepOIS: 50% peor alineación. ISPRS: 300% más incertidumbre. | Papers [P64], [P65] + Docs Gyroflow |
| **IMU mejora rolling shutter** | 3 papers con resultados cuantitativos | Papers [P17][P18][P19] |
| **IMU mejora deblurring** | 5% PSNR gain, 19% menos cómputo | Paper [P22] |
| **Video estabilizado vs fotos** | MangoYOLO: +22% detección con video | Paper [P66] |
| **Motion blur + YOLO** | Citrus GAN: 86.4% mAP drop por blur | Paper [P68] |
| **Estabilización en agricultura** | Crop row: 66% supresión desplazamiento | Paper [P67] |
| **IMU → YOLO mAP** | **No existe en agricultura** | Gap — tu contribución |

---

## Contradicciones y Matices — Investigación Complementaria

> **Contexto:** Se realizó una búsqueda sistemática (julio 2025) vía Semantic Scholar y web search para identificar papers que contradicen, matizan o validan las afirmaciones del Paso 2. Los resultados se presentan a continuación.

### 1. OIS Debe Estar OFF — Matiz importante

| Fuente | Hallazgo | Implicancia |
|--------|----------|-------------|
| **Qualcomm US20200412954A1** (2024) | Combina OIS+EIS exitosamente usando sensores Hall para leer posición del lente | El conflicto OIS-giroscopio es **corregible** si se tiene acceso a la posición del lente |
| **Google Pixel 2 — Fused Video Stabilization** (2017) | Sistema híbrido que fusiona datos del giroscopio con posición OIS mediante ML | Demostración comercial de que OIS+EIS pueden coexistir |
| **Apple US9596411** (2015) | OIS maneja alta frecuencia (>1-5Hz), EIS compensa baja frecuencia residual | Separación de bandas de frecuencia como estrategia de convivencia |
| **DeepOIS [P64] con compensación** | Con compensación: error 0.709 (vs 0.688 sin OIS) — solo **3% peor** | **El problema no es OIS per se, sino la falta de compensación** |
| **HyperOIS (IEEE TCE, 2024)** | Integración OIS+smartphone, SR -34.37dB a -26.90dB | OIS moderno puede ser compatible con procesamiento digital |

**Conclusión para la tesis:** La regla "OIS OFF" se mantiene para nuestro pipeline porque **Sensor Logger es una fuente externa** — no tenemos acceso a los sensores Hall del lente para compensar OIS. Pero el matiz es importante: en sistemas con realimentación de posición (cámaras modernas, gimbals), OIS no necesita desactivarse.

**Nuevas referencias:** Qualcomm (US20200412954A1) → [P100], HyperOIS → [P101]

---

### 2. Frecuencia de Muestreo IMU — 100 Hz es suficiente PERO con límites

| Fuente | Hallazgo | Aplica a tesis |
|--------|----------|----------------|
| ✅ **Fan et al. 2025 [P25]** | 100 Hz óptimo para orientación en walking | ✅ Sí, nuestro uso es orientación (sincronización video-IMU) |
| ⚠️ **Torun et al. (Sensors, 2021)** | 100 Hz **inadecuado** para parámetros espaciales (250 Hz óptimo). Useful gait content hasta 120 Hz | ❌ No, no estimamos stride length ni velocidad |
| ⚠️ **Gruber et al. (2022)** | 100 Hz subestima aceleraciones pico 19-36% | ❌ No, no medimos aceleraciones de impacto |
| ⚠️ **PLOS ONE (2019)** | 60 Hz altera análisis DFA; recomienda 120 Hz mínimo | ⚠️ Borde, pero no aplicamos DFA |

**Conclusión:** 100 Hz es adecuado para el propósito de la tesis (sincronizar video con IMU para estabilización). Las contradicciones aplican a **análisis de marcha preciso** o **estimación de parámetros espaciales** (stride length, velocidad), que no son el objetivo.

**Nueva referencia:** Torun et al. (2021) → [P102]

---

### 3. Gyroflow — Validado pero con limitaciones documentadas

| Limitación | Severidad | Mitigación |
|------------|-----------|------------|
| **Clock drift** en grabaciones largas (~1ms/20min Insta360) | Media | Videos de tesis serán cortos (1-2 min por hilera) |
| **Motion blur NO se corrige** con Gyroflow | Alta | Requiere shutter speed fijo + ND filters |
| **Jello >600Hz** no corregible por software | Baja | Walking handheld no genera vibraciones de alta frecuencia |
| **Sony IBIS** causa warping en algunos casos | Media | No usamos Sony, es smartphone |
| **Plugin DaVinci** rendimiento pobre con videos largos | Baja | Procesaremos en standalone Gyroflow, no plugin |
| **Sync drift** con Sensor Logger como fuente externa | Media | Usar clap sync + verificar sync visualmente |

**Sin papers académicos usando Gyroflow en agricultura** — gap confirmado que valida la oportunidad de la tesis.

---

### 4. Motion Blur + YOLO — El 86.4% es ENG1OSO

El paper Citrus GAN [P68] reporta "86.4% mAP@0.5:0.95 improvement" que es una **mejora relativa tras deblurring** — no una degradación absoluta.

| Fuente | Degradación real por blur | Modelo |
|--------|--------------------------|--------|
| **Citrus GAN [P68]** (imagen borrosa vs sharp) | **48.6%** mAP drop (0.630 → 0.324) | YOLO (no especifica versión) |
| **FEGW-YOLO (PMC, 2026)** | **21.4%** mAP@0.5 drop a blur severo (k=11) | YOLOv8n |
| **Quantization Study (arXiv, 2025)** | **11-15%** mAP drop con blur medio | YOLOv12 |
| **Knowledge Distillation (Springer, 2024)** | **2.5%** mAP@0.5 drop al 100% velocidad | YOLOv8 + KD |
| **MDPI Electronics (2025)** | **15-25%** mAP drop bajo blur según modelo | YOLOv3/v4/v7/v9/v11 |

**Dato crítico:** YOLOv4 tiene MEJOR robustez a blur que YOLOv8-v11. Las versiones más nuevas NO son más robustas.

**Conclusión:** La degradación por motion blur es real pero de magnitud **15-50%** (no 86.4%). Esto no debilita la justificación de estabilización, pero es importante reportar la métrica correcta.

**Nuevas referencias:** FEGW-YOLO → [P103], Quantization Study → [P104], Knowledge Distillation → [P105], MDPI Electronics → [P106]

---

### 5. Video Estabilizado > Fotos (+22%) — La mejora NO es por estabilización

El paper MangoYOLO [P66] reporta +22% de conteo con video (62.3%) vs fotos dual-view (40.2%). **Pero:**

- La mejora proviene de **cobertura multi-vista + tracking** (Kalman Filter + Hungarian algorithm), no de estabilización
- Múltiples papers agrícolas logran SOTA (mAP>0.9) sin estabilización de video
- No hay evidencia directa de que estabilización por sí sola dé +22%

**Conclusión:** La comparación relevante para la tesis es **video raw vs video estabilizado**, no video vs fotos.

---

### 6. IMU Supera a Óptica — Desactualizado (2014-2021)

Bell et al. (NVIDIA, 2014) [P26] demostró que giroscopio supera a feature-based en ese momento. Pero **el estado del arte cambió:**

| Método | Estabilidad (benchmark NUS) | Limitación |
|--------|---------------------------|------------|
| **Gyro-only** (Bell 2014) | ~0.83 | No mide traslación |
| **DeepFused** (WACV 2022) — IMU + optical flow | 0.853 | Híbrido, mejor que cada uno solo |
| **DUT** (IEEE TIP 2022) — Deep learning | 0.833 | Sin IMU necesaria |
| **MetaStab+DIFRINT** (CVPR 2024) | 0.862 | Test-time adaptation |
| **RStab** (CVPR 2024) — 3D multi-frame | 0.92 | SOTA actual |
| **GaVS** (SIGGRAPH 2025) — 3DGS | ~0.92 | SOTA actual |

**Conclusión:** Para agricultura (traslación dominante por caminar), IMU puro es inadecuado. Gyroflow es un sistema híbrido (IMU + corrección de lente + rolling shutter) — el enfoque correcto.

**Nuevas referencias:** DeepFused → [P107], RStab → [P108]

---

### 7. Rolling Shutter Correction — Beneficio es para geometría, NO para detección

| Fuente | Hallazgo | Relevancia |
|--------|----------|------------|
| ✅ **Mo et al. 2020 [P17]** | IMU mejora RS correction para SLAM | Baja (no hacemos SLAM) |
| ❌ **"Let's Roll" (arXiv, 2024)** | RS correction **NO necesaria** para detección de objetos a IoU≥0.5 | **Alta — directamente relevante** |
| ❌ **UAV Photogrammetry (MDPI, 2023)** | Modelos de corrección RS pueden debilitar estabilidad del bundle adjustment | Media |
| ⚠️ **iPhone 15 Pro** | Rolling shutter: **~5ms** (excepcional) | Medio — smartphones modernos tienen RS bajo |
| ⚠️ **DFRSC (2024), JCD (2021)** | Toda corrección RS introduce artefactos (deformación, pérdida de detalles) | Alta — riesgo de degradar calidad de imagen |

**Conclusión:** La corrección de rolling shutter que hace Gyroflow puede no aportar beneficio mensurable para detección YOLO. Es posible que desactivarla no degrade mAP, o incluso lo mejore al evitar artefactos. **La tesis puede medir esto como variable adicional.**

**Nueva referencia:** "Let's Roll" → [P109]

---

### 8. Gap de la Tesis — Reevaluación

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| **"No existe paper IMU→YOLO mAP en agricultura"** | ✅ Gap confirmado | ✅ **Sigue siendo gap — confirmado** |
| **zhouzypaul/object-recognition-imu (Brown 2022)** | No evaluado | ⚠️ Es POST-procesamiento, no PRE-procesamiento. No cierra el gap |
| **YOLO robustez a degradación** | No evaluado | ⚠️ Si YOLO es robusto, el efecto del preprocesamiento podría ser pequeño |
| **Riesgo de resultado nulo** | No evaluado | ⚠️ Un resultado nulo (poca mejora) sigue siendo contribución científica válida |

> **El gap se confirma.** No existe paper que mida cuantitativamente IMU preprocessing → YOLO mAP en agricultura. Sin embargo, la magnitud del efecto es incierta — la tesis debe estar preparada para un resultado modesto.

---

## Gap confirmado para la tesis

> **No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en métricas YOLO (mAP) o MOT (MOTA) para video agrícola.**

### Progreso en justificación del Paso 2

| Aspecto | Antes | Ahora | Matiz |
|---------|-------|-------|-------|
| **Gimbal mejora estabilidad** | ✅ [P43] | ✅ [P43] | — |
| **IMU supera a óptica** | ✅ [P11][P13] | ✅ [P11][P13] | ⚠️ **[P107][P108]** Deep learning 2024-2025 supera a IMU puro. Gyroflow (híbrido) es correcto. |
| **Rolling shutter con IMU** | ✅ [P18] | ✅ [P18] | ⚠️ **[P109]** RS correction no necesaria para detección a IoU≥0.5. Podría desactivarse sin pérdida. |
| **❌ OIS OFF** | ⚠️ Solo docs técnicas | ✅ **Resuelto** — [P64] DeepOIS 50% + [P65] ISPRS 300% | ⚠️ **[P100]** Con sensores Hall (posición lente), OIS puede coexistir. Nuestro pipeline (Sensor Logger externo) no tiene acceso → OIS OFF se mantiene. |
| **Video > Fotos detección** | ❌ No existía | ✅ [P66] MangoYOLO +22% | ⚠️ Mejora viene de **tracking multi-vista**, no de estabilización. |
| **Motion blur + YOLO** | ⚠️ Solo deblurring | ✅ [P68] Citrus GAN 86.4% | ⚠️ **[P103][P104][P105][P106]** El 86.4% es mejora relativa. Degradación real: 15-50% según modelo. YOLOv4 es más robusto que v8-v11. |
| **Estabilización agrícola** | ❌ No existía | ✅ [P67] Crop row 66% | — |
| **IMU preprocessing → YOLO mAP** | ❌ Gap | ❌ **Sigue siendo gap — tu contribución** | ⚠️ zhouzypaul (Brown 2022) es POST-procesamiento. Gap confirmado pero posible resultado modesto por robustez de YOLO. |

Tu tesis puede medir:
- mAP de YOLO sobre video **raw handheld**
- mAP de YOLO sobre video **estabilizado con Gyroflow**
- MOTA (ID switches) en ambos casos

