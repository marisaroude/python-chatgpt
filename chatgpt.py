#!/usr/bin/python
import openai
import sys
#……. [ mas Código de inicialización aqui ] …………
openai.api_key = ("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")
USERNAME = 'You: '
IA = 'chatGPT: '
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=["You: ", "chatGPT: "]
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"
 #Buffer para almacenar consultas no nulas.


#…..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
# Set up the model and prompt
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



def chatgpt_queris(with_context = False):
    buffer = ''
    if with_context == False:
        while True:
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


        

