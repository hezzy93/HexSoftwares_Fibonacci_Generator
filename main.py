# Fibonacci function
def generate_fibonacci(n):
        if n <= 0:
                return None
                
        fib_sequence = []
        a, b = 0, 1
        
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        
        return fib_sequence

while True:
    print('\nWelcome to My Fibonacci Generator'"\n"
          'Enter 1 to USE'"\n"
          'Enter 0 to QUIT')
    
    choice = input("\nEnter your choice (1 or 0): ")

    if choice == "1":
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate: "))
            if n <=0:
                 print("Please enter a positive integer greater than 0.")
            else:
                 print(f"\nThis is the first {n} Fibonacci sequence:\n{generate_fibonacci(n)}")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '0':
        print('Goodbye')
        break
    else:
        print("Invalid choice. Please enter 1 or 0")

    