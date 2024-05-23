from assistant import Assistant

def main():
    assistant = Assistant()
    while True:
        assistant.handle_command()

if __name__ == "__main__":
    main()
