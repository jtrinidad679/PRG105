"""
A nutritionist who works for a fitness club helps members by evaluating their diets.
As part of her evaluation, she asks members for the number of fat grams, carbohydrate
grams, and protein grams that they consumed in a day. Then, she calculates the number
of calories that result from the fat, using the following formula:

calories from fat = fat grams X 9

Next, she calculates the number of calories that result from the carbohydrates,
using the following formula:

calories from carbs = carb grams X 4

Next, she calculates the number of calories that result from the proteins,
using the following formula:

calories from protein = protein grams X 4


Use a different function for each nutrient to make calculations
by nutrient, and print the calories for that nutrient on screen.
Return the results from each function to variables in the main method.
Add the variables in the main method to display the total calories
for the day. Use meaningful names for each variable and function.
Add a comment to each function describing what it does.
 """
# The main function calls the other functions to work
# and then it prints their total calories for the day

# I got main to call the other functions properly but
# wasn't sure how to total them all up so I assigned
# new variables (fat, carb, protein) to the existing
# functions and added them together to get the total!


def main():
    fat = fat_calories()
    carb = carb_calories()
    protein = protein_calories()
    print("You ate a total of " + str(fat + carb + protein) + " calories today.")


# Each function here, (fat_calories, carb_calories, and protein_calories,
# all do the same thing. They ask the user to input how many grams of what
# they ate in that day, and then print the amount back to the user. Then, I
# returned the results to main and assigned new variables to total the calories.
# I'm not entirely sure if return total_(fat, carbs, protein) actually does anything.


def fat_calories():
    total_fat = int(input("How many grams of dat did you eat today? ")) * 9
    print("You ate " + str(total_fat) + " calories from fat today.")
    return total_fat


def carb_calories():
    total_carbs = int(input("How many grams of carbs did you eat today? ")) * 4
    print("You ate " + str(total_carbs) + " calories from carbs today.")
    return total_carbs


def protein_calories():
    total_protein = int(input("How many grams of protein did you eat today? ")) * 4
    print("You ate" + str(total_protein) + "calories from protein today.")
    return total_protein


main()
