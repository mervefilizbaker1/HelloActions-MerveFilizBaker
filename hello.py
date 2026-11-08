import os

who_to_greet = os.getenv("WHO_TO_GREET", "GitHub Actions Student")

print(f"Hello {who_to_greet}!")
print("This program is running inside GitHub Actions.")
