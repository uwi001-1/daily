#Find the longest daily streak of a habit

def longest_streak(habits):
    streak = 0

    for habit in habits:
        if habit:
            streak += 1
        else:
            streak = 0

    return streak

hab = [True, True, False, True, True, True, True]
print(f"The longest streak is: {longest_streak(hab)}")
