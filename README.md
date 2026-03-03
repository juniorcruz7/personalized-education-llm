# Sistema Adaptativo com LLM

Projeto pessoal focado na construção de um sistema adaptativo baseado em Modelos de Linguagem de Grande Escala (LLMs).

O objetivo é explorar como modelos de linguagem podem ajustar dinamicamente suas respostas com base em padrões de interação, contexto e configuração modular de modelos.

O projeto é estruturado desde o início com foco em organização, escalabilidade e boas práticas de engenharia.

---

## 🚀 Visão Geral

Este sistema foi projetado para:

- Gerar respostas adaptativas utilizando LLMs
- Permitir troca de modelo sem alterar o código
- Manter separação clara entre configuração e lógica
- Suportar evolução para arquitetura mais robusta (memória, avaliação, roteamento de modelos)

A estrutura foi pensada para evoluir de experimento para aplicação escalável.

---

## 🧠 Configuração Atual do Modelo

Atualmente, o sistema está configurado para testes com:


MODEL_NAME=gemma-3-1b-it


Esse modelo leve permite iteração rápida e validação de arquitetura.

A troca para modelos mais avançados pode ser feita apenas alterando variáveis de ambiente, sem necessidade de refatoração.

---

## 🏗 Princípios de Arquitetura

- Configuração baseada em variáveis de ambiente
- Abstração do modelo de linguagem
- Separação entre lógica e infraestrutura
- Estrutura de projeto escalável
- Gerenciamento seguro de chaves de API
- Ambiente reprodutível

---

## 🛠 Tecnologias Utilizadas

- Python
- API Google Gemini
- Ambiente virtual (`venv`)
- Gerenciamento de variáveis de ambiente
- Estrutura modular para integração com LLM

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/juniorcruz7/personalized-education-llm.git
cd SEU_REPOSITORIO
2️⃣ Criar ambiente virtual
python -m venv .venv

Ativar:

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Configurar variáveis de ambiente

Criar um arquivo .env na raiz do projeto:

GEMINI_API_KEY=sua_chave_aqui
MODEL_NAME=gemma-3-1b-it

⚠️ O arquivo .env não deve ser versionado.
Utilize o .env.example como referência.

🔁 Alterando o Modelo

Para utilizar outro modelo, basta modificar:

MODEL_NAME=gemini-1.5-flash

Sem necessidade de alterar o código da aplicação.

📁 Estrutura do Projeto
project-root/
│
├── .venv/              # Ambiente virtual (ignorado)
├── .env                # Variáveis locais (ignorado)
├── .env.example        # Exemplo de configuração
├── .gitignore
├── requirements.txt
└── src/                # Código-fonte
🔐 Boas Práticas Aplicadas

Chaves de API isoladas via variáveis de ambiente

Arquivos sensíveis ignorados pelo Git

Histórico limpo (sem versionamento de ambiente virtual)

Estrutura preparada para expansão

🎯 Próximos Passos

 Evoluir para modelo de maior capacidade

 Implementar camada de memória adaptativa

 Criar mecanismo de avaliação de respostas

 Implementar roteamento entre múltiplos modelos

 Disponibilizar como API

 Containerização com Docker

📌 Filosofia do Projeto

Este projeto busca aplicar princípios reais de engenharia em sistemas baseados em LLM:

Clareza arquitetural

Modularidade

Reprodutibilidade

Preparação para produção

Evolução incremental

Trata-se de uma base experimental com potencial de expansão para aplicações mais robustas.

👤 Autor

Desenvolvido por Júnior Cruz.
