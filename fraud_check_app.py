

import pandas as pd
import streamlit as st
import skops.io as sio

# Load your machine learning model
model = sio.load('pipeline.skops')

# Create a function to define the "Home" page
def home():
    st.title("Loan Fraud Detection App")
    st.write("Welcome to the Loan Fraud Detection App.")
    st.write("Please select an option from the sidebar.")
        # Add an image to the Home page
    st.image('loan.jpg')  

def about():
    st.title("About the Creator")
    st.write("This app was created by Naeem Bozdar.")
    st.write("You can find more about the creator on the following platforms:")
    
    # Add links to GitHub, Fiverr, Kaggle, and LinkedIn profiles
    st.markdown("[Fiverr Profile](https://www.fiverr.com/naeembozdar600)")
    st.markdown("[Kaggle Profile](https://github.com/Naeemkgf)")
    st.markdown("[LinkedIn Profile](linkedin.com/in/naeem-bozdar-95b8a825b)")

# Create a function to define the "Loan Fraud Check" page
def loan_fraud_check():
    st.title("Loan Fraud Check")
    
    # Input form for loan fraud detection
    st.subheader('Input Transaction Details')
    type_val = st.selectbox('Transaction Type', ('PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'))
    amount = st.number_input('Amount')
    old_balance_dest = st.number_input('Old Balance Destination')
    new_balance_dest = st.number_input('New Balance Destination')

    if st.button('Predict'):
        # Make a prediction
        result = predict_fraud(type_val, amount, old_balance_dest, new_balance_dest)
        st.success(f'The transaction is: {result}')

# Define a function to preprocess input data and make predictions
def predict_fraud(type_val, amount, old_balance_dest, new_balance_dest):
    # Map 'type' to numerical values
    type_mapping = {'PAYMENT': 1, 'TRANSFER': 4, 'CASH_OUT': 2, 'DEBIT': 5, 'CASH_IN': 3}
    type_val = type_mapping[type_val]
    
    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[type_val, amount, old_balance_dest, new_balance_dest]],
                              columns=['type', 'amount', 'oldbalanceDest', 'newbalanceDest'])
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    return "Fraud" if prediction[0] == 1 else "Not Fraud"

# Create a function to define the "About" page



def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page:", ["Home", "Loan Fraud Check","About"])

    if page == "Home":
        home()
    elif page == "Loan Fraud Check":
        loan_fraud_check()

    elif page == "About":
        about()

if __name__ == "__main__":
   main()
