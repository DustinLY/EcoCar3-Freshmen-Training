"""Running this file will run the program"""


import circle as c
import rectangle as r
import triangle as t


thearray = []  # Shapes, circle's, tri's and rects


def main():
    # ----------  Fill the array section ----------
    thearray.append(c.Circle(20, 20, 40))
    thearray.append(t.Triangle(70, 70, 20, 30))
    thearray.append(r.Rectangle(150, 150, 40, 40))
    # ----------  array fill done ----------
    # ----------  loop through the array  ----------
    totalarea = 0.0
    for i in range(0, len(thearray)):  # loop through all objects in the array
        thearray[i].display()  # don’t care what kind of object, display it
        print('\tArea:', thearray[i].area())
        totalarea += thearray[i].area()
    # end while loop
    print('The total area for', str(len(thearray)), 'Shape objects is', totalarea)
# end of run

if __name__ == '__main__':
    main()
