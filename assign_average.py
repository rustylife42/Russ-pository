# Program Name: assign_average.py
# Program Author: Russell Holmes
# Last Edit Date: 10/19/2020

def switch_average(x):
    switch = {
        'A': 100,
        'B': 101,
        'C': 102,
        'D': 103,
        'E': 104,
        'F': 105    # This assignment was exceedingly difficult to understand what you wanted from us, I understand I am
                    # partially to blame for this, though sometimes when the copy-paste strategy of your assignment
                    # details are incorrectly edited to fit the new assignment it makes it impossible to complete the
                    # assignment to your specifications as your specifications are inconsistent or impossible to meet

                    # That said, I gave this assignment my best try, and I hope it is alright,
                    # in future I will ask for clarification earlier in the week
    }
    return switch.get(x, "Invalid Key")

