# CONTEXTO DE INVESTIGACIÓN — Datos de Campo

## Objetivo General

Establecer un **protocolo de recolección de datos en campo** para grabar **videos manuales con smartphone** en **huertos densos de mandarinas**, asegurando que el material capturado sea óptimo para modelos de **detección YOLO** y **seguimiento MOT**.

El enfoque principal es **capturar el video de la forma más limpia posible desde el origen**, mitigando problemas físicos en el momento de la grabación (no en post-procesamiento computacional).

---

## Problemas a Mitigar Durante la Captura Manual

| Problema | Riesgo |
|---|---|
| Movimiento brusco de cámara (shake) | 🔴 Muy Alto |
| Desenfoque por movimiento (motion blur) | 🔴 Muy Alto |
| Cambios de altura/distancia al dosel | 🔴 Muy Alto |
| Cambios de ángulo e inclinación | 🔴 Muy Alto |
| Objetivo fuera del encuadre | 🔴 Alto |
| Oclusiones (personas, ramas, vehículos) | 🔴 Alto |
| Variaciones de iluminación (nubes, sombras) | 🔴 Alto |
| Autofoco inestable (focus hunting) | 🟠 Alto |
| Exposición incorrecta | 🟠 Alto |
| Velocidad inconsistente de movimiento | 🟠 Medio |
| Rotación de cámara (roll) | 🟠 Medio |
| Cambios de zoom digital | 🟠 Medio |
| Compresión excesiva del dispositivo | 🟠 Medio |
| Diferencias entre dispositivos | 🟡 Medio-Bajo |
| Distorsión de lente (gran angular) | 🟡 Bajo |
| Reflejos/flare solar | 🟡 Bajo |
| Ruido digital (poca luz) | 🟡 Bajo |
| Variaciones de balance de blancos (AWB) | 🟡 Bajo |

---

## Preguntas de Investigación (No Respondidas en los Papers Actuales)

### 1. Software de Captura y Bloqueo de Sensores

Investigar por qué **la cámara nativa en modo automático es perjudicial** para datasets de visión computacional en agricultura. Evaluar y documentar el uso de aplicaciones como:

- **Open Camera** — Bloqueo de autofoco (AF), exposición (ISO/shutter), balance de blancos (AWB)
- **Filmic Pro** — Control manual de parámetros de video
- Otras apps de cámara profesional para smartphone

**Respaldo requerido:** Papers que demuestren que el focus hunting, autoexposición y AWB automático degradan la calidad de datasets para detección/tracking.

### 2. Registro de Telemetría (IMU) en Tiempo Real

Necesidad de ejecutar aplicaciones como **Sensor Logger** en segundo plano durante la caminata por el huerto para registrar:

- **Giroscopio** (velocidad angular en X, Y, Z)
- **Acelerómetro** (aceleración lineal)
- **Magnetómetro** (orientación)

**Propósito:** Capturar la firma del movimiento humano para su uso obligatorio en post-producción (deblurring, estabilización, corrección de rolling shutter).

**Respaldo requerido:** Papers que usen datos IMU de smartphone para corrección de blur o mejora de calidad de video en entornos agrícolas o similares.

### 3. Diseño del Protocolo de Caminata y Captura

Metodologías documentadas sobre cómo debe caminar el operador:

- **Distancia recomendada** hacia el dosel (ej: 0.5m, 1m, 1.5m)
- **Ángulo de inclinación** de la cámara (ej: 0°, 15°, 30° hacia arriba)
- **Velocidad de desplazamiento** (ej: lento constante vs. variable)
- **Horarios óptimos** de grabación (luz difusa vs. luz directa)
- **Trayectoria** (zigzag, pasillo continuo, ambos lados de la fila)
- **Estrategia para evitar doble conteo** y oclusiones

**Respaldo requerido:** Papers de agricultura de precisión, robótica agrícola o visión computacional en campo que definan protocolos de captura.

---

## Papers Actuales en el Repositorio y su Relación con los Objetivos

| Archivo | Relevancia |
|---|---|
| `136670017.md` (NAFNet) | **Baja** — Restauración genérica de imágenes. No agricultura ni captura. |
| `AP-Geo-referenced-factor-graph-2026.md` | **Media** — SLAM + reconstrucción 3D de manzanas. Usa tractor/robot, no smartphone. Útil como referencia de pipeline de post-procesamiento. |
| `information-12-00495-v2.md` | **Baja** — Detección de flores con YOLO. No habla de captura. |
| `Orchard+Obstacle+D2-YOLO.md` | **Media** — Deblurring en果园 con GAN + YOLO. Robot sobre orugas. Solución post-captura. |
| `plants-14-03085-v2.md` | **Media** — Deblurring de cítricos con GAN liviana. Usan iPhone 13 solo para dataset. |
| `sindelar-0434272.md` | **Alta** — Único paper que usa giroscopio de smartphone para deblurring por handshake. Desactualizado (2014). |

**Conclusión:** Los papers actuales NO responden las preguntas de captura. Se necesita investigación adicional en la literatura.

---

## Stack Tecnológico Objetivo

- **Captura:** Smartphone (Android/iOS) con app de cámara profesional (Open Camera, Filmic Pro)
- **Telemetría:** Sensor Logger (IMU: giroscopio + acelerómetro)
- **Detección:** YOLO (v9, v11 o variantes)
- **Seguimiento:** CoTracker3 / ByteTrack / SORT
- **Post-procesamiento:** Deblurring (NAFNet, DeblurGAN-v2, AGG-DeblurGAN), SLAM (iSAM2), Bundle Adjustment
- **Estimación de rendimiento:** Reconstrucción 3D multiframe + factor-graph optimization

---

## Notas

- La prioridad es **respaldo bibliográfico** para cada decisión de captura
- El objetivo final es producir un dataset de video de alta calidad para modelos YOLO + MOT
- El contexto es un huerto de **mandarinas denso** (altaoclusión, follaje denso, frutospequeños)
- La captura es **manual** (operador caminando con smartphone), no robótica
