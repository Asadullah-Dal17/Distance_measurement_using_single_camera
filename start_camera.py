import sys

from Speed.updated_speed import *


def main():
    gui = False
    if len(sys.argv) >= 2:
        gui = sys.argv[1] == 'gui'
    for (distance, speed, frame) in get_incoming_danger(gui):
        # print(f"distance: {distance} , speed: {speed}")
        if should_alert(distance, speed):
            alert(distance, speed, frame)


def alert(distance, speed, frame):
    print(f"ALERT: distance: {distance} , speed: {speed}")


def should_alert(distance, speed):
    return distance < 2 and speed > 3 or distance < 0.5


if __name__ == '__main__':
    main()
