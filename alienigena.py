import pygame
from pygame.sprite import Sprite


class Alienigena(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, configuracoes, tela):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alienigena, self).__init__()
        self.tela = tela
        self.configuracoes = configuracoes

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('imagens/alienigena.png')
        comp, larg = self.image.get_size()
        self.image = pygame.transform.smoothscale(self.image, (int(comp * 0.085), int(larg * 0.085)))

        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    def posicionar_alienigena(self):
        """Desenha o alienígena em sua posição atual."""
        self.tela.blit(self.image, self.rect)

    def verificar_arestas(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienígena para a direita."""
        # Se direcao_frota == 1, fator_velocidade_alienigena será somado à posição atual, movendo-se para a direita;
        # se direcao_frota == -1, mover-se-a para a esquerda.
        self.x += self.configuracoes.fator_velocidade_alienigena * self.configuracoes.direcao_frota
        self.rect.x = self.x
