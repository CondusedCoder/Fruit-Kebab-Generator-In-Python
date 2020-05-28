import random
import cv2
import numpy as np

strawberry = "strawberry"
kiwi = "kiwi"
apple = "apple"
orange = "orange"
peach = "peach"
blueberry = "blueberry"
fruits = [strawberry, kiwi, apple, orange, peach, blueberry]

available_fruits = []

width = 800
height = 800
amount_of_available_fruits = input("how many available fruit(needs 10 or more)")

for i in range(int(amount_of_available_fruits)):
    available_fruits.append(fruits[random.randint(0,len(fruits)-1)])

def make_kebab():
    kebab = []

    if len(available_fruits) < 10:
        return []
    
    for i in range(10):
        
        fruit = available_fruits[random.randint(0,len(available_fruits)-1)]
        kebab.append(fruit)
        available_fruits.remove(fruit)

    return kebab

stick = cv2.imread("D:/Coding Files/python projects/frauit kebab generator/images/stick.png", cv2.IMREAD_COLOR)
stick = cv2.resize(stick, (width,height))

def pasteImage(x1,x2,y1,y2,img_name):
    img = cv2.imread(f"D:/Coding Files/python projects/frauit kebab generator/images/{img_name}.png", cv2.IMREAD_COLOR)
    
    stick[x1:x2,y1:y2] = cv2.resize(img, (y2-y1,x2-x1))

    


while True:
    
    kebab = make_kebab()
    print(f"kebab: {kebab}")
    print(f"available_fruits: {available_fruits}")
    
    if (kebab != []):

        pasteImage(760,780,350, 450,kebab[0])
        pasteImage(720,740,350,450,kebab[1])
        pasteImage(680,700,350, 450,kebab[2])
        pasteImage(640,660,350,450,kebab[3])
        pasteImage(600,620,350, 450,kebab[4])
        pasteImage(560,580,350,450,kebab[5])
        pasteImage(520,540,350, 450,kebab[6])
        pasteImage(480,500,350,450,kebab[7])
        pasteImage(440,460,350, 450,kebab[8])
        pasteImage(400,420,350,450,kebab[9])

    else:
        stick = cv2.imread("D:/Coding Files/python projects/frauit kebab generator/images/stick.png", cv2.IMREAD_COLOR)
    cv2.imshow("kebab", stick)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    input()

        
        


