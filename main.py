# Ponto de entrada da aplicação. Orquestra seleção de aluno, tópico e geração de conteúdo.

import json
from content_generator import (generate_explanation, generate_examples, generate_reflection_questions, generate_visual_summary)
from storage import (save_execution, get_full_history, get_history_by_student, get_history_by_topic)


def load_students():
    with open("students.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    students = load_students()

    print("Escolha um aluno:")
    for student in students:
        print(f"[{student['id']}] {student['name']}")

    selected_id = int(input("\nAluno: "))

    student_profile = next(
        student for student in students if student["id"] == selected_id
    )

    topic = input("\nDigite o tópico: ")

    print("""
Escolha o tipo de conteúdo:
[1] Explicação conceitual
[2] Exemplos práticos
[3] Perguntas de reflexão
[4] Resumo visual
[5] Ver histórico
""")

    option = input("Conteúdo: ")

    if option != "5":
        if option == "1":
            result = generate_explanation(topic, student_profile)
        elif option == "2":
            result = generate_examples(topic, student_profile)
        elif option == "3":
            result = generate_reflection_questions(topic, student_profile)
        elif option == "4":
            result = generate_visual_summary(topic, student_profile)
        else:
            print("Opção inválida.")
            return

        print("\nResultado:\n")
        print(result)

        #Salvando os resultados
        content_map = {
            "1": "explanation",
            "2": "examples",
            "3": "reflection",
            "4": "visual_summary"
        }

        content_type = content_map.get(option, "desconhecido")

        save_execution(
            student_profile=student_profile,
            topic=topic,
            content_type=content_type,
            output=result
        )

    else:
        print("\n[1] Ver histórico completo")
        print("[2] Filtrar por aluno")
        print("[3] Filtrar por tema")

        sub_option = input("\nOpção: ")

        if sub_option == "1":
            history = get_full_history()

        elif sub_option == "2":
            history = get_history_by_student(student_profile['name'])

        elif sub_option == "3":
            history = get_history_by_topic(topic)

        else:
            print("Opção inválida.")
            return

        if not history:
            print("\nNenhum registro encontrado.")
            return

        print("\n=== HISTÓRICO ===\n")
        for record in history:
            print(f"Data: {record['timestamp']}")
            print(f"Aluno: {record['student']}")
            print(f"Tema: {record['topic']}")
            print(f"Tipo: {record['content_type']}")
            print(f"Fonte: {record['source']}")
            print("-" * 40)



if __name__ == "__main__":
    main()