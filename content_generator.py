# Orquestra a geração dos diferentes tipos de conteúdo usando prompt_engine e llm_client.

from storage import (get_cached_response, store_response_in_cache, add_to_history)
from prompt_engine import build_prompt
from llm_client import call_llm


def generate_explanation(topic: str, student_profile: dict) -> str:
    student_name = student_profile["name"]
    level = student_profile["level"]

    #Verifica cache antes de tudo
    cached = get_cached_response(student_name, topic, "Explicação")

    if cached:
        print("Resposta vinda do CACHE")
        add_to_history(student_name, topic, "Explicação", "cache", cached)
        return cached

    print("Gerando nova resposta via API...")

    #Ajuste de profundidade baseado no nível
    if level == "Iniciante":
        depth_instruction = "Use linguagem simples, evite termos técnicos complexos e utilize analogias."
    elif level == "Intermediário":
        depth_instruction = "Use linguagem técnica moderada e inclua explicações detalhadas."
    else:
        depth_instruction = "Use linguagem técnica aprofundada e inclua detalhes conceituais avançados."

    instruction = f"""
    Explique o tema de forma didática e organizada.
    {depth_instruction}
    Regras: Use apenas Markdown simples. Não use emojis fora dos títulos. Não mencione que é uma IA.

    FORMATO OBRIGATÓRIO (use Markdown):

    ## 📌 Introdução
    Apresente o tema de forma clara e contextualizada.

    ## 🧠 Desenvolvimento
    Explique progressivamente os principais conceitos.
    Use parágrafos curtos.
    Se necessário, utilize listas com "-".

    ## ✅ Conclusão
    Resuma os pontos principais de forma objetiva.
    """

    prompt = build_prompt(topic, student_profile, instruction)
    response = call_llm(prompt)

    store_response_in_cache(student_name, topic, "Explicação", response)

    add_to_history(student_name, topic, "Explicação", "api", response)

    return response


def generate_examples(topic: str, student_profile: dict) -> str:
    student_name = student_profile["name"]    
    age = student_profile["age"]
    level = student_profile["level"]
    learning_style = student_profile["learning_style"]

    #Verifica cache antes de tudo
    cached = get_cached_response(student_name, topic, "Exemplos")

    if cached:
        print("Resposta vinda do CACHE")
        add_to_history(student_name, topic, "Exemplos", "cache", cached)
        return cached

    print("Gerando nova resposta via API...")

    #Ajuste por faixa etária
    if age <= 13:
        context_instruction = "Use situações do cotidiano infantil ou escolar."
    elif age <= 18:
        context_instruction = "Use situações relacionadas à escola, tecnologia ou redes sociais."
    else:
        context_instruction = "Use situações profissionais, acadêmicas ou do cotidiano adulto."

    #Ajuste por nível
    if level == "Iniciante":
        depth_instruction = "Use exemplos simples e diretos."
    elif level == "Intermediário":
        depth_instruction = "Inclua exemplos com um pouco mais de complexidade."
    else:
        depth_instruction = "Inclua exemplos mais elaborados e conectados a contextos técnicos."

    #Ajuste por estilo de aprendizado
    if learning_style == "visual":
        style_instruction = "Descreva cenas ou situações que possam ser facilmente imaginadas visualmente."
    elif learning_style == "auditivo":
        style_instruction = "Inclua analogias que possam ser explicadas verbalmente."
    elif learning_style == "leitura-escrita":
        style_instruction = "Organize os exemplos em formato enumerado e estruturado."
    else:
        style_instruction = "Inclua exemplos que envolvam ações práticas ou experiências."

    instruction = f"""
    Forneça exemplos claros e variados sobre o tema.
    {context_instruction}
    {depth_instruction}
    {style_instruction}
    Regras: Use Markdown. Mantenha organização visual.

    FORMATO OBRIGATÓRIO (use Markdown):

    ## 📘 Conceito Base
    Explique brevemente o conceito central.

    ## 🔍 Exemplos Práticos
    Apresente pelo menos 3 exemplos organizados em lista:

    - Exemplo 1:
    - Exemplo 2:
    - Exemplo 3:

    ## 🎯 Aplicação
    Explique como esses exemplos ajudam na compreensão.
    """

    prompt = build_prompt(topic, student_profile, instruction)
    response = call_llm(prompt)

    store_response_in_cache(student_name, topic, "Exemplos", response)

    add_to_history(student_name, topic, "Exemplos", "api", response)

    return response


def generate_reflection_questions(topic: str, student_profile: dict) -> str:
    student_name = student_profile["name"]    
    level = student_profile["level"]
    age = student_profile["age"]

    #Verifica cache antes de tudo
    cached = get_cached_response(student_name, topic, "Reflexão")

    if cached:
        print("Resposta vinda do CACHE")
        add_to_history(student_name, topic, "Reflexão", "cache", cached)
        return cached

    print("Gerando nova resposta via API...")

    #Ajuste por nível cognitivo
    if level == "Iniciante":
        complexity_instruction = "Gere perguntas simples que estimulem curiosidade e compreensão básica do tema."

    elif level == "Intermediário":
        complexity_instruction = "Gere perguntas que incentivem análise e conexão entre o tema e situações do cotidiano."

    else:
        complexity_instruction = "Gere perguntas que estimulem pensamento crítico profundo, análise de consequências, comparação de cenários e formulação de hipóteses."

    #Ajuste leve por idade
    if age <= 13:
        age_instruction = "Use linguagem simples e direta."
    else:
        age_instruction = "Use linguagem adequada à maturidade do aluno."

    instruction = f"""
    Estimule pensamento crítico sobre o tema.
    {complexity_instruction}
    {age_instruction}
    Regras: Use Markdown.Não responda as perguntas.

    FORMATO OBRIGATÓRIO (use Markdown):

    ## 🌍 Contexto
    Apresente o tema sob uma perspectiva reflexiva.

    ## ❓ Perguntas para Reflexão
    Liste pelo menos 5 perguntas abertas usando "-".

    ## 🧭 Encerramento
    Incentive aprofundamento e análise pessoal.
    """

    prompt = build_prompt(topic, student_profile, instruction)
    response = call_llm(prompt)

    store_response_in_cache(student_name, topic, "Reflexão", response)

    add_to_history(student_name, topic, "Reflexão", "api", response)

    return response


def generate_visual_summary(topic: str, student_profile: dict) -> str:
    student_name = student_profile["name"]    
    learning_style = student_profile["learning_style"]
    level = student_profile["level"]

    #Verifica cache antes de tudo
    cached = get_cached_response(student_name, topic, "Resumo visual")

    if cached:
        print("Resposta vinda do CACHE")
        add_to_history(student_name, topic, "Resumo visual", "cache", cached)
        return cached

    print("Gerando nova resposta via API...")

    #Ajuste por nível
    if level == "Iniciante":
        depth_instruction = "Use poucos níveis hierárquicos e conceitos principais."
    elif level == "Intermediário":
        depth_instruction = "Inclua conceitos principais e subconceitos."
    else:
        depth_instruction = "Inclua estrutura detalhada com múltiplas conexões entre conceitos."

    if learning_style == "visual":
        format_instruction = "Crie um mapa mental em ASCII usando: Setas (→), ramificações, estrutura em árvore"

    else:
        format_instruction = "Crie um diagrama hierárquico estruturado em formato de tópicos."

    instruction = f"""
    Gere um resumo visual estruturado sobre o tema.

    Regras: 
    - É proibido o uso de textos explicativos. 
    - Não inclua exemplos, apenas estrutura visual organizada. - Use espaçamento adequado.

    {depth_instruction}
    {format_instruction}
    """
        
    prompt = build_prompt(topic, student_profile, instruction)
    response = call_llm(prompt)

    store_response_in_cache(student_name, topic, "Resumo visual", response)

    add_to_history(student_name, topic, "Resumo visual", "api", response)

    return response
