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
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Enter the following details to predict your Insurance Premium </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    age = st.text_input("Age","Type Here")
    sex = st.text_input("Sex","Type Here")
    children = st.text_input("Childrens","Type Here")
    smoker_norm = st.text_input("Smoking","Type Here")
    obese = st.text_input("Obesity","Type Here")
#    safe_html="""  
#      <div style="background-color:#F4D03F;padding:10px >
#       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
#       </div>
#    """
#    danger_html="""  
#      <div style="background-color:#F08080;padding:10px >
#       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
#       </div>
#    """

    if st.button("Predict"):
        output=predict_forest(age,sex,children,smoker_norm,obese)
        output = round(output,2)
        st.success('You should take an health insurance premium of Rs.{}'.format(output))

        #if output > 0.5:
        #    st.markdown(danger_html,unsafe_allow_html=True)
        #else:
        #    st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
    
    
