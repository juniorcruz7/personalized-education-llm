# 🧠 Prompt Engineering Notes

## 1. Objetivo

Este projeto trata engenharia de prompt como **componente arquitetural central**, não como simples instrução textual. O objetivo é gerar conteúdo educacional de alta qualidade, adaptado dinamicamente ao perfil de cada aluno, com controle rigoroso de estrutura e comportamento do modelo.

---

## 2. Estratégia Geral

A construção dos prompts combina múltiplas camadas de adaptação em um único sistema coeso:

```
Persona Prompting
      ↓
Context Setting (perfil do aluno)
      ↓
Adaptação Multicamadas (nível + idade + estilo)
      ↓
Instrução Específica por Tipo de Conteúdo
      ↓
Controle de Formatação + Restrições Comportamentais
```

Cada tipo de conteúdo possui um prompt **completamente independente**, evitando interferência entre objetivos distintos e permitindo experimentação controlada.

---

## 3. Persona Prompting

Todos os prompts iniciam com a seguinte instrução base:

> *"Você é um especialista em ensino adaptativo e didática personalizada. Seu objetivo é ensinar o tema de forma altamente personalizada."*

**Por que essa persona?**

Modelos de linguagem respondem melhor quando assumem um papel claro. A persona de especialista em ensino adaptativo:

- Induz comportamento pedagógico consistente
- Reduz respostas excessivamente técnicas ou genéricas
- Estimula adaptação natural ao perfil do aluno
- Mantém coerência de tom ao longo de toda a resposta

**Alternativas testadas e descartadas:**

| Persona | Problema identificado |
|---|---|
| "Professor universitário" | Respostas muito formais para alunos iniciantes |
| "Tutor amigável" | Pouca profundidade técnica para alunos avançados |
| Sem persona definida | Inconsistência de tom entre execuções |

---

## 4. Context Setting Estruturado

O perfil completo do aluno é injetado diretamente no prompt a cada chamada:

```
Nome: {name}
Idade: {age}
Nível de conhecimento: {level}
Estilo de aprendizagem: {learning_style}
```

**Impacto observado:** A inclusão explícita do perfil reduz ambiguidade e melhora significativamente a coerência da resposta. Sem esses dados, o modelo tende a gerar conteúdo genérico ignorando características individuais.

---

## 5. Adaptação Multicamadas

A adaptação ocorre em três dimensões independentes e combinadas:

### 5.1 Por Faixa Etária

Controla vocabulário, complexidade sintática e tipo de exemplos utilizados:

| Faixa | Instrução injetada |
|---|---|
| Até 13 anos | Situações do cotidiano infantil ou escolar; linguagem simples e direta |
| 14–18 anos | Situações de escola, tecnologia e redes sociais |
| 19+ anos | Situações profissionais, acadêmicas ou do cotidiano adulto |

### 5.2 Por Nível Cognitivo

Define a profundidade conceitual e o grau de tecnicidade da resposta:

| Nível | Instrução injetada |
|---|---|
| Iniciante | Linguagem simples, analogias, ausência de jargões complexos |
| Intermediário | Termos técnicos moderados com explicações de suporte |
| Avançado | Alta densidade conceitual, conexões entre ideias, detalhamento técnico |

### 5.3 Por Estilo de Aprendizagem (Modelo VARK)

Adapta a forma como a informação é apresentada:

| Estilo | Estratégia aplicada |
|---|---|
| Visual | Metáforas visuais, estrutura em esquemas, organização visual clara |
| Auditivo | Linguagem fluida e conversacional, perguntas reflexivas intercaladas |
| Leitura-Escrita | Definições formais, texto bem estruturado, termos conceituais precisos |
| Cinestésico | Exemplos práticos, aplicações no mundo real, situações concretas |

---

## 6. Separação por Tipo de Conteúdo

O sistema possui quatro geradores completamente independentes. Cada um define suas próprias regras, estrutura obrigatória e controle de profundidade:

### 6.1 Explicação Conceitual

**Técnica principal:** Chain-of-Thought implícito via estrutura obrigatória.

O prompt força uma progressão lógica:

```
## 📌 Introdução   → contextualização do tema
## 🧠 Desenvolvimento → conceitos em progressão crescente
## ✅ Conclusão     → síntese objetiva
```

Isso simula raciocínio encadeado sem expor o processo interno do modelo.

### 6.2 Exemplos Práticos

**Técnica principal:** Contextualização tripla (idade + nível + estilo).

As três dimensões de adaptação são combinadas, gerando exemplos altamente personalizados. A estrutura obrigatória é:

```
## 📘 Conceito Base     → ancoragem do tema
## 🔍 Exemplos Práticos → mínimo 3 exemplos em lista
## 🎯 Aplicação         → conexão com a aprendizagem
```

### 6.3 Perguntas de Reflexão

**Técnica principal:** Restrição comportamental explícita — o modelo é instruído a **não responder** as perguntas que gera.

A complexidade das perguntas é controlada pelo nível:

- Iniciante → curiosidade e compreensão básica
- Intermediário → análise e conexão com o cotidiano
- Avançado → hipóteses, consequências, comparação de cenários

### 6.4 Resumo Visual

**Técnica principal:** Controle rígido de formato com proibição de texto explicativo.

O formato varia conforme o estilo de aprendizagem:

- Visual → mapa mental em ASCII com setas e ramificações
- Outros → diagrama hierárquico em tópicos estruturados

> ⚠️ Esta é a função mais sensível ao modelo utilizado. Modelos menores tendem a descumprir a restrição de não usar texto explicativo.

---

## 7. Controle Estrutural de Saída (Output Formatting)

Todos os prompts especificam um **formato de resposta obrigatório** em Markdown, com seções e títulos fixos.

**Objetivos:**

- Previsibilidade entre execuções
- Comparabilidade entre versões de prompt
- Renderização consistente na interface Streamlit
- Facilidade de auditoria no histórico JSON

**Exemplo de instrução de formatação:**

```
FORMATO OBRIGATÓRIO (use Markdown):

## 📌 Introdução
## 🧠 Desenvolvimento
## ✅ Conclusão
```

---

## 8. Restrições Comportamentais (Negative Prompting)

Instruções negativas foram incluídas em todos os prompts para reduzir comportamentos indesejados:

| Restrição | Problema evitado |
|---|---|
| "Não mencione que é uma IA" | Quebra de imersão pedagógica |
| "Não exponha seu raciocínio interno" | Respostas com "thinking out loud" desnecessário |
| "Não saia do escopo do tema" | Divagações e respostas irrelevantes |
| "Não responda as perguntas" | Violação da proposta de reflexão (gerador de perguntas) |
| "Produza apenas o conteúdo final" | Preambles e metacomentários do modelo |

---

## 9. Sistema de Cache e Rastreabilidade

O cache é indexado pela combinação:

```
{nome_aluno}_{topico}_{tipo_conteudo}
```

Cada execução é registrada no histórico com o campo `source`, indicando se a resposta veio da API ou do cache. Isso permite:

- Auditoria completa do comportamento do sistema
- Comparação direta entre versões de prompt (mesma chave, prompts diferentes)
- Reprodutibilidade de experimentos
- Redução de custos com chamadas à API

---

## 10. Estratégia de Experimentação

A arquitetura foi projetada para facilitar testes controlados de engenharia de prompt. Para comparar duas versões de um prompt:

1. Altere a instrução em `content_generator.py` ou `prompt_engine.py`
2. Limpe a entrada correspondente no `cache.json`
3. Execute com o mesmo aluno, tópico e tipo de conteúdo
4. Compare os resultados no histórico (`history.json`) ou na interface

Isso mantém todas as variáveis constantes, isolando o impacto da mudança no prompt.

---

## 11. Limitações Identificadas

- **Qualidade dependente do perfil:** uma classificação incorreta de nível ou estilo gera conteúdo inadequado.
- **Sem avaliação semântica automática:** a qualidade do conteúdo é avaliada manualmente.
- **Resumos ASCII** exigem maior capacidade do modelo para serem bem estruturados.
- **Prompts longos** aumentam o custo por chamada e podem reduzir aderência em modelos de menor capacidade.

---

## 12. Decisões Arquiteturais Relevantes

| Decisão | Justificativa |
|---|---|
| Separação entre `prompt_engine.py` e `content_generator.py` | Isola construção do prompt da lógica de geração, facilitando manutenção e testes |
| Quatro geradores independentes | Evita interferência entre tipos de conteúdo e permite otimização individual |
| Variáveis de ambiente para modelo e chave | Permite troca de modelo sem alteração de código |
| Persistência em JSON | Rastreabilidade completa de todas as execuções |
| Cache por chave composta | Granularidade adequada para experimentação controlada |

---

## Conclusão

A engenharia de prompt neste projeto foi tratada como **componente arquitetural estratégico**. As principais contribuições técnicas foram:

- Personalização real por três dimensões independentes (nível, idade, estilo)
- Controle estrutural de saída com formato obrigatório
- Separação clara entre construção de prompt e execução
- Infraestrutura de rastreabilidade para experimentação controlada
- Uso combinado de persona prompting, context setting, output formatting e negative prompting

