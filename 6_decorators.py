import time

def timer(original_function):  # This is the decorator function that takes the original function as an argument
    
    def wrapper(*args, **kwargs): 
        start_time = time.time()
        
        # 1. Execute the actual function and save its result
        result = original_function(*args, **kwargs)
        
        end_time = time.time()
        print(f"Execution time of '{original_function.__name__}': {end_time - start_time:.4f} seconds")
        
        # 2. Return the result of the original function execution
        return result
        
    return wrapper  # Return the inner wrapper function ready to go

@timer
def process_heavy_data(num_elements: int):
    # Simulating a data processing loop
    total = sum(i * i for i in range(num_elements))
    return total

# Without the decorator, we can manually apply it like this:
# process_heavy_data = timer(process_heavy_data)  # Manually applying the decorator
# result = process_heavy_data(10**6)  # This will print the execution time and return the result
# print(f"Result: {result}")

# With decorator syntax
result = process_heavy_data(10**6)  # This will automatically apply the timer decorator
print(f"Result: {result}")


