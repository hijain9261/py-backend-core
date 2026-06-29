# Method Overriding
class api_fetch:
    def fetch(self):
        print("Fetching data from API...")

class db_fetch:
    def fetch(self):
        print("Fetching data from Database...")

class s3_fetch:
    def fetch(self):
        print("Fetching data from S3...")

obj = s3_fetch()
obj.fetch()  # Output: Fetching data from S3...