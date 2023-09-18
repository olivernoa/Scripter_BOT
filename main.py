import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} is down (Status Code: {response.status_code})")
    except requests.ConnectionError:
        print(f"{url} is down!")

if __name__ == "__main__":
    website_url = "https://scripter.geekybloxyt.repl.co/"
    interval = 2
    run_time = 900  # 15 minutes in seconds

    total_time = 0
    while total_time < run_time:
        check_website(website_url)
        time.sleep(interval)
        total_time += interval
