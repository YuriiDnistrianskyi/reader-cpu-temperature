import requests
import asyncio
import time

PARAMETER: str = "Core Max"
DEBOUNCE_READ: float = 5.0

parameter_value = None
is_recursive = True

def main():
    global is_recursive
    while True:
        data = requests.get('http://127.0.0.1:8085/data.json').json()

        if not is_recursive:
            is_recursive = True

        asyncio.run(recursive_find(data))

        print(parameter_value)

        time.sleep(DEBOUNCE_READ)

async def recursive_find(data):
    global is_recursive, parameter_value
    if is_recursive:
        if isinstance(data, dict):
            if data.get('Text') == PARAMETER:
                parameter_value = data.get('Value')
                is_recursive = False
            else:
                for value in data.values():
                    await recursive_find(value)
        elif isinstance(data, list):
            for value in data:
                await recursive_find(value)
    else:
        return

if __name__ == "__main__":
    try:
        print("Start read 🌡️")
        main()
    except Exception as ex:
        print(f"Error: {ex}")
        print("End read ⛔")
        exit(1)
    except KeyboardInterrupt:
        print("End read ✅")
        exit(0)
