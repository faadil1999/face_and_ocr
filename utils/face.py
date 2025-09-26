import face_recognition
import dlib
print("dlib imported successfully")
print("dlib version:", dlib.__version__)
print("CUDA available:", dlib.DLIB_USE_CUDA)


def compare_faces(img_path1, img_path2):
    img1 = face_recognition.load_image_file(img_path1)
    img2 = face_recognition.load_image_file(img_path2)

    enc1 = face_recognition.face_encodings(img1)
    enc2 = face_recognition.face_encodings(img2)

    if len(enc1) == 0 or len(enc2) == 0:
        return None
    result = face_recognition.compare_faces([enc1[0]], enc2[0])
    distance = face_recognition.face_distance([enc1[0]], enc2[0])[0]
    return result[0], 1 - distance