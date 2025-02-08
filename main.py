import colorama
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

colorama.init(autoreset=True)

user_id = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE + "Enter Github Username: ")

github_url = f"https://github.com/{user_id}"


def refresh_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(github_url)

    try:
        while True:
            time.sleep(1)
            driver.refresh()
            print(f"Page refreshed: {github_url}")
    except KeyboardInterrupt:
        print("Stopping...")
        driver.quit()


num_browsers = 2
threads = []

for _ in range(num_browsers):
    t = threading.Thread(target=refresh_page)
    threads.append(t)
    t.start()


for t in threads:
    t.join()
