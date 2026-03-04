import streamlit as st
import json

from content_generator import (
    generate_explanation,
    generate_examples,
    generate_reflection_questions,
    generate_visual_summary
)

from storage import (
    get_full_history,
    get_history_by_student,
    get_history_by_topic
)

#Configurações da página
st.set_page_config(
    page_title="Sistema Educacional com IA",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Sistema Educacional Inteligente")
st.markdown("Geração personalizada de conteúdo com histórico e cache.")

#Carregar alunos
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

student_names = [student["name"] for student in students]

#Seleção de perfil
st.markdown("## 👤 Perfil do Aluno")

selected_name = st.selectbox(
    "Selecione o aluno:",
    student_names
)

student_profile = next(
    student for student in students if student["name"] == selected_name
)

col1, col2, col3 = st.columns(3)
col1.metric("Idade", student_profile["age"])
col2.metric("Nível", student_profile["level"])
col3.metric("Estilo", student_profile["learning_style"])

st.markdown("---")

#Tema
st.markdown("## 📝 Tema")

topic = st.text_input("Digite o tema que deseja estudar:")

st.markdown("---")

#Ação principal
st.markdown("## 🚀 Ação")

main_option = st.radio(
    "O que deseja fazer?",
    ("Gerar Conteúdo", "Ver Histórico")
)

#Gerar conteúdo
if main_option == "Gerar Conteúdo":

    content_type = st.radio(
        "Escolha o tipo de conteúdo:",
        ("Explicação", "Exemplos", "Reflexão", "Visual")
    )

    if st.button("✨ Gerar Agora"):

        if not topic:
            st.warning("Por favor, digite um tema antes de gerar.")
        else:
            with st.spinner("Gerando conteúdo personalizado..."):

                if content_type == "Explicação":
                    result = generate_explanation(topic, student_profile)

                elif content_type == "Exemplos":
                    result = generate_examples(topic, student_profile)

                elif content_type == "Reflexão":
                    result = generate_reflection_questions(topic, student_profile)

                else:
                    result = generate_visual_summary(topic, student_profile)

            st.markdown("---")
            st.markdown("## 📄 Resultado")
            st.markdown(result)


#Histórico
else:

    st.markdown("## 📊 Histórico")

    history_option = st.radio(
        "Filtrar histórico por:",
        ("Completo", "Por Aluno Selecionado", "Por Tema Atual")
    )

    if history_option == "Completo":
        history = get_full_history()

    elif history_option == "Por Aluno Selecionado":
        st.info(f"Mostrando histórico de: {selected_name}")
        history = get_history_by_student(selected_name)

    else:
        if topic:
            st.info(f"Mostrando histórico do tema: {topic}")
            history = get_history_by_topic(topic)
        else:
            st.warning("Digite um tema para filtrar por assunto.")
            history = []

    if history:
        st.markdown(f"### 🔎 {len(history)} registro(s) encontrado(s)")

        for record in reversed(history):
            st.markdown("---")
            st.markdown(f"**📅 Data:** {record['timestamp']}")
            st.markdown(f"**👤 Aluno:** {record['student']}")
            st.markdown(f"**📚 Tema:** {record['topic']}")
            st.markdown(f"**📌 Tipo:** {record['content_type']}")

            with st.expander("📖 Ver Conteúdo"):
                st.markdown(record["output"])
    else:
        st.info("Nenhum registro encontrado.")
