import time

from demo.config import settings


def main():
    print(settings.app_name)
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
