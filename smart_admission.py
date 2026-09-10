def calculate_admission(grade, score, fees):
    # 1. Grade Eligibility Check
    if grade == "Class 10":
        base_status = "High School Eligible"
    elif grade == "Class 9":
        base_status = "Middle School Eligible"
    else:
        base_status = "Grade Not Supported"

    # 2. Scholarship & Fee Calculation
    if score >= 90 and fees > 5000:
        final_fees = fees - 1000
        scholarship_status = "Scholarship Awarded!"
    else:
        final_fees = fees
        scholarship_status = "No Discount"

    # 3. Combine Everything into One Clean Return Statement
    return f"Status: {base_status} | {scholarship_status} | Final Fees: {final_fees}"

# Test Calls
print(calculate_admission("Class 10", 95, 6000))
print(calculate_admission("Class 9", 75, 4000))
print(calculate_admission("Class 8", 92, 6000))
