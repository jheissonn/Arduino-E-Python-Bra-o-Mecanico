from tkinter import * # importa as bibliotecas necessárias
import serial
import struct


conexao = serial.Serial("COM3",9600) #inicia a conexão


# as funções de cada scale
def motor1(valor):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get()))#manda as informações para o arduino
def motor2(valor1):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get()))
def motor3(valor2):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get())) 
 
def sair(): #uma função para sair da janela
   conexao.close() 
   janela.destroy() 

 
janela = Tk() 
janela.geometry("400x300+200+200")
janela.mainloop() 

 
motora = Scale( janela, from_=0, to=180, command =motor1, width=9,  )
motora.pack(anchor=CENTER)

motorb = Scale( janela, from_=0, to=180, command =motor2, width=50  )
motorb.pack(anchor=CENTER)

motorc = Scale( janela, from_=0, to=180, command =motor3, width=10  )
motorc.pack(anchor=CENTER)

b = Button(janela, text ='Exit', command = sair)
b.pack()

