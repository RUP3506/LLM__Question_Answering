import streamlit as st
import dotenv
import os
import google.generativeai as genai
from datetime import datetime
# importing the variables from .env
dotenv.load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key= api_key)
# now we call the google models 



def run_model(prompt,model_name="gemini-pro"):
    start_time = datetime.now()
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    end_time = datetime.now()
    duration = end_time - start_time

    return response.text, str(duration.total_seconds())



# writing a function that will store the model lists 
list_1 = []
def model_list(model=genai):
    try:
         for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                    name = str(m.name)
                    name = name.split('/')[1]
                    list_1.append(name)
         return list_1
        
    except Exception as e:
        print(f"Error listing models: {e}")
    
model_lists = model_list()



st.header("RUPxAI V1.01")

# default model is - "gemini-pro"
default_model = "gemini-pro"

with st.sidebar:
    # creating containers 
    container_1 = st.container()
    clicked_1 = container_1.button('Show Models')

    if clicked_1:
        container_1.write('Available Models,')
        for i in model_lists:
            container_1.write(i)


selection_1 = st.selectbox(" Select Model",options=model_lists)
default_model = selection_1

clicked_2 = st.sidebar.button('Minimize')
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")


# this will reset the model
clicked_3 = st.sidebar.button('Reset Model')
if clicked_3:
    default_model = "gemini-pro"


selection_2 = st.selectbox("Select an option",options=['Text','Image'])
st.text(f"current model {default_model}")

if selection_2 == "Text":
    input_text = st.text_input("Ask me a question and I will try to answer :")
    if input_text is None:
         st.text("...")
    elif input_text:
          output,time = run_model(prompt=str(input_text),model_name = default_model)
          st.write(output)
          st.button(f"Total Time Taken : {time}")
if selection_2 == "Image":
     st.write("We are working on it, soon we will launch models which will take images as input..")

