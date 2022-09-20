from time import sleep
from alarme import Alarme
from cronometro import Cronometro
from relogio import Relogio


# Puxando a classe Relogio para Variável Relógio
relogio = Relogio()
# Iniciando a Thread relogio
relogio.start()

option = 0

def menu(option):
    while option < 7:
            
        print('''[ Menu com Opções ]\n''')
        print('''[ 0 ] - Ajustar Horário''')
        print('''[ 1 ]- Visualizar Horário''')
        print('''[ 2 ]- Iniciar Cronômetro''')
        print('''[ 3 ]- Parar Cronômetro e Mostrar valor atual''')
        print('''[ 4 ]- Zerar Cronômetro''')
        print('''[ 5 ]- Definir Alarme''')
        print('''[ 6 ]- Continuar Cronômetro\n''')
        
        option = int(input('Escolha uma das Opções:'))
        
        if option == 0:
            relogio.showTime()
            horas = int(input("Informe um valor de tempo hora: "))
            minutos = int(input("Informe um valor de tempo minuto: "))
            segundos = int(input("Informe um valor de tempo segundo: "))
            relogio.setupTime(horas, minutos, segundos)
            relogio.showTime()
            sleep(1)
                    
        elif option == 1:
            relogio.showTime()
            sleep(1)
                    
        elif option == 2:
            # Puxa a classe cronometro para poder inicar a Thread
            cronometro = Cronometro()
            # Inicia a Thread
            cronometro.start()
            # Inicia o Cronometro
            cronometro.initCronometro()
            print("Inicializou cronometro")
            sleep(1)
                    
        elif option == 3:
            print("Pausando cronometro em: ")
            cronometro.pause()
            cronometro.showTime()
            sleep(1)
            
        elif option == 4:
            print("Reiniciando cronometro a partir de: ")
            cronometro.showTime()
            cronometro.restart()
            sleep(1)
            
        elif option == 5:
            relogio.showTime()
            fhoras = int(input("Informe um valor de tempo hora: "))
            fminutos = int(input("Informe um valor de tempo minuto: "))
            fsegundos = int(input("Informe um valor de tempo segundo: "))
            h,m,s = relogio.returnTime()
            alarme = Alarme(h,m,s)
            alarme.tocar(fhoras,fminutos,fsegundos)
            alarme.start()
            sleep(1)
            
        
        elif option == 6:
            cronometro.resume()
            cronometro.showTime()
            sleep(1)
            
        else:
            print("Saindo do Menu")
            sleep(1)
           

if __name__ == '__main__':
    print("\n")
    print("Inicializou \n")
    menu(option)

