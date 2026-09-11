def evaluate_quiz(correct_answers, total_questions, plan_type):
    Score_percentage = (correct_answers / total_questions) * 100
    
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
