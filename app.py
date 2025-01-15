#This function takes a list of ingredients and simulates
#making a sandwhich
def build_sandwich(ingredients): #function and in () is parameter functions takes
    #Check if the ingredients list is empty
    if not ingredients:
        print("You need to choose some ingredients!")
        return

    print("Let's make a sandwich!")
    print("First we grab some bread...")

    #Now use a loop - perform task multiple times
    #Loop thru ingredients list and add it to the sandwhich
    # i in loop is the current item
    # enumerate gives ingredient and it's position in list
    # include ingredient in enumerate to specify ingredient
    for i, ingredient in enumerate(ingredients, 1):
        print(f"Adding {ingredient}...") #f puts the variable in the string, also with the varaible in {}

    print("And top it with bread!")

    #Join all ingredients together for a final message
    #\n tell computer there is to be extra line of space
    #Use join function to add ingredients chosen to the final print statement
    print(f"\nCongrats! You made a {' and '.join(ingredients)} sandwich!")

    # create main function
    # calls build_sandwhich
    # uses error handling and user input
def main():
    try:
        # use try to error handle
        print("Welcome to the Sandwich Maker!")

        # Get ingredients from user as a comma-seperated string
        # ingredients list from user input
        ingredients_input = input("Enter ingredients (seperated by commas): ")

        #Convert the input string to a list
        #1. Split string at commas
        #2. Remove extra whitespace from each ingredient
        # define list with square brackets []
        ingredients = [i.strip() for i in ingredients_input.split(",")] #splitting current ingredient based on comma, pass comma to strip function, and stripping off white space

        # call the sandwhich building function with our list of ingredients
        build_sandwich(ingredients)

    # catch any errors that happen during execution
    # catch error with except
    # use Exception to declare all errors
    except Exception as e:
        print("Oops, something went wrong. Let's try again!"); #print error message

#Standard python code to only run the main function
if __name__ == "__main__":
    main()