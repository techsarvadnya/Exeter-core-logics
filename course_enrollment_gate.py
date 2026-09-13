# Phoenix-Learn: Dynamic Course Enrollment Gate
# Purpose: Validates student course registration based on prerequisites, seat availability, and account status.
# Logic: Multi-variable evaluation engine using nested boolean logic and guard clauses.

def evaluate_enrollment(prereq_completed, seats_available, account_active):
    # Guard Clause: Check account status first to avoid redundant evaluations
    if not account_active:
        return "Enrollment Denied: Student Account Inactive"

    # Compound Gate: Must have completed prerequisites AND seats must be > 0
    if prereq_completed and seats_available > 0:
        return "Enrollment Approved: Seat Reserved"
    elif not prereq_completed:
        return "Enrollment Pending: Missing Prerequisite Courses"
    else:
        return "Enrollment Waitlisted: Course Full"

# Test Calls: Testing different boundary conditions
print(evaluate_enrollment(True, 5, True))   # Standard Pass -> Approved
print(evaluate_enrollment(False, 10, True))  # Missing Prereq -> Pending
print(evaluate_enrollment(True, 0, True))    # No Seats -> Waitlisted
print(evaluate_enrollment(True, 2, False))   # Inactive User -> Denied
