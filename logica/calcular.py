class Calcular:
    def __init__(self, dificuldade: int, /) -> None:
        from random import shuffle, choice
        self.__dificuldade: int = dificuldade
        self.__operacoes: list = ['+', '-', '*']
        shuffle(self.__operacoes)
        self.__operacao: str = choice(self.__operacoes)
        self.__formula: tuple = self.__gera_formula()

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def operacoes(self) -> list:
        return self.__operacoes

    @property
    def operacao(self) -> str:
        return self.__operacao

    @property
    def formula(self) -> tuple:
        return self.__formula

    def __gera_formula(self) -> tuple:
        from random import randint

        if self.__dificuldade == 1:
            n1 = randint(1, 50)
            n2 = randint(1, 50)

            if self.__operacao == '+':
                return n1, n2, '+'
            elif self.__operacao == '-':
                return n1, n2, '-'
            else:
                n1 = randint(1, 10)
                n2 = randint(1, 10)

                return n1, n2, '*'

        elif self.__dificuldade == 2:
            n1 = randint(2, 100)
            n2 = randint(2, 100)

            if self.__operacao == '+':
                return n1, n2, '+'
            elif self.__operacao == '-':
                return n1, n2, '-'
            else:
                n1 = randint(1, 15)
                n2 = randint(1, 15)

                return n1, n2, '*'
        elif self.__dificuldade == 3:
            n1 = randint(1, 200)
            n2 = randint(1, 200)

            if self.__operacao == '+':
                return n1, n2, '+'
            elif self.__operacao == '-':
                return n1, n2, '-'
            else:
                n1 = randint(2, 20)
                n2 = randint(2, 20)

                return n1, n2, '*'
        elif self.__dificuldade == 4:
            n1 = randint(1, 1000)
            n2 = randint(1, 1000)

            if self.__operacao == '+':
                return n1, n2, '+'
            elif self.__operacao == '-':
                return n1, n2, '-'
            else:
                n1 = randint(3, 50)
                n2 = randint(3, 50)

                return n1, n2, '*'
        else:
            print('Dificuldade Inválida!')
            return 0, 0, '+'

    def mostrar_operacao(self) -> None:
        print(f'Operação: {self.__formula[0]} {self.__formula[2]} {self.__formula[1]}')

    def checar_resultado(self, resultado: int) -> bool:
        if self.__formula[2] == '+':
            if (self.__formula[0] + self.__formula[1]) == resultado:
                return True
            else:
                return False
        elif self.__formula[2] == '-':
            if (self.__formula[0] - self.__formula[1]) == resultado:
                return True
            else:
                return False
        else:
            if (self.__formula[0] * self.__formula[1]) == resultado:
                return True
            else:
                return False

    def __str__(self) -> str:
        return f'Dificuldade: {self.__dificuldade} \nOperações Disponíveis: {self.__operacoes} ' \
               f'\nOperação: {self.__operacao} \nOperação: {self.__formula}'
