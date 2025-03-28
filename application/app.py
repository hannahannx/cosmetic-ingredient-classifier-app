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

with st.sidebar:
    st.write("This project aims so classify inputted ingredient list into suitable skin types")

st.text_area("Ingredients")
st.button("Classify")

allSkinTypes = ["Oily","Dry","Sensitive","Combination"]
options = st.segmented_control(
     "Skin Type", allSkinTypes, selection_mode="multi"
)
st.write(f"Based on these ingredients, this product is suitable for :{options}")
