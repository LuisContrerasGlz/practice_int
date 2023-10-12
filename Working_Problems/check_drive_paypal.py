def check_driving_eligibility(age):
    try:
        age = int(age)  # Convert input to integer
        if age < 0:
            raise ValueError("Age cannot be negative.")  # Raise an exception for negative age
        elif age < 18:
            drive_car()
        else:
            do_not_drive()
    except ValueError:
        print("Invalid age. Please provide a valid age as a positive integer.")

def drive_car():
    print("You are eligible to drive a car.")

def do_not_drive():
    print("You are not eligible to drive.")

# Test cases
check_driving_eligibility(16)  # Younger than 18, should print "You are not eligible to drive."
check_driving_eligibility(21)  # 18 or older, should print "You are eligible to drive a car."
check_driving_eligibility("abc")  # Invalid age, should print "Invalid age. Please provide a valid age as a positive integer."
check_driving_eligibility(-10)  # Invalid age, should print "Invalid age. Please provide a valid age as a positive integer."
