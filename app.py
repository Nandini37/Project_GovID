import streamlit as st
from PIL import Image
from service import predict
import os
import shutil
import time

# Title for the app
st.title("Adhar Card Processor")

# Sidebar for uploading image
st.sidebar.header("Upload your image here:")
uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_image is not None:
    # Open the image using PIL
    image = Image.open(uploaded_image)
    
    if st.button("Save Me"):
    # Perform an action when the button is clicked
   
        image.save("image.png")
        st.write("Button clicked! Performing an operation...")
    
        # Display the image in the main window
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Display image details
        st.write("Image Format: ", image.format)
        st.write("Image Size: ", image.size)
        st.write("Image Mode: ", image.mode)

        response = predict()
        st.write(response)
        st.image("static/runs/detect/predict/image.png")
       # time.sleep(10)
        #os.rmdir("static/runs")
        shutil.rmtree("static/runs")

else:
    st.write("Upload an image to display its details.")
