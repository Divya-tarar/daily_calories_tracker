# Name:Divya
# Date: 9 November 2025
# Project Title: Daily Calorie Tracker

# Welcome message and introduction
print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you track your meals and total calorie intake.\n")

# Task 2: Input & Data Collection

meals = []
calories = []
num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

# Task 3: Calorie Calculations

total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System

if total_calories > daily_limit:
    print("\n You exceeded your daily calorie limit!")
else:
    print("\n You are within your daily calorie limit!")


# Task 5: Neatly Formatted Output

print("\nMeal Name\tCalories")
print("--------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("--------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

print("\nThank you for using the Daily Calorie Tracker!")
