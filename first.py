import streamlit as st
import tempfile
from gemini import get_response_from_model
import json
from streamlit_lottie import st_lottie 
import time
import os

st.session_state['file_details']=''
def streamlit_app():
  API_KEY=""
  with st.sidebar:
    API_KEY=st.text_input("Gemini API Key", key="gemini_api_key", type="password")
  
  st.title(":rainbow[Code Converter]")  # Display a heading
  uploaded_file = st.file_uploader("Choose a Java file (.java)", type='java')

  if uploaded_file is not None:
    file_details = uploaded_file.name
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
      tmp_file.write(uploaded_file.read())
      file_path = tmp_file.name  # Get the full path of the temporary file
    st.success(f"Successfully uploaded '{file_details}'")
    st.session_state['file_details']=file_details
    display_java_code(file_path,API_KEY)



   

def display_java_code(file_path,API_KEY):
  """Displays the contents of the selected Java file."""
  # path = ".\\Animation - 1717139221779.json"
  path = "JAVA-PY-code-converter/Animation - 1717139221779.json"
  st.write(os.path.exists(path))
  with open(path,"r") as file: 
    url = json.load(file) 
  try:
    with open(file_path, 'r') as java_file:
      java_code = java_file.read()
      if st.checkbox(":blue[View Input Code]"):
        st.code(java_code,language="java")  # Highlight as Java code
      if st.button('Generate'):
        F=0
        # with st.spinner("Generating code"):
        output=""
        with st.empty():
          col1,col2,col3=st.columns([1,1,1])
          with col2:
            st_lottie(url, 
              reverse=True, 
              height=150, 
              width=150, 
              speed=1, 
              loop=True, 
              quality='high', 
              key='Loader'
            )
          time.sleep(1)
          output=get_response_from_model(java_code,API_KEY)
          st.success("Generated Code Successfully.")
          F=1
        if F==1:
          st.code(output,language="python")
          if output is not '':
            download_code(output)
        
  except FileNotFoundError:
    st.error(f"Error: File '{file_path}' not found.")
  

def download_code(code):

  button_clicked = st.download_button(
      label="Download Code",
      data=code,
      file_name=st.session_state['file_details'].replace(".java",".py"), 
      mime="text/python",
  )

  # Optional: Display a success message if the button is clicked
  if button_clicked:
    st.success("Code downloaded successfully!")
streamlit_app()

