#

## Laboratorium 3. Ćwiczenia w programowaniu proceduralnym

### Funkcje, parametry opcjonalne, argumenty nazwane i lambdy

Podobnie jak w przypadku C++ argumenty funkcji mogą posiadać domyślne wartości (możemy ominąć je wtedy przy wywoływaniu funkcji). To co odróżnia Pythona to parametry nazwane, co pozwala na podawanie argumentów w dowolnej kolejno±ci, o ile znamy ich nazwę. Możliwe jest to ponieważ lista argumentów w Pythonie jest sprowadzana do postaci słownika.
**Uwaga:** argumenty opcjonalne muszą zawsze znajdować się na końcu.
**Uwaga:** jako parametry opcjonalne zaleca się stosowanie prostych typów danych lub niezmiennych/stałych (immutable) obiektów. W języku Python argumenty opcjonalne inicjalizowane są jednokrotnie, jakiekolwiek zmiany w obiekcie zostaną zapamiętane między wywołaniami.

```python
def nazwa(par1, par2 = 5, par3 = 10):
    a = par1 *par2
    b = par2 + par3
    return (a, b)
#mozliwe wywołania:
nazwa(5)
nazwa(5,6)
nazwa(5,par3 = 6)
nazwa(pa3 = 6, par2 = 6, par1 = 2)
```

Python pozwala tak»e na wykorzystanie funkcji lambda.

```python
f = lambda a : a + 1 0
print (f(5))
```

---

### Funkcje o nieograniczonej liczbie parametrów

W funkcjach o nieograniczonej liczbie parametrów, argumenty poprzedza się jedną lub dwiema gwiazdkami. Najczęściej stosowanymi dla tego typu zmiennych są nazwy **args** oraz **kwargs**.

```python
def test(*args, **kwargs):
    print (args, " - ", kwargs)
```

Wyrażenie z jedną gwiazdką, tj. **args** (od słowa argument), czyli argumenty, to zazwyczaj zmienna, która zawiera tuple argumentów pozycyjnych. Używamy go, gdy do funkcji chcemy przekazać dowolną liczbe argumentów pozycyjnych. Parametr *args umieszczamy na końcu listy parametrów w defenicji funkcji.

```python
def suma( a, *args):
    print (a, " - ", args)
    sum = a
    for i in args:
    sum += i
    print(sum)
suma (2, 5, 6, 8, 1)

>>> 2
>>> (5, 6, 8, 1)
>>> 22
```

Wyrażenie z dwoma gwiazdkami, tj. **kwargs** (od słowa **keyword arguments**), czyli argumenty nazwane, to zmienna, która zawiera pary argumentów nazwa-wartość. Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika (tj. par klucz-wartość).

```python
def utworz_figure(typ, **kwargs):
    print(typ)
    print(kwargs)
    if typ == 'trojkat':
        print(kwargs['a'] * kwargs['h'] * 0.5)
    elif typ == 'prostokat':
        print(kwargs['a']*kwargs['b'])
utworz_figure('prostokat', a = 4, b = 6)

>>> prostokat
>>> {'a': 4, 'b': 6}
>>> 24
```

Nic nie stoi na przeszkodzie, aby jednocześnie używać **args** oraz **kwargs**, musimy jedynie pamiętać o ich kolejności. Należy zacząć od podania zdefinowanych argumentów, następnie wyrażenie z jedną gwiazdką i na samym końcu z dwoma.

---

**Zadanie 1.** Napisz funkcję, która przyjmuje na wejście wartość w sekundach, a zwraca czas w postaci "x godzin, y minut , z sekund".

---

**Zadanie 2.** Napisz funkcję wyznaczają wartość poniższego wzoru, posiadającą dwa opcjonalne parametry: stopień logarytmu - domyślnie 10, wartość k - domyślnie 2.
f(x, n, k) = logn(x**2 + 5) * (k + 1) * x

---

**Zadanie 3.** Wykorzystaj funkcję lambda do zaimplementowania następującego wzoru:
f(x) = sin(x + 1) + cos(x4).
Oblicz wartość dla liczb całkowitych z przedziału < −5, 2 >, wynik zapisz w liście.

---

**Zadanie 4.** Napisz funkcję, która przyjmie dowolną liczbę argumentów typu integer i wyznaczy oraz zwróci ich sumę.

---

**Zadanie 5.** Napisz funkcję, która oblicza objętości brył: kuli, prostopadłościanu, walca, stożka wykorzystując wyrażenie kwargs. Przetestuj napisaną funkcję dla każdej z brył.

---

**Zadanie 6.** Napisz jedną linijkę kodu, która pozwoli rozpakować cztery wartości z listy do osobnych zmiennych na dwa sposoby: bez zastosowania funkcji oraz z zastosowaniem funkcji.

---

**Zadania 7.** Napisz funkcję obliczającą silnię na dwa sposoby: z wykorzystaniem rekurencji oraz wersję tradycyjną.

---

**Zadanie 8.** Zaimplementuj funkcję obliczająca w sposób rekurencyjny n-ty wyraz ciągu Fibonacciego.

---
