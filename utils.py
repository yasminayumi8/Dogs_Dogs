import uuid

from models import Veterinario, db_session, Consulta, Animal, Cliente
from sqlalchemy import select

#def chamar_func(tabela):
   # inserir_tabela()

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def inserir_veterinario():
    veterinario = Veterinario(salario2=float(input('Insira o salario do veterinario: ')),
                              nomeVet=str(input('Insira o nome do veterinario: ')),
                              crmv=int(input('Insira o ID do crmv: ')),
                              v_consulta1=float(input('Insira o valor da consulta : '))
                              )
    print(veterinario)
    veterinario.save()

def consultar_veterinario():
    var_vet = select(Veterinario)
    var_vet = db_session.execute(var_vet).all()
    print(var_vet)


def atualizar_veterinario():
    var_vet = select(Veterinario).where(Veterinario.nomeVet == str(input('Nome do veterinario: ')))
    var_vet = db_session.execute(var_vet).scalar()
    print(var_vet)
    var_vet.nome = str(input('Novo Nome: '))
    var_vet.save()


def deletar_veterinario():
    var_vet = select(Veterinario).where(str(input('Novo Nome: ')) == Veterinario.nomeVet)
    var_vet = db_session.execute(var_vet).scalar()
    var_vet.delete()

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

def inserir_consulta():

    consulta = Consulta(motivo_id2=str(input('Insira o motivo da consulta: ')),
                        hora=str(input('Insira o hora da consulta: ')),
                        minuto=str(input('Insira o minuto da consulta: ')),
                        data1=int(input('Insira o data da consulta: ')),
                        idVeterinario=int(input('Insira o ID do veterinario: ')),
                        idAnimal2=int(input('Insira o ID do animal do veterinario: '))
                       )
    print(consulta)
    consulta.save()


def consultar_consulta():
    var_consulta = select(Consulta)
    var_consulta = db_session.execute(var_consulta).all()
    print(var_consulta)


def atualizar_consulta():
    var_consulta = select(Consulta).where(str(input('Motivo: ')) == Consulta.motivo_id2)
    var_consulta = db_session.execute(var_consulta).scalar()
    print(var_consulta)
    var_consulta.nome = str(input('Novo motivo: '))
    var_consulta.save()


def deletar_consulta():
    var_consulta = select(Consulta).where(str(input('novo motivo: ')) == Consulta.motivo_id2)
    var_consulta = db_session.execute(var_consulta).scalar()
    var_consulta.delete()

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def inserir_animal():
    animal = Animal(nome_animal=str(input('Insira o nome do animal : ')),
                    raca1=str(input('Insira o Raça  : ')),
                    anoNasci=int(input('Insira o ano do nascimento')),
                    idCliente3=int(input('Insira o ID do cliente : ')),
                    )
    print(animal)
    animal.save()


def consultar_animal():
    var_animal = select(Animal)
    var_animal= db_session.execute(var_animal).all()
    print(var_animal)


def atualizar_animal():
    var_animal = select(Animal).where(str(input('Nome do animal: ')) == Animal.nome_animal)
    var_animal = db_session.execute(var_animal).scalar()
    print(var_animal)
    var_animal.nome = str(input('Novo Nome: '))
    var_animal.save()


def deletar_animal():
    var_animal = select(Animal).where(str(input('Novo Nome: ')) == Animal.nome_animal)
    var_animal = db_session.execute(var_animal).scalar()
    var_animal.delete()

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


def inserir_cliente():
    cliente = Cliente(CPF=str(input('Insira o CPF do cliente: ')),
                      Nome1=str(input('Insira o nome do cliente: ')),
                      telefone=str(input('Insira o telefone do cliente: ')),
                      profissao=str(input('Insira o profissao do cliente: ')),
                      area=str(input('Insira o area do cliente: '))
                      )
    print(cliente)
    cliente.save()


def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).all()
    print(var_cliente)


def atualizar_cliente():
    var_cliente = select(Cliente).where(str(input('Nome: ')) == Cliente.Nome1)
    var_cliente = db_session.execute(var_cliente).scalar()
    print(var_cliente)
    var_cliente.nome = str(input('Novo Nome: '))
    var_cliente.save()


def deletar_cliente():
    var_cliente = select(Cliente).where(str(input('Novo Nome: ')) == Cliente.Nome1)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()


if __name__ == '__main__':

    while True:
        print('Oque você deseja modificar?')
        print('1.  Veterinario')
        print('2.  Consulta')
        print('3.  Animal')
        print('4.  Cliente')
        print('5. Sair')
        numero = input("Escolha: ")

        if numero == '1':
           print("MENU")
           print("1 -Inserir veterinario")
           print("2 -Consultar veterinario")
           print("3 -Atualizar veterinario")
           print("4 -Deletar veterinario")
           print("5 -Sair")
           escolha = input("escolha: ")
           if escolha == "1":
               inserir_veterinario()
           elif escolha == "2":
               consultar_veterinario()
           elif escolha == "3":
               atualizar_veterinario()
           elif escolha == "4":
               deletar_veterinario()
           elif escolha == "5":
               break

        elif numero == '2':
            print("MENU")
            print("1 -Inserir consulta")
            print("2 -Consultar consulta")
            print("3 -Atualizar consulta")
            print("4 -Deletar consulta")
            print("5 -Sair")
            escolha = input("escolha: ")
            if escolha == "1":
                inserir_consulta()
            elif escolha == "2":
                consultar_consulta()
            elif escolha == "3":
                atualizar_consulta()
            elif escolha == "4":
                 deletar_consulta()
            elif escolha == "5":
                break

        elif numero == '3':
            print("MENU")
            print("1 -inserir animal")
            print("2 -Consultar animal")
            print("3 -Atualizar animal")
            print("4 -Deletar animal")
            print("5 -Sair")
            escolha = input("escolha: ")
            if escolha == "1":
                inserir_animal()
            elif escolha == "2":
                consultar_animal()
            elif escolha == "3":
                atualizar_animal()
            elif escolha == "4":
                deletar_animal()
            elif escolha == "5":
                break

        elif numero == '4':
            print("MENU")
            print("1 -inserir cliente")
            print("2 -Consultar cliente")
            print("3 -Atualizar cliente")
            print("4 -Deletar cliente")
            print("5 -Sair")
            escolha = input("escolha: ")
            if escolha == "1":
               inserir_cliente()
            elif escolha == "2":
                consultar_cliente()
            elif escolha == "3":
                atualizar_cliente()
            elif escolha == "4":
                deletar_cliente()
            elif escolha == "5":
                break
