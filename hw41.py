import random
import requests
import sys


def generate_random_integers(n):
    return ','.join(str(random.randint(0, 100)) for _ in range(n))


def main():
    
    if len(sys.argv) < 2:
        print("Please provide the size of the dataset as a command-line argument.")
        sys.exit(1)

    try:
        dataset_size = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the dataset size.")
        sys.exit(1)

    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }

    
    URL = "https://db4.us/tech136/statapp.html"
    r = requests.get(URL, headers=headers)
    print(r)
    print(r.content)

    
    scores = generate_random_integers(dataset_size)

    
    r = requests.get(f"https://db4.us/cgi-bin/statapp.py?scores={scores}", headers=headers)
    print(r)
    print(r.content)

if __name__ == "__main__":
    main()
