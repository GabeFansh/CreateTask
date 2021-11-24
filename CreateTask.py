import tkinter
from tkinter import ttk, END
from math import *

"""
This is the first set up of the tkinter window that is needed for anything to start generating
"""

root = tkinter.Tk()
root.title('Travel Time Calculator')
root.resizable(0, 0)

field_font = ('Cambria', 10)
bg_color = "#67E11F"
button_color = "#f5cf87"
root.config(bg=bg_color)



"""
The dictionary below keeps track of all the locations and the locations specific latitude and longitude coordinate
The cordinates are then plugged into the distance formula below and are used to find how long it would take to travel between
the two locations.
"""


DIRECTORY = {
    "New York" : [40.7128, 74.0060],
    "Las Vegas" : [36.1699, 115.1398],
    "California" : [36.7783, 119.4179],
    "Boston" : [42.3601, 71.0589],
    "Philadelphia": [39.9526, 75.1652],
    "Washington D.C": [38.9072, 77.0369],
    "Grand Canyon": [36.0544, 112.1401],
    "Yellowstone National Park": [44.4280, 110.5885],
    "Disney World": [28.3772, 81.5707]
}


MODIFIERS = {
    "Plane": 0.118,
    "Car": 1,
    "Train/Bus": 1.5,
    "Walk": 20
}

"""
This function below is the main component of the calculations. It collects the data that the user has inputed:
The starting and ending location, and the method of travel. Then using the distance formula, its able to determine the distance 
between the 2 locations and then based on the method of travel, will multiply in a modifier to account for the change of speed
between the travle methods.

"""

def calculate():
    StartingLocation = input_combobox.get()
    EndLocation = output_combobox.get()
    MethodTravel = travelMethod_combobox.get()

    """
    This is the distance formula used to find the distance between the two chosen locations
    """

    Distance = sqrt(((DIRECTORY[EndLocation][0] - DIRECTORY[StartingLocation][0])**2) + ((DIRECTORY[EndLocation][1] - DIRECTORY[StartingLocation][1])**2))

    """
    This changes the modifier based on the method of travel chosen by the user
    """

    for i in [*MODIFIERS]:
        if MethodTravel == i:
            TotalDistance = Distance * MODIFIERS[MethodTravel]


    if output_field.get() != "":
        output_field.delete(0, END)
        output_field.insert(END, str(round(abs(TotalDistance))) + " Hours")
    else:
        output_field.insert(END, str(round(abs(TotalDistance))) + " Hours")





#Everything from this point on is setting up the Tkinter GUI


output_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3)
equal_label = tkinter.Label(root, text="to", font=field_font, bg=bg_color)



output_field.grid(row=1, column=2, padx=10, pady=10)

"""This generates the lists used for the starting location and the end location."""
"""
[*DIRECTORY] takes all the keys from the DIRECTORY dictionary listed above and turns it into its own list instead of
having a seperate list coded in. Makes the code more efficient. Same applies to [*MODIFIER]
"""



input_combobox = ttk.Combobox(root, value=[*DIRECTORY], font=field_font, justify='center')
output_combobox = ttk.Combobox(root, value=[*DIRECTORY], font=field_font, justify='center')

travelMethod_combobox = ttk.Combobox(root, value=[*MODIFIERS], font=field_font, justify='center')

"""This positions the boxes in an organized way so the GUI looks neat and organized."""

to_label = tkinter.Label(root, text="to", font=field_font, bg=bg_color)
to_label.grid(row=0, column=1, padx=10, pady=10)
input_combobox.grid(row=0, column=0, padx=10, pady=10)
output_combobox.grid(row=0, column=2, padx=10, pady=10)
travelMethod_combobox.grid(row=1, column=0, padx=10, pady=10)

"""This sets the drop down boxes to a default menu item that can be changed when selecting a location"""
input_combobox.set('Choose Location')
output_combobox.set('Choose Location')
travelMethod_combobox.set('Choose method of travel')

"""This generates the calculate button to calculate the distance"""
calculate_button = tkinter.Button(root, text='Calculate', font=field_font, bg=button_color, command=calculate)
calculate_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

root.mainloop()