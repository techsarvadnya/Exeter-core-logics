# Phoenix-Learn: Subscription Entitlement Engine
# Purpose: Dynamic tier-based access control system based on user membership levels.
# Logic: Evaluates explicit string inputs using an sequential evaluation waterfall (if-elif-else).

def check_plan(user_plan):
    # Tier 1: Highest privilege check (Pro Access)
    if user_plan == "Pro":
        return "All Courses + AI Tutor Unlocked"
    # Tier 2: Mid-level access evaluation (Basic Access)
    elif user_plan == "Basic":
        return "Basic Courses Only"
    # Fallback Tier: Invalid/Free user profile redirect
    else:
        return "Please Upgrade Plan"

# Test Executions across all valid and invalid subscription tiers
print(check_plan("Pro"))
print(check_plan("Basic"))
print(check_plan("Free"))
