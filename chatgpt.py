"""
Consumo de API de Chatgpt para establecer comunicación 
con la misma, con o sin contexto.
"""
import sys
import openai
# ……. [ mas Código de inicialización aqui ] …………
# Se establece la clave de la API de OpenAI y se definen algunas variables
openai.api_key = "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"
username = 'You: '  # Define el prefijo del usuario
IA = 'chatGPT: '  # Define el prefijo de la inteligencia artificial
top_p = 1  # Define el parámetro top_p para el modelo de OpenAI
freq_penalty = 0  # Define el parámetro frequency_penalty para el modelo de OpenAI
pres_penalty = 0  # Define el parámetro presence_penalty para el modelo de OpenAI
# Define las palabras de parada para la conversación
stop = ['You: ', 'chatGPT: ']
max_tokens = 1024  # Define la cantidad máxima de tokens para la generación de texto
temperature = 0.75  # Define el parámetro temperature para el modelo de OpenAI
nmax = 1  # Define el parámetro n para el modelo de OpenAI
model_engine = "text-davinci-003"  # Define el motor del modelo de OpenAI
"""
En esta función se genera el completion para no repetirlo dentro
de la función de chatgpt_queris, ya que se utiliza en dos oportunidades
Para conversaciones con contexto y sin.
"""
def generate_completion(MODEL_ENGINE, PROMPT, MAX_TOKENS, N_MAX, TOP_P, FREQ_PENALTY,PRES_PENALTY, TEMPERATURE, STOP):
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=PROMPT,
        max_tokens=MAX_TOKENS,
        n=N_MAX,
        top_p=TOP_P,
        frequency_penalty=FREQ_PENALTY,
        presence_penalty=PRES_PENALTY,
        temperature=TEMPERATURE,
        stop=STOP
    )
    return completion.choices[0].text
# Funcion para activar la conversación con chatgpt
# en principio comienza con la variable with_context en false
def chatgpt_queris(with_context=False):
    buffer = ''  # buffer para añadir las consultas.
    if with_context == False:
        while True:  # se ejecuta el ciclo while hasta que se ingrese un exit
            try:
                print("Ingrese una consulta válida (o escriba 'exit' para salir): ")
                user_text = input("You: ")
                if len(user_text) == 0:
                    # genera manualmente la excepcion
                    raise ValueError("Error: La consulta está vacía")
                elif user_text == 'exit':
                    break  # Si el cliente ingresa por consola "exit" se finaliza el programa
            except ValueError as value_error:
                print(value_error)
            else:
                response = generate_completion(
                    model_engine, user_text, max_tokens, nmax, top_p, freq_penalty, pres_penalty, temperature, stop)
                print(f'{IA}{response}\n')
    else:
        with_context = True
        while True:
            try:
                print("Ingrese una consulta válida (o escriba 'exit' para salir): ")
                user_text = input("You: ")
                if len(user_text) == 0:
                    raise ValueError("Error: La consulta está vacía")
                elif user_text == 'exit':
                    break
            except ValueError as value_error:
                print(value_error)
            else:
                buffer += f'{username}{user_text}\n {IA}'
                response = generate_completion(
                    model_engine, buffer, max_tokens, nmax, top_p, freq_penalty, pres_penalty, temperature, stop)
                buffer += response
                print(f'{IA}{response.strip()}\n')
# Si el tamaño del argumento es mayor a uno quiere decir que se ha ingresado una consulta.
if len(sys.argv) > 1:
    # en esta linea chequea si en la primer posición se encuentra la palabra '--convers'
    if sys.argv[1] == '--convers':
        print('¡Bienvenido a la conversación con ChatGPT!')
        chatgpt_queris(with_context=True)
else:
    chatgpt_queris(with_context=False)