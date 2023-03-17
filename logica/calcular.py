class Calcular:
    def __init__(self, dificuldade: int, /) -> None:
        from random import shuffle, choice
        self.__dificuldade: int = dificuldade
        self.__operacoes: list = ['+', '-', '*']
        shuffle(self.__operacoes)
        self.__operacao: str = choice(self.__operacoes)
        self.__valor1 = self.__gerar_valor()
        self.__valor2 = self.__gerar_valor()
        self.__resultado: int = self.__gerar_resultado()

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
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def resultado(self) -> int:
        return self.__resultado

    def __gerar_valor(self) -> int:
        from random import randint

        if self.dificuldade == 1:
            if self.operacao == '+' or self.operacao == '-':
                return randint(1, 50)
            else:
                return randint(1, 10)
        elif self.dificuldade == 2:
            if self.operacao == '+' or self.operacao == '-':
                return randint(1, 100)
            else:
                return randint(2, 15)
        elif self.dificuldade == 3:
            if self.operacao == '+' or self.operacao == '-':
                return randint(1, 200)
            else:
                return randint(2, 20)
        elif self.dificuldade == 4:
            if self.operacao == '+' or self.operacao == '-':
                return randint(1, 1000)
            else:
                return randint(3, 50)
        else:
            return randint(3, 100_000)

    def __gerar_resultado(self) -> int:
        if self.__operacao == '+':
            return self.valor1 + self.valor2
        elif self.__operacao == '-':
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    def checar_resultado(self, resultado: int) -> bool:
        print(f'{self.valor1} {self.operacao} {self.valor2} = {self.resultado}')
        if self.__resultado == resultado:
            print('Parabéns você acertou!')
            return True
        else:
            print('Resposta Errada :(')
            print('Na próxima você vai conseguir!')
            return False

    def mostrar_operacao(self) -> None:
        print(f'Operação: {self.valor1} {self.operacao} {self.valor2} = ?')

    def __str__(self) -> str:
        return f'Dificuldade: {self.dificuldade} \nOperações Disponíveis: {self.operacoes} ' \
               f'\nOperação: {self.operacao} \nValor1: {self.valor1} \nValor2: {self.valor2}'
