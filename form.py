import requests

class Sitema:
    def __init__(self):
        self.lista_form = []

    def menu_principal(self):
        print('='*30)
        print('BEM VINDO A NOSSA PLATAFORMA')
        print('='*30)
        print('1- Cadastrar formulário\n2- Visualizar formulários\n3- Ediar formulários')
        try:
            opcao = int(input('\nQual opção você deseja: '))
        except ValueError:
            print('\nVocê digitou o valor errado!!!\ndigite um número inteiro entre 1 e 3')
            opcao = int(input('\nQual opção você deseja: '))
        
        if opcao == 1:
            self.cadastrar_form()
        elif opcao == 2:
            self.visualizar_form()
        elif opcao == 3:
            self.editar_form()
    
    def cadastrar_form(self):
        form = []
        print('-=-'*8)
        print('CADASTRAR O FORMULARIO')
        print('-=-'*8)
        nome = input('Nome: ')
        email = input('E-mail: ')
        cpf_cnpj = int(input('CPF ou CNPJ: '))
        telefone = int(input('Telfone: '))
        cep = input('CEP: ')

        url = f'https://ws.apicep.com/cep/{cep}.json'
        r = requests.get(url)
        r = r.json()

        if r['status'] == 400:
            msg =r['message']
            print(f'{msg}, digite novamente')

        elif r['status'] == 200:
            logradouro = r['address']
            bairro = r['district']
            cidade = r['city']
            estado = r['state']
            print(f'\nLogradou: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}')
            print('Digite o número para concluir o cadastro')
            try:
                num = int(input('Número: '))
            except ValueError:
                print('\nVocê digitou um texto digite um número por favor.')
                num = int(input('Número: '))
            print('\nParabéns cadastro feito com sucesso!!!')

            form.append(nome)
            form.append(email)
            form.append(cpf_cnpj)
            form.append(telefone)
            form.append(cep)
            form.append(logradouro)
            form.append(bairro)
            form.append(cidade)
            form.append(estado)
            form.append(num)
            self.lista_form.append(form)

        while True:
            voltar = int(input('\nPara voltar ao menu dgite 1: '))
            if voltar == 1:
                self.menu_principal()
                break
            else:
                print('Não digite letras tem que ser o 1')


    
    def visualizar_form(self):
        qtd = len(self.lista_form)
        print('-=-'*8)
        print('VISUALIZAR OS FORMULARIOS')
        print('-=-'*8)
        print(f'1- Visualizar todos os formulários\n2- Visualizar por id\nTotal de formulários é {qtd}')
        opcao = int(input('\nDigite qual opção você deseja: '))
        if opcao == 1:
            cont = 0
            if len(self.lista_form) == 0:
                print('Não tem nenhum formulário')
            else:
                for x in self.lista_form:
                    cont += 1
                    print('='*20)
                    print('id formulario: ',cont)
                    print('Nome: ', x[0])
                    print('E-mail: ', x[1])
                    print('CPF/CNPJ: ', x[2])
                    print('Telefone: ',x[3])
                    print('CEP: ', x[4])
                    print('Logradouro: ',x[5])
                    print('Número: ',x[9])
                    print('Bairro: ',x[6])
                    print('Cidade: ', x[7])
                    print('Estado: ',x[8],)
                    
        if opcao == 2:
            try:
                opcao2 = int(input('Digite um id: '))
            except IndexError:
                print(f'Digite um valor entre 1 e {qtd}')
                opcao2 = int(input('Digite um id: '))
            except ValueError:
                print('Digite um numero inteiro!')
                opcao2 = int(input('Digite um id: '))

            if opcao2 == 1:
                x = self.lista_form[0]
                print('='*20)
                print('Nome: ', x[0])
                print('E-mail: ', x[1])
                print('CPF/CNPJ: ', x[2])
                print('Telefone: ',x[3])
                print('CEP: ', x[4])
                print('Logradouro: ',x[5])
                print('Número: ',x[9])
                print('Bairro: ',x[6])
                print('Cidade: ', x[7])
                print('Estado: ',x[8],)
            elif opcao2 > 1:
                x = self.lista_form[opcao2-1]
                print('='*20)
                print('Nome: ', x[0])
                print('E-mail: ', x[1])
                print('CPF/CNPJ: ', x[2])
                print('Telefone: ',x[3])
                print('CEP: ', x[4])
                print('Logradouro: ',x[5])
                print('Número: ',x[9])
                print('Bairro: ',x[6])
                print('Cidade: ', x[7])
                print('Estado: ',x[8],)
        while True:
            voltar = int(input('\nPara voltar ao menu dgite 1: '))
            if voltar == 1:
                self.menu_principal()
                break
            else:
                print('Não digite letras tem que ser o 1')

    def editar_form(self):
        qtd = len(self.lista_form)
        print('-=-'*8)
        print('EDITAR OS FORMULARIOS')
        print('-=-'*8)
        print('1- remover formulario\n2- Editar formulário')
        opcao = int(input('Qual opação você deseja: '))
        if opcao == 1:
            print(f'id´s disponiveis esta entre 1 e {qtd}')
            num_id = int(input('Digite o número do id: '))
            if num_id == 1:
                num_id = 0
            else:
                num_id = num_id-1
            self.lista_form.pop(num_id)
            print('Formulário excluido com sucesso!!')
        elif opcao == 2:
            print(f'id´s disponiveis esta entre 1 e {qtd}')
            num_id = int(input('Digite o número do id: '))
            if num_id == 1:
                num_id = 0
            else:
                num_id = num_id-1
            
            campo = input('Digite o campo ex(nome, telefone): ').lower()
            if campo == 'nome':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][0] = valor
            elif campo == 'e-mail':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][1] = valor
            elif campo == 'telefone':
                valor = int(input('digite o novo valor: '))
                self.lista_form[num_id][2] = valor
            elif campo == 'cnpj' or 'cpf':
                valor = int(input('digite o novo valor: '))
                self.lista_form[num_id][3] = valor
            elif campo == 'cep':
                valor = int(input('digite o novo valor: '))
                self.lista_form[num_id][4] = valor
            elif campo == 'logradouro':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][5] = valor
            elif campo == 'número':
                valor = int(input('digite o novo valor: '))
                self.lista_form[num_id][9] = valor
            elif campo == 'bairro':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][6] = valor
            elif campo == 'cidade':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][7] = valor
            elif campo == 'estado':
                valor = input('digite o novo valor: ')
                self.lista_form[num_id][8] = valor
        while True:
            voltar = int(input('\nPara voltar ao menu dgite 1: '))
            if voltar == 1:
                self.menu_principal()
                break
            else:
                print('Não digite letras tem que ser o 1')
            

     
sis = Sitema()
sis.menu_principal()
