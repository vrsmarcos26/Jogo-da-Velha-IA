<div align="center">
  <h1>
    Jogo da Velha com Inteligência Artificial
  </h1>
</div>

<p align="center">
  <img alt="Linguagem Principal" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Licença" src="https://img.shields.io/github/license/SEU-USUARIO/SEU-REPOSITORIO?style=for-the-badge&color=blue">
</p>

<p align="center">
  Uma implementação do clássico Jogo da Velha em Python, onde o jogador enfrenta uma IA imbatível baseada no algoritmo Minimax.
</p>

<p align="center">
  <a href="#-objetivos-de-aprendizagem">Objetivos</a> •
  <a href="#-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-rodar-o-projeto">Como Rodar</a> •
  <a href="#-demonstração">Demonstração</a> •
  <a href="#-licença">Licença</a>
</p>

---

### 🎯 Objetivos de Aprendizagem

Este laboratório foi projetado para demonstrar na prática:
-   A implementação do algoritmo de decisão **Minimax**.
-   O conceito de **busca em árvore (depth-first)** para explorar estados de um jogo.
-   A criação de uma interface de usuário interativa em um notebook usando **`ipywidgets`**.
-   A manipulação de matrizes para representar o tabuleiro do jogo com **`numpy`**.

---

### 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando o ecossistema Python em um ambiente de notebook interativo.

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"></a>
  <a href="#"><img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy"></a>
</p>

---

### ⚙️ Como Rodar o Projeto

Para executar o jogo, o ambiente ideal é o **Google Colab** ou um **Jupyter Notebook** local.

#### 1. Pré-requisitos
-   Python 3.x instalado.
-   Gerenciador de pacotes `pip`.

#### 2. Clone o Repositório
```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
```

#### 3. Instale as Dependências
```bash
pip install numpy ipywidgets
```

#### 4. Inicie o Jogo
Abra o arquivo `.ipynb` no Google Colab ou Jupyter e execute as células. A interface do jogo será renderizada e você poderá iniciar a partida.

```python
# Célula final para iniciar o jogo
game = TicTacToeAI(ai_starts=False)
game.start()
```

---

### 🎬 Demonstração

A interface permite que o jogador (círculo) clique em uma posição vazia. A IA (X) responde imediatamente com a jogada ótima, calculada pelo algoritmo Minimax. Neste exemplo, a IA vence a partida.

<summary><strong>💡 Análise Técnica do Algoritmo (Write-up)</strong></summary>
<br>

A inteligência do jogo reside no algoritmo **Minimax**, que é implementado através de algumas funções principais:

1.  **`get_game_status(board)`**: A cada jogada, esta função verifica se o jogo terminou. Ela analisa as somas das linhas, colunas e diagonais para encontrar um vencedor ou determinar se houve um empate.

2.  **`get_possible_moves(board, player)`**: Gera uma lista de todos os "tabuleiros futuros" possíveis a partir do estado atual.

3.  **`get_score(winner, n_moves)`**: Atribui uma pontuação a um estado final do jogo. Uma vitória da IA recebe uma pontuação positiva, uma derrota recebe uma pontuação negativa, e um empate é zero. A pontuação também favorece vitórias mais rápidas.

4.  **`mini_max(board, player)`**: É a função recursiva central. Ela simula todas as sequências de jogadas possíveis, assumindo que a IA (jogador MAX) sempre tentará maximizar a pontuação, enquanto o oponente (jogador MIN) sempre tentará minimizá-la. Ao final, ela retorna a jogada que leva ao melhor resultado possível para a IA.


---

### 📝 Licença

Este projeto está sob a licença MIT.

<hr>

<p align="center">
  Desenvolvido por <b>Marcos Vinícius Rocha Silva</b>
</p>
