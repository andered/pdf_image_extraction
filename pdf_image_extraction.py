import streamlit as st
import io
import os
import fitz
from PIL import Image
from os import listdir


st.set_page_config(page_title='PDF Image Extraction')
st.title('PDF Image Extraction')


with st.sidebar:
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    #st.markdown('Images will be extracted from an uploaded PDF')
    st.markdown('**Right click on images and save to file**')

    
if uploaded_file is not None:
    file_details = {"filename":uploaded_file.name, "filetype":uploaded_file.type,"filesize":uploaded_file.size}
    st.write("Filename: ",uploaded_file.name)
    st.write("File type: ", uploaded_file.type)
    st.write("File size: ", uploaded_file.size)
    
    #st.json(file_details)
    pdf_file = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    image_count = 0
    
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()
        # printing number of images found in this page
        #if image_list:
          #  st.markdown(f"**[+] Found {len(image_list)} images in page {page_index}**")
      #  else:
           # st.markdown(f"**[!] No images found on page {page_index}**")
    
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            image_count=image_count+1
            st.markdown(f"image number: {image_count} / file type:  {image_ext} / page: {page_index+1} ")
            #st.image(image, width=500, caption= (f"page: {page_index+1} / image number:  {image_count} / file type: {image_ext}"))
            with st.container():
                st.image(image, width=500)
                st.markdown("""---""")
    

    
    
    