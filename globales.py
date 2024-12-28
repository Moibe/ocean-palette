import gradio as gr

#MAIN
version = "4.6.11"
env = "dev"
aplicacion = "astroblend-dev"

seleccion_api = "eligeGratisOCosto" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = "Moibe/image-blend"
api_cost = "Moibe/image-blend"

#A o B
api_a = "Moibe/image-blend"
api_b = "Moibe/image-blend"

#Gratis o Costo
api_gratis = "Moibe/image-blend"
api_costo = "Moibe/image-blend"

same_api = True
process_cost = 0
#api = "Kwai-Kolors/Kolors-Character-With-Flux"
seto = "image-blend"
work = "picswap"
app_path = "/boilerplate"
server_port=7860
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"

#Future: Put age to cookies.