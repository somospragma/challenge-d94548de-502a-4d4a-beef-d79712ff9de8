# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
// === ARCHIVO: airflow_dags/pipeline_orchestration.py ===
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('pipeline_orchestration', default_args=default_args, schedule_interval='@daily') as dag:
    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )
    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )
    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract >> transform >> load

// === ARCHIVO: scripts/extract_data.py ===
import pandas as pd

def extract_data():
    data = pd.read_csv('data/sample_transactions.csv')
    print('Data extracted successfully')

// === ARCHIVO: scripts/transform_data.py ===
import pandas as pd

def transform_data():
    data = pd.read_csv('data/sample_transactions.csv')
    data['amount'] = data['amount'].astype(float)
    data.to_csv('data/transformed_transactions.csv', index=False)
    print('Data transformed successfully')

// === ARCHIVO: scripts/load_data.py ===
import pandas as pd
import boto3

def load_data():
    data = pd.read_csv('data/transformed_transactions.csv')
    s3 = boto3.client('s3')
    s3.upload_file('data/transformed_transactions.csv', 'my-bucket', 'transformed_transactions.csv')
    print('Data loaded successfully')

// === ARCHIVO: data/sample_transactions.csv ===
id,date,amount,description
1,2024-05-01,100.0,Purchase
2,2024-05-01,200.0,Transfer

// === ARCHIVO: config/airflow.cfg ===
[core]
executor = LocalExecutor
sql_alchemy_conn = sqlite:////opt/airflow/airflow.db

// === ARCHIVO: tests/test_pipeline.py ===
import unittest
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.load_data import load_data

class TestPipeline(unittest.TestCase):
    def test_extract_data(self):
        extract_data()
        self.assertTrue(True)

    def test_transform_data(self):
        transform_data()
        self.assertTrue(True)

    def test_load_data(self):
        load_data()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

// === ARCHIVO: config/aws_config.yaml ===
aws_access_key_id: YOUR_ACCESS_KEY_ID
aws_secret_access_key: YOUR_SECRET_ACCESS_KEY
region_name: us-east-1

// === ARCHIVO: airflow_dags/aws_s3_listener.py ===
import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class AWSS3Listener(BaseOperator):
    @apply_defaults
    def __init__(self, bucket_name, prefix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bucket_name = bucket_name
        self.prefix = prefix

    def execute(self, context):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket_name, Prefix=self.prefix)
        for obj in response.get('Contents', []):
            self.log.info(f'Detected object: {obj['Key']}')

// === ARCHIVO: airflow_dags/aws_sns_handler.py ===
import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class AWSSNSHandler(BaseOperator):
    @apply_defaults
    def __init__(self, topic_arn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topic_arn = topic_arn

    def execute(self, context):
        sns = boto3.client('sns')
        sns.publish(TopicArn=self.topic_arn, Message='New data available')

// === ARCHIVO: airflow_dags/aws_iam_policy.json ===
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}

```
