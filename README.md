# Orquestación de un pipeline de datos para análisis de transacciones financieras

Una empresa de servicios financieros necesita orquestar un pipeline de datos que procese y analice transacciones diarias. El objetivo es identificar patrones de fraude y generar informes mensuales para los clientes. El pipeline debe ser escalable, mantener la integridad de los datos y ser resiliente a fallos.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Orquestación de pipelines de datos |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 5-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del pipeline

**Objetivo:** Definir las etapas del pipeline y los datos que se procesarán.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica las fuentes de datos disponibles (ej. transacciones diarias, registros de clientes).
- Define las etapas del pipeline (ej. extracción, transformación, carga, análisis).
- Especifica los datos que se procesarán en cada etapa.

**Entregable:** Descripción detallada del pipeline y sus etapas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la integridad y consistencia de los datos en cada etapa.
- Piensa en cómo manejarás los datos faltantes o inconsistentes.

</details>

### Fase 2: Implementación de la orquestación

**Objetivo:** Implementar la orquestación del pipeline utilizando un servicio de workflow.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Elige un servicio de workflow para orquestar el pipeline (ej. AWS Step Functions, Apache Airflow).
- Configura las tareas y dependencias entre ellas.
- Establece los mecanismos de reintento y notificación de fallos.

**Entregable:** Configuración del servicio de workflow con las tareas y dependencias definidas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la escalabilidad y la resiliencia del pipeline.
- Piensa en cómo manejarás los fallos y reintentos.

</details>

### Fase 3: Optimización y escalabilidad

**Objetivo:** Optimizar el pipeline para mejorar su rendimiento y escalabilidad.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica las etapas del pipeline que pueden ser optimizadas.
- Aplica técnicas de paralelismo y particionamiento de datos.
- Evalúa el rendimiento del pipeline y realiza ajustes necesarios.

**Entregable:** Pipeline optimizado con mejoras en rendimiento y escalabilidad.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de caché y almacenamiento temporal para mejorar la eficiencia.
- Piensa en cómo manejarás la latencia y el throughput del pipeline.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un pipeline de datos y por qué es importante en este contexto?
- **paraQueSirve**: ¿Para qué sirve cada etapa del pipeline en el análisis de transacciones financieras?
- **comoSeUsa**: ¿Cómo se usa un servicio de workflow para orquestar el pipeline?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar un pipeline de datos y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la optimización del pipeline y cómo afecta su rendimiento y escalabilidad?

## Criterios de Evaluacion

- Definición clara del pipeline y sus etapas.
- Implementación correcta de la orquestación utilizando un servicio de workflow.
- Optimización del pipeline para mejorar su rendimiento y escalabilidad.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
