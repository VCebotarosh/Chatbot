# Import required libraries
import socket
import threading
import sys
import datetime
from emoji_dictionary import emoji

HOST = "127.0.0.1"
PORT = 1234
LISTENER_LIMIT = 5
active_client = []  # all currently connected users


def main():
    # AF_INET means that we will use IPv4 adresses
    # SOCK_STREAM means that we will use TCP/IP protocol instead of
    # using the UDP protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"The server is running on {HOST} {PORT}")
    except:
        sys.exit(f"Unable to bind to host {HOST} and port {PORT}")

    server.listen(LISTENER_LIMIT)

    while True:
        client_socket, address = server.accept()
        print(f"Succesfully connected to client {address[0]}, {address[1]}")

        threading.Thread(target=client_handler, args=(client_socket,)).start()


def client_handler(client):
    while True:
        # Receive and decode any information that the user sends of length 2048
        username = client.recv(2048).decode("utf-8")
        if username != "":
            active_client.append((username, client))
            send_messages_to_all(
                f"SERVER~{username}~{datetime.datetime.now().strftime('%H:%M')} joined the chat"
            )
            break
        else:
            print("Client username is empty")
    threading.Thread(target=listen_for_messages, args=(client, username)).start()


# Listen for any upcoming messages from a client
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            message = check_messages_for_bad_words(message, bad_word_list_creator)
            message = convert_symbols_to_emoji(message)
            final_message = (
                f"{username}~{message}~{datetime.datetime.now().strftime('%H:%M')}"
            )
            send_messages_to_all(final_message)
        else:
            print(f"THe message sent from the client {username} is empty")


def check_messages_for_bad_words(message, list_creator):
    words = list_creator()
    for word in words:
        if word in message.split(" "):
            message = message.replace(word, "*" * len(word))
    return message

def bad_word_list_creator():
    words = []
    with open("swearWords.txt", "r") as f:
        for word in f:
            words.append(word.rstrip())
    return words

def convert_symbols_to_emoji(message):
    for key, value in emoji.items():
        if key in message:
            message = message.replace(key, value)
    return message

def send_message_to_client(client, message):
    client.sendall(message.encode())


def send_messages_to_all(message):
    for user in active_client:
        send_message_to_client(user[1], message)

def number_of_active_users(active):
    return len(active)

if __name__ == "__main__":
    main()
