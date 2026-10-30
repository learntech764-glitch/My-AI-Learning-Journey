import time

def fetch_data(name):
    print(f"Fetching data for {name}...")
    time.sleep(2)  # Simulate a delay in fetching data
    print(f"Data fetched for {name}.")
   
def main():
    fetch_data("users")
    fetch_data("orders")
    fetch_data("products")

start_time = time.time()
main()
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")