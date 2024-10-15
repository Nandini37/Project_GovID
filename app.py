import streamlit as st
from PIL import Image

# Title for the app
st.title("Image Uploader")

# Sidebar for uploading image
st.sidebar.header("Upload your image here:")
uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_image is not None:
    # Open the image using PIL
    image = Image.open(uploaded_image)
    
    # Display the image in the main window
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Display image details
    st.write("Image Format: ", image.format)
    st.write("Image Size: ", image.size)
    st.write("Image Mode: ", image.mode)

    # Option to download the image
    with open("download_image.png", "wb") as f:
        f.write(uploaded_image.getbuffer())
    st.download_button(label="Download Image", data=open("download_image.png", "rb"), file_name="downloaded_image.png")

else:
    st.write("Upload an image to display its details.")
