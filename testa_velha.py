import velha

# No começo do teste de cada caso, os outros testes foram comentados para uma melhor leitura do problema propostp. 

l1 = [1,1,1]
l2 = [2,2,2]
l3 = [1,2,1]

# def test_Xganhou():
 #    assert 1 == velha.velha(l1,l2,l3)

# def test_Oganhou(): #unico caso possível em que o O ganha é na diagonal.
  #  assert 2 == velha.velha(l1,l2,l3)

# def test_JogoEmpatado(): 
   #assert 0 == velha.velha(l1,l2,l3)

def test_JogoImpossivel():
    assert -2 == velha.velha(l1,l2,l3)