def main():
    while True:
        # Ask for student's name
        name = input("Enter student's name (or type 'Exit' to quit): ")

        if name.lower() == 'exit':
            break

        try:
            # Ask for 3 subject marks
            mark1 = float(input("Enter marks for Subject 1: "))
            mark2 = float(input("Enter marks for Subject 2: "))
            mark3 = float(input("Enter marks for Subject 3: "))

            # Calculate the average
            average = (mark1 + mark2 + mark3) / 3

            # Determine grade
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"

            # Display results
            print("-" * 30)
            print(f"Name    : {name}")
            print(f"Average : {average:.1f}")
            print(f"Grade   : {grade}")
            print("-" * 30 + "\n")

        except ValueError:
            print("Error: Please enter valid numeric marks.\n")

if __name__ == "__main__":
    main()
