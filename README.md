# 🧴 Cosmetic Ingredient Classifier
*A Machine Learning Web App for Skin Type Classification*

## 📌 Overview  
This project explores the use of machine learning and natural language processing (NLP) techniques to classify skincare products by skin type (e.g., oily, dry, sensitive) based on their ingredient lists.

The system allows users to paste product ingredients into a web interface, and it predicts which skin types the product is most suitable for.
---

## 🎯 Objectives  
- Develop an interactive web app for ingredient-based product analysis  
- Apply NLP to process unstructured ingredient lists  
- Train multiple supervised machine learning models  
- Evaluate classification performance using metrics like precision, recall, and F1-score  
- Provide explainable outputs to help users understand predictions  

---

## 💡 Features s 
- 🌿 **Ingredient Input Box**: Paste a list of ingredients directly into the app  
- 🔍 **Multi-label Classification**: Predicts all applicable skin types (e.g., "dry", "oily", "sensitive")  
- 🧠 **ML Models Used**:  
  - Random Forest (with `MultiOutputClassifier`)  
  - K-Nearest Neighbour  
  - Support Vector Machine  
  - Neural Network (MLPClassifier)  
- 🧾 **TF-IDF Vectorization** for NLP-based feature extraction  
- 📊 **Model Comparison Dashboard** (coming soon)  

---

## 🛠 Technologies Used  
- Python  
- Streamlit  
- scikit-learn  
- pandas, numpy  
- matplotlib  

---

## 🧪 Dataset  
- A curated dataset of skincare products and their ingredient lists  
- Labelled with appropriate skin types (multi-label)  
- Cleaned and pre-processed for ML tasks  

---

## 🧩 How It Works  
1. User pastes a product’s ingredient list into the web interface  
2. The system preprocesses the text using TF-IDF vectorisation  
3. The trained model(s) predict the most suitable skin types  
4. Results are displayed clearly

---
---

## 🚧 Project Status  
- Features and functionality may change over time  
- Some models and data visualizations are still being refined  

