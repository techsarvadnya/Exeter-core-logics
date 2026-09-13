# Phoenix-Learn: Dynamic Smart Admission & Financial Aid Engine
# Purpose: Evaluates grade eligibility and automates merit-based scholarship fee reductions.
# Logic: Combines multi-path string logic with compound numeric threshold gates and f-string formatting.

def calculate_admission(grade, score, fees):
    # Section 1: Grade Eligibility Classification (String Waterfall)
    if grade == "Class 10":
        base_status = "High School Eligible"
    elif grade == "Class 9":
        base_status = "Middle School Eligible"
    else:
        base_status = "Grade Not Supported"

    # Section 2: Compound Scholarship Gate & Financial Calculation
    # Requires high performance (score >= 90) AND substantial base fee (> 5000)
    if score >= 90 and fees > 5000:
        final_fees = fees - 1000
        scholarship_status = "Scholarship Awarded!"
    else:
        final_fees = fees
        scholarship_status = "No Discount"

    # Section 3: Returns aggregated status report using F-string extrapolation
    return f"Status: {base_status} | {scholarship_status} | Final Fees: {final_fees}"

# Test Executions: Validating high school scholarship, middle school full-fee, and unsupported grades
print(calculate_admission("Class 10", 95, 6000))
print(calculate_admission("Class 9", 75, 4000))
print(calculate_admission("Class 8", 92, 6000))
