# 🧠 Prompt Engineering Notes

## 1. Objetivo

Este projeto foi desenvolvido com foco em engenharia de prompt estruturada e adaptativa, visando geração de conteúdo educacional personalizado com base no perfil do aluno.

A engenharia de prompt foi tratada como parte central da arquitetura do sistema, e não como simples instrução textual.

---

## 2. Estratégia Geral

A construção dos prompts combina múltiplas camadas de adaptação:

- Persona Prompting
- Context Setting explícito
- Adaptação por nível cognitivo
- Adaptação por faixa etária
- Adaptação por estilo de aprendizagem
- Controle rígido de formatação
- Separação por tipo de conteúdo

Cada tipo de conteúdo possui um prompt independente, reduzindo interferência entre objetivos.

---

## 3. Persona Prompting

Todos os prompts partem da seguinte instrução base:

> "Você é um especialista em ensino adaptativo e didática personalizada."

Objetivos:

- Induzir comportamento pedagógico
- Reduzir respostas excessivamente técnicas
- Estimular adaptação natural ao perfil do aluno
- Manter consistência de tom

---

## 4. Context Setting Estruturado

O perfil do aluno é explicitamente incluído no prompt:

- Nome
- Idade
- Nível (Iniciante, Intermediário, Avançado)
- Estilo de aprendizagem

Isso reduz ambiguidade e melhora coerência adaptativa.

---

## 5. Adaptação Multicamadas

### 5.1 Por Idade
Controla:
- Vocabulário
- Complexidade sintática
- Tipo de exemplos

### 5.2 Por Nível Cognitivo
Define profundidade conceitual:

- Iniciante → linguagem simples, menos jargões
- Intermediário → termos técnicos com explicação
- Avançado → maior densidade conceitual

### 5.3 Por Estilo de Aprendizagem

Visual → organização estruturada e metáforas visuais  
Auditivo → linguagem fluida e reflexiva  
Leitura-escrita → organização textual formal e estruturada  
Cinestésico → exemplos práticos e aplicações reais  

---

## 6. Separação por Tipo de Conteúdo

O sistema possui quatro geradores independentes:

- Explicação conceitual
- Exemplos práticos
- Perguntas de reflexão
- Resumo visual

Cada um contém:

- Regras próprias
- Estrutura obrigatória
- Controle específico de profundidade

Essa separação evita respostas híbridas ou inconsistentes.

---

## 7. Controle Estrutural de Saída

Os prompts utilizam:

- Estruturas obrigatórias em Markdown
- Títulos fixos
- Seções pré-definidas
- Regras explícitas de formatação

Exemplo:

## 📌 Introdução  
## 🧠 Desenvolvimento  
## ✅ Conclusão  

Objetivos:

- Previsibilidade
- Consistência
- Comparabilidade entre execuções

---

## 8. Restrições Comportamentais

Foram incluídas instruções negativas como:

- Não mencionar que é uma IA
- Não expor raciocínio interno
- Não sair do escopo
- Não responder perguntas quando solicitado apenas gerar perguntas

Essas restrições reduzem ruído e aumentam controle.

---

## 9. Sistema de Cache e Histórico

O sistema implementa cache por:

(Aluno + Tema + Tipo de Conteúdo)

Benefícios:

- Redução de chamadas à API
- Reprodutibilidade
- Comparação entre versões de prompt
- Auditoria de geração (API vs Cache)

---

## 10. Estratégia de Experimentação

A arquitetura permite testar variações mantendo:

- Mesmo perfil
- Mesmo tópico
- Mesmo tipo de conteúdo

Isso viabiliza experimentação controlada de engenharia de prompt.

---

## 11. Limitações Identificadas

- Modelos menores apresentam menor aderência a formatação rígida.
- A qualidade depende da correta classificação do perfil.
- Não há avaliação automática de qualidade semântica.
- ASCII estruturado exige maior capacidade do modelo.

---

## 12. Decisões Arquiteturais Relevantes

- Separação entre construção de prompt e chamada ao modelo.
- Modularização por tipo de conteúdo.
- Controle explícito de profundidade.
- Uso de variáveis de ambiente para troca de modelo.
- Persistência em JSON para rastreabilidade.

---

## Conclusão

A engenharia de prompt foi tratada como componente arquitetural estratégico, buscando:

- Personalização real
- Controle estrutural
- Previsibilidade
- Modularidade
- Capacidade de experimentação
