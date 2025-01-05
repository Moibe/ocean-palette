import sets
import time

def inputs_selector(set):    

    # Obtener la configuración según el valor de 'set'
    config = sets.configuraciones.get(set)

    # Si la configuración existe, usarla
    if config:
        if len(config) == 2:
            input1 = config["input1"]
            result = config["result"]
            return input1, result
        elif len(config) == 3:
            input1 = config["input1"]
            input2 = config["input2"]
            result = config["result"]            
            return input1, input2, result
        elif len(config) == 4: #palette
            input1 = config["input1"]
            result1 = config["result1"]
            result2 = config["result2"]
            result3 = config["result3"]
            return input1, result1, result2, result3 
    else:
        print("Set no válido")