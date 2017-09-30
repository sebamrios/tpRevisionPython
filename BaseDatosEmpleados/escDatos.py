class Escritura():
    #archivo=""
    #cadena=""

    def __inti__(self):
        self.archivo=""
        self.cadena=""

    def abrirDoc(self,nombre,datos):
        self.archivo=nombre
        f.open(self.archivo,'a')
        f.write(datos)
        f.close
