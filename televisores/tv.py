class TV:
    
    _canal: int = 1
    _precio: int = 500
    _estado: bool
    _volumen: int = 1
    numTV: int = 0

    def __init__(self, marca, estado: bool):
        self._marca = marca
        self._estado = estado
        TV._numTV += 1

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._estado and self._canal < 120):
            self._canal +=1

    def canalDown(self):
        if (self._estado and self._canal > 1):
            self._canal -= 1

    def volumenUp(self):
        if (self._estado and self._volumen < 7):
            self._volumen += 1

    def volumenDow(self):
        if (self.estado and  self._volume > 0):
            self._volumen -= 1

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if (self._estado and canal >= 1 and canal <= 120):
            self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if (self._estado and volumen >= 0 and volumen <= 7):
            self._volumen = volumen

    def getNumTV ():
        return TV.numTV  

    def setNumTV(numTV: int):
        TV.numTV = numTV

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    




