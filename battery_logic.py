# Phoenix-Learn: Battery Gate & Power Saver System
# Purpose: Monitors device battery levels to automatically trigger system power profiles.
# Logic: Evaluates numerical threshold boundaries using binary decision logic (if-else).

def battery_gate(level):
    # Boundary Check: Evaluates if battery percentage drops to critical threshold (<= 20)
    if level <= 20:
        status = "Low Battery - Saver Mode ON"
    # Fallback Profile: Standard operational state for safe energy levels
    else:
        status = "Battery OK - Normal Mode"

    return status

# Test Executions: Validating threshold response at 15% and 85%
print(battery_gate(15))
print(battery_gate(85))
