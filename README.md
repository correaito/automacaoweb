<h1 align="center"> Projeto Automação Web - Busca de Preços </h1>
<h4 align="center">Objetivo: treinar um projeto em que a gente tenha que usar automações web com Selenium para buscar as informações que precisamos.</h4>

![imagem](https://img.shields.io/badge/-Python-orange) ![imagem](https://img.shields.io/badge/-pywin32-black) ![imagem](https://img.shields.io/badge/-Pandas-brown) ![imagem](https://img.shields.io/badge/-Openpyxl-green) ![imagem](https://img.shields.io/badge/-Selenium-red)

<a id="tecnologias" class="anchor"></a>
### :rocket:  Tecnologias

------------
Esse projeto foi desenvolvido como um Projeto Pessoal, com as seguintes tecnologias:

- [Python](https://www.python.org/ "Python")
- [Pandas](https://pandas.pydata.org/ "Pandas")
- [Selenium](https://selenium-python.readthedocs.io/ "Selenium")
- [Pywin32](https://pypi.org/project/pywin32/ "Pywin32")

<a id="informacao-uso" class="anchor"></a>
### :information_source:  Como Usar
------------
Para executar este aplicativo, você precisará apenas clonar e abrir em seu navegador. 

Da sua linha de comando:

    # Clone este repositório
    $ git clone https://github.com/correaito/automacaoweb.git
    
    # Vá para o repositório
    $ cd automacao_processo
    
    # Instale as extensões
    $ pip install pandas
    $ pip install selenium
    $ pip install openpyxl
    $ pip install pywin32

Agora, para executar o script, dentro do PyCharm, abra o arquivo main.py, clique com o botão direito do mouse, e depois em "Run main.py", ou com <kbd>SHIFT</kbd> + <kbd>CTRL</kbd> + <kbd>F10</kbd>.

<a id="descricao" class="anchor"></a>
### :clipboard:  Descrição

- Imagina que você trabalha na área de compras de uma empresa e precisa fazer uma comparação de fornecedores para os seus insumos/produtos.

- Nessa hora, você vai constantemente buscar nos sites desses fornecedores os produtos disponíveis e o preço, afinal, cada um deles pode fazer promoção em momentos diferentes e com valores diferentes.

- Seu objetivo: descobrir o produto mais barato e atualizar isso em uma planilha.
- Caso o valor seja 20% (ou mais) abaixo do preço original, queremos também ser avisados por e-mail para poder agir rápido e aproveitar essa promoção.

- No nosso caso, vamos fazer com produtos comuns em sites como Amazon, Magazine Luiza e Lojas Americanas, mas a ideia é a mesma.

<a id="infoimportantes" class="anchor"></a>
### :mag_right:  O que temos disponiveis?

- Planilha de Produtos, com os nomes dos produtos e o link em cada loja, além do preço original cadastrado.

<a id="infoimportantes" class="anchor"></a>
### :pencil:  O que devemos fazer?

- Cadastrar na coluna Preço Atual o menor preço encontrado e na Coluna Local o nome do Local onde foi encontrado esse preço
- Enviar um e-mail para compras com a notificação do menor preço encontrado e o link de compra, caso o preço encontrado esteja com 20% ou mais de desconto em relação ao preço original. (Vou usar o e-mail correaito+compras@gmail.com. Use um e-mail seu para fazer os testes para ver se a mensagem está chegando)

<a id="infoimportantes" class="anchor"></a>
### :triangular_flag_on_post:  Informações Importantes

- Podemos colocar esse programa para rodar de 4 em 4 horas ou então todo dia as 10hrs da manhã. Podemos fazer isso via agendador de tarefas do Windows ou então deixar o código rodando em background com um time.sleep(tempo)
- Caso queira, você pode deixar o navegador sem aparecer ao término do seu código, para ficar mais sutil o seu programa

------------
Feito com ♥ por Alan Garmatter 👋 
