print ("Programa Gerenciador de Time")

def cadastratime():
    nomedapessoa=str(input("Digite o seu nome: "))
    nomedotime=str(input("Digite o nome do seu time: "))
    print (f"Olá, {nomedapessoa}, bem vindo ao gerenciador do seu time {nomedotime}")

def cadastrotitulares():
    entrada = input('Digite seus jogadores: ')
    vetor = entrada.split(',')
    print(vetor)

def main():
    cadastratime()
    cadastrotitulares()

if __name__ == "__main__":
    main()