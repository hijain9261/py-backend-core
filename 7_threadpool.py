from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url: str):
    print(f"Fetching data from {url}...")
    time.sleep(5)
    result = f"Data from {url}"
    print(f"Finished fetching data from {url}") 
    return result


urls = [
    "https://example.com/data1", 
    "https://example.com/data2", 
    "https://example.com/data3", 
    "https://example.com/data4", 
    "https://example.com/data5"
]

with ThreadPoolExecutor(max_workers=len(urls)) as executor:
    # Wrapped executor.map in list() to extract the returned values
    result = list(executor.map(fetch_url, urls))
    print(result)



