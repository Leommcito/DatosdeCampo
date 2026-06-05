# Pipeline de Captura Recomendado — Huerto de Mandarinas

## Resumen de decisiones con justificación

---

### Etapa 1 — App de Cámara

**Decisión:** Open Camera (gratis, open-source, Camera2 API)

| Característica | Por qué la elegimos | Fuente | Ref. |
|---|---|---|---|
| AF Lock | Evita focus hunting al caminar entre ramas | Documentación Open Camera | [D1], [P40] |
| AE Lock | Evita cambios de exposición sol/sombra | Documentación Open Camera | [D1], [P40], [P41] |
| WB Lock | Evita cambios de color cielo/nube/sombra | Documentación Open Camera | [D1] |
| ISO manual | Fija ISO bajo para minimizar ruido | Documentación Open Camera | [D1], [P40] |
| Shutter manual | Fija velocidad para congelar/blur controlado | Documentación Open Camera | [D1], [P40] |
| Bitrate configurable | Calidad constante en todo el video | Documentación Open Camera | [D1] |
| Gratis + open-source | Reproducible. Sin barrera económica. | SourceForge | [D1] |
| Sin marca de agua | A diferencia de apps gratuitas con watermark | — | — |

**Apps descartadas:**
- **Filmic Pro** ($5/semana): Subscription cara. Perfiles Log innecesarios para detección.
- **MCPro24fps** (~$20): Paga. Interfaz compleja. Overkill para detección de objetos.
- **Cámara nativa**: Sin control manual. No se pueden bloquear parámetros.

**Configuración recomendada:**
```
Camera2 API: ON (obligatorio)
Resolución: 4K (3840×2160) o 1080p si overheating
FPS: 30 fps
Shutter speed: 1/60s (regla 180°) o 1/120s si hay blur
ISO: 100-200 (lo más bajo posible con luz de día)
AF: LOCK (tocar fruta más cercana → lock)
WB: Daylight (~5200K) o Cloudy (~6500K)
Bitrate: 50-100 Mbps (el máximo que el dispositivo soporte)
Codec: H.264 por compatibilidad
```

---

### Etapa 2 — Estabilización

**Decisión:** Gimbal mecánico + Gyroflow (post-procesamiento)

| Componente | Justificación | Fuente | Ref. |
|---|---|---|---|
| **Gimbal DJI Osmo Mobile SE/6** | Elimina micro-shake sin warpear la imagen. El EIS deforma y confunde a detectores basados en geometría. | Comparativas técnicas de gimbals (ver referencias) | [P43] |
| **Gyroflow** | Estabilización basada en datos IMU reales. Corrige rolling shutter + distorsión de lente. No warpea. | [gyroflow.xyz](https://gyroflow.xyz) — 8.9k stars GitHub | [P11], [P13], [P18], [D2] |

**Gimbals recomendados (ordenados por precio):**
1. DJI Osmo Mobile SE (~$99) — 8h batería, magnético, plegable
2. DJI Osmo Mobile 6 (~$149) — igual + ActiveTrack (innecesario)
3. Zhiyun Smooth 5S (~$169) — 24h batería, luz integrada, mejor para jornadas largas

**⚠️ Regla crítica:** OIS debe estar desactivado si se usa Gyroflow ([docs Gyroflow](https://docs.gyroflow.xyz/app/getting-started/supported-cameras/mobile-phones))

---

### Etapa 3 — Logging IMU

**Decisión:** OpenCamera Sensors (fork) + Sensor Logger (backup)

| App | Ventaja | Fuente | Ref. |
|---|---|---|---|
| **OpenCamera Sensors (fork)** | Video + IMU sincronizados en el mismo clock nativo. Sin sync post-hoc. | [GitHub prime-slam](https://github.com/prime-slam/opencamera-sensors) | [D4] |
| **Sensor Logger** | Backup validado en investigación. Exporta CSV/JSON. Background recording. | [tszheichoi.com](https://www.tszheichoi.com/sensorlogger); Choi (CEUR Workshop, 2024) | [P23], [D3] |

**Frecuencia de muestreo suficiente:** **100 Hz** para caminata (~0.5-1.2 m/s).
- Respaldo: Fan et al. (2025) — Sensors MDPI — walking a 1.2 m/s con 100 Hz es suficiente
- El acelerómetro >100 Hz incluso degrada precisión
- Giroscopio es más importante que acelerómetro para orientación

---

### Etapa 4 — Sincronización Video-IMU

**Decisión:** OpenCamera Sensors (sincronización nativa) / Clap sync

| Método | Precisión | Cuándo usarlo | Ref. |
|---|---|---|---|
| **OpenCamera Sensors** | Frame-level | Opción A — sincronización nativa en el mismo clock | [D4] |
| **Clap sync** | ~1-2 frames | Opción B — si se usan apps separadas (grabar un aplauso audible) | [P24] |
| **Sync de Gyroflow** | <200ms típico | Cuando se usa Sensor Logger como fuente externa | [D2] |

**Respaldo:** MARS Logger paper (arXiv 2001.00470) — sincronización Camera2 API + SensorEvent en Android con offsets <5ms.

---

### Etapa 5 — Calibración de Cámara

**Decisión:** OpenCV + patrón Charuco (una vez al inicio del proyecto)

| Herramienta | Justificación | Fuente | Ref. |
|---|---|---|---|
| OpenCV + Charuco | Gratis, bien documentado. RMSE < 1px. | — | [P10], [P03] |
| MATLAB Camera Calibrator | Alternativa paga pero más fácil | Con licencia | — |

**Respaldo:** Elicit encontró 3 papers de calibración móvil. El más relevante (Peng et al., 2020) reporta corrección en GPU a 25fps en Android.

**Por qué es necesaria:** La distorsión de lente gran angular afecta la detección YOLO en los bordes del frame.

---

### Etapa 6 — Pre-procesamiento

**Decisión:** Gyroflow (estabilización + rolling shutter + distorsión) → (Opcional) Deblurring → YOLO

| Paso | Algoritmo | Propósito | Respaldo | Ref. |
|---|---|---|---|---|---|
| 1 | Gyroflow | Estabilizar + corregir rolling shutter + corregir distorsión | docs.gyroflow.xyz | [P11], [P13], [P18], [D2] |
| 2 | Frame selection (FFmpeg) | Descartar frames borrosos | Ingeniería de video | — |
| 3 | (Opcional) Deblurring | Eliminar motion blur residual | D2-YOLO paper (citrus) | [P22] |
| 4 | **YOLO + ByteTrack/CoTracker3** | Detección y tracking | — | [P34], [P35] |

**Respaldo:** Elicit encontró que el patrón en papers agrícolas es: capturar → rectificar temprano → detectar sobre frames limpios.

---

### Etapa 7 — Pipeline de Datos

| Parámetro | Recomendación | Razón | Ref. |
|---|---|---|---|---|
| **Formato** | MP4 | Universal | — |
| **Codec** | H.264 | Compatibilidad con todas las herramientas | — |
| **Bitrate** | 50 Mbps (4K) / 20 Mbps (1080p) | Calidad suficiente para detección | [P28] |
| **Extracción frames** | FFmpeg: `select=not(mod(n\,N))` | N = 1 para 30fps, N = 2 para 15fps | — |
| **Metadata** | ExifTool para GPS timestamps | Organización del dataset | — |

---

## Paso 0 — Pre-captura: Verificaciones obligatorias (hacer antes de salir)

### 1. Almacenamiento

| Cálculo | Valor |
|---|---|
| 4K @ 30fps a 50Mbps | **22 GB por hora** |
| 1080p @ 30fps a 20Mbps | **5 GB por hora** |
| Grabación estimada (30 min) | **11 GB (4K)** o **2.5 GB (1080p)** |

**Acción:** Verificar espacio libre en el teléfono. Si <20GB libres → bajar a 1080p o llevar tarjeta SD.

### 2. Batería

- Grabación 4K con pantalla encendida: **30-60 minutos** hasta batería agotada
- Sensor Logger en background: consumo adicional
- Gimbal: batería propia (~6-24h según modelo)

**Acción:** Smartphone al 100% + **power bank** + cable. Cargar gimbal al 100%.

### 3. Prueba de overheating — OBLIGATORIO hoy

**Procedimiento:**
1. Abrir Open Camera
2. Configurar en 4K 30fps
3. Grabar **10 minutos seguidos** (sin pausa)
4. Al final, tocar la parte trasera del teléfono

| Resultado | Decisión |
|---|---|
| **Tibia** (se puede sostener) | ✅ Grabar en 4K mañana |
| **Caliente** (no se puede sostener) | ⚠️ Grabar en **1080p** mañana. El overheating puede cerrar la app o bajar calidad sin avisar. |

### 4. Verificación final antes de salir

- [ ] Espacio libre suficiente para el tiempo estimado de grabación
- [ ] Power bank cargado + cable
- [ ] Open Camera instalada y probada (Camera2 API funcionando)
- [ ] Sensor Logger instalado y configurado (gyro+accel, 100Hz)
- [ ] Gimbal cargado
- [ ] Cuaderno + lápiz para anotar número de hilera por grabación

---

## Pipeline completo

```
PRE-CAPTURA (hoy):
  └─ Verificar espacio libre en el teléfono (mínimo 20GB para 4K)
  └─ Probar overheating: grabar 10 min en 4K, verificar temperatura
  └─ Cargar smartphone + gimbal + power bank
  └─ Cargar cuaderno para anotar hileras

EN CAMPO (8:30 AM):
  1. Abrir Open Camera → Camera2 API → ON
  2. Configurar: ISO=100-200, shutter=1/60-1/120, AF=Lock, WB=Daylight
  3. Res=4K (o 1080p si overheating), FPS=30, bitrate=50Mbps, codec=H.264
  4. Montar smartphone en gimbal
  5. Iniciar Sensor Logger (background, 100Hz, gyro+accel)
  6. Verificar que ambas apps graban
  7. Anotar número de hilera en cuaderno INICIAR grabación
  8. Caminar a ~0.5-1 m/s, distancia 0.5-1.5m del dosel
  9. Detener grabación → nueva grabación por hilera

POST-PROCESAMIENTO (después):
  1. Gyroflow: cargar video + datos IMU → estabilizar + RS + lente
  2. FFmpeg: extraer frames
  3. (Opcional) Deblurring
  4. Anotación (CVAT/Roboflow) + división train/val/test
  5. Entrenar YOLO + ByteTrack/CoTracker3
```

---

## Justificación académica por capa — ACTUALIZADO con papers reales

| Decisión | Tipo de evidencia | Fuente (paper real) | Ref. |
|---|---|---|---|---|
| Open Camera vs nativa | Documentación técnica | [Open Camera Help](https://opencamera.sourceforge.io/help.html) | [D1] |
| AF/AE/WB Lock | **Indirecta** — papers que demuestran que iluminación variable degrada detección | **FNF paper** (Kurtser et al.): exposición fija 20µs mejora detección. **ICNet (2025)**: compensación de iluminación mejora PSNR 28→40.79dB. **Coffee monitoring (Sensors, 2020)**: AUTO causa blur, necesitaron IMU para seleccionar frames. | [P40], [P41], [P27] |
| Shutter 1/60-1/120 | Paper + Regla 180° | **Rolling shutter + distance (Sensors, 2020)**: RSE inversamente proporcional a distancia, lineal con velocidad. **Rice GMC (Sensors, 2021)**: ISO=25, shutter=1/400s fijo. | [P40] |
| ISO 100-200 | Paper que fijó ISO | **Rice GMC (Sensors, 2021)**: ISO=25 fijo para minimizar variabilidad. | [P40] |
| Gimbal | **Paper directo** | **Gašparović & Jurjević**: gimbal mejora 6x estabilidad de orientación. Roll/pitch 69.9°→2.56°. **sUAS gimbal survey**: MIS (gimbal) > OIS > DIS. | [P43] |
| Sensor Logger 100Hz | Paper específico | **Fan et al. (2025)** — Sensors MDPI. Walking 1.2m/s, 100Hz suficiente. | [P25] |
| Gyroflow | Documentación técnica + GitHub | [gyroflow.xyz](https://gyroflow.xyz) — 8.9k stars. Soporta Sensor Logger. | [P11], [P13], [P18], [D2] |
| Distancia 0.3-1.5m | **Paper que compara distancias** | **Kuznetsova et al. (2020)** — YOLOv3 apple detection. Comparó **0.2m, 0.5m, 1.0m, 2.0m** con Nikon D3500. También comparó ángulos (front, side, back, scattered). | [P28] |
| Velocidad de caminata | Paper que reporta velocidad | **OrangeYolo (2024)**: rover a **2 m/s** uniforme, DJI Osmo Action, 60fps 1080p. **Coffee monitoring (2020)**: **3 cm/s** sobre rama, máx 5 cm/s para evitar blur. | [P31], [P27] |
| 4K 30fps | Inferencia + papers que usan altas resoluciones | **Apple YOLOv3 (2020)**: usaron 3888×5184 a 4032×3024. **Rice GMC (2021)**: 4032×3024. Múltiples papers. | [P28] |

### Nivel de respaldo por decisión

| Decisión | ¿Respaldo real en paper con nombre? | Confianza | Referencias |
|---|---|---|---|---|
| Open Camera (app específica) | ❌ Inferencia — ningún paper agrícola nombra Open Camera | Baja | [D1] |
| AF/AE/WB Lock | ⚠️ Indirecto — papers demuestran que estabilizar captura mejora detección | Media | [P40], [P41] |
| Shutter 1/60-1/120 | ⚠️ Parcial — hay papers que fijan shutter | Media | [P40] |
| ISO 100-200 | ⚠️ Parcial — hay paper que fija ISO=25 | Media | [P40] |
| **Gimbal** | ✅ **Sí, paper directo** — Gašparović & Jurjević | **Alta** | [P43] |
| **Sensor Logger 100Hz** | ✅ **Sí, paper directo** — Fan et al. (2025) | **Alta** | [P25] |
| **Gyroflow** | ✅ Sí — docs técnicas + GitHub + papers IMU | **Alta** | [P11], [P13], [D2] |
| **Distancia 0.3-1.5m** | ✅ **Sí, paper compara distancias** — Kuznetsova et al. (2020) | **Alta** | [P28], [P37] |
| Velocidad caminata | ⚠️ Reportado pero no comparado — OrangeYolo a 2m/s, Coffee a 3cm/s | Media | [P31], [P27] |
| 4K 30fps | ⚠️ Inferencia — papers usan altas resoluciones pero no comparan | Media | [P28] |

### Gap confirmado para la tesis

**No existe un paper agrícola que:**
1. Nombre una app de captura específica (Open Camera, Filmic Pro)
2. Compare auto vs manual con métricas YOLO
3. Compare distancias al dosel con métricas de detección para smartphone
4. Compare walking speeds con métricas de tracking

**Tu contribución original:** Documentar y medir cuantitativamente el impacto de estas decisiones en mAP/MOTA para video de mandarinas.
