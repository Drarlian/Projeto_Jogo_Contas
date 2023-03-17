def game(pontos: int) -> None:
    from logica.calcular import Calcular

    print('Opções de dificuldade: | 1 | 2 | 3 | 4 |')
    dificuldade: int = verifica_dificuldade('Digite a dificuldade: ')

    calc: Calcular = Calcular(dificuldade)

    print(f' Dificuldade: {dificuldade} '.center(60, '-'))

    calc.mostrar_operacao()
    resposta: int = verifica_int('Digite a resposta da operação: ')

    if calc.checar_resultado(resposta):
        pontos += 1

    print(f'Você tem {pontos} ponto(s).')
    print('-' * 60)

    while True:
        decisao: str = verifica_decisao('Deseja continuar jogando? [S/N] ')
        if decisao == 'S':
            game(pontos)
        elif decisao == 'N':
            print('Fim de Jogo!')
            print('Obrigado por Jogar!')
            print(f'Pontuação final: {pontos}')
            print('-' * 60)
            exit()
        else:
            print('Digite uma opção válida!')


def verifica_int(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
        except (TypeError, ValueError):
            print('Digite uma opção válida!')
        except KeyboardInterrupt:
            print('\nO usuário escolheu não continuar.')
            exit()
        else:
            return valor


def verifica_dificuldade(mensagem):
    while True:
        valor = verifica_int(mensagem)
        if 1 <= valor <= 4:
            return valor
        print('Digite uma dificuldade válida!')
        print('Opções de dificuldade: | 1 | 2 | 3 | 4 |')


def verifica_decisao(mensagem: str) -> str:
    while True:
        try:
            opcao = str(input(mensagem)).strip().upper()[0]
        except (TypeError, ValueError):
            print('Digite uma opção válida!')
        except KeyboardInterrupt:
            print('\nO usuário escolheu não continuar.')
            exit()
        else:
            if opcao == 'S' or opcao == 'N':
                return opcao
            else:
                print('Digite uma opção válida!')

def main() -> None:
    pontos = 0
    game(pontos)
