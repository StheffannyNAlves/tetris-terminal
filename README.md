# 🧱 TETRIS TERMINAL — Powered by Python + Curses
Jogo Tetris em Python com interface em terminal usando Curses e NumPy. Em refatoração para PyGame.
🎮 Tetris Terminal (versão curses) – Stheffanny N. Alves

> 🚧 **Este projeto está em processo de refatoração para se tornar um app modular com interface gráfica em `pygame`.**  
> O código atual representa a **versão funcional em terminal**, feita como projeto acadêmico na disciplina MI-Algoritmos, por meio da Metodologia PBL(Problem-Based Learning ou Aprendizagem Baseada em Problemas).



🧩 Sobre o Projeto

Esse Tetris foi desenvolvido com foco em:

    Jogabilidade fluida com Super Rotation System (SRS) e wall kicks

    Peça bomba 💣 que explode áreas inteiras do tabuleiro

    Sistema de combos, níveis dinâmicos e pontuação estratégica

    Totalmente jogável via interface textual (modo terminal) usando a biblioteca curses

🚀 Funcionalidades

✅ 7 peças clássicas do Tetris
✅ Peça especial Bomba com explosão em área
✅ Detecção de colisão e remoção de linhas
✅ Sistema de combo com tempo limite
✅ Progressão de dificuldade com aumento de velocidade
✅ Menu inicial, opções de dificuldade e mapeamento de controles
✅ Pontuação por tipo de peça, combo e nível
✅ Configuração por menu (WASD ou Setas)




---

🧠 Tecnologias utilizadas

- Python 3.10+  
- NumPy  
- Curses (modo texto)  
- [Planejado] PyGame (GUI futura)  

---
🧪 Requisitos

- Python 3.10+
- Sistema compatível com `curses`
  - ✅ Linux/macOS: roda nativamente
  - ⚠️ Windows: usar [Windows Terminal](https://aka.ms/terminal) + [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)


🕹️ Controles

| Ação             | Tecla WASD | Tecla Setas |
| ---------------- | ---------- | ----------- |
| Mover Esquerda   | `A`        | `←`         |
| Mover Direita    | `D`        | `→`         |
| Mover Para Baixo | `S`        | `↓`         |
| Rotacionar Peça  | `W`        | `↑`         |
| Pausar/Reiniciar | `P`        | `P`         |
| Sair             | `Q`        | `Q`         |


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
   python3 tetris.py
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

![Tetris Gameplay](imagens/gameplay.gif)


> *
---

🔮 Futuras Expansões

Adicionar efeitos sonoros (playsound ou pygame.mixer)

Porta gráfica com pygame

Ranking local/salvamento de pontuação

Modo multiplayer local

Versão para web com WebAssembly ou Flask

---

 🧑‍💻 Autora

**Stheffanny N. Alves**
Stheffanny Nascimento Alves
🎓 Estudante de Engenharia de Computação — UEFS
🔐 Foco em Cibersegurança, Programação e Engenharia de Software
🖤 Apaixonada por tecnologia e desenvolvimento de jogos
📫 stheffannyalvesnascimento@gmail.com
🔗 GitHub

---

📄 Licença

Projeto sob a licença MIT.

    Sinta-se livre pra usar, modificar e compartilhar😎💣

---

⚠️ Aviso Final

Esse repositório representa **uma fase inicial** de um projeto maior. Se você quer ver a evolução para interface gráfica e modularização avançada, **acompanhe a branch `dev`** ou aguarde novas atualizações.


