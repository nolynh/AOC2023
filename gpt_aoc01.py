def extract_calibration_values(document):
    total_calibration = 0

    for line in document:
        # Find the first and last digits in the line
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())

        # Combine the first and last digits to form a two-digit number
        calibration_value = int(first_digit + last_digit)

        # Add the calibration value to the total
        total_calibration += calibration_value

    return total_calibration

# Example usage
document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

document = open('1.txt').readlines(-1)

result = extract_calibration_values(document)

print("Total Calibration:", result)