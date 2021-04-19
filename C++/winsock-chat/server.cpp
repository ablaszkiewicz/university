#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <winsock.h>
#include <thread>
#include <vector>
#include <cstring>
#include <sstream>

using namespace std;

struct Client {
    SOCKET socket;
    string name;
};

const int PORT = 1234;

vector<thread> handlers;
vector<Client> clients;

void sendToAllClients(Client owner, char message[]) {
    cout << owner.name << " sent message: " << message << " to all clients" << endl;
    string fullMessage = "[" + owner.name + "]: " + (string)message;
    char* fullMessageChar = new char[fullMessage.length()];
    strcpy(fullMessageChar, fullMessage.c_str());
    for (Client client : clients) {
        if (client.socket == owner.socket) {
            continue;
        }
        send(client.socket, fullMessageChar, 80, 0);
    }
}

void sendToSpecificClient(Client owner, string receiver, char message[]) {
    cout << owner.name << " sent private message: " << message << " to client: " << receiver << endl;

    string fullMessage = "[PRIVATE][" + owner.name + "]: " + (string)message;
    char* fullMessageChar = new char[fullMessage.length()];
    strcpy(fullMessageChar, fullMessage.c_str());

    for (Client client : clients) {
        if (client.name == receiver) {
            send(client.socket, fullMessageChar, 80, 0);
        }
    }
}

void clientHandler(Client client) {
    char buf[80];
    while (recv(client.socket, buf, 80, 0) > 0)
    {
        if (buf[0] != '@') {
            sendToAllClients(client, buf);
        }
        else {
            istringstream iss((string)buf);
            string receiverName;
            string message;

            getline(iss, receiverName, ' ');
            receiverName = receiverName.substr(1, receiverName.length());

            getline(iss, message, ' ');
            char* messageChar = new char[message.length()];
            strcpy(messageChar, message.c_str());

            sendToSpecificClient(client, receiverName, messageChar);
        }
        
        if (strcmp(buf, "KONIEC") == 0)
        {
            closesocket(client.socket);
            WSACleanup();
            return;
        }
    };
}

int main()
{

    WSADATA wsas;
    int result;
    WORD wersja;
    wersja = MAKEWORD(1, 1);
    result = WSAStartup(wersja, &wsas);
    SOCKET s;
    s = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sa;
    memset((void*)(&sa), 0, sizeof(sa));
    sa.sin_family = AF_INET;
    sa.sin_port = htons(PORT);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);

    result = bind(s, (struct sockaddr FAR*) & sa, sizeof(sa));
    result = listen(s, 5);

   

    SOCKET si;
    struct sockaddr_in sc;
    int lenc;

    

    while (1) {
        lenc = sizeof(sc);
        si = accept(s, (struct sockaddr FAR*) & sc, &lenc);
        
        char buf[80];
        recv(si, buf, 80, 0);

        cout << buf << " connected. Clients count: " << clients.size() + 1 << endl;
        
        Client newClient;
        newClient.socket = si;
        newClient.name = buf;
        handlers.push_back(thread(clientHandler, newClient));
        clients.push_back(newClient);
    }

    for (int i = 0; i < handlers.size(); i++) {
        handlers[i].join();
    }
    
    return 0;
}