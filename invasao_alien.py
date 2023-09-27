import pygame
from pygame.sprite import Group

from botao import Botao
from configuracoes import Configuracoes
from placar import Placar
from estatisticas_jogo import EstatisticasJogo
from nave import Nave
import funcoes_jogo as funcoes


def iniciar_jogo():
    pygame.init()
    configuracoes = Configuracoes()
    tela = pygame.display.set_mode((configuracoes.tela_comprimento, configuracoes.tela_altura))
    pygame.display.set_caption("Invasão Alien")
    bg_image = pygame.image.load('imagens/background.jpg').convert_alpha()  # Salvando uma imagem para o fundo
    botao_play = Botao(configuracoes, tela, "Play")
    estatisticas = EstatisticasJogo(configuracoes)
    placar = Placar(configuracoes, tela, estatisticas)
    nave = Nave(configuracoes, tela)
    projeteis = Group()
    alienigenas = Group()
    projeteis_alienigenas = Group()
    funcoes.criar_frota(configuracoes, tela, nave, alienigenas)

    while True:
        funcoes.checar_eventos(configuracoes, tela, estatisticas, placar, botao_play, nave, alienigenas, projeteis)
        
        if estatisticas.jogo_ativo:
            nave.atualizar()
            funcoes.atualizar_projeteis(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)
            funcoes.atualizar_alienigenas(configuracoes, tela, estatisticas, placar, nave, alienigenas, projeteis)

        funcoes.atualizar_tela(configuracoes, tela, estatisticas, placar, nave,
                               alienigenas, projeteis, botao_play, bg_image)



iniciar_jogo()
