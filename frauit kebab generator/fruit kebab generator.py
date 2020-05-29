import random
import cv2
import os

strawberry = "strawberry"
kiwi = "kiwi"
apple = "apple"
orange = "orange"
peach = "peach"
blueberry = "blueberry"
fruits = [strawberry, kiwi, apple, orange, peach, blueberry]

available_fruits = []
save_dir = ""

amount_made_kebabs = 0

width = 800
height = 800
amount_strawberrys = input("how many available strawberys")
amount_kiwis = input("how many available kiwis")
amount_apples = input("how many avaible apples")
amount_oranges = input("how many oranges")
amount_peaches = input("how many peaches")
amount_blueberrys = input("how many bluberrys")

if (int(amount_strawberrys) + int(amount_kiwis) + int(amount_apples) + int(amount_oranges) + int(amount_peaches) + int(amount_blueberrys)) < 10:
    print("error: 10 or mre fruit needed")
    quit()
print("pressed enter to generate a kebab, type \"quit\" to exit\ type \"save\" TO save the picture")

for i in range(int(amount_strawberrys)):
    available_fruits.append(strawberry)
for i in range(int(amount_kiwis)):
    available_fruits.append(kiwi)
for i in range(int(amount_apples)):
    available_fruits.append(apple)
for i in range(int(amount_oranges)):
    available_fruits.append(orange)
for i in range(int(amount_peaches)):
    available_fruits.append(peach)
for i in range(int(amount_blueberrys)):
    available_fruits.append(blueberry)

def make_kebab():
    kebab = []

    if len(available_fruits) < 10:
        return []
    
    for i in range(10):
        
        fruit = available_fruits[random.randint(0,len(available_fruits)-1)]
        kebab.append(fruit)
        available_fruits.remove(fruit)

    return kebab

stick = cv2.imread("D:/Coding Files/python projects/fruit kebab generator/images/stick.png", cv2.IMREAD_COLOR)
stick = cv2.resize(stick, (width,height))

def pasteImage(x1,x2,y1,y2,img_name):
    img = cv2.imread(f"D:/Coding Files/python projects/fruit kebab generator/images/{img_name}.png", cv2.IMREAD_COLOR)
    
    stick[x1:x2,y1:y2] = cv2.resize(img, (y2-y1,x2-x1))

    


while True:
    amount_made_kebabs+=1
    
    kebab = make_kebab()
    print(f"kebab{amount_made_kebabs}: {kebab}")
    print(f"available_fruits: {len(available_fruits)}")
    
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
        stick = cv2.imread("D:/Coding Files/python projects/fruit kebab generator/images/stick.png", cv2.IMREAD_COLOR)
    cv2.imshow("kebab", stick)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    i = input()
    if i == "quit":
        break
        quit()
    if i == "save":
        if save_dir == "":
            save_dir = input("what directory to save image to:")
            try:
                
                os.chdir(save_dir)
            except:
                print("error: directory not found")
                break
                quit()
        
        file_name = f"kebab{amount_made_kebabs}"
        file_type= ".jpg"
        cv2.imwrite(f"{file_name}{file_type}", stick)
        os.system(f"{file_name}{file_type}")
        

        
