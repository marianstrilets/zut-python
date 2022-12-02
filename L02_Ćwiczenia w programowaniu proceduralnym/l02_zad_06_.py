
'''
Utwórz poniższą macierz, wykorzystuj¡c jedną linijkę kodu 
(dwie pętlę for inicjalizujące listę): [[1, 4, 7], [1, 4, 7], [1, 4, 7]]
'''

l = [ [ i for i in range(1,8,3)] for j in range(3) ]
print(l)