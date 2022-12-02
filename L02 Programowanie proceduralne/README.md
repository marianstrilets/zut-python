#

## Laboratorium 2. Ćwiczenia w programowaniu proceduralnym

### Krotki (tuple) i listy (list)

**Krotka (tupla)** pozwala na przechowywanie kilku wartoćci (mogą mieć one różne typy) w jednej zmiennej, przy czym po utworzeniu tupli nie można już tych wartości zmodyfikować. Stosuje się je najczęściej jako argumenty funkcji, lub do zwrócenia kilku wartości z funkcji. W przypadku drugiej opcji pozwala to na proste rozdzielenie (rozpakowanie) zwróconych wartości do kilku zmiennych.

```python
>>> b = (5, 'a', 1.0)
>>> type(b)
<class 'tuple'>

>>>print(b[0])
5
```

**Listy** w przypadku języka Python są podstawową strukturą tablicową. W przeciwieństwie do tablic znanych z języka C++ pozwalają one jednak na przechowywanie wartości różnych typów. Umożliwiają one także dynamiczne dodawanie nowych wartości. Różnice są widoczne także w samej ich obsłudze, możliwe jest np. wybranie danych z podanego zakresu indeksów **(początek:koniec:krok)**.

```python
>>> c = [5, 'a', 1.0]
>>> type(c)
<class 'list'>

>>> c.append(77)
>>> print(c)
[5, 'a', 1.0, 77]

>>> print(1:3)
['a', 1.0]
```

---

### Moduły oraz pakiety

**Moduły** w Pythonie są zbiorem funkcji zapisanych w pliku "nazwa_modulu.py". W celu załadowania funkcji z utworzonego modułu stosuje się polecenie **import**.

```python
    import math
    print(math.pi)
```

**Pakiety** są natomiast przestrzeniami nazw zawierającymi wiele modułów. Aby zaimportować moduł z pakietu możemy skorzystać z jednej z dwóch metod:

```python
    import pakiet.modul      #metoda 1
    from pakiet import modul #metoda 2
```

Jeśli nie chcemy poprzedzać nazwy funkcji pełnymi nazwami modułów, możemy użyć komendy **as** i podać własną nazwę pod którą dostępne będą zaimportowane obiekty:

```python
    import math as m
    print(m.pi)
```

Aby zaimportować zawartość modułu do aktualnej przestrzeni nazw możemy zastosować poniszą komendę:

```python
    from math import *
    print(pi)
```

---

**Zadanie 1.** Utwórz listę zawierającę 6 elementów [0, −2, 1, 7, 3, 4] a następnie wypisz jej zawartość w odwrotnej kolejności, bez stosowania funkcji, zy pętli.

---

**Zadanie 2.**  Zaimportuj moduł matematyczny, a następnie napisz skrypt którzy pobierze wartości dla dwóch zmiennych x, y i wyznaczy oraz wyświetli wartość, dla podanej funkcji:

---

**Zadanie 3.**  Napisz skrypt, który pobierze od użytkownika trzy wartości x, y, z oraz numer opcji c. Jeśli c == 1 zwróć ich sumę, jeżeli c == 2 różnicę, dla c == 3 iloczyn, a w przeciwnym razie iloraz. Upewnij się, że nie dojdzie do dzielenia przez 0, jeśli taka sytuacja miała by miejsce, wyświetl odpowiedni komunikat.

---
**Zadanie 5.** Napisz program drukujący na ekranie trójkąt o wysokośći podanej przez użytkownika. Przykładowy trójkąt o wysokości 4

---

**Zadanie 6.** Utwórz poniższą macierz, wykorzystując jedną linijkę kodu (dwie pętlę for inicjalizujące listę):

```python
[[1, 4, 7], [1, 4, 7], [1, 4, 7]]
```

---
**Zadanie 7.** Napisz program, który znajdzie i wy±wietli n pierwszych liczb pierwszych (zakładając, że pierwszą liczbą pierwszą jest liczba 2).

---

**Zadanie 8.** Napisz program, który wyznaczy i wyświetli na ekranie sumę liczb naturalnych mniejszych od n (liczba n podawana jest przez użytkownika), które są zakończone liczbą 3 lub 14

---
