# Investigación — P4: Selección de Parcelas para Muestreo en Campo

## Contexto General

Se dispone de **4 parcelas** de mandarina variedad **Murcott** de **4 años de edad**, cada una de **0.5 ha** (≈70×70 m), de forma cuadrada, con **13 hileras** cada una. Las parcelas tienen el mismo marco de plantación, están alejadas de bordes y son similares en condiciones de manejo.

Se dispone de **imágenes Sentinel-2** con los índices **NDVI (10m)**, **NDRE (20m)** y **MSAVI2 (10m)**. Sin embargo, la resolución espacial de Sentinel-2 no permite discriminar hileras individuales (cada hilera ocupa ~5.4 m, mientras que un píxel NDVI cubre 10 m ≈ 2 hileras).

**Objetivo:** Seleccionar qué parcela(s) y qué hilera(s) capturar para el experimento A/B (Protocolo vs Cámara Nativa), justificando cada decisión con el nivel de respaldo bibliográfico correspondiente.

---

## Fuentes consultadas

- **Librarian agent (Semantic Scholar):** 4 rondas de búsqueda con más de 30 términos en total
- **Búsqueda web complementaria (Exa):** Múltiples búsquedas específicas
- **Papers consultados:** Ver Tabla Maestra [P79-P89]

---

## Limitación Física: Resolución de Sentinel-2

| Índice | Resolución | Píxeles en tu parcela (70×70m) | ¿Resuelve hileras? |
|---|---|---|---|
| **NDVI** | 10 m | ~7×7 = 49 píxeles | ❌ Cada píxel cubre ~2 hileras |
| **MSAVI2** | 10 m | ~7×7 = 49 píxeles | ❌ Cada píxel cubre ~2 hileras |
| **NDRE** | 20 m | ~3.5×3.5 = 12 píxeles | ❌ Cada píxel cubre ~4 hileras |

**Conclusión:** Sentinel-2 **no permite seleccionar hileras individuales** ni árboles dentro de una parcela. Su uso se limita a la **caracterización entre parcelas** a nivel de parcela completa.

---

## Metodologías de Muestreo en Huertos — Nivel de Respaldo

### Método 1: Muestreo Aleatorio Simple (MAS o SRS)

| Aspecto | Detalle |
|---|---|
| **Descripción** | Cada unidad (parcela o hilera) tiene igual probabilidad de ser seleccionada |
| **Respaldo** | ✅ **Estadística universal** — teoría de muestreo de Cochran (1977), textbook clásico |
| **Uso en agricultura** | Usado como baseline en Miranda et al. (2018) [P79] y Uribeetxebarria et al. (2018) [P80] |
| **Aplicación a este caso** | Seleccionar k parcelas de 4 mediante sorteo con generador de números aleatorios |

### Método 2: Muestreo Estratificado con NDVI

| Aspecto | Detalle |
|---|---|
| **Descripción** | Usar NDVI como variable auxiliar para crear estratos homogéneos |
| **Respaldo** | ⚠️ **Extrapolación** — Miranda et al. (2018) [P79] y Uribeetxebarria et al. (2018) [P80] lo hicieron con **imagen aérea 0.25m** dentro de una parcela, no con Sentinel entre parcelas |
| **Aplicación a este caso** | Ordenar parcelas por NDVI medio y seleccionar baja-media-alta. **Debe documentarse como decisión experimental.** |

### Método 3: Muestreo Sistemático Uniforme (SUR)

| Aspecto | Detalle |
|---|---|
| **Descripción** | Seleccionar cada k-ésima unidad con arranque aleatorio |
| **Respaldo** | ✅ **Wulfsohn et al. (2012)** [P88] — error <10% en 11/14 huertos comerciales |
| **Aplicación a este caso** | Hileras 3, 7, 11 dentro de cada parcela seleccionada |

### Método 4: Caracterización con NDVI/NDRE de Sentinel (descripción)

| Aspecto | Detalle |
|---|---|
| **Descripción** | Extraer el valor medio de NDVI y NDRE por parcela para describir su vigor |
| **Respaldo** | ✅ **Morocco citrus (2022)** [P85]: usó mean NDVI de Sentinel-2 para 50 parcelas de cítricos |
| **Adicional** | ✅ **Kinnow mandarin (2022)** [P86]: Red Edge (NDRE) es superior al NDVI para cítricos |

---

## Tabla de Respaldo por Decisión

| Decisión | Método | ¿Respaldo directo? | Fuente |
|---|---|---|---|
| **Seleccionar parcelas** | MAS (aleatorio simple) | ✅ **Sí** — teoría universal | Cochran (1977), usado en [P79][P80] |
| **Seleccionar parcelas** | Estratificado por NDVI | ⚠️ **Extrapolación** — no hay paper que lo haga con Sentinel-10m entre parcelas | [P79][P80] usan 0.25m aéreo |
| **Seleccionar hileras** | SUR sistemático (3, 7, 11) | ✅ **Sí** — validado en 14 huertos | [P88] Wulfsohn et al. (2012) |
| **Describir parcelas** | NDVI medio por parcela | ✅ **Sí** — validado en cítricos | [P85] Morocco citrus (2022) |
| **Describir parcelas** | NDRE medio por parcela | ✅ **Sí** — recomendado para cítricos | [P86] Kinnow mandarin (2022) |
| **Seleccionar hileras con Sentinel** | Cualquier índice | ❌ **No** — resolución insuficiente | Limitación física del sensor |

---

## Plan de Muestreo Recomendado

### Paso 1: Selección de parcelas

**Opción recomendada: MAS (Muestreo Aleatorio Simple)**

> "Se seleccionaron k parcelas de las 4 disponibles mediante muestreo aleatorio simple (MAS), método estadístico estándar en el que cada unidad tiene igual probabilidad de ser elegida (Cochran, 1977)."

| Opción | Parcelas | Tiempo |
|---|---|---|
| **A — 2 parcelas (30 min)** | Sorteo aleatorio de 2 | ~30 min |
| **B — 3 parcelas (45 min)** | Sorteo aleatorio de 3 | ~45 min |

**Alternativa: estratificación por NDVI (decisión experimental)**

> "Como alternativa, se ordenaron las parcelas por su NDVI medio derivado de Sentinel-2 y se seleccionaron aquellas que representan los niveles bajo, medio y alto de vigor, extrapolando el principio de estratificación documentado en Miranda et al. (2018) [P79]. Esta extrapolación no tiene respaldo bibliográfico directo para Sentinel-2 en parcelas de 0.5 ha, por lo que se documenta como decisión experimental."

### Paso 2: Selección de hileras dentro de cada parcela

**Método: SUR sistemático**

> "Dentro de cada parcela seleccionada, se eligieron 3 hileras mediante muestreo sistemático uniforme (SUR) con arranque aleatorio: hileras 3, 7 y 11. Este método fue validado por Wulfsohn et al. (2012) [P88], quien reportó errores de estimación inferiores al 10% en 11 de 14 huertos comerciales."

| Hilera | Posición en la parcela |
|---|---|
| **3** | Cercana al borde |
| **7** | Central |
| **11** | Cercana al borde opuesto |

### Paso 3: Caracterización de parcelas con Sentinel-2

> "Las parcelas seleccionadas se caracterizaron mediante el NDVI y NDRE medios derivados de Sentinel-2, siguiendo la metodología de Morocco citrus (2022) [P85] para NDVI y de Kinnow mandarin (2022) [P86] para Red Edge, quienes demostraron que estos índices son efectivos para describir la variabilidad entre parcelas de cítricos."

### Paso 4: Captura de video (según P3)

> "La captura de video se realizó siguiendo el protocolo establecido en P3: velocidad ~1 m/s, distancia 0.8-1.5 m del dosel, ángulo 15-30° hacia arriba, con bloqueo AF/AE/WB."

---

## Tabla Comparativa de Opciones

| Opción | Selección parcelas | Hileras | Tiempo | Respaldo |
|---|---|---|---|---|
| **✅ MAS-2** | **2 al azar (sorteo)** | **SUR: 3, 7, 11** | **~30 min** | **✅ Directo — teoría universal + [P88]** |
| MAS-3 | 3 al azar (sorteo) | SUR: 3, 7, 11 | ~45 min | ✅ Directo — teoría universal + [P88] |
| NDVI-2 | 2 por NDVI (extremos) | SUR: 3, 7, 11 | ~30 min | ⚠️ Experimental — extrapolación de [P79] |
| NDVI-3 | 3 por NDVI (baja-media-alta) | SUR: 3, 7, 11 | ~45 min | ⚠️ Experimental — extrapolación de [P79] |

---

## Decisión Final

> **Opción seleccionada:** MAS-2 (Muestreo Aleatorio Simple — 2 parcelas)

| Elemento | Valor | Respaldo |
|---|---|---|
| **Parcelas** | 2 (sorteo aleatorio simple) | Cochran (1977) — teoría universal de muestreo |
| **Hileras por parcela** | 3 (SUR: 3, 7, 11) | [P88] Wulfsohn et al. (2012) |
| **Total videos** | 6 | |
| **Tiempo estimado** | ~30 min | |
| **Índices para describir** | NDVI + NDRE medio por parcela | [P85] Morocco citrus (2022) + [P86] Kinnow mandarin (2022) |

### Justificación textual completa

> "La selección de parcelas se realizó mediante muestreo aleatorio simple (MAS), método estadístico estándar en el que cada unidad poblacional tiene igual probabilidad de ser seleccionada (Cochran, 1977). Este método fue utilizado como referencia en estudios de muestreo en huertos frutales (Miranda et al., 2018 [P79]; Uribeetxebarria et al., 2018 [P80]) y no requiere variables auxiliares para su aplicación, lo que garantiza la imparcialidad de la selección.
>
> "Dentro de cada parcela seleccionada, las hileras se eligieron mediante muestreo sistemático uniforme (SUR) con arranque aleatorio (hileras 3, 7 y 11), siguiendo la metodología validada por Wulfsohn et al. (2012) [P88], quienes reportaron errores de estimación inferiores al 10% en 11 de 14 huertos comerciales evaluados.
>
> "Las parcelas seleccionadas se caracterizaron mediante los valores medios de NDVI y NDRE derivados de Sentinel-2, siguiendo el enfoque utilizado por Morocco citrus (2022) [P85] para 50 parcelas de cítricos, y complementado con el índice de Red Edge (NDRE) que demostró ser superior al NDVI para la evaluación de mandarinos (Kinnow mandarin, 2022 [P86]). Estos índices se utilizaron exclusivamente para describir las parcelas, no para su selección, debido a que la resolución espacial de Sentinel-2 (10-20 m) no permite discriminar hileras individuales dentro de cada parcela."

---

## Respaldo bibliográfico completo

| ID | Título corto | Año | Hallazgo clave |
|---|---|---|---|
| [P79] | Miranda et al. — Sampling stratification in peach | 2018 | NDVI + TCSA reduce muestra 20-35% (imagen aérea 0.25m) |
| [P80] | Uribeetxebarria et al. — Stratified sampling orchards | 2018 | NDVI estratificado reduce 17% muestra (imagen aérea 0.25m) |
| [P81] | Martínez-Casasnovas et al. — RSS peach orchards | 2019 | RSS reduce muestra 50% con UAV |
| [P82] | Meyers et al. — Satellite NDVI sampling (NDVI3) | 2020 | 3 píxeles Landsat representan variabilidad del bloque |
| [P83] | Spatial Sampling — Costos NDVI3 vs aleatorio | 2024 | NDVI3 reduce recorrido 90% vs aleatorio |
| [P84] | UAV vs Sentinel-2 management zones | 2024 | Sentinel-2 captura zonas principales de vigor |
| **P85** | **Morocco citrus yield prediction (NUEVO)** | **2022** | **Mean NDVI de Sentinel-2 usado para caracterizar 50 parcelas de cítricos** |
| **P86** | **Kinnow mandarin Red Edge (NUEVO)** | **2022** | **Red Edge (NDRE) superior al NDVI para cítricos en Sentinel-2** |
| **P87** | **Citrus orchard mapping Iran (NUEVO)** | **2022** | **Sentinel-2 clasifica huertos de cítricos con 99.7% precisión** |
| **P88** | **Wulfsohn et al. — SUR sampling fruit orchards (NUEVO)** | **2012** | **SUR sistemático: error <10% en 11/14 huertos** |
| **P89** | **Mediterranean orchard assessment Sentinel (NUEVO)** | **2024** | **Selección de parcelas por criterios agronómicos: edad, variedad, manejo** |

---

**Última actualización:** 05/06/2026 | **IDs:** P79-P89
