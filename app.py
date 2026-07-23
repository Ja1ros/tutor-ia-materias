import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Tutor IA por Materia", page_icon="🎓")
st.title("🎓 Tutor IA por Materia")
st.write("Elige una materia y hazme tus preguntas. Te ayudare a entender el tema paso a paso.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
materia = st.sidebar.selectbox(
    "Materia",
    ["Matematicas", "Programacion", "Fisica", "Quimica", "Biologia"],
)
nivel = st.sidebar.selectbox("Nivel", ["Escolar", "Bachillerato", "Universitario"])

SYSTEM_PROMPT_TEMPLATE = (
    "Eres un tutor experto en {materia} para nivel {nivel}. "
    "Explica los conceptos de forma clara, con ejemplos y pasos numerados. "
    "Si el estudiante comete un error, corrigelo con amabilidad y explica por que."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Escribe tu pregunta aqui")

if question:
    if not api_key:
        st.warning("Ingresa tu API Key de OpenAI en la barra lateral.")
    else:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        client = OpenAI(api_key=api_key)
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(materia=materia, nivel=nivel)
        history = [{"role": "system", "content": system_prompt}] + st.session_state.messages

        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=history,
                temperature=0.3,
            )
            answer = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
