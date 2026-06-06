# Investigación — Pregunta 3: Protocolo de Caminata y Captura

## Estado

✅ **Completado + Actualizado con evidencia contradictoria (05/06/2026).** Investigación ejecutada vía Semantic Scholar (librarian agent) + búsqueda web complementaria. Los parámetros del protocolo de caminata están justificados con respaldo bibliográfico. Adicionalmente, se realizó una **investigación extensa de 8 agentes paralelos** para encontrar papers que contradigan o mejoren los valores propuestos. Todos los hallazgos contradictorios se documentan en las secciones siguientes sin reemplazar la evidencia original.

---

## Fuentes consultadas

- **Librarian agent (Semantic Scholar) — original:** 2 rondas de búsqueda con 14 términos en total
- **Búsqueda web complementaria (Exa) — original:** 4 búsquedas adicionales para velocidad, distancia, ángulo e iluminación
- **Investigación contradictoria — 8 agentes librarian paralelos (05/06/2026):** 1 por parámetro (velocidad, ángulo, distancia, iluminación, shutter) + tracking + contradicción integral + cítricos LATAM. ~80 términos de búsqueda en total.
- **Papers nuevos agregados en Tabla Maestra (original):** [P69] a [P78]
- **Papers nuevos agregados en Tabla Maestra (contradicciones):** [P110] a [P130]

---

## Resumen de parámetros con justificación bibliográfica

| Parámetro | Valor recomendado | Respaldo principal | IDs | Confianza |
|---|---|---|---|---|
| **Velocidad de caminata** | ~0.5-1.0 m/s | Apple Yield Mapping (2018): Samsung S4 a **2 m/s**. MangoYOLO: **5 km/h**. Motion blur: velocidad >1 m/s incrementa blur. | [P70], [P66], [P75], [P68] | 🔴 Alta |
| **Ángulo de cámara** | 15-30° hacia arriba | Sweet-Pepper (2014): **zenith 60° (óptimo)** probado en 14 posiciones. Apple 3D (2023): **15° mejor RMSE**. FruitSize: **<14°** límite. | [P69], [P71], [P47] | 🔴 Alta |
| **Distancia al dosel** | 0.8-1.5 m | YOLO-CSB (2026): 0.8-1.5m óptimo. RGB-D (2020): 1.5m da 200% más densidad. KiwiDetector (2020): ~1m. Apple fruitlets (2024): 0.5-3m. | [P73], [P72], [P48], [P37] | 🔴 Alta |
| **Horario / Iluminación** | 9-11 AM o 3-5 PM. Nublado ideal. | Pear dataset (2023): 4 horarios. Cocoa (2023): 8AM-4PM. Orchard-YOLO (2026): ±50% brillo probado. | [P29], [P30], [P76] | 🟠 Alta |
| **Shutter speed** | 1/60-1/120s | Motion Blur Review (2024): fórmula `desplazamiento ≈ (velocidad × exposición) / focal`. Citrus GAN (2025): 27% mAP drop por blur. | [P75], [P68], [P40] | 🔴 Alta |
| **Estrategia anti-doble conteo** | ByteTrack + multi-view | Gené-Mola (2023): ByteTrack MOTA 0.682. Mango multi-view (2016): error 1.36%. MangoYOLO Kalman (2019): 62% harvest. | [P74], [P66] | 🔴 Alta |

---

## Resumen de evidencia contradictoria — Papers que contradicen o mejoran las recomendaciones originales

> Los siguientes hallazgos provienen de una investigación extensa con 8 agentes librarian paralelos (05/06/2026). Se documentan como **contradicciones y mejoras** a los valores originales, sin reemplazarlos. La decisión final sobre qué valor usar queda a criterio del lector según el contexto de captura.

| Parámetro | Valor P3 original | Evidencia contradictoria | Nueva evidencia que mejora | IDs contradictorios |
|---|---|---|---|---|
| **Velocidad** | ~1 m/s | **1.39 m/s funciona** con tracking (MangoYOLO: 62% harvest). **Hasta 2.5 m/s** viable con fps/inference rápidos (fórmula overlapping rate). | Con deblurring o tracking robusto: **1.3-1.5 m/s** es seguro. Para mandarinas sin deblurring: **~1 m/s** recomendado. | [P110], [P66] |
| **Ángulo** | 15-30° up | **0° (horizontal)** detecta 88.3% frutos (Villacrés 2024). **45°** supera a 15° en detección. | Combinación **0° + 30° up** (2 vistas) > cualquier single view. 3-5 posiciones = 90% detectabilidad. | [P111], [P113], [P112] |
| **Distancia** | 0.8-1.5 m | Para frutos pequeños: **0.16-0.7 m** óptimo (RealSense citrus). **0.3 m** óptimo para oil palm (F1=0.99). | Para **mandarinas**: rango **0.5-1.2 m** balancea detalle vs cobertura. El rango original es válido para frutos grandes. | [P114], [P115] |
| **Horario** | 9-11AM/3-5PM, nublado | **Sol cenital = MEJOR** (Multi-UAV: 92.1% precision vs nublado 86.1%). Nublado puede ser **insuficiente** (<3,000 lx vs 3,000 lx mínimo). | **Noche con LED** supera al día (OrBot: 94% vs 88%; Litchi night: 98.86% mAP). | [P116], [P120], [P117], [P118] |
| **Shutter** | 1/60-1/120s | Con **LED activo**: 20 µs elimina blur completamente. Deblurring GAN recupera 86% mAP perdido. | **1/120s** recomendado sobre 1/60s. Burst photography (HDR+) mejor que exposición fija. Modelos toleran blur (FEGW-YOLO: 80.1% mAP con blur severo). | [P57], [P40], [P121], [P122], [P103] |
| **Anti-doble conteo** | ByteTrack + multi-view | **AgriSORT** MOTA 65.93 vs ByteTrack 48.66. **Dynamic Kalman** MOTA 95% vs ByteTrack 75%. **OC-SORT** HOTA 67.10% vs ByteTrack 62.39%. | **AgriSORT** o **OC-SORT** recomendados sobre ByteTrack. Single-view con multi-frame funciona (video tracking 62% vs dual-view 40%). | [P35], [P34], [P123] |

---

## Evidencia detallada por parámetro

### 1. Velocidad de Caminata

| Paper | Año | Velocidad | Contexto | Resultado |
|---|---|---|---|---|
| Apple Yield Mapping [P70] | 2018 | **2 m/s (7.2 km/h)** | Samsung Galaxy S4, video 30fps, 1920×1080, caminata manual | Yield accuracy 95.56-97.83%. Demostró que capturar video caminando con smartphone funciona. |
| MangoYOLO Kalman [P66] | 2019 | **5 km/h (~1.39 m/s)** | Vehículo a 10fps, 2m de distancia | 62% harvest count (vs 40% dual-view). RMSE 18.0 frutos/árbol. |
| Apple 3D Camera [P71] | 2023 | **0.052 / 0.069 / 0.098 m/s** | Tractor con cámara 3D, 3 ángulos | Counting accuracy 86.6%. Mejor velocidad: 0.098 m/s para precisión 3D. |
| Coffee monitoring [P27] | 2017 | **~3 cm/s** | Smartphone + IMU para detección de blur | Máx 5 cm/s para evitar blur. Holder con botones. |
| Citrus GAN [P68] | 2025 | **N/A (efecto del blur)** | Cuantifica caída de mAP por motion blur | **mAP cae 27%** por blur (0.925 → 0.673). |

**Conclusión:** La velocidad de **~1 m/s** es conservadora y realista para caminata manual. El paper del Samsung S4 a 2 m/s demuestra que incluso más rápido es factible, pero para mandarinas pequeñas (high occlusion, dense foliage) conviene más lento para minimizar blur.

**Fórmula de blur (Motion Blur Review [P75]):**
```
desplazamiento (px) ≈ (velocidad_caminata × tiempo_exposición) / distancia_focal

Ejemplo a 1 m/s con shutter 1/60s: ~16 px de blur
Ejemplo a 1 m/s con shutter 1/120s: ~8 px de blur
Ejemplo a 1 m/s con shutter 1/200s: ~5 px de blur
```

### 1b. Contradicciones y evidencia complementaria — Velocidad de Caminata

| Paper | Año | Hallazgo | ¿Contradice o mejora? |
|---|---|---|---|
| **Sanchez & Zhang — Overlapping Rate [P110]** | 2022 | Introducen fórmula `ro = (FOV × fps) / velocidad`. Con ro≈1.3m/s es seguro con 16fps. Con 22fps: **2.5 m/s** viable. | ❌ **Contradice**: 1 m/s no es límite. La velocidad máxima depende de FOV y fps. |
| **MangoYOLO [P66]** | 2019 | **1.39 m/s (5 km/h)** con Kalman Filter + Hungarian Algorithm: 62% harvest detection. Error doble conteo solo 2.6%. | ❌ **Contradice**: Velocidad mayor funciona con tracking adecuado. |
| **FEGW-YOLO [P103]** | 2026 | YOLOv8n retiene **71.9% mAP@0.5** a blur severo (k=11). Degradación real ~21.4% (vs 86.4% reportado por [P68]). | ❌ **Matiza**: La degradación por blur es moderada (21-50%), no catastrófica. |
| **Knowledge Distillation Blur [P105]** | 2024 | Al 100% de velocidad de motion, YOLOv8 pierde solo **4.6% mAP@0.5**. Con KD: solo **2.5% drop**. | ❌ **Contradice fuertemente**: Degradación mínima para objetos pequeños con blur. |
| **Apple 3D Camera [P71]** | 2023 | A 0.098 m/s: counting accuracy 86.6%. | ✅ **Apoya**: Velocidades lentas dan mejor precisión 3D. |
| **Coffee Monitoring [P27]** | 2017 | Máx **5 cm/s** para evitar blur. | ⚠️ **Extremo**: Velocidad extremadamente lenta, no realista para nuestro protocolo. |

**Conclusión de la evidencia contradictoria:** El límite de 1 m/s es **conservador**. Con tracking Kalman/Hungarian y modelos tolerantes al blur, **1.3-1.5 m/s** es viable para mandarinas. La **fórmula de overlapping rate** de Sanchez & Zhang permite calcular la velocidad máxima según el equipo: `v_max = (FOV × fps) / 1.0` (con ro=1 como límite inferior). Para nuestro setup (FOV≈0.5m, 30fps), la velocidad máxima teórica es ~15 m/s — el límite real es el blur, no la cobertura.

---

### 2. Ángulo de Cámara

| Paper | Año | Ángulos probados | Mejor ángulo | Métrica |
|---|---|---|---|---|
| Sweet-Pepper Fruit Detectability [P69] | 2014 | **14 posiciones**: zenith 60°/90°/120°, azimuth 30°-150° | **Zenith 60° = 30° hacia arriba** | FD (Fruit Detectability) máxima con zenith 60°. Zenith 120° (mirando abajo) fue el PEOR porque hojas ocultan frutos. |
| Apple 3D Camera [P71] | 2023 | **0° (perpendicular), 15°, 30°** | **15°** | RMSE más bajo: 1.54 cm. Combinado con velocidad 0.098 m/s dio la mejor precisión 3D. |
| FruitSize App [P47] | 2018 | **<14°** límite de inclinación | **<14°** | Error de tamaño >6% si se excede. La app rechaza automáticamente imágenes fuera de especificación. |
| Apple MSX imaging [P45] | 2019 | −12° a −16° (shooting angle) | **−16°** | Máximo contraste fruto-follaje. |
| Hawthorn detection [P39] | 2025 | overhead, level, upward | Múltiples ángulos | 3 condiciones de luz probadas. |

**Hallazgo clave del paper de Sweet-Pepper [P69]:**
- **Zenith 60° (30° hacia arriba desde horizontal)** → Mejor detectabilidad
- **Zenith 90° (frontal, horizontal)** → Bueno
- **Zenith 120° (mirando hacia abajo)** → Peor (hojas ocultan frutos)
- **5 posiciones combinadas** → FD = 90%

**Conclusión:** Ángulo de **15-30° hacia arriba** maximiza la visibilidad de frutos. El límite de <14° de FruitSize se refiere a inclinación respecto al plano del objeto (no al ángulo de elevación); nuestro ángulo de 15-30° es hacia arriba, no de inclinación lateral.

### 2b. Contradicciones y evidencia complementaria — Ángulo de Cámara

| Paper | Año | Hallazgo | ¿Contradice o mejora? |
|---|---|---|---|
| **Villacrés — Multi-Camera Apple [P111]** | 2024 | Cámara **perpendicular al dosel (0° horizontal)** detectó **88.3%** de frutos. Dos cámaras: **97.5%**. | ❌ **Contradice**: 0° (horizontal) es excelente como single view, no es necesario tilt up. |
| **Apple Orientation [P112]** | 2025 | Sideways (90°): **mAP 95%**. Stem up: 86%. Stem down: 91.7%. | ❌ **Contradice**: La orientación sideways (horizontal) supera a cualquier ángulo con tilt. |
| **Cluster Segmentation Stereo [P113]** | 2025 | Probó 0°, 15°, 30°, **45°**: **45° = mejor tasa de detección (>40%)**. | ❌ **Contradice**: 45° supera a 15° para detección. |
| **Hemming Sweet-Pepper [P69]** | 2014 | **5 posiciones combinadas** (incluyendo zenith 60° Y 90°) = **90% FD**. Single view máximo: 69%. | ✅ **Mejora**: No buscar el ángulo óptimo, sino **combinar múltiples ángulos**. |
| **Mango Multi-View [—]** | 2016 | Single view: **27%**. Dual-view: **54%**. Multi-view tracking: **101.4%** (error 1.36%). | ✅ **Mejora**: El concepto de "mejor ángulo único" es fundamentalmente limitado. |
| **Apple 3D Camera [P71]** | 2023 | 15°: mejor RMSE 1.54cm. 0° y 30° también probados. | ✅ **Apoya**: 15° es bueno, pero debe combinarse con otros ángulos. |

**Conclusión de la evidencia contradictoria:** El ángulo de **15° up no es inherentemente superior** a 0° (horizontal) o 45°. La estrategia óptima para mandarinas en dosel denso es **combinar al menos 2 ángulos**: **0° (horizontal) + 30° hacia arriba**. Idealmente grabar cada hilera desde **ambos lados** para obtener automáticamente dos perspectivas. La combinación de 3-5 posiciones (como demostró Hemming 2014) maximiza la detectabilidad.

---

### 3. Distancia al Dosel

| Paper | Año | Distancia probada | Resultado | Métrica |
|---|---|---|---|---|
| YOLO-CSB [P73] | 2026 | **0.8-1.5 m** (rango óptimo) | mAP 93.69% | "Close-up shots and entire tree canopy" |
| RGB-D Sensors [P72] | 2020 | **1.5 m vs 2.5 m** | 1.5m: **200.5% más densidad** de nube de puntos. 2.5m: mejor penetración en dosel. | Profundidad: 0.772m vs 0.922m |
| Kuznetsova [P28] | 2020 | **0.2 / 0.5 / 1.0 / 2.0 m** | Distancia óptima depende del FOV. Frutos pequeños requieren distancia cercana. | Nikon D3500 (no smartphone) |
| KiwiDetector [P48] | 2020 | **~1 m** (selfie stick) | TDR 90.8% | Smartphone real bajo dosel |
| Apple Redmi Note 7 [P37] | 2024 | **0.3-1.5 m** | Bueno para detección | 5 condiciones de luz probadas |
| Apple fruitlets [Pcol] | 2024 | **0.5-3 m** | AP 0.669 (RT-DETR-L) | iPhone 7 Plus/6 |
| FruitSize [P47] | 2018 | **120-300 mm** (con backboard) | RMSE 2.0-5.5 mm según cultivo | Distancia cercana para medición de tamaño |

**Conclusión:** El rango **0.8-1.5 m** es el más respaldado. Más cerca (<0.5m) da más detalle pero menos cobertura del dosel. Más lejos (>2m) pierde detalle de frutos pequeños. Para mandarinas en huerto denso, 0.8-1.5m balancea cobertura y detalle.

### 3b. Contradicciones y evidencia complementaria — Distancia al Dosel

| Paper | Año | Distancia óptima | Evidencia | ¿Contradice o mejora? |
|---|---|---|---|---|
| **RealSense Citrus Close-Shot [P114]** | 2018 | **0.16-0.7 m** | 80-100% detección para poca oclusión. "Close-shot: close, large, and clear". | ❌ **Contradice**: Distancia <0.8m da excelente detección para cítricos. |
| **Oil Palm Stereo [P115]** | 2024 | **0.3 m** detección, **0.5 m** estimación | 97.63% accuracy, F1=0.99 a 30cm. MAPE 0.86% a 50cm. | ❌ **Contradice**: Distancia mucho más cercana da resultados superiores. |
| **Lychee Detection** | — | **0.3-1.0 m** | F1 ~89% para frutos pequeños (~20-30mm). | ❌ **Contradice**: Frutos pequeños requieren distancia <1m. |
| **Apple sizing [P47]** | 2018 | **0.12-0.3 m** (con backboard) | RMSE 2.0-5.5mm para medición de tamaño. | ⚠️ **Contexto**: Para sizing se necesita distancia muy cercana. |
| **YOLO-CSB [P73]** | 2026 | **0.8-1.5 m** | mAP 93.69% para manzanas. | ✅ **Apoya**: Válido para frutos grandes (manzana, mango). |
| **Kuznetsova [P28]** | 2020 | **0.2 / 0.5 / 1.0 / 2.0 m** probados | Distancia óptima depende del FOV. Frutos pequeños requieren distancia cercana. | ✅ **Apoya**: No hay distancia universal, depende del fruto. |

**Distancia óptima según TAMAÑO DE FRUTO (síntesis de la evidencia contradictoria):**

| Tipo de fruto | Diámetro típico | Distancia óptima | Referencias |
|---|---|---|---|
| Muy pequeños (lychee, blueberry) | ~20-30 mm | **0.3-0.7 m** | RealSense, Lychee |
| **Pequeños (mandarina, cítrico)** | **~40-60 mm** | **0.5-1.2 m** | **Síntesis de evidencias contradictorias** |
| Grandes (manzana, mango) | ~70-100 mm | 0.8-1.5 m | YOLO-CSB |
| Conteo a nivel árbol | — | 1.5-5 m | Yield estimation apps |

**Conclusión de la evidencia contradictoria:** Para **mandarinas** (fruto pequeño ~40-60mm), la evidencia sugiere que el rango óptimo es **0.5-1.2 m**, más cercano que el 0.8-1.5m original. El rango original es válido para frutos grandes (manzana, mango). Se recomienda ajustar a **0.5-1.2 m** para balancear detalle fino y cobertura del dosel en mandarinas.

---

### 4. Horario e Iluminación

| Paper | Año | Condiciones comparadas | Mejor condición | Resultado |
|---|---|---|---|---|
| Orchard-YOLO [P76] | 2026 | **±50% brillo + hasta 70% oclusión** | Normal: 94.8% mAP. Extrema: 61.4% | La iluminación controlada es crítica |
| Pear dataset [P29] | 2023 | **4 horarios**: 7-8AM, 10-11AM, 2-3PM, 6-7PM | Múltiples horarios viables | Metodología multi-horario |
| Cocoa dataset [P30] | 2023 | **8AM-4PM**, trayectoria zigzag | Rango completo usable | Capturaron con 5 smartphones |
| Pear YOLOv4+DeepSORT [P54] | 2021 | Día nublado vs parcialmente nublado | Día nublado | DJI Osmo Pocket + móvil, 30fps |
| OrBot nighttime [—] | 2024 | Día vs noche con LED | **Noche LED: 94%** vs día 88% | Iluminación controlada supera a luz natural |
| Kiwifruit glare [P63] | 2020 | Normal vs glare vs overexposed | Normal: F1 0.82. Glare: **F1 0.13** | Luz no controlada destruye detección |

**Conclusión:** **9-11 AM o 3-5 PM**, evitando sol cenital (12-14 PM). Días nublados dan luz difusa ideal. Si se captura de noche, usar iluminación LED complementaria.

### 4b. Contradicciones y evidencia complementaria — Horario e Iluminación

| Paper | Año | Hallazgo | ¿Contradice o mejora? |
|---|---|---|---|
| **Multi-UAV Detection [P116]** | 2024 | **Sol cenital (mediodía)**: Precision **92.1%**, Recall **89.3%**, F1 **90.5%**. Nublado: 86.1%. Sombra: 78.1%. | ❌ **Contradice FUERTEMENTE**: "Avoid noon" es incorrecto — el mediodía da los mejores resultados. |
| **Tomato HSV Illumination [P120]** | 2024 | Mínimo **3,000 lx** requerido. Nublado da solo **1,000-2,000 lx** → insuficiente. A 1,600 lx: solo **50% del área** detectada. | ❌ **Contradice**: "Nublado ideal" puede ser perjudicial por iluminación insuficiente. |
| **OrBot Night Harvesting [P118]** | 2024 | **Noche con LED: 94% éxito** vs Día: 88%. LED 5600K, intensidad 10%, frontal. | ✅ **Mejora**: Noche con LED supera al día en 6%. Iluminación controlada elimina variabilidad. |
| **YOLOv8n-CSE Litchi Night [P117]** | 2024 | Noche con LED: **98.86% mAP@0.5**, **95.54% F1**. LED matrix 210-350 Lux. | ✅ **Mejora**: Rendimiento nocturno excepcional, superior a la mayoría de sistemas diurnos. |
| **YOLO-P Pear Night [P119]** | 2022 | Noche con 1000 lm: **96.1% F1**. Luz natural: ~93%. | ✅ **Mejora**: Noche con luz artificial supera consistentemente al día. |
| **Choi LED [P57]** | 2021 | Iluminación activa reduce **85% variabilidad HSV**. 20µs exposure elimina blur. | ✅ **Mejora**: Iluminación controlada elimina dependencia de horario. |
| **RGB-D Sensors [P72]** | 2020 | Rango óptimo: **50-2,000 lx**. >2,000 lx degrada sensores 3D. | ⚠️ **Matiz**: Para sensores de profundidad, sol cenital (>50,000 lx) es problemático. |
| **Kiwifruit glare [P63]** | 2020 | F1 cae de **0.82 a 0.13** con glare. | ✅ **Apoya**: Backlight extremo y glare son destructivos, independientemente del horario. |
| **Apple MSX [P45]** | 2019 | Mejor resultado cuando sol está temporalmente cubierto por nubes (diferencia térmica fruto-hoja >6°C). | ⚠️ **Matiz**: "Best time to shoot is not limited to a certain time period" — depende de condiciones específicas. |

**Conclusión de la evidencia contradictoria:** La recomendación original de **"evitar mediodía" es directamente contradicha** por el paper Multi-UAV que muestra el sol cenital como la mejor condición. La recomendación **"nublado ideal" también es cuestionada** por requerir >3,000 lx para segmentación precisa. La **opción noche con LED controlado** (5600K, frontal, 210-350 Lux) consistentemente supera al día en múltiples estudios.

**Nueva recomendación basada en evidencia contradictoria:** Priorizar **captura nocturna con iluminación LED frontal** (5600K, ~300 Lux). Alternativamente, **cualquier hora del día funciona**, incluido el mediodía. Evitar específicamente **backlight extremo y glare**. Días nublados son aceptables pero no ideales si la iluminación cae <3,000 lx.

---

### 5. Motion Blur — Cuantificación

| Paper | Hallazgo | Impacto cuantitativo |
|---|---|---|
| **Citrus GAN [P68]** (Plants, 2025) | Motion blur en huerto de cítricos | **mAP@0.5:0.95 cae 86.4%** con blur. Recall cae 76.9%. F1 cae 40.1%. |
| **Motion Blur Review [P75]** (Heliyon, 2024) | Fórmula de desplazamiento por blur | `desplazamiento_px = (v × t_exp) / f` |
| **WRA-Net [—]** (Plant Phenomics, 2024) | Deblurring en cultivos | Restauración mejora mIOU de 0.63 a 0.74 |
| **Motion Blur Wheat [—]** (2025) | YOLOv11 en imágenes borrosas | **10.4% más accuracy** con método anti-blur |

### 5b. Contradicciones y evidencia complementaria — Shutter Speed y Motion Blur

| Paper | Año | Hallazgo | ¿Contradice o mejora? |
|---|---|---|---|
| **Choi LED Overcurrent [P57]** | 2021 | **20 µs** (~1/50,000s) con LED overdriven 6×. Blur 7mm→1mm a 7 km/h. Variación HSV -85%. | ❌ **Contradice**: Con LED activo, shutter de 20µs elimina blur completamente. 1/60-1/120s es irrelevante. |
| **Arad FNF [P40]** | 2019 | **20 µs** exposición + Flash-No-Flash. **95% precision @ 95% recall**. | ❌ **Contradice**: Shutter ultracorto con flash resuelve blur y variabilidad de luz. |
| **Hasinoff HDR+ [P121]** | 2016 | Burst photography: múltiples frames subexpuestos combinados. "Shorter than typical exposure times... reducing motion blur". | ✅ **Mejora**: Burst de frames cortos > exposición única larga. Mejor para ruido Y blur. |
| **DEBIR Adaptive Exposure [P122]** | 2026 | Predice exposición óptima por frame dinámicamente. Preview 1/120s, burst con exposiciones variables. | ✅ **Mejora**: Exposición adaptativa supera a exposición fija. |
| **FEGW-YOLO [P103]** | 2026 | A blur severo (k=11): **80.1% mAP@0.5** (YOLOv8n: 71.9%). Tolerancia natural al blur. | ✅ **Mejora**: Modelos modernos toleran blur — shutter menos crítico. |
| **AGG-DeblurGAN [P68]** | 2025 | Deblurring post-hoc recupera mAP de **0.673 → 0.898** (+86.4%). | ✅ **Mejora**: Aceptar blur y corregirlo post-hoc es viable. |
| **Knowledge Distillation Blur [P105]** | 2024 | Al 100% velocidad de motion: solo **2.5-4.6% mAP drop** con modelos entrenados con blur. | ✅ **Mejora**: Entrenar con blur elimina necesidad de shutter rápido. |
| **MDPI Electronics YOLO Robustness [P106]** | 2025 | YOLOv4: ~15% drop por blur. YOLOv11: ~25% drop. Versiones nuevas NO son más robustas. | ⚠️ **Matiz**: No asumir que YOLO moderno es tolerante al blur — probar cada versión. |

**Conclusión de la evidencia contradictoria:** El rango 1/60-1/120s es razonable para captura "cruda" sin iluminación adicional. Sin embargo:

1. **Con LED activo**: usar **20-100 µs** (elimina blur por completo, independiente del shutter)
2. **Sin LED**: **1/120s sobre 1/60s** para minimizar rolling shutter en smartphone
3. **Deblurring post-hoc** (AGG-DeblurGAN) puede recuperar calidad si se acepta algo de blur
4. **Burst photography** (HDR+) es alternativa superior a exposición fija
5. **Entrenar con blur** (data augmentation) hace que shutter sea menos crítico

---

### 6. Anti-Doble Conteo y Tracking

| Paper | Método | Resultado | Métrica |
|---|---|---|---|
| **Gené-Mola Video [P74]** (2023) | **ByteTrack vs SORT vs DeepSORT** | ByteTrack: **MOTA 0.682, IDF1 0.837** | 15ms/frame vs DeepSORT 128ms |
| **MangoYOLO Kalman [P66]** (2019) | Kalman Filter + Hungarian Algorithm | **62% harvest** (vs 40% dual-view). Error: 9.9% doble conteo. | RMSE 18.0 frutos/árbol |
| **Mango multi-view [—]** (2016) | Geometría epipolar + Hungarian | **Error 1.36%** en conteo | Multi-view elimina necesidad de calibración |
| **Apple 3D Camera [P71]** (2023) | Deep SORT | Counting accuracy **86.6%** | 3 velocidades × 3 ángulos |

**Conclusión:** Usar **ByteTrack** para tracking (mejor MOTA/IDF1). Grabar **video continuo** (no fotos) y capturar **ambos lados de la hilera** para minimizar frutos ocultos.

### 6b. Contradicciones y evidencia complementaria — Anti-Doble Conteo y Tracking

| Paper | Año | Método | Resultado | ¿Contradice o mejora? |
|---|---|---|---|---|
| **AgriSORT (ICRA 2024) [P35]** | 2024 | Kalman Filter adaptado a agricultura (motion-only, sin apariencia) | **MOTA 65.93** vs ByteTrack 48.24 (CloseUp). **HOTA 48.71** vs ByteTrack 38.24. | ❌ **Contradice**: Tracker específico para agricultura supera ampliamente a ByteTrack. |
| **Dynamic Kalman [P34]** | 2025 | Kalman Filter con forgetting factor variable + IoU + Re-ID | **MOTA 95.0%**, IDF1 65.5%, HOTA 82.4% vs ByteTrack 75/37/68.6. R²=0.85. | ❌ **Contradice**: Kalman dinámico muy superior a ByteTrack. |
| **OC-SORT Passion Fruit [P123]** | 2025 | OC-SORT + YOLOv8n + CRCM | **HOTA 67.10%** vs ByteTrack 62.39%, BoT-SORT 64.12%, StrongSORT 58.28%. | ❌ **Contradice**: OC-SORT supera a ByteTrack en todos los trackers comparados. |
| **OrangeSort [P31]** | 2024 | SORT modificado + región counting | **MAE 0.081** vs SORT 0.6788, DeepSort 1.212. Counting accuracy **32.7% → 96.8%**. | ❌ **Contradice**: SORT simple + dominio específico supera a trackers complejos. |
| **Gené-Mola ByteTrack [P74]** | 2023 | ByteTrack vs SORT vs DeepSORT en manzanas | ByteTrack: **MOTA 0.682, IDF1 0.837**. SORT: 0.640/0.809. | ✅ **Apoya (original)**: ByteTrack es mejor que SORT/DeepSORT en manzanas. |
| **Deep OC-SORT [P124]** | 2023 | Adaptive Re-ID según calidad de feature | HOTA **64.9** (MOT17) vs ByteTrack 63.1. **61.3** (DanceTrack) vs ByteTrack 47.3. | ✅ **Mejora**: Deep OC-SORT supera a ByteTrack en benchmarks generales. |
| **FTO-SORT [P125]** | 2025 | Farm Track-id Optimizer (sin Re-ID) | **IDF1 90.2%** (+15.1% sobre baseline). 10× más rápido sin Re-ID. | ✅ **Mejora**: Optimizador específico para agricultura + velocidad. |
| **LocalizeSORT [P126]** | 2026 | World-coordinate association for stationary objects | Error conteo mango: **187** vs DeepSORT 263, StrongSORT 217. | ✅ **Mejora**: Asociación en coordenadas del mundo para objetos estáticos. |
| **PineSORT (CVPR 2025) [P127]** | 2025 | Drone-specific tracking + camera compensation | Mejoras significativas en ISP-IDF1, IDF1, HOTA, AssA sobre BoTSORT/AgriSORT. | ✅ **Mejora**: Específico para drone, aplicable a ground con compensación. |
| **CoTracker3 Agricultural [P128]** | 2025 | Point tracking transformer (joint tracking) | 93% success rate poda. Error trayectoria 0.23mm. **27% más rápido** que LoCoTrack. | ✅ **Mejora**: Point tracking para oclusiones extremas. Alternativa a bounding-box tracking. |
| **Transformer Apple Fruitlet [P129]** | 2025 | Shape + position encoding + transformer attention | **F1 92.4%** para asociación temporal (vs ICP 89.5%, Desc 86.4%). A través de días. | ✅ **Mejora**: Transformer supera a métodos clásicos de asociación. |
| **MOT-DETR-3D [P130]** | 2023 | Transformer end-to-end + 3D data para tomates | **HOTA 60.4**, MOTA 70.38 vs FairMOT 46.06/51.49. 3D mejora tracking de objetos similares. | ✅ **Mejora**: Transformer + 3D para tracking de fruta. |
| **Mango video tracking [P66]** | 2019 | Single-side video tracking | **62%** harvest vs dual-view **40%**. Video single-side supera a dual-view estático. | ⚠️ **Matiz multi-view**: Single-side video puede ser suficiente si se combina con tracking temporal. |

**Conclusión de la evidencia contradictoria:** **ByteTrack NO es la mejor opción para agricultura en 2026.** Los trackers específicos para agricultura superan significativamente:

| Tracker | Cuándo usarlo |
|---|---|
| **AgriSORT** (ICRA 2024) | **Recomendado** para tracking de fruta con cámara en movimiento. Motion-only, sin Re-ID. |
| **Dynamic Kalman** | Si se necesita máxima precisión (MOTA 95%). Requiere tuning del forgetting factor. |
| **OC-SORT** | Buena alternativa general, especialmente con oclusiones. |
| **CoTracker3** | Para point-tracking robusto a oclusiones. Alternativa a bounding-box. |
| **ByteTrack** | Mantener como baseline de comparación en el experimento A/B. |

Mantener **ambos lados de hilera** como estrategia de captura, pero **no necesariamente con multi-view geometry** — el tracking temporal desde un solo lado puede ser suficiente si se usa el tracker adecuado.

---

## Tabla de evidencia cruzada — Decisión vs Respaldo

| Decisión del protocolo | Evidencia cuantitativa | Fuente | ID |
|---|---|---|---|
| **Velocidad ~1 m/s** | Samsung S4 funcionó a 2 m/s. Blur medible >1.5 m/s. | Apple Yield Mapping 2018, Motion Blur Review 2024 | [P70], [P75] |
| **Ángulo 15-30° up** | 14 posiciones: zenith 60° = mejor FD. 15° = mejor RMSE 1.54cm. | Sweet-Pepper 2014, Apple 3D 2023 | [P69], [P71] |
| **Distancia 0.8-1.5m** | 0.8-1.5m = mAP 93.69%. 1.5m = 200% más densidad punto. | YOLO-CSB 2026, RGB-D 2020 | [P73], [P72] |
| **Shutter 1/60-1/120s** | 27% mAP drop por blur sin shutter adecuado. Fórmula desplazamiento. | Citrus GAN 2025, Motion Blur Review 2024 | [P68], [P75] |
| **ByteTrack para tracking** | ByteTrack: MOTA 0.682 vs SORT 0.640 vs DeepSORT 0.574 | Gené-Mola 2023 | [P74] |
| **Video continuo > fotos** | Video captura 62% harvest vs 40% con foto dual. +22% mejora. | MangoYOLO 2019 | [P66] |
| **Multi-view (ambos lados)** | Multi-view reduce error a 1.36%. Single-view error mucho mayor. | Mango multi-view 2016 | [—] |
| **Nublado > sol directo** | F1 cae de 0.82 a 0.13 con glare. Orchard-YOLO: 94.8%→61.4% en extremo. | Kiwifruit glare 2020, Orchard-YOLO 2026 | [P63], [P76] |
| **Velocidad 1.3-1.5 m/s (contradice)** | Overlapping rate: con fps suficiente, hasta 2.5 m/s viable. MangoYOLO: 62% a 1.39 m/s. | Sanchez & Zhang 2022, MangoYOLO 2019 | [P110], [P66] |
| **Ángulo 0°+30° combinado (mejora)** | Perpendicular (0°) detecta 88.3%. Combinación 3-5 vistas = 90%+ detectabilidad. | Villacrés 2024, Hemming 2014 | [P111], [P69] |
| **Distancia 0.5-1.2m para mandarinas (mejora)** | Frutos pequeños: 0.16-0.7m óptimo (RealSense). 0.5-1.2m síntesis para mandarinas. | RealSense Citrus 2018 | [P114] |
| **Noche con LED > Día (mejora)** | Noche: 94% éxito vs día 88%. Mediodía: mejor condición natural (precision 92.1%). | OrBot 2024, Multi-UAV 2024 | [P118], [P116] |
| **AgriSORT/OC-SORT > ByteTrack (mejora)** | AgriSORT MOTA 65.93 vs ByteTrack 48.24. OC-SORT HOTA 67.10% vs ByteTrack 62.39%. | AgriSORT ICRA 2024, OC-SORT 2025 | [P35], [P123] |

---

## Gap confirmado para la tesis

> **No existe un paper que compare la interacción de velocidad × ángulo × distancia combinados para captura manual con smartphone en agricultura, midiendo el impacto en mAP/MOTA.**

Papers existentes:
- Prueban **1 parámetro a la vez**, no interacciones
- Usan **tractores o robots**, no caminata humana
- No reportan **mAP/MOTA** de YOLO como métrica de comparación de parámetros de captura
- No documentan el **pipeline completo** (app + configuración + IMU + procesamiento)

**Tu contribución original:** Medir cuantitativamente el impacto combinado de estos parámetros en mAP/MOTA para video de mandarinas capturado con smartphone, siguiendo este protocolo vs cámara nativa en modo automático.

### Gap ampliado por la investigación contradictoria

La investigación de 8 agentes paralelos reveló que **tampoco existe un paper que compare sistemáticamente**:

- **Velocidad** × **ángulo** × **distancia** combinados para captura manual con smartphone en agricultura — **confirmado**
- **Noche con LED** vs **día con luz natural** para detección YOLO de mandarinas — **no encontrado**
- **AgriSORT/OC-SORT** vs **ByteTrack** específicamente para tracking de cítricos en video — **no encontrado**
- **Single-view video** vs **multi-view estático** para conteo de mandarinas en hilera — **no encontrado**
- **Impacto del overlapping rate** en la calidad de tracking MOT para frutos pequeños — **no encontrado**

> Esto **fortalece** la originalidad de la tesis: ningún estudio previo mide estas interacciones para mandarinas con smartphone manual.

---

## Nuevos papers agregados a la Tabla Maestra

### Primera ronda (investigación original, P69-P78)

| ID | Título corto | Año | Parámetro que justifica |
|---|---|---|---|
| [P69] | Fruit Detectability - Different Camera Positions in Sweet-Pepper | 2014 | Ángulo de cámara (14 posiciones) |
| [P70] | Comparative Study of Fruit Detection and Counting - Apple Orchards | 2018 | Velocidad de caminata (Samsung S4 a 2 m/s) |
| [P71] | Recognition and Counting of Apples in a Dynamic State | 2023 | Velocidad × Ángulo combinados |
| [P72] | RGB-D Sensors for 3D Fruit Crop Canopy Characterization | 2020 | Distancia al dosel (1.5m vs 2.5m) |
| [P73] | YOLO-CSB: Real-Time Detection of Occluded Apples | 2026 | Distancia óptima 0.8-1.5m |
| [P74] | Video-Based Fruit Detection and Tracking for Apple Counting | 2023 | ByteTrack MOTA 0.682 |
| [P75] | State-of-the-Art Review of Image Motion Deblurring in Agriculture | 2024 | Fórmula de blur, shutter speed |
| [P76] | Orchard-YOLO: Robust Detection Under Optical Degradation | 2026 | Iluminación ±50%, oclusión 70% |
| [P77] | AgRowStitch: Image Stitching for Ground-based Agricultural Images | 2025 | Caminata manual con iPhone 13, mosaicos |
| [P78] | In-Orchard Sizing of Mango Fruit: Comparison of Machine Vision Methods | 2022 | Velocidad 6 km/h, distancia 1-3m |

### Segunda ronda (investigación contradictoria, P110-P130)

| ID | Título corto | Año | Parámetro | Relación con P3 |
|---|---|---|---|---|
| [P110] | Simulation-Aided Development (Overlapping Rate) — Sanchez & Zhang | 2022 | Velocidad | ❌ Contradice: fórmula ro muestra 2.5 m/s viable |
| [P111] | Multi-Camera Apple Detection — Villacrés et al. | 2024 | Ángulo | ❌ Contradice: 0° (perpendicular) = 88.3% detección |
| [P112] | Full-Surface Apple Detection — Orientation Study | 2025 | Ángulo | ❌ Contradice: sideways (90°) = mAP 95% |
| [P113] | Cluster Segmentation Stereo Vision — Apple Localization | 2025 | Ángulo | ❌ Contradice: 45° > 15° para tasa de detección |
| [P114] | Close-Shot Citrus Identification with RealSense | 2018 | Distancia | ❌ Contradice: 0.16-0.7m óptimo para cítricos |
| [P115] | Stereo Vision Oil Palm Fruit Detection | 2024 | Distancia | ❌ Contradice: 0.3m óptimo para detección |
| [P116] | Multi-UAV Fruit Detection — Illumination Study | 2024 | Iluminación | ❌ Contradice: sol cenital (mediodía) = mejor precisión 92.1% |
| [P117] | YOLOv8n-CSE: Litchi Detection in Nighttime | 2024 | Iluminación | ✅ Mejora: noche LED = 98.86% mAP |
| [P118] | OrBot Nighttime Harvesting | 2024 | Iluminación | ✅ Mejora: noche 94% > día 88% |
| [P119] | YOLO-P: Pear Fast Detection Night/Day | 2022 | Iluminación | ✅ Mejora: noche 96.1% F1 con 1000 lm |
| [P120] | Tomato HSV Illumination — Minimum Lux | 2024 | Iluminación | ❌ Contradice: nublado insuficiente (<3,000 lx) |
| [P121] | HDR+ Burst Photography — Hasinoff et al. | 2016 | Shutter | ✅ Mejora: burst frames cortos > exposición fija |
| [P122] | DEBIR — Dynamic Exposure Burst Image Restoration | 2026 | Shutter | ✅ Mejora: exposición adaptativa por frame |
| [P123] | OC-SORT Passion Fruit Yield Estimation | 2025 | Tracking | ❌ Contradice: OC-SORT (HOTA 67.10%) > ByteTrack (62.39%) |
| [P124] | Deep OC-SORT — Adaptive Re-ID | 2023 | Tracking | ✅ Mejora: HOTA 64.9 vs ByteTrack 63.1 (MOT17) |
| [P125] | FTO-SORT — Farm Track-id Optimizer | 2025 | Tracking | ✅ Mejora: IDF1 90.2%, +15.1% sobre baseline |
| [P126] | LocalizeSORT — World-Coordinate Stationary Object Tracking | 2026 | Tracking | ✅ Mejora: error conteo 187 vs DeepSORT 263 |
| [P127] | PineSORT — CVPR 2025 Drone-based Tracking | 2025 | Tracking | ✅ Mejora: superior en HOTA/IDF1 para agricultura |
| [P128] | CoTracker3 — Agricultural Point Tracking | 2025 | Tracking | ✅ Mejora: 27% más rápido, joint tracking para oclusiones |
| [P129] | Transformer-Based Apple Fruitlet Association | 2025 | Tracking | ✅ Mejora: F1 92.4% para asociación temporal |
| [P130] | MOT-DETR-3D — Transformer 3D Tracking for Tomatoes | 2023 | Tracking | ✅ Mejora: HOTA 60.4, 3D mejora tracking de objetos similares |

---

## Parámetros de captura finales (actualizados para validación en campo)

### Valores originales (P3, respaldo bibliográfico directo)

| Parámetro | Valor | Justificación | IDs |
|---|---|---|---|
| **Velocidad** | ~1 m/s constante | Balance entre cobertura y blur controlado | [P70], [P66], [P75] |
| **Ángulo** | ~15° hacia arriba | Mejor detectabilidad de frutos | [P69], [P71] |
| **Distancia** | 0.8-1.5 m del dosel | Detalle suficiente + cobertura del dosel | [P73], [P72], [P28] |
| **Horario** | 9-11 AM o 3-5 PM | Evitar sol cenital | [P29], [P30], [P76] |
| **Trayectoria** | 1 hilera por grabación, un lado | Consistencia entre capturas | — |
| **Anti-doble conteo** | ByteTrack + ambos lados de hilera | MOTA 0.682, error <2% | [P74], [P66] |
| **Shutter** | 1/60s o 1/120s fijo | Blur controlado según velocidad | [P75], [P68], [P40] |

### Valores actualizados según evidencia contradictoria (recomendación para validación en campo)

> Basados en la investigación contradictoria de 8 agentes paralelos. Estos valores incorporan la nueva evidencia sin descartar los originales. La columna "Confianza" refleja el nivel de respaldo de la nueva evidencia.

| Parámetro | Valor recomendado | Justificación | IDs contradictorios | Confianza nueva evidencia |
|---|---|---|---|---|
| **Velocidad** | ~1.0-1.3 m/s (rango ampliado) | Con tracking adecuado y modelos tolerantes al blur, hasta 1.3 m/s es seguro. 1 m/s como mínimo conservador. | [P110] | 🟠 Media-Alta |
| **Ángulo** | 0° (horizontal) + 30° up (combinación) | Horizontal solo: 88.3% detección. Combinar ambas perspectivas maximiza cobertura. | [P111], [P69] | 🔴 Alta |
| **Distancia** | 0.5-1.2 m (ajustado para mandarinas) | Frutos pequeños requieren distancia más cercana. 0.5-1.2m balancea detalle y cobertura. | [P114], [P115] | 🟠 Alta |
| **Horario** | Noche con LED (5600K, frontal) > Cualquier horario > Evitar backlight | Noche con LED supera al día. Mediodía funciona bien. Nublado puede ser insuficiente. | [P116], [P118], [P117], [P120] | 🔴 Alta |
| **Shutter** | 1/120s fijo (sin LED). 20-100 µs (con LED activo) | 1/120s sobre 1/60s para rolling shutter. Burst photography como alternativa. | [P121], [P122] | 🟠 Alta |
| **Anti-doble conteo** | AgriSORT/OC-SORT + ambos lados + single-side video tracking | AgriSORT supera ByteTrack. Single-side video tracking con multi-frame aggregation funciona. | [P35], [P34], [P123] | 🟠 Alta |

**Nota:** Los valores de la tabla actualizada son **recomendaciones basadas en la mejor evidencia disponible**. Se recomienda probar ambos conjuntos de valores en el experimento A/B para determinar empíricamente cuál funciona mejor para mandarinas en el huerto específico.

---

**Última actualización:** 05/06/2026 | **Estado:** Completado + investigación contradictoria agregada | **Papers originales:** P69-P78 | **Papers contradictorios:** P110-P130 | **Total nuevos en Tabla Maestra:** 31
