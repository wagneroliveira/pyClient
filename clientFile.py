# coding: iso-8859-1 -*-

import sys

dataFile = 'cliente.txt'

# List

def listCustomers():
    print("LISTAGEM DE CLIENTES:")

    f = open(dataFile, "r")

    lines = f.readlines()

    for line in lines:
        line = line.strip()

        # print(line)

        info = line.split('|')

        print('CPF: ' + info[0])
        print('Nome: ' + info[1])
        print('Fone: ' + info[2])
        print('Endereco: ' + info[3])
        print('-----------------')

    f.close()

    return f

# Search item and print

def searchCustomer():
    print("PESQUISAR CLIENTE:")

    cpf = input("Informe o CPF do cliente: ")
    print('--------------------------')

    f = open(dataFile, "r")

    lines = f.readlines()

    for index in range(len(lines)):
        line = lines[index].strip()

        info = line.split('|')

        if (info[0] == cpf):
            print('Registro encontrado.')
            print('*********************')
            print('CPF: ' + info[0])
            print('Nome: ' + info[1])
            print('Phone: ' + info[2])
            print('Endereco: ' + info[3])
            print('*********************')

            break

    f.close()

def addCustomer():
    print("CADASTRAR NOVO CLIENTE:")
    # Add item

    cpf = input("Informe o CPF: ")
    name = input("Informe o nome: ")
    phone = input("Informe o telefone: ")
    address = input("Informe o endereco: ")

    recordStr = cpf + '|' + name + '|' + phone + '|' + address + "\n"

    # Write to file

    f = open(dataFile, "a+")

    f.write(recordStr)

    f.close()


# Search item and delete it

def deleteCustomer():
    print("EXCLUIR CLIENTE")

    cpf = input("Informe o CPF para exclusao do cliente: ")

    cpf = cpf.strip()

    f = open(dataFile, "r")

    lines = f.readlines()

    for index in range(len(lines)):
        line = lines[index].strip()

        info = line.split('|')

        if (info[0] == cpf):
            print('********* Excluindo cliente com CPF: ' + cpf)

            lines.pop(index)

            break

    f.close()

    f = open(dataFile, "w")

    f.writelines(lines)

    f.close()

# Main

while (1):
    print("Opcoes:")
    print("1 - Cadastrar novo cliente")
    print("2 - Listagem de clientes")
    print("3 - Pesquisar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair da aplicacao")

    option = input("Opcoes: ")

    print('')

    if (option == "1"):

        addCustomer()

    elif (option == "2"):

        listCustomers()

    elif (option == "3"):

        searchCustomer()

    elif (option == "4"):

        deleteCustomer()

    elif (option == "5"):

        break
