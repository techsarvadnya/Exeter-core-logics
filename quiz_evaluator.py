# Phoenix-Learn: Quiz Evaluator Module
# Purpose: Calculates percentage scores and determines access tiers based on subscription plans.
# Logic: Combines mathematical operations, multiple boolean conditions (AND), and multi-branch logic (if-elif-else).

def evaluate_quiz(correct_answers, total_questions, plan_type):
    # Dynamic calculation of percentage
    Score_percentage = (correct_answers / total_questions) * 100
    
    # Priority check: High score AND premium plan gets honors status
    if Score_percentage >= 80 and plan_type == "Pro":
        status = "Passed with Honors! Next level unlocked."
    elif Score_percentage >= 50:
        status = "Passed! Good job."
    else:
        status = "Failed. Please retry."

    return f"Score: {Score_percentage}% | Status: {status}"

# Test calls
print(evaluate_quiz(9, 10, "Pro"))
print(evaluate_quiz(6, 10, "Basic"))
print(evaluate_quiz(4, 10, "Pro"))
