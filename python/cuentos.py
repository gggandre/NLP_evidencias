import os
import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import threading
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

class GeneradorDeCuentos:
    def __init__(self, api_key):
        self.api_key = api_key

    def generar_cuento(self, inicio, longitud=100, temperatura=0.7):
        """
        La función generar_cuento genera un cuento para niños utilizando el modelo GPT-3.5-turbo de OpenAI,
        comenzando con un prompt dado.
        :param inicio: El parámetro "inicio" es una cadena que representa la oración inicial o prompt para el cuento.
        Es la entrada inicial proporcionada al modelo de lenguaje para generar el resto del cuento.
        :param longitud: El parámetro "longitud" determina el número máximo de tokens (palabras o caracteres)
        que debe tener el cuento generado. Especifica la longitud deseada del cuento, por defecto es 100 (opcional).
        :param temperatura: El parámetro "temperatura" en la función "generar_cuento" se utiliza para controlar la aleatoriedad 
        del texto generado. Un valor de temperatura más alto (por ejemplo, 1.0) resultará en una salida más aleatoria y creativa,
        mientras que un valor de temperatura más bajo (por ejemplo, 0) producirá una salida más predecible y conservadora.
        :return: La función generar_cuento devuelve un cuento generado para niños basado en los parámetros dados.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': 'Genera un cuento para niños que comience con: ' + inicio},
                {'role': 'user', 'content': inicio}
            ],
            'max_tokens': longitud,
            'temperature': temperatura
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        cuento = response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()
        return cuento

def generar_y_mostrar():
    """
    La función generar_y_mostrar genera y muestra una historia basada en la entrada del usuario para el punto de inicio,
    longitud y temperatura.
    """
    try:
        inicio = entrada_inicio.get()
        longitud = int(entrada_longitud.get())
        temperatura = float(entrada_temperatura.get())

        # Validar la longitud del cuento (tokens)
        if longitud < 50 or longitud > 500:
            messagebox.showerror("Error", "La longitud debe estar entre 50 y 500 tokens.")
            return

        # Validar la temperatura
        if temperatura < 0 or temperatura > 2:
            messagebox.showerror("Error", "La temperatura debe estar entre 0 y 2.")
            return

        boton_generar.config(state=tk.DISABLED)
        texto_cuento.delete(1.0, tk.END)

        def generar():
            cuento = generador.generar_cuento(inicio, longitud, temperatura)
            texto_cuento.insert(tk.END, cuento)
            boton_generar.config(state=tk.NORMAL)

        threading.Thread(target=generar).start()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para longitud y temperatura.")

def guardar_cuento():
    """
    La función guardar_cuento() guarda el contenido de un cuadro de texto en un archivo seleccionado por el usuario.
    """
    cuento = texto_cuento.get(1.0, tk.END)
    archivo = filedialog.asksaveasfilename(defaultextension='.txt')
    if archivo:
        with open(archivo, 'w') as f:
            f.write(cuento)

# Cargar la clave API desde el archivo .env
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No se encontró la clave API de OpenAI. Asegúrate de que esté definida en el archivo .env")

generador = GeneradorDeCuentos(api_key)

ventana = tk.Tk()
ventana.title("Generador de Cuentos para Niños")

tk.Label(ventana, text="Inicio del cuento:").pack()
entrada_inicio = tk.Entry(ventana, width=50)
entrada_inicio.pack()

tk.Label(ventana, text="Longitud del cuento (tokens):").pack()
entrada_longitud = tk.Entry(ventana, width=20)
entrada_longitud.insert(0, "100")
entrada_longitud.pack()

tk.Label(ventana, text="Temperatura (creatividad):").pack()
entrada_temperatura = tk.Entry(ventana, width=20)
entrada_temperatura.insert(0, "0.7")
entrada_temperatura.pack()

boton_generar = tk.Button(ventana, text="Generar Cuento", command=generar_y_mostrar)
boton_generar.pack()

texto_cuento = tk.Text(ventana, height=15, width=50)
texto_cuento.pack()

boton_guardar = tk.Button(ventana, text="Guardar Cuento", command=guardar_cuento)
boton_guardar.pack()

ventana.mainloop()
