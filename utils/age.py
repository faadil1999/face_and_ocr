from deepface import DeepFace

def estimate_age(img_path):
    try:
        analysis = DeepFace.analyze(img_path=img_path, actions= ['age'], enforce_detection=False)
        return analysis[0]['age']
    except Exception as e: 
        return f"Erreur : {str(e)}"