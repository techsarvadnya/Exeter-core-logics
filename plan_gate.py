def check_plan(user_plan):
    if user_plan == "Pro":
        return "All Courses + AI Tutor Unlocked"
    elif user_plan == "Basic":
        return "Basic Courses Only"
    else:
        return "Please Upgrade Plan"

# Test calls
print(check_plan("Pro"))
print(check_plan("Basic"))
print(check_plan("Free"))
