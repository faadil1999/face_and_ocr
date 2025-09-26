# 🧑‍💻 Face Recognition & OCR App

Application en **Python + Streamlit** permettant :  
- 🔍 **Comparer des visages** (détection et similarité avec `face-recognition`)  
- 👤 **Estimer l’âge** d’une personne (`DeepFace`)  
- 📄 **Extraire du texte de documents d’identité** (OCR via `Tesseract`)  

---

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/ton-compte/face_id_ocr.git
cd face_id_ocr
```
### 2. Créer et activer un environnement Conda
```
conda create -n face_id_ocr python=3.9 -y
conda activate face_id_ocr
```
### 3. Installer les dépendances système (Ubuntu)
```
sudo apt update
sudo apt install -y build-essential cmake libopenblas-dev liblapack-dev \
libx11-dev libgtk-3-dev libboost-all-dev python3-dev \
tesseract-ocr libtesseract-dev
```
### 4. Installer les dépendances Python
Toutes les dépendances sont listées dans requirements.txt.
```
pip install -r requirements.txt
```

## 🚀 Utilisation
Lancer l’application avec :
```
streamlit run app.py

```

## 📂 Structure du projet
```
face_id_ocr/
│── app.py                # Interface principale (Streamlit)
│── utils/
│   ├── face.py            # Comparaison des visages
│   ├── age.py             # Estimation d'âge avec DeepFace
│   └── ocr.py             # Extraction de texte (OCR)
│── assets/                # Images temporaires
│── requirements.txt       # Dépendances Python
```
