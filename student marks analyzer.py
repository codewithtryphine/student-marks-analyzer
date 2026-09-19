marks = [72, 45, 88, 51, 39]

average = sum(marks) / len(marks)
print("Average:", average)

maximum = max(marks)

minimum = min(marks)

passed = 0
failed = 0

for mark in marks:
    if mark >= 50:
        passed =passed +1
        
    else:
        failed = failed + 1

print("Highest:", maximum)
print("Lowest:", minimum)
print("Passed:", passed)
print("Failed:", failed)