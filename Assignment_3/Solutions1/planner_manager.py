"""PlannerManager

This is a file used to manager the planner

"""
import planner as pln
import appointment as apt
import math
import dates as d


class PlannerManager:
    """The PlannerManager class creates a class capable of managing the planner

    The PlannerManager will allow the user to view a menu and select what to
    do with their planner from the menu.

    """
    def __init__(self):
        self.my_planner = pln.Planner()
        self.switch = {
            '1': self.view_apmts,
            '2': self.add_apmt,
            '3': self.delete_apmt,
            '4': self.view_apmts_by_month,
            '5': self.view_apmts_by_day,
            'e': self.exit
        }

    def print_list(self, array):
        """Prints each appointment within the calendar formated nicely
        """
        index = 1
        for obj in array:
            print(index, '. ', obj, '\n', sep="", end="")

    def view_apmts(self):
        """Prints all appointments within the planner
        """
        print('')
        self.my_planner.list_appointments_4()
        print('')
        return True

    def add_apmt(self):
        """Takes the inputs to add an appointment to the planner
        """
        print('')
        month = input('What month? ')
        day = input('What day? ')
        hour = input('What hour? ')
        minute = input('What minute')
        message = input('What is the appointment? ')
        self.my_planner.add_appointment(month, day, hour, minute, message)
        print('')
        return True

    def delete_apmt(self):
        """Asks for an index and removes that appointment from the planner
        """
        print('')
        index = float(
            input('Which apointment would you like to delete (enter the #)? '))
        if not math.isnan(index):
            index = int(index)
            deleted = self.my_planner.delete_appointment(index - 1)
            print('You deleted', deleted)
            choice = input('Would you like to undo this delete (y for yes)? ')
            if(choice == 'y' or choice == 'Y'):
                self.my_planner.insert_appointment(deleted)
        print('')
        return True

    def view_apmts_by_month(self):
        """Asks for a month and prints all apointments filtered by the month
        """
        print('')
        month = input('\nWhich month would you like to see? ').lower()
        if month in d.VALIDATE_MONTHS:
            mon = d.VALIDATE_MONTHS[month]
            new_list = []
            for apmt in self.my_planner.get_appointments():
                if apmt.get_month() == mon:
                    new_list.append(apmt)
            self.print_list(new_list)
        print('')
        return True

    def view_apmts_by_day(self):
        """Asks for a date and prints all appointments filtered by the date
        """
        print('')
        month = input('\nWhich month would you like to see? ').lower()
        day = float(input('Which day would you like to see? '))
        if not math.isnan(day):
            day = int(day)
            if month in d.VALIDATE_MONTHS:
                mon = d.VALIDATE_MONTHS[month]
                new_list = []
                for apmt in self.my_planner.get_appointments():
                    if apmt.get_month() == mon and apmt.get_day() == day:
                        new_list.append(apmt)
                self.print_list(new_list)
        else:
            print('That is not a valid date.')
        print('')
        return True

    def exit(self):
        """Used to exit the loop using the Dictionary (switch style)
        """
        return False

    def menu(self):
        """Creates the loop menu to run the program
        """
        loop = True
        while loop:
            choice = input('Choose an option:\n'
                           '1. View appointments\n'
                           '2. Add an appointment\n'
                           '3. Delete an appointment\n'
                           '4. View appointments by month\n'
                           '5. View appointments by day\n'
                           'e. Exit the program\n')
            loop = self.switch[choice]()
