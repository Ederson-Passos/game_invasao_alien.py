# Explorando a Arte da Programação com Python: Desenvolvendo um Jogo

![Badge em desenvolvimento](https://img.shields.io/badge/Status-Em%20desenvolvimento-dark) ![Badge linguagem Python](https://img.shields.io/badge/linguagem-Python-orange
) ![Habilidade POO](https://img.shields.io/badge/habilidade-POO-blue) ![Biblioteca Pygame](https://img.shields.io/badge/biblioteca-Pygame-8A2BE2)

# Índice
* [Introdução](#introdução)
* [Objetivos do projeto](#objetivos-do-projeto)
* [O jogo](#o-jogo)
* [Etapas do projeto](#etapas-do-projeto)
* [Conclusão](#conclusão)
* [Referências bibliográficas](#referências-bibliográficas)

___
# Introdução
Compartilho com você um projeto que visa mergulhar no mundo da programação enquanto nos divertimos com a criação de um jogo em Python usando a biblioteca Pygame. Meu nome é Éderson Passos, sou professor de Matemática e estudante de Ciência da Computação. Meu interesse pela interseção entre raciocínio, design, criatividade e arte me levou a embarcar nessa jornada, e estou empolgado em compartilhar com vocês os detalhes deste projeto e o que aprendi ao longo de sua elaboração.
___
# Objetivos do projeto
O objetivo principal da criação deste projeto foi aprender, desenvolver e praticar os princípios fundamentais da programação orientada a objetos, servindo de instrumentos a linguagem Python e a biblioteca Pygame para a criação de um ambiente gráfico interativo, ou de forma mais simples, a criação de um jogo. Nessa jornada pude explorar conceitos como: classes, herança, polimorfismo, encapsulamento e abstração. Estes princípios da OOP permitiram a estruturação sólida do jogo, bem como a organização clara do código. Também usei de forma ostensiva a criação de funções (programação funcional) para a organização do cógigo de forma eficiente, possibilitando a sua reutilização. Acima de tudo, o alvo era refinar a lógica de programação através do desenvolvimento de um jogo completo.
___
# O jogo
Consiste em um jogo de tiros em 2D (duas dimensões, estilo arcade), composto por uma nave que deve eliminar outras naves alienígenas, isto com um grau crescente de dificuldade conforme o jogador progredir de fase. A biblioteca Pygame foi utilizada para criar os gráficos e administrar as interações do usuário, via teclado e mouse, com os elementos visuais.

___
# Etapas do projeto
1. `Aprendizado dos fundamentos da linguagem Python:` diferentes tipos de dados; armazenamento através de variáveis, listas, dicionários e tuplas; utilização de laços de repetição e os condicionais if, elif e else; tratamento de inputs do usuário; criação de funções para reutilização e organização do código (funções locais e funções lambda); documentação e depuração (refatoração) do código; tratatamento de erros; criação de testes simples; consulta e utilização da documentação da linguagem.

![Imagens dos livros utilizados para estudo.](https://github.com/Ederson-Passos/game_invasao_alien.py/assets/145729066/d8b63a17-7e48-4da6-952a-2b16bfb2cf35)
*<center>Foto: Os livros utilizados no projeto.</center>*

2. `Configuração inicial:` preparação do ambiente de desenvolvimento com Python e Pygame, configuração da janela do jogo e loop principal, criação dos módulos principais: "Configurações" e "Funções do jogo", com a criação de suas respectivas funções locais `__init__(self)`.

3. `Programação orientada a objetos:` criação de classes para representar a nave, a frota de alienígenas, os projéteis, o placar de pontuação, níveis, recordes, botão "play", entre outros. Utilização dos princípios de herança e polimorfismo para organizar e otimizar o código, tratando adequadamente diferentes elementos do jogo.

4. `Lógica do jogo:` desenvolvimento de funções para gerenciamento do movimento dos personagens, - tanto da nave quanto da frota de alienígenas -, implementação de funções para detecção de colisões, contagem de pontos, recordes e níveis, com consequente aumento no grau de dificuldade.

![Animação do jogo em desenvolvimento.](https://github.com/Ederson-Passos/game_invasao_alien.py/assets/145729066/07362b7c-c7d0-44b1-96ab-bd556ffd5649)
*<center>Foto: Animação do jogo em execução em uma de suas versões de desenvolvimento.</center>*

5. `Estilo e design:` utilizamos para os personagens imagens de livre uso da internet, realizando seus tratamentos e adaptações para inserção e utilização no projeto (remoção de fundo, redimensionamento, mudança de cor, conversão de formato).
___
# Conclusão
Este projeto foi uma grande oportunidade de aplicar os conceitos de programação que estudei e aprendi. Ele desafiou-me a pensar criativamente e a resolver problemas, isto enquanto construía um jogo divertido. Apesar de ser no estilo "arcade", pude verificar com admiração a quantidade de saberes que são necessários para a criação de um simples jogo. À medida que bugs, erros de lógica e/ou de sintaxe, desafios e problemas novos iam surgindo, mais pesquisas eram necessárias, mais estudos e consultas a sites e repositórios, isso ao longo de horas que comporam alguns meses de dedicação. Assim, pude constatar que:

1. Programar e estudar Ciência da Computação é muito mais do que conhecer e saber mexer em computadores. Nas palavras do cientista da computação holandês Edsger W. Dijkstra: *"Ciência da computação não é a ciência dos computadores, assim como a astronomia não é a ciência dos telescópios."*
2. O projeto permanecerá em desenvolvimento, dado caberem várias melhorias, como frotas e projéteis diferentes, uma nave "alfa" para ser derrotada, adicionar efeitos sonoros.
3. Programar é uma forma de arte, como pintar um quadro, compor uma música, demonstrar um teorema ou confeccionar um móvel de madeira com as próprias mãos; logo, é algo desafiador, mas extremamente gratificante.
___
# Referências Bibliográficas
* *Curso intensivo de Python, uma introdução prática e baseada em projetos à programação*, Eric Matthes, 2016, Novatec Editora;
* *Python Fluente*, Luciano Ramalho, 2015, Novatec Editora;
* *Pense em Python*, Allen B. Downey, 2016, Novatec Editora.
