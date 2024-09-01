## 🌐 [English Version of README](README_EN.md)

# Sistema de Geração de Certificados

Um projeto desenvolvido com Django e SQLite para controle de eventos e geração de certificados. Este sistema é ideal para eventos onde a emissão de certificados para participantes é necessária.

## 🔨 Funcionalidades do Projeto

- **Controle de Eventos**: Gerenciamento de eventos com informações detalhadas.
- **Geração de Certificados**: Criação e armazenamento de certificados personalizados em formato PNG.
- **Busca de Certificados**: Funcionalidade para procurar certificados por e-mail.
- **Visualização de Certificados**: Exibição de certificados gerados para os participantes e administradores.

### Exemplo Visual do Projeto

![image](https://github.com/user-attachments/assets/d5aa7568-f98d-45a3-959f-ffc44087cadd)
![image](https://github.com/user-attachments/assets/3e143541-ac6e-4567-b73e-bceec462256f)
![image](https://github.com/user-attachments/assets/7e08598f-3e47-4c42-b1d0-8775449cea66)
![image](https://github.com/user-attachments/assets/1aaa8d21-9200-4888-84e4-074deb938832)

## ✔️ Técnicas e Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido e seguro.
- **SQLite**: Banco de dados leve para armazenamento de dados.
- **Python**: Linguagem de programação utilizada no backend.
- **Pillow**: Biblioteca para manipulação de imagens e geração de certificados.

### Funcionalidades e Descrições

- **Criação de Certificados**: Modelo e view para gerar certificados com informações do evento e participante.
- **Exibição de Certificados**: Interface para visualização e download dos certificados gerados.
- **Busca de Certificados**: Formulário para procurar certificados pelo e-mail do participante.
- **Gerenciamento de Eventos**: Páginas para gerenciar eventos e visualizar participantes.

## 📂 Estrutura dos Arquivos

- **cliente/**: Código relacionado ao módulo cliente.
- **eventos/**: Código relacionado ao módulo eventos.
- **media/**: Arquivos de mídia, como imagens e certificados.
- **templates/**: Templates HTML utilizados pelo projeto.
- **type_event/**: Código relacionado ao tipo de eventos.
- **usuarios/**: Código relacionado ao módulo de usuários.
- **.gitignore**: Arquivo para ignorar arquivos e diretórios no Git.
- **LICENSE**: Arquivo de licença do projeto.
- **README.md**: Este arquivo com a documentação do projeto.
- **db.sqlite3**: Banco de dados SQLite.
- **manage.py**: Script de gerenciamento do Django.
- **requirements.txt**: Lista de dependências do projeto.

## 🛠️ Abrir e Rodar o Projeto

### Pré-requisitos

- Python 3.x instalado na máquina
- Django instalado (veja `requirements.txt` para as dependências)

### Comandos Básicos

- `pip install -r requirements.txt` -> Instala as dependências do projeto.
- `venv\Scripts\Activate` -> Ativa o ambiente virtual.
- `python manage.py makemigrations` -> Cria arquivos de migração com base nas alterações nos modelos do Django.
- `python manage.py migrate` -> Aplica as migrações pendentes ao banco de dados.
- `python manage.py runserver` -> Inicia o servidor de desenvolvimento do Django em http://localhost:8000/.

## Recursos Adicionais

- [Versão em Inglês do README](README_EN.md)

## PSW 6.0
[PSW 6.0](https://grizzly-amaranthus-f6a.notion.site/PSW-6-0-4926964e82e843e4b95a00f5107c40b8)

## Notion All Classes
[Notion All Classes](https://grizzly-amaranthus-f6a.notion.site/PSW-e33ff4be6f624a87bc1e8574ba435e8d)
