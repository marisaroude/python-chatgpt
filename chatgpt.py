#!/usr/bin/python
import openai

#……. [ mas Código de inicialización aqui ] …………
openai.api_key = ("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")
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

#…..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
# Set up the model and prompt

while True: #se ejecutará hasta el break. 
    userText = input("\nIngrese su consulta:" ) #En el userText se ingresa la consulta del usuario
    try:
        if len(userText) > 0: #Verifica si la longitud del input es mayor a cero para aceptar una consulta valida y no vacía
            completion = openai.Completion.create(  #puse el completion dentro del if porque al ingresar una consulta vacía me guardaba una respuesta random desde chatgpt y al hacer la consulta correcta me devolvía cualquier cosa, entonces, en este caso, primero se evalúa la longitud para invocar al completion
                engine=MODEL_ENGINE,
                prompt=userText,
                max_tokens=MAX_TOKENS,
                n=NMAX,
                top_p=TOP_P,
                frequency_penalty=FREQ_PENALTY,
                presence_penalty=PRES_PENALTY,
                temperature=TEMPERATURE,                
                stop=STOP
            )
            print("You: ",userText) #devuelve la consulta 
            print("ChatGPT: ",completion.choices[0].text) #devuelve la primer opción de respuesta desde la API
            break
        else: #Si la consulta esta vacia se produce una excepción en este caso value error que muestra que la consulta está vacía
            raise ValueError("La consulta está vacía, por favor ingresa una consulta válida.") #este raise genera manualmente la excepcion
    except ValueError as e:  #except maneja la excepción ya producida
            print(e)
   
