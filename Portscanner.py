import socket 
import threading
import time

while True:
    while True:
        user_input = input("Scann [S] or exit [X]: ")
        if user_input == "X":
            exit()
        if user_input == "S":
            target = input("Enter scann target: ")
            break
        if user_input != "S" or "X":
            print("Please enter 'S' or 'X'")
            continue


    while True:
        try:
            port_range_start = int(input("Enter Port Start: "))
            port_range_end = int(input("Enter Port End: "))
            break
        except ValueError:
            print("Please enter valid Port")
            continue

    print("-----------------------------")

    def port_scanner(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            print(f"Port {port} is open")
        except:
            pass

    for port in range(port_range_start, port_range_end):
        time.sleep(0.01)
        thread = threading.Thread(target = port_scanner, args=[port])
        thread.start()

    print("-----------------------------")

    continue