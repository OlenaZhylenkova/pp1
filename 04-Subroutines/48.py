# 49.	The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def max_dice_streak(dice):
    if not dice:
        return 0

    max_streak = 1  # Initialize the maximum streak to 1
    current_streak = 1 # Initialize the current streak to 1
    max_streak_number = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > max_streak:
            max_streak = current_streak
            max_streak_number = dice[i]

    return max_streak_number

# Sample results
print(max_dice_streak("5233165554211"))  # Output: 5
print(max_dice_streak("2133"))           # Output: 3
