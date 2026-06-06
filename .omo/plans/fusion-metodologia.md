# Plan de Trabajo: Fusión de Investigaciones en Documento Único "Metodologia_final.md"

## TL;DR

> **Quick Summary**: Fusionar 6+ archivos de investigación (~1.500 líneas) en un solo documento académico "Metodologia_final.md" con formato de tesis/protocolo, preservando el 100% del contenido y convirtiendo el sistema de citas [PXX] a formato APA (Autor, Año).
>
> **Deliverables**:
> - `Metodologia_final.md` — Documento único integrado con estructura: Marco Teórico → Estado del Arte → Metodología (P1-P4) → Discusión → Conclusiones → Referencias
> - Trazabilidad de citas preservada mediante tabla de mapeo [PXX]→APA
> - Notas al pie de las anotaciones HTML de P3
>
> **Estimated Effort**: Large (~1.500+ líneas de contenido denso para reorganizar)
> **Parallel Execution**: YES — 4 waves, max 4 concurrent tasks
> **Critical Path**: T2 (mapeo citas) → T6-T10 (capítulos metodología) → T11-T12 (discusión + conclusiones) → T14 (QA final)

---

## Context

### Original Request
Unir todos los archivos de investigación metodológica en un solo documento "Metodologia_final.md" con estándar académico, sin omitir ni inventar contenido, siguiendo una estructura de tesis/protocolo.

### Archivos Fuente a Fusionar

| # | Archivo | Líneas | Contenido principal |
|---|---|---|---|
| 1 | `CONTEXTO-INVESTIGACION.md` | 108 | Contexto general, objetivos, problemas, preguntas de investigación, stack tecnológico |
| 2 | `Metodologia final/Investigacion-P1-Software-Captura.md` | 441 | App de cámara, bloqueo de sensores, evidencia cuantitativa (14+ papers) |
| 3 | `Metodologia final/Investigacion-P2-IMU-Telemetria.md` | 332 | Registro IMU, estabilización, OIS OFF, contradicciones |
| 4 | `Metodologia final/Investigacion-P3-Protocolo-Caminata-REVISADO-v2.md` | 472 | Protocolo caminata, 6 parámetros, contradicciones de 8 agentes (21+ papers) |
| 5 | `Metodologia final/Investigacion-P4-Seleccion-Parcelas.md` | 179 | Selección de parcelas con NDVI Sentinel-2 y SUR |
| 6 | `README.md` | ~150 | Pipeline 7 etapas, tabla de parámetros, experimento A/B (solo esencial) |
| 7 | `Tabla-Maestra-Papers.md` | 429 | **138 referencias** con IDs [PXX] para mapeo a APA |
| 8 | `.specify/memory/constitution.md` | 227 | 5 principios rectores del proyecto |

### Decisiones del Usuario

| Decisión | Opción elegida | Implicancia |
|---|---|---|
| **Estructura** | Tesis/Protocolo: Marco Teórico → Estado del Arte → Metodología → Discusión → Conclusiones | Define la arquitectura del documento |
| **Formato de citas** | Solo APA (Autor, Año) — sin [PXX] inline | Requiere mapeo completo [PXX]→APA de 138 referencias |
| **Contradicciones** | Dentro de cada sub-capítulo (P1, P2, P3) | Cada P tiene su propia sección de evidencia contradictoria |
| **Constitución** | Incluir como sub-sección "Principios Rectores" en Marco Teórico | Sección 1.4 del documento |
| **Anotaciones HTML P3** | Como notas al pie visibles | 9+ anotaciones convertidas a notas al pie numeradas |
| **README** | Solo lo esencial | Extraer pipeline, parámetros y experimento A/B |

### Metis Review — Riesgos Identificados

| # | Riesgo | Severidad | Mitigación en el plan |
|---|---|---|---|
| R1 | **Error en conversión de 138 citas** [PXX]→APA | 🔴 Crítico | T2: Construir tabla de mapeo COMPLETA antes de escribir; verificar cada cita |
| R2 | **Duplicación de contenido** entre archivos | 🟠 Alto | T14: Deduplicación con referencias cruzadas ("ver Sección X.X") |
| R3 | **Inconsistencia interna** (recomendación original vs contradictoria) | 🟠 Alto | Presentar como: original → evidencia contradictoria → decisión final |
| R4 | **Autores faltantes** en Tabla Maestra ("—") para citas APA | 🟠 Alto | T3: Identificar y marcar; usar título entre comillas como alternativa |
| R5 | **IDs no existentes** (P123, P126) referenciados en texto | 🟠 Alto | T3: Marcar con advertencia en nota al pie |
| R6 | **P4 ya usa APA** — los demás no | 🟡 Medio | Usar P4 como plantilla de estilo |
| R7 | **Anotaciones HTML** pueden perderse en la fusión | 🟡 Medio | T9: Convertir a notas al pie visibles |
| R8 | **Principio II (trazabilidad)** se pierde al eliminar [PXX] | 🔴 Crítico | Incluir tabla de mapeo [PXX]→APA como apéndice de trazabilidad |

---

## Work Objectives

### Core Objective
Producir un documento metodológico único "Metodologia_final.md" que integre el 100% del contenido de las 4 investigaciones (P1-P4) más el contexto del proyecto, con formato académico presentable a autoridades, citado en APA y estructurado como tesis/protocolo.

### Concrete Deliverables
- `Metodologia_final.md` — Documento completo en la raíz del proyecto
- Estructura de capítulos: Marco Teórico, Estado del Arte, Metodología (P1-P4), Discusión, Conclusiones, Referencias
- Sistema de citas convertido: todos los [PXX] reemplazados por (Autor, Año)
- Notas al pie para las 9+ anotaciones HTML de P3
- Tabla de trazabilidad [PXX]→APA como apéndice
- Marcado de IDs no existentes (P123, P126) con advertencia

### Definition of Done
- [ ] Todas las líneas de los 6+ archivos fuente están representadas en el documento final
- [ ] Todas las citas [PXX] convertidas a formato APA (Autor, Año)
- [ ] Ningún contenido cuantitativo (%, métricas, fórmulas) se ha perdido o alterado
- [ ] Las anotaciones HTML de P3 son notas al pie visibles
- [ ] La tabla de trazabilidad [PXX]→APA existe como apéndice
- [ ] Los IDs P123 y P126 tienen advertencia de "no verificado en bibliografía"
- [ ] Formato uniforme en todo el documento (tablas, referencias cruzadas, estilo)
- [ ] Sin contenido inventado o agregado más allá de los archivos fuente

### Must Have
- Preservación del 100% del contenido de los archivos fuente
- Conversión completa [PXX] → APA (Autor, Año) con tabla de trazabilidad
- Estructura: Marco Teórico → Estado del Arte → Metodología (P1-P4) → Discusión → Conclusiones → Referencias
- Notas al pie para todas las anotaciones HTML de P3
- Principios rectores de la constitución en Marco Teórico
- Contradicciones documentadas dentro de cada sub-capítulo

### Must NOT Have
- Contenido nuevo inventado o agregado que no esté en los archivos fuente
- Eliminación de evidencia contradictoria o matices
- "Limpieza" o simplificación del lenguaje académico original
- Nombres de autores inventados para papers marcados con "—"
- Eliminación de métricas cuantitativas o valores numéricos

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — Toda la verificación es ejecutada por el agente usando Bash y grep.

### QA Policy
Cada tarea incluye escenarios de verificación específicos. Evidencia guardada en `.omo/evidence/`.

### Verification Commands Clave
```bash
# 1. Verificar que cada [PXX] citado en fuente existe en el documento final
grep -oP '\(.*?,\s*\d{4}\)' Metodologia_final.md | sort -u

# 2. Verificar métricas clave preservadas
Select-String -Path "Metodologia_final.md" -Pattern "85%"
Select-String -Path "Metodologia_final.md" -Pattern "MSE 1.57"
Select-String -Path "Metodologia_final.md" -Pattern "74% menor MAE"
Select-String -Path "Metodologia_final.md" -Pattern "100 Hz"
Select-String -Path "Metodologia_final.md" -Pattern "MOTA 0.682"

# 3. Verificar que no hay [PXX] sin convertir
Select-String -Path "Metodologia_final.md" -Pattern "\[P\d+\]"

# 4. Verificar referencias de P4 preservadas
Select-String -Path "Metodologia_final.md" -Pattern "Ali, A., Imran"
Select-String -Path "Metodologia_final.md" -Pattern "Wulfsohn, D."

# 5. Verificar notas al pie de anotaciones HTML
Select-String -Path "Metodologia_final.md" -Pattern "\[^1\]"
```

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Preparación — 4 tareas paralelas):
├── T1: Lectura e inventario de contenido fuente [quick]
├── T2: Construcción de tabla de mapeo [PXX]→APA [quick]
├── T3: Identificación de citas problemáticas [quick]
└── T4: Extracción de contenido esencial del README [quick]

Wave 2 (Redacción de capítulos — 6 tareas paralelas):
├── T5: Redacción Marco Teórico (Cap. 1) [writing]
├── T6: Redacción Estado del Arte (Cap. 2) [writing]
├── T7: Redacción P1 — Software de Captura (3.1) [writing]
├── T8: Redacción P2 — IMU y Telemetría (3.2) [writing]
├── T9: Redacción P3 — Protocolo de Caminata (3.3) [writing]
└── T10: Redacción P4 — Selección de Parcelas (3.4) + Pipeline + Parámetros [writing]

Wave 3 (Integración — 3 tareas secuenciales):
├── T11: Redacción Discusión (Cap. 4) [writing]
├── T12: Redacción Conclusiones (Cap. 5) [writing]
└── T13: Compilación de lista de referencias APA [writing]

Wave FINAL (Verificación — 4 tareas paralelas):
├── T14: QA completo de contenido y citas [unspecified-high]
├── T15: Verificación de trazabilidad y notas al pie [unspecified-high]
├── T16: Formato final y consistencia visual [writing]
└── T17: Validación con grep de métricas clave [quick]

--- Revisión del usuario → Ajustes → Aprobación final ---
```

### Critical Path
T2 → T7→T8→T9→T10 → T11 → T12 → T13 → T14+T15+T16+T17 → User Review

### Dependency Matrix
- T1: — blocks T5-T10
- T2: — blocks T7-T10, T13
- T3: — blocks T11 (discusión sobre limitaciones)
- T4: — blocks T5, T10
- T5-T10: blocks T11-T12
- T11: T5-T10 blocks T13
- T12: T11 blocks T13
- T13: T2, T11, T12 blocks T14-T17
- T14-T17: T13 blocks user review

---

## TODOs

> **NOTA IMPORTANTE**: Cada tarea debe LEER los archivos fuente completos ANTES de comenzar a escribir. NO confiar en resúmenes o memoria del contexto.
> **Formato**: Etiquetas con números simples (`1.`, `2.`, etc.) — NO usar `T1.`, `Task 1.`.
> **Citas**: Reemplazar cada `[PXX]` por su equivalente APA `(Autor, Año)` usando la tabla de mapeo de T2.

### Wave 1 — Preparación y Mapeo de Citas (4 tareas paralelas)

- [ ] 1. **Lectura e Inventario de Contenido Fuente**

  **What to do**:
  - Leer COMPLETAMENTE cada archivo fuente y construir un inventario estructurado:
    - `CONTEXTO-INVESTIGACION.md` — Identificar: objetivo general, 18 problemas, 3 preguntas de investigación, stack tecnológico, papers actuales
    - `Metodologia final/Investigacion-P1-Software-Captura.md` — Identificar: 14+ papers, tabla de evidencia cuantitativa, comparativa apps, gap confirmado
    - `Metodologia final/Investigacion-P2-IMU-Telemetria.md` — Identificar: papers de estabilización, sampling rate, OIS OFF, contradicciones
    - `Metodologia final/Investigacion-P3-Protocolo-Caminata-REVISADO-v2.md` — Identificar: 6 parámetros, tabla de evidencia por parámetro, 21+ papers contradictorios (P110-P130), anotaciones HTML, apéndice A
    - `Metodologia final/Investigacion-P4-Seleccion-Parcelas.md` — Identificar: estado del arte, metodología 4 pasos, limitaciones, referencias en APA
    - `README.md` — Identificar: pipeline 7 etapas, tabla de parámetros de captura, experimento A/B, referencias rápidas
    - `.specify/memory/constitution.md` — Identificar: 5 principios rectores
  - Documentar: qué contenido va a qué capítulo del documento destino
  - Detectar y registrar solapamientos entre archivos (contenido duplicado)

  **Must NOT do**:
  - No comenzar a escribir aún — solo inventariar
  - No resumir ni omitir secciones

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Tarea de lectura y catalogación, no de escritura creativa
  - **Skills**: None needed (lectura de archivos + organización)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4)
  - **Blocks**: Tasks 5-10
  - **Blocked By**: None (can start immediately)

  **References**:
  - All source files in root directory and `Metodologia final/` folder

  **Acceptance Criteria**:
  - [ ] Inventario estructurado creado con mapeo: fuente → capítulo destino
  - [ ] Solapamientos detectados y documentados
  - [ ] Número de [PXX] únicos por archivo registrado

  **QA Scenarios**:
  ```
  Scenario: Verificar que todos los archivos fuente fueron leídos
    Tool: Bash
    Steps:
      1. ls Metodologia final/ — verificar que existen los 4 archivos .md
      2. ls *.md — verificar CONTEXTO-INVESTIGACION.md y README.md
      3. Get-ChildItem -Path ".specify/memory/constitution.md" — verificar constitución
    Expected Result: Los 8 archivos existen y son legibles
    Evidence: .omo/evidence/task-1-file-inventory.txt
  ```

- [ ] 2. **Construcción de Tabla de Mapeo [PXX] → APA**

  **What to do**:
  - Leer `Tabla-Maestra-Papers.md` COMPLETAMENTE (429 líneas)
  - Extraer CADA referencia [PXX] con su metadata:
    - ID [PXX]
    - Autores (completos o "—")
    - Año
    - Título
    - Publicación / Conferencia
    - DOI / URL
  - Construir tabla estructurada con:
    - Columna 1: [PXX]
    - Columna 2: Cita APA generada: `(Apellido et al., Año)` o `(Título, Año)` si autor es "—"
    - Columna 3: Cita APA completa para lista de referencias
    - Columna 4: Notas (incompleto, no verificado, etc.)
  - **Reglas de conversión APA**:
    - Si autor tiene "—": usar título del paper entre comillas: `("Título del Paper", Año)`
    - Si autor completo: `(Apellido et al., Año)` para 3+ autores, `(Apellido y Apellido, Año)` para 2, `(Apellido, Año)` para 1
    - Si no hay año: usar `(s.f.)` — "sin fecha"
  - Incluir TODOS los 138+ IDs [PXX] de la Tabla Maestra
  - **CRÍTICO**: Marcar P123 y P126 como "NO VERIFICADO: ID no encontrado en bibliografía"

  **Must NOT do**:
  - No inventar autores donde hay "—"
  - No omitir ningún [PXX]

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Tarea estructurada de extracción y formateo de datos
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4)
  - **Blocks**: Tasks 7-10, 13
  - **Blocked By**: None (can start immediately)

  **References**:
  - `Tabla-Maestra-Papers.md` — fuente de datos para todas las referencias

  **Acceptance Criteria**:
  - [ ] Tabla de mapeo con TODOS los [PXX] de la Tabla Maestra
  - [ ] Cada entrada tiene: [PXX] → APA inline → APA full reference
  - [ ] P123 y P126 marcados como no verificados
  - [ ] Papers con autor "—" tienen cita por título
  - [ ] Tabla guardada como referencia para tareas de escritura

  **QA Scenarios**:
  ```
  Scenario: Verificar cobertura de la tabla de mapeo
    Tool: Bash
    Steps:
      1. Extraer todos los [PXX] únicos de la tabla
      2. Comparar contra [PXX] en Tabla-Maestra-Papers.md
      3. Verificar que P123 y P126 están marcados
    Expected Result: 100% de cobertura. P123/P126 con advertencia.
    Evidence: .omo/evidence/task-2-citation-map.txt
  ```

- [ ] 3. **Identificación de Citas Problemáticas**

  **What to do**:
  - Revisar la tabla de mapeo de T2 e identificar:
    - IDs marcados como "NO EXISTE EN BIBLIOGRAFÍA" (P123, P126 según P3)
    - Autores con "—" que requieren cita por título
    - IDs referenciados en texto pero sin entrada completa en Tabla Maestra
    - Cualquier inconsistencia entre referencias en texto vs Tabla Maestra
  - Documentar cada caso problemático con:
    - ID
    - Dónde aparece en los archivos fuente
    - Naturaleza del problema
    - Solución propuesta (cita por título, nota al pie, etc.)
  - Servirá como guía para el escritor de cada capítulo

  **Must NOT do**:
  - No modificar los archivos fuente
  - No resolver las citas aún — solo documentar

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Identificación de problemas, tarea estructurada
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4)
  - **Blocks**: Tasks 11-12 (discusión sobre limitaciones)
  - **Blocked By**: Task 2 (necesita la tabla de mapeo)

  **References**:
  - Output de Task 2 — tabla de mapeo
  - `Metodologia final/Investigacion-P3-Protocolo-Caminata-REVISADO-v2.md` — donde aparecen P123, P126

  **Acceptance Criteria**:
  - [ ] Lista completa de citas problemáticas
  - [ ] Solución documentada para cada caso
  - [ ] P123 y P126 con advertencia explícita

  **QA Scenarios**:
  ```
  Scenario: Verificar documentación de problemas
    Tool: Bash
    Steps:
      1. Verificar que P123 está en la lista de problemas
      2. Verificar que P126 está en la lista de problemas
      3. Verificar que papers con autor "—" están documentados
    Expected Result: Todos los casos problemáticos documentados
    Evidence: .omo/evidence/task-3-problematic-citations.txt
  ```

- [ ] 4. **Extracción de Contenido Esencial del README**

  **What to do**:
  - Leer `README.md` completamente
  - Extraer SOLO el contenido que es relevante para el documento metodológico:
    - **Pipeline de Captura** (tabla de 7 etapas) → para Metodología 3.5
    - **Parámetros de Captura** (tabla con ISO, shutter, AF, AE, WB, bitrate, OIS) → para Metodología 3.6
    - **Parámetros en Campo** (distancia, velocidad, ángulo, horario, IMU) → para Metodología 3.6
    - **Experimento A/B** (Grupo A Protocolo vs Grupo B Control) → para Metodología 3.7
    - **Sistema de Trazabilidad** (Decisión → [PXX] → Tabla Maestra → DOI) → para Marco Teórico o apéndice
    - **Estado del Proyecto** → SINTETIZAR (no copiar completo)
  - Descartar: metadatos del proyecto (fecha, versión), estructura del repo, referencias rápidas (duplicadas de Tabla Maestra), enlaces a archivos

  **Must NOT do**:
  - No copiar el README completo
  - No extraer secciones que son solo navegación del repositorio

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Extracción selectiva de contenido
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3)
  - **Blocks**: Tasks 5, 10
  - **Blocked By**: None

  **References**:
  - `README.md` — archivo fuente

  **Acceptance Criteria**:
  - [ ] Pipeline 7 etapas extraído
  - [ ] Parámetros de captura extraídos
  - [ ] Experimento A/B extraído
  - [ ] Sistema de trazabilidad documentado

  **QA Scenarios**:
  ```
  Scenario: Verificar extracción correcta
    Tool: Bash
    Steps:
      1. Verificar que contiene "Pipeline de Captura (7 Etapas)"
      2. Verificar que contiene "ISO 200 fijo"
      3. Verificar que contiene "Experimento A/B"
    Expected Result: Contenido esencial presente
    Evidence: .omo/evidence/task-4-readme-extraction.txt
  ```

### Wave 2 — Redacción de Capítulos (6 tareas paralelas, dependen de Wave 1)

> Cada tarea de redacción debe:
> 1. Leer los archivos fuente relevantes COMPLETAMENTE
> 2. Usar la tabla de mapeo de T2 para convertir TODAS las citas [PXX] a APA
> 3. Preservar el 100% del contenido (no resumir, no omitir, no inventar)
> 4. Seguir el estilo académico de P4 como modelo
> 5. Incluir referencias cruzadas a otras secciones cuando haya solapamiento

- [ ] 5. **Redacción — Marco Teórico (Capítulo 1)**

  **What to do**:
  - Escribir sección 1.1 **Objetivo General** desde `CONTEXTO-INVESTIGACION.md`
  - Escribir sección 1.2 **Problemas a Mitigar** desde `CONTEXTO-INVESTIGACION.md` (tabla de 18 problemas con riesgos)
  - Escribir sección 1.3 **Preguntas de Investigación** desde `CONTEXTO-INVESTIGACION.md` (P1, P2, P3)
  - Escribir sección 1.4 **Principios Rectores** desde `.specify/memory/constitution.md` (resumir los 5 principios)
  - Escribir sección 1.5 **Stack Tecnológico Objetivo** desde `CONTEXTO-INVESTIGACION.md`
  - Convertir TODAS las citas [PXX] a APA usando la tabla de T2

  **Must NOT do**:
  - No agregar contenido nuevo
  - No omitir ninguno de los 18 problemas
  - No omitir ninguna pregunta de investigación

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Redacción académica de sección introductoria
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 6-10)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11 (Discusión)
  - **Blocked By**: Task 1 (inventario), Task 4 (extracción README)

  **References**:
  - `CONTEXTO-INVESTIGACION.md` (líneas 1-108)
  - `README.md` (stack tecnológico)
  - `.specify/memory/constitution.md` (5 principios)

  **Acceptance Criteria**:
  - [ ] Marco Teórico completo con 5 secciones
  - [ ] 18 problemas documentados con su nivel de riesgo
  - [ ] 3 preguntas de investigación presentadas
  - [ ] 5 principios rectores incluidos
  - [ ] Stack tecnológico documentado
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario: Verificar contenido del Marco Teórico
    Tool: Bash
    Steps:
      1. grep "Objetivo General" Metodologia_final.md
      2. grep "Stack Tecnológico" Metodologia_final.md
      3. grep "Principios Rectores" Metodologia_final.md
      4. grep "Preguntas de Investigación" Metodologia_final.md
    Expected Result: Las 5 secciones existen
    Evidence: .omo/evidence/task-5-marco-teorico.txt
  ```

- [ ] 6. **Redacción — Estado del Arte (Capítulo 2)**

  **What to do**:
  - Sintetizar el "estado del arte" de CADA investigación en secciones:
    - 2.1 **Software de Captura en Agricultura**: desde P1 ("Lo que dice la literatura", papers Elicit + Semantic Scholar)
    - 2.2 **IMU y Estabilización en Video Agrícola**: desde P2 (resultados Elicit, papers de estabilización, sampling rate)
    - 2.3 **Protocolos de Captura en Campo**: desde P3 (tablas de evidencia por parámetro, papers originales P69-P78)
    - 2.4 **Selección de Parcelas y Muestreo**: desde P4 sección 3 (Estado del Arte: MAS, estratificado, SUR)
    - 2.5 **Gap de Investigación Confirmado**: síntesis de los gaps de cada P + CONTEXTO-INVESTIGACION.md sección "Papers Actuales"
  - Convertir TODAS las citas [PXX] a APA
  - Usar referencias cruzadas ("ver Sección 3.X") en lugar de repetir contenido

  **Must NOT do**:
  - No incluir las contradicciones aquí (van en cada sub-capítulo de Metodología)
  - No incluir las decisiones del protocolo (van en Metodología)
  - No duplicar contenido que estará en Metodología

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Síntesis de literatura académica
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5, 7-10)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11 (Discusión)
  - **Blocked By**: Task 1 (inventario)

  **References**:
  - P1: "Lo que dice la literatura" secciones
  - P2: "Resultados de Elicit" y papers
  - P3: Tablas de evidencia por parámetro
  - P4: Sección 3 (Estado del Arte)
  - CONTEXTO-INVESTIGACION.md: Papers actuales

  **Acceptance Criteria**:
  - [ ] 5 secciones del Estado del Arte completas
  - [ ] Gap de investigación claramente formulado
  - [ ] Sin [PXX] sin convertir
  - [ ] Referencias cruzadas a Metodología donde corresponda

  **QA Scenarios**:
  ```
  Scenario: Verificar Estado del Arte
    Tool: Bash
    Steps:
      1. grep "Gap de Investigación" Metodologia_final.md
      2. grep "Software de Captura" Metodologia_final.md
      3. grep "IMU y Estabilización" Metodologia_final.md
    Expected Result: Secciones del Estado del Arte presentes
    Evidence: .omo/evidence/task-6-estado-arte.txt
  ```

- [ ] 7. **Redacción — P1: Software de Captura y Bloqueo de Sensores (Sección 3.1)**

  **What to do**:
  - Leer COMPLETAMENTE `Metodologia final/Investigacion-P1-Software-Captura.md` (441 líneas)
  - Escribir sub-capítulo 3.1 con TODO el contenido:
    - Introducción: problema de captura con app nativa
    - Lo que dice la literatura (papers Elicit + Semantic Scholar)
    - Tabla de evidencia cuantitativa (Paso 1)
    - Tabla resumen cruzada Elicit + Semantic Scholar
    - Nueva evidencia encontrada (papers P57-P63, P95-P99)
    - Análisis de apps (Open Camera, Filmic Pro, MCPro24fps, Blackmagic)
    - Gap confirmado para la tesis
    - Discusión: Nuevo paradigma de detección robusta (2024-2026)
    - Tabla resumen: Qué hacer vs Qué evitar
    - Nota sobre valores propuestos vs documentados
    - Limitación: Protocolo solo para Android
    - Evidencia contradictoria (sección propia dentro de 3.1)
  - Convertir TODAS las citas [PXX] a APA
  - Conservar TODAS las tablas, métricas, porcentajes, valores numéricos

  **Must NOT do**:
  - No omitir ningún paper, tabla o métrica
  - No eliminar la discusión sobre el nuevo paradigma de detección robusta
  - No eliminar la nota sobre valores propuestos vs documentados
  - No eliminar la limitación de Android

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Redacción de sub-capítulo metodológico denso
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5, 6, 8, 9, 10)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11
  - **Blocked By**: Task 1 (inventario), Task 2 (mapeo citas)

  **References**:
  - `Metodologia final/Investigacion-P1-Software-Captura.md` (completo)

  **Acceptance Criteria**:
  - [ ] Todo el contenido de P1 transferido
  - [ ] Tablas de evidencia cuantitativa preservadas
  - [ ] Comparativa de apps preservada
  - [ ] Gap y contribución original documentados
  - [ ] Limitación Android documentada
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario: Verificar contenido crítico de P1
    Tool: Bash
    Steps:
      1. grep "85% menos variación" Metodologia_final.md
      2. grep "MSE 1.57" Metodologia_final.md
      3. grep "74% menor MAE" Metodologia_final.md
      4. grep "Open Camera" Metodologia_final.md
      5. grep "Protocolo solo para Android" Metodologia_final.md
    Expected Result: Métricas clave y apps preservadas
    Evidence: .omo/evidence/task-7-p1-software.txt
  ```

- [ ] 8. **Redacción — P2: Registro de Telemetría IMU (Sección 3.2)**

  **What to do**:
  - Leer COMPLETAMENTE `Metodologia final/Investigacion-P2-IMU-Telemetria.md` (332 líneas)
  - Escribir sub-capítulo 3.2 con TODO el contenido:
    - Introducción: necesidad de registrar IMU durante captura
    - Resultados de Elicit (papers P11-P22)
    - Sampling rate IMU: 100 Hz es suficiente [P25]
    - Gyroflow: documentación técnica
    - OIS debe estar desactivado: [P64] DeepOIS, [P65] ISPRS
    - Video estabilizado vs fotos: [P66] MangoYOLO +22%
    - Motion blur + YOLO: [P68] Citrus GAN
    - Estabilización en agricultura: [P67]
    - Tabla resumen de evidencia
    - **Evidencia contradictoria (sección 3.2.X)**:
      - OIS debe estar OFF — Matiz importante (Qualcomm, Google Pixel, Apple, HyperOIS)
      - Frecuencia de muestreo IMU — 100 Hz suficiente PERO con límites
      - Gyroflow — Validado pero con limitaciones
      - Motion Blur + YOLO — El 86.4% es engañoso (degradación real 15-50%)
      - Video estabilizado > Fotos — La mejora no es por estabilización
      - IMU supera a óptica — Desactualizado (2014-2021)
      - Rolling Shutter Correction — Beneficio para geometría, NO para detección
      - Gap de la tesis — Reevaluación
    - Gap confirmado para la tesis
    - Tabla de progreso en justificación
  - Convertir TODAS las citas [PXX] a APA
  - Conservar TODOS los valores numéricos, porcentajes y métricas

  **Must NOT do**:
  - No omitir ninguna sección de contradicciones
  - No simplificar los matices de OIS
  - No eliminar la reevaluación del gap

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Redacción de sub-capítulo metodológico con contradicciones
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5, 6, 7, 9, 10)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11
  - **Blocked By**: Task 1, Task 2

  **References**:
  - `Metodologia final/Investigacion-P2-IMU-Telemetria.md` (completo)

  **Acceptance Criteria**:
  - [ ] Todo el contenido de P2 transferido
  - [ ] Sección de contradicciones completa (8 sub-secciones)
  - [ ] OIS OFF con matiz Qualcomm documentado
  - [ ] Degradación real de blur (15-50%) documentada
  - [ ] Gap reevaluado
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario: Verificar contenido crítico de P2
    Tool: Bash
    Steps:
      1. grep "100 Hz" Metodologia_final.md
      2. grep "DeepOIS\|50% peor\|OIS" Metodologia_final.md
      3. grep "86.4%" Metodologia_final.md
      4. grep "MangoYOLO" Metodologia_final.md
    Expected Result: Métricas clave preservadas
    Evidence: .omo/evidence/task-8-p2-imu.txt
  ```

- [ ] 9. **Redacción — P3: Protocolo de Caminata y Captura (Sección 3.3)**

  **What to do**:
  - Leer COMPLETAMENTE `Metodologia final/Investigacion-P3-Protocolo-Caminata-REVISADO-v2.md` (472+ líneas)
  - Escribir sub-capítulo 3.3 con TODO el contenido:
    - **Resumen de parámetros** (tabla con 6 parámetros, valores, respaldo, IDs, confianza)
    - **Evidencia detallada por parámetro** (6 sub-secciones, una por parámetro):
      - 3.3.1 Velocidad de Caminata (~1 m/s)
      - 3.3.2 Ángulo de Cámara (15-30° up)
      - 3.3.3 Distancia al Dosel (0.8-1.5 m)
      - 3.3.4 Horario e Iluminación (9-11AM/3-5PM)
      - 3.3.5 Motion Blur y Shutter Speed (1/60-1/120s)
      - 3.3.6 Anti-Doble Conteo y Tracking (ByteTrack + multi-view)
    - Para CADA parámetro: tabla de papers + conclusión
    - **CRÍTICO**: Después de cada parámetro, incluir su sub-sección de **evidencia contradictoria**:
      - 3.3.1b Contradicciones — Velocidad (Sanchez & Zhang: 2.5 m/s viable)
      - 3.3.2b Contradicciones — Ángulo (0° horizontal = 88.3%, 45° superior)
      - 3.3.3b Contradicciones — Distancia (0.5-1.2m para mandarinas)
      - 3.3.4b Contradicciones — Horario (noche con LED > día, nublado cuestionado)
      - 3.3.5b Contradicciones — Shutter (20µs con LED, burst photography)
      - 3.3.6b Contradicciones — Tracking (AgriSORT/OC-SORT > ByteTrack)
    - **Tabla de evidencia cruzada** (Decisión vs Respaldo)
    - **Gap confirmado** (incluyendo gap ampliado por contradicciones)
    - **Parámetros de captura finales**: tabla con valores originales + tabla con valores actualizados según contradicciones
    - **Apéndice A**: Tabla de Trazabilidad Bibliográfica Completa (P27-P130)
  - **Convertir ANOTACIONES HTML a notas al pie**:
    - Buscar TODAS las `<!-- ANOTACIÓN: ... -->` en el archivo fuente
    - Cada una debe convertirse en nota al pie visible: `[^N]` al final del párrafo relevante y `[^N]: Texto de la anotación` al final del capítulo
    - Anotaciones identificadas:
      - Velocidad ~0.5-1.0 m/s : SÍNTESIS PROPIA
      - Ángulo 15-30° : SÍNTESIS PROPIA
      - Distancia 0.5-1.2m para mandarinas : EXTRAPOLACIÓN
      - Shutter 1/60-1/120s : INCONSISTENCIA INTERNA
      - Fórmula de blur : CORREGIDA
      - Regla 180° : SIN RESPALDO ACADÉMICO
      - Horario 9-11AM/3-5PM : CONTRADICCIÓN DOCUMENTADA (CORREGIDA)
      - Noche con LED para mandarinas : EXTRAPOLACIÓN MÚLTIPLE
      - AgriSORT/OC-SORT para mandarinas : SIN VALIDACIÓN EN MANDARINAS
      - Parámetro "Trayectoria" con ID "—" : SIN REFERENCIA DIRECTA
  - Convertir TODAS las citas [PXX] a APA

  **Must NOT do**:
  - No omitir NINGUNA de las anotaciones HTML — cada una debe ser nota al pie
  - No omitir ninguna contradicción de los 8 agentes paralelos
  - No eliminar el Apéndice A de trazabilidad bibliográfica
  - No eliminar la tabla de valores actualizados según contradicciones
  - No simplificar las advertencias de extrapolación (EXTRAPOLACIÓN, SÍNTESIS PROPIA, etc.)

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Sub-capítulo más extenso y complejo, con anotaciones y contradicciones
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5, 6, 7, 8, 10)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11
  - **Blocked By**: Task 1, Task 2

  **References**:
  - `Metodologia final/Investigacion-P3-Protocolo-Caminata-REVISADO-v2.md` (completo)

  **Acceptance Criteria**:
  - [ ] Todo el contenido de P3 transferido (472+ líneas)
  - [ ] 6 parámetros con sus tablas de evidencia
  - [ ] 6 sub-secciones de contradicciones (una por parámetro)
  - [ ] TODAS las anotaciones HTML convertidas a notas al pie visibles
  - [ ] Apéndice A de trazabilidad bibliográfica preservado
  - [ ] Tabla de valores actualizados incluida
  - [ ] Gap ampliado documentado
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario 1: Verificar contenido crítico de P3
    Tool: Bash
    Steps:
      1. grep "0.5-1.2 m" Metodologia_final.md
      2. grep "AgriSORT\|ByteTrack" Metodologia_final.md
      3. grep "noche con LED" Metodologia_final.md
      4. grep "EXTRAPOLACIÓN\|SÍNTESIS PROPIA" Metodologia_final.md
    Expected Result: Contenido crítico preservado
    Evidence: .omo/evidence/task-9-p3-caminata-1.txt

  Scenario 2: Verificar notas al pie de anotaciones HTML
    Tool: Bash
    Steps:
      1. grep "\[^1\]" Metodologia_final.md — buscar notas al pie
      2. grep "\[^2\]" Metodologia_final.md
      3. grep "SIN RESPALDO ACADÉMICO\|SIN REFERENCIA DIRECTA" Metodologia_final.md
    Expected Result: Notas al pie presentes para anotaciones clave
    Evidence: .omo/evidence/task-9-p3-caminata-2.txt
  ```

- [ ] 10. **Redacción — P4 + Pipeline + Parámetros (Secciones 3.4, 3.5, 3.6, 3.7)**

  **What to do**:
  - Sección **3.4 Selección de Parcelas para Muestreo**:
    - Leer COMPLETAMENTE `Metodologia final/Investigacion-P4-Seleccion-Parcelas.md` (179 líneas)
    - Escribir con TODO el contenido:
      - Introducción (importancia de la selección)
      - Área de Estudio y Datos Disponibles (4 parcelas Murcott, Sentinel-2)
      - Estado del Arte (MAS, estratificado, SUR, otros métodos)
      - Metodología (4 pasos: NDVI, SUR, caracterización, captura)
      - Discusión (elección NDVI vs NDRE, limitaciones)
      - Conclusión (tabla resumen: 2 parcelas × 3 hileras = 6 videos)
      - Referencias (YA en APA — preservar tal cual)
  - Sección **3.5 Pipeline de Captura**:
    - Desde README: tabla de 7 etapas (Pre-captura → Captura → Post-procesamiento → Entrenamiento)
  - Sección **3.6 Parámetros de Captura**:
    - Desde README: tabla de parámetros de cámara (ISO, shutter, AF, AE, WB, bitrate, OIS)
    - Desde README: tabla de parámetros en campo (distancia, velocidad, ángulo, horario, IMU)
  - Sección **3.7 Experimento A/B**:
    - Desde README: Grupo A (Protocolo) vs Grupo B (Control), métricas (mAP, MOTA, IDF1)
  - Convertir TODAS las citas [PXX] a APA usando tabla de T2
  - P4 ya tiene referencias en APA — preservar formato

  **Must NOT do**:
  - No modificar las referencias de P4 (ya están en APA correcto)
  - No omitir ninguna limitación de P4
  - No omitir la tabla resumen final de P4

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Integración de contenido metodológico y de pipeline
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5, 6, 7, 8, 9)
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 11
  - **Blocked By**: Task 1, Task 2, Task 4 (extracción README)

  **References**:
  - `Metodologia final/Investigacion-P4-Seleccion-Parcelas.md` (completo)
  - `README.md` (pipeline, parámetros, experimento A/B)

  **Acceptance Criteria**:
  - [ ] P4 completo con sus 6 secciones internas
  - [ ] Pipeline 7 etapas incluido
  - [ ] Parámetros de captura incluidos (cámara + campo)
  - [ ] Experimento A/B incluido
  - [ ] Referencias de P4 preservadas en APA
  - [ ] Limitaciones documentadas
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario 1: Verificar contenido de P4
    Tool: Bash
    Steps:
      1. grep "Murcott" Metodologia_final.md
      2. grep "Sentinel-2" Metodologia_final.md
      3. grep "6 videos\|2 parcelas.*3 hileras" Metodologia_final.md
      4. grep "Ali, A., Imran" Metodologia_final.md
    Expected Result: Contenido de P4 y referencias preservados
    Evidence: .omo/evidence/task-10-p4-parcelas.txt

  Scenario 2: Verificar Pipeline y Parámetros
    Tool: Bash
    Steps:
      1. grep "Pipeline de Captura\|7 Etapas" Metodologia_final.md
      2. grep "ISO.*200\|Shutter.*1/100" Metodologia_final.md
      3. grep "Experimento A/B\|Grupo A.*Protocolo\|Grupo B.*Control" Metodologia_final.md
    Expected Result: Pipeline, parámetros y experimento A/B presentes
    Evidence: .omo/evidence/task-10-pipeline-params.txt
  ```

---

### Wave 3 — Integración (3 tareas secuenciales)

- [ ] 11. **Redacción — Discusión (Capítulo 4)**

  **What to do**:
  - Escribir capítulo 4 **Discusión** integrando:
    - **4.1 Evidencia Contradictoria Consolidada**: Síntesis de las contradicciones de P1, P2 y P3, destacando los patrones comunes:
      - La velocidad no es tan crítica como se pensaba (modelos toleran blur)
      - La iluminación controlada (noche+LED) supera consistentemente al día
      - Los trackers específicos para agricultura (AgriSORT) superan a ByteTrack
      - El paradigma de detección robusta (2024-2026) no invalida el control de captura
    - **4.2 Discusión sobre Valores Propuestos vs Documentados**: desde P1 ("Nota sobre valores propuestos vs valores documentados en papers") — explicar que ISO 100-200 y shutter 1/60-1/120s son decisiones de ingeniería informadas por la literatura, no valores extraídos directamente
    - **4.3 Limitaciones de la Metodología**:
      - Desde P4 (sección 5.2): número reducido de parcelas, resolución Sentinel-2, solo 2 parcelas, variedad única
      - Desde P1: limitación a Android (Camera2 API)
      - Desde P2: Nyx del gap (posible resultado nulo por robustez de YOLO)
      - Desde P3: extrapolaciones marcadas (mandarinas no estudiadas directamente)
    - **4.4 Implicaciones para el Experimento A/B**: cómo las contradicciones afectan el diseño experimental
  - Usar referencias cruzadas a las secciones de Metodología
  - Convertir TODAS las citas [PXX] a APA

  **Must NOT do**:
  - No repetir textualmente el contenido de los sub-capítulos (usar referencias cruzadas)
  - No eliminar matices o contradicciones

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Síntesis integradora de alto nivel
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (after Wave 2)
  - **Blocks**: Task 12
  - **Blocked By**: Tasks 5-10 (todos los capítulos de Metodología)

  **References**:
  - Todos los sub-capítulos de Metodología (T7-T10)
  - P1: "Discusión: Nuevo paradigma de detección robusta"
  - P2: "Contradicciones y Matices", "Gap de la Tesis — Reevaluación"
  - P3: Tablas de evidencia contradictoria, "Parámetros de captura finales"
  - P4: Sección 5 "Discusión"

  **Acceptance Criteria**:
  - [ ] 4 secciones de Discusión completas
  - [ ] Evidencia contradictoria consolidada con referencias cruzadas
  - [ ] Limitaciones documentadas de todas las fuentes
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario: Verificar contenido de Discusión
    Tool: Bash
    Steps:
      1. grep "Discusión" Metodologia_final.md
      2. grep "Limitaciones" Metodologia_final.md
      3. grep "Android\|Camera2 API" Metodologia_final.md
    Expected Result: Capítulo de Discusión completo
    Evidence: .omo/evidence/task-11-discusion.txt
  ```

- [ ] 12. **Redacción — Conclusiones (Capítulo 5)**

  **What to do**:
  - Escribir capítulo 5 **Conclusiones** integrando:
    - **5.1 Gap de Investigación Confirmado**: Sintetizar los gaps de P1 ("ningún paper documenta app+config+IMU+pipeline"), P2 ("no existe IMU→YOLO mAP en agricultura"), P3 ("no existe comparación velocidad×ángulo×distancia combinados"), P4 (documentado como metodología reproducible)
    - **5.2 Contribución Original**: De cada P — documentar el pipeline completo con métricas cuantitativas (P1), medir impacto IMU preprocessing en YOLO mAP (P2), medir interacción de parámetros combinados (P3), metodología de selección de parcelas con NDVI (P4)
    - **5.3 Valores Finales del Protocolo**: Tabla consolidada con los valores recomendados para la validación en campo, incluyendo:
      - Valores originales (con respaldo bibliográfico directo)
      - Valores actualizados según evidencia contradictoria
      - Nivel de confianza de cada valor
    - **5.4 Trabajo Futuro**: Sugerencias para validación experimental

  **Must NOT do**:
  - No agregar conclusiones que no se deriven del contenido de los archivos fuente
  - No inventar trabajo futuro

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Síntesis final del documento
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (after Task 11)
  - **Blocks**: Task 13
  - **Blocked By**: Task 11

  **References**:
  - P1: "Gap confirmado para la tesis", "Contribución original"
  - P2: "Gap confirmado para la tesis", "Progreso en justificación"
  - P3: "Gap confirmado para la tesis", "Gap ampliado por contradicciones", "Parámetros de captura finales"
  - P4: Sección 6 "Conclusión"

  **Acceptance Criteria**:
  - [ ] Gap confirmado sintetizado de todas las fuentes
  - [ ] Contribución original documentada
  - [ ] Tabla de valores finales del protocolo incluida
  - [ ] Sin [PXX] sin convertir

  **QA Scenarios**:
  ```
  Scenario: Verificar Conclusiones
    Tool: Bash
    Steps:
      1. grep "Conclusiones" Metodologia_final.md
      2. grep "Contribución Original\|Gap" Metodologia_final.md
      3. grep "Valores Finales del Protocolo" Metodologia_final.md
    Expected Result: Capítulo de Conclusiones completo
    Evidence: .omo/evidence/task-12-conclusiones.txt
  ```

- [ ] 13. **Compilación de Lista de Referencias APA (Capítulo 6)**

  **What to do**:
  - Compilar la lista completa de referencias en formato APA a partir de:
    - Tabla de mapeo de T2 (todas las referencias [PXX])
    - Referencias de P4 (ya en APA, preservar exactamente)
    - Documentación técnica (GitHub, webs, etc.) con el formato: `Autor/Empresa. (Año). Título. URL`
  - Formatear cada entrada según APA 7ª edición:
    - `Apellido, A., Apellido, B., & Apellido, C. (Año). Título del artículo. *Nombre de la Revista*, *Volumen*(Número), Páginas. DOI`
    - Para papers con autor "—": `Título del artículo. (Año). *Nombre de la Revista*, *Volumen*(Número), Páginas. DOI`
    - Para documentación técnica: `Nombre. (Año). *Título*. URL`
  - Ordenar alfabéticamente por primer autor
  - Incluir TODAS las referencias (P1-P130, D1-D8, P95-P99)

  **Must NOT do**:
  - No inventar datos faltantes (autores, páginas, etc.)
  - No omitir ninguna referencia citada en el texto

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Formateo de referencias bibliográficas
  - **Skills**: None needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (after Tasks 11, 12)
  - **Blocks**: Tasks 14-17 (QA)
  - **Blocked By**: Task 2 (tabla de mapeo), Tasks 11, 12

  **References**:
  - Output de Task 2 — tabla de mapeo [PXX]→APA
  - `Tabla-Maestra-Papers.md` — fuente de datos crudos
  - `Metodologia final/Investigacion-P4-Seleccion-Parcelas.md` — sección 7 (referencias en APA)

  **Acceptance Criteria**:
  - [ ] Lista de referencias completa (138+ entradas)
  - [ ] Formato APA 7ª edición consistente
  - [ ] Orden alfabético
  - [ ] Referencias de P4 preservadas exactamente
  - [ ] Papers con autor "—" formateados por título

  **QA Scenarios**:
  ```
  Scenario: Verificar lista de referencias
    Tool: Bash
    Steps:
      1. grep "^.*(20[0-9][0-9])\." Metodologia_final.md | head -20 — verificar formato APA
      2. grep "Ali, A., Imran" Metodologia_final.md — verificar P4 preservado
      3. grep -c "Apellido\|Autor\|—" Metodologia_final.md — contar autores
    Expected Result: Referencias en APA correcto
    Evidence: .omo/evidence/task-13-referencias.txt
  ```

---

## Final Verification Wave (Wave FINAL — 4 tareas paralelas)

- [ ] F1. **QA Completo de Contenido y Citas** — `unspecified-high`

  **What to do**:
  1. Verificar que NO hay contenido faltante comparando con los archivos fuente:
     - Línea por línea de CONTEXTO-INVESTIGACION.md está en el documento destino
     - Cada sección de P1, P2, P3, P4 está representada
  2. Verificar que NO hay `[PXX]` sin convertir (deben ser todos APA)
  3. Verificar que cada cita APA en el texto tiene su entrada en la lista de referencias
  4. Verificar que no hay "huérfanos" — referencias en la lista que no se citan en el texto

  **Verification**:
  ```bash
  # Verificar que no hay [PXX] residuales
  Select-String -Path "Metodologia_final.md" -Pattern "\[P\d+\]" | Select-Object -First 5

  # Verificar métricas clave
  Select-String -Path "Metodologia_final.md" -Pattern "85%"
  Select-String -Path "Metodologia_final.md" -Pattern "MSE 1.57"
  Select-String -Path "Metodologia_final.md" -Pattern "74%"
  Select-String -Path "Metodologia_final.md" -Pattern "100 Hz"
  Select-String -Path "Metodologia_final.md" -Pattern "MOTA 0.682"
  Select-String -Path "Metodologia_final.md" -Pattern "27.2%"
  ```
  Output: `Content [N/N preserved] | Citations [N/N converted] | Metrics [N/N verified] | VERDICT`

- [ ] F2. **Verificación de Trazabilidad y Notas al Pie** — `unspecified-high`

  **What to do**:
  1. Verificar que TODAS las anotaciones HTML de P3 se convirtieron a notas al pie visibles
  2. Verificar que P123 y P126 tienen advertencia de "no verificado"
  3. Verificar que los papers con autor "—" se manejaron correctamente (cita por título)
  4. Verificar que la tabla de trazabilidad [PXX]→APA existe como apéndice

  **Verification**:
  ```bash
  # Verificar notas al pie
  Select-String -Path "Metodologia_final.md" -Pattern "\[\^" | Measure-Object | Select-Object Count

  # Verificar advertencias P123/P126
  Select-String -Path "Metodologia_final.md" -Pattern "P123\|P126"

  # Verificar que no hay <!-- anotaciones HTML sin convertir
  Select-String -Path "Metodologia_final.md" -Pattern "<!-- ANOTACIÓN"
  ```
  Output: `HTML annotations [N/N as footnotes] | P123/P126 [FLAGGED] | "—" authors [N handled] | VERDICT`

- [ ] F3. **Formato Final y Consistencia Visual** — `writing`

  **What to do**:
  1. Verificar consistencia de formato en TODO el documento:
     - Mismo nivel de encabezados (# ## ### ####)
     - Tablas con el mismo estilo (alineación, separadores)
     - Notas al pie numeradas secuencialmente [^1], [^2], etc.
     - Referencias cruzadas correctas (ver Sección X.X apunta a secciones existentes)
  2. Verificar que no hay:
     - Líneas en blanco excesivas
     - Código fuente de los archivos originales que no debería estar (como `<!-- ANOTACIÓN:`)
     - Saltos de sección inconsistentes
  3. Verificar que el documento es válido Markdown

  **Verification**: Leer visualmente el documento completo y verificar formato uniforme
  Output: `Sections [N] | Footnotes [N sequential] | Headers [consistent] | Tables [uniform] | VERDICT`

- [ ] F4. **Validación con Grep de Métricas Clave** — `quick`

  **What to do**:
  - Ejecutar comandos grep para verificar que métricas específicas NO se perdieron:
  ```bash
  # Métricas de P1
  Select-String -Path "Metodologia_final.md" -Pattern "85% menos variación"  # P57
  Select-String -Path "Metodologia_final.md" -Pattern "2.7x más consistente" # P58
  Select-String -Path "Metodologia_final.md" -Pattern "4x menos datos"       # P59
  Select-String -Path "Metodologia_final.md" -Pattern "74% menor MAE"        # P62
  Select-String -Path "Metodologia_final.md" -Pattern "F1.*0.82.*0.13"       # P63

  # Métricas de P2
  Select-String -Path "Metodologia_final.md" -Pattern "32% mejor estabilización" # P11
  Select-String -Path "Metodologia_final.md" -Pattern "50% peor\|1.038\|0.688"   # P64
  Select-String -Path "Metodologia_final.md" -Pattern "\+22%\|62.3%\|40.2%"       # P66

  # Métricas de P3
  Select-String -Path "Metodologia_final.md" -Pattern "mAP 93.69%"   # P73
  Select-String -Path "Metodologia_final.md" -Pattern "MOTA 0.682"    # P74

  # Métricas de P4
  Select-String -Path "Metodologia_final.md" -Pattern "6 videos\|30 minutos" # P4
  ```
  Output: `P1 metrics [N/N] | P2 metrics [N/N] | P3 metrics [N/N] | P4 metrics [N/N] | VERDICT`

> **Proceso**: F1-F4 se ejecutan en PARALELO. Todos deben devolver VERDICT: PASS para que el documento se considere completo. Si algún FALL, se corrige y se re-ejecuta.

---

## Commit Strategy

- **1**: `docs: fusionar 4 investigaciones metodologicas en Metodologia_final.md`
  - Files: `Metodologia_final.md`
  - Pre-commit: Verificar que el archivo existe y tiene contenido significativo

---

## Success Criteria

### Final Checklist
- [ ] Contenido de los 6+ archivos fuente preservado al 100%
- [ ] 138+ referencias convertidas de [PXX] a APA
- [ ] Tabla de trazabilidad [PXX]→APA incluida como apéndice
- [ ] P123 y P126 marcados con advertencia de "no verificado"
- [ ] Autores faltantes ("—") manejados con citas por título
- [ ] Anotaciones HTML de P3 convertidas a notas al pie visibles
- [ ] Principios rectores de la constitución incluidos en Marco Teórico
- [ ] Contradicciones documentadas dentro de cada sub-capítulo de Metodología
- [ ] Contenido del README extraído solo lo esencial (pipeline, parámetros, experimento A/B)
- [ ] Sin contenido inventado — solo reorganización del material fuente
- [ ] Sin [PXX] residuales sin convertir a APA
- [ ] Métricas cuantitativas clave verificadas (85%, MSE 1.57, 74%, 100 Hz, MOTA 0.682, etc.)
- [ ] Referencias de P4 preservadas exactamente como están (ya en APA)
- [ ] Formato uniforme en tablas, encabezados y estilo en todo el documento
- [ ] Documento listo para presentación a autoridades académicas
