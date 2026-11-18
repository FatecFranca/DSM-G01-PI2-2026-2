# 🏋️ GYMtech — Sistema Integrado de Gestão Fitness

![Projeto](https://img.shields.io/badge/Projeto-Interdisciplinar-blue?style=for-the-badge)
![FATEC Franca](https://img.shields.io/badge/FATEC-Franca-005A9C?style=for-the-badge)
![Semestre](https://img.shields.io/badge/Período-2026%2F2-informational?style=for-the-badge)
![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)
![Banco de Dados](https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

Repositório do **GYMtech**, projeto interdisciplinar desenvolvido no curso de **Desenvolvimento de Software Multiplataforma (DSM)** da **Faculdade de Tecnologia de Franca — FATEC Franca**, durante o **segundo semestre de 2026 (2026/2)**.

Este repositório reúne as aplicações **Frontend** e **Backend**, além dos documentos acadêmicos e artefatos de análise e modelagem produzidos ao longo do projeto.

---

## 🎯 Objetivo do Projeto

O GYMtech tem como objetivo desenvolver uma plataforma para centralizar e facilitar a gestão das atividades de uma academia, aproximando alunos, profissionais e responsáveis pela administração.

A proposta é reduzir a dispersão de informações relacionadas aos treinos, avaliações físicas e aulas, oferecendo um ambiente no qual os usuários possam consultar e gerenciar essas atividades de acordo com seus perfis de acesso.

A plataforma busca:

- Permitir que alunos consultem seus treinos, histórico e evolução;
- Possibilitar o agendamento de aulas e avaliações físicas;
- Apoiar profissionais na criação e atualização de treinos;
- Facilitar o registro e o acompanhamento das avaliações físicas;
- Auxiliar a academia na administração de usuários, profissionais, aulas e atividades;
- Centralizar informações e tornar a comunicação e a organização da rotina da academia mais práticas.

---

## 👥 Perfis de Usuário

O sistema considera diferentes perfis, com permissões e funcionalidades específicas:

| Perfil | Responsabilidades e funcionalidades |
|---|---|
| **Academia / Administrador** | Gerenciar informações da academia, usuários, profissionais, alunos, exercícios e aulas. |
| **Profissional** | Gerenciar alunos vinculados, elaborar e atualizar treinos, acompanhar agendas e registrar avaliações físicas. |
| **Aluno** | Consultar treinos, acompanhar o progresso e o histórico, além de agendar aulas e avaliações físicas. |

---

## ✨ Principais Funcionalidades

### 🏢 Gestão da academia
- Cadastro e gerenciamento de academias;
- Gerenciamento de usuários e perfis de acesso;
- Cadastro e organização de aulas;
- Gerenciamento do catálogo de exercícios;
- Acompanhamento de reservas e agendamentos.

### 🧑‍🏫 Área do profissional
- Visualização dos alunos vinculados;
- Criação e atualização de treinos individualizados;
- Organização da agenda;
- Consulta de notificações;
- Registro de avaliações físicas;
- Acompanhamento do histórico e da evolução dos alunos.

### 🏃 Área do aluno
- Visualização do dashboard e do treino do dia;
- Consulta dos treinos e do histórico;
- Acompanhamento do progresso;
- Consulta e agendamento de aulas;
- Agendamento de avaliações físicas;
- Acesso ao perfil e às notificações.

---

## 🧰 Tecnologias Utilizadas

### Frontend
- **React 19** — construção da interface;
- **Vite 8** — ferramenta de desenvolvimento e build;
- **React Router 7** — gerenciamento de rotas;
- **Axios** — comunicação HTTP com a API;
- **Lucide React** — ícones;
- **JavaScript e CSS** — lógica e estilização da aplicação.

### Backend
- **Python** — linguagem de programação;
- **FastAPI** — desenvolvimento da API REST;
- **SQLAlchemy** — mapeamento objeto-relacional (ORM);
- **Pydantic** — validação e estruturação de dados;
- **MySQL** — banco de dados relacional;
- **PyMySQL** — conexão com o MySQL;
- **Uvicorn** — servidor ASGI;
- **APScheduler** — execução de tarefas agendadas;
- **PyJWT e bcrypt** — recursos relacionados à autenticação e segurança;
- **Jinja2** — templates de e-mail.

---

## 📁 Estrutura do Repositório

A organização proposta para este repositório é:

```text
GYMtech/
│
├── frontend/                   # Aplicação web (React + Vite)
│   ├── public/                 # Arquivos públicos e ícones
│   ├── src/
│   │   ├── assets/             # Imagens e recursos visuais
│   │   ├── componets/          # Componentes reutilizáveis
│   │   ├── hooks/              # Hooks personalizados
│   │   ├── pages/              # Páginas e telas por funcionalidade
│   │   ├── routes/             # Rotas e proteção de acesso
│   │   ├── services/           # Comunicação com a API e autenticação
│   │   └── utils/              # Funções auxiliares
│   ├── package.json
│   └── vite.config.js
│
├── backend/                    # API (Python + FastAPI)
│   ├── app/
│   │   ├── core/               # Configurações, segurança e recursos centrais
│   │   ├── models/             # Modelos das entidades do banco
│   │   ├── routes/             # Endpoints da API
│   │   ├── schemas/            # Schemas de entrada e saída
│   │   └── services/           # Regras de negócio e serviços
│   ├── sql/                    # Scripts SQL do banco de dados
│   ├── .env.example            # Exemplo de variáveis de ambiente
│   └── requirements.txt        # Dependências Python
│
├── documentacao/               # Documentos e diagramas do projeto
│   ├── BPMN.jpeg
│   ├── DiagramaConceitualV3.drawio.png
│   ├── DiagramaLogicoV3.drawio.png
│   ├── ModelagemConceitualV2.drawio.png
│   ├── ModelagemLogicaV2.drawio.png
│   ├── Modelagem_Conceitual_GYMtech_v1.drawio.png
│   ├── Modelagem_Logica_GYMtech.drawio.png
│   ├── Modelo DSM V5 - versao 2.pdf
│   └── Modelo DSM V5 - versao 3.pdf
│
└── README.md
```

> A árvore acima representa a organização esperada dos diretórios no repositório. Os nomes das pastas podem ser ajustados na publicação, mantendo a separação entre frontend, backend e documentação.

### 📚 Sobre a pasta `documentacao/`

A pasta reúne os materiais utilizados para especificar, representar e registrar o projeto:

| Arquivo | Conteúdo |
|---|---|
| `BPMN.jpeg` | Representação do fluxo do processo e das atividades dos usuários e do sistema. |
| `DiagramaConceitualV3.drawio.png` | Exportação da versão 3 do diagrama conceitual de dados. |
| `DiagramaLogicoV3.drawio.png` | Exportação da versão 3 do diagrama lógico de dados. |
| `ModelagemConceitualV2.drawio.png` | Exportação de uma versão anterior da modelagem conceitual. |
| `ModelagemLogicaV2.drawio.png` | Exportação de uma versão anterior da modelagem lógica. |
| `Modelagem_Conceitual_GYMtech_v1.drawio.png` | Registro da primeira versão identificada da modelagem conceitual do GYMtech. |
| `Modelagem_Logica_GYMtech.drawio.png` | Registro da modelagem lógica do banco de dados do GYMtech. |
| `Modelo DSM V5 - versao 2.pdf` | Documento acadêmico do projeto, com apresentação da proposta, requisitos, regras de negócio, casos de uso, modelagem e protótipo. |
| `Modelo DSM V5 - versao 3.pdf` | Outra versão do documento acadêmico, mantida para registrar a evolução da documentação. |

Os arquivos de imagem são exportações dos diagramas. Quando houver necessidade de editar a modelagem, recomenda-se manter também os arquivos-fonte editáveis do diagrams.net/Draw.io no repositório.

---

## 🚀 Como Executar o Projeto

Para executar a aplicação localmente, é necessário configurar o banco de dados, iniciar o Backend e, em seguida, iniciar o Frontend.

### Pré-requisitos

- [Git](https://git-scm.com/);
- [Python](https://www.python.org/) compatível com as dependências do Backend;
- [Node.js e npm](https://nodejs.org/);
- [MySQL](https://www.mysql.com/) — versão 8.0 ou superior.

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd GYMtech
```

### 2. Configurar o banco de dados

1. Inicie o servidor MySQL.
2. Acesse o MySQL por uma ferramenta de sua preferência.
3. Execute o script localizado em `backend/sql/gymtech.sql`.
4. Confira se o banco `gymtech` e suas tabelas foram criados.

**Atenção:** o script SQL atual contém `DROP DATABASE IF EXISTS gymtech` antes da criação do banco. Portanto, sua execução pode apagar um banco `gymtech` já existente. Faça backup dos dados antes de executá-lo.

### 3. Configurar e iniciar o Backend

Entre na pasta do Backend:

```bash
cd backend
```

Crie e ative um ambiente virtual Python.

**Windows:**

```bash
py -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `.env` a partir do exemplo:

**Windows (Prompt de Comando):**

```bash
copy .env.example .env
```

**Linux / macOS / Git Bash:**

```bash
cp .env.example .env
```

Edite o `.env` e informe os dados de conexão com o MySQL, a chave secreta e as configurações necessárias para os serviços de e-mail. As principais variáveis estão documentadas no próprio `.env.example`.

Para iniciar a API:

```bash
uvicorn app.main:app --reload
```

Por padrão, a API ficará disponível em:

- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

### 4. Configurar e iniciar o Frontend

Abra outro terminal e entre na pasta do Frontend:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

A aplicação utiliza a variável `VITE_API_URL` para definir o endereço da API. Caso necessário, crie um arquivo `.env` na pasta `frontend`:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

O Vite exibirá no terminal o endereço local para acessar a aplicação (normalmente http://localhost:5173).

---

## 🔐 Segurança e Configurações

- Não publique o arquivo `.env` com credenciais reais.
- Utilize o `.env.example` como referência para configurar o ambiente.
- Mantenha a `SECRET_KEY` privada e utilize uma chave forte.
- Não envie senhas de e-mail, tokens ou dados pessoais para o repositório.
- O Backend utiliza autenticação por token e controle de acesso conforme o perfil do usuário.
- O Frontend envia o token de autenticação nas requisições à API.

---

## 🧪 Documentação e Testes da API

Com o Backend em execução, utilize o **Swagger UI** em http://127.0.0.1:8000/docs para consultar os endpoints disponíveis e realizar testes das requisições.

A documentação interativa permite visualizar parâmetros, modelos de dados, respostas e testar as operações disponibilizadas pela API.

---

## 🎓 Contexto Acadêmico

**Projeto:** GYMtech — Sistema Integrado de Gestão Fitness  
**Instituição:** Faculdade de Tecnologia de Franca — FATEC Franca  
**Curso:** Desenvolvimento de Software Multiplataforma (DSM)  
**Período:** 2º semestre de 2026 (2026/2)  
**Natureza:** Projeto Interdisciplinar

O repositório centraliza os artefatos de software e a documentação acadêmica relacionados ao desenvolvimento do projeto.

---

## 👩‍💻 Equipe

- Maria Fernanda Campos Cintra
- Maria Julia Campos Cintra
- Milena Clara Custódio

---

## 📌 Observações

- Os diretórios `frontend/`, `backend/` e `documentacao/` mantêm separadas as partes da aplicação e os materiais acadêmicos.
- O conteúdo deste repositório pode evoluir conforme as etapas de desenvolvimento e as entregas do Projeto Interdisciplinar.
- Consulte os documentos da pasta `documentacao/` para obter mais detalhes sobre requisitos, processos, modelagem e protótipo.

---
