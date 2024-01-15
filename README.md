# Not-by-Bot: Authentic Human Content Certificate

This project is dedicated to ensuring the authenticity of human-generated content. Our goal is to leverage 

## Technologies Used
- **KerasNLP**
- **Streamlit**
- **NextJs**
- **FastAPI**
- **Docker**

## Project Structure

### 1. Frontend
- **Landing Page:** Placeholder for detailed information.

### 2. Backend
- **Streamlit Dashboard:** Interactive dashboard for data visualization.
- **API (FastAPI):** Backend API to handle requests.
- **Deep Learning Model (Keras NLP):** Utilizing Keras for Natural Language Processing.

## Team
- **Mann Acharya (E21CSEU0410)**
- **Salik Uddin**
- **Nabh Raghav**
- **Aviral Jain**
- **Archit Ojha**

## Dependencies
- pandas
- numpy
- keras
- keras-nlp
- tensorflow
- fastapi
- streamlit

## Installation Guide

### 1. Frontend
```bash
npm install
npm run dev
```

### 2. Backend
```bash
poetry install
# To export requirements.txt
poetry export -f requirements.txt --output requirements.txt

# To start Streamlit app
streamlit run app.py

# To run the backend
uvicorn run ...
```