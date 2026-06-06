# Corrección de Justificaciones — ISO 100-200 y Shutter 1/60-1/120

## TL;DR

> **Quick Summary**: Corregir 3 archivos donde ISO 100-200 y shutter 1/60-1/120s están justificados con referencias bibliográficas incorrectas ([P57][P58][P40][P55] no respaldan esos valores específicos). La corrección usa [P99] como respaldo directo para ISO=200 y shutter=1/100s, y aclara que ISO=100 y shutter=1/60-1/120s son decisiones del protocolo, no valores extraídos de papers.

> **Deliverables**:
> - `README.md` — Corregir referencias de ISO y shutter (líneas 99-100)
> - `Pipeline-Captura-Recomendado.md` — Reemplazar tabla de justificación (líneas 212-213) y tabla de nivel de respaldo (líneas 227-228)
> - `P1/bibliografia/listado-referencias-P1.md` — Corregir tabla de trazabilidad (líneas 291-292)

> **Estimated Effort**: Quick
> **Parallel Execution**: NO — 3 tareas secuenciales (cada una edita un archivo diferente pero pueden hacerse en paralelo)

---

## Context

### Problema detectado

El análisis de consistencia reveló que los valores **ISO 100-200** y **shutter 1/60-1/120s** están justificados con referencias que NO respaldan esos valores específicos:

| Referencia actual | Lo que realmente dice | Problema |
|---|---|---|
| [P57] LEDs paper | Cámara industrial, exposición 200µs, ganancia baja. **NO** especifica ISO ni shutter para smartphone | ❌ No respalda el valor |
| [P58] Phenotyping | Canon DSLR, ISO automático. Compara manual vs auto pero no da valores | ❌ No respalda el valor |
| [P55] Rice GMC | ISO=**25**, shutter=**1/400s** | ❌ Valores muy diferentes a 100-200 y 1/60-1/120 |
| [P40] FNF paper | Exposición fija 20µs con flash. Principio general, no valores | ❌ No respalda el rango |

### Qué respaldo REAL existe

| Valor | Respaldo real | Fuente |
|---|---|---|
| ISO=200 | ✅ Documentado en Open Camera para fenotipado | [P99] |
| ISO=100 | ❌ **Sin respaldo bibliográfico** — decisión del protocolo | — |
| Shutter=1/100s | ✅ Documentado en Open Camera para fenotipado | [P99] |
| Shutter=1/60-1/120 | ⚠️ Rango basado en regla 180° (cine, no académico) + compromiso práctico. [P75] recomienda ≥1/200s | [P75] |

---

## Work Objectives

### Core Objective
Corregir las justificaciones de ISO y shutter en 3 documentos para que sean académicamente honestas: citar [P99] para valores documentados, y marcar como "decisión del protocolo" lo que no tiene respaldo bibliográfico.

### Must Have
- [P99] debe ser la referencia principal para ISO=200 y shutter=1/100s
- ISO=100 debe marcarse como "decisión del protocolo, sin respaldo bibliográfico directo"
- Shutter 1/60-1/120 debe eliminarse como "justificado por papers" y marcarse como compromiso práctico + regla 180°
- [P55] (Rice GMC con ISO=25) NO debe usarse para justificar ISO 100-200

### Must NOT Have
- No modificar archivos fuente de los papers en `P1/bibliografia/`
- No cambiar los valores propuestos (ISO 100-200 y shutter 1/60-1/120s se mantienen)
- No agregar información de P2/P3/P4

---

## Verification Strategy

> ZERO HUMAN INTERVENTION
> Cada tarea incluye un grep de verificación post-edición.

---

## TODOs

- [ ] 1. **Corregir `README.md` — líneas 99-100**

  **What to do**:
  Editar la tabla de parámetros de captura. Cambiar las referencias de ISO y shutter:

  **Old text (líneas 99-100)**:
  ```
  | **ISO** | 100-200 fijo | Minimiza ruido digital [P57][P58] |
  | **Shutter** | 1/60s o 1/120s fijo | Motion blur controlado [P57] |
  ```

  **New text**:
  ```
  | **ISO** | 200 fijo (100 si hay suficiente luz) | ISO=200 documentado en [P99] (Open Camera, fenotipado). Principio de fijar ISO respaldado por [P55] (ISO fijo en laboratorio) y [P57] (ganancia baja en cámara industrial). ISO=100 es decisión del protocolo (mínimo práctico en exteriores), no valor extraído de la literatura. |
  | **Shutter** | 1/100s fijo (rango 1/60-1/120) | Shutter=1/100s documentado en [P99] (Open Camera). [P75] recomienda ≥1/200s para walking shake, pero 1/100s es compromiso entre blur y suficiente luz sin flash. Regla 180° (cinematografía, 30fps) da 1/60s como límite inferior. |
  ```

  **Verification**:
  - `grep -c "\[P57\]\[P58\]" README.md` → debe dar 0
  - `grep -c "\[P99\] (Open Camera" README.md` → debe dar 2 (uno para ISO, uno para shutter)

  **Commit**: YES
  - Message: `fix(readme): corregir justificaciones ISO y shutter - usar P99 como respaldo directo`
  - Files: `README.md`

- [ ] 2. **Corregir `Pipeline-Captura-Recomendado.md` — tabla de justificación (líneas 212-213)**

  **What to do**:
  Reemplazar las filas de Shutter e ISO en la tabla "Justificación académica por capa":

  **Old text (líneas 212-213)**:
  ```
  | Shutter 1/60-1/120 | Paper + Regla 180° | **Rolling shutter + distance (Sensors, 2020)**: RSE inversamente proporcional a distancia, lineal con velocidad. **Rice GMC (Sensors, 2021)**: ISO=25, shutter=1/400s fijo. | [P40] |
  | ISO 100-200 | Paper que fijó ISO | **Rice GMC (Sensors, 2021)**: ISO=25 fijo para minimizar variabilidad. | [P40] |
  ```

  **New text**:
  ```
  | Shutter 1/60-1/120 | Documentación técnica + Paper parcial | **P99 (PMC12057810, 2024)**: shutter=1/100s documentado en Open Camera v1.52. **P75 (Motion Blur Review, Heliyon 2024)**: recomienda ≥1/200s para walking shake (más rápido que el rango propuesto). Rango 1/60-1/120s es compromiso práctico para captura sin flash en exteriores, complementado con regla 180° (cinematografía, 30fps). | [P99], [P75] |
  | ISO 200 | Paper documenta valor | **P99 (PMC12057810, 2024)**: ISO=200 fijo en Open Camera v1.52 para fenotipado de hojas. Razón explícita: "to ensure uniformity across images". | [P99] |
  | ISO 100 | Sin respaldo bibliográfico directo | Decisión del protocolo: mínimo ISO práctico en exteriores con luz de día. El principio de "usar el ISO más bajo posible" está respaldado por [P55] (ISO=25 en arroz, laboratorio) y [P57] (ganancia baja en cámara industrial). | — |
  ```

  **Verification**:
  - `grep -c "Rice GMC.*ISO=25" Pipeline-Captura-Recomendado.md` → debe dar 1 (solo en línea 211, no en ISO/shutter)
  - `grep -c "P99.*PMC12057810" Pipeline-Captura-Recomendado.md` → debe ser ≥ 2

  **Commit**: YES (grupo con tarea 3)
  - Message: `fix(pipeline): corregir justificaciones ISO y shutter - separar ISO=200 (P99) de ISO=100 (decisión)`
  - Files: `Pipeline-Captura-Recomendado.md`

- [ ] 3. **Corregir `Pipeline-Captura-Recomendado.md` — tabla de nivel de respaldo (líneas 227-228)**

  **What to do**:
  Reemplazar las filas de Shutter e ISO en la tabla "Nivel de respaldo por decisión":

  **Old text (líneas 227-228)**:
  ```
  | Shutter 1/60-1/120 | ⚠️ Parcial — hay papers que fijan shutter | Media | [P40] |
  | ISO 100-200 | ⚠️ Parcial — hay paper que fija ISO=25 | Media | [P40] |
  ```

  **New text**:
  ```
  | Shutter 1/100s | ⚠️ Parcial — [P99] documenta 1/100s, [P75] recomienda ≥1/200s | Media | [P99], [P75] |
  | ISO=200 | ✅ **Valor documentado en paper** — P99 (PMC12057810) con Open Camera | **Alta** | [P99] |
  | ISO=100 | ❌ **Sin respaldo bibliográfico** — decisión del protocolo | Baja | — |
  ```

  **Verification**:
  - `grep -c "Parcial.*P99" Pipeline-Captura-Recomendado.md` → debe ser ≥ 1
  - `grep -c "Sin respaldo bibliográfico" Pipeline-Captura-Recomendado.md` → debe ser ≥ 1

  **Commit**: YES (grupo con tarea 2)

- [ ] 4. **Corregir `P1/bibliografia/listado-referencias-P1.md` — tabla de trazabilidad (líneas 291-292)**

  **What to do**:
  Reemplazar las filas de ISO y Shutter en la tabla "Trazabilidad: Decisión ↔ Paper":

  **Old text (líneas 291-292)**:
  ```
  | **ISO fijo (100-200)** | P55, P57, P99 |
  | **Shutter fijo (1/60-1/120)** | P49, P55, P57 |
  ```

  **New text**:
  ```
  | **ISO fijo** | P55 (principio, valor ISO=25), P57 (principio, baja ganancia), P99 (valor ISO=200 documentado en Open Camera) |
  | **Shutter fijo** | P49 (principio, ~250µs cámara industrial), P55 (principio, 1/400s arroz), P99 (valor 1/100s documentado en Open Camera) |
  ```

  **Verification**:
  - `grep -c "100-200" listado-referencias-P1.md` → debe dar 0 (en la tabla de trazabilidad)
  - `grep -c "principio" listado-referencias-P1.md` → debe ser ≥ 2

  **Commit**: YES (grupo con tareas 2 y 3)
  - Message: `fix(bibliografia): corregir trazabilidad ISO/shutter - separar principio de valor documentado`
  - Files: `P1/bibliografia/listado-referencias-P1.md`

---

## Commit Strategy

- **1**: `fix(readme): corregir justificaciones ISO y shutter - usar P99 como respaldo directo` — `README.md`
- **2-4**: `fix(pipeline,bibliografia): corregir justificaciones ISO y shutter - separar principio de valor` — `Pipeline-Captura-Recomendado.md`, `P1/bibliografia/listado-referencias-P1.md`

---

## Success Criteria

### Verification Commands
```bash
cd D:\Universidad\Tesis\Codigo opencodego\Datos de campo obtencion\DatosdeCampo

# README.md - verificar que [P57][P58] ya no justifican ISO/shutter
Select-String -Pattern "\[P57\]\[P58\]" README.md
# Expected: no output (not found)

# README.md - verificar que [P99] ahora es la referencia para ISO
Select-String -Pattern "P99.*ISO|ISO.*P99" README.md
# Expected: match with ISO=200

# Pipeline - verificar que ISO=25 ya no justifica ISO 100-200
Select-String -Pattern "ISO=25.*100-200" Pipeline-Captura-Recomendado.md
# Expected: no output (not found)

# Pipeline - verificar nueva estructura
Select-String -Pattern "ISO 200.*Paper documenta|ISO 100.*Sin respaldo" Pipeline-Captura-Recomendado.md
# Expected: 2 matches

# listado-referencias - verificar rango eliminado
Select-String -Pattern "100-200" P1/bibliografia/listado-referencias-P1.md
# Expected: 0 matches (en tabla de trazabilidad; puede aparecer en otra sección)
```

### Final Checklist
- [ ] README.md: [P57][P58] eliminados de ISO/shutter. [P99] citado correctamente
- [ ] Pipeline-Captura-Recomendado.md: ISO=200 justificado por [P99], ISO=100 marcado como "decisión del protocolo"
- [ ] Pipeline-Captura-Recomendado.md: Shutter 1/60-1/120 justificado como compromiso + regla 180°, no como valor de paper
- [ ] listado-referencias-P1.md: ISO y shutter separan "principio" de "valor documentado"
- [ ] [P55] Rice GMC (ISO=25) ya no se usa para justificar ISO 100-200
- [ ] Todos los archivos fuente de papers en `P1/bibliografia/` NO fueron modificados
