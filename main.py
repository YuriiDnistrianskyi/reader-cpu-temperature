from app import main

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
