# 🧩 Projeto Dashboard

Este é um projeto de **Dashboard** desenvolvido com **Django** para avaliação da matéria de **WEB1**.

---

Dashboard de Estatísticas
- Criar um painel administrativo com gráficos e cards de estatísticas.
- Usar JavaScript para gerar gráficos dinâmicos.
- Implementar um sistema de tabs ou navegação lateral.

---

## 🚀 Tecnologias Utilizadas

- Python
- Django
- HTML/CSS/JavaScript
- Chart.js
- Bootstrap

---

## ⚙️ Como Executar o Projeto

### 1. Passo Clone o repositório, instale o ambiente virtual e as dependências.

```bash
# Clone o repositório
git clone https://github.com/Arthurms02/prova_web1.git
cd prova_web1

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configure seu banco PostgreSQL no `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Execute migrações

```bash
python manage.py migrate
```
### 4. Carregue os dados no projeto

```bash
python manage.py loaddata fixtures/dados_iniciais.json
```

### 5. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```
