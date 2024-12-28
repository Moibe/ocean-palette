import gradio as gr

#MAIN
version = "4.8.12"
env = "dev"
aplicacion = "astroblend-dev"

seleccion_api = "eligeGratisOCosto" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/image-blend", "gratis")
api_cost = ("Moibe/image-blend", "costo")
#A o B
api_a = ("Moibe/image-blend", "gratis")
api_b = ("Moibe/image/blend", "gratis")
#Gratis o Costo
api_gratis = ("Moibe/image-blend", "gratis")
api_costo = ("Moibe/image-blend", "costo")

process_cost = 0
seto = "image-blend"
work = "picswap"
app_path = "/boilerplate"
server_port=7860
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"

#Future: Put age to cookies.