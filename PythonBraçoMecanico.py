from tkinter import * #importa as bibliotecas necessárias 
import serial
import struct

conexao = serial.Serial("COM3",9600)# inicia a conexao


 
def motor1(valor):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get()))
def motor2(valor1):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get()))
def motor3(valor2):
    conexao.write(struct.pack('>BBB',motora.get(),motorb.get(),motorc.get())) 

 

 
def sair(): 
   conexao.close() 
   janela.destroy() 

 
janela = Tk() 
janela.geometry("400x300+200+200")
 

 
motora = Scale( janela, from_=0, to=180, command =motor1, width=10,  )
motora.place(x=250,y=50)

motorb = Scale( janela, from_=40, to=180, command =motor2, width=20  )
motorb.place(x=150,y=50)

motorc = Scale( janela, from_=0, to=180, command =motor3, width=30  )
motorc.place(x=50,y=50)

b = Button(janela, text ='sair', command = sair)
b.pack()

janela.mainloop() 
