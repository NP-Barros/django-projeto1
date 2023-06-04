# 🍲 Sabores da Terceira Idade

Descubra os segredos culinários guardados a sete chaves pelos nossos avós com a plataforma Sabores da Terceira Idade. Compartilhe suas receitas favoritas e experimente novos sabores em um ambiente amigável e fácil de usar. Conecte-se com outros amantes da culinária caseira e explore um mundo de possibilidades culinárias. Junte-se à nossa comunidade e ajude a promover a inclusão digital de idosos. Venha cozinhar conosco!

## 🎯 Objetivo
O objetivo desta plataforma é fornecer um espaço para que idosos possam compartilhar suas receitas e conhecimentos culinários com outras pessoas. Além disso, a plataforma também tem como objetivo ajudar aqueles que desejam aprender novas receitas e experimentar novos sabores. A plataforma também busca promover a inclusão digital de idosos, oferecendo uma interface amigável e fácil de usar.



<div valign="top"><br>

## 💻 Tecnologias Utilizadas


**Python<img align="center" alt="Python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
Django <img align="center" alt="HTML" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" /> 
MySQL <img align="center" alt="HTML" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg" />
HTML <img align="center" alt="HTML" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
CSS <img align="center" alt="CSS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">
JavaScript <img align="center" alt="Js" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">
Git <img align="center" alt="git" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
GitHub <img align="center" alt="github" height="35" width="35" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" />**
<div>          

## 📋 Funcionalidades
1. Inserir usuário :raising_hand_woman:
2. Excluir conta :wastebasket:
3. Inserir receitas (com opção de não publicá-las):pencil:
4. Publicar receitas inseridas :rocket:
5. Favoritar receitas :heart:
6. Dashboard :bar_chart:
7. Comentar em receitas :speech_balloon:
8. Avaliar receitas :thumbsup:

## 👥 Público-alvo

Plataforma voltada para idosos que desejam compartilhar suas receitas e para aqueles que desejam aprender novas receitas.

## 📖 Como utilizar

1. Acesse o site da plataforma.   :link::globe_with_meridians:
2. Clique em "Criar conta" e preencha o formulário com suas informações.   :new:  :memo:
3. Faça login com suas credenciais. :key:  :bust_in_silhouette:
4. Navegue pelas receitas disponíveis utilizando a barra de pesquisa ou os filtros de categoria. :mag: :open_file_folder:
5. Para adicionar suas próprias receitas, clique em "Adicionar receita" e preencha o formulário com as informações da sua receita.  :heavy_plus_sign:  :memo:
6. Você pode optar por publicar ou não a sua receita imediatamente. :outbox_tray:  :rocket:
7. Para comentar ou avaliar uma receita, clique na receita desejada e utilize os campos de comentário e avaliação.:speech_balloon: :thumbsup:
8. Você pode acessar o seu dashboard para ver suas receitas publicadas e favoritas. :heart:


## Ambiente de Desenvolvimento
 
O projeto foi desenvolvido utilizando as seguintes tecnologias:

- Linguagem de Programação: Python 3.11
- Framework: Django 4.1.5
- Banco de Dados: MySQL (É utilizada a ferramenta do Django para gerenciar o banco de dados)

## Instalação e Execução
Para executar o projeto em seu ambiente local, siga as instruções abaixo:

1. Certifique-se de ter o Python 3.11 instalado. Você pode fazer o download da versão mais recente do Python em [link para o site oficial do Python].

2. Clone este repositório para o seu computador ou faça o download do código-fonte.

3. No terminal, navegue até o diretório raiz do projeto.

4. Crie um ambiente virtual executando o comando:
 ```
python -m venv myenv
```

5. Ative o ambiente virtual:
- No Linux/macOS:
```
source myenv/bin/activate
```
- No Windows:
```
myenv\Scripts\activate
```

6. Instale as dependências do projeto executando o comando:
```
pip install -r requirements.txt
```

7. Execute as migrações do banco de dados:
```
python manage.py migrate
```

8. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

9. Acesse o projeto em seu navegador através do link [http://localhost:8000](http://localhost:8000).

## Requisitos de Sistema
 Para executar o projeto, é necessário ter os seguintes requisitos de sistema:

- Python 3.11
- Django 4.1.5
- MySQL (versão específica, se necessário)
- [Outros requisitos específicos do projeto, como versões de bibliotecas adicionais]

Certifique-se de atender a esses requisitos antes de tentar executar o projeto.

  
## Banco de Dados

O projeto utiliza o Django, um framework web em Python, que oferece um poderoso conjunto de ferramentas para o gerenciamento de banco de dados. O banco de dados utilizado é o MySQL.

O Django fornece uma camada de abstração de banco de dados, permitindo que você defina seus modelos de dados usando classes Python. O Django cuida da criação e manipulação do banco de dados, facilitando o desenvolvimento de aplicativos com persistência de dados.

Para configurar a conexão com o banco de dados MySQL, você precisa atualizar as configurações no arquivo `settings.py`. Localize a seção `DATABASES` e modifique as configurações de acordo com as suas necessidades. Por exemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
 ```
Certifique-se de ter o MySQL instalado em seu sistema e as devidas credenciais para acesso ao banco de dados.

Depois de configurar corretamente as informações de conexão, o Django cuidará da criação e atualização do banco de dados automaticamente ao executar as migrações.

Para executar as migrações e criar as tabelas do banco de dados, utilize o seguinte comando no terminal:
```
 python manage.py migrate
 ```
O Django também oferece um poderoso ORM (Object-Relational Mapping), que permite que você manipule o banco de dados usando objetos Python em vez de escrever consultas SQL manualmente. Isso facilita o desenvolvimento e a manutenção do código relacionado ao banco de dados.

Para obter mais informações sobre o uso do Django com bancos de dados, consulte a documentação oficial do Django.

  
## Contribuição

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.

2. Crie um branch para a sua nova feature:
```
git checkout -b minha-nova-feature
```

3. Faça as alterações desejadas e faça commit delas:
```
git commit -m "Descrição das alterações"
```

4. Envie as alterações para o seu repositório fork:
```
git push origin minha-nova-feature
```

5. Abra um pull request neste repositório, descrevendo suas alterações.

Agradecemos antecipadamente por suas contribuições!

## Práticas de Código Limpo

Durante o desenvolvimento deste projeto, foram aplicadas práticas de código limpo, incluindo:

- Nomenclatura significativa de variáveis, funções e classes.
- Organização e estruturação adequadas do código.
- Comentários relevantes para auxiliar na compreensão do código.
- Utilização de padrões e convenções da linguagem Python.

## Testes Automatizados

Foram implementados testes automatizados baseados em TDD (Test Driven Development) utilizando as seguintes bibliotecas:

- Pytest
- Selenium

Os testes podem ser encontrados no diretório de cada App dentro da aplicação.

Para executar os testes, utilize o seguinte comando:
```
python manage.py test
```

## Padrão de Projeto de Software

O padrão de projeto de software utilizado neste projeto é o Model-View-Controller (MVC).

O MVC é um padrão de arquitetura de software que separa a lógica de negócios (Model), a interface do usuário (View) e o fluxo de controle (Controller).

No projeto, a camada Model é responsável pela interação com o banco de dados MySQL, definindo os modelos e suas relações. A camada View trata da apresentação dos dados ao usuário, utilizando os templates do Django para renderização. E a camada Controller gerencia as requisições do usuário, processando-as e atualizando o Model ou a View conforme necessário.

O uso do padrão MVC proporciona uma separação clara de responsabilidades e facilita a manutenção e evolução do código, permitindo que as partes do sistema sejam modificadas independentemente umas das outras.
 
 
 # :fire::meat_on_bone: Divirta-se explorando as deliciosas receitas caseiras! :stew:
