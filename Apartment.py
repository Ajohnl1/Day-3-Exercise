# Dunder
if __name__ == "__main__":
    # Defining function to search for apartments
    def apt_search1(city, max_rent, min_beds, pets_allowed):

        # Defining the city variable using user input
        city = str(input("Which city are you looking for an apartment in? "))

        # User input for max rent
        max_rent = int(input("What is the maximum budget? "))

        # user input for number of bedrooms
        min_beds = int(input("How many bedrooms do you need? "))

        # user input for pets allowed
        pets_allowed = str(input("Are you looking for a place that allows pets? y/n "))

        # Statement to user
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments,"
              f" all within a budget of ${max_rent}.")

        # bool statement
        if pets_allowed.lower() == "y":
            print("Pets are allowed.")

    apt_search1(2, 3, 4, 5)

    # Function 2 for search with default values for min beds and pets allowed
    def apt_search2(city, max_rent, min_beds=0, pets_allowed=False):

        # When min beds and pets are used in search
        if min_beds and pets_allowed:
            print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments,"
                  f"all within a budget of ${max_rent}. Pets are allowed!")

        # When min beds is used and pets are omitted
        elif min_beds:
            print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments,"
                  f" all within a budget of ${max_rent}.")

        # When Pets are allowed and min beds are omitted
        elif pets_allowed:
            print(f"Welcome to GC Property Management! Looking up listings in {city} within a budget of ${max_rent}. "
                  f"Pets are allowed!")

        # Neither pets or min beds are used in this search
        else:
            print(f"Welcome to GC Property Management! Looking up listings in {city} all within a budget of "
                  f"${max_rent}.")

    # min beds and pets are omitted
    apt_search2('Taylor', 3500)

    # min beds is used and pets are omitted
    apt_search2("Taylor", 1500, min_beds=4)

    # pets are allowed and min beds are omitted
    apt_search2("Taylor", 4000, pets_allowed=True)

    # Plus 100
    def plus_one_hundred(x):
        return x + 100

    result1 = plus_one_hundred(25)
    print(result1)

    # Square Number
    def square_num(x):
        return x ** 2

    result2 = square_num(10)
    print(result2)

    # Concatenate
    def concatenate(x):
        return " - " + x

    result3 = concatenate("hello")
    print(result3)

    # Divide by 3
    def divide_by_three(x):
        return x / 3

    result4 = divide_by_three(30)
    print(result4)
