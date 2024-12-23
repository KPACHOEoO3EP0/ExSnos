import requests
import random
import time

emails = [
    "sumvdnature@gmail.com",
    "kerasinoviy4d@gmail.com",
    "40tutnatured@gmail.com",
    "nemobilen120@gmail.com",
    "urodecc990@gmail.com",
    "poryadot503@gmail.com",
    "poradoxpora@gmail.com",
    "recrutivnost@gmail.com",
    "bolotny11@gmail.com",
    "her4sima999@gmail.com",
    "helpex100@gmail.com",
    "extalstg10@gmail.com",
    "gerasimob12@gmail.com",
    "sasham1d@gmail.com",
    "rexander@gmail.com"
]

phones = [
    "+74330332552",
    "+71025777325",
    "+75333574269",
    "+73683703849",
    "+74091498519",
    "+380570392614",
    "+380412853796"
]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
]

def send_support_request(message, email, phone):
    url = "https://telegram.org/support"
    payload = {
        "message": message,
        "email": email,
        "phone": phone,
        "setln": "ru"
    }
    headers = {
        "User-Agent": random.choice(user_agents)
    }
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        return response.status_code == 200
    except requests.exceptions.Timeout:
        print("\033[91m>Ошибка: Превышено время ожидания запроса. Повторная попытка через некоторое время.\033[0m")
        time.sleep(random.uniform(2, 5))
        return False
    except requests.exceptions.RequestException as e:
        print(f"\033[91m>Ошибка: {e}\033[0m")
        return False

def print_centered(text):
    columns = 80
    padding = (columns - len(text)) // 2
    print(" " * padding + text)

def print_banner():
    banner = """
    ______     _____                           
   / ____/  __/ ___/____  ____  ________  _____
  / __/ | |/_/\__ \/ __ \/ __ \/ ___/ _ \/ ___/
 / /____>  < ___/ / / / / /_/ (__  )  __/ /    
/_____/_/|_|/____/_/ /_/\____/____/\___/_/     
                                               """
    print_centered(banner)

def main():
    print_banner()
    message = input("[ES] Введите текст поддержки: ")
    num_requests = int(input("[ES] Сколько репортов отправить: "))

    for i in range(num_requests):
        email = random.choice(emails)
        phone = random.choice(phones)
        success = send_support_request(message, email, phone)
        if success:
            print(f"\033[92m>Запрос {i + 1} отправлен успешно\033[0m")
        else:
            print(f"\033[91m>Запрос {i + 1} не отправлен\033[0m")
        time.sleep(random.uniform(3, 8))

if __name__ == "__main__":
    main()
