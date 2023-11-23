
# README para el Generador de Cuentos para Niños

## Introducción
Este programa es un generador de cuentos para niños utilizando la API de OpenAI GPT-3.5-turbo. Permite al usuario ingresar un inicio de cuento, especificar la longitud y la "temperatura" (creatividad) para generar un cuento único. También ofrece la opción de guardar el cuento generado en un archivo.

## Requisitos
- Python 3
- Bibliotecas `tkinter`, `requests`, y `python-dotenv` (Pueden instalarse usando `pip install tkinter requests python-dotenv`)
- Una clave API de OpenAI (Puede obtenerse registrándose en [OpenAI](https://openai.com/))

## Configuración
1. **Clave API de OpenAI**: Debe tener una clave API de OpenAI. Esta clave se debe colocar en un archivo `.env` en el mismo directorio que el script. El archivo `.env` debe tener el siguiente formato:
`OPENAI_API_KEY='tu_clave_api_aquí'`

## Ejecución del programa
1. **Iniciar el programa**: Ejecuta el script `python nombre_del_archivo.py`.
2. **Interfaz de Usuario**: Se abrirá una ventana de interfaz gráfica.

## Uso de la Interfaz
1. **Inicio del cuento**: Ingresa en el campo correspondiente la oración inicial o el prompt para el cuento.
2. **Longitud del cuento**: Define la longitud deseada del cuento en términos de tokens (por defecto es 100). El rango válido es entre 50 y 500 tokens.
3. **Temperatura**: Ajusta la "temperatura" para controlar la creatividad del cuento generado. El rango válido es entre 0 y 2.
4. **Generar Cuento**: Haz clic en "Generar Cuento" para procesar la solicitud.
5. **Visualizar el Cuento**: El cuento generado se mostrará en la caja de texto grande.
6. **Guardar Cuento**: Si deseas, puedes guardar el cuento generado haciendo clic en "Guardar Cuento" y eligiendo la ubicación y el nombre del archivo.

## Notas Adicionales
- La generación del cuento puede tardar unos segundos dependiendo de la longitud y la complejidad del prompt inicial.
- Asegúrate de tener una conexión a internet activa ya que el script hace llamadas a la API de OpenAI.

## Soporte
Para obtener ayuda o reportar problemas, contacta al desarrollador o consulta la documentación de la API de OpenAI.

# Ejecución del programa demo
https://github.com/gggandre/NLP_evidencias/assets/84719490/59cf690f-f8fe-45ff-949d-74dcef5a19ed
