class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme("vingadores - ultimato", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(
    f"Nome: {vingadores.nome} - Ano: {vingadores.ano}"
    f" - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}"
)

umbrella_academy = Serie("umbrella academy", 2018, 2)
umbrella_academy.dar_like()
umbrella_academy.dar_like()
print(
    f"Nome: {umbrella_academy.nome} - Ano: {umbrella_academy.ano}"
    f" - Temporadas: {umbrella_academy.temporadas}"
    f" - Likes: {umbrella_academy.likes}"
)
