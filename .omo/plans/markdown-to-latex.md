# Plan: Conversión de Metodología (Markdown → LaTeX)

## TL;DR

> **Quick Summary**: Convertir el documento metodológico completo de Markdown a LaTeX, preservando el 100% del contenido (texto, tablas, figuras, referencias, notas al pie, formato), produciendo un archivo .tex compilable.

> **Deliverables**:
> - `Metodologia_final_corregido.tex` — documento LaTeX completo
> - Paquete de recursos (si hay imágenes) listos para compilar
>
> **Estimated Effort**: Medium-Large (~987 líneas, 22 tablas, 37 emojis)
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: Task 1 → Task 4 → Task 6 → Task F1→F4

---

## Context

### Original Request
Convertir el archivo `Metodologia_final_corregido.md` (markdown) a formato LaTeX (.tex), manteniendo toda la información original sin pérdidas.

### Estructura del Documento Fuente

| Elemento | Cantidad |
|---|---|
| Líneas totales | 987 |
| H1 / H2 / H3 / H4 | 1 / 7 / 26 / 40 |
| Tablas | 22 (desde 2 hasta 10+ columnas) |
| Bloques de código | 6 |
| Notas al pie | 8 |
| Emojis (✅❌🔒) | 37 |
| Flechas (→) | 13 |
| Reglas horizontales | 7 |
| Citas en `("Título", Año)` | ~186 |
| Citas en `(Autor et al., Año)` | ~45 |

### Herramientas Disponibles
- **Python 3.14** disponible en el sistema
- **Pandoc NO** disponible
- Se usará script Python de conversión + post-procesamiento manual

---

## Work Objectives

### Core Objective
Producir un archivo `Metodologia_final_corregido.tex` que:
1. Contenga el 100% del contenido del .md original
2. Sea compilable con `pdflatex` o `xelatex`
3. Use codificación UTF-8 (recomendado: XeLaTeX o LuaLaTeX)
4. Mantenga la estructura jerárquica del documento

### Must Have
- [ ] Todas las secciones preservadas (H1→H4 correctamente anidadas)
- [ ] Todas las tablas convertidas a entorno `tabular`/`tabularx`/`longtable`
- [ ] Todo el texto, incluyendo acentos y caracteres Unicode
- [ ] Citas y referencias preservadas textualmente
- [ ] Formato bold/italic/code preservado
- [ ] Notas al pie convertidas a `\footnote{}`
- [ ] Bloques de código en `\begin{verbatim}`
- [ ] Preámbulo LaTeX completo con paquetes necesarios

### Must NOT Have (Guardrails)
- [ ] NO modificar, resumir o alterar el contenido original
- [ ] NO inventar nuevas secciones o contenido
- [ ] NO eliminar información por dificultad técnica
- [ ] NO usar figuras/imágenes que no existan en el original

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### QA Policy
- **Archivo .tex**: Verificar con `pdflatex` o `xelatex` que compile sin errores
- **Contenido**: Comparar líneas clave entre .md y .tex con scripts de diff
- **Tablas**: Verificar que el número de tablas coincida (22)
- **Caracteres especiales**: Buscar caracteres no escapados ($, %, &, etc.)
- **Emojis**: Verificar que todos estén reemplazados por comandos LaTeX
- Evidencia guardada en `.omo/evidence/`

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation — preparación, 2 tareas):
├── Task 1: Crear preámbulo LaTeX con paquetes necesarios [quick]
├── Task 2: Escribir script Python de conversión markdown→latex [unspecified-high]

Wave 2 (Conversión — paralelo máximo, 4 tareas):
├── Task 3: Ejecutar conversión completa del .md → .tex [unspecified-high]
├── Task 4: Post-procesar tablas (tabular/longtable) [unspecified-high]
├── Task 5: Post-procesar emojis y caracteres especiales [visual-engineering]
├── Task 6: Post-procesar citas, notas al pie y referencias [quick]

Wave 3 (Validación — 2 tareas):
├── Task 7: Compilar .tex con xelatex y corregir errores [quick]
├── Task 8: Verificar integridad del contenido contra .md original [unspecified-high]

Wave FINAL (4 revisiones paralelas):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Código LaTeX quality review (unspecified-high)
├── Task F3: QA de contenido (comparar .md vs .tex) (unspecified-high)
├── Task F4: Scope fidelity check (deep)

Critical Path: Task 1 → Task 3 → Task 7 → F1-F4 → user okay
```

### Dependency Matrix
- **1**: - → 3
- **2**: - → 3
- **3**: 1, 2 → 4, 5, 6
- **4**: 3 → 7
- **5**: 3 → 7
- **6**: 3 → 7
- **7**: 4, 5, 6 → 8
- **8**: 7 → F1-F4

---

## TODOs

- [ ] 1. Crear preambulo LaTeX con paquetes necesarios

  **What to do**:
  - Crear archivo latex-preamble.tex con:
    - inputenc (utf8), fontenc (T1), babel (spanish)
    - amsmath, amssymb - matematicas
    - graphicx, hyperref, xcolor
    - booktabs, tabularx, longtable, array - tablas
    - geometry (margenes 2.5cm), setspace (1.5 interlineado)
    - fancyhdr, titlesec, verbatim, fancyvrb
    - enumitem, microtype
    - Definir comandos para emojis: checkmark, xmark, lock

  **Must NOT do**: No incluir paquetes innecesarios

  **Recommended Agent Profile**: `quick`
  **Parallelization**: Wave 1 (with Task 2) | Blocks: Task 3

  **Acceptance Criteria**:
  - [ ] latex-preamble.tex creado con todos los paquetes
  - [ ] Compila con xelatex (test minimo)

  **QA Scenarios**:
  ```
  Scenario: Preamble compiles
    Tool: Bash
    Steps: xelatex test.tex (con input del preamble)
    Expected: Exit code 0
  ```

  **Commit**: NO (groups with Task 3)

---

- [ ] 2. Escribir script Python de conversion markdown a LaTeX

  **What to do**:
  - Crear convert_md_to_tex.py que procese:
    1. Headers: # Title -> section, ## -> subsection, ### -> subsubsection, #### -> paragraph
    2. Bold/Italic: **text** -> textbf, *text* -> textit
    3. Codigo inline: `code` -> texttt
    4. Bloques codigo: ``` -> begin{verbatim}
    5. Listas: - item -> itemize, 1. item -> enumerate
    6. Tablas: markdown table -> tabular/tabularx
    7. Blockquotes: > text -> begin{quote}
    8. Notas al pie: [^N] -> footnote
    9. Enlaces: [text](url) -> href{url}{text}
    10. Reglas: --- -> hline
    11. Emojis: checkmark, xmark, lock
    12. Escapar caracteres especiales LaTeX: $ % & # _ { } ~ ^
    13. Preservar citas textualmente
  - Incluir input{latex-preamble} al inicio
  - Output: Metodologia_final_corregido.tex

  **Recommended Agent Profile**: `unspecified-high`
  **Parallelization**: Wave 1 (with Task 1) | Blocks: Task 3

  **Acceptance Criteria**:
  - [ ] Script creado y ejecuta sin errores
  - [ ] .tex generado contiene todas las secciones

  **Commit**: NO (groups with Task 3)

---

- [ ] 3. Ejecutar conversion completa del .md a .tex

  **What to do**:
  - Ejecutar: python convert_md_to_tex.py
  - Generar Metodologia_final_corregido.tex completo
  - Verificar: 1 seccion, 7 subsecciones, 26 sub-subsecciones, 40 sub4-secciones
  - Guardar en directorio raiz del proyecto

  **Recommended Agent Profile**: `unspecified-high`
  **Parallelization**: Sequential (after 1,2) | Blocks: 4,5,6

  **Acceptance Criteria**:
  - [ ] Archivo .tex generado y completo
  - [ ] Mismas secciones que el .md original

  **Commit**: YES - `docs(latex): convert Metodologia_final to LaTeX`

---

- [ ] 4. Post-procesar tablas a formato LaTeX

  **What to do**:
  - Revisar las 22 tablas convertidas y corregir:
    - Tablas con muchas columnas -> tabularx o longtable
    - Usar toprule/midrule/bottomrule de booktabs
    - Verificar bold/italic dentro de celdas
    - Atencion especial a: tabla Open Camera (10 cols), tabla Que Hacer/Evitar, tabla trazabilidad (90+ filas)

  **Recommended Agent Profile**: `unspecified-high`
  **Parallelization**: Wave 2 (with 5,6) | Blocks: 7 | Blocked By: 3

  **Acceptance Criteria**:
  - [ ] 22 tablas en formato LaTeX correcto
  - [ ] No causan errores de compilacion

  **Commit**: NO (groups with Task 7)

---

- [ ] 5. Post-procesar emojis y caracteres especiales

  **What to do**:
  - Reemplazar 37 emojis: checkmark (verde), xmark (rojo), lock
  - Escapar caracteres LaTeX: $ % & # _ { } ~ ^
  - Unicode flechas (->), multiplicacion (x), grados(deg), micro (mu): decidir mantener o convertir a comandos
  - Preferir mantener Unicode si se usa XeLaTeX

  **Recommended Agent Profile**: `visual-engineering`
  **Parallelization**: Wave 2 (with 4,6) | Blocks: 7 | Blocked By: 3

  **Acceptance Criteria**:
  - [ ] No quedan emojis raw en el .tex
  - [ ] Caracteres especiales escapados

  **Commit**: NO (groups with Task 7)

---

- [ ] 6. Post-procesar citas, notas al pie y referencias

  **What to do**:
  - Notas al pie: verificar formato footnote correcto
  - Citas ("Titulo", Ano) y (Autor et al., Ano): preservar textualmente
  - URLs/DOIs en capitulo 6: convertir a href
  - Tabla de trazabilidad: verificar completa

  **Recommended Agent Profile**: `quick`
  **Parallelization**: Wave 2 (with 4,5) | Blocks: 7 | Blocked By: 3

  **Acceptance Criteria**:
  - [ ] 8 notas al pie en formato correcto
  - [ ] Referencias con href para DOIs

  **Commit**: NO (groups with Task 7)

---

- [ ] 7. Compilar .tex con xelatex y corregir errores

  **What to do**:
  - Compilar: xelatex Metodologia_final_corregido.tex (2 pasadas)
  - Revisar .log por errores
  - Corregir: paquetes faltantes, caracteres no escapados, tablas mal formadas
  - Repetir hasta compilacion limpia (sin errores)

  **Recommended Agent Profile**: `quick`
  **Parallelization**: Sequential (after 4,5,6) | Blocks: 8

  **Acceptance Criteria**:
  - [ ] Compila sin errores con xelatex
  - [ ] PDF generado

  **Commit**: YES - `docs(latex): post-process tables emoji citations fix compilation`

---

- [ ] 8. Verificar integridad del contenido

  **What to do**:
  - Comparar contenido .tex vs .md original
  - Verificar seccion por seccion que no falte contenido
  - Puntos criticos: Capitulo 3 (extenso), tabla trazabilidad (90+ filas), referencias (DOIs)
  - Usar diff de texto plano

  **Recommended Agent Profile**: `unspecified-high`
  **Parallelization**: Sequential (after 7) | Blocks: F1-F4

  **Acceptance Criteria**:
  - [ ] Sin diferencias de contenido entre .md y .tex
  - [ ] Documento de verificacion generado

  **Commit**: NO

---

## Final Verification Wave

- [ ] F1. **Plan Compliance Audit** (oracle)
  Verificar Must Have / Must NOT Have. Revisar evidencias.
  Output: `VERDICT: APPROVE/REJECT`

- [ ] F2. **LaTeX Quality Review** (unspecified-high)
  Compilar .tex sin errores. Revisar estructura, tablas, caracteres escapados.
  Output: `Compilation | Tables | Structure | VERDICT`

- [ ] F3. **Content QA** (unspecified-high)
  Comparar .md vs .tex: secciones, tablas (22), notas (8), emojis (37).
  Output: `Content | Tables | Footnotes | Emoji | VERDICT`

- [ ] F4. **Scope Fidelity** (deep)
  Verificar que cada tarea cumplio su objetivo. Sin contaminacion ni perdida.
  Output: `Tasks 8/8 | Contamination CLEAN | VERDICT`

---

## Commit Strategy

- **Task 3**: `docs(latex): convert Metodologia_final_corregido to LaTeX`
  Files: Metodologia_final_corregido.tex, convert_md_to_tex.py, latex-preamble.tex
- **Task 7**: `docs(latex): post-process tables emoji citations fix compilation`
  Files: Metodologia_final_corregido.tex

---

## Success Criteria

### Verification Commands
```bash
xelatex -interaction=nonstopmode Metodologia_final_corregido.tex
grep -c "section{" Metodologia_final_corregido.tex | head -5
grep -c "begin{tabular}" Metodologia_final_corregido.tex
grep -c "footnote{" Metodologia_final_corregido.tex
```

**Expected**: 0 errores de compilacion, secciones correctas, 22 tablas, 8 notas

### Final Checklist
- [ ] All Must Have present
- [ ] All Must NOT Have absent
- [ ] Compilacion sin errores
- [ ] Contenido 100% preservado

- [ ] 1. Crear preámbulo LaTeX

  **What to do**:
  - Crear el archivo `latex-preamble.tex` con los siguientes paquetes/configuraciones necesarias para el documento:
  - Paquetes requeridos:
    - `inputenc` (utf8), `fontenc` (T1) — codificación
    - `babel` (spanish) — idioma
    - `amsmath`, `amssymb` — matemáticas básicas
    - `graphicx` — imágenes (si hay)
    - `hyperref` — enlaces y referencias cruzadas
    - `booktabs`, `tabularx`, `longtable`, `array` — tablas
    - `xcolor`, `colortbl` — colores en tablas
    - `geometry` — márgenes (2.5 cm estilo tesis)
    - `setspace` — interlineado (1.5)
    - `fancyhdr` — encabezados y pies
    - `titlesec` — formato de títulos
    - `verbatim`, `fancyvrb` — bloques de código
    - `enumitem` — listas personalizadas
    - `microtype` — microtipografía
  - Configurar metadatos: título, autor, fecha
  - Crear entorno de documento con \begin{document} y \end{document}
  - Definir comandos personalizados para emojis:
    - `\checkmark` para ✅
    - `\xmark` para ❌
    - `\lock` para 🔒

  **Must NOT do**:
  - No incluir paquetes innecesarios (evitar bloat)
  - No usar pdflatex si hay problemas con UTF-8 (preferir xelatex)

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 2)
  - **Blocks**: Task 3
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] Archivo `latex-preamble.tex` creado con todos los paquetes
  - [ ] Compila solo (test vacío) con `xelatex latex-preamble.tex`

  **QA Scenarios**:
  ```
  Scenario: Verify preamble compiles standalone
    Tool: Bash
    Preconditions: latex-preamble.tex exists
    Steps:
      1. Create minimal test: \documentclass{article} \input{latex-preamble} \begin{document} Test \end{document}
      2. Run: xelatex test.tex
    Expected Result: Exit code 0, no errors in .log
    Evidence: .omo/evidence/task-1-preamble-test.log
  ```

  **Commit**: NO (groups with Task 3)

---

- [ ] 2. Escribir script Python de conversión markdown → LaTeX

  **What to do**:
  - Crear `convert_md_to_tex.py` que convierta el archivo markdown a LaTeX
  - El script debe procesar secuencialmente:
    1. **Headers**: `# Title` → `\section{Title}`, `## Title` → `\subsection{Title}`, etc.
    2. **Bold/Italic**: `**texto**` → `\textbf{texto}`, `*texto*` → `\textit{texto}`
    3. **Código inline**: `` `code` `` → `\texttt{code}`
    4. **Bloques código**: ``` → `\begin{verbatim}...\end{verbatim}`
    5. **Listas**: `- item` → `\begin{itemize}\item item`
    6. **Listas numeradas**: `1. item` → `\begin{enumerate}\item item`
    7. **Tablas**: Convertir markdown table a `\begin{tabular}` o `\begin{tabularx}`
    8. **Blockquotes**: `> texto` → `\begin{quote}texto\end{quote}`
    9. **Notas al pie**: `[^N]` → `\footnote{}`
    10. **Enlaces**: `[texto](url)` → `\href{url}{texto}`
    11. **Reglas horizontales**: `---` → `\hline`
    12. **Emojis**: ✅ → `\checkmark`, ❌ → `\xmark`, 🔒 → `\lock`
    13. **Caracteres especiales LaTeX**: Escapar $, %, &, #, _, {, }, ~, ^
    14. **Preservar**: Citas en formato `("Título", Año)` y `(Autor et al., Año)`
  - Manejar edges cases:
    - Tablas sin alineación explícita (centradas por defecto)
    - Celdas con formato bold/italic dentro de tablas
    - Líneas en blanco entre párrafos
    - Caracteres Unicode en tablas
  - Incluir `\input{latex-preamble}` al inicio del documento
  - Output: `Metodologia_final_corregido.tex`

  **Must NOT do**:
  - No modificar el contenido textual de las citas referencias
  - No simplificar o perder información de las tablas

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 1)
  - **Blocks**: Task 3
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] `convert_md_to_tex.py` creado
  - [ ] Script ejecuta sin errores de Python
  - [ ] Archivo .tex generado contiene todas las secciones esperadas

  **QA Scenarios**:
  ```
  Scenario: Script runs without errors
    Tool: Bash
    Preconditions: convert_md_to_tex.py exists
    Steps:
      1. Run: python convert_md_to_tex.py
    Expected Result: Exit code 0, file Metodologia_final_corregido.tex created
    Evidence: .omo/evidence/task-2-script-run.log

  Scenario: Verify section count matches
    Tool: Bash
    Preconditions: Metodologia_final_corregido.tex exists
    Steps:
      1. Run: grep -c "\section{" Metodologia_final_corregido.tex
      2. Run: grep -c "\subsection{" Metodologia_final_corregido.tex
    Expected Result: Matches source (1 section, 7 subsection)
    Evidence: .omo/evidence/task-2-sections.log
  ```

  **Commit**: NO (groups with Task 3)

---

- [ ] 3. Ejecutar conversión completa del .md → .tex

  **What to do**:
  - Ejecutar `python convert_md_to_tex.py` sobre `Metodologia_final_corregido.md`
  - Generar `Metodologia_final_corregido.tex` completo con preámbulo incluido
  - Verificar que el archivo generado:
    - Tiene todos los capítulos (6 H2)
    - Tiene todas las sub-secciones (26 H3, 40 H4)
    - Preserva el orden del documento original
    - Incluye el preámbulo correctamente
  - Guardar el archivo en el directorio raíz del proyecto

  **Must NOT do**:
  - No editar manualmente el contenido generado (se hará en Tasks 4-6)
  - No eliminar líneas aunque parezcan redundantes

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (after Tasks 1, 2)
  - **Blocks**: Tasks 4, 5, 6
  - **Blocked By**: Tasks 1, 2

  **Acceptance Criteria**:
  - [ ] `Metodologia_final_corregido.tex` generado y completo
  - [ ] Misma cantidad de secciones que el .md original

  **QA Scenarios**:
  ```
  Scenario: Run conversion
    Tool: Bash
    Preconditions: convert_md_to_tex.py, Metodologia_final_corregido.md exist
    Steps:
      1. python convert_md_to_tex.py
      2. Test-Path Metodologia_final_corregido.tex
    Expected Result: File exists, non-empty
    Evidence: .omo/evidence/task-3-conversion.log
  ```

  **Commit**: YES
  - Message: `docs(latex): convert Metodologia_final_corregido.md to LaTeX`
  - Files: `Metodologia_final_corregido.tex`, `convert_md_to_tex.py`, `latex-preamble.tex`

---
