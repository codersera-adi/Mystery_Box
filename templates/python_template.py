import requests
import random

# Example API call
url = "https://api.quotable.io/random"

data = requests.get(url).json()
print(data)
