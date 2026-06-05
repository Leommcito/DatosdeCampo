# Draft: Plan de Investigación — Contradicciones/Validaciones Paso 2 (IMU Telemetría)

## Claims Evaluados (7 frentes de investigación)

### 1. OIS Debe Estar OFF [P64][P65]
- **Veredicto**: ⚠️ **MATIZADO**
- **Contradice**: Qualcomm Patent US20200412954A1, Google Pixel 2 Fused, Sony Xperia Hybrid, Apple US9596411, HyperOIS (IEEE TCE 2024) — todos combinan OIS+EIS exitosamente con sensores Hall
- **Valida**: DeepOIS muestra 1.038 vs 0.688 (49% peor) SIN compensación
- **Conclusión**: "OIS debe estar OFF" aplica solo a sistemas NAIVE que no leen posición del lente (Hall sensor). Si el pipeline NO puede leer posición OIS, entonces SÍ debe estar OFF.

### 2. 100 Hz Suficiente para Walking
- **Veredicto**: ✅ **MAYORMENTE VALIDADO** (con matiz)
- **Valida**: Fan et al. 2025 confirma 100 Hz óptimo para orientación en walking. Revisión sistemática de 66 papers encuentra que 42 usan 100-200 Hz, 30 exactamente 100 Hz.
- **Contradice**: Torun et al. 2021 — 100 Hz INADECUADO para parámetros espaciales (250 Hz óptimo), útil gait content hasta 120 Hz. Gruber 2022 — 100 Hz subestima aceleraciones pico 19-36%.
- **Matiz**: Para sincronización video-IMU (propósito de la tesis), 100 Hz es suficiente. Para análisis de marcha preciso (NO es el objetivo), no lo sería.

### 3. Gyroflow como Herramienta de Estabilización
- **Veredicto**: ✅ **VALIDADO** con limitaciones documentadas
- **Valida**: ICCV 2021 paper (GyroFlow) — 26.46% mejor EPE que segundo mejor. Comunidad FPV/drones lo prefiere sobre built-in EIS. CineD (2022) lo llama "revolucionario". Rolling shutter correction y dynamic zoom son ventajas únicas.
- **Contradice/Limitaciones**: Clock drift en grabaciones largas (1ms/20min Insta360). Sony IBIS causa warping en algunos casos. NO corrige motion blur (necesita ND filters + shutter rápido). High-freq jello (>600Hz) no corregible por software.
- **Sin papers agrícolas usando Gyroflow** — gap que valida la oportunidad de la tesis.

### 4. Motion Blur Degrada YOLO 86.4% mAP
- **Veredicto**: ❌ **CONTRADICCIÓN SIGNIFICATIVA** en la magnitud
- **Valida parcialmente**: Citrus GAN sí muestra degradación, pero el 86.4% es mejora RELATIVA tras deblurring, no degradación absoluta.
- **Contradice**: Múltiples papers muestran degradación mucho menor:
  - FEGW-YOLO (2026): solo 21.4% drop a blur severo
  - Quantization Study (2025): Medium blur = 11-15% drop
  - Knowledge Distillation (2024): solo 2.5% drop al 100% de velocidad
  - MDPI Electronics 2025: YOLOv4 solo 15-25% degradación
- **Dato crítico**: YOLOv8-v11 son MÁS susceptibles a blur que YOLOv3/v4
- **Conclusión**: El 86.4% es engañoso. La degradación real está en 15-50% según el modelo y severidad.

### 5. Video Estabilizado > Fotos (+22%)
- **Veredicto**: ⚠️ **MATIZADO** — mejora NO es por estabilización
- **Valida parcialmente**: MangoYOLO sí obtuvo +22%, pero la mejora viene de COBERTURA MULTI-VISTA y TRACKING (Kalman Filter), no de estabilización.
- **Contradice**: Múltiples papers agrícolas logran SOTA sin estabilización de video — sugieren que el beneficio es contextual.
- **Conclusión**: No hay evidencia directa de que la estabilización (vs video raw) produzca +22% en detección.

### 6. IMU Supera a Óptica (32% Mejor)
- **Veredicto**: ❌ **CONTRADICCIÓN PARCIAL** — desactualizado
- **Valida (2014)**: Bell et al. (NVIDIA) — IMU supera a feature-based en rotación-dominante, baja luz, tiempo real.
- **Contradice**: 
  - IMU puro NO puede medir TRASLACIÓN (caminar tiene traslación dominante)
  - Deep Learning (RStab, GaVS, MetaStab, TranStable 2024-2025): 0.85-0.92 estabilidad vs ~0.83 gyro-only
  - El 32% de Han et al. era un método HÍBRIDO (IMU+visual), no IMU puro
- **Conclusión**: Para video agrícola caminando (traslación dominante), IMU puro es inadecuado. Gyroflow + optical flow (híbrido) es el enfoque correcto.

### 7. Rolling Shutter Correction con IMU
- **Veredicto**: ⚠️ **MATIZADO** — beneficio es para geometría, NO para detección
- **Valida**: Mo et al. 2020 — IMU mejora corrección RS para SLAM/VIO. Gyroflow corrige RS línea-por-línea.
- **Contradice**: 
  - "Let's Roll" (2024, arXiv:2309.08136): RS correction NO es necesaria para detección de objetos a IoU≥0.5
  - Múltiples papers agrícolas logran SOTA SIN corrección RS
  - Smartphones modernos (iPhone 15 Pro): ~5ms readout, "excepcional"
  - Toda corrección RS introduce artefactos (DFRSC 2024, JCD 2021, RSGR 2022)
- **Conclusión**: Para detección YOLO (no SLAM), el beneficio de RS correction puede ser negligible.

---

## 🎯 Gap de la Tesis — Evaluación Crítica

### "No existe paper que mida IMU preprocessing → YOLO mAP en agricultura"

**Veredicto**: ✅ **VÁLIDO — El gap SE CONFIRMA**

Fortalece el gap:
- ✅ zhouzypaul/object-recognition-imu es POST-procesamiento (después de YOLO), no PRE-procesamiento
- ✅ Ningún paper agrícola usa Gyroflow específicamente
- ✅ Múltiples papers logran alta mAP pero ninguno mide el impacto del pipeline de captura

Debilita el gap:
- ⚠️ Papers muestran que YOLO es robusto a degradación moderada (compresión, blur)
- ⚠️ Métodos de agregación temporal (YOLOV, Temporal-YOLOv8) logran mejoras similares en inferencia
- ⚠️ Un resultado NEGATIVO (preprocesamiento tiene poco efecto) sería científicamente válido pero podría hacer la contribución menos impactante

### Recomendación
El gap es REAL. Tu tesis puede medir no solo SI el preprocesamiento con IMU mejora mAP, sino CUÁNTO. Incluso un resultado nulo o pequeño sería una contribución válida porque:
1. Nadie lo ha medido cuantitativamente
2. Ayudaría a la comunidad a decidir si vale la pena el overhead
