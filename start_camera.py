import sys

import requests

from Speed.updated_speed import *


def main():
    gui = False
    if len(sys.argv) >= 2:
        gui = sys.argv[1] == 'gui'
    for (distance, speed, frame) in get_incoming_danger(gui):
        # print(f"distance: {distance} , speed: {speed}")
        if should_alert(distance, speed):
            alert(distance, speed, frame)
        else:
            relax(calculate_danger(distance, speed))


def send_frame(frame):
    pass


def notify_server(danger, alert=1):
    try:
        params = {'danger': danger, 'alert': alert}
        response = requests.post('http://localhost:3001/notify', params=params)
        print(response)
    except Exception as e:
        pass


def calculate_danger(distance, speed):
    danger = 15 / distance + 4 * speed
    return danger


relax_counter = 0


def relax(danger):
    global relax_counter
    print("relaxing")
    relax_counter += 1
    if relax_counter >= 10:
        notify_server(danger=danger, alert=0)
        relax_counter = 0


def alert(distance, speed, frame):
    send_frame(frame)
    notify_server(danger=calculate_danger(distance, speed))
    print(f"ALERT: distance: {distance} , speed: {speed}")


def should_alert(distance, speed):
    return (speed >= 0 or distance < 0.5) and calculate_danger(distance, speed) > 30


if __name__ == '__main__':
    main()
