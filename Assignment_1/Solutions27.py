import math


# create a function that takes in the radius and calculates the area of a sphere
def sphere_Area(radius):
    try:
        return 4 * (float(radius) ** 2) * math.pi
    except:
        return -1
    # area = 4 * (radius ^ 2) * math.pi
    # print area
    # return area


# create a function that takes in a length calculate the volume of a sphere
def volume_Sphere(radius):
    if radius < 0:
        return -1
    try:
        return (4 * (float(radius) ** 3) * math.pi) / 3
    except:
        return -1
    # volume = (4 / 3) * (radius ^ 3) * math.pi
    # print volume
    # return volume


# create a function that takes in a price and calculates the tip. The function should return the total. (TIP IS 9%)
def calculate_Tip(sub_total):
    try:
        return float(sub_total) * 1.09
    except:
        return -1

    # total = sub_total *= 1.09
    # print total
    # return total


def calculate_Tip_adjustable(sub_total, tip):
    try:
        if float(tip) > 1:
            return float(sub_total) * (1 + (float(tip) * .01))
        else:
            return float(sub_total) * (1 + float(tip))
    except:
        return -1
    # real_tip = 1
    # if tip > 1:
    #     real_tip += (tip * .01)
    # else:
    #     real_tip += tip
    # total = sub_total *= tip
    # print total
    # return total


# create a function that takes in a temperature and converts celsius to fahrenheit;
def cel_to_fahren(temp_in_cel):
    try:
        return (float(temp_in_cel) * 1.8) + 32
    except:
        return None
    # temp_in_fahren = (temp_in_cel * 1.8) + 32
    # print temp_in_fahren
    # return temp_in_fahren


# create a function that takes in a temperature and converts farenheit to celsius
def fahren_to_cel(temp_in_fahren):
    try:
        return (float(temp_in_fahren) - 32) / 1.8
    except:
        return None
    # temp_in_cel = (temp_in_fahren - 32) / 1.8
    # print temp_in_cel
    # return temp_in_cel


def main():
    loop = True
    while loop:
        choice = raw_input('\n1. Area of a sphere\n2. Volume of a sphere\n' +
                           '3. Calculate tip on bill (9%)\n4. Calculate tip ' +
                           'on bill(custom tip percentage)\n5. Convert ' +
                           'celsius to fahrenheit\n6. Convert fahrenheit to ' +
                           'celsius\n7. Exit Program\n')
        if choice == '1':
            area = sphere_Area(raw_input('Enter the radius: '))
            if area < 0:
                print 'Error'
            else:
                print area
        elif choice == '2':
            volume = volume_Sphere(raw_input('Enter the radius: '))
            if volume < 0:
                print 'Error'
            else:
                print volume
        elif choice == '3':
            tip = calculate_Tip(raw_input('Enter the bill total: '))
            if tip < 0:
                print 'Error'
            else:
                print tip
        elif choice == '4':
            tip = calculate_Tip_adjustable(raw_input('Enter the bill total: '),
                                           raw_input('Enter the tip: '))
            if tip < 0:
                print 'Error'
            else:
                print tip
        elif choice == '5':
            temp = cel_to_fahren(raw_input('Enter the temp in celsius: '))
            if temp is None:
                print 'You did not enter a valid number'
            else:
                print temp
        elif choice == '6':
            temp = fahren_to_cel(raw_input('Enter the temp in fahrenheit: '))
            if temp is None:
                print 'You did not enter a valid number'
            else:
                print temp
        elif choice == '7':
            loop = False
        else:
            print 'That is not a valid option. Try again.'

if __name__ == '__main__':
    main()
