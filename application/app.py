import streamlit as st

#css
st.markdown(
    """
    <style>
        .stApp {
            background-color: pink;
            text-align: center;

        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Skincare Ingredient Classifier")
st.write("Please paste your ingredient list here:")

st.text_area("Ingredients")
st.button("Classify")

st.write("Based on these ingredients, this product is suitable for :")
