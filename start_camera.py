import os
import sys
import argparse
import requests

from Speed.updated_speed import *


def main(gui, server_hostname):
    for (distance, speed, frame) in get_incoming_danger(gui):
        # print(f"distance: {distance} , speed: {speed}")
        if should_alert(distance, speed):
            alert(distance=distance, speed=speed, frame=frame, server_hostname=server_hostname)
        else:
            relax(danger=calculate_danger(distance, speed), server_hostname=server_hostname)


def send_frame(frame):
    pass


def notify_server(server_hostname, danger, alert=1):
    try:
        params = {'danger': danger, 'alert': alert}
        response = requests.post(f'http://{server_hostname}/notify', params=params)
        print(response)
    except Exception as e:
        pass


def calculate_danger(distance, speed):
    danger = 15 / distance + 4 * speed
    return danger


relax_counter = 0


def relax(server_hostname, danger):
    global relax_counter
    print("relaxing")
    relax_counter += 1
    if relax_counter >= 10:
        notify_server(server_hostname=server_hostname, danger=danger, alert=0)
        relax_counter = 0


def alert(server_hostname, distance, speed, frame):
    send_frame(frame)
    notify_server(server_hostname=server_hostname, danger=calculate_danger(distance, speed))
    print(f"ALERT: distance: {distance} , speed: {speed}")


def should_alert(distance, speed):
    return (speed >= 0 or distance < 0.5) and calculate_danger(distance, speed) > 30


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server-hostname", default=os.environ.get("SERVER_URL", "localhost:3001"),
                        help="The name of the server, INCLUDING port (for example 127.0.0.1:1337")
    parser.add_argument("--gui", action="store_true")
    args = parser.parse_args()
    main(gui=args.gui, server_hostname=args.server_hostname)
