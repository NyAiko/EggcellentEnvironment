import streamlit as st
import numpy as np
import pandas as pd
import joblib
def main():
    st.title("Egg Production - Environmental Effect")
    st.text("Welcome to this APP. See here how total egg production will be based on environment")
    form = st.form(key='form')
    Amount_of_chicken = form.number_input(label="Amount of Chicken",step=1,min_value=2550)
    Temperature = form.number_input(label="Temperature",min_value=28,max_value=35)
    Light_Intensity = form.number_input(label="Light Intensity",min_value=200,max_value=385)
    Noise = form.number_input(label="Noise",min_value=75,max_value=245)

    form.form_submit_button(label="Predict")
    cols = ["Amount_of_chicken", "Temperature", "Light_Intensity", "Noise"]
    data = np.array([Amount_of_chicken, Temperature, Light_Intensity, Noise]).reshape(1,-1)
    X_input = pd.DataFrame(data, columns=cols)
    prediction = predict(X_input)
    st.write(f"Total Production: {prediction} Eggs")
    
def predict(X):
    model = joblib.load("ml_model.p")
    return int(model.predict(X))
    
if __name__=="__main__":
    main()
    