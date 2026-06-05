# Investigación — Pregunta 3: Protocolo de Caminata y Captura

## Estado

⚠️ **Pendiente de ejecutar en Elicit.** El prompt está listo para copiar y pegar.

---

## Prompt de búsqueda para Elicit

```
# Research Question

In manual smartphone video capture for fruit detection and tracking in orchard environments, what are the documented optimal capture parameters — distance to canopy, camera angle, walking speed, lighting conditions, and trajectory pattern — that maximize downstream detection accuracy (mAP) and tracking consistency (MOTA)?

# Context

We are designing a field capture protocol for dense mandarin orchards (small fruit, high occlusion, dense foliage) for YOLO detection + MOT tracking. We need to define:
- Distance from camera to canopy (0.5m, 1m, 1.5m+)
- Camera tilt angle (0° frontal, 15°-30° upward)
- Walking speed (slow constant vs variable)
- Lighting conditions (diffuse vs direct light, time of day)
- Trajectory pattern (continuous row, zigzag, both sides)
- Strategy to avoid double counting and occlusions

We need papers that document ANY of these parameters quantitatively, preferably with detection metrics.

# Columns to use in Elicit

Set these manually in the Elicit interface:

- **Intervention**: The specific capture parameter tested (distance, angle, speed, lighting, trajectory)
- **Outcome**: Quantitative result (mAP, MOTA, F1, recall, precision, % fruit counted correctly, error rate)
- **Methodology**: How the parameter was tested (controlled experiment, field trial, ablation study)
- **Population**: Crop type, orchard type, environment (dense, trellis, traditional)
- **Key Finding**: One-sentence summary of what parameter value worked best and why

# Specific data points to extract

For every relevant paper, extract:

1. **Crop and orchard type**: Mandarins? Citrus? Apples? Grapes? Dense? Trellis?
2. **Distance(s) tested**: Exact distances from camera to canopy (e.g., 0.5m, 1m, 1.5m)
3. **Distance recommended**: Which distance gave best results
4. **Camera angle(s) tested**: Exact angles (0°, 15°, 30°, 45°)
5. **Angle recommended**: Which angle gave best results
6. **Walking speed**: Speed in m/s or qualitative (slow, moderate, fast)
7. **Speed recommended**: Which speed gave best results
8. **Lighting tested**: Time of day, sunny/cloudy, direct/diffuse
9. **Lighting recommended**: Optimal conditions
10. **Trajectory pattern**: How the operator moved (single pass, both sides, zigzag)
11. **Double counting strategy**: How they avoided counting same fruit twice
12. **Detection metric**: mAP, F1, MOTA, counting accuracy, error rate, correlation (R²)

# Search terms

Search these separately in Elicit:

1. "optimal distance camera canopy fruit detection orchard"
2. "camera angle fruit detection smartphone walking"
3. "walking speed video capture object detection agriculture"
4. "lighting conditions fruit detection outdoor orchard"
5. "capture protocol trajectory fruit counting double counting"
6. "smartphone video capture methodology orchard canopy"
7. "time of day fruit detection accuracy outdoor"
8. "occlusion handling camera angle fruit trees"

# Constraints

- Agricultural papers only (fruit trees, orchards, vineyards, row crops)
- 2018-2025 preferred (but include seminal older papers if directly relevant)
- Papers MUST report a quantitative comparison between at least 2 parameter values (e.g., distance=0.5m vs 1m, angle=0° vs 30°)
- EXCLUDE papers that only mention capture parameters in passing without testing them
- EXCLUDE papers where capture was done by robot/tractor unless the parameter recommendation transfers to manual handheld capture
- EXCLUDE papers about fruit counting from static cameras or aerial drones
- If a paper recommends a parameter but does NOT test it quantitatively (just "we used X"), note it but flag as "recommendation without testing"

# Stopping condition

Stop when:
- You have 8-12 relevant papers, OR
- After searching all 8 terms, fewer than 3 papers contain quantitative parameter comparisons (report as genuine gap)

# Output format

A table with columns: Paper | Year | Crop | Parameter Tested | Values Compared | Best Value | Metric | Metric Improvement | Key Recommendation

Also include a brief note on which parameters HAVE literature support vs which are GAPS.
```

---

## Datos parciales desde Semantic Scholar (mientras se espera Elicit)

Papers que reportan distancia y ángulo (aunque no comparan múltiples valores):

| Paper | Distancia | Ángulo | Condiciones de luz |
|---|---|---|---|
| Rice GMC (Sensors, 2021) | 27.5 cm | — | Sin sol directo |
| Coffee monitoring (Sensors, 2020) | 80-150 mm | 11.3° | Sin control |
| Apple detection Redmi Note 7 (2024) | 0.3-1.5 m | — | 5 condiciones probadas |
| DHN-YOLO fresas (2025) | 50-80 cm | ~45° | Variadas |
| Cocoa dataset (Data, 2023) | — | Múltiples ángulos | 8:00-16:00 |

**Nota:** Ninguno de estos papers **compara** dos valores del mismo parámetro (ej: 0.5m vs 1m) con métricas. Son valores fijos que usaron, no experimentos de optimización.
