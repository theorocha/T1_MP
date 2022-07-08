# T1_MP
Theo Marques da Rocha - 190038489

LINK do Repositório do GitHub com todos os  15 commits de casos de teste. -> https://github.com/theorocha/T1_MP.git 


Desenvolvi o projeto em python no VScode, importanto o velha.py dentro do arquivo de testes testa_velha.py. A compilação e execução foram realizadas dentro do próprio VScode usando o atalho CTRL + SHIFT + N para desenvolvimento do código principal. Para os casos de testes, foi usada a biblioteca PYTEST, e testes foram executados no terminal usando o comando pytest testa_velha.py, conforme a foto em anexo.

O projeto foi desenvolvido orientado a testes, usando o linter PYLINT a cada etapa de desenvolvimento. Os teste  foram realizados um por um conforme os resultados esperados e estando bem explicados cada etapa em cada commit.

Apenas um esclarecimento: um jogo foi considerado indefinido quando ainda existem jogadas a serem feitas... Após todas as jogadas forem realizadas, aí sim ocorre
a checagem se um jogo é impossível ou não. EX: 2 2 2  é um jogo impossível e indefinido(ainda existem lacunas a serem preenchidas). Pelo fato de o retorno ser único,
                                               0 1 2
                                               0 2 2
o indefinido precedeu o impossível em minha implementação.
