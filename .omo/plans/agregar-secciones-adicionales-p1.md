# Agregar Secciones Adicionales al P1 — Do's & Don'ts + Valores del Protocolo + Limitación iOS

## TL;DR

> **Quick Summary**: Agregar 3 secciones al final del documento `P1/Investigacion-P1-Software-Captura.md`:
> 1. **Tabla "Qué hacer vs Qué evitar"** (Do's and Don'ts basada en la bibliografía)
> 2. **Nota sobre diferencia entre valores de papers y valores del protocolo** (por qué ISO/shutter del protocolo difieren de los papers)
> 3. **Limitación iOS vs Android** (por qué el protocolo solo funciona en Android)
>
> **Deliverables**: Modificaciones al archivo `P1/Investigacion-P1-Software-Captura.md` (agregar ~60-80 líneas al final)
>
> **Estimated Effort**: Quick (< 30 min)
> **Parallel Execution**: NO — secuencial

---

## Context

El documento `P1/Investigacion-P1-Software-Captura.md` actualmente termina con la sección "Discusión: Nuevo paradigma de detección robusta" y un párrafo final. No tiene una sección práctica de resumen ni discute explícitamente:
- Por qué los valores propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120) son diferentes a los valores documentados en los papers (ISO=25, 1/400s, etc.)
- Que el protocolo es Android-only por limitaciones de iOS (Camera2 API vs AVFoundation)
- Una tabla consolidada de "qué hacer" vs "qué evitar" para el investigador que lea el documento

---

## Work Objectives

### Core Objective
Agregar 3 secciones al final del P1 para mejorar su completitud y utilidad práctica.

### Must Have
- La tabla "Qué hacer vs Qué evitar" debe incluir TODAS las decisiones del P1 con sus referencias [PXX]
- La nota sobre valores del protocolo debe explicar por qué ISO=100 y shutter 1/60-1/120 no son valores extraídos de papers sino decisiones del protocolo
- La limitación iOS debe citar correctamente [P62] como fuente
- El contenido existente NO debe modificarse (solo agregar al final)

### Must NOT Have
- No modificar las secciones existentes del documento
- No cambiar valores propuestos del protocolo
- No agregar información de P2/P3/P4

---

## Verification Strategy

> ZERO HUMAN INTERVENTION
> Cada adición se verificará con grep para confirmar que el texto nuevo está presente y el texto antiguo no fue modificado.

---

## TODOs

- [ ] 1. **Agregar tabla "Qué hacer vs Qué evitar" al final del documento**

  **What to do**:
  Insertar DESPUÉS de la línea 390 (última línea del documento actual), ANTES del final del archivo:

  ```
  
  ---

  ## Resumen práctico: Qué hacer vs Qué evitar en la captura

  | ✅ Hacer (Recomendado) | ❌ Evitar (No recomendado) | Respaldo bibliográfico |
  |---|---|---|
  | **Bloquear AE/AF/WB** (exposición, enfoque, balance de blancos) | Dejar parámetros en automático (causa fluctuación 13-14%) | [P57], [P58], [P96] |
  | **Fijar ISO en 200** (100 solo si hay suficiente luz) | ISO automático (varía entre frames, degrada consistencia) | [P99], [P55] |
  | **Fijar shutter en 1/100s** (rango 1/60-1/120 según luz) | Shutter automático (cambia exposición frame a frame) | [P99], [P75] |
  | **Usar tone mapping lineal** (Camera2 API, CONTRAST_CURVE) | Tone mapping automático (transformaciones no lineales irreversibles) | [P62] |
  | **Usar Open Camera** (gratis, open-source, Camera2 API) | App nativa del fabricante (no permite bloquear parámetros) | [P99], [D1] |
  | **Iluminación LED fija** (4000K, distancia constante) | Flash de cámara o luz solar directa (glare, sombras) | [P99], [P63] |
  | **Deshabilitar OIS** si usas Gyroflow (interfiere con IMU) | OIS activo con estabilización basada en giroscopio | [P64], [P65] |
  | **Mantener distancia constante al dosel** (0.5-1.5m) | Cambiar distancia entre tomas (afecta resolución del fruto) | [P28] |
  | **Procesar en RAW si es posible** (7.1% más precisión) | Confiar en el ISP por defecto (pierde información útil) | [P97] |
  | **Optimizar ISP para detección** (no para ojo humano) | Usar pipeline ISP default (sub-óptimo para YOLO, 28% menos mAP) | [P98] |
  ```

  **Verification**:
  - `grep -c "Qué hacer vs Qué evitar" P1/Investigacion-P1-Software-Captura.md` → debe dar 1
  - `grep -c "Bloquear AE/AF/WB" P1/Investigacion-P1-Software-Captura.md` → debe dar 1

  **Commit**: YES (grupo con tareas 2 y 3)
  - Message: `feat(p1): agregar tabla resumen Que hacer vs Que evitar en captura`
  - Files: `P1/Investigacion-P1-Software-Captura.md`

- [ ] 2. **Agregar nota sobre diferencia entre valores de papers y valores del protocolo**

  **What to do**:
  Insertar DESPUÉS de la tabla del punto 1, con el siguiente texto:

  ```
  
  ### Nota sobre los valores propuestos vs valores documentados en papers

  Los valores específicos propuestos por el protocolo (ISO 100-200, shutter 1/60-1/120s) **no son valores extraídos directamente de un paper**, sino decisiones del protocolo basadas en el principio de "usar el valor mínimo práctico para condiciones de campo". Los papers consultados usaron valores distintos según sus condiciones específicas:

  | Valor documentado en paper | Paper | Condiciones de ese paper |
  |---|---|---|
  | ISO=25, shutter=1/400s | [P55] Rice GMC | iPhone 8, laboratorio, tabla de calibración Spyder Checkr 24, sin luz solar directa |
  | ISO=200, shutter=1/100s | [P99] Open Camera | Redmi Note 7 Pro, iluminación LED controlada 4000K, 50cm distancia, interior |
  | Exposición ~250 µs (~1/4000s) | [P49] Vineyard | Cámara industrial Basler Ace, flash xenon sincronizado, montaje en vehículo |
  | Exposición 200 µs (~1/5000s) | [P57] LEDs | Cámara industrial con LED overcurrent-driven 6×, exterior con flash sincronizado |

  El protocolo propone **ISO 100-200** porque ISO=200 está documentado [P99] como valor funcional en campo, e ISO=100 es el mínimo práctico en exteriores sin llegar a ISO=25 (que requiere condiciones controladas de laboratorio [P55]).

  El protocolo propone **shutter 1/60-1/120s** porque 1/100s está documentado [P99], y el rango es un compromiso entre: (a) un shutter lo suficientemente rápido para evitar motion blur al caminar (~8-16 px a 1 m/s), y (b) un shutter lo suficientemente lento para capturar suficiente luz sin flash en exteriores. La revisión de técnicas de deblurring [P75] recomienda ≥1/200s para walking shake, pero adoptar ese valor requeriría ISO más alto (más ruido digital) o iluminación activa adicional (como en [P57] y [P49]).

  > **Conclusión**: Los valores del protocolo son una decisión de ingeniería informada por la literatura, no un valor extraído directamente de un paper. El experimento A/B (Protocolo vs Cámara Nativa) validará si esta decisión es adecuada.
  ```

  **Verification**:
  - `grep -c "valores propuestos vs valores documentados" P1/Investigacion-P1-Software-Captura.md` → debe dar 1
  - `grep -c "decisión de ingeniería informada" P1/Investigacion-P1-Software-Captura.md` → debe dar 1

  **Commit**: YES (grupo con tarea 1)

- [ ] 3. **Agregar limitación iOS vs Android al final**

  **What to do**:
  Insertar DESPUÉS de la nota del punto 2, con el siguiente texto:

  ```
  
  ### Limitación: Protocolo solo para Android

  Es importante señalar que el presente protocolo de captura **solo es aplicable a dispositivos Android** que soporten Camera2 API. La razón es que iOS (AVFoundation) **no expone control sobre el tone mapping** de la cámara, según lo documentado por [P62]:

  > *"It is only possible to manually set the camera tone mapping to linear within the Android Camera 2 API. Such an option is not available in iOS. Although it is possible to capture RAW photos using iOS AVFoundation, the RAW capture mode is not possible for video recordings necessary for cPPG measurements."* — Xuan et al. (2023), Frontiers in Digital Health [P62]

  Esto implica que:
  - En **Android**: Se puede usar Camera2 API para configurar tone mapping lineal, bloquear AF/AE/WB, y controlar ISO/shutter manualmente. El protocolo es completamente aplicable.
  - En **iOS**: No es posible controlar el tone mapping en video. La cámara nativa de iOS aplica transformaciones no lineales irreversibles. Incluso usando apps de terceros, el control sobre el pipeline ISP es limitado.

  **Recomendación para iOS**: Si bien el protocolo completo no es replicable en iOS, se recomienda al menos:
  1. Bloquear AE/AF/WB si la app lo permite (algunas apps como Filmic Pro lo ofrecen)
  2. Usar la resolución más alta disponible y bitrate máximo
  3. Considerar que los resultados del experimento A/B pueden no ser directamente transferibles entre plataformas

  **Implicación para la reproducibilidad**: El protocolo está diseñado para Android con Camera2 API. Cualquier investigador que desee replicar el experimento debe usar un dispositivo Android compatible. Se recomienda verificar el soporte de Camera2 API antes de la captura (apps como "Camera2 API Probe" pueden verificarlo).
  ```

  **Verification**:
  - `grep -c "Protocolo solo para Android" P1/Investigacion-P1-Software-Captura.md` → debe dar 1
  - `grep -c "Camera2 API Probe" P1/Investigacion-P1-Software-Captura.md` → debe dar 1

  **Commit**: YES (grupo con tareas 1 y 2)

---

## Commit Strategy

- **1-3 (grupo)**: `feat(p1): agregar tabla resumen, nota valores protocolo, y limitacion iOS` — `P1/Investigacion-P1-Software-Captura.md`

---

## Success Criteria

### Final Checklist
- [ ] Tabla "Qué hacer vs Qué evitar" con 10 filas de recomendaciones
- [ ] Sección "Nota sobre los valores propuestos vs valores documentados en papers" con tabla comparativa de 4 papers
- [ ] Sección "Limitación: Protocolo solo para Android" con cita textual de [P62]
- [ ] Contenido existente del P1 intacto (no se modificaron secciones previas)
- [ ] Todas las referencias [PXX] existen en `P1/bibliografia/`
