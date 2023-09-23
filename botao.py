import pygame.font


class Botao:

    def __init__(self, configuracoes, tela, mensagem):
        """Inicializa os atributos do botão."""
        self.tela = tela
        self.tela_rect = tela.get_rect()

        # Define as dimensões e as propriedades do botão
        self.width, self.height = 200, 50
        self.cor_botao = (255, 0, 0)
        self.cor_texto = (255, 255, 255)
        self.fonte = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.tela_rect.center

        # Prepara a mensagem para o botão
        self.imagem_mensagem = self.fonte.render(mensagem, True, self.cor_texto, self.cor_botao)
        self.imagem_mensagem_rect = self.imagem_mensagem.get_rect()
        self.imagem_mensagem_rect.center = self.rect.center

    def desenhar_botao(self):
        # Desenha um botão em branco e, em seguida, desenha a mensagem
        self.tela.fill(self.cor_botao, self.rect)  # Desenha a parte retangular
        self.tela.blit(self.imagem_mensagem, self.imagem_mensagem_rect)  # Desenha a imagem do texto
