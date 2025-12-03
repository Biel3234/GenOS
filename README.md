# GenOS - Sistema de Gestão de Ordens de Serviço

**GenOS** é um sistema web moderno e intuitivo para gerenciar ordens de serviço em oficinas de motocicletas. Permite criar, listar, visualizar, pesquisar e deletar ordens de serviço, além de gerar PDFs automatizados.

---

## 🎯 Funcionalidades

- ✅ **Autenticação de usuários** — Login seguro com validação de credenciais
- ✅ **CRUD completo de Ordens de Serviço** — Criar, listar, visualizar e deletar
- ✅ **Geração de PDFs** — Baixar ordens em formato PDF com layout profissional
- ✅ **Paginação** — Listagem com até 10 ordens por página
- ✅ **Busca** — Campo de pesquisa rápida nas ordens
- ✅ **Design responsivo** — Paleta de cores: laranja, cinza claro e preto
- ✅ **Confirmação de deleção** — Página de confirmação antes de remover ordem
- ✅ **Mensagens de erro** — Avisos claros (usuário não encontrado, etc.)

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3 (custom design)
- **Banco de Dados:** SQLite
- **PDF:** WeasyPrint 66.0
- **Servidor:** Gunicorn 23.0.0
- **Containerização:** Docker & Docker Compose

---

## 📋 Requisitos

- Python 3.8+
- Docker & Docker Compose

---

## ⚙️ Instalação e Setup

### 1. Clone o repositório

```bash
git clone https://github.com/Biel3234/GenOS.git
cd GenOS
```

### 2. Crie um ambiente virtual (opcional mas recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações do banco de dados

```bash
python manage.py migrate
```

### 5. Crie um super usuário (admin)

```bash
python manage.py createsuperuser
```

Siga as instruções para definir:
- Username (ex.: `admin`)
- Email (ex.: `admin@example.com`)
- Senha

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse a aplicação em: **http://127.0.0.1:8000/**

---

## 🐳 Usando Docker

### Build da imagem

```bash
docker build -t genos .
```

### Execute com Docker Compose

```bash
docker compose up
```

A aplicação estará disponível em: **http://localhost:8000/**

---

## 📖 Como Usar

### 1. **Login**

- Acesse `/login/`
- Digite seu username e senha
- Se as credenciais forem inválidas, você verá a página "Usuário não encontrado"

### 2. **Home**

- Página inicial com atalhos para:
  - Criar nova Ordem de Serviço
  - Listar todas as ordens

### 3. **Listar Ordens**

- Exibe tabela com:
  - **ID** — Identificador único
  - **Cliente / Moto** — Nome do cliente e moto
  - **Data** — Data e hora de criação
  - **Ações** — Botões: PDF, Ver, Deletar

- **Pesquisar:** Use a barra de busca no canto superior direito para filtrar ordens (integração com backend)
- **Paginação:** Navegue entre páginas usando os botões na base da tabela

### 4. **Criar Ordem de Serviço**

- Acesse `/criar/` ou clique no botão "Criar OS"
- Preencha o formulário com:
  - Nome do cliente
  - Telefone
  - Modelo da moto
  - Placa da moto
  - Problema relatado
  - Serviço executado
  - Mecânico responsável
  - Valor total

- Clique em "Criar Ordem de Serviço"
- O atendente responsável é registrado automaticamente como o usuário logado

### 5. **Visualizar Ordem**

- Na listagem, clique em "Ver" para abrir a ordem em detalhes
- Exibe um layout profissional com todos os dados

### 6. **Gerar PDF**

- Na listagem, clique em "PDF" para baixar a ordem em PDF
- Abre em nova aba com layout formatado e pronto para impressão

### 7. **Deletar Ordem**

- Na listagem, clique em "Deletar"
- Você será levado a uma página de **confirmação**
- Clique em "Sim, deletar" para confirmar a remoção
- A ordem será removida do banco de dados

### 8. **Logout**

- Clique em "Sair" no menu superior
- Você será redirecionado para a página de login

---

## 🎨 Design e Paleta de Cores

| Cor | Uso |
|-----|-----|
| **Laranja (#ff7a00)** | Botões primários, logo, hover |
| **Cinza claro (#f3f4f6)** | Fundo da página |
| **Preto (#000000)** | Cabeçalho, texto, border |
| **Cinza médio (#6b7280)** | Texto secundário/muted |

---

## 📁 Estrutura do Projeto

```
GenOS/
├── app/                    # App Django principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css   # Estilos globais (responsive)
│   │   └── os/
│   │       └── logo.png    # Logo da aplicação
│   ├── templates/
│   │   ├── base.html       # Template base (herança)
│   │   ├── home.html       # Página inicial
│   │   ├── create_os.html  # Formulário de criação
│   │   ├── list_os.html    # Listagem com paginação e busca
│   │   ├── login.html      # Página de login
│   │   ├── os_pdf.html     # Layout do PDF
│   │   ├── confirmar_delete_os.html
│   │   ├── usuario_nao_existe.html
│   │   └── usuario_ja_existe.html
│   ├── forms.py            # Formulários Django
│   ├── models.py           # Modelos (OrdemServico, User)
│   ├── views.py            # Views (lógica)
│   ├── urls.py             # Rotas
│   ├── admin.py            # Configuração admin
│   └── apps.py
├── setup/                  # Configuração do projeto Django
│   ├── settings.py         # Configurações
│   ├── urls.py             # URLs principais
│   ├── wsgi.py
│   └── asgi.py
├── db.sqlite3              # Banco de dados (desenvolvimento)
├── manage.py               # CLI Django
├── requirements.txt        # Dependências Python
├── Dockerfile              # Configuração Docker
├── docker-compose.yml      # Orquestração Docker
└── README.md               # Este arquivo
```

---

## 🔧 Variáveis de Ambiente (Produção)

Para usar em produção, crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-super-longa
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://user:password@localhost/genos
```

---

## 📝 Modelos de Dados

### OrdemServico

```python
cliente: CharField (max_length=70)
telefone: CharField (max_length=20)
moto: CharField (max_length=50)
placa: CharField (max_length=10)
problema_relatado: TextField (max_length=500)
servico_executado: TextField (max_length=500)
mecanico_responsavel: CharField (max_length=30)
atendente_responsavel: ForeignKey(User)
valor_total: DecimalField
data: DateTimeField (auto_now_add=True)
```

---

## 🚀 Rotas (URLs)

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/login/` | GET, POST | Autenticação |
| `/logout/` | GET | Deslogar usuário |
| `/listar/` | GET | Lista ordens (paginada) |
| `/criar/` | GET, POST | Criar nova ordem |
| `/detalhar/<id>/` | GET | Visualizar ordem |
| `/atualizar/<id>/` | GET, POST | Atualizar ordem |
| `/deletar/<id>/` | GET, POST | Deletar ordem (com confirmação) |
| `/pdf/<id>/` | GET | Download PDF da ordem |

---

## 🔐 Segurança

- ✅ **CSRF Token** — Proteção contra CSRF em todos os formulários
- ✅ **Login Required** — Todas as views (exceto login) requerem autenticação
- ✅ **Senha hasheada** — Usando o sistema padrão do Django
- ✅ **Validação de entrada** — Formulários validados no backend

---

## 🎓 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT — veja o arquivo LICENSE para detalhes.

---

## 👤 Autor

**Biel3234** — GitHub: [@Biel3234](https://github.com/Biel3234)

---

## 💬 Suporte

Se encontrar problemas, abra uma [issue](https://github.com/Biel3234/GenOS/issues) no repositório.

---

## 📦 Próximas Melhorias

- [ ] Autenticação por email/2FA
- [ ] Dashboard com gráficos (ordens por mês, faturamento)
- [ ] Exportar relatórios em Excel/CSV
- [ ] Sistema de permissões (admin, mecânico, atendente)
- [ ] Notificações por email
- [ ] API REST para mobile
- [ ] Dark mode

---

**Versão:** 1.0.0 | **Data:** Dezembro de 2025
