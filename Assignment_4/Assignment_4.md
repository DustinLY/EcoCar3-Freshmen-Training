# Assignment 4

## Phase 1

I will demonstrate the working code for Phase 1 Thursday 11/17/2015

### Classes Needed

#### Shape

The generic abstract class shape will serve as the parent class to Circle,j
Rectangle and Triangle. This class MUST be abstract and it will contain
abstract methods

##### Variables

-   x – x coordinate for the shape, an integer
-   y – y coordinate for the shape, an integer

##### Methods

-   getX() returns an int for the shapes x position
-   setX()  assign the shapes x position
-   getY() returns an int for the shapes y position
-   setY()  assign the shapes y position
-   \__init__() with optional parameters
-   display()  an abstract method to display the shape
-   area() an abstract method to calculate the shapes area

#### Circle

It must inherit Shape.

##### Variables

-   radius – an int, length of the radius

##### Methods

-   getRadius() returns an int for the circles radius
-   setRadius ()  assign the circles radius
-   \__init__() with optional parameters x, y, radius parameters (in that order)
-   display() - display the circle as a text string containing the word Circle, and the x, y and radius values
-   area()  - calculate and return a double of the area and return it

#### Rectangle

It must inherit Shape.

##### Variables

-   width –  an int
-   height – an int

##### Methods

-   getHeight() returns an int for the rectangles height
-   setHeight ()  assign the rectangles height
-   getWidth() returns an int for the rectangles width
-   setWidth ()  assign the rectangles width
-   \__init__() with optional parameters x, y, height, width parameters(in that order)
-   display() - display the rectangle as a text string containing the word Rectangle, and the x, y, width and height values
-   area()  - calculate and return a double of the area and return t

#### Triangle

It must inherit Shape.

##### Variables

-   base –  an int
-   height – an int

##### Methods:

-   getHeight() returns an int for the Triangle height
-   setHeight ()  assign the Triangle height
-   getBase() returns an int for the Triangle base
-   setBase ()  assign the Triangle base
-   \__init__() with optional parameters x, y, height, base parameters (in that order)
-   display() - display the triangle as a text string containing the word Triangle, and the x, y, width and height values
-   area()  - calculate and return a double of the area and return it

Note: all display() methods should use print() to output a text description of the shape to the console.

If you build the classes correctly, the following code should work:

    import circle as c
    import triangle as t
    import rectangle as r


    thearray = []  # Shapes, circle's, tri's and rects


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


When get the main program above working make sure it works with different Shape objects placed in the array. When I test the program I will provide a different ‘Fill in the array’ section of the code and expect your program to work with the new objects. This means you must implement all the methods listed in the class specifications exactly as I ask. The new code I provide will assume they are available and will call them. Remember: I will only change (and you should only change when testing) the following section of code:


    # ----------  Fill the array section ----------
    thearray.append(c.Circle(20, 20, 40))
    thearray.append(t.Triangle(70, 70, 20, 30))
    thearray.append(r.Rectangle(150, 150, 40, 40))
    # ----------  array fill done ----------

## Phase 2

DO NOT attempt phase 2 unless the rest of the assignment is completed.

Display the Shape’s on the GUI window in addition to displaying them on the console.

Make very few changes to the original code:

-   import tkinter
-   main.py will set up the gui
-   the classes will need a display method for tkinter
