#!/usr/bin/python
import openai
import sys
#……. [ mas Código de inicialización aqui ] …………
# Se establece la clave de la API de OpenAI y se definen algunas variables
openai.api_key = ("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")
USERNAME = 'You: ' # Define el prefijo del usuario
IA = 'chatGPT: ' # Define el prefijo de la inteligencia artificial
TOP_P = 1 # Define el parámetro top_p para el modelo de OpenAI
FREQ_PENALTY = 0 # Define el parámetro frequency_penalty para el modelo de OpenAI
PRES_PENALTY = 0 # Define el parámetro presence_penalty para el modelo de OpenAI
STOP = ['You: ', 'chatGPT: '] # Define las palabras de parada para la conversación
MAX_TOKENS = 1024 # Define la cantidad máxima de tokens para la generación de texto
TEMPERATURE = 0.75 # Define el parámetro temperature para el modelo de OpenAI
NMAX = 1 # Define el parámetro n para el modelo de OpenAI
MODEL_ENGINE = "text-davinci-003" # Define el motor del modelo de OpenAI

#funcion para generar el completion y no repetir en la funcion de chatgpt_queris
def generate_completion(MODEL_ENGINE,prompt, MAX_TOKENS, NMAX, TOP_P, FREQ_PENALTY, PRES_PENALTY, TEMPERATURE, STOP):
    completion = openai.Completion.create(
                engine=MODEL_ENGINE,
                prompt=prompt,
                max_tokens=MAX_TOKENS,
                n=NMAX,
                top_p=TOP_P,
                frequency_penalty=FREQ_PENALTY,
                presence_penalty=PRES_PENALTY,
                temperature=TEMPERATURE,                
                stop=STOP
                )
    return completion.choices[0].text


#Funcion para activar la conversación con chatgpt, en principio comienza con la variable with_context en false
def chatgpt_queris(with_context = False):
    buffer = '' '' #buffer para añadir las consultas.
    if with_context == False:
        while True: #Mientras se siga ingresando consultas se ejecutará el ciclo hasta que escriban por consola "exit"
            try:
                print("Ingrese una consulta válida (o escriba 'exit' para salir): ")
                userText = input("You: ")
                if len(userText) == 0:
                    raise ValueError("Error: La consulta está vacía") #este raise genera manualmente la excepcion
                elif userText == 'exit':
                    break #Si el cliente ingresa por consola "exit" se finaliza el programa
            except ValueError as e:
                print(e)
            else:
                response = generate_completion(MODEL_ENGINE,userText, MAX_TOKENS, NMAX, TOP_P, FREQ_PENALTY, PRES_PENALTY, TEMPERATURE, STOP)
                print(f'{IA}{response}\n')  
    else:
        with_context = True
        while True: #Mientras se siga ingresando consultas se ejecutará el ciclo hasta que escriban por consola "exit"
            try:
                print("Ingrese una consulta válida (o escriba 'exit' para salir): ")
                userText = input("You: ")
                if len(userText) == 0:
                    raise ValueError("Error: La consulta está vacía") #este raise genera manualmente la excepcion
                elif userText == 'exit':
                    break
            except ValueError as e:
                print(e)
            else:
                buffer += f'{USERNAME}{userText}\n {IA}'
                response = generate_completion(MODEL_ENGINE,buffer, MAX_TOKENS, NMAX, TOP_P, FREQ_PENALTY, PRES_PENALTY, TEMPERATURE, STOP)
                buffer += response
                print(f'{IA}{response.strip()}\n')  


      
if len(sys.argv) > 1: #Si el tamaño del argumento es mayor a uno quiere decir que se ha ingresado una consulta, además chequea si en la primer posición se encuentra la palabra '--convers'
    if sys.argv[1] == '--convers':
        print('¡Bienvenido a la conversación con ChatGPT!')
        chatgpt_queris(with_context = True)
else:
    chatgpt_queris(with_context = False)


        

