import pygame
from pygame.sprite import Sprite


class Projetil(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""

    def __init__(self, configuracoes, tela, nave):
        """Cria um objeto para o projétil na posição atual da espaçonave."""
        super().__init__()  # super() para herdar de Sprite.
        self.tela = tela

        # Cria um retângulo para o projétil em (0,0) e, em seguida, define a posição correta.
        self.rect = pygame.Rect(0, 0, configuracoes.projetil_largura, configuracoes.projetil_altura)
        # Definindo o centerx do projétil para ser igual ao do retângulo da nave.
        self.rect.centerx = nave.rect.centerx
        # Para parecer que o projétil emerge do topo da espaçonave:
        self.rect.top = nave.rect.top

        # Armazena a posição do projétil como um valor decimal.
        self.y = float(self.rect.y)

        self.cor = configuracoes.projetil_cor
        self.fator_velocidade = configuracoes.fator_velocidade_projetil

    def update(self):
        """Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil.
        self.y -= self.fator_velocidade
        # Atualiza a posição de 'retangulo'.
        self.rect.y = self.y

    def desenhar_projetil(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.tela, self.cor, self.rect)
