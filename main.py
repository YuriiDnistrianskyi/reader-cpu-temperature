import requests
import asyncio

parameter: str = "Core Max"

parameter_value = None
is_recursive = True

async def main():
    data = requests.get('http://127.0.0.1:8085/data.json').json()

    await recursive_find(data)

    print(parameter_value)

async def recursive_find(data):
    global is_recursive, parameter_value
    if is_recursive:
        if isinstance(data, dict):
            if data.get('Text') == parameter:
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
    asyncio.run(main())
