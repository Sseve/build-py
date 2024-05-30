import time

from demo.config import settings


def main():
    try:
        while True:
            time.sleep(2)
            print(time.ctime(), settings.app_name)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
