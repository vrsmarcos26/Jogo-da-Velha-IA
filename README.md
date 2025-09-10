# Tic-Tac-Toe with AI (Minimax Algorithm)

[cite_start]Este projeto é uma implementação do clássico Jogo da Velha, onde você pode desafiar uma Inteligência Artificial que nunca perde[cite: 66]. [cite_start]A IA foi desenvolvida utilizando o algoritmo **Minimax**, uma técnica fundamental em teoria dos jogos e IA[cite: 1].

Este trabalho foi desenvolvido como uma atividade acadêmica para aplicar conceitos de busca em árvore e algoritmos de decisão.

[cite_start]*Resultado de uma partida onde o jogador humano (O) perde para a IA (X)[cite: 66, 76].*

## 🧠 O Conceito Chave: Algoritmo Minimax

O Minimax é um algoritmo de decisão usado em jogos de dois jogadores com informações perfeitas e soma zero (o que um jogador ganha, o outro perde). O nome "Minimax" vem do seu objetivo:
* [cite_start]O jogador **MAX** (nossa IA) tenta **maximizar** sua pontuação[cite: 140, 141].
* [cite_start]O jogador **MIN** (o oponente) tenta **minimizar** a pontuação da IA[cite: 143, 144].

Funciona assim:
1.  [cite_start]**Árvore de Jogadas**: O algoritmo cria uma árvore com todas as jogadas possíveis a partir do estado atual do jogo[cite: 125, 127].
2.  [cite_start]**Pontuação (Score)**: A cada estado final do jogo (vitória, derrota ou empate), é atribuída uma pontuação[cite: 37, 50]. Por exemplo:
    * [cite_start]**Pontuação positiva** se a IA ganha[cite: 40, 41].
    * [cite_start]**Pontuação negativa** se o jogador humano ganha[cite: 42, 43].
    * [cite_start]**Zero** se for empate[cite: 44, 45].
    * [cite_start]O algoritmo também considera o número de jogadas, para que a IA prefira vitórias mais rápidas[cite: 39, 41].
3.  [cite_start]**Busca em Profundidade**: O algoritmo explora a árvore de jogadas até o final de cada ramo (vitória, derrota ou empate) para calcular as pontuações[cite: 47, 133]. Em seguida, ele propaga os resultados de volta na árvore, permitindo que o jogador MAX e MIN façam suas escolhas ótimas.

![Diagrama do algoritmo Minimax](https://i.imgur.com/sZV4z4E.png)

## 🛠️ Estrutura do Código

O código em Python está estruturado em funções principais que trabalham em conjunto para criar o jogo e a IA:

-   [cite_start]`get_game_status(board)`: Verifica o estado atual do tabuleiro para ver se o jogo terminou[cite: 2, 3]. [cite_start]Ela checa todas as linhas [cite: 7, 10][cite_start], colunas [cite: 13, 15] [cite_start]e diagonais [cite: 18, 19] [cite_start]em busca de um vencedor ou de um empate[cite: 24, 25].

-   [cite_start]`get_possible_moves(board, player)`: Recebe um tabuleiro e um jogador, e retorna uma lista com todos os tabuleiros possíveis após a próxima jogada[cite: 26, 33].

-   [cite_start]`get_score(winner, n_moves)`: Calcula a pontuação de um jogo finalizado, favorecendo vitórias rápidas para a IA e derrotas mais lentas[cite: 37, 39].

-   `mini_max(board, player, n_moves)`: O coração da IA. [cite_start]Implementa o algoritmo Minimax de forma recursiva [cite: 47] [cite_start]para encontrar a melhor jogada possível a partir de um estado do tabuleiro[cite: 53, 54, 63].

-   `class TicTacToeAI`: Integra toda a lógica do jogo com uma interface gráfica interativa criada com `ipywidgets`, permitindo que o usuário jogue clicando nos botões.

## 🚀 Como Executar o Projeto

Este projeto foi desenvolvido para ser executado em um ambiente de notebook, como **Google Colab** ou **Jupyter Notebook**.

### Pré-requisitos

Você precisa ter as seguintes bibliotecas Python instaladas:
-   `numpy`
-   `ipywidgets`

Você pode instalá-las usando pip:
```bash
pip install numpy ipywidgets
```

### Passo a Passo

1.  **Clone ou baixe este repositório** para a sua máquina.
2.  **Abra o arquivo `jogo_da_velha_IA.ipynb`** no Google Colab ou em um Jupyter Notebook local.
3.  **Execute todas as células** do notebook.
4.  A interface do jogo aparecerá e você poderá começar a jogar contra a IA!

Para iniciar uma partida onde o jogador humano começa:
```python
# O jogador humano começa
game = TicTacToeAI(ai_starts=False)
game.start()
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
