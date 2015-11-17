# Day Planner

## Description

In this project we are going to build a simple Day Planner program.
This program will allow the user to type in the month, day, hour and minute of
various appointments and will insert each into an array.
Be sure to insert each appointment into the array in the proper position,
according to the date and time of the appointment.
These means the earliest appointment should be at the start of the array, and
the last appointment at the end of the array.

Please pre load your array with the following appointments:

-   Mar 4, 17:30 Quiz 1
-   Apr 1, 17:30 Midterm
-   May 6, 17:30 Quiz 2
-   Jun 3, 17:30 Final

## Implementation

### Phase 1

The class Appointment is essentially a record;
an object built from this class will represent an appointment in a Day Planner.

It will contain 5 fields:

-   month (3 character String)
-   day (int)
-   hour (int)
-   minute (int)
-   message (String no longer then 40 characters).

Write four methods in this class

-   printAppointment()

    -   will nicely format and print the Appointment object.

-   \__init__()

    -   will be used to create the default appointments listed above, so it needs parameter(s) passed to it

### Phase 2

Create a class Planner

In this class

-   declare an array of Appointment objects

Some methods you must implement in the Planner class for this project:

-   \__init__()

    -   constructor that places the 4 default Appointment objects in the array

-   compareAppointments(Appointment A1, Appointment A2)

    -   returns true if A1 < A2, false otherwise

-   insertAppointment(Appointment A1)

    -   places A1 in the proper (sorted) slot of the array

-   listAppointment()

    -   list all appointments in the array (in order) with a number in front

-   deleteAppointment()

    -   delete an appointment selected by the user

You may name the methods whatever you wish and you may add additional methods to the Planner and Appointment classes as long as you clearly document 'what' and 'why' you added the method. Each class should be in its own file.
