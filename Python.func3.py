def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return  average

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

num_scores = int(input("How many test scores do you have? "))
scores = []
i = 1

while i <= num_scores:
    score = float(input(f" Enter score {i}: "))
    scores.append(score)
    i = i + 1

average = calculate_average(scores)
letter = get_letter_grade(average)

print("=== GRADE REPORT ===")
print(f"Test Scores: {scores}")
print(f" Average Score: {average}")
print(f"Letter grade: {letter}")