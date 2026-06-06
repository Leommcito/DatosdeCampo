# P1 Mejora Académica — Log de Cambios

## Sesión: 2026-06-05

### Correcciones aplicadas a `P1/Investigacion-P1-Software-Captura.md`

#### 1. [P96] Corrección de claim erróneo (líneas ~282, ~313)
- **Problema:** El documento afirmaba "29 objetos reales (5.4x falsos)" sin respaldo en la fuente original.
- **Fuente verificada:** P96 (ECCV 2022 AROW) dice: "Our tracker reported 157 track-ids when the original Yolov5 model was used... 94 track-ids when the transfer-learning trained Yolov5 model was used (i.e., 40.1% fewer mistakes in tracking)."
- **Corrección:** Reemplazado por "Original YOLOv5 generó 157 track-IDs vs 94 con transfer-learning (40.1% menos errores)."
- **Impacto:** Elimina métrica inventada; ahora todas las cifras de P96 son trazables al paper.

#### 2. [P49] Nueva sección agregada (después de P63)
- **Problema:** P49 no aparecía en el documento a pesar de ser una fuente relevante para justificar shutter fijo e iluminación controlada.
- **Fuente:** Rançon et al. (2023), Sensors 23, 847. Sistema proximal para viñedos con Basler Ace + flash xenon + exposición ~250 µs + app Android Wi-Fi + 8 años de campo.
- **Adición:** Nueva subsección "Paper 14: Sistema de adquisición proximal para viñedos (Sensors, 2023) — [P49]" con tabla de hallazgos y relevancia.
- **Impacto:** Fortalece la justificación de exposición fija con evidencia de campo a largo plazo.

#### 3. [P49] Agregado a tabla de evidencia cuantitativa
- **Adición:** Fila "Exposición fija corta + flash sincronizado | ~250 µs con flash xenon, 8 años de campo | Vineyard proximal sensing (2023) | [P49]"
- **Impacto:** P49 ahora tiene trazabilidad cuantitativa en la tabla maestra de evidencia.

#### 4. [P99] Completar detalles técnicos faltantes
- **Problema:** La sección P99 mencionaba ISO=200 y shutter=1/100s pero omitía datos clave de iluminación y distancia.
- **Fuente verificada:** P99 (PMC12057810, 2024) especifica: "4 neutral-white (4000 K) LED tube-lights... camera-to-stage distance of 50 cm".
- **Corrección:** Agregados "4 tubos LED neutral-white (4000 K) a distancia fija de 50 cm cámara-hoja" y "Dispositivo: Redmi Note 7 Pro (Sony IMX 586, 48 MP, f/1.8)".
- **Impacto:** Configuración de P99 ahora es reproducible con todos los parámetros técnicos documentados.

### Verificaciones realizadas

#### Métricas cuantitativas validadas vs fuentes
| Métrica | Valor en doc | Valor en fuente | Estado |
|---|---|---|---|
| P57 reducción HSV | 85% | 85% menos variación | ✅ OK |
| P58 MSE manual vs auto | 1.57 vs 4.26 (2.7x) | 1.57 vs 4.26; 4.26/1.57=2.71 | ✅ OK |
| P59 menos datos | 4x | 4x menos datos | ✅ OK |
| P62 MAE lineal | 74% menor | 74% menor MAE | ✅ OK |
| P96 fluctuación | 13-14% | F2 hasta 13.0%, F10 hasta 14.0% | ✅ OK |
| P96 track-IDs | 157 vs 94 (40.1%) | 157 vs 94 (40.1% fewer mistakes) | ✅ OK (corregido) |
| P97 RAW vs ISP | 7.1% más precisión | 7.1% más precisión | ✅ OK |
| P98 AdaptiveISP | 28% mejora | 28% mejor mAP | ✅ OK |

#### Parámetros verificados
- ISO: ✅ [P55] (25), [P57], [P58], [P99] (200)
- Shutter: ✅ [P55] (1/400s), [P57] (200 µs), [P99] (1/100s), [P49] (~250 µs)
- AF: ✅ [P61] (focus hunting), [P99] (AF deshabilitado)
- AE: ✅ [P57], [P58], [P60]
- WB: ✅ [P62] (tone mapping), [P99]
- Bitrate: ✅ Documentado en sección Open Camera
- OIS: ⚠️ No aparece en P1 (es parámetro de hardware estabilización, pertenece a P2/P3; no se agregó para respetar alcance estricto de P1)

### Estado final
- Archivo editado: `P1/Investigacion-P1-Software-Captura.md`
- Archivos bibliografía: ❌ NO modificados (cumple restricción)
- Información P2/P3/P4: ❌ NO agregada (cumple restricción)
- Todos los claims cuantitativos ahora son trazables a fuentes bibliográficas.
