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

### Paper 10: Stanford — CNN + Exposure Bias (Google Research, 2018) — [P60] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Caída de precisión CNN** | **~20%** cuando hay sesgo de exposición |
| **Conclusión** | Exposición inconsistente degrada directamente la precisión de detección |

**Relevancia:** Evidencia directa de que AE Lock mejora la detección.

---

### Paper 11: Focus Hunting (CVPR, 2025) — [P61] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Focus hunting** | El lente oscila repetitivamente creando inestabilidad en el video |
| **Efectos** | Reduce nitidez, cambia el campo de visión (FoV) |
| **Reducción** | 18% menos FH con método DRL propuesto |

**Relevancia:** Documenta que el focus hunting es un problema real. Respalda AF Lock.

---

### Paper 12: Camera2 API para investigación (Nature/PMC, 2023) — [P62] 🟠 Alta

| Hallazgo | Valor |
|---|---|
| **Tone mapping automático** | Aplica transformaciones **no lineales irreversibles** |
| **Camera2 API** | Permite desactivar tone mapping, fijar WB y control manual total |
| **Conclusión** | Camera2 API es necesaria para investigación científica con smartphone |

**Relevancia:** Valida que Camera2 API es el estándar para captura científica. Respalda usar Open Camera.

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
| Exposición inconsistente degrada CNN | ~20% caída precisión | Stanford (2018) | [P60] |
| Focus hunting degrada calidad | Lente oscila, FoV cambia | CVPR (2025) | [P61] |
| Camera2 API necesario para control científico | Tone mapping irreversible en auto | Nature/PMC (2023) | [P62] |
| Luz no controlada destruye detección | F1 0.82 → 0.13 con glare | Kiwifruit (2020) | [P63] |

---

## Tabla resumen cruzada Elicit + Semantic Scholar

| Aspecto | Elicit | Semantic Scholar | Gap |
|---|---|---|---|
| Apps de cámara nombradas | ❌ Ninguna | ❌ Ninguna | **Nadie documenta qué app usó** |
| Parámetros de cámara (ISO, shutter, etc.) | ❌ No reportados | ⚠️ 1 paper (arroz) sí los reporta | Solo 1 paper en toda la literatura |
| Justificación de por qué fijar parámetros | ❌ No existe | ⚠️ 1 paper dice "to minimize lighting factors" | Justificación débil |
| Distancia al objetivo | ❌ No reportada | ✅ Varios papers: 0.3-1.5m, 8-15cm, 27.5cm | Hay datos pero no comparativos |
| Holder/soporte físico | ❌ No reportado | ✅ 1 paper (café) con holder + botones | Solo 1 paper |
| Integración IMU + cámara | ❌ No reportada | ✅ 1 paper (café) con IMU para blur detection | Solo 1 paper |
| Dispositivos específicos | ⚠️ Algunos (iPhone X, Xiaomi, Huawei) | ✅ Varios (iPhone 8, Galaxy S5, Redmi Note 7, etc.) | Complementario |
| Open Camera / Filmic Pro / MCPro24fps | ❌ No existen en papers agrícolas | ❌ No existen en papers agrícolas | **Gap confirmado — contribución de tu tesis** |

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

> **No existe un paper agrícola que documente qué app de cámara profesional se usó, con qué configuración y por qué.**

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
| [P60] | Stanford CNN | ~20% caída precisión con exposición variable |
| [P61] | CVPR 2025 | Focus hunting es un problema real |
| [P62] | Camera2 API | Control manual necesario para investigación |
| [P63] | Kiwifruit glare | F1 cae de 0.82 a 0.13 con luz no controlada |

**Gap que persiste:** Ninguno de estos papers usa ni compara apps de cámara específicas (Open Camera, Filmic Pro) ni documenta el flujo completo app + IMU + procesamiento.

**Tu contribución original:** Documentar y justificar todo el pipeline de captura (app + configuración + IMU + procesamiento) con métricas cuantitativas de impacto en YOLO.**
