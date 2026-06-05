# Bibliografía del Paso 4 — Selección de Parcelas

> Buscar cada título completo en **Google Scholar** (pegarlo entre comillas).
> Descargar PDF y renombrar como `PXX-titulo-corto.pdf` dentro de esta carpeta.

---

## Grupo A — Respaldo DIRECTO a la selección (7 imprescindibles)

### P82
- **Título:** "A New, Satellite NDVI-Based Sampling Protocol for Grape Maturation Monitoring"
- **Autores:** Meyers, J.M.; Dokoozlian, N.; Ryan, C.; Bioni, C.; Vanden Heuvel, J.E.
- **Revista:** *Remote Sensing*, 2020, 12(7), 1159
- **Hallazgo clave:** NDVI3: 3 píxeles Landsat representando cola baja, media y alta del NDVI. Misma representatividad que 20 puntos aleatorios.
- **Justifica en P4:** Principio de usar NDVI satelital para seleccionar por cuantiles extremos.

### P84
- **Título:** "Effectiveness of Management Zones Delineated from UAV and Sentinel-2 Data for Precision Viticulture Applications"
- **Autores:** —
- **Revista:** *Remote Sensing*, 2024, 16(4), 635
- **Hallazgo clave:** Sentinel-2 (10m) captura las principales zonas de vigor a nivel parcela, comparable a UAV de 3-4cm.
- **Justifica en P4:** Valida que S2-10m sirve para caracterizar/estratificar parcelas.

### P85
- **Título:** "Machine Learning Applied to Tree Crop Yield Prediction Using Field Data and Satellite Imagery: A Case Study in a Citrus Orchard"
- **Autores:** Moussaid, A.; El Fkihi, S.; Zennayi, Y.; Lahlou, O.; Kassou, I.; Bourzeix, F.; El Mansouri, L.; Imani, Y.
- **Revista:** *Informatics*, 2021, 9(3), 80 (también indexado como MDPI Instruments, 2022)
- **Hallazgo clave:** Usó mean NDVI de Sentinel-2 para caracterizar 50 parcelas de cítricos (mandarina Afourer).
- **Justifica en P4:** Valida el uso de mean NDVI S2 en cítricos para describir vigor entre parcelas.

### P88
- **Título:** "Multilevel Systematic Sampling to Estimate Total Fruit Number"
- **Autores:** Wulfsohn, D.; Aravena, F.; Potin, C.; Zamora, I.; García-Fiñana, M.
- **Revista:** *Precision Agriculture*, 2012 (Springer)
- **Hallazgo clave:** SUR sistemático en 14 huertos comerciales (kiwi, manzana, uva). Error <5% en 6 huertos, 5-10% en 5 huertos.
- **Justifica en P4:** La selección de hileras 3, 7, 11 mediante SUR.

### P90
- **Título:** "Fruit Yield Estimation of Kinnow Mandarin (Citrus reticulata) Orchards – Integrating Canopy Physiology with Remote Sensing"
- **Autores:** Sun, Y.; Qin, Q.; Zhang, J.; Ren, H.; Han, R.
- **Revista:** *Arabian Journal of Geosciences*, 2026, 19, 126
- **Hallazgo clave:** Usó Sentinel-2 Red Edge para mandarina Kinnow. R² = 0.85. Variabilidad intra-huerto significativa.
- **Justifica en P4:** Variedad más cercana a Murcott. Valida que S2 captura variabilidad en mandarinos.

### P91
- **Título:** "Comparing Efficiency of Different Sampling Schemes to Estimate Yield and Quality Parameters in Fruit Orchards"
- **Autores:** Arnó, J.; Martínez-Casasnovas, J.A.; Uribeetxebarria, A.; Escolà, A.; Rosell-Polo, J.R.
- **Revista:** *Advances in Animal Biosciences*, 2017, 8(2), 471-476
- **Hallazgo clave:** Estratificación por NDVI es significativamente más eficiente que aleatorio simple. Con 2 estratos se captura la mayor parte de la variabilidad.
- **Justifica en P4:** Seleccionar extremos (2 estratos) es mejor que el azar.

### P92
- **Título:** "Delineating Citrus Management Zones Using Spatial Interpolation and UAV-Based Multispectral Approaches"
- **Autores:** Longo-Minnolo, G. et al.
- **Revista:** *Precision Agriculture*, 2023, 24(5), 1570-1592 (Springer)
- **Hallazgo clave:** Delineó zonas de manejo en cítricos con NDVI (K-means). Zonas con diferente vigor mostraron diferencias estadísticamente significativas.
- **Justifica en P4:** Valida en cítricos que dividir por vigor captura diferencias reales.

---

## Grupo B — Contexto y Caracterización (4 papers)

### P79
- **Título:** "Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards"
- **Autores:** Miranda, C.; Santesteban, L.G.; Urrestarazu, J.; Loidi, M.; Royo, J.B.
- **Revista:** *Agriculture*, 2018, 8(6), 78
- **Hallazgo clave:** NDVI aéreo (0.25m) + TCSA reduce muestra 20-35% vs aleatorio simple.
- **Uso en P4:** Contexto — principio de estratificación con NDVI.

### P80
- **Título:** "Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps: A Comparative Analysis to Improve Yield and Quality Estimates"
- **Autores:** Uribeetxebarria, A.; Martínez-Casasnovas, J.A.; Escolà, A.; Rosell-Polo, J.R.; Arnó, J.
- **Revista:** *Precision Agriculture*, 2018, 19, 1031-1050
- **Hallazgo clave:** NDVI estratificado (2-3 estratos) reduce muestra 17% vs SRS.
- **Uso en P4:** Contexto — NDVI como variable auxiliar mejora el muestreo.

### P86
- **Título:** "Evaluating Sentinel-2 Red Edge for Monitoring LAI and Chlorophyll in Kinnow Mandarin Orchards"
- **Autores:** —
- **Revista:** *ScienceDirect*, 2022
- **Hallazgo clave:** NDRE superior al NDVI para estimar LAI y clorofila en mandarinos con Sentinel-2.
- **Uso en P4:** Caracterización — NDRE describe, no selecciona.

### P93
- **Título:** "UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence"
- **Autores:** Ampatzidis, Y.; Partel, V.
- **Revista:** *Remote Sensing*, 2019, 11(4), 410
- **Hallazgo clave:** NDVI correlaciona con tamaño de copa y sanidad en cítricos. Usó YOLOv3 con 99.9% precisión.
- **Uso en P4:** Contexto — conecta NDVI + YOLO + cítricos.

---

## Grupo C — Opcionales (3 papers)

### P81
- **Título:** "Assessing Ranked Set Sampling and Ancillary Data to Improve Fruit Load Estimates in Peach Orchards"
- **Autores:** Martínez-Casasnovas, J.A.; Uribeetxebarria, A.; Escolà, A.; Arnó, J.; Rosell-Polo, J.R.
- **Revista:** *Computers and Electronics in Agriculture*, 2019
- **Hallazgo:** RSS reduce muestra 50% con UAV.

### P83
- **Título:** "Spatial Sampling of Fruit Maturity Reduces Sampling Costs for Winegrapes in California and New York"
- **Autores:** Meyers, J.M.; Vanden Heuvel, J.E.
- **Revista:** *American Journal of Enology and Viticulture*, 2024
- **Hallazgo:** NDVI3 reduce recorrido 90% vs aleatorio.

### P94
- **Título:** "Sampling Strategies for Soil Property Mapping Using Multispectral Sentinel-2 and Hyperspectral EnMAP Satellite Data"
- **Autores:** Castaldi, F.; Chabrillat, S.; van Wesemael, B.
- **Revista:** *Remote Sensing*, 2019, 11(3), 309
- **Hallazgo:** S2 (10m) suficiente para crear zonas de manejo.

---

## Cómo buscar cada uno

| ID | Buscar en Google Scholar (copiar y pegar el título completo entre comillas) |
|---|---|
| **P82** | "A New, Satellite NDVI-Based Sampling Protocol for Grape Maturation Monitoring" |
| **P84** | "Effectiveness of Management Zones Delineated from UAV and Sentinel-2 Data for Precision Viticulture Applications" |
| **P85** | "Machine Learning Applied to Tree Crop Yield Prediction Using Field Data and Satellite Imagery A Case Study in a Citrus Orchard" |
| **P88** | "Multilevel Systematic Sampling to Estimate Total Fruit Number" Wulfsohn |
| **P90** | "Fruit Yield Estimation of Kinnow Mandarin Orchards Integrating Canopy Physiology with Remote Sensing" |
| **P91** | "Comparing Efficiency of Different Sampling Schemes to Estimate Yield and Quality Parameters in Fruit Orchards" |
| **P92** | "Delineating Citrus Management Zones Using Spatial Interpolation and UAV-Based Multispectral Approaches" |
| **P79** | "Sampling Stratification Using Aerial Imagery to Estimate Fruit Load in Peach Tree Orchards" |
| **P80** | "Stratified Sampling in Fruit Orchards Using Cluster-Based Ancillary Information Maps" |
| **P86** | "Evaluating Sentinel-2 Red Edge for Monitoring LAI and Chlorophyll in Kinnow Mandarin Orchards" |
| **P93** | "UAV-Based High Throughput Phenotyping in Citrus Utilizing Multispectral Imaging and Artificial Intelligence" |

---

> **Carpeta:** `P4-Seleccion-Parcelas/bibliografia/`
> **Nombrar como:** `PXX-titulo-corto.pdf` (ej: `P82-Meyers-NDVI3.pdf`)
> **Cuando tengas los del Grupo A, avisame y los leo para verificar que respaldan lo dicho en el P4.**
