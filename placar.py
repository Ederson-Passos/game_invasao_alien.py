import pygame.font
from pygame.sprite import Group

from nave import Nave


class Placar:
    """Uma classe para mostrar informações sobre pontuação."""

    def __init__(self, configuracoes, tela, estatisticas):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.configuracoes = configuracoes
        self.estatisticas = estatisticas

        # Configurações de fonte para as informações de pontuação
        self.cor_texto = (0, 255, 0)
        self.fonte = pygame.font.Font("ARCADECLASSIC.TTF", 24)

        # Prepara a imagem de pontuações iniciais
        self.prepara_score()
        self.prepara_pontuacao_maxima()
        self.prepara_nivel()
        self.prepara_naves()

    def prepara_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        score_arredondado = round(self.estatisticas.pontuacao, -1)
        score_str = "Pontos  {:,}".format(score_arredondado)
        self.score_image = self.fonte.render(score_str, True, self.cor_texto, self.configuracoes.cor_tela)

        # Exibe a pontuação na parte superior direita da tela
        self.pontuacao_rect = self.score_image.get_rect()
        self.pontuacao_rect.right = self.tela_rect.right - 20
        self.pontuacao_rect.top = 20

    def apresenta_score(self):
        """Desenha a pontução na tela."""
        self.tela.blit(self.score_image, self.pontuacao_rect)
        self.tela.blit(self.pontuacao_maxima_imagem, self.pontuacao_maxima_rect)
        self.tela.blit(self.nivel_imagem, self.nivel_rect)

    def prepara_pontuacao_maxima(self):
        """Transforma a pontuação máxima em uma imagem renderizada."""
        pontuacao_maxima = round(self.estatisticas.pontuacao_maxima, -1)
        pontuacao_maxima_str = "Recorde   {:,}".format(pontuacao_maxima)
        self.pontuacao_maxima_imagem = self.fonte.render(
            pontuacao_maxima_str, True, self.cor_texto, self.configuracoes.cor_tela)

        # Centraliza a pontuação máxima na parte superior da tela.
        self.pontuacao_maxima_rect = self.pontuacao_maxima_imagem.get_rect()
        self.pontuacao_maxima_rect.centerx = self.tela_rect.centerx
        self.pontuacao_maxima_rect.top = self.pontuacao_rect.top

    def prepara_nivel(self):
        """Transforma o nivel em uma imagem renderizada."""
        self.nivel_imagem = self.fonte.render(
            str("Nivel {} ".format(self.estatisticas.nivel)), True, self.cor_texto, self.configuracoes.cor_tela)

        # Posiciona o nível abaixo da pontuação.
        self.nivel_rect = self.nivel_imagem.get_rect()
        self.nivel_rect.right = self.pontuacao_rect.right
        self.nivel_rect.top = self.pontuacao_rect.bottom + 10

    def prepara_naves(self):
        """Mostra quantas espaçonaves restam."""
        pass