class Recipiente:
    
    def __init__(self, tamanho: float, conteudo: float = 0, limpo : bool = True) -> None:
        self.tamanho = tamanho if tamanho > -1 else 0
        self.conteudo = conteudo
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        return True if self.conteudo == 0 else False
    
    def lavar(self):
        self.limpo = True
        self.conteudo = 0
        
    def esta_limpo(self):
        return self.limpo
    
    def estado(self):
        return "limpo" if self.limpo else "sujo"
    
    def sujar(self):
        self.limpo = False
        
    def __str__(self):
        return f"Um recipiente {self.estado()} não especificado"
    
    def __repr__(self):
        return f"Um recipiente {self.estado()} não especificado"
    
