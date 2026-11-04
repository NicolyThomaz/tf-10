class MiniGit:
    __slots__ = (
        "__pais",
        "__mensagens",
        "__branches",
        "__branch_atual",
        "__contador",
        "__passos"
    )

    def __init__(self):
        self.__pais = {}
        self.__mensagens = {}
        self.__branches = {"main": None}
        self.__branch_atual = "main"
        self.__contador = 0
        self.__passos = 0

    def commitar(self, mensagem):
        if not mensagem:
            raise ValueError('A mensagem não pode ser vazia.')

        self.__contador += 1
        identificador = f"c{self.__contador}"

        commit_anterior = self.__branches[self.__branch_atual]

        pais_do_commit = []

        if commit_anterior is not None:
            pais_do_commit.append(commit_anterior)

        self.__pais[identificador] = pais_do_commit
        self.__mensagens[identificador] = mensagem

        self.__branches[self.__branch_atual] = identificador

        self.__passos = 2

        return identificador

    def mensagem(self, identificador):
        self.__passos = 1

        if identificador not in self.__mensagens:
            raise ValueError("Commit não encontrado.")

        return self.__mensagens[identificador]

    def pais(self, identificador):
        self.__passos = 1

        if identificador not in self.__pais:
            raise ValueError("Commit não encontrado")

        return tuple(self.__pais[identificador])

    @property
    def passos(self):
        return self.__passos