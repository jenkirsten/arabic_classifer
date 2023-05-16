import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2

def main():
    st.title("Streamlit App")
   
    @st.cache_resource
    def load_model():
        model = tf.keras.models.load_model('arabic_classifier.hdf5')
        return model
    
    def import_and_predict(image_data, model):
        size=(64,64)
        image = ImageOps.fit(image_data,size, Image.LANCZOS)
        image = np.asarray(image)
        image = image / 255.0
        img_reshape = np.reshape(image, (1, 64, 64, 1))
        prediction = model.predict(img_reshape)
        return prediction

    model = load_model()
    class_names =  ['أ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى']

    st.write("# Arabic Handwritten Classification")
   
    file = st.file_uploader("Choose photo from computer", type=["jpg", "png", "jpeg"])

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        prediction = import_and_predict(image, model)
        class_index = np.argmax(prediction)
        class_name = class_names[class_index]
        string = "Handwritten Output: " + class_name
        st.success(string)
 
if __name__ == "__main__":
    main()
