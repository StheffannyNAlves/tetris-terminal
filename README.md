# tetris-terminal
Jogo Tetris em Python com interface em terminal usando Curses e NumPy. Em refatoração para PyGame.
🎮 Tetris Terminal (versão curses) – Stheffanny N. Alves

> 🚧 **Este projeto está em processo de refatoração para se tornar um app modular com interface gráfica em `pygame`.**  
> O código atual representa a **versão funcional em terminal**, feita como desafio técnico durante processo simulado da Blizzard Entertainment.



📜 Descrição

Esta é uma implementação do clássico **Tetris**, utilizando **Python**, **NumPy** e **Curses** para rodar inteiramente no terminal. O projeto foca em:

- Representação matricial das peças  
- Sistema de rotação avançado (SRS + Wall Kicks)  
- Interface textual responsiva  
- Sistema de pontuação com combos  
- Inclusão de uma peça especial: **Bomba**, que explode áreas do tabuleiro  

---

🧠 Tecnologias utilizadas

- Python 3.10+  
- NumPy  
- Curses (modo texto)  
- [Planejado] PyGame (GUI futura)  

---

🕹️ Controles

| Tecla      | Ação                            |
|------------|--------------------------------|
| `W` / ↑    | Rotacionar peça (anti-horário) |
| `A` / ←    | Mover para esquerda             |
| `D` / →    | Mover para direita              |
| `S` / ↓    | Mover para baixo (queda suave) |
| `P`        | Pausar / Retomar jogo           |
| `Q`        | Sair                           |

---

💣 Peça Bomba

- Representada como peça `B`  
- Ao colidir, explode uma área 3x3 ao redor  
- Remove peças fixas e concede pontos extras  
- Adiciona estratégia ao gameplay  

---

🚀 Como rodar

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/tetris-terminal.git
   cd tetris-terminal
``

2. (Recomendado) Crie um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Rode o jogo:

   ```bash
   python3 main.py
   ```

⚠️ No Ubuntu, certifique-se que o terminal suporta `curses`. O jogo roda diretamente no terminal.

---

 🛠️ Em desenvolvimento

* [x] Versão funcional em curses
* [ ] Refatoração completa em arquitetura modular
* [ ] Transição para interface gráfica usando PyGame
* [ ] Exportação para executável standalone
* [ ] Versão Web com PyScript (em estudo)

---

 🧠 Professor: Notou um "glitch" nas cores?

Identificado: após fixação das peças, `curses.color_pair()` tentava renderizar valores inválidos.
**Corrigido na versão modular em andamento.**

---

 📸 Screenshot

> *

---

 🧑‍💻 Autora

**Stheffanny N. Alves**
Estudante de Engenharia de Computação – UEFS
[stheffannyalvesnascimento@gmail.com](mailto:stheffannyalvesnascimento@gmail.com)

---

📄 Licença

MIT License

---

⚠️ Aviso Final

Esse repositório representa **uma fase inicial** de um projeto maior. Se você quer ver a evolução para interface gráfica e modularização avançada, **acompanhe a branch `dev`** ou aguarde novas atualizações.


