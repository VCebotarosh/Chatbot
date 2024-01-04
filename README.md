  # VMessenger (Messenger Chat Application)
    #### Video Demo:  https://youtu.be/6ZJXF-RU1Ac
    #### Description: A chat application that allows friends (up to 5) to communicate with each other

    I designed this project as part of CS50P homework. In this application, I tried to implement something
    new for me, the socket library with which I haven't worked. This is my first try using it in real code.
    I built a chat application because it sounded interesting to me and it was also fun to build because I
    learned a lot of new information.

    This project consists of mainly two parts: server_project.py and client_project.py. The first one
    is responsible for server-side code and the second one is responsible for client-side code.

    The server tries to establish a connection to IP and PORT and is set to 5 listeners. It is responsible
    to handle the new client(its username) as well as their messages. The client_handler function is responsible for
    handling the username. It accepts the socket as input, decodes the message in utf-8 and than concatenates the message
    so that the final message has the following structure: "[Username]~Message~Date". The same method is used for listening for new
    messages. The server receives and decodes the message than checks for swear words than converts any symbold to emoji (if any). It also
    takes as the input a socket.


    Responsible for checking for bad words is check_messages_for_bad_words that takes as parameters a message and another function that creates
    the bad words list. check_messages_for_bad_words splits every word by space so as not to display asterisks in hello when printed. It returns the
    message with asterisks instead of bad words.

    As for converting symbols to emojis comes the convert_symbols_to_emoji function. It takes as input the message and checks if there are any symbols that
    match any emoji. If yes, they convert these symbols using a dictionary. This functions returns the message with emojis.

    The clients pass their username in the box and when clicked, the JOIN button is inactive. When the JOIN button is pressed, the client try to
    connect to the socket and to establish a connection via "connect" function implemented in the client_project.py. It takes no arguments as input
    and has no return value. It just takes the username, displays on the screen if it was added to the chat and sets up a thread that listens for any
    upcoming messages from the server

    The "send" function is as simple as it sounds. It has no arguments to pass and does not return anything. It just sends the message that is written
    in the textbox and then deletes the contents of the textbox so as to have space for new messages.

