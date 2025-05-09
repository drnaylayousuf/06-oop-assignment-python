# Create a decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the original function
    return wrapper

# Apply the decorator to say_hello function
@log_function_call
def say_hello():
    print("Hello!")

# Call the function
say_hello()
