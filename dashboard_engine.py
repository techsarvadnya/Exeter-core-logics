# 1. Battery Saver Logic
def battery_gate(level):
    if level <= 20:
        return "Low Battery - Saver Mode ON"
    else:
        return "Battery OK - Normal Mode"

# 2. Subscription Plan Logic
def check_plan(user_plan):
    if user_plan == "Pro":
        return "All Courses + AI Tutor Unlocked"
    elif user_plan == "Basic":
        return "Basic Courses Only"
    else:
        return "Please Upgrade Plan"

# 3. Certificate Eligibility Logic
def issue_certificate(score, attendance):
    if score >= 80 and attendance >= 90:
        return "Eligible for Certificate"
    else:
        return "Requirements Not Met"

# 4. MASTER FEATURE: Complete Dashboard Access Engine
def student_dashboard_engine(battery_level, plan_type, score, attendance):
    print("--- PHOENIX-LEARN SYSTEM STATUS ---")
    
    # Battery Check
    sys_battery = battery_gate(battery_level)
    print("Device Status:", sys_battery)
    
    # Plan Access Check
    sys_access = check_plan(plan_type)
    print("Account Access:", sys_access)
    
    # Certification Check
    sys_cert = issue_certificate(score, attendance)
    print("Certificate Eligibility:", sys_cert)

# System Test Call
student_dashboard_engine(85, "Pro", 92, 95)
