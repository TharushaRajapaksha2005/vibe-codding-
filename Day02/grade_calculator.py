def main():
    name = input("Enter student's name: ")
    
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value for the mark.")

    average = sum(marks) / len(marks)
    
    print(f"\nStudent Name: {name}")
    print(f"Average Mark: {average:.2f}")
    
    if average >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

if __name__ == "__main__":
    main()
