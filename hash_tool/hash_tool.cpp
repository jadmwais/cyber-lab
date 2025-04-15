#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

void hashString(const string& input, const string& algorithm) {
    string command;

    if (algorithm == "md5") {
        command = "echo -n \"" + input + "\" | openssl md5";
    } else if (algorithm == "sha256") {
        command = "echo -n \"" + input + "\" | openssl sha256";
    } else {
        cout << "Unsupported algorithm." << endl;
        return;
    }

    system(command.c_str());
}

int main() {
    string text;
    int choice;

    cout << "Hash Generator (C++)\n" << endl;
    cout << "Enter text to hash: ";
    getline(cin, text);

    cout << "\nChoose algorithm:\n1. MD5\n2. SHA-256\nChoice: ";
    cin >> choice;

    if (choice == 1) {
        cout << "\nMD5 Hash:\n";
        hashString(text, "md5");
    } else if (choice == 2) {
        cout << "\nSHA-256 Hash:\n";
        hashString(text, "sha256");
    } else {
        cout << "Invalid option." << endl;
    }

    return 0;
}
