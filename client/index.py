import argparse
import socket
import threading



# /////////////////////////
parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="(String): The IP to the Chat Server.")
parser.add_argument("-port", help="(String): The Port of the Chat Server.")
args = parser.parse_args()


# /////////////////////////


def delete_last_lines(n=1):
    pass

class Client:
    def send_msg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))
            delete_last_lines()

    def __init__(self, ip, port):
        print("Generating Socket... (", str(ip), ", ", str(port), ")", sep="")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Connecting...")
        self.sock.connect((str(ip), int(port)))
        print("Connected!")

        print("Setting up...")
        iThread = threading.Thread(target=self.send_msg)
        iThread.daemon = True
        print("... Ready!\nLet's Chat!\n\n\n")
        iThread.start()


        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print("RECV:", str(data, "utf-8"))


print("Starting Client...", end="\n\n")
Client(args.ip, args.port)
