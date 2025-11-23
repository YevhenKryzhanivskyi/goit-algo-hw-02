import queue
import random
import time

# Черга заявок
request_queue = queue.Queue()

# Лічильник для унікальних ID заявок
request_id = 0


def generate_request():
    global request_id
    request_id += 1
    processing_time = random.randint(1, 5)
    request = (request_id, processing_time)
    request_queue.put(request)
    print(
        f"[+] Запит {request_id} згенеровано. "
        f"Час обробки: {processing_time} секунд."
    )


def process_request():
    if not request_queue.empty():
        req_id, processing_time = request_queue.get()
        print(f"[-] Обробка запиту {req_id} (час {processing_time} секунд)")
        time.sleep(processing_time)
        print(f"[✓] Запит {req_id} оброблено.")
    else:
        print("[!] Черга порожня, немає заявок для обробки.")
        time.sleep(1)


def main():
    try:
        while True:
            if random.choice([True, False]):
                generate_request()
            process_request()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nЗавершення програми.")


if __name__ == "__main__":
    main()
