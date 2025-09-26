import streamlit as st
from utils.face import compare_faces
from utils.age import estimate_age
from utils.ocr import extract_text

st.set_page_config(page_title="Face & ID OCR", layout="wide")

st.title("🧑‍💻 Face Recognition & OCR App")

menu = st.sidebar.radio("Navigation", ["Comparer Visages", "Estimer Âge", "OCR Document"])

if menu == "Comparer Visages":
    st.header("Comparer deux visages")
    img1 = st.file_uploader("Choisir la première image", type=["jpg","jpeg","png"])
    img2 = st.file_uploader("Choisir la deuxième image", type=["jpg","jpeg","png"])
    if img1 and img2:
        with open("assets/img1.jpg","wb") as f: f.write(img1.read())
        with open("assets/img2.jpg","wb") as f: f.write(img2.read())
        result, score = compare_faces("assets/img1.jpg", "assets/img2.jpg")
        st.success(f"Résultat : {'Même personne ✅' if result else 'Différente ❌'} (similarité : {score:.2f})")

elif menu == "Estimer Âge":
    st.header("Estimation de l’âge")
    img = st.file_uploader("Choisir une image", type=["jpg","jpeg","png"])
    if img:
        with open("assets/age.jpg","wb") as f: f.write(img.read())
        age = estimate_age("assets/age.jpg")
        st.info(f"Âge estimé : {age} ans")

elif menu == "OCR Document":
    st.header("OCR sur document d’identité")
    img = st.file_uploader("Choisir une image (ID, passeport...)", type=["jpg","jpeg","png"])
    if img:
        with open("assets/doc.jpg","wb") as f: f.write(img.read())
        text = extract_text("assets/doc.jpg")
        st.text_area("Texte extrait :", text, height=200)
