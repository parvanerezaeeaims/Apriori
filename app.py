
import streamlit as st  
import pandas as pd  
from Apriori import apriori_product



# Set up the page configuration  
st.set_page_config(page_title="Customer Grocery Transactions:", page_icon=":bar_chart:", layout="wide")
st.title("Customer Grocery Transactions:")
st.sidebar.title("Apriori Algorithm:")
st.sidebar.markdown("""
    <div style='border: 2px solid #ddd; padding: 15px; border-radius: 8px; background-color: #001f3f; color: white;'>
        <h1 style='font-size:18px;'>min_support = 0.1</h1>
        <h1 style='font-size:18px;'>min_lift = 1.2</h1>
        <h1 style='font-size:18px;'>min_confidence = 0.7</h1>
    </div>
""", unsafe_allow_html=True)



df=df = pd.read_excel(r"C:\Users\ASUS\Desktop\project\apriori\Apriori.xlsx")  




# Display the first few rows of the dataset  
st.subheader("Dataset Overview")  
st.write(df.head(10))  


# Run Apriori analysis and cache the result
result = apriori_product(df, min_support=0.1, min_lift=1.2, min_confidence=0.7)



if not result.empty:
    st.subheader("Association Rules:")
    st.dataframe(result.style.background_gradient(cmap="viridis"))
else:
    st.write("No association rules found with the given parameters.")
