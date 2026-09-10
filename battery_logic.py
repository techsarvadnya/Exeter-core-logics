def battery_gate(level):
    if level <= 20:
        status = "Low Battery - Saver Mode ON"
    else:
        status = "Battery OK - Normal Mode"

    return status

# Test calls
print(battery_gate(15))
print(battery_gate(85))
