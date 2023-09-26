import sys
from time import sleep

import pygame
from alienigena import Alienigena
from projetil import Projetil


def checar_eventos_keydown(evento, configuracoes, tela, nave, projeteis):
    """Responde a pressionamentos de tecla."""
    if evento.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita:
        nave.movendo_direita = True
    elif evento.key == pygame.K_LEFT:
        nave.movendo_esquerda = True
    elif evento.key == pygame.K_SPACE:
        disparar_projetil(configuracoes, tela, nave, projeteis)
    # Atalho para encerrar o jogo:
    elif evento.key == pygame.K_q:
        sys.exit()


def disparar_projetil(configuracoes, tela, nave, projeteis):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    # Cria um novo projétil e o adiciona ao grupo de projéteis.
    if len(projeteis) < configuracoes.projeteis_permitidos:
        novo_projetil = Projetil(configuracoes, tela, nave)
        projeteis.add(novo_projetil)


def checar_eventos_keyup(evento, nave):
    """Responde a solturas de tecla."""
    if evento.key == pygame.K_RIGHT:
        nave.movendo_direita = False
    elif evento.key == pygame.K_LEFT:
        nave.movendo_esquerda = False


def checar_eventos(configuracoes, tela, estatisticas, placar, botao_play, nave, alienigenas, projeteis):
    """Responde aos eventos de pressionamento de teclas e mouse."""
    pygame.mouse.set_visible(False)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        elif evento.type == pygame.KEYDOWN:  # Verificando se é a seta para a direita ou esquerda.
            checar_eventos_keydown(evento, configuracoes, tela, nave, projeteis)

        elif evento.type == pygame.KEYUP:
            checar_eventos_keyup(evento, nave)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            verificar_botao_play(configuracoes, tela, estatisticas, placar, botao_play, nave, alienigenas,
                                 projeteis, mouse_x, mouse_y)

        elif evento.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)


def verificar_botao_play(configuracoes, tela, estatisticas, placar, botao_play, nave, alienigenas,
                         projeteis, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    botao_clicado_play = botao_play.rect.collidepoint(mouse_x, mouse_y)
    if botao_clicado_play and not estatisticas.jogo_ativo:
        # Reinicia as configurações do jogo
        configuracoes.inicializa_configuracoes_dinamicas()

        # Reinicia os dados estatísticos do jogo
        estatisticas.resetar_estatisticas()
        estatisticas.jogo_ativo = True

        # Reinicia as imagens do painel de pontuação
        placar.prepara_score()
        placar.prepara_pontuacao_maxima()
        placar.prepara_nivel()
        placar.prepara_naves()

        # Esvazia a lista de alienígenas e de projetéis
        alienigenas.empty()
        projeteis.empty()

        # Cria uma nova frota e centraliza a espaçonave
        criar_frota(configuracoes, tela, nave, alienigenas)
        nave.centralizar_nave()


def atualizar_tela(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis, botao_play, bg_image):
    """Atualiza as imagens na tela e alterna para a nova tela a cada passagem pelo laço principal."""
    # Redesenha a tela a cada passagem pelo laço
    tela.fill(configuracoes.cor_tela)

    # Desenha a imagem de fundo da tela
    tela.blit(dimensionando_fundo(bg_image), (0, 0))

    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas.
    for projetil in projeteis.sprites():
        projetil.desenhar_projetil()
    nave.posicionar_nave()
    # Chamando draw() em um grupo Pygame desenha automaticamente cada elemento do grupo na posição
    # Definida pelo seu atributo rect.
    alienigenas.draw(tela)

    # Desenha a informação sobre pontuação
    placar.apresenta_score()

    # Desenha o botão Play se o jogo estiver inativo
    if not estatisticas.jogo_ativo:
        botao_play.desenhar_botao()

    # Deixa a tela mais recente visível
    pygame.display.flip()


def dimensionando_fundo(bg_image):
    """Redimensiona a imagem de fundo da tela."""
    comp, larg = bg_image.get_size()
    bg_image = pygame.transform.smoothscale(bg_image, (int(comp * 2.8), int(larg * 2.8)))
    return bg_image


def atualizar_projeteis(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis:
    projeteis.update()

    # Livra-se dos projéteis que desapareceram:
    for projetil in projeteis.copy():
        if projetil.rect.bottom <= 0:
            projeteis.remove(projetil)

    verificar_colisao_de_projetil_e_alienigena(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)


def verificar_colisao_de_projetil_e_alienigena(configuracoes, tela, estatisticas, placar, nave,
                                               alienigenas, projeteis):
    """Responde a colisões entre projéteis e alienígenas."""
    # Verifica se algum projétil atingiu os alienígenas analisando se ouve sebreposição de rects
    # "colisoes" será um dicionário onde a chave é o projétil e o valor é uma lista de alienígenas
    # Se sim, livra-se do projétil e do alienígena pelos dois argumentos True
    # Deixar o terceiro parâmetro como False criaria um projétil que destruiria alienígenas até o topo da tela
    colisoes = pygame.sprite.groupcollide(projeteis, alienigenas, True, True)

    if colisoes:
        for alienigenas in colisoes.values():
            estatisticas.pontuacao += configuracoes.pontos_alienigena * len(alienigenas)
            placar.prepara_score()
        verificar_pontuacao_maxima(estatisticas, placar)

    if len(alienigenas) == 0:
        # Se a frota for toda destruída, inicia um novo nível
        projeteis.empty()
        configuracoes.incrementa_velocidade()

        # Aumenta o nível
        estatisticas.nivel += 1
        placar.prepara_nivel()

        criar_frota(configuracoes, tela, nave, alienigenas)


def obter_num_alienigenas(configuracoes, alienigena_largura):
    """Determina o número de alienígenas que cabem em uma linha."""
    # Deixando duas margens livres com a largura de um alienígena:
    espaco_disponivel_x = configuracoes.tela_comprimento - (2 * alienigena_largura)
    # Definindo o espaço entre os alienígenas: um alienígena de largura.
    numero_alienigenas_x = int(espaco_disponivel_x / (2 * alienigena_largura))
    return numero_alienigenas_x


def obter_num_linhas(configuracoes, nave_altura, alienigena_altura):
    """Determina o número de linhas com alienígenas que cabem na tela."""
    espaco_disponivel_y = configuracoes.tela_altura - 3 * alienigena_altura - nave_altura
    numero_linhas = int(espaco_disponivel_y / (9 * alienigena_altura))
    return numero_linhas


def criar_alienigena(configuracoes, tela, alienigenas, numero_alienigena, numero_linhas):
    # Cria um alienígena e o posiciona na linha
    alienigena = Alienigena(configuracoes, tela)
    alienigena_largura = alienigena.rect.width
    # Definindo a posição horizontal em função da margem,do espaço de duas naves vezes
    # o número de naves:
    alienigena.x = alienigena_largura + 2 * alienigena_largura * numero_alienigena
    alienigena.rect.x = alienigena.x
    alienigena.rect.y = alienigena.rect.height + 2 * alienigena.rect.height * numero_linhas
    alienigenas.add(alienigena)


def criar_frota(configuracoes, tela, nave, alienigenas):
    """Cria uma frota completa de alienígenas"""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alienigena = Alienigena(configuracoes, tela)
    numero_alienigenas_x = obter_num_alienigenas(configuracoes, alienigena.rect.width)
    numero_linhas = obter_num_linhas(configuracoes, nave.rect.height, alienigena.rect.height)

    # Cria a frota de alienígenas
    for numero_linha in range(numero_linhas):
        for numero_alienigena in range(numero_alienigenas_x):
            # Cria um alienígena e o posiciona na linha
            criar_alienigena(configuracoes, tela, alienigenas, numero_alienigena, numero_linha)


def mudar_direcao_frota(configuracoes, alienigenas):
    """Faz toda a frota descer e modifica a sua direção."""
    for alienigena in alienigenas.sprites():
        alienigena.rect.y += configuracoes.velocidade_queda_frota
    configuracoes.direcao_frota *= -1


def verificar_arestas_frota(configuracoes, alienigenas):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alienigena in alienigenas.sprites():
        if alienigena.verificar_arestas():
            mudar_direcao_frota(configuracoes, alienigenas)
            break


def nave_atingida(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis):
    """Responde ao evento de a nave ser atingida por um alienígena."""
    if estatisticas.naves_usadas > 0:
        # Decrementa naves_usadas
        estatisticas.naves_usadas -= 1

        # Atualiza o painel de pontuações
        placar.prepara_naves()

        # Esvazia a lista de alienígenas e de projéteis
        alienigenas.empty()
        projeteis.empty()

        # Cria uma nova frota e centraliza a espaçonave
        criar_frota(configuracoes, tela, nave, alienigenas)
        nave.centralizar_nave()

        # Faz uma pausa para o jogador
        sleep(1.0)

    else:
        estatisticas.jogo_ativo = False
        pygame.mouse.set_visible(True)


def verificar_aresta_inferior_alienigenas(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    tela_rect = tela.get_rect()
    for alienigena in alienigenas.sprites():
        if alienigena.rect.bottom >= tela_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            nave_atingida(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)
            break


def atualizar_alienigenas(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis):
    """
    Verifica se a frota está em uma das bordas
    e então atualiza as posições de todos os alienígenas da frota.
    """
    verificar_arestas_frota(configuracoes, alienigenas)
    alienigenas.update()

    # Verifica se houve colisões entre alienígenas (group) e a espaçonave (sprite), devolvendo o primeiro
    # membro do group que colidiu
    if pygame.sprite.spritecollideany(nave, alienigenas):
        nave_atingida(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)

    verificar_aresta_inferior_alienigenas(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)


def verificar_pontuacao_maxima(estatisticas, placar):
    """Verifica se há uma nova pontuação máxima."""
    if estatisticas.pontuacao > estatisticas.pontuacao_maxima:
        estatisticas.pontuacao_maxima = estatisticas.pontuacao
        placar.prepara_pontuacao_maxima()
