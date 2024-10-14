import gradio as gr

def greet(name):
    return f"Hello, Hola, Tervetuloa, Cheers {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch(root_path="/gradio-demo")

# try:
#     demo = gr.Interface(fn=greet, inputs="text", outputs="text").launch(root_path="/gradio-demo")
# except:
#     raise gr.Error("ERROR 182")
