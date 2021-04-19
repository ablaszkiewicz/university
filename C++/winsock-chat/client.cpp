#include <iostream>
#include <winsock.h>
#include <thread>
#include <cstring>

using namespace std;

const int PORT = 1234;
const char ADDRESS[] = "127.0.0.1";
string NICK;

void sendingFunction(SOCKET socket) {
    int dlug;
    char buf[80];
    for (;;)
    {
        fgets(buf, 80, stdin);
        dlug = strlen(buf);
        buf[dlug - 1] = '\0';
        send(socket, buf, dlug, 0);
        if (strcmp(buf, "KONIEC") == 0) break;
    }
}

void receivingFunction(SOCKET socket) {
    char buf[80];
    for (;;)
    {
        recv(socket, buf, 80, 0);
        cout << buf << endl;
    }
}

int main()
{
    SOCKET s;
    struct sockaddr_in sa;
    WSADATA wsas;
    WORD wersja;
    wersja = MAKEWORD(2, 0);
    WSAStartup(wersja, &wsas);
    s = socket(AF_INET, SOCK_STREAM, 0);
    memset((void*)(&sa), 0, sizeof(sa));
    sa.sin_family = AF_INET;
    sa.sin_port = htons(PORT);
    sa.sin_addr.s_addr = inet_addr(ADDRESS);

    int result;
    result = connect(s, (struct sockaddr FAR*) & sa, sizeof(sa));
    if (result == SOCKET_ERROR)
    {
        printf("\nBlad polaczenia !");
        return 0;
    }

    //send name
    cout << "Type your nick: ";
    int dlug;
    char buf[80];
    fgets(buf, 80, stdin);
    dlug = strlen(buf);
    buf[dlug - 1] = '\0';
    send(s, buf, dlug, 0);

    thread sender(sendingFunction, s);
    thread receiver(receivingFunction, s);

    sender.join();
    receiver.detach();
    

    closesocket(s);
    WSACleanup();

    return 0;
}