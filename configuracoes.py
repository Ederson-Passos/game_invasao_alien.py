class Configuracoes:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.tela_comprimento = 1300
        self.tela_altura = 710
        self.cor_tela = (0, 0, 0)

        # Configurações da espaçonave
        self.limite_de_naves = 3

        # Configurações dos projéteis:
        self.projetil_largura = 3
        self.projetil_altura = 15
        self.projetil_cor = (255, 0, 0)
        self.projeteis_permitidos = 5

        # Configurações dos alienígenas:
        self.velocidade_queda_frota = 2

        # A taxa com que a velocidade do jogo aumenta
        self.escala_aumento_velocidade = 1.25

        # A taxa com que os pontos para cada alienígena aumentam
        self.score_escala = 1.5

        self.inicializa_configuracoes_dinamicas()

    def inicializa_configuracoes_dinamicas(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.fator_velocidade_nave = 1.5
        self.fator_velocidade_projetil = 2
        self.fator_velocidade_alienigena = 1

        # direcao_frota igual a 1 representa direita; -1 representa esquerda.
        self.direcao_frota = 1

        # Pontuação
        self.pontos_alienigena = 10

    def incrementa_velocidade(self):
        """Aumenta as configurações de velocidade e os pontos para cada alienígena."""
        self.fator_velocidade_nave *= self.escala_aumento_velocidade
        self.fator_velocidade_projetil *= self.escala_aumento_velocidade
        self.fator_velocidade_alienigena *= self.escala_aumento_velocidade

        self.pontos_alienigena = int(self.pontos_alienigena * self.score_escala)
