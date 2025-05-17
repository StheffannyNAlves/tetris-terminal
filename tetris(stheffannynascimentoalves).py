# Bibliotecas
import curses
import random
import time
import numpy as np 

# Inicialização das variáveis globais
altura = 20 # Altura do tabuleiro
largura = 10  # Largura do tabuleiro
velocidade_incremento = 0.02  # Incremento de velocidade
velocidade_minima = 0.1        # Velocidade mínima 
tempo_combo = 2                # Tempo limite para combos (em segundos)

# Pontuação por peça
pontuacao_pecas = {
    'I': 10,
    'O': 20,
    'T': 30,
    'S': 40,
    'Z': 50,
    'J': 60,
    'L': 70,
    'B': 100  # Peça bomba
}

# Definição das Peças
pecas = {
    'I': np.array([[1] ,[1], [1], [1]]),
    'O': np.array([[2, 2], [2, 2]]),
    'T': np.array([[0, 3, 0], [3, 3, 3]]),
    'S': np.array([[0, 4, 4], [4, 4, 0]]),
    'Z': np.array([[5, 5, 0], [0, 5, 5]]),
    'J': np.array([[6, 0, 0], [6, 6, 6]]),
    'L': np.array([[0, 0, 7], [7, 7, 7]]),
    'B': np.array([[8]])  # Peça bomba
}

# Definição das Cores
cores = {
    1: curses.COLOR_CYAN,
    2: curses.COLOR_YELLOW,
    3: curses.COLOR_MAGENTA,
    4: curses.COLOR_GREEN,
    5: curses.COLOR_MAGENTA,
    6: curses.COLOR_BLUE,
    7: curses.COLOR_WHITE,
    8: curses.COLOR_RED  # Cor para peça bomba
}

# Configurações padrões
configuracoes = {
    "dificuldade": "Fácil",  # Dificuldade padrão
    "controles": "WASD"      # Controle padrão
}

# Funções Auxiliares

def criar_peca():
    """Cria uma nova peça aleatória com orientação inicial."""
    tipo = random.choice(list(pecas.keys()))
    return {
        'tipo': tipo,
        'matriz': pecas[tipo].copy(),
        'rotacao': 0  # Orientação inicial da peça
    }


def rotacionar_peca(peca): # Rotaciona a peça 90 graus no sentido anti-horário.
    peca['matriz'] = np.rot90(peca['matriz'])
    peca['rotacao'] = (peca['rotacao'] + 1) % 4


def detectar_colisao(peca, x, y, tabuleiro): # Detecta colisão com as bordas ou com outras peças no tabuleiro.
    for i in range(peca['matriz'].shape[0]):
        for j in range(peca['matriz'].shape[1]):
            if peca['matriz'][i, j] != 0:
                novo_x = x + j
                novo_y = y + i
                if (
                    novo_x < 0
                    or novo_x >= largura
                    or novo_y >= altura
                ):
                    return True
                if novo_y >= 0 and tabuleiro[novo_y, novo_x] != 0:
                    return True
    return False

# Função que tenta rotacionar a peça com o "wall kicks"(Ajuste na posição da peça após ela ser rotacionada).
def tentar_rotacao(peca, x, y, tabuleiro): 
    matriz_original = peca['matriz'].copy() # Salva uma cópia da matriz da peça
    rotacao_original = peca['rotacao']
    rotacionar_peca(peca)  
    
    # Se houver colisão, a função tentar aplicar o "wall kicks". 
    # Se não, retorna a nova posição da peça.
    if not detectar_colisao(peca, x, y, tabuleiro):
        return x, y

    # Dicionário que define os ajuste de posição para cada tipo de peça
    wall_kicks = {
        'I': [
            [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)],  # Rotação 0 -> 1
            [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)],  # Rotação 1 -> 2
            [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)],  # Rotação 2 -> 3
            [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)],  # Rotação 3 -> 0
        ],
        'O': [],  # A peça O não precisa porque sua rotação não altera sua posição.
        'T': [
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        ],
        'S': [
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        ],
        'Z': [
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        ],
        'J': [
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        ],
        'L': [
            [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
            [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        ],
        'B': [],  # A peça B não precisa porque sua rotação não altera sua posição.
    }

    # Tenta cada "wall kick"
    for dx, dy in wall_kicks[peca['tipo']][rotacao_original]:
        if not detectar_colisao(peca, x + dx, y + dy, tabuleiro):
            return x + dx, y + dy

    # Se nenhum wall kick funcionar, desfaz a rotação e restaura a matriz.
    peca['matriz'] = matriz_original
    peca['rotacao'] = rotacao_original
    return x, y


def adicionar_peca_ao_tabuleiro(tabuleiro, peca, x, y): # Adiciona a peça à matriz do tabuleiro.
    for i in range(peca['matriz'].shape[0]):
        for j in range(peca['matriz'].shape[1]):
            if peca['matriz'][i, j] != 0:
                if y + i >= 0:  # Verifica se a peça está dentro dos limites
                    tabuleiro[y + i, x + j] = peca['matriz'][i, j]


def remover_linhas_completas(tabuleiro): # Verifica, remove linhas completas, retorna a matriz atualizada e a quantidade removida.
    linhas_removidas = 0
    linhas_para_remover = []
    for i in range(altura):
        if 0 not in tabuleiro[i]:
            linhas_para_remover.append(i)
    linhas_removidas = len(linhas_para_remover)
    if linhas_removidas > 0:
        tabuleiro = np.delete(tabuleiro, linhas_para_remover, axis=0)
        for _ in range(linhas_removidas):
            tabuleiro = np.insert(tabuleiro, 0, np.zeros(largura, dtype=int), axis=0)
    return tabuleiro, linhas_removidas


def desenhar_peca(janela, peca, x, y): # Desenha a peça na janela.
    for i in range(peca['matriz'].shape[0]):
        for j in range(peca['matriz'].shape[1]):
            if peca['matriz'][i, j] != 0:
                try:
                    cor = cores[peca['matriz'][i, j]]
                    janela.addstr(y + i + 1, (x + j) * 2 + 1, "▧", curses.color_pair(cor))
                except curses.error:
                    pass


def desenhar_tabuleiro(janela, tabuleiro): # Desenha o tabuleiro na janela.
    for i in range(altura):
        for j in range(largura):
            if tabuleiro[i, j] != 0:
                try:
                    janela.addstr(i + 1, j * 2 + 1, "▧", curses.color_pair(tabuleiro[i, j]))
                except curses.error:
                    pass


def mostrar_proxima_peca(janela_proxima, proxima_peca): # Exibe a próxima peça na janela designada.
    janela_proxima.erase()
    janela_proxima.border()
    janela_proxima.addstr(0, 2, " Próxima ")
    for i in range(proxima_peca['matriz'].shape[0]):
        for j in range(proxima_peca['matriz'].shape[1]):
            if proxima_peca['matriz'][i, j] != 0:
                try:
                    janela_proxima.addstr(i + 2, j * 2 + 2, "▧", curses.color_pair(proxima_peca['matriz'][i, j]))  # Ajustado para centralizar
                except curses.error:
                    pass


def mostrar_pontuacao(janela_pontuacao, pontuacao, nivel, linhas, combo): # Exibe a pontuação, nível, linhas removidas e combos na janela designada."""
    janela_pontuacao.erase()
    janela_pontuacao.border()
    janela_pontuacao.addstr(0, 2, " Pontuação ")
    janela_pontuacao.addstr(1, 2, f"Pontuação: {pontuacao}")
    janela_pontuacao.addstr(2, 2, f"Nível: {nivel}")
    janela_pontuacao.addstr(3, 2, f"Linhas: {linhas}")
    janela_pontuacao.addstr(4, 2, f"Combo: {combo}")


def explodir_peca(janela, peca, x, y, tabuleiro, pontuacao): # Aplica o efeito de explosão da peça bomba.
    explosao = []
    if peca['tipo'] == 'B':
        for i in range(peca['matriz'].shape[0]):
            for j in range(peca['matriz'].shape[1]):
                if peca['matriz'][i, j] != 0:
                    for k in range(y + i - 1, y + i + 2):
                        for l in range(x + j - 1, x + j + 2):
                            if 0 <= k < altura and 0 <= l < largura:
                                if tabuleiro[k, l] != 0:
                                    explosao.append((k, l))
                                    tabuleiro[k, l] = 0
        # Aplica o efeito visual da explosão
        for (k, l) in explosao:
            try:
                janela.addstr(k + 1, l * 2 + 1, "💥", curses.color_pair(8) | curses.A_BOLD)  # Caractere de explosão
            except curses.error:
                pass
        janela.refresh()
        time.sleep(0.1)
        # Remove efeito visual
        for (k, l) in explosao:
            try:
                janela.addstr(k + 1, l * 2 + 1, "  ", curses.color_pair(tabuleiro[k, l]))
            except curses.error:
                pass
        # Pontuação adicional por explosão
        pontuacao += len(explosao) * 5
    return pontuacao


def finalizar_jogo(stdscr, pontuacao): # Exibe a tela de Game Over e opções de reinício ou saída.
    stdscr.clear()
    altura_tela, largura_tela = stdscr.getmaxyx()
    game_over_msg = "Game Over!"
    pontuacao_msg = f"Pontuação final: {pontuacao}"
    opcao_msg = "Pressione 'r' para reiniciar ou 's' para sair."
    try:
        stdscr.addstr(altura_tela // 2 - 1, (largura_tela - len(game_over_msg)) // 2, game_over_msg, curses.A_BOLD)
        stdscr.addstr(altura_tela // 2, (largura_tela - len(pontuacao_msg)) // 2, pontuacao_msg)
        stdscr.addstr(altura_tela // 2 + 1, (largura_tela - len(opcao_msg)) // 2, opcao_msg)
    except curses.error:
        pass
    stdscr.refresh()
    while True:
        tecla_final = stdscr.getch()
        if tecla_final in [ord('r'), ord('R')]:
            main(stdscr)  # Reiniciar o jogo
            break
        elif tecla_final in [ord('s'), ord('S')]:
            break  # Sair do jogo


def mostrar_menu(stdscr): # Exibe o menu inicial na tela.
    stdscr.clear()
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Opções do menu
    opcoes = ["Iniciar Jogo", "Opções", "Sair"]
    opcao_selecionada = 0

    while True:
        stdscr.erase()
        stdscr.border(curses.ACS_DIAMOND, curses.ACS_DIAMOND, curses.ACS_DIAMOND, curses.ACS_DIAMOND)

        # Título do jogo
        titulo = "TETRIS"
        moldura = "▄" * (len(titulo) + 3)  
        stdscr.addstr(altura_tela // 2 - 5, (largura_tela - len(moldura)) // 2, moldura)
        stdscr.addstr(altura_tela // 2 - 4, (largura_tela - len(titulo)) // 2, titulo, curses.A_BOLD | curses.A_CHARTEXT | curses.A_BLINK)
        stdscr.addstr(altura_tela // 2 - 3, (largura_tela - len(moldura)) // 2, moldura)
        # Opções do menu
        for i, opcao in enumerate(opcoes):
            atributos = curses.A_REVERSE if i == opcao_selecionada else 0
            stdscr.addstr(altura_tela // 2 - 1 + i, (largura_tela - len(opcao)) // 2, opcao, atributos)

        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla == curses.KEY_UP: # Tecla para cima
            opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
        elif tecla == curses.KEY_DOWN: # Tecla para baixo
            opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
        elif tecla == curses.KEY_ENTER or tecla in [10, 13]:  # Tecla Enter
            if opcao_selecionada == 0: 
                return  # Sai do menu e inicia o jogo
            elif opcao_selecionada == 1:  # Opções
                mostrar_opcoes(stdscr)  # Chama a função de opções
            elif opcao_selecionada == 2:  # Opção sair
                exit()  # Sai do jogo


def mostrar_opcoes(stdscr): # Exibe as opções do jogo."""
    stdscr.clear()
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Opções configuráveis no menu
    opcoes = {
        "Dificuldade": ["Fácil", "Médio", "Difícil"],
        "Controles": ["WASD", "Setas"]
    }
    opcoes_selecionadas = {chave: 0 for chave in opcoes}
    opcao_atual = list(opcoes.keys())[0]

    while True:
        stdscr.erase()
        stdscr.border()

        # Título da tela de opções
        titulo = "Opções"
        stdscr.addstr(altura_tela // 2 - 6, (largura_tela - len(titulo)) // 2, titulo, curses.A_BOLD)

        # Opções do menu
        for i, (chave, valores) in enumerate(opcoes.items()):
            atributos = curses.A_REVERSE if chave == opcao_atual else 0
            stdscr.addstr(altura_tela // 2 - 3 + i, 2, chave + ":", atributos)
            for j, valor in enumerate(valores):
                atributos_valor = curses.A_REVERSE if j == opcoes_selecionadas[chave] else 0
                stdscr.addstr(altura_tela // 2 - 3 + i, 15 + j * 10, valor, atributos_valor)

        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla == curses.KEY_UP:
            indice_opcao_atual = list(opcoes.keys()).index(opcao_atual)
            indice_opcao_atual = (indice_opcao_atual - 1) % len(opcoes)
            opcao_atual = list(opcoes.keys())[indice_opcao_atual]
        elif tecla == curses.KEY_DOWN:
            indice_opcao_atual = list(opcoes.keys()).index(opcao_atual)
            indice_opcao_atual = (indice_opcao_atual + 1) % len(opcoes)
            opcao_atual = list(opcoes.keys())[indice_opcao_atual]
        elif tecla == curses.KEY_LEFT:
            opcoes_selecionadas[opcao_atual] = (opcoes_selecionadas[opcao_atual] - 1) % len(opcoes[opcao_atual])
        elif tecla == curses.KEY_RIGHT:
            opcoes_selecionadas[opcao_atual] = (opcoes_selecionadas[opcao_atual] + 1) % len(opcoes[opcao_atual])
        elif tecla == curses.KEY_ENTER or tecla in [10, 13]:  # Enter
            # Salva as opções no dicionário global
            configuracoes["dificuldade"] = opcoes["Dificuldade"][opcoes_selecionadas["Dificuldade"]]
            configuracoes["controles"] = opcoes["Controles"][opcoes_selecionadas["Controles"]]
            break  # Volta ao menu principal


def main(stdscr): # Principal função
    # Inicialização do terminal e da comdiguração das cores
    curses.curs_set(0) 
    if not curses.has_colors():
        stdscr.addstr(0, 0, "Seu terminal não suporta cores.\n")
        stdscr.addstr(1, 0, "Pressione qualquer tecla para sair...")
        stdscr.refresh()
        stdscr.getch()
        return

    curses.start_color()
    curses.use_default_colors()
    for i in range(1, len(cores) + 1):
        curses.init_pair(i, cores[i], -1) 


    # Mostra o menu inicial
    mostrar_menu(stdscr)

    # Aplica as configurações de dificuldade 
    if configuracoes["dificuldade"] == "Fácil":
        velocidade_inicial = 0.3
    elif configuracoes["dificuldade"] == "Médio":
        velocidade_inicial = 0.2
    elif configuracoes["dificuldade"] == "Difícil":
        velocidade_inicial = 0.1

    altura_tela, largura_tela = stdscr.getmaxyx()

    # Ajusta a posição e dimensões da janela principal
    janela_altura = altura + 2
    janela_largura = largura * 2 + 2  #
    janela_x = max((largura_tela // 2 - janela_largura // 2), 0)
    janela_y = max((altura_tela // 2 - janela_altura // 2), 0)
    janela = curses.newwin(janela_altura, janela_largura, janela_y, janela_x)
    janela.keypad(True)
    janela.nodelay(True)
    janela.border()

    # Janela para a próxima peça
    janela_proxima = curses.newwin(8, 14, janela_y, janela_x + janela_largura + 4)
    janela_proxima.border()
    janela_proxima.addstr(0, 2, " Próxima ")

    # Janela para a pontuação
    janela_pontuacao = curses.newwin(10, 20, janela_y + 10, janela_x + janela_largura + 4)
    janela_pontuacao.border()
    janela_pontuacao.addstr(0, 2, " Pontuação ")

    # Inicializa o tabuleiro
    tabuleiro = np.zeros((altura, largura), dtype=int)

    # Inicializa a primeira peça e a próxima peça
    peca_atual = criar_peca()
    proxima_peca = criar_peca()
    x, y = largura // 2 - 2, 0  # Posição inicial ajustada para o centro

    pontuacao = 0
    nivel = 1
    linhas_removidas = 0
    velocidade = velocidade_inicial
    tempo_ultima_queda = time.time()
    combo = 0
    tempo_ultimo_combo = time.time()
    pausado = False
    jogo_em_andamento = True

    # Loop principal
    while jogo_em_andamento:
        janela.erase()
        janela.border()

        # Desenha a peça atual
        desenhar_peca(janela, peca_atual, x, y)

        # Desenha o tabuleiro
        desenhar_tabuleiro(janela, tabuleiro)

        # Exibe a próxima peça
        mostrar_proxima_peca(janela_proxima, proxima_peca)

        # Exibe a pontuação
        mostrar_pontuacao(janela_pontuacao, pontuacao, nivel, linhas_removidas, combo)

        # Atualiza a tela
        janela.refresh()
        janela_proxima.refresh()
        janela_pontuacao.refresh()

        # Captura a entrada do usuário, considerando as configurações de controles
        tecla = janela.getch()
        if tecla != -1:
            if configuracoes["controles"] == "WASD":
                if tecla == ord('a'):  # Move a peça para esquerda
                    if not detectar_colisao(peca_atual, x - 1, y, tabuleiro):
                        x -= 1
                elif tecla == ord('d'):  # Move a peça para direita
                    if not detectar_colisao(peca_atual, x + 1, y, tabuleiro):
                        x += 1
                elif tecla == ord('s'):  # Move a peça para baixo
                    if not detectar_colisao(peca_atual, x, y + 1, tabuleiro):
                        y += 1
                elif tecla == ord('w'):  # Rotaciona a peça
                    x, y = tentar_rotacao(peca_atual, x, y, tabuleiro)
            elif configuracoes["controles"] == "Setas":
                if tecla == curses.KEY_LEFT:  #  Move a peça para esquerda
                    if not detectar_colisao(peca_atual, x - 1, y, tabuleiro):
                        x -= 1
                elif tecla == curses.KEY_RIGHT:  #  Move a peça para direita
                    if not detectar_colisao(peca_atual, x + 1, y, tabuleiro):
                        x += 1
                elif tecla == curses.KEY_DOWN:  #  Move a peça para baixo
                    if not detectar_colisao(peca_atual, x, y + 1, tabuleiro):y += 1
                elif tecla == curses.KEY_UP:  # Rotaciona a peça
                    x, y = tentar_rotacao(peca_atual, x, y, tabuleiro)
            elif tecla in [ord('p'), ord('P')]: # P
                pausado = not pausado
            elif tecla in [ord('q'), ord('Q')]:
                break  # Sair do jogo

        if not pausado:
            current_time = time.time()
            if current_time - tempo_ultima_queda > velocidade:
                if not detectar_colisao(peca_atual, x, y + 1, tabuleiro):
                    y += 1
                else:
                    # Fixar a peça no tabuleiro
                    adicionar_peca_ao_tabuleiro(tabuleiro, peca_atual, x, y)

                    # Se a peça for bomba, exploda
                    pontuacao = explodir_peca(janela, peca_atual, x, y, tabuleiro, pontuacao)

                    # Remove linhas completas
                    tabuleiro, linhas = remover_linhas_completas(tabuleiro)
                    linhas_removidas += linhas

                    # Verifica combos
                    if linhas > 0:
                        if current_time - tempo_ultimo_combo <= tempo_combo:
                            combo += 1
                        else:
                            combo = 1
                        pontuacao += linhas * 100 * combo  # Pontuação por combo
                        tempo_ultimo_combo = current_time
                        curses.beep()
                    else:
                        if current_time - tempo_ultimo_combo > tempo_combo:
                            combo = 0

                    # Adiciona pontuação da peça
                    pontuacao += pontuacao_pecas.get(peca_atual['tipo'], 0)

                    # Atualiza o nível e velocidade
                    novo_nivel = linhas_removidas // 10 + 1  # Aumenta o nível a cada 10 linhas
                    if novo_nivel > nivel:
                        nivel = novo_nivel
                        velocidade = max(velocidade - velocidade_incremento, velocidade_minima)
                        curses.flash()

                    # Gera uma nova peça
                    peca_atual = proxima_peca
                    proxima_peca = criar_peca()
                    x, y = largura // 2 - 2, 0  # Posição inicial no centro

                    # Verifica se a nova peça colide com o topo, se sim, imediatamente indica que o jogador perdeu (Game Over)
                    if detectar_colisao(peca_atual, x, y, tabuleiro):
                        jogo_em_andamento = False

                tempo_ultima_queda = current_time

        time.sleep(0.01)  # Pequena pausa para reduzir o uso da CPU

    # Finaliza o jogo
    finalizar_jogo(stdscr, pontuacao)


if __name__ == "__main__": # Executa o programa
    curses.wrapper(main)


# Autor: Stheffanny Nascimento Alves
# Componente Curricular: MI Algoritmos
# Concluído em: 27/10/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.