import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('Pickle_file.pkl','rb'))

def predict_forest(age,sex,children,smoker_norm,obese):
    input=np.array([[age,sex,children,smoker_norm,obese]]).astype(np.float64)
    prediction=model.predict(input)
    prediction = float(prediction)
    round(prediction,2)
    return (prediction)


def main():
    st.title("Insurance Premium Calculator")
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://image.freepik.com/free-photo/top-view-health-insurance-form-eyeglasses-with-stethoscope-wooden-background-business-healthcare-concept-savings-flat-lay-copy-space_1921-31.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://image.freepik.com/free-photo/top-view-health-insurance-form-eyeglasses-with-stethoscope-wooden-background-business-healthcare-concept-savings-flat-lay-copy-space_1921-31.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    html_temp = """
    <div style="background-color:#EFC970 ;padding:10px">
    <h2 style="color:black;text-align:left;font-size: 20px">Enter the following details to predict your Health Insurance Premium </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age","Type Here")
    sex = st.text_input("Sex","Type Here: 0-Female; 1-Male")
    smoker_norm = st.text_input("Smoking","Type Here: 0-No; 1-Yes")
    obese = st.text_input("Obesity","Type Here: 0-No; 1-Yes")
    children = st.text_input("Children","Type Here")

    if st.button("Predict"):
        output=predict_forest(age,sex,children,smoker_norm,obese)
        output = round(output,2)
        st.success('We suggest you to choose an health insurance premium coverage of Rs.{}'.format(output))

if __name__=='__main__':
    main()
    
    
