from threading import Thread
from time import sleep


class Alarme(Thread):
    def __init__(self, horas, minutos, segundos):
        Thread.__init__(self)
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.fhoras = 0
        self.fminutos = 0
        self.fsegundos = 0

    def tocar(self,fhoras,fminutos,fsegundos):
       self.fhoras = fhoras
       self.fminutos = fminutos
       self.fsegundos = fsegundos


    def run(self):
        while True:
            sleep(1)  
            self.segundos += 1
            self.format_time()
            print(f"Segundo: {self.segundos}")
            if(self.fhoras == self.horas and self.minutos == self.fminutos and self.segundos == self.fsegundos):
                print("Despertou o Alarme")
                break

    

    def format_time(self):
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
        if self.horas >= 24:
            self.horas = 0


