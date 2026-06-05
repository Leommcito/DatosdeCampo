# Metodología de Captura — Video Manual con Smartphone en Huertos de Mandarinas

**Proyecto:** Tesis — Protocolo de recolección de datos en campo para detección YOLO y seguimiento MOT
**Cultivo objetivo:** Mandarinas en huerto denso (alta oclusión, follaje denso, frutos pequeños)
**Tipo de captura:** Manual (operador caminando con smartphone)
**Fecha de validación en campo:** 05/06/2026
**Condiciones climáticas:** Día despejado o parcialmente nublado. Sin lluvia. Temperatura <35°C.

---

## 1. Dispositivo

| Parámetro | Especificación |
|---|---|
| **Modelo de smartphone** | [Completar con modelo real] |
| **Sistema operativo** | Android [versión] |
| **Camera2 API** | ✅ Sí compatible / ❌ No compatible |
| **IMU disponible** | Giroscopio, Acelerómetro, Magnetómetro |
| **Almacenamiento libre** | [X] GB al inicio de la captura |
| **Batería al inicio** | 100% |

**Criterio de selección:** Se requiere un smartphone Android con soporte de Camera2 API para acceder a controles manuales de cámara (ISO, shutter, AF lock, AE lock, WB lock). Cualquier dispositivo que cumpla este requisito es apto.

**Verificación:** Instalar la app gratuita **"Camera2 API Probe"** (Google Play) para confirmar que el dispositivo tiene soporte completo de Camera2 API (nivel de soporte "FULL" o "LEVEL_3"). Si el dispositivo solo tiene soporte "LEGACY", no podrá usar controles manuales y deberá reemplazarse.

---

## 2. Software

### 2.1 App de captura de video

| Parámetro | Valor |
|---|---|
| **App** | Open Camera |
| **Versión** | [Última disponible en Google Play] |
| **Licencia** | GPLv3 (gratuita y open-source) |
| **URL** | https://opencamera.sourceforge.io/ |

**Justificación:** Open Camera es la única app gratuita y open-source que permite el bloqueo simultáneo de autofoco (AF), exposición (AE) y balance de blancos (WB), junto con control manual de ISO, shutter speed y bitrate. Su naturaleza open-source garantiza reproducibilidad para otros investigadores.

**Alternativas descartadas:**
- **Filmic Pro** ($5/semana): Subscription costosa. Perfiles Log innecesarios para detección de objetos.
- **MCPro24fps** (~$20): Paga. Funciones profesionales excesivas para detección de objetos.
- **Cámara nativa:** No permite bloquear parámetros individualmente.

### 2.2 App de logging IMU

| Parámetro | Valor |
|---|---|
| **App** | Sensor Logger |
| **Versión** | [Última disponible] |
| **Licencia** | Gratuita (funciones básicas) |
| **URL** | https://www.tszheichoi.com/sensorlogger |

**Justificación:** Sensor Logger es la app más completa para registro de sensores en background. Está validada en investigación (Choi, CEUR Workshop 2024), exporta en CSV, y es compatible con Gyroflow como fuente de datos IMU.

---

## 3. Configuración de cámara

### 3.1 Parámetros de captura

| Parámetro | Valor | Fundamento |
|---|---|---|
| **Resolución** | 4K (3840×2160) o 1080p (1920×1080) | 4K provee más píxeles por fruto pequeño. Si overheating, bajar a 1080p. |
| **FPS** | 30 | Suficiente para tracking (ByteTrack, CoTracker3). 60fps duplica el dataset sin ganancia probada. |
| **ISO** | 100-200 (lo más bajo posible con luz de día) | Minimiza ruido digital que YOLO puede confundir con textura de fruto. |
| **Shutter speed** | 1/60s (regla 180°) o 1/120s (si hay motion blur) | Balance entre motion blur natural y nitidez de frame. |
| **Autofocus (AF)** | LOCK — tocar la fruta más cercana para enfocar, luego lock | Evita focus hunting al caminar entre ramas. |
| **Exposición (AE)** | LOCK | Evita cambios de exposición al pasar por sombra/sol. |
| **White balance (WB)** | Daylight (~5200K) o Cloudy (~6500K) | Evita cambios de color cielo/nube/sombra. |
| **Bitrate** | 50 Mbps (máximo que el dispositivo soporte estable) | Calidad constante en todo el video. |
| **Codec** | H.264 | Compatibilidad universal con herramientas de post-procesamiento. |
| **Camera2 API** | ON (obligatorio) | Desbloquea controles manuales. |

### 3.2 Procedimiento de configuración en Open Camera

1. Settings → Camera2 API → **ON**
2. Settings → Video Settings:
   - Video resolution: 4K o 1080p
   - Video bitrate: 50 Mbps
   - Video FPS: 30
   - Codec: H.264
   - Enable video stabilization: **OFF** (lo hará Gyroflow)
3. Volver a la vista de cámara
4. Tocar la pantalla sobre la fruta más cercana → aparece el rectángulo de enfoque
5. Tocar el ícono 🔒 AF (autofocus lock) — aparece candado
6. Tocar el ícono 🔒 AE (exposure lock) — aparece candado
7. Tocar el ícono W (white balance lock) — aparece candado
8. Verificar en pantalla: ISO y shutter fijos, AF lock, AE lock, WB lock

---

## 4. Configuración de IMU

| Parámetro | Valor |
|---|---|
| **Sensores activados** | Giroscopio (Rotation Rate) + Acelerómetro (Device Acceleration) |
| **Frecuencia de muestreo** | 100 Hz |
| **Formato de exportación** | CSV (Zipped CSV) |
| **Modo de grabación** | Background |

**Fundamento de frecuencia:** Fan et al. (2025) — Sensors MDPI — demostró que **100 Hz es suficiente** para capturar la firma de movimiento humano al caminar a 1.2 m/s. Frecuencias mayores no mejoran precisión y el acelerómetro >100 Hz incluso la degrada.

### ⚠️ Importante: Evitar que Android mate Sensor Logger en background

Android puede cerrar automáticamente las apps en background para ahorrar batería. Para evitarlo:

1. Settings → Apps → Sensor Logger → **"Ignorar optimización de batería"** (o "Sin restricciones")
2. Settings → Apps → Sensor Logger → **Permitir actividad en segundo plano**

Si no se hace esto, Sensor Logger puede dejar de grabar IMU a mitad de la caminata sin que el operador lo note.

### Procedimiento de configuración en Sensor Logger

1. Seleccionar sensores: Gyroscope + Accelerometer
2. Sampling frequency: 100 Hz
3. Export format: Zipped CSV
4. **Iniciar y detener Sensor Logger por CADA grabación** (no dejarlo corriendo todo el día)
5. La app corre en background mientras OpenCamera graba video

**Recomendación:** Iniciar Sensor Logger → iniciar OpenCamera → grabar → detener OpenCamera → detener Sensor Logger. Esto genera 1 archivo CSV por video, facilitando la sincronización.

### Respaldo académico

- **Principio:** Fan et al. (2025) — Sensors. Walking 1.2 m/s, 100Hz suficiente.
- **App:** Choi (CEUR Workshop, 2024) — Sensor Logger validado para investigación.
- **Compatibilidad Gyroflow:** Sensor Logger listado como fuente IMU compatible (docs.gyroflow.xyz)

---

## 5. Equipo de estabilización

### 5.1 Hardware

| Elemento | Especificación |
|---|---|
| **Gimbal** | [Modelo: DJI Osmo Mobile SE / 6 / Zhiyun Smooth 5S / otro] |
| **Autonomía** | [X] horas |
| **Peso** | [X] g |

**Fundamento:** Gašparović & Jurjević demostraron que el uso de gimbal mejora la estabilidad de orientación **6 veces** (variación de roll/pitch de 69.9° sin gimbal a 2.56° con gimbal). La estabilización mecánica (gimbal) es superior a la electrónica (EIS) porque no warpea ni deforma la imagen (sUAS gimbal survey, IEEE).

### 5.2 Regla crítica

**OIS (Optical Image Stabilization) del teléfono debe estar DESACTIVADO.**

El OIS interfiere con la estabilización basada en datos IMU de Gyroflow. Si no se puede desactivar en el modelo específico, documentar y evaluar el impacto.

---

## 6. Procedimiento de captura en campo

### 6.1 Antes de salir (verificación pre-campo)

| Verificación | Criterio |
|---|---|
| **Almacenamiento** | ≥20 GB libres para 4K / ≥5 GB para 1080p |
| **Batería smartphone** | 100% + power bank cargado |
| **Batería gimbal** | 100% |
| **Prueba de overheating** | Grabar 10 min en 4K — si el teléfono se calienta demasiado, bajar a 1080p |
| **Apps instaladas** | Open Camera + Sensor Logger |
| **Configuración de cámara** | Verificar AF Lock, AE Lock, WB Lock |
| **Configuración IMU** | Verificar sensores y frecuencia |
| **Gimbal** | Probar balance del teléfono |
| **Material de anotación** | Cuaderno + lápiz para registrar hileras |

### 6.2 En campo

1. **Posicionamiento del operador:**
   - Parado frente a la hilera, de frente al dosel lateral
   - Smartphone en horizontal (landscape) montado en gimbal
   - Cámara apuntando al dosel lateral (0-30° hacia arriba)

2. **Antes de cada grabación:**
   - Verificar configuración de Open Camera (AF lock, AE lock, WB lock)
   - Iniciar Sensor Logger (background)
   - Anotar en cuaderno: número de grabación, hilera, hora, condiciones de luz
   - Iniciar grabación en Open Camera

3. **Durante la grabación:**
   - Caminar a velocidad constante (~0.5-1 m/s)
   - Mantener distancia de 0.5-1.5 m del dosel
   - No usar zoom digital
   - No cambiar ángulo bruscamente
   - Evitar que el sol dé directo a la lente

4. **Después de cada grabación:**
   - Detener grabación en Open Camera
   - Detener grabación en Sensor Logger
   - Anotar finalización en cuaderno

5. **Repetir por cada hilera**

### 6.3 Tamaño de muestra

| Parámetro | Valor mínimo recomendado |
|---|---|
| **Hileras** | ≥5 (ideal 8-10) |
| **Duración por hilera** | 3-5 minutos |
| **Tiempo total de grabación** | 15-50 minutos |
| **Frames totales estimados** (30fps, 1 frame cada 5) | 5,400-18,000 imágenes |
| **Frutos por imagen** | Variable (depende de densidad del huerto) |

**Nota:** Para un dataset de YOLO, se recomienda mínimo 1,000-2,000 imágenes anotadas. Con 5 hileras de 3 minutos extrayendo 1 frame cada 5 (6 fps) obtenés ~5,400 imágenes, de las cuales anotás una muestra representativa.

### 6.4 Sincronización video-IMU

**Método principal — Iniciar/detener Sensor Logger por grabación:**

1. Iniciar Sensor Logger → **anotar hora exacta** en cuaderno
2. Iniciar OpenCamera → grabar hilera
3. Detener OpenCamera → **anotar hora exacta**
4. Detener Sensor Logger

Esto genera **1 archivo CSV por video**. El nombre del CSV incluye la fecha y hora de inicio, que debe coincidir con lo anotado en el cuaderno.

**Método de respaldo — Clap sync (si Sensor Logger corre continuamente):**

1. Antes de cada grabación, dar una palmada fuerte frente al teléfono
2. La palmada genera un pico de audio en el video y un pico de aceleración en el CSV
3. En post-procesamiento: alinear ambos picos para sincronizar

### 6.5 Condiciones climáticas adversas

| Condición | Acción |
|---|---|
| **Lluvia** | Cancelar captura. El agua en la lente arruina el dataset. |
| **Viento fuerte** (>20 km/h) | Posponer. El movimiento de ramas genera motion blur adicional no controlable. |
| **Nublado** | ✅ Grabar normalmente. Ajustar WB a Cloudy. Luz difusa es buena para detección. |
| **Sol cenital** (12:00-14:00) | Evitar. Sombras duras y alto contraste degradan detección. |
| **Temperatura >35°C** | Monitorear overheating. Considerar pausas entre grabaciones. |

### 6.6 Parámetros de captura resumidos

| Parámetro | Valor | Fundamento |
|---|---|---|
| **Lado de la hilera** | Un solo lado por grabación. Para cubrir ambos lados, hacer dos grabaciones separadas. | Evita mezclar perspectivas. |
| **Distancia al dosel** | 0.5-1.5 m | Kuznetsova et al. (2020) comparó 0.2, 0.5, 1.0, 2.0m. Rango óptimo. |
| **Ángulo de cámara** | 0-30° hacia arriba | Práctica documentada en papers de detección de frutos. |
| **Velocidad de caminata** | ~0.5-1 m/s | Basado en OrangeYolo (2 m/s en rover) y Coffee monitoring (3 cm/s en rama). Rango intermedio para captura manual. |
| **Duración por grabación** | 3-5 minutos continuos | Suficiente para cubrir una hilera. |
| **Trayectoria** | Una hilera por grabación | Evita mezclar condiciones entre hileras. |
| **Horario** | 8:30 AM en adelante | Cocoa dataset (2023) capturó 8:00-16:00. Evitar sol cenital (12:00-14:00). |

---

## 7. Post-procesamiento

### 7.1 Estabilización con Gyroflow

| Paso | Descripción |
|---|---|
| **1** | Cargar video en Gyroflow |
| **2** | Cargar datos IMU (Sensor Logger CSV) |
| **3** | Sincronizar video + IMU (auto-sync o manual) |
| **4** | Seleccionar perfil de lente (o crear uno nuevo) |
| **5** | Aplicar estabilización + corrección de rolling shutter |
| **6** | Exportar video estabilizado |

**Fundamento:** Gyroflow (8.9k estrellas GitHub, 40+ contribuidores) es la herramienta open-source estándar para estabilización basada en datos IMU. Corrige rolling shutter y distorsión de lente sin warpear la imagen (a diferencia del EIS).

**Papers que respaldan el enfoque IMU-based:**
- Han et al.: 32% mejor estabilización que métodos ópticos en walking
- Li et al. (2025): 47.8% mejora SSIM con fusión giroscopio + visión
- Zhang & Zhang (2023): rolling shutter con IMU de alta frecuencia supera SOTA en Android

### 7.2 Extracción de frames

| Herramienta | Comando | Descripción |
|---|---|---|
| FFmpeg | `ffmpeg -i video.mp4 -vf "select=not(mod(n\,N))" frames/%05d.jpg` | Extrae 1 frame cada N (ej: N=1 para 30fps, N=5 para 6fps) |

**Opcional:** Descartar frames borrosos mediante Laplacian variance. Umbral típico: 100. Frames con varianza < umbral se descartan.

### 7.3 Organización de datos

```
/dataset/
  /hilera-01/
    2026-06-05_hilera-01_soleado_raw.mp4        # video original
    2026-06-05_hilera-01_soleado_imu.csv         # datos IMU sincronizados
    2026-06-05_hilera-01_soleado_estabilizado.mp4  # post Gyroflow
    /frames/
      frame_00001.jpg
      frame_00002.jpg
      ...
  /hilera-02/
    ...
```

**Nomenclatura de archivos:**
- Video: `YYYY-MM-DD_hilera-XX_condiciones.mp4`
- IMU CSV: `YYYY-MM-DD_hilera-XX_condiciones_imu.csv`
- Video estabilizado: `YYYY-MM-DD_hilera-XX_condiciones_estabilizado.mp4`

Ejemplo: `2026-06-05_hilera-03_soleado.mp4` y `2026-06-05_hilera-03_soleado_imu.csv`

Si se usa el método de iniciar/detener Sensor Logger por grabación, el CSV generado por la app tendrá un nombre automático con timestamp. **Renombrarlo inmediatamente después de cada grabación** para que coincida con el nombre del video. Esto evita pérdida de sincronización.

---

## 8. Anotación y división del dataset (post-captura)

### 8.1 Anotación

Las anotaciones se realizan con **CVAT** (Computer Vision Annotation Tool, gratuita):
1. Subir los frames extraídos
2. Dibujar bounding boxes alrededor de cada fruto visible
3. Etiquetar cada fruto como "mandarina"
4. Exportar en formato YOLO (.txt con coordenadas normalizadas)

**Criterio de anotación:**
- Anotar TODO fruto visible, incluso si está parcialmente ocluido
- NO anotar frutos si >80% del área está oculta
- NO anotar frutos en el borde extremo del frame (<5% del borde)

### 8.2 División train/val/test

| Grupo | Porcentaje | Criterio |
|---|---|---|
| **Train** | 70% | Hileras completas seleccionadas al azar |
| **Validation** | 20% | Hileras completas seleccionadas al azar |
| **Test** | 10% | Hileras completas **NUNCA vistas por el modelo** |

**Regla crítica:** La división debe ser por **hilera**, no por frame. Si un frame de la hilera 1 está en train, ningún frame de la hilera 1 puede estar en test. Esto evita data leakage.

---

## 9. Evaluación de la metodología

Para validar si este protocolo mejora la calidad del dataset, se propone un **experimento comparativo**:

### 9.1 Experimento A/B

| Grupo | Captura |
|---|---|
| **A (Protocolo)** | Video capturado siguiendo esta metodología (AF Lock, AE Lock, WB Lock, gimbal, IMU) |
| **B (Control)** | Video capturado con cámara nativa en modo automático, mismo árbol, misma hilera, mismo día |

### 9.2 Métricas de comparación

| Métrica | Qué mide |
|---|---|
| **mAP@0.5** | Precisión de YOLO entrenado con cada grupo |
| **MOTA** | Calidad de tracking (ByteTrack/CoTracker3) |
| **IDF1** | Consistencia de identidades en tracking |
| **% frames borrosos** | Calidad del video capturado |
| **Ratio de frames útiles** | Frames aprovechables para detección |

### 9.3 Hipótesis

> El dataset capturado con el protocolo propuesto producirá un mAP@0.5 superior al dataset capturado sin protocolo, debido a la reducción de motion blur, focus hunting y variaciones de exposición.

---

## 10. Limitaciones de la metodología

| Limitación | Descripción |
|---|---|
| **Específica para huertos densos** | Este protocolo fue diseñado para mandarinas en huerto denso con alta oclusión. No necesariamente aplica a otros cultivos (viñedos, berries, cultivos de campo abierto). |
| **Solo Android** | Open Camera solo funciona en Android. iOS requiere apps alternativas (Filmic Pro, ProMovie). |
| **Requiere Camera2 API** | No todos los smartphones Android soportan Camera2 API completa. Dispositivos de gama baja pueden no tener controles manuales. |
| **Una sola sesión de captura** | La validación se realizó en una fecha específica. Condiciones climáticas estacionales (lluvia, viento, temperatura) pueden afectar la reproducibilidad. |
| **Gimbal requerido** | Sin gimbal, la calidad de estabilización se reduce significativamente. No se evaluó el protocolo sin gimbal. |
| **Overheathing no controlado** | La decisión de bajar a 1080p por overheating es reactiva. No hay un mecanismo de monitoreo de temperatura del dispositivo. |

---

## 11. Reproducibilidad

Para que otro investigador reproduzca exactamente este experimento, necesita:

| Elemento | Especificación |
|---|---|
| **Smartphone** | Cualquier Android con Camera2 API (verificar con "Camera2 API Probe") |
| **Open Camera** | Versión [última] |
| **Sensor Logger** | Versión [última] |
| **Gyroflow** | Versión 1.6.3+ |
| **FFmpeg** | Versión [última] |
| **Gimbal** | 3-axis smartphone gimbal (DJI Osmo, Zhiyun, Hohem, Insta360) |
| **Huerto** | Mandarinas, densidad alta, distancia entre hileras [X]m |

---

## 12. Metodologías similares encontradas en la literatura

| Referencia | Cultivo | Dispositivo | Protocolo | Datos reportados |
|---|---|---|---|---|
| **Coffee cherry counting (2024)** — YOLOv8 con farmers locales | Café | Smartphones varios (Xiaomi, Samsung, Motorola) | **3 ramas/árbol** (superior, media, inferior). Fotos entre 6AM-6PM. Sin sol directo en lente. Sin mover cámara post-captura. Res: 768×768 a 1024×1024. | 2,968 árboles, 8,904 fotos. Anotación PASCAL VOC. División dataset no especifica. |
| **OrangeYolo (2024)** — Rover + DJI Osmo Action | Naranjas | DJI Osmo Action (1920×1080, 60fps) | Rover a **2 m/s uniforme**. Cámara **perpendicular a la hilera**. Distancia constante. 145° FOV. | 1,465 muestras. División 7:3 train/test. |
| **Strawberry longitudinal (2020)** — 3 cámaras a 45° | Fresas | 3 cámaras RGB, plataforma robótica Thorvald | **3 veces al día, 3 veces por semana**, 2 meses. Cámaras a **45°** entre sí. Markers visuales para consistencia. 1920×1080. | 6,189 imágenes, 150 anotadas manualmente. Incluye datos de clima y temperatura. |
| **Pear dataset (2023)** — Trípode + UAV | Peras | Kodak AZ651 (trípode) + DJI Phantom 4 (UAV) | **4 horarios**: 7-8AM, 10-11AM, 2-3PM, 6-7PM. Ángulo 20°-80°. Velocidad UAV **1 m/s** para evitar blur. Res: 1280×720. | 7,541 imágenes → 3,680 (ORB para eliminar similares). División 80/10/10. |
| **Cocoa dataset (2023)** — 5 smartphones | Cacao | Samsung Galaxy, iPhone SE, Motorola, LG | **8AM-4PM**. Trayectoria **zigzag**. 1-4 fotos/ángulo por fruto. Aspect ratio **1:1**. Resize a 3000×3000. | 4,116 imágenes, 7,917 instancias. Anotación CVAT. Formato COCO + segmentation mask. |
| **Strawberry phenotyping (2022)** — QR marker | Fresas | iPhone 6S Plus, Galaxy S8 | **6AM-6PM**. Cámara **perpendicular** al objetivo con **QR code** como referencia de calibración espacial. Exposure en **AUTO**, AF en **AUTO**. | 70 plantas, 6 fenotipos. Uso de QR para corrección de distorsión. |
| **Apple YOLOv3 (2020)** — Nikon D3500 | Manzanas | Nikon D3500 + lente 18-140mm | **Comparó 4 distancias**: 0.2, 0.5, 1.0, 2.0m. **4 condiciones de luz**: front, side, back, scattered. Varias resoluciones (3888×5184 a 4032×3024). | 878 imágenes, 5,142 manzanas. Distancia óptima: k=3 para far-view. |
| **Apple recognition (2023)** — 4 períodos | Manzanas | Cámara CCD | **4 períodos**: mañana, mediodía, tarde, noche. **Iluminaciones**: front, side, back, artificial. **Ángulo y distancia variables**. Res: 4032×3024. | 2,200 frames → 4,000 con aumentación. LabelImg. Formato Pascal VOC. |

### Lecciones aprendidas para tu protocolo

| Aspecto | Lo que hacen los papers | Lo que hacemos nosotros |
|---|---|---|
| **Horario** | 6AM-6PM / 8AM-4PM. Evitan sol cenital (12-2PM). | ✅ 8:30AM en adelante. Evitar 12-14PM. |
| **Distancia** | 0.2-2.0m (Kuznetsova compara 4 distancias). 50-80cm (fresas). | ✅ 0.5-1.5m rango respaldado. |
| **Velocidad** | 2 m/s rover (OrangeYolo). 1 m/s UAV (peras). 3 cm/s rama (café). | ⚠️ Nuestra velocidad 0.5-1 m/s es conservadora pero razonable. |
| **Ángulo** | 20°-80° (peras). 45° (fresas). Perpendicular (naranjas). | ✅ 0-30°. Consistente, aunque podríamos considerar más variedad. |
| **Múltiples dispositivos** | Cocoa usa 5 smartphones distintos. Sweet cherry usa 3. | ❌ Nosotros usamos 1 solo dispositivo. Limita generalización del dataset. |
| **Condiciones de luz** | Todos capturan en múltiples condiciones (soleado, nublado, varios horarios). | ✅ Planeado. |
| **Nivel de detalle metodológico** | **Ninguno** reporta app de cámara, ni ISO, ni shutter, ni AF lock. | **Este es nuestro gap y nuestra contribución.** |

---

## 13. Referencias

- Fan, B. et al. (2025). "Influence of Sampling Rate on Wearable IMU Orientation Estimation Accuracy for Human Movement Analysis". *Sensors*, 25(7), 1976.
- Kuznetsova, A. et al. (2020). "Using YOLOv3 Algorithm with Pre- and Post-Processing for Apple Detection in Fruit-Harvesting Robot". *Agronomy*, 10(7), 1016.
- Gašparović, M. & Jurjević, L. "Gimbal Influence on the Stability of Exterior Orientation Parameters of UAV Acquired Images". *Sensors*.
- Choi, K.T.H. (2024). "Sensor Logger: A Framework for Smartphone-based Sensor Data Collection". *CEUR Workshop Proceedings*.
- Li, C. et al. (2025). "Towards Visual-Inertial Integration: Multi-Modal Collaboration-based Video Stabilization". *IEEE ICDCS 2025*.
- Zhang, K. & Zhang, M. (2023). "Point feature correction based rolling shutter modeling for EKF-based visual-inertial odometry". *Measurement Science and Technology*.
- Restrepo-Arias, J.F. et al. (2023). "RipSetCocoaCNCH12: Labeled Dataset for Ripeness Stage Detection of Cocoa Pods". *Data*, 8(7), 112.
- Han, F. et al. (2021). "Video Stabilization for Camera Shoot in Mobile Devices via Inertial-Visual State Tracking". *IEEE Transactions on Mobile Computing*.
- OrangeYolo — [Citrus counting with OrangeSort and OrangeYolo]. *Computers and Electronics in Agriculture*.
- Coffee cherry YOLOv8 — Sampling protocol for coffee cherry counting with smartphones. *Precision Agriculture*.
- Strawberry longitudinal dataset — Kirk et al. "LabFruits Dataset". *University of Lincoln*.
- Pear dataset — YOLOv5s-FP for pear detection. *Computers and Electronics in Agriculture*.
- Open Camera Documentation. https://opencamera.sourceforge.io/help.html
- Gyroflow Documentation. https://docs.gyroflow.xyz/
- Sensor Logger. https://www.tszheichoi.com/sensorlogger
