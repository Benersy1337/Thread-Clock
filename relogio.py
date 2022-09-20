from threading import Thread
from time import sleep


class Relogio(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.segundos = 0
        self.minutos = 0
        self.horas = 0

    def run(self):
        while True:
            sleep(1)
            self.segundos += 1
            self.format_time()


    def setupTime(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        

    def showTime(self):
        print(f"Tempo: {self.horas}:{self.minutos}:{self.segundos}")

    def format_time(self):
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        if self.horas >= 24:
            self.horas = 0

    def returnTime(self):
        return self.horas, self.minutos, self.segundos
    

