from threading import Thread
from time import sleep


class Cronometro(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.parado = True

    def run(self):
        while True:
            # Enquanto o self.parado nao for True
            while not self.parado:
                self.segundos += 1
                self.format_time()
                sleep(1)


    def initCronometro(self):
        self.parado = False

    def showTime(self):
        print(f'Tempo do cronometro: {self.horas}:{self.minutos}:{self.segundos}')

    def pause(self):
        if(self.parado):
            return
        else:
            self.parado = True

    def resume(self):
        if (self.parado):
            self.parado = False
        else:
            return

    def restart(self):
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.parado = True

    def format_time(self):
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        if self.horas >= 24:
            self.horas = 0
