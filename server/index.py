import socket
import threading
from os import system, name


print("Chat Server\n(c) 2019 - Matix Media, Inc.\n\n\n")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("Chat Server\n(c) 2019 - Matix Media, Inc.\n\n\n")

Running = True

print("Generating Server Socket...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Binding Server Socket...")

sock.bind(("0.0.0.0", 1101))

print("Prepare to listen on Port 1101...")

sock.listen(1)
print("Now listening! (...)", end="\n\n")

connections = []
ip_s = []


def command_operator():
    global Running
    global sdResAccepting

    while Running:
        command = input("")
        if "list" == command:
            print("\nListing all connections:")
            for ip in ip_s:
                print("  - @", str(ip), sep="")
        elif "exit" == command:
            print("Shutting down the Server...", end="\n\n")
            Running = False
            print("Waiting for response...")
            print("Disconnecting from Clients...")
            for connection in connections:
                connection.close()

            print("Closing Connecting...")
            sock.close()
            print("Server closed.\n     Exit!")
            exit()
        elif "cls" == command:
            clear()
        elif "clear" == command:
            clear()
        else:
            print("Could not the command ", command)


def cHandler(c, a):
    print("\n+", "@" + str(a), "JOIN", end="\n\n")

    while Running:
        global connections

        try:
            data = c.recv(1024)

        except ConnectionResetError:
            print("\n-", "@" + str(a), "LEFT", end="\n\n")
            connections.remove(c)
            c.close()
            break

        print("@" + str(a), "RECV:", str(data, "utf-8"))
        for connection in connections:
            connection.send(bytes(data))

        if not data:
            print("\n-", "@" + str(a), "LEFT", end="\n\n")
            connections.remove(c)
            c.close()
            break

    pass


comThread = threading.Thread(target=command_operator)
comThread.daemon = False
comThread.start()

while Running:
    try:
        c, a = sock.accept()
        cThread = threading.Thread(target=cHandler, args=(c, a))
        cThread.daemon = True
        cThread.start()
        connections.append(c)
        ip_s.append(a)
    except OSError:
        if Running:
            print("Error while accepting request!")

    pass
