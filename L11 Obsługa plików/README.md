#

## Laboratorium 11. Ćwiczenia w odczycie i zapisie plików tekstowych, binarnych i XML

### Wczytywanie danych z pliku tekstowego

Do otwarcia pliku w Pythonie służy funkcja **open**, w najprostszej postaci wywoływana z jednym parametrem - sćieżką do pliku.

Po otwarciu pliku, jego zawartość można odczytać metodą **read**, jeśli chcemy odczytać całą zawartość, lub **readline**, jeśli chcemy odczytać pojedynczą linię.

Po zakończeniu pracy z plikiem, pamiętaj o jego zamknięciu metoda **close**.

---

#### Types of File in Python

##### Text file

- Web standerts: html, XML, CSS, JSON
- Source Code:   c, app, js, py, java
- Documents:     txt, tex, RTF
- Tabular data:  csv, tsv
- Configuration: ini, cfg, reg

##### Binary file

- Documents files:  .pdf, .doc, .xls
- Images files:     .png, .jpg, .gif, .bmp
- Video files:      .mp4, .3gp, .mkv, .avi
- Audio files:      .mp3, .wav, .mka, .aac
- Database files:   .mdb, .accde, .frm, .sqlite
- Archives files:   .zip, .rar, .iso, .7z
- Exucutable files: .exe, .dll, .class

---

**Open()**
file_object = open("**filename**", "**mode**")

```python
fileNamePath = "./files/zad1.txt"
fileName = open(fileNamePath.read(), "r")
print(fileName.read())
filename.close()
```

**_mode_**

mode | value
-|-
**'r'**  | read mode
**'w'**  | write mode
**'a'**  | append mode
**'r+'** | read or write mode
**'a+'** | read of append mode

---

### Zapis danych do pliku tekstowego

Do zapisu tekstu do pliku służy metoda **write**, która dopisze wskazywany jako argument element na koniec pliku.

---

**Zadanie 1.** Wczytaj zawartość pliku _zad1.txt_ linia po linii. Każdą wczytaną linię dodaj do listy.

Powyższe zadanie można zrealizować także przy pomocy jednej linii kodu stosując metodą **readlines**, która wczytuje całą zawartość pliku i dzieli go względem znaków nowej linii, a następnie całość umieszcza w liście.

**Zadanie 2.** Napisz funkcję, która wczyta zawartość pliku _iris.txt_ do listy dwuwymiarowej, gdzie wiersz zawierać będzie pojedynczą próbkę, a kolumny tego wiersza kolejne atrybuty.

**Zadanie 3.** Rozszerz funkcję z _Zadania 2_ tak, aby dane numeryczne były konwertowane do typu **float** (podpowiedż: obsłuż wyjątek ValueError dla konwersji danych).

**Zadanie 4.** Zapisz do pliku o nazwie _zad4.txt_ te wiersze z listy z _Zadania 3_, których pierwsza wartość jest większa od 5 oraz wyświetl ile jest takich wierszy. Jako separator elementów w kolejnych wierszach użyj spacji.
