import velha

l1 = [2,1,2]
l2 = [1,2,1]
l3 = [1,1,2]

# def test_Xganhou():
 #    assert 1 == velha.velha(l1,l2,l3)

def test_Oganhou(): #unico caso possível em que o O ganha é na diagonal.
    assert 2 == velha.velha(l1,l2,l3)


