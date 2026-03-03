#Constrói prompts dinâmicos com base no perfil do aluno, tópico e versão escolhida.

def build_prompt(topic: str, student_profile: dict, instruction: str) -> str:
    name = student_profile["name"]
    age = student_profile["age"]
    level = student_profile["level"]
    learning_style = student_profile["learning_style"]

    #Adaptação por estilo de aprendizagem
    if learning_style == "visual":
        style_instruction = "Utilize metáforas visuais, descreva esquemas mentais e organize a informação de forma visualmente estruturada."
    elif learning_style == "leitura-escrita":
        style_instruction = "Utilize definições claras, explicações textuais bem organizadas e termos conceituais precisos."
    elif learning_style == "auditivo":
        style_instruction = "Use linguagem mais conversacional, exemplos explicativos e perguntas reflexivas ao longo da explicação."
    else:  #Cinestesico
        style_instruction = "Inclua exemplos práticos, aplicações no mundo real e situações concretas para facilitar a aprendizagem."

    prompt = f"""
    Você é um especialista em ensino adaptativo e didática personalizada.
    Seu objetivo é ensinar o tema "{topic}" de forma altamente personalizada.

    PERFIL DO ALUNO:
    Nome: {name}, idade: {age}, nível de conhecimento: {level}, estilo de aprendizagem: {learning_style}

    Adapte a explicação considerando:
    Faixa etária do aluno, profundidade adequada ao nível, estratégias compatíveis com o estilo de aprendizagem

    {style_instruction}

    INSTRUÇÕES ESPECÍFICAS DA TAREFA:
    {instruction}

    REGRAS IMPORTANTES:
    Não mencione que é uma IA. Não mostre seu raciocínio interno. Não saia do escopo do tema. Mantenha clareza e organização.

    Produza apenas o conteúdo final.
    """
    return prompt