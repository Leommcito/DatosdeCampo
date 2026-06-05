# Protocolo de Captura Manual con Smartphone para Detección YOLO y Tracking MOT en Huertos Densos de Mandarinas

**Tesis | Fecha de validación en campo:** 05/06/2026

---

## 📋 Descripción del Proyecto

Este proyecto de tesis establece un **protocolo de recolección de datos en campo** para grabar **videos manuales con smartphone** en **huertos densos de mandarinas**, optimizado para modelos de detección **YOLO** y seguimiento **MOT (Multiple Object Tracking)**.

### Problema que resuelve

Los papers académicos actuales en agricultura de precisión usan smartphones para capturar datos, pero **ninguno documenta cómo lo hace** — no dicen qué app usaron, qué configuración de cámara, a qué distancia, a qué velocidad. Esto hace que los experimentos no sean reproducibles y que los datasets sean de calidad subóptima.

### Contribución original

> **No existe un paper agrícola que:**
> 1. Nombre una app de captura específica (Open Camera, Filmic Pro)
> 2. Compare auto vs manual con métricas YOLO
> 3. Compare distancias al dosel con métricas de detección para smartphone
> 4. Compare walking speeds con métricas de tracking
>
> **Tu contribución original:** Documentar y medir cuantitativamente el impacto de estas decisiones en **mAP/MOTA** para video de mandarinas.

---

## 🏗️ Pipeline de Captura (7 Etapas)

```
PRE-CAPTURA → CAPTURA → POST-PROCESAMIENTO → ENTRENAMIENTO
```

| Etapa | Qué se hace | App/Equipo | Ref. clave |
|---|---|---|---|
| **1. App de Cámara** | Bloquear AF/AE/WB + ISO/shutter fijos | Open Camera (Camera2 API) | [P57][P58][P60] |
| **2. Estabilización** | Gimbal mecánico + Gyroflow (post) | DJI Osmo + Gyroflow | [P43][P11][P64] |
| **3. Logging IMU** | Giroscopio + acelerómetro 100 Hz | Sensor Logger | [P25][P23] |
| **4. Sincronización Video-IMU** | Frame-level sync | OpenCamera Sensors / Clap sync | [P24][D4] |
| **5. Calibración de Cámara** | Corrección de distorsión | OpenCV + Charuco | [P10][P03] |
| **6. Pre-procesamiento** | Estabilización + (opcional) deblurring | Gyroflow + FFmpeg | [P22][P26] |
| **7. Pipeline de Datos** | YOLO + ByteTrack/CoTracker3 | YOLO + TrackEval | [P28][P31][P34] |

---

## 📊 Tabla Maestra de Referencias

**Total: 74 referencias** (68 papers académicos + 6 documentación técnica)

### Por nivel de importancia

| Nivel | Cantidad | Propósito |
|---|---|---|
| 🔴 **Crítico** | 16 | Decisión central del pipeline |
| 🟠 **Alta** | 21 | Respalda decisiones técnicas |
| 🟡 **Media** | 18 | Contexto metodológico |
| 🟢 **Baja** | 13 | Referencia general |
| ⚪ **Informativa** | 6 | Documentación técnica |

### Papers más importantes

| ID | Paper | Hallazgo clave |
|---|---|---|
| [P25] | Fan et al. (2025) | **100 Hz suficiente** para walking |
| [P28] | Kuznetsova et al. (2020) | **Compara 4 distancias** 0.2-2.0m |
| [P43] | Gašparović | **Gimbal mejora 6x** estabilidad |
| [P57] | LEDs + fixed exposure (2021) | **85% menos** variación HSV con exposición fija |
| [P58] | Phenotyping manual vs auto (2018) | **MSE 1.57 vs 4.26** — manual 2.7x mejor |
| [P64] | DeepOIS (2021) | **OIS interfiere 50%** con giroscopio |
| [P40] | Kurtser (FNF) | Exposición fija mejora detección |

Ver archivo completo: [`Tabla-Maestra-Papers.md`](Tabla-Maestra-Papers.md)

---

## 📁 Estructura del Proyecto

| Archivo | Propósito |
|---|---|
| [`CONTEXTO-INVESTIGACION.md`](CONTEXTO-INVESTIGACION.md) | Marco general del proyecto, problemas, stack tecnológico |
| [`Metodologia-Captura.md`](Metodologia-Captura.md) | Protocolo completo paso a paso (429 líneas) |
| [`Pipeline-Captura-Recomendado.md`](Pipeline-Captura-Recomendado.md) | Versión sintética con decisiones y justificaciones |
| [`Tabla-Maestra-Papers.md`](Tabla-Maestra-Papers.md) | **74 referencias catalogadas con IDs, importancia y trazabilidad** |
| [`Investigacion-P1-Software-Captura.md`](Investigacion-P1-Software-Captura.md) | App de cámara y bloqueo de sensores |
| [`Investigacion-P2-IMU-Telemetria.md`](Investigacion-P2-IMU-Telemetria.md) | Registro IMU y estabilización |
| [`Investigacion-P3-Protocolo-Caminata.md`](Investigacion-P3-Protocolo-Caminata.md) | ⚠️ Pendiente de ejecutar en Elicit |
| [`Investigacion-Herramientas-Motores-Busqueda.md`](Investigacion-Herramientas-Motores-Busqueda.md) | Comparativa de herramientas de búsqueda académica |
| [`.specify/memory/constitution.md`](.specify/memory/constitution.md) | Constitución del proyecto v1.0.0 |

---

## 🧪 Parámetros de Captura

| Parámetro | Valor | Justificación |
|---|---|---|
| **App** | Open Camera (Camera2 API ON) | Única gratuita con AF/AE/WB Lock |
| **Resolución** | 4K (3840×2160) o 1080p | Píxeles por fruto pequeño |
| **FPS** | 30 | Suficiente para tracking |
| **ISO** | 100-200 fijo | Minimiza ruido digital [P57][P58] |
| **Shutter** | 1/60s o 1/120s fijo | Motion blur controlado [P57] |
| **AF** | 🔒 LOCK | Evita focus hunting [P61] |
| **AE** | 🔒 LOCK | Brillo constante [P58][P60] |
| **WB** | 🔒 LOCK | Color estable [P62] |
| **Bitrate** | 50 Mbps | Calidad constante |
| **OIS** | OFF | Interfiere con Gyroflow [P64][P65] |

### En campo

| Parámetro | Valor | Ref. |
|---|---|---|
| **Distancia al dosel** | 0.5 - 1.5 m | [P28][P37] |
| **Velocidad** | ~0.5 - 1 m/s constante | [P31][P27] |
| **Ángulo** | 0-30° hacia arriba | [P45][P39] |
| **Horario** | 8:30 AM+, evitar 12-14PM | [P30] |
| **IMU** | 100 Hz (gyro + accel) | [P25] |

---

## 📈 Estado del Proyecto

| Componente | Estado | Detalle |
|---|---|---|
| **Constitución v1.0.0** | ✅ Completado | 5 principios + trazabilidad bibliográfica |
| **P1 — App de Cámara** | ✅ Completado | 23 papers, justificación manual vs auto cerrada |
| **P2 — IMU/Telemetría** | ✅ Completado | 20+ papers, gap OIS OFF cerrado |
| **P3 — Protocolo Caminata** | ❌ Pendiente | Prompt listo para ejecutar en Elicit |
| **Pipeline** | ✅ Completado | 7 etapas con referencias y IDs |
| **Metodología** | ✅ Completado | 13 secciones, 12 metodologías similares |
| **Tabla Maestra** | ✅ Completado | 74 referencias con trazabilidad |
| **Validación en campo** | 🔜 Pendiente | 05/06/2026 |

---

## 🔗 Sistema de Trazabilidad (Constitución Principio II)

Cada decisión técnica está atada a un ID de paper:

```
Decisión → [PXX] → Tabla Maestra → DOI/URL → Verificable
```

Ejemplo:
```
AE Lock (exposición fija)
  → [P58] Phenotyping (Plant Methods, 2018)
    → MSE 1.57 manual vs 4.26 auto
    → Manual es 2.7x más consistente
```

---

## 🎯 Experimento A/B (validación)

| Grupo | Captura |
|---|---|
| **A (Protocolo)** | Siguiendo todos los pasos del pipeline |
| **B (Control)** | Cámara nativa en modo automático |
| **Métrica** | mAP@0.5, MOTA, IDF1, % frames borrosos |

---

## 📚 Referencias Rápidas por Etapa

| Paso | IDs de referencia |
|---|---|
| **Paso 1** — App de Cámara | [P40][P41][P49][P55][P57][P58][P59][P60][P61][P62][P63][D1] |
| **Paso 2** — Estabilización | [P11][P12][P13][P18][P22][P26][P43][P51][P64][P65][P66][P67][P68][D2][D5] |
| **Paso 3** — Logging IMU | [P23][P25][D3][D4] |
| **Paso 4** — Sincronización | [P23][P24][D4] |
| **Paso 5** — Calibración | [P03][P10][P47] |
| **Paso 6** — Pre-procesamiento | [P22][P26][P49][D2][D5] |
| **Paso 7** — Pipeline Datos | [P28][P31][P34][P35][P37][P47][P54][D6] |

---

*Documento generado el 05/06/2026. 74 referencias catalogadas con trazabilidad completa.*
