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

while True: #bucle infinito que se ejecuta continuamente hasta que lo detiene explicitamente el break
    userText = input("\nIngrese su consulta:" ) #En el userText se ingresa la consulta del usuario

    completion = openai.Completion.create(
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
    if len(userText) > 0:
        print("You: ",userText)
        print("ChatGPT: ",completion.choices[0].text)
        break
    else:
        print("La consulta está vacía, por favor ingresa una consulta válida.")


    