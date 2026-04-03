from app import main
from app.mqtt import connect_broker

if __name__ == "__main__":
    client = connect_broker()
    try:
        client.loop_start()
        print("Start read 🌡️")
        main(client)
    except Exception as ex:
        print(f"Error: {ex}")
        print("End read ⛔")
        exit(1)
    except KeyboardInterrupt:
        client.loop_stop()
        print("End read ✅")
        exit(0)
