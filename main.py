#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, sys, select

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.setblocking(False)

serverAddr = ("192.168.1.4", 667)

def mensagem():
    # Verifica se foi digitado algo
    if select.select([sys.stdin,],[],[],0.0)[0]:
        # Formata a string para mandar "Cliente: <entrada>"
        entrada = "Cliente: {}".format(sys.stdin.readline())
        entrada = entrada.encode('utf-8')

        return entrada
    return False

try:
    while 1:
        try:
            msg, friend = cliente.recvfrom(1024)
            # friend[0] - IP / friend[1] - porta

            # rstrip() é para eliminar a quebra de linha
            msg = msg.decode('utf-8').rstrip()
            print("{}: {}".format(friend[0], msg))
        except:
            pass

        try:
            entrada = mensagem()
            if(entrada != False):
                cliente.sendto(entrada, serverAddr)

        except KeyboardInterrupt:
            sys.exit("\nChat encerrado!")

    cliente.close()

except Exception as erro:
    print("O erro foi: {}".format(erro))
    client.close()