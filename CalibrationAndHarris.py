#python CalibrationAndHarris.py -c 1.jpg -i Border1GIMP.jpg

# import the necessary packages
import cv2
import imutils
import argparse
import statistics
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
from statistics import median, mode, variance, stdev
# importing scikit-image submodule to compute histograms
from skimage import exposure as iml 
import pandas as pd
coord_Cal = []

def mouseCoord(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        print("Coordinates of pixel: X: ",x,"Y: ",y)

        coord_Cal.append((x,y))

        if len(coord_Cal) == 4:
            # print(coord)
            return coord_Cal


# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--calibration", required=True,
    help="path to input image")



ap.add_argument("-i", "--image", required=True,
    help="path to input image")
# ap.add_argument("-c", "--calibration", required=True,
#     help="calibration output in px/mm")
args = vars(ap.parse_args())


image = cv2.imread(args["calibration"])

imageHar = cv2.imread(args["image"])

resized = imutils.resize(image, width=500)

  

print("Zaznacz i kliknij lewym przyciskiem myszy na linijce 0 mm, 5 mm, 10 mm oraz 15 mm \n postaraj sie zaznaczac punkty po linii")
print("\n Po zaznaczeniu czterech punktow wcisnij ESC")
cv2.namedWindow('Calibration')
cv2.setMouseCallback('Calibration',mouseCoord)


cv2.imshow('Calibration',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'wspolrzedne zaznaczonych punktow: {coord_Cal}')

dist_Cal = []
for i, elem in enumerate(coord_Cal):
    if i < len(coord_Cal) - 1:
        if abs(coord_Cal[i][1] - coord_Cal[i+1][1]) < 6:
            if abs(coord_Cal[i][0] - coord_Cal[i+1][0]) > 6:
                dist = abs(coord_Cal[i][0] - coord_Cal[i+1][0])
        elif abs(coord_Cal[i][1] - coord_Cal[i+1][1]) >= 6:
            dist = abs(coord_Cal[i][1] - coord_Cal[i+1][1])
        
        dist_Cal.append(dist)

# print(dist_Cal)

srednia = int(statistics.mean(dist_Cal))

one_mm = srednia//5

print(f"Wartosc 1 mm to {one_mm} px")


scale = 1
delta = 0
ddepth = cv2.CV_16S

class my_dictionary(dict):
 
    # __init__ function
    def __init__(self):
        self = dict()
         
    # Function to add key:value
    def add(self, key, value):
        self[key] = value

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)


# construct the argument parser and parse the arguments


resizedHar = imutils.resize(imageHar, width=500)

imgHar = cv2.cvtColor(resizedHar,cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(imgHar, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray,(3,3),0)
# Find Canny edges
# edged = cv2.Canny(gray, 30, 40)

operatedImage = np.float32(gray)/255

dest = cv2.cornerHarris(operatedImage, 5, 5, 0.07)
dest = cv2.erode(dest, None)
resizedHar[dest > 0.01 * dest.max()]=[0, 0, 255]


# the window showing output image with corners
# plt.imshow(image,cmap='gray'),plt.show()
# gray1 = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

lower_red = np.array([0, 0, 200], dtype = "uint8") 

upper_red= np.array([0, 0, 255], dtype = "uint8")

mask = cv2.inRange(resizedHar, lower_red, upper_red)

output_red = cv2.bitwise_and(resizedHar, resizedHar, mask = mask)

gray1 = cv2.cvtColor(output_red, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray1 , 10,255,cv2.THRESH_BINARY)


# Creating kernel
kernel = np.ones((6, 6), np.uint8)

# Using cv2.erode() method 
erode = cv2.erode(thresh, kernel, cv2.BORDER_REFLECT) 

# find the contours
contours,hierarchy = cv2.findContours(thresh,
cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours detected:", len(contours))


x_coord = []
y_coord = []
# Main Function
dict_obj = my_dictionary()

# draw contour and shape number
for i, cnt in enumerate(contours):
   
   if cv2.contourArea(cnt) < 5:  ##################################Trzeba zmieniać te wartości jak nie pokazują się wierzcholki!
       continue
   M = cv2.moments(cnt)
   x1, y1 = cnt[0,0]
#    img1 = cv2.drawContours(resized, [cnt], -1, (0,255,255), 2) 

   (x1,y1),radius = cv2.minEnclosingCircle(cnt)
    
   center = (int(x1),int(y1))
   radius = int(radius)

   cv2.circle(resizedHar,center,radius,(0,255,255),2)

   cv2.putText(resizedHar, f'Node:{i}', center,
   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

   

   print(f'Coord. of Node {i}:  X: {int(x1)}, Y: {int(y1)}')

   x_coord.append(x1)
   y_coord.append(y1)

   dict_obj.add(i, (x1,y1))



# print(f"x_coord: {x_coord}")
# print("##############################################################")
# print(f"y_coord: {y_coord}")

coord = []

for i, tupleXY in enumerate(zip(x_coord, y_coord)):
    coord.append(tupleXY)
print("##############################################################")
print(f"List of coordinates: {coord}")

distance = []

for i, elem in enumerate(coord):
    if i < len(coord)-2:
        # if coord[i][1] - coord[i+1][1] < coord[i][1] - coord[i+2][1]:###########Changing horizontal restriction
        if coord[i][1] - coord[i+1][1] < 33:
            if abs(coord[i][0]-coord[i+1][0]) < abs(coord[i][0]-coord[i+2][0]):
                dist = round(math.sqrt(((coord[i][0] - coord[i+1][0])**2)+((coord[i][1] - coord[i+1][1])**2)))
                distance.append(dist)
            elif abs(coord[i][0]-coord[i+1][0]) > abs(coord[i][0]-coord[i+2][0]):
                if coord[i][1] - coord[i+2][1] < 33:
                    dist = round(math.sqrt(((coord[i][0] - coord[i+2][0])**2)+((coord[i][1] - coord[i+2][1])**2)))
                    distance.append(dist)
                elif coord[i][1] - coord[i+2][1] > 33:
                    dist = round(math.sqrt(((coord[i][0] - coord[i+1][0])**2)+((coord[i][1] - coord[i+1][1])**2)))
                    distance.append(dist)

            print(f"distance between node {i} and {i+1} equals: {dist} pixels")
        else:
            continue
##################################################
# print(dict_obj)
# print(distance)

#Enter number of pixels for one milimeter from CalibrationCoord.py
# one_mm = 3  #1 mm equals to 2 pixels

# one_mm = int(args["calibration"])

true_dist = [round(i / one_mm )for i in distance]
sorted_true = sorted(true_dist, key = lambda x:int(x))
###wstawic tutaj warunek dla malej ilosci probek
#deleting outliers
if len(sorted_true) >= 30:
    del sorted_true[-2:]
    del sorted_true[:2]
else:
    pass

print(f'List of true distances:  {sorted_true}')

#STATYSTYKA

mu = statistics.mean(sorted_true)
mediana = median(sorted_true)
moda = mode(sorted_true)
maximum = max(sorted_true)
minimum = min(sorted_true)
range = maximum - minimum
wariancja = variance(sorted_true)
sigma = stdev(sorted_true)



data = [[mu, mediana, moda , maximum, minimum, range, wariancja, sigma]]
df = pd.DataFrame(data, columns = ['Średnia', 'Mediana', 'Moda', 'Max', 
                                   'Min','Zakres', 'Wariancja', 
                                   'Odchylenie Standardowe'])


arr = np.array(sorted_true)

fig, ax = plt.subplots()

plt.axvline(mu, color = 'red', linestyle = 'dashed')
plt.axvline(mu + sigma, color = 'y', linestyle = 'dashed')
plt.axvline(mu - sigma, color = 'y', linestyle = 'dashed')


plt.style.use('ggplot')
histogram = plt.hist(sorted_true, bins = len(sorted_true), color = 'blue',edgecolor = 'k')
plt.xlabel("Szerokość komórki detonacyjnej / mm")
plt.ylabel("Częstość")
plt.title("Histogram")

hist_image = plt.savefig('hist.png')  #nazwe polaczyc z nazwa zdjecia!

plt.show()




# print(f'Average value of width of the detonation cell yields: {mean} mm')


##############################################################################

# 1. Set up multiple variables to store the titles, text within the report
page_title_text='Raport'
title_text = 'Dane statystyczne'
text = 'Analiza statystyczna szerokości komórek detonacyjnych'
histogram1 = 'Histogram'
stats_text = 'Podstawowe wielkości analizy statystycznej'

html = f'''
    <html>
        <head>
            <title>{page_title_text}</title>
        </head>
        <body>
            <h1>{title_text}</h1>
            <p>{text}</p>
            <h2>{histogram1}</h2>
            <img src = 'hist.png' width = "700">
            <h2>{stats_text}</h2>
            {df.to_html()}
        </body>
    </html>
    '''
with open('html_raport.html', 'w', encoding = "utf-8") as f:
    f.write(html)


##############################################################################

# plt.hist(gray1.ravel(),256,[0,256]); plt.show()

cv2.imshow('Image with Borders', resizedHar)
# cv2.waitKey(0)
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
