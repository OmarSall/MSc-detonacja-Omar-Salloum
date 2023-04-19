# Algorytm do analizy zdjęć komórek detonacji gazowej - instrukcja obsługi

## Wymagane narzędzia:
1. [Python 3](https://docs.python.org/pl/3/installing/index.html)
2. Program do obróbki graficznej, np. [GIMP](https://www.gimp.org/downloads)
3. Instalacja środowiska wirtualnego - [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
4. Instalacja bibliotek - uruchomienie [requirements.txt](https://pip.pypa.io/en/latest/user_guide/#requirements-files)

W folderze MScOS powinny znajdować się dwa pliki: `BlackBorders.py` oraz `CalibrationAndHarris.py`.
W tym samym folderze należy skopiować zdjęcia, które chcemy przeanalizować.
Na potrzeby instrukcji, będzie to zdjęcie `1.jpg`.

**Zdjęcia, które kopiujemy do folderu MScOS muszą być w odpowiedniej orientacji – szerokość komórki detonacyjnej musi być krótszą przekątną, którą ustawiamy jako przekątną poziomą**

Aby przygotować środowisko wirtualne i zainstalować wymagane zależności, należy wykonać:

```
python3 -m venv ./venv/
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Uruchomienie BlackBorders.py

`python3 BlackBorders.py -i 1.jpg -o Border1.jpg`

* `-i` oznacza zdjęcie wejściowe (input)
* `-o` oznacza zdjęcie wyjściowe (output)
 
Po uruchomieniu BlackBorders.py w folderze MScOS powinno pojawić się nowe zdjęcie `Border1.jpg`
Następnym etapem jest otworzenie programu do obróbki graficznej (w rozważanym przykładzie jest to GIMP) i załadowanie zdjęcia `Border1.jpg`.

## Edycja zdjęcia

Gdy otworzy nam się zdjęcie należy wybrać opcję Pencil Tool, wybrać kolor biały i klikać w tych miejscach gdzie są punkty potrójne (wierzchołki rombów). Kształt narzędzia rysującego musi być okrągły, a rozmiar należy dopasowywać do wielkości komórki detonacyjnej, aby kropki się nie pokrywały i był widoczny odstęp między kropkami.


Po zaznaczeniu wszystkich interesujących nas punktów potrójnych należy wyeksportować zdjęcie do folderu „MScOS”.
W folderze MScOS powinno pojawić się zdjęcie Border1GIMP.jpg


## Uruchomienie `CalibrationAndHarris.py`:

`python3 CalibrationAndHarris.py -c 1.jpg -i Border1GIMP.jpg`

* `-c` oznacza zdjęcie, które będzie wykorzystane do kalibracji
* `-i` oznacza zdjęcie, które wyeksportowano z programu GIMP

## Kalibracja

![Reference Image](/screenshots/screenshot1.jpg)
![Reference Image](/screenshots/screenshot2.jpg)


* Po zaznaczeniu *czterech* współrzędnych, należy wcisnąć ESC, bądź zamknąć zdjęcie poprzez kliknięcie krzyżyka w prawym górnym rogu.
* Następnie powinien pojawić się histogram, który zostanie zapisany do finalnego raportu, aby przejść dalej należy zamknąć histogram.
* W celu zakończenia programu, należy zamknąć dwa zdjęcia („Image with Borders” oraz „Threshold”) _za pomocą przycisku ESC_.

Po zamknięciu zdjęć, w folderze MScOS powinien pokazać się raport o nazwie `html_raport.html` oraz zdjęcie histogramu o nazwie `hist.png`.
