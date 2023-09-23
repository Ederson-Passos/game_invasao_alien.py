class EstatisticasJogo:
    """Armazena dados estatísticos da Invasão Alien."""

    def __init__(self, configuracoes):
        """Inicializa os dados estatísticos."""
        self.configuracoes = configuracoes
        self.resetar_estatisticas()

        # Inicia o jogo em um estado inativo
        self.jogo_ativo = False
        self.pontuacao_maxima = 0

    def resetar_estatisticas(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.naves_usadas = self.configuracoes.limite_de_naves
        self.pontuacao = 0
        self.nivel = 1