# 📚 Sistema Educacional Inteligente

Plataforma educativa que gera conteúdo personalizado para alunos de diferentes perfis usando técnicas avançadas de engenharia de prompt com a API do Google Gemini.

Desenvolvido como solução para o **Desafio Técnico de Estágio em IA e Engenharia de Prompt**.

---

## 🎯 Funcionalidades

- Seleção de perfil de aluno com dados de idade, nível e estilo de aprendizado
- Geração de 4 tipos de conteúdo educativo personalizado:
  - **Explicação Conceitual** — com estrutura didática e profundidade adaptada ao nível
  - **Exemplos Práticos** — contextualizados para faixa etária e estilo de aprendizado
  - **Perguntas de Reflexão** — que estimulam pensamento crítico
  - **Resumo Visual** — mapa mental em ASCII ou diagrama hierárquico
- Sistema de **cache** para evitar chamadas desnecessárias à API
- **Histórico** de execuções salvo em JSON com timestamp
- Interface web com **Streamlit** e interface de linha de comando (**CLI**)

---

## 🧠 Técnicas de Engenharia de Prompt Utilizadas

| Técnica | Aplicação |
|---|---|
| **Persona Prompting** | O modelo assume o papel de "especialista em ensino adaptativo e didática personalizada" |
| **Context Setting** | Perfil completo do aluno (nome, idade, nível, estilo) é injetado em cada prompt |
| **Chain-of-Thought** | Instruções de formato obrigatório guiam o modelo a estruturar a resposta progressivamente |
| **Output Formatting** | Formato Markdown detalhado com seções obrigatórias é especificado em cada prompt |
| **Adaptive Prompting** | As instruções mudam dinamicamente de acordo com o nível, idade e estilo de aprendizado do aluno |

> Para mais detalhes, consulte o arquivo [`PROMPT_ENGINEERING_NOTES.md`](./PROMPT_ENGINEERING_NOTES.md).

---

## 🗂️ Estrutura do Projeto

```
📦 projeto/
├── app.py                      # Interface web com Streamlit
├── main.py                     # Interface CLI
├── content_generator.py        # Orquestra a geração dos 4 tipos de conteúdo
├── prompt_engine.py            # Constrói prompts dinâmicos por perfil
├── llm_client.py               # Comunicação com a API do Google Gemini
├── config.py                   # Configurações e chaves de API
├── storage.py                  # Cache, histórico e persistência em JSON
├── students.json               # Perfis dos alunos cadastrados
├── requirements.txt            # Dependências do projeto
├── .env.example                # Exemplo de variáveis de ambiente
├── .gitignore
├── PROMPT_ENGINEERING_NOTES.md
├── outputs/
│   ├── cache.json              # Cache de respostas geradas
│   └── history.json            # Histórico de execuções
└── samples/
    ├── sample1.json
    ├── sample2.json
    ├── sample3.json
    └── sample4.json
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.9+
- Conta e chave de API no [Google AI Studio](https://aistudio.google.com/)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```bash
cp .env.example .env
```

Edite o `.env` e insira sua chave:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ **Nunca suba o arquivo `.env` para o repositório.** Ele já está listado no `.gitignore`.

### 4. Execute a aplicação

**Interface Web (Streamlit):**
```bash
streamlit run app.py
```

**Interface CLI:**
```bash
python main.py
```

---

## 👤 Perfis de Alunos Disponíveis

| Nome | Idade | Nível | Estilo de Aprendizado |
|---|---|---|---|
| Mirella | 19 | Avançado | Visual |
| Marçal | 23 | Intermediário | Leitura-Escrita |
| Diego | 16 | Iniciante | Auditivo |
| Gabriel | 25 | Intermediário | Cinestésico |

---

## 🔄 Sistema de Cache

O cache é salvo em `outputs/cache.json`. A chave é gerada a partir de:

```
{nome_aluno}_{topico}_{tipo_conteudo}
```

Se já existir uma resposta para a mesma combinação, ela é retornada diretamente do cache, sem nova chamada à API.

---

## 📦 Dependências

```
google-genai
python-dotenv
streamlit
```

