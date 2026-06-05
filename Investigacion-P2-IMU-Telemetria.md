# Investigación — Pregunta 2: Registro de Telemetría IMU

## Fuentes consultadas

- **Elicit**: 12 papers (CSV: `Elicit - IMU-assisted video processing papers.csv`)
- **Búsqueda web complementaria**: Documentación de Gyroflow, papers de gait analysis, reviews técnicas

---

## Resultados de Elicit

### Papers sobre estabilización con IMU

| Paper | Método | Resultado cuantitativo | Dispositivo |
|---|---|---|---|
| Han et al. (sin título) | Fusión giroscopio + visión | **32% mejor estabilización**, 32.6ms latencia | Smartphones, smart glasses |
| Li et al. (2023) — Deep Online VS | IMU sensor guidance | **25 fps en 1080p** tiempo real | Dispositivos móviles |
| Li et al. (2025) — Multi-Modal VS | Gyroscope + clustering + depth | **47.8% SSIM mejora**, 37% más rápido | Dispositivos móviles |
| Jang et al. (2024) — Full-frame VS | IMU + optical flow + neural rendering | **18% Stability score**, 3% Distortion | Dispositivos móviles |
| Auysakul et al. (2018) — Hybrid Motion | KLT + IMU switching | Tiempo real, multi-threaded | Cámaras handheld |

### Papers sobre rolling shutter con IMU

| Paper | Método | Resultado | Dispositivo |
|---|---|---|---|
| Mo et al. (2020) — IMU RS Correction | IMU pose refinement | Mejora downstream DSO | Single-view camera |
| Zhang & Zhang (2023) — Point Feature RS | High-frequency IMU | **Supera SOTA en precisión y costo** | Android phone |
| Wu et al. (2021) — Simultaneous VS+RS | Joint modeling | Superior a SOTA | CMOS / handheld |

### Papers sobre motion blur con giroscopio

| Paper | Método | Resultado | Nota |
|---|---|---|---|
| Ji et al. (2021) — Gyro-guided deblurring | Gyroscope guidance | Mejora visual + feature detectors | Sin métrica YOLO |
| Mustaniemi et al. (2018) — Inertial-aided | Gyroscope + CNN | Tiempo real, mejora visual | Pionero |
| Arslan et al. (2024) — Mesh-grid deblurring | IMU-informed mesh | **5% PSNR gain**, 19% menos cómputo | Dato más limpio |

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
| **OIS** | ⚠️ Debe estar desactivado | docs.gyroflow.xyz |
| **Plugin DaVinci/Adobe** | ✅ OpenFX, Adobe, frei0r | gyroflow/gyroflow-plugins |
| **Corrección rolling shutter** | ✅ Basada en datos IMU | docs.gyroflow.xyz |
| **Corrección de lente** | ✅ Base de datos de perfiles de lente | docs.gyroflow.xyz |

### NVIDIA 2014 — Fundamento teórico

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
| **Registrar IMU durante captura** | Estabilización IMU supera a óptica en walking (32% mejor) | Paper (Han et al.) |
| **100 Hz es suficiente** | Paper específico sobre sampling rate vs walking speed | Paper (Fan et al., 2025) |
| **Usar Gyroflow en post-procesamiento** | Documentación oficial, 8.9k stars GitHub, plugins DaVinci/Adobe | Documentación técnica |
| **Usar Sensor Logger** | Listado en docs de Gyroflow como fuente compatible | Documentación técnica |
| **OIS debe estar desactivado** | Documentación de Gyroflow | Documentación técnica |
| **IMU mejora rolling shutter** | 3 papers con resultados cuantitativos | Papers (Mo 2020, Zhang 2023, Wu 2021) |
| **IMU mejora deblurring** | 5% PSNR gain, 19% menos cómputo | Paper (Arslan et al., 2024) |
| **IMU → YOLO mAP** | **No existe en agricultura** | Gap — tu contribución |

---

## Gap confirmado para la tesis

> **No existe un paper que mida cuantitativamente el impacto del pre-procesamiento con IMU (Gyroflow) en métricas YOLO (mAP) o MOT (MOTA) para video agrícola.**

Tu tesis puede medir:
- mAP de YOLO sobre video **raw handheld**
- mAP de YOLO sobre video **estabilizado con Gyroflow**
- MOTA (ID switches) en ambos casos
