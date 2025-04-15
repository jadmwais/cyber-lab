#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

void scanPorts(const char* ip, int startPort, int endPort) {
    struct sockaddr_in address;
    int sock;

    cout << "Scanning " << ip << " from port " << startPort << " to " << endPort << "...\n" << endl;

    for (int port = startPort; port <= endPort; ++port) {
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) {
            cerr << "Socket creation failed\n";
            continue;
        }

        address.sin_family = AF_INET;
        address.sin_port = htons(port);
        inet_pton(AF_INET, ip, &address.sin_addr);

        int result = connect(sock, (struct sockaddr*)&address, sizeof(address));
        if (result == 0) {
            cout << "Port " << port << " is OPEN" << endl;
        }
        close(sock);
    }
}

int main() {
    string ip;
    int startPort, endPort;

    cout << "Enter target IP (e.g., 127.0.0.1): ";
    cin >> ip;
    cout << "Enter start port: ";
    cin >> startPort;
    cout << "Enter end port: ";
    cin >> endPort;

    scanPorts(ip.c_str(), startPort, endPort);

    return 0;
}
