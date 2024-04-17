rules = {
    "rule1": "If the employee meets all project deadlines, add 20 points to their score.",
    "rule2": "If the employee consistently exceeds expectations, add 30 points to their score.",
    "rule3": "If the employee shows initiative and takes on additional responsibilities, add 15 points to their score.",
    "rule4": "If the employee is frequently absent or misses deadlines, subtract 25 points from their score.",
    "rule5": "If the employee consistently performs below expectations, subtract 35 points from their score."
}

def evaluate_employee_performance(deadlines_met, expectations_exceeded, initiative_taken, absences, performance_below_expectations):
    score = 0
    if deadlines_met:
        score += 20
    if expectations_exceeded:
        score += 30
    if initiative_taken:
        score += 15
    if absences:
        score -= 25
    if performance_below_expectations:
        score -= 35
    return score

employee_data = {}
n = int(input("Enter the number of employees you want to evaluate: "))
for i in range(n):
    name = input("Enter the name of the employee: ")
    data = {
        "deadlines_met": bool(int(input("Enter 1 if the employee meets all project deadlines, 0 otherwise: "))),
        "expectations_exceeded": bool(int(input("Enter 1 if the employee consistently exceeds expectations, 0 otherwise: "))),
        "initiative_taken": bool(int(input("Enter 1 if the employee shows initiative and takes on additional responsibilities, 0 otherwise: "))),
        "absences": bool(int(input("Enter 1 if the employee is frequently absent or misses deadlines, 0 otherwise: "))),
        "performance_below_expectations": bool(int(input("Enter 1 if the employee consistently performs below expectations, 0 otherwise: ")))
    }
    employee_data[name] = data

print("Rules for employee evaluation:")
for rule in rules.values():
    print(f"- {rule}")

print("\nEmployee Evaluation Results:")
for name, data in employee_data.items():
    score = evaluate_employee_performance(**data)
    print(f"Employee {name} scored {score} points.")
