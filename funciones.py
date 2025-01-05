import bridges
import globales
import sulkuPypi
import sulkuFront
import gradio as gr
import gradio_client
import time
import tools

btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, request: gr.Request): #Éstos inputs debes ponerlos manuales.

    #Future: Maneja una excepción para el concurrent.futures._base.CancelledError
    #Future: Que no se vea el resultado anterior al cargar el nuevo resultado! (aunque solo se ven los resultados propios.)         

    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(tokens, globales.work)
    if autorizacion is True:
        try: 
            resultado1, resultado2, resultado3 = mass(input1)
        except Exception as e:
            print("Éste es el except de perform...")            
            info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.titulizaExcepDeAPI(e))
            return resultado, resultado, resultado, info_window, html_credits, btn_buy
    else:
        info_window, resultado, html_credits = sulkuFront.noCredit(request.username)
        return "no-credits", resultado, resultado, info_window, html_credits, btn_buy    
    
    #IMPORTANTE: Por el momento no usaré ésto porque no estamos lidiando con imagenes.
    if 1 == 1: #Porque no habrá chequeo de imagen aquí y siempre debitaremos.
        #Si es imagen, debitarás.
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    else: 
        #Si no es imagen es un texto que nos dice algo.
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.titulizaExcepDeAPI(resultado))
        return resultado, info_window, html_credits, btn_buy      
    
    # #2: ¿El resultado es debitable?
    # if debit_rules.debita(resultado) == True:
    #     html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    # else:
    #     html_credits, info_window = sulkuFront.presentacionFinal(request.username, "no debita") 
            
    #Lo que se le regresa oficialmente al entorno.
    return resultado1, resultado2, resultado3, info_window, html_credits, btn_buy

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1): #Los inputs que recibe mass también se deben agregar manualmente.
    
    api, tipo_api = tools.eligeAPI(globales.seleccion_api)
    print("Una vez elegido API, el tipo api es: ", tipo_api)

    client = gradio_client.Client(api, hf_token=bridges.hug)   
    imagenSource = gradio_client.handle_file(input1) 
          
    
    try: 
        result1, result2, result3 = client.predict(imagenSource, api_name=globales.interface_api_name)
                
        #(Si llega aquí, debes debitar de la quota, incluso si detecto no-face o algo.)
        if tipo_api == "quota":
            print("Como el tipo api fue gratis, si debitaremos la quota.")
            sulkuPypi.updateQuota(globales.process_cost)
        #No debitas la cuota si no era gratis, solo aplica para Zero.         
        
        #result = splash_tools.desTuplaResultado(result)
        return result1, result2, result3 

    except Exception as e:
            #La no detección de un rostro es mandado aquí?! Siempre?
            mensaje = tools.titulizaExcepDeAPI(e)        
            return mensaje