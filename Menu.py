def make_menu(argument,tree_data):
    
    menu = {
        1: "Make a Decison Tree",
        2: "Apply the Decison Tree ",
        3: "Save the current decison Tree",
        4: "Load a Decison Tree",
        5: "Quit",
    }
    print (menu.get(argument, "Invalid Choice"))
    return(argument)
                           
def one():
    return(print("Called 1") 
           
def two():
    return(print("Called 2")
           
def three():
    return(print("Called 3") 
           
def four():
    return(print("Called 4")
           
def five();
    return(print("Called 5")

def numbers_to_choice(argument):
    menu = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
    }
    # Get the function from menu dictionary
    choice = menu.get(argument, lambda: "Invalid month")
    func = choice
    return(func)

class Menu(object):
    def numbers_to_choice(self, argument):
        """Dispatch method"""
        method_name = 'choice_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def choice_1(self):
        return "one"
 
    def choice_2(self):
        return "two"
 
    def choice_3(self):
        return "three"    
    
    def choice_4(self):
        return "four"
    
    def choice_5(self):
        return "five"
 
