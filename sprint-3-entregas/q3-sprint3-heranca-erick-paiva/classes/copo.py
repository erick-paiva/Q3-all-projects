from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self,tamanho:float) -> None:
        super().__init__(tamanho)
        self.bebida = ""
        
    def encher(self,bebida:str = "água"):
        if self.limpo == False:
            return "Não se pode encher um copo sujo"
        else:
            self.limpo = False
            self.bebida = bebida
            self.conteudo = self.tamanho
                
    def beber(self,quantidade: float):
        if quantidade < 0: return "Quantidade deve ser positiva"
        
        if quantidade > self.tamanho: return "Não há bebida suficiente no copo"
        
        self.conteudo -= quantidade if quantidade > 0 else 0
        
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
    
    def __str__(self):
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo == 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
    
    def __repr__(self):
        return f"Um copo vazio de {float(self.tamanho)}ml" if self.conteudo == 0 else f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
    
