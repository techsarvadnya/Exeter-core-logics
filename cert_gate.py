def issue_certificate(score, attendance):
    if score >= 80 and  attendance >= 90:
        return "Eligible for Certificate"
    else:
        return "Requirements Not Met"

print(issue_certificate(91, 95))
print(issue_certificate(33, 67))
