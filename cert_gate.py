# Phoenix-Learn: Dynamic Certificate Eligibility Gate
# Purpose: Validates student performance and attendance threshold before certificate issuance.
# Logic: Implements compound logic gates (AND operator) to enforce dual qualification rules.

def issue_certificate(score, attendance):
    # Dual-Validation Gate: Score must be >= 80 AND attendance must be >= 90
    if score >= 80 and attendance >= 90:
        return "Eligible for Certificate"
    else:
        return "Requirements Not Met"

# Test Executions
print(issue_certificate(91, 95))  # Pass: Both criteria met
print(issue_certificate(33, 67))  # Fail: Neither criteria met
