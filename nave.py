import pygame
from pygame.sprite import Sprite


# A classe Nave herda de Sprite
class Nave(Sprite):

    def __init__(self, configuracoes, tela):
        """Inicializa a espaçonave e define sua posição inicial."""
        super(Nave, self).__init__()
        self.tela = tela
        self.configuracoes = configuracoes  # Recebendo acesso às configurações de velocidade

        # Carrega a imagem da espaçonave e obtém seu rect
        self.imagem = pygame.image.load('imagens/nave_sem_fundo.png')

        # Recuperando a escala da imagem:
        comp, larg = self.imagem.get_size()
        # Redimensionando a imagem:
        self.imagem = pygame.transform.smoothscale(self.imagem, (int(comp * 0.1), int(larg * 0.1)))

        self.rect = self.imagem.get_rect()  # Trata a imagem como retângulos, 'rect', daí podermos manipular
        # suas coordenadas
        # Armazenando a tela em um retângulo:
        self.tela_retangulo = tela.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.tela_retangulo.centerx
        self.rect.bottom = self.tela_retangulo.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        # Flags de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False

    def atualizar(self):
        """Atualiza a posição da nave de acordo com as flags de movimento."""
        # Atualiza o valor do centro da espaçonave e não o retângulo
        if self.movendo_direita and self.rect.right < self.tela_retangulo.right:
            self.center += self.configuracoes.fator_velocidade_nave
        if self.movendo_esquerda and self.rect.left > 0:
            self.center -= self.configuracoes.fator_velocidade_nave

        # Atualiza o objeto "retangulo" de acordo com self.centro
        self.rect.centerx = self.center

    def posicionar_nave(self):
        """Desenha a espaçonave em sua posição atual."""
        self.tela.blit(self.imagem, self.rect)

    def centralizar_nave(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.tela_retangulo.centerx
