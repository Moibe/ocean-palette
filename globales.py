import gradio as gr

#MAIN
version = "0.0.3"
env = "dev"
aplicacion = "palette-dev"

seleccion_api = "eligeGratisOCosto" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/image-blend", "quota")
api_cost = ("Moibe/image-blend", "costo")
#A o B
api_a = ("Moibe/image-blend", "gratis")
api_b = ("Moibe/image-blend", "gratis")
#Gratis o Costo
api_gratis = ("Moibe/deteccion-colores", "gratis")
api_costo = ("Moibe/deteccion-colores", "costo")

interface_api_name = "/gradio_interface" #El endpoint al que llamará client.

process_cost = 0
seto = "palette"
work = "picswap"
app_path = "/palette-dev"
server_port=7820
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"

#Future: Put age to cookies.
