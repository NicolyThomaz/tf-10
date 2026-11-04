# MiniGit
O projeto simula funcionalidade básicas do Git, como a criação de commits, branches, histórico e merge

## Medição: leitura x escrita

| Commits | Passos do commitar | Passos do log |
|---------|--------------------|---------------|
| 10      | 2                  | 10            |
| 100     | 2                  | 100           |
| 1000    | 2                  | 1000          |

## 1. Por que o commitar gasta sempre 2 passos, e o log gasta mais conforme o historico cresce? (leitura x escrita)

O commitar precisa criar o commit e atualizar o ponteiro da branch, por isso sempre gasta 2 passos. O log percorre os commits do histórico, então a quantidade de passos é determinada pela quantidade de commits.

## 2. Por que mensagem(commit) gasta 1 passo e buscar(texto) pode gastar muitos? O que o dicionario ganha quando se procura pela chave, e o que ele nao ajuda quando se procura pelo valor?

A mensagem procura pela chave no dicionário. O buscar procura pelo texto dentro das mensagens, sendo necessário verificar os valores até encontrar o resultado. 

## 3. Por que o merge e um commit com dois pais, e por que isso faz do historico um grafo, e nao uma lista?

O merge junta duas branches em um commit, que precisa guardar os dois commits anteriores como pais. Por isso, o histórico não segue uma sequência única, podendo ter diferentes caminhos e formando um grafo, e não uma lista.

## 4. Por que o metodo pais devolve uma tupla, e nao a lista que esta guardada dentro do dicionario?

A tupla não permite alterações depois de criada, protegendo a lista original contra modificações externas.