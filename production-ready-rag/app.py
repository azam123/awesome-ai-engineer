import gradio as gr
from vectorstore import build_index
from rag import ask
state={'db':None}
def upload(pdf): 
  state['db']=build_index(pdf.name);
  return 'Indexed'
  
def chat(m,h): 
  return ask(state['db'],m) if state['db'] else 'Upload PDF first'
  with gr.Blocks() as demo:
   gr.Markdown('# Production RAG PDF Chatbot');f=gr.File(file_types=['.pdf']);s=gr.Markdown();f.upload(upload,f,s);gr.ChatInterface(chat)
  demo.launch(debug=True,share=True)
