def ask_question(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        else:
            print("Please answer with 'yes' or 'no'.")

def evaluate_performance():
    print("Employee Performance Evaluation Expert System\n")
    
    attendance = ask_question("Is the attendance above 80%?")
    projects = ask_question("Has the employee completed more than 5 projects?")
    feedback = ask_question("Is the peer feedback mostly positive?")

    score = sum([attendance, projects, feedback])
    
    if score == 3:
        result = "Excellent"
    elif score == 2:
        result = "Good"
    elif score == 1:
        result = "Average"
    else:
        result = "Needs Improvement"

    print(f"\nPerformance Evaluation Result: {result}")


evaluate_performance()
