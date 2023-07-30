import pickle
from pathlib import Path
import streamlit_authenticator as stauth
names=["Kalki","Salaar"]
usernames=["KNatuva","Rjeev"]
passwords=["KN123","Ra123"]
hspass=stauth.Hasher(passwords).generate()
file_path=Path(__file__).parent / "hashsed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hspass,file)