# Sistema Adaptativo com LLM

Sistema adaptativo baseado em Modelos de Linguagem de Grande Escala (LLMs), desenvolvido com foco em organização arquitetural, engenharia de prompt e boas práticas de desenvolvimento.

O projeto explora como modelos de linguagem podem ajustar dinamicamente suas respostas com base em perfil de usuário, contexto e configuração modular.

## 🌐 Acesse a Aplicação

A aplicação pode ser acessada em:

🔗 https://adaptive-prompt-education.streamlit.app/

---

## 🚀 Visão Geral

O sistema permite:

- Geração de conteúdo adaptado ao perfil do estudante
- Troca de modelo via variável de ambiente
- Persistência de histórico em JSON
- Controle estruturado de saída via engenharia de prompt
- Arquitetura modular e escalável

---

## 🛠 Tecnologias Utilizadas

- Python
- Google Gemini API
- Streamlit (interface)
- Ambiente virtual (`venv`)
- JSON para persistência de dados

---

## 📁 Estrutura do Projeto

```

personalized-education-llm/
│
├── .venv/                        # Ambiente virtual (ignorado pelo Git)
├── .env                          # Variáveis locais (ignorado)
├── .env.example                  # Exemplo de configuração
├── .gitignore
├── requirements.txt
├── README.md
├── PROMPT_ENGINEERING_NOTES.md
│
├── samples/                      # Exemplos de saída JSON
│   ├── sample1.json
│   ├── sample2.json
│   └── sample3.json
│
├── outputs/                      # Arquivos gerados pelo sistema
│   ├── cache.json
│   └── history.json
│
├── students.json                 # Base de dados local
│
├── main.py                       # Execução via terminal
├── app.py                        # Interface Streamlit
├── config.py                     # Configurações do sistema
├── content_generator.py          # Lógica de geração
├── prompt_engine.py              # Construção dos prompts
├── llm_client.py                 # Comunicação com o modelo
└── storage.py                    # Persistência de dados

```

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/juniorcruz7/personalized-education-llm.git
cd personalized-education-llm
2️⃣ Criar ambiente virtual
python -m venv .venv

Ativar:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate
3️⃣ Instalar dependências
pip install -r requirements.txt
⚙️ Configuração do Ambiente

Criar um arquivo .env na raiz:

GEMINI_API_KEY=sua_chave_aqui
MODEL_NAME=gemma-3-1b-it

O arquivo .env não deve ser versionado.
Utilize .env.example como referência.

▶️ Como Executar

Execução via terminal:

python main.py

Ou execução da interface:

streamlit run app.py
📂 Exemplos de Saída

A pasta /samples contém exemplos reais de respostas geradas pelo sistema em formato JSON, conforme exigido no edital.

Esses arquivos demonstram:

Estrutura de resposta

Adaptação por perfil

Persistência em formato estruturado

🧠 Engenharia de Prompt

As estratégias de engenharia de prompt utilizadas no projeto estão documentadas detalhadamente em:

PROMPT_ENGINEERING_NOTES.md

O documento descreve:

Estruturação de prompts

Controle de formato de saída

Estratégias de restrição

Adaptação por nível de usuário

Problemas encontrados e soluções adotadas

🔐 Boas Práticas Aplicadas

Variáveis sensíveis isoladas em .env

Arquivos críticos ignorados via .gitignore

Separação clara de responsabilidades

Persistência estruturada em JSON

Arquitetura preparada para evolução

🎯 Conclusão

O projeto demonstra aplicação prática de:

Engenharia de Prompt

Arquitetura modular em Python

Integração com LLM

Controle estruturado de saída

Persistência e organização de dados

👤 Autor

Desenvolvido por Júnior Cruz.


