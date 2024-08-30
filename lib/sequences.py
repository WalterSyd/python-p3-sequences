

def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        print("[]")
        return
    if length == 1:
        print("[0]")
        return

    # Initialize the Fibonacci sequence
    fib_list = [0, 1]
    
    # Generate the sequence up to the specified length
    while len(fib_list) < length:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    
    # Print the result
    print(fib_list)

print_fibonacci(9)