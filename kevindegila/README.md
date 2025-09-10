python -m venv .venv

cd dossier

.\.venv\Scripts\activate

pip install fastapi

pip install "uvicorn[standard]"

Lancer CLIs:
uvicorn api:app --reload
streamlit run frontend.py

→

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

