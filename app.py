while True:
    print("\n--- Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '4':
      print("Exiting the program. Goodbye!")
      break
    elif choice in ('1', '2', '3'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            result = num1 + num2
            print(result)
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")