class Camera:
    def __init__(self, nome, filmando = False, fotografando = False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografando

    def filmar(self):
        if self.filmando and not self.fotografando:
            print(f'A camera {self.nome} JÁ está filmando')
            return
        elif not self.filmando and not self.fotografando:
            print(f'A camera {self.nome} começou a filmar agora')
            self.filmando = True
        elif not self.filmando and self.fotografando:
            print(f'A camera {self.nome} está fotografando, então não pode filmar, desligando modo de fotografia')
            return self.parar_fotografar()
        
    def fotografar(self):
        if not self.filmando and self.fotografando:
            print(f'A camera {self.nome} JÁ está fotografando')
            return
        elif not self.filmando and not self.fotografando:
            print(f'A camera {self.nome} pode fotografar agora')
            self.fotografando = True
        elif  self.filmando and not self.fotografando:
            print(f'A camera {self.nome} está filmando, então não pode tirar foto, desligando modo de filmagem')
            return self.parar_filmar()

    def parar_filmar(self):
        self.filmando = False
        return
    
    def parar_fotografar(self): 
        self.fotografando = False
        return

    
    

c1 = Camera('canon')
c2 = Camera('nokia')
# print(c1.nome)
# print(c2.nome)
# print()
print(c1.filmando)
c1.filmar()
c1.filmar()
c1.fotografar()
c1.fotografar()
c1.filmar()
c1.filmar()

c2.filmar()
c2.filmar()
c2.fotografar()
c2.fotografar()
c2.filmar()
c2.filmar()