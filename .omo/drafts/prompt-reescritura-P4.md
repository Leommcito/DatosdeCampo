# Prompt: Reescribir el Paso 4 como Documento Académico-Científico

## Objetivo

Reescribir el archivo `P4-Seleccion-Parcelas/Investigacion-P4-Seleccion-Parcelas.md` como un documento académico formal para tesis, con estructura científica (Introducción → Estado del arte → Metodología → Discusión → Conclusión), citas formales (Autor, año), y justificación bibliográfica completa de cada decisión metodológica.

---

## Contexto del proyecto

**Tesis:** Protocolo de captura manual con smartphone en huertos densos de mandarinas para detección YOLO y seguimiento MOT.

**Cultivo:** Mandarina variedad Murcott, 4 años, 4 parcelas de 0.5 ha (≈70×70m), 13 hileras por parcela.

**Datos disponibles:** Imágenes Sentinel-2 con NDVI (10m, ~49 píxeles/parcela), NDRE (20m, ~12 píxeles/parcela), MSAVI2 (10m).

**Objetivo del P4:** Seleccionar qué parcelas y qué hileras capturar para el experimento A/B (Protocolo vs Cámara Nativa). La captura de video sigue el protocolo P3: velocidad ~1 m/s, distancia 0.8-1.5 m, ángulo 15-30° hacia arriba, bloqueo AF/AE/WB.

---

## Estructura requerida del documento académico

### 1. Introducción
- Contexto del problema: necesidad de seleccionar parcelas representativas para un experimento de captura de video en huerto de mandarinas
- Por qué es importante la selección de parcelas: afecta la generalización de los resultados del experimento A/B
- Objetivo específico del P4
- Estructura del documento

### 2. Área de estudio y datos disponibles
- Descripción de las 4 parcelas (variedad Murcott, 4 años, 0.5 ha, 13 hileras)
- Imágenes Sentinel-2 disponibles
- Limitación de resolución: NDVI 10m (49 píxeles/parcela) vs NDRE 20m (12 píxeles/parcela). No permite discriminar hileras individuales (~5.4m de ancho)
- Justificación de por qué Sentinel-2 permite comparar parcelas enteras pero no hileras individuales

### 3. Estado del arte — Métodos de muestreo en huertos frutales

#### 3.1 Muestreo Aleatorio Simple (MAS/SRS)
- Descripción: cada unidad tiene igual probabilidad
- Ventaja: teoría universal (Cochran, 1977), simple de implementar
- Limitación para este caso: con solo 4 parcelas, el azar puede seleccionar 2 con vigor muy similar, perdiendo representatividad
- Referencias: usado como baseline en Miranda et al. (2018) [P79] y Uribeetxebarria et al. (2018) [P80]

#### 3.2 Muestreo Estratificado con NDVI (alta resolución)
- Descripción: usar NDVI para crear estratos homogéneos
- Evidencia: Miranda et al. (2018) [P79] y Uribeetxebarria et al. (2018) [P80] usaron imagen aérea 0.25m para estratificar árboles en durazno, reduciendo muestra 17-35%
- Limitación: requiere resolución submétrica (0.25m), Sentinel-2 (10m) no lo permite
- Conclusión: no aplica directamente a este caso

#### 3.3 Muestreo Estratificado con NDVI Satelital — MÉTODO SELECCIONADO
- Descripción: usar NDVI medio derivado de satélite para ordenar parcelas por vigor y seleccionar extremos
- Cadena de evidencia:
  - **Principio general:** Meyers et al. (2020) [P82] desarrolló NDVI3, usando Landsat (30m) para seleccionar píxeles por cuantiles (cola baja, media, alta), alcanzando misma representatividad que 20 puntos aleatorios
  - **Sensor:** Ortuani et al. (2024) [P84] demostró que Sentinel-2 (10m) captura las principales zonas de vigor a nivel parcela, comparable a UAV de 3-4cm
  - **Cultivo:** Moussaid et al. (2022) [P85] usó mean NDVI de Sentinel-2 para caracterizar 50 parcelas de cítricos (mandarina Afourer)
  - **Eficiencia:** Arnó et al. (2017) [P91] demostró que estratificar por NDVI es más eficiente que aleatorio simple en huertos frutales; con 2 estratos se captura la mayor parte de la variabilidad
  - **Cítricos específico:** Longo-Minnolo et al. (2023) [P92] delineó zonas de manejo en cítricos con NDVI (K-means), encontrando diferencias significativas entre zonas de vigor
  - **Mandarina específico:** Sun et al. (2026) [P90] predijo rendimiento de mandarina Kinnow con Sentinel-2 Red Edge (R²=0.85), confirmando variabilidad intra-huerto capturable por satélite

#### 3.4 Muestreo Sistemático Uniforme (SUR) — MÉTODO SELECCIONADO para hileras
- Descripción: seleccionar cada k-ésima unidad con arranque aleatorio
- Evidencia: Wulfsohn (2010) explica que SUR es superior a SRS para poblaciones con autocorrelación espacial, y Wulfsohn et al. (2012) [P88] reportó errores <10% en 11/14 huertos comerciales. Uribeetxebarria et al. (2018) [P80] cita este mismo resultado (error de solo 10%).
- Aplicación: hileras 3, 7, 11 de 13 (arranque aleatorio = 3, intervalo = 4)

#### 3.5 Otros métodos considerados (resumen)
- Ranked Set Sampling (RSS) con UAV (Martínez-Casasnovas et al., 2019 [P81]): reduce muestra 50% pero requiere UAV, no disponible
- Costos de NDVI3 (Meyers & Vanden Heuvel, 2024 [P83]): demuestra eficiencia pero no aplica directamente
- Mediterráneo (2024) [P89]: selección por criterios agronómicos complementarios

### 4. Metodología propuesta (4 pasos)

#### Paso 1: Selección de parcelas por NDVI medio de Sentinel-2
- Extraer NDVI medio de cada parcela desde Sentinel-2 (10m, ~49 píxeles/parcela)
- Ordenar por vigor
- Seleccionar 2 parcelas: una del extremo inferior (menor NDVI) y una del extremo superior (mayor NDVI)
- **Justificación:** el principio de selección por cuantiles NDVI satelital (Meyers et al., 2020), validado para S2 (Ortuani et al., 2024), aplicado a cítricos (Moussaid et al., 2022) y específicamente a mandarina (Sun et al., 2026). La estratificación por NDVI es más eficiente que el azar (Arnó et al., 2017) y genera zonas con diferencias significativas en cítricos (Longo-Minnolo et al., 2023)

#### Paso 2: Selección de hileras mediante SUR sistemático
- Dentro de cada parcela, seleccionar hileras 3, 7 y 11
- **Justificación:** SUR con arranque aleatorio. Validado por Wulfsohn et al. (2012) con error <10% en 11/14 huertos. Wulfsohn (2010) demuestra que SUR es superior a aleatorio para poblaciones con autocorrelación espacial

#### Paso 3: Caracterización de parcelas con NDVI + NDRE
- NDVI (10m) como índice primario, siguiendo Moussaid et al. (2022) [P85]
- NDRE (20m) como descriptor complementario, siguiendo Ali & Imran (2022) [P90, reemplazo] que demostró que NDRE es superior para LAI y clorofila en Kinnow mandarin (R²=0.86)
- **Importante:** NDRE no se usa para selección por su menor resolución (20m vs 10m)

#### Paso 4: Captura de video
- Según protocolo P3

### 5. Discusión

#### 5.1 Por qué NDVI y no NDRE para selección
- **Resolución espacial:** NDVI 10m (49 píxeles/parcela) vs NDRE 20m (12 píxeles). Para parcelas de 0.5ha, 49 píxeles dan una media más robusta
- **Respaldo bibliográfico:** El principio de selección por cuantiles NDVI satelital está validado (Meyers et al., 2020), mientras que no existe un paper equivalente para NDRE. Arnó et al. (2017) y Longo-Minnolo et al. (2023) respaldan la estratificación por NDVI en huertos y cítricos
- **Tradición:** Todos los papers de muestreo estratificado con índices vegetativos usan NDVI (Miranda et al., 2018; Uribeetxebarria et al., 2018; Meyers et al., 2020; Arnó et al., 2017)
- **Correlación con vigor:** Ampatzidis & Partel (2019) [P93] demostró que NDVI correlaciona con tamaño de copa y sanidad en cítricos

#### 5.2 Limitaciones de la metodología
- Solo 4 parcelas disponibles → tamaño de muestra pequeño pero justificado por estratificación
- Sentinel-2 no resuelve hileras individuales → SUR como solución
- Solo 2 parcelas seleccionadas → sacrifica cobertura por representatividad de extremos

### 6. Conclusión
- Resumen de la decisión final
- Tabla resumen con decisiones, métodos, y respaldo bibliográfico

---

## Formato de citación — FORMATO DUAL OBLIGATORIO

**Cada referencia debe incluir AMBOS formatos simultáneamente:**

- Primera mención: `[PXX] (Autor et al., año)` — ej: `[P82] (Meyers et al., 2020)`
- Menciones siguientes: `(Autor et al., año) [PXX]` — ej: `(Meyers et al., 2020) [P82]`

Esto permite trazabilidad directa con la Tabla Maestra (via [PXX]) Y formato académico APA (via Autor, año).

**Mapeo completo de IDs a citas APA:**

| ID | Cita APA completa |
|---|---|
| P79 | Miranda, C., Santesteban, L.G., Urrestarazu, J., Loidi, M. & Royo, J.B. (2018) |
| P80 | Uribeetxebarria, A., Martínez-Casasnovas, J.A., Escolà, A., Rosell-Polo, J.R. & Arnó, J. (2018) |
| P81 | Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A., Arnó, J. & Rosell-Polo, J.R. (2019) |
| P82 | Meyers, J.M., Dokoozlian, N., Ryan, C., Bioni, C. & Vanden Heuvel, J.E. (2020) |
| P83 | Meyers, J.M. & Vanden Heuvel, J.E. (2024) |
| P84 | Ortuani, B., Mayer, A., Bianchi, D., Sona, G., Crema, A., Modina, D., Bolognini, M., Brancadoro, L., Boschetti, M. & Facchi, A. (2024) |
| P85 | Moussaid, A., El Fkihi, S., Zennayi, Y., Lahlou, O., Kassou, I., Bourzeix, F., El Mansouri, L. & Imani, Y. (2022) |
| P86 | Ali, A., Imran, M., Ali, A. & Khan, M.A. (2022) — *reemplazo por Ali & Imran* |
| P87 | Toosi, A., Dadrass Javan, F., Samadzadegan, F., Mehravar, S., Kurban, A. & Azadi, H. (2022) |
| P88 | Wulfsohn, D., Aravena, F., Potin, C., Zamora, I. & García-Fiñana, M. (2012) |
| P89 | — (Mediterranean orchard assessment, 2024) |
| P90 | Sun, Y., Qin, Q., Zhang, J., Ren, H. & Han, R. (2026) — *o Ali & Imran (2022) si se reemplaza* |
| P91 | Arnó, J., Martínez-Casasnovas, J.A., Uribeetxebarria, A., Escolà, A. & Rosell-Polo, J.R. (2017) |
| P92 | Longo-Minnolo, G., Consoli, S., Vanella, D., Pappalardo, S., Guarrera, S., Manetto, G. & Cerruto, E. (2023) |
| P93 | Ampatzidis, Y. & Partel, V. (2019) |
| P94 | Castaldi, F., Chabrillat, S. & van Wesemael, B. (2019) |
| — | Wulfsohn, D. (2010) |
| — | Cochran, W.G. (1977) |

**Ejemplo de cómo debe verse en el texto:**
> "Las parcelas se seleccionaron siguiendo el principio de selección por cuantiles NDVI satelital [P82] (Meyers et al., 2020), quienes demostraron que 3 píxeles Landsat representando la cola baja, media y alta del NDVI alcanzan la misma representatividad que 20 puntos aleatorios. El uso de Sentinel-2 para este fin está respaldado por [P84] (Ortuani et al., 2024), quienes confirmaron que S2 captura las principales zonas de vigor a nivel de parcela."

---

## Tabla de respaldo para incluir al final

| Decisión | Método | Respaldo principal |
|---|---|---|
| Seleccionar parcelas | Estratificación por NDVI medio S2 (extremos) | [P82] (Meyers et al., 2020); [P84] (Ortuani et al., 2024); [P85] (Moussaid et al., 2022); [P91] (Arnó et al., 2017); [P92] (Longo-Minnolo et al., 2023); [P90] (Sun et al., 2026) |
| Seleccionar hileras | SUR sistemático (3, 7, 11) | (Wulfsohn, 2010); [P88] (Wulfsohn et al., 2012) |
| Caracterizar parcelas | NDVI medio S2 (primario) + NDRE (complementario) | [P85] (Moussaid et al., 2022); [P86] (Ali & Imran, 2022) |

---

## Instrucciones para el agente que ejecute esta reescritura

1. **NO** cambiar las decisiones metodológicas — solo mejorar la presentación y justificación
2. **NO** eliminar contenido existente — solo reorganizar y expandir
3. **Formato DUAL obligatorio:** cada referencia debe incluir `[PXX]` + `(Autor et al., año)` en el mismo texto
4. **NO** escribir código ni archivos fuera del markdown del P4
5. El tono debe ser académico pero claro, propio de una tesis de grado/máster
6. Incluir una sección de "Limitaciones" al final
7. Si hay imprecisiones menores (como P79 usando RVI no NDVI, o P93 usando CNN no YOLO), corregirlas en la nueva versión
8. Al final del documento, incluir una sección "Referencias" con la lista completa en formato APA
9. Mantener coherencia con la Tabla Maestra: los IDs [PXX] deben coincidir exactamente con los de la Tabla Maestra
