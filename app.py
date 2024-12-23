import streamlit as st
from PIL import Image
from service import predict
from proces_output import process_crops
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
   
        try:
            image.save("image.jpg")
            st.write("Button clicked! Performing an operation...")
        
            # Display the image in the main window
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Display image details
            st.write("Image Format: ", image.format)
            st.write("Image Size: ", image.size)
            st.write("Image Mode: ", image.mode)

            response = predict()
            # st.write(response)
            st.image("govt_id/adhaar/image.jpg")

            result = process_crops()

            st.write(result)
        except: 
            if os.path.isdir("govt_id/adhaar/") :
                shutil.rmtree("govt_id/adhaar/")

else:
    st.write("Upload an image to display its details.")
