from collections import deque

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

    def criar_branch(self, nome):
        self.__passos = 1

        if nome in self.__branches:
            raise ValueError("Essa branch já existe")

        commit_atual = self.__branches[self.__branch_atual]

        if commit_atual is None:
            raise ValueError("Não existem commits no repositório")

        self.__branches[nome] = commit_atual

    def trocar_branch(self, nome):
        self.__passos = 1

        if nome not in self.__branches:
            raise ValueError("Branch não encontrada")

        self.__branch_atual = nome

    def mesclar(self, nome):
        self.__passos = 2

        if nome not in self.__branches:
            raise ValueError("Branch não encontrada")

        if nome == self.__branch_atual:
            raise ValueError("Não é possível mesclar a própria branch")

        commit_atual = self.__branches[self.__branch_atual]
        commit_outra_branch = self.__branches[nome]

        self.__contador += 1
        identificador = f"c{self.__contador}"

        self.__pais[identificador] = [
            commit_atual,
            commit_outra_branch
        ]

        self.__mensagens[identificador] = f"merge de {nome}"

        self.__branches[self.__branch_atual] = identificador

        return identificador

    @property
    def branch_atual(self):
        return self.__branch_atual

    def log(self):
        commit_atual = self.__branches[self.__branch_atual]

        if commit_atual is None:
            self.__passos = 0
            return ()

        fila = deque([commit_atual])
        visitados = set()
        resultado = []

        while fila:
            identificador = fila.popleft()

            if identificador in visitados:
                continue

            visitados.add(identificador)
            resultado.append(identificador)

            for pai in self.__pais[identificador]:
                fila.append(pai)

        self.__passos = len(resultado)

        return tuple(resultado)

    def buscar(self, texto):
        self.__passos = 0

        for identificador in self.__mensagens:
            self.__passos += 1

            if texto in self.__mensagens[identificador]:
                return identificador

        return None

    def merges(self):
        self.__passos = 0
        resultado = []

        for identificador in self.__pais:
            self.__passos += 1

            if len(self.__pais[identificador]) > 1:
                resultado.append(identificador)

        return tuple(resultado)


def tentar(acao):
    try:
        acao()
    except ValueError as erro:
        print("erro:", erro)

git = MiniGit()

git.commitar("primeiro commit")
print(git.passos)

git.commitar("segundo commit")
git.criar_branch("feature")
print(git.passos)

git.commitar("terceiro commit")
git.trocar_branch("feature")
git.commitar("quarto commit")
git.trocar_branch("main")
git.mesclar("feature")

print(git.pais("c5"))
print(git.log(), git.passos)
print(git.mensagem("c3"), git.passos)
print(git.buscar("quarto"), git.passos)
print(git.merges())

git.trocar_branch("feature")
print(git.log(), git.passos)
git.trocar_branch("main")

tentar(lambda: git.trocar_branch("inexistente"))
tentar(lambda: git.criar_branch("main"))
tentar(lambda: git.mesclar("main"))
tentar(lambda: git.pais("c99"))

def medir(quantidade):
    git = MiniGit()

    for numero in range(quantidade):
        git.commitar(f"commit {numero}")

    passos_commitar = git.passos

    git.log()
    passos_log = git.passos

    return passos_commitar, passos_log

print()
print(f"{'commits':<10}{'passos do commitar':<22}{'passos do log'}")

for quantidade in (10, 100, 1000):
    passos_commitar, passos_log = medir(quantidade)

    print(f"{quantidade:<10}{passos_commitar:<22}{passos_log}")
