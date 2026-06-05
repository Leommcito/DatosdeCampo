<!--
  ═══════════════════════════════════════════════════════════════
  SYNC IMPACT REPORT — v0.0.0 → v1.0.0
  ═══════════════════════════════════════════════════════════════
  Version change: 0.0.0 (template) → 1.0.0 (initial ratification)
  
  Modified principles:
    - [PLACEHOLDER] → I. Investigación Basada en Evidencia
    - [PLACEHOLDER] → II. Trazabilidad Bibliográfica Integral (NON-NEGOTIABLE)
    - [PLACEHOLDER] → III. Reproducibilidad y Documentación Exhaustiva
    - [PLACEHOLDER] → IV. Rigor en la Captura de Datos
    - [PLACEHOLDER] → V. Validación Cuantitativa
  
  Added sections:
    - Stack Tecnológico y Dependencias
    - Flujo de Trabajo y Ciclo de Investigación
    - Gobernanza (completa con control de cambios)
  
  Removed sections: N/A (initial version)
  
  Templates requiring updates:
    - .specify/templates/plan-template.md ⚠ pending
    - .specify/templates/spec-template.md ⚠ pending
    - .specify/templates/tasks-template.md ⚠ pending
  
  Follow-up TODOs: N/A
  ═══════════════════════════════════════════════════════════════
-->
# Protocolo de Captura Manual con Smartphone para Detección YOLO
y Tracking MOT en Huertos Densos de Mandarinas — Constitución

## Core Principles

### I. Investigación Basada en Evidencia

Toda decisión técnica dentro del proyecto —ya sea un parámetro de captura,
una herramienta seleccionada, un paso del pipeline o una verificación de
campo— DEBE estar respaldada por al menos una referencia bibliográfica
revisada por pares o documentación técnica verificable.

Ningún parámetro, paso del protocolo o selección de herramienta puede
incorporarse sin una justificación citada explícitamente.

**Rationale**: La contribución central de esta tesis es documentar y medir
cuantitativamente el impacto de las decisiones de captura. Cada elección
debe poder rastrearse hasta la evidencia que la respalda, cerrando el gap
actual en la literatura agrícola donde ningún paper documenta cómo captura.

### II. Trazabilidad Bibliográfica Integral (NON-NEGOTIABLE)

Cada elemento del proyecto —paso del pipeline, parámetro de captura,
verificación, decisión técnica o modificación futura— DEBE ser trazable
hasta al menos una referencia bibliográfica registrada en la Tabla Maestra
(`Tabla-Maestra-Papers.md`).

Reglas obligatorias:

1. **ID único**: Cada referencia en la Tabla Maestra DEBE tener un ID
   canónico en formato `PXX` (ej: `P01`, `P25`, `P43`).

2. **Metadatos completos**: Cada entrada DEBE incluir: título, autores,
   año, publicación, resumen, DOI/link, contexto en el proyecto, nivel de
   importancia y los pasos del proyecto que justifica.

3. **Citas con ID**: Toda mención a un paper en cualquier documento del
   proyecto DEBE usar el formato `[PXX]`. Está PROHIBIDO citar un paper
   que no esté registrado en la Tabla Maestra.

4. **Modificaciones**: Cualquier cambio, adición o eliminación de un paso,
   parámetro o verificación REQUIERE:
   a) Agregar los papers que justifican el cambio a la Tabla Maestra
   b) Actualizar la columna "Justifica a" con la nueva etapa
   c) Actualizar la sección de Trazabilidad de la Tabla Maestra

5. **Decisiones experimentales**: Si no existe un paper que respalde una
   decisión, debe documentarse como:
   `[Decisión experimental — sin respaldo bibliográfico directo]`
   y marcarse para validación futura.

**Rationale**: Este principio garantiza que cualquier persona que lea la
tesis pueda seguir la cadena: Decisión → Paper → DOI → Verificación.
Elimina las decisiones "porque sí" o "por sentido común" sin evidencia.

### III. Reproducibilidad y Documentación Exhaustiva

Todo protocolo, configuración y procedimiento DEBE estar documentado con
el detalle suficiente para que otro investigador pueda replicarlo
exactamente sin necesidad de adivinar parámetros.

Requisitos específicos:

- Todos los parámetros de captura DEBEN estar explícitamente declarados:
  ISO, shutter speed, resolución, FPS, bitrate, codec, estado de AF lock,
  AE lock, WB lock, Camera2 API.
- Las especificaciones de hardware DEBEN registrarse: modelo de smartphone,
  versión de SO, modelo de gimbal, apps con números de versión.
- Las condiciones ambientales DEBEN documentarse por sesión de captura:
  clima, hora, temperatura, condiciones de luz, viento.
- La nomenclatura de archivos DEBE seguir el formato establecido:
  `YYYY-MM-DD_hilera-XX_condiciones.mp4`.

**Rationale**: La falta de reproducibilidad es el gap principal que esta
tesis busca cerrar. Los papers actuales no documentan configuración;
este protocolo debe ser el estándar contra el cual se comparen futuros
trabajos.

### IV. Rigor en la Captura de Datos

La captura en campo DEBE seguir el protocolo documentado sin desviaciones.
Cada sesión de captura es un experimento científico, no una grabación
informal.

Reglas obligatorias:

- Antes de cada grabación: verificar AF Lock 🔒, AE Lock 🔒, WB Lock 🔒.
- IMU DEBE registrarse simultáneamente a 100 Hz (giroscopio + acelerómetro)
  mediante Sensor Logger o equivalente.
- OIS (Optical Image Stabilization) DEBE estar desactivado si se usa
  Gyroflow para estabilización post-captura.
- Cada grabación DEBE registrar en cuaderno: número de hilera, hora
  exacta, condiciones de luz y cualquier anomalía observada.
- Distancia al dosel: 0.5-1.5 m. Ángulo: 0-30° hacia arriba.
- Velocidad de caminata: ~0.5-1 m/s constante.
- Sin zoom digital. Sin cambios de ángulo bruscos.

**Rationale**: Un dataset capturado con parámetros inconsistentes produce
métricas de detección y tracking no atribuibles a factores controlados.
El rigor en captura es condición necesaria para la validez del experimento.

### V. Validación Cuantitativa

Toda decisión DEBE ser evaluable mediante métricas objetivas. No se
aceptan validaciones puramente cualitativas o visuales.

Métricas obligatorias:

- **Detección**: mAP@0.5, mAP@0.5:0.95, Precision, Recall
- **Tracking**: MOTA, HOTA, DetA, AssA, IDF1, #ID switches
- **Calidad de video**: % frames borrosos (Laplacian variance < umbral),
  ratio de frames útiles

El experimento A/B (Protocolo vs Cámara Nativa) es el mecanismo primario
de validación. Los resultados DEBEN reportarse con comparación cuantitativa
entre ambos grupos, no con observación cualitativa.

**Rationale**: La tesis no solo propone un protocolo — demuestra que
funciona midiendo su impacto. Sin métricas, no hay contribución validable.

## Stack Tecnológico y Dependencias

| Capa | Tecnología | Justificación |
|------|-----------|---------------|
| **Dispositivo de captura** | Smartphone Android con Camera2 API FULL/LEVEL_3 | Acceso a controles manuales (ISO, shutter, AF/AE/WB lock) |
| **App de captura** | Open Camera (GPLv3, gratuita, open-source) | Única app gratuita con bloqueo simultáneo AF+AE+WB + control manual completo |
| **Logging IMU** | Sensor Logger (100 Hz, giroscopio + acelerómetro) | Validada en investigación (Choi, CEUR 2024), compatible con Gyroflow |
| **Estabilización (HW)** | Gimbal mecánico 3-axis (DJI Osmo Mobile, Zhiyun Smooth) | Gašparović: gimbal mejora 6x estabilidad vs handheld |
| **Estabilización (SW)** | Gyroflow (open-source, IMU-based) | 8.9k stars GitHub, corrige rolling shutter + distorsión sin warpear |
| **Detección** | YOLO (v9/v11 o variantes) | State-of-the-art en detección de frutos, balance velocidad-precisión |
| **Tracking** | CoTracker3 / ByteTrack / SORT | Evaluación comparativa: CoTracker3 mejor HOTA (42.63%) y AssA (55.97%) |
| **Post-procesamiento** | FFmpeg + (opcional) NAFNet / DeblurGAN-v2 | Extracción de frames, deblurring si es necesario |
| **Evaluación** | TrackEval (MOTChallenge metrics) | Estándar en la literatura para evaluación de tracking |

## Flujo de Trabajo y Ciclo de Investigación

Cada ciclo de investigación en el proyecto DEBE seguir estos pasos:

1. **Identificar** la pregunta de investigación o decisión técnica necesaria
2. **Buscar** en la literatura (Elicit, Semantic Scholar, web) evidencia
   que respalde la decisión
3. **Registrar** los papers encontrados en la Tabla Maestra con metadatos
   completos (título, autores, año, DOI, resumen)
4. **Clasificar** cada paper con nivel de importancia y vincularlo al/los
   pasos del proyecto que justifica
5. **Documentar** la decisión en el archivo correspondiente usando el ID
   canónico `[PXX]`
6. **Validar** en campo si la decisión involucra captura de datos
7. **Medir** métricas cuantitativas y actualizar la documentación
8. **Actualizar** la sección de Trazabilidad en la Tabla Maestra
9. **Verificar** que no haya referencias sin ID ni IDs sin entrada completa

## Gobernanza

### Supremacía

Esta Constitución prevalece sobre cualquier otra práctica, guía o
costumbre del proyecto. Toda modificación debe cumplir con sus principios.

### Control de Cambios con Trazabilidad

Toda modificación al pipeline, metodología, parámetros o verificaciones
REQUIERE:

1. **Identificar** el/los papers que justifican el cambio (ID `[PXX]`)
2. **Verificar** que cada paper está completo en la Tabla Maestra
   (todos los campos llenos, importancia asignada, pasos vinculados)
3. **Actualizar** el documento modificado usando los IDs canónicos
4. **Actualizar** la sección "Trazabilidad" de la Tabla Maestra
5. **Propagar** los cambios a las plantillas dependientes si aplica

### Política de Versionado

| Versión | Cambio |
|---------|--------|
| **MAJOR** | Eliminación o redefinición de principios existentes |
| **MINOR** | Adición de nuevos principios o secciones |
| **PATCH** | Clarificaciones, ajustes de redacción, correcciones |

### Revisión de Cumplimiento

Toda incorporación de cambios al proyecto DEBE verificar:

- [ ] Cada decisión técnica tiene al menos un paper que la respalda
- [ ] Todas las referencias usan IDs canónicos `[PXX]`
- [ ] La Tabla Maestra está completa y actualizada
- [ ] No hay decisiones "por sentido común" sin documentar
- [ ] Los niveles de importancia están asignados y justificados

### Excepciones

Única excepción permitida: Decisiones puramente logísticas que no afectan
la calidad del dataset ni la reproducibilidad científica (ej: "llevar power
bank", "cargar el gimbal al 100%"). Estas no requieren respaldo
bibliográfico pero DEBEN estar documentadas como logísticas.

---

**Version**: 1.0.0 | **Ratified**: 2026-06-05 | **Last Amended**: 2026-06-05
