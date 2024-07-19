def outer_function(x):
    def inner_function(y):
        return x + y  # inner function has access to x from the outer scope
    return inner_function  # return the inner function as a closure

# Create a closure by calling the outer function
closure = outer_function(10)

# Use the closure
result = closure(5)  # This will return 15 (10 + 5)
