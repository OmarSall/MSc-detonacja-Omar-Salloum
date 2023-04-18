# Algorytm do analizy zdjęć komórek detonacji gazowej instrukcja obsługi

## Wymagane narzędzia:
1. Python (<https://docs.python.org/pl/3/installing/index.html>)
2. Program do obróbki graficznej (np.:GIMP <https://www.gimp.org/downloads/>)<br />
3. Instalacja środowiska wirtualnego (<https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/?fbclid=IwAR1ict-dLli3d579_8WJFFG8RVH2zsZ9XhAqUIjUwQlCS73fjGcoiHyYb-4>)<br />
4. Instalacja bibliotek - uruchomienie requirements.txt  
https://pip.pypa.io/en/latest/user_guide/#requirements-files
---------------------------

 <br />
W folderze MScOS powinny znajdować się dwa pliki: BlackBorders.py oraz CalibrationAndHarris.py.<br />
W tym samym folderze należy skopiować zdjęcia, które chcemy przeanalizować. <br />
Na potrzeby instrukcji, będzie to zdjęcie 1.jpg.<br /><br />

--------------------------
### **Zdjęcia, które kopiujemy do folderu MScOS muszą być w odpoiedniej orientacji – szerokość komórki detonacyjnej musi być krótszą przekątną, którą ustawiamy jako przekątną poziomą**<br />
---------------------------------

<br />

Po instalacji środowiska wirtualnego należy uruchomić plik **requirements.txt**

<br />
---------------------------------------------------------<br />

Uruchomienie BlackBorders.py: <br />
**python BlackBorders.py -i 1.jpg -o Border1.jpg**
<br />----------------------------------------------------------<br />

*„-i” oznacza zdjęcie wejściowe (input)*<br />
*„-o” oznacza zdjęcie wyjściowe (output)*
 
•	Po uruchomieniu BlackBorders.py w folderze MScOS powinno pojawić się nowe zdjęcie **Border1.jpg**.
 
•	Następnym etapem jest otworzenie programu do obróbki graficznej (w rozważanym przykładzie jest to GIMP) i załadowanie zdjęcia Border1.jpg.
 <br />


•	Gdy otworzy nam się zdjęcie należy wybrać opcję Pencil Tool, wybrać kolor biały i klikać w tych miejscach gdzie są punkty potrójne (wierzchołki rombów). Kształt narzędzia rysującego musi być okrągły, a rozmiar należy dopasowywać do wielkości komórki detonacyjnej, aby kropki się nie pokrywały i był widoczny odstęp między kropkami.

<br />

•	Po zaznaczeniu wszystkich interesujących nas punktów potrójnych należy wyeksportować zdjęcie do folderu „MScOS”.
 
<br />

W folderze MScOS powinno pojawić się zdjęcie Border1GIMP.jpg.<br />
 <br />----------------------------------------------------------------------<br />
Uruchomienie CalibrationAndHarris.py:

**python CalibrationAndHarris.py -c 1.jpg -i Border1GIMP.jpg**
<br />-----------------------------------------------------------------------<br /><br />
*“-c” oznacza zdjęcie, które będzie wykorzystane do kalibracji <br />*
*„-i” oznacza zdjęcie, które wyeksportowano z programu GIMP <br />*

# Kalibracja

  
![Reference Image](/screenshots/screenshot1.jpg) <br /><br />
![Reference Image](/screenshots/screenshot2.jpg)


*Po zaznaczeniu **czterech** współrzędnych, należy wcisnąć ESC, bądź zamknąć zdjęcie poprzez kliknięcie krzyżyka w prawym górnym rogu.*

*Następnie powinien pojawić się histogram, który zostanie zapisany do finalnego raportu, aby przejść dalej należy zamknąć histogram.*
 

W celu zakończenia programu, należy zamknąć dwa zdjęcia („Image with Borders” oraz „Threshold”).

Po zamknięciu zdjęć, w folderze MScOS powinien pokazać się raport o nazwie html_raport.html oraz zdjęcie histogramu o nazwie hist.png.
 
