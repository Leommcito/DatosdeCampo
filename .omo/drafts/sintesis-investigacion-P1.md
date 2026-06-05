# Síntesis de Investigación — Validación/Contradicción del Paso 1

## Metodología
6 investigaciones paralelas con agente `librarian` (Semantic Scholar, Google Scholar, web, GitHub, arXiv, MDPI, Nature, IEEE, CVF)
Fecha: 05/06/2026

---

## 🔴 LO QUE SE CONTRADIJO (DEBILITADO/REFUTADO)

### 1. "Ningún paper agrícola documenta qué app de cámara usó"
**INVESTIGACIÓN 1 — REFUTADO**

Se encontraron **10+ papers** que documentan apps y configuración:
- **PMC12057810 (2024)**: Nombra **Open Camera v1.52**, documenta ISO=200, shutter=1/100s, AF deshabilitado, compensación de exposición deshabilitada. Razón explícita: "para asegurar uniformidad entre imágenes"
- **PMID 24171108 (2013)**: Nombra **Filmic Pro**, documenta control independiente de foco, exposición e intensidad de luz
- **Journal MTM (2014)**: Nombra **Filmic Pro**, documenta 24fps, 1080p, iluminación LED constante
- **Plant Methods (2023)**: Documenta configuración DSLR detallada (f/4.2, 1/200s, ISO=100, RAW) y compara con modo automático en móviles
- **JARS (2023)**: Compara **auto-exposure vs fixed-exposure** para calibración UAV, cuantifica el error

**⛔ Impacto para tu tesis**: La afirmación absoluta ("ningún paper") es **insostenible**. Debes cambiarla por un matiz: "es **raro** que se documente" / "solo **un puñado** de papers lo hace" / "ningún paper documenta el **flujo completo** (app + IMU + pipeline)".

### 2. [P60] "Stanford CNN ~20% precision drop con exposición variable"
**INVESTIGACIÓN 6 — NO VERIFICADO**

El paper fue encontrado ("Optimizing Image Acquisition Systems for Autonomous Driving", Stanford, 2018) pero **la cifra de 20% no aparece en él**. Podría ser de otro paper o una aproximación.

**⛔ Impacto para tu tesis**: **Verifica la fuente original.** Si no puedes encontrar el 20%, cita el paper con lo que SÍ dice (asimetría sub/sobre-exposición, redes no generalizan bien) sin poner un número que no está verificado.

### 3. "Manual settings are superior for detection" (claim general)
**INVESTIGACIÓN 2 — SIGNIFICATIVAMENTE DEBILITADO**

La investigación encontró **evidencia masiva de 2024-2026** que muestran que el paradigma ha cambiado:

| Paper | Resultado | Contradice |
|---|---|---|
| **Orchard-YOLO (2026)** | 94.8% mAP con ±50% variación iluminación | [P57][P58][P60] |
| **YOLO-PBGM (2025)** | 96.2% mAP en huertos de cítricos | [P57][P58] |
| **Data augmentation (1803.07721)** | Exposición randomizada en training mejora más que fijar captura | [P57] |
| **YOLA (NeurIPS 2024)** | Aprende features illumination-invariant; resultados en luz baja, normal y sobreexpuesta | [P60] |
| **Potato Harvesting (Sensors 2025)** | **F1=0.97** con auto-exposure completo | [P58] |
| **PocketMaize (2022)** | **99.5% accuracy** con auto-fixed smartphone camera | [P58] |

**⛔ Impacto para tu tesis**: La afirmación de que "modo manual es superior" era válida para modelos de 2018, pero **los detectores modernos (2024-2026) son mucho más robustos a variaciones de exposición gracias a data augmentation, atención mechanisms y features illumination-invariant**. Necesitas:
1. Reconocer este cambio de paradigma
2. Justificar por qué tu tesis sigue siendo relevante (pistas: tu experimento A/B validará esto precisamente)
3. Sugerir que **ambas estrategias** (control de captura + entrenamiento robusto) son complementarias

### 4. "Open Camera es la mejor opción gratuita"
**INVESTIGACIÓN 4 — DEBILITADO**

Open Camera tiene **50+ bugs documentados**: crashes con Camera2 API, ANR en Pixel 5a, video corrupto en algunos dispositivos, HDR images verdes en Samsung Qualcomm.

Alternativas modernas como **CameraX** (Google) ofrecen compatibilidad con 98%+ dispositivos, actualizaciones automáticas de Google, y soporte para HDR/night mode mediante vendor extensions.

**⛔ Impacto para tu tesis**: Open Camera sigue siendo válida (y la mejor opción gratuita *open-source*), pero debes:
1. Documentar sus limitaciones conocidas
2. Incluir un paso de verificación de compatibilidad Camera2 API (ya lo tienes en Metodología)
3. Mencionar CameraX como alternativa moderna

### 5. "Auto-exposure falla catastróficamente"
**INVESTIGACIÓN 4 — DEBILITADO**

La investigación encontró sistemas modernos que contradicen esto:
- **DRL-AE (CVPR 2024)**: Auto-exposure con deep reinforcement learning converge en 3-5 frames (vs 10-30 de AE tradicional)
- **Neural Auto-Exposure (CVPR 2021)**: Supera a AE convencional por 6.6 mAP points
- **AdaptiveISP (NeurIPS 2024)**: Genera pipelines ISP óptimos automáticamente para detección
- **NEC System (Nature Communications 2024)**: Control de exposición neuromórfico mantiene tasa de sobreexposición bajo 35%

**⛔ Impacto para tu tesis**: El argumento sigue siendo válido para **auto-exposure tradicional** (built-in camera), pero los sistemas modernos con IA resuelven este problema. Recomiendo que la tesis:
1. Diferencie entre "auto-exposure tradicional de cámara" vs "auto-exposure con IA"
2. Aclare que los sistemas con IA no están disponibles en apps de cámara comerciales
3. Esto refuerza tu punto: **Open Camera con parámetros fijos es la única forma práctica hoy**

---

## 🟢 LO QUE SE VALIDÓ (CONFIRMADO/FORTALECIDO)

### 1. Tone mapping automático es irreversible y degrada detección
**INVESTIGACIONES 5 y 6 — CONFIRMADO SÓLIDAMENTE**

El paper [P62] fue encontrado (aunque no en Nature, sino **Frontiers in Digital Health, 2023**, PMC10705321):
- "Default automatic tone mapping operates as a black box algorithm"
- **74% menor MAE** con tone mapping lineal vía Camera2 API
- "The adaptive control causes nonlinear effects that cannot be reversed in post processing"
- Camera2 API es el **único** modo de obtener tone mapping lineal en móvil (iOS no lo permite)

**NUEVA evidencia encontrada (no citada en tu tesis):**
- **"Impact of ISP Tuning on Object Detection" (MDPI Sensors, 2023)**: Contraste, gamma y saturación causan degradación significativa en YOLOv5, YOLOv8, Faster R-CNN, RT-DETR
- **RAW domain detection**: Múltiples papers (2024-2026) muestran que detección en dominio RAW supera a RGB procesado por ISP
- **RAWild (2026)**: "freedom from the nonlinear distortions introduced by the Image Signal Processor"

**✅ Esto es un PUNTO FUERTE de tu tesis.** Deberías **expandir esta sección** con estos nuevos hallazgos.

### 2. Focus hunting es real y degrada detección
**INVESTIGACIÓN 3 — CONFIRMADO**

Papers de CVPR 2025, WACV 2025, ECCV 2022 confirman:
- "focus hunting (FH), whereby the camera drives the lens forward and backward"
- Causa variaciones en nitidez y cambia el **campo de visión (FoV)**
- **ECCV 2022**: La cámara actúa como "unintentional adversary": 13-14% fluctuación en detección estática, ~40% errores de tracking

**Matiz importante**: El focus hunting es un problema **resuelto para hardware moderno con PDAF** (phase detection AF). Pero los smartphones de gama media/baja y equipos legacy todavía usan CDAF (contrast detection) que sufre de focus hunting.

**✅ Sugerencia para tu tesis**: Añadir distinción entre PDAF (bajo riesgo) y CDAF (alto riesgo) para fortalecer el argumento.

### 3. Glare/destello destruye detección
**INVESTIGACIÓN 6 — CONFIRMADO**

Paper [P63] verificado: F1 cae de **0.82 → 0.13** con glare. Con preprocessing sube a 0.42, sigue siendo muy bajo.

### 4. Luz no controlada es problema real en huertos
**INVESTIGACIÓN 3 — CONFIRMADO**

Papers de agricultura de precisión confirman que el entorno agrícola es **particularmente desafiante**:
- Desplazamientos laterales de hasta **66% del espacio entre hileras**
- Vibración del terreno + viento en hojas complican sistemas VIO/SLAM
- Movimiento a 7km/h + auto-exposure crea **7mm de error** en medición (LEDs paper [P57])

### 5. Papers [P57][P58][P59][P61][P63] existen y sus claims son correctos
**INVESTIGACIÓN 6 — TODOS VERIFICADOS**

| Ref | Publicado en | Claim | Verificado |
|-----|-------------|-------|-----------|
| P57 | Computers and Electronics in Agriculture (Elsevier, 2021) | 85% menos variación HSV | ✅ Citación: 11 |
| P58 | Plant Methods (OA, 2018) | MSE 1.57 vs 4.26 (2.7x) | ✅ |
| P59 | IROS 2021 (arXiv→conference) | 4x menos datos | ✅ (es conferencia, no journal) |
| P61 | CVPR 2025 | Focus hunting es real | ✅ Paper muy reciente |
| P63 | arXiv 2020 (preprint) | F1 0.82→0.13 | ✅ |

---

## 🟡 NEUTRAL / MATIZADO

### El paradigma ha cambiado (2018 → 2026)

La tesis actual se basa en evidencia de **2018-2021**. La investigación encontró que entre **2023-2026** surgió un nuevo paradigma:

**Paradigma antiguo (tu tesis):**
```
Controlar la captura → Imágenes consistentes → Mejor detección
```

**Paradigma nuevo (2023-2026):**
```
Entrenar modelos robustos → Detección invariante a iluminación → No necesitas controlar captura
```

**Pero esto NO invalida tu tesis** — al contrario, la hace **más interesante**:
1. Tu **experimento A/B** (protocolo vs cámara nativa) es precisamente lo que falta en la literatura
2. Puedes posicionar tu tesis como **"el viejo paradigma sigue siendo relevante porque..."** 
3. O mejor aún: **"ambos paradigmas son complementarios — captura controlada + modelos robustos dan el mejor resultado"**

---

## 📋 RECOMENDACIONES PARA ACCIÓN

### Urgente (corregir antes de defender):
1. ☐ **[P60] Verificar origen del claim "~20% caída precisión"** — no encontrado en el paper citado
2. ☐ **[P62] Corregir cita**: El paper es de Frontiers in Digital Health (2023), no Nature/PMC. Agregar DOI: 10.3389/fdgth.2023.1301019
3. ☐ **[P59] Aclarar que es conferencia**, no journal

### Importante (fortalecer la tesis):
4. ☐ **Suavizar afirmación absoluta**: Cambiar "ningún paper documenta" por "escasez/rareza de documentación"
5. ☐ **Añadir nuevo evidence**: Papers de ISP tuning (MDPI Sensors 2023), RAW detection, ECCV 2022 "unintentional adversary"
6. ☐ **Reconocer el nuevo paradigma** (2023-2026) y posicionar tu tesis en relación a él
7. ☐ **Documentar limitaciones de Open Camera** y agregar alternativa CameraX

### Opcional (para publicar):
8. ☐ **Comparar PDAF vs CDAF** y su impacto en focus hunting
9. ☐ **Expandir la sección de tone mapping** con los nuevos papers encontrados
10. ☐ **Agregar discusión sobre auto-exposure con IA** (para mostrar que tu contribución no es obsoleta)

---

## 📊 BALANCE FINAL

| Aspecto | Estado | Acción |
|---------|--------|--------|
| Afirmación "ningún paper documenta apps" | ❌ Refutado | Matizar |
| [P60] 20% precision drop | ❌ No verificado | Verificar fuente |
| Auto > Manual (claim general) | ⚠️ Debilitado | Matizar + posicionar |
| Open Camera mejor opción | ⚠️ Debilitado | Documentar limitaciones |
| Tone mapping irreversible | ✅ Validado + Ampliado | ¡Expandir! |
| Focus hunting real | ✅ Validado | Añadir matiz PDAF/CDAF |
| Glare destruye detección | ✅ Validado | OK |
| Entorno agrícola desafiante | ✅ Validado | OK |
| Papers [P57][P58][P59][P61][P63] | ✅ Verificados | OK |

**La tesis NO está invalidada.** Los hallazgos nuevos la hacen **más rica y matizada**. Pero necesitas ajustar algunas afirmaciones absolutas y reconocer el cambio de paradigma en detección 2024-2026.
