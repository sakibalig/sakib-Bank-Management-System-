//# sakib-Bank-Management-System-
#include <iostream>
#include <conio.h>

using namespace std;

class Bank {
    char name[100], add[100], Y;
    int balance;

  public:
    void open_account();
    void deposit_money();
    void withdraw_money();
    void display_account();
};

void Bank::open_account() {
    cout << "Enter your full name: ";
    cin.ignore();
    cin.getline(name, 100);
    cout << "Enter your address: ";
    cin.getline(add, 100);
    cout << "What type of account do you want to open? Saving (s) or current (c): ";
    cin >> Y;
    cout << "Enter the initial deposit amount: ";
    cin >> balance;
    cout << "Your account has been created." << endl;
}

void Bank::deposit_money() {
    int amount;
    cout << "Enter the amount you want to deposit: ";
    cin >> amount;
    balance += amount;
    cout << "Total amount after deposit: " << balance << endl;
}

void Bank::withdraw_money() {
    float amount;
    cout << "Enter the amount you want to withdraw: ";
    cin >> amount;
    if (amount > balance) {
        cout << "Insufficient balance." << endl;
    } else {
        balance -= amount;
        cout << "Amount withdrawn. Remaining balance: " << balance << endl;
    }
}

void Bank::display_account() {
    cout << "Name: " << name << endl;
    cout << "Address: " << add << endl;
    cout << "Account Type: " << Y << endl;
    cout << "Balance: " << balance << endl;
}

int main() {
    int ch, x;
    Bank obj;

    do {
        cout << "1) Open account" << endl;
        cout << "2) Deposit money" << endl;
        cout << "3) Withdraw money" << endl;
        cout << "4) Display account" << endl;
        cout << "5) Exit" << endl;
        cout << "Select an option from above: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "Open account" << endl;
                obj.open_account();
                break;
            case 2:
                cout << "Deposit money" << endl;
                obj.deposit_money();
                break;
            case 3:
                cout << "Withdraw money" << endl;
                obj.withdraw_money();
                break;
            case 4:
                cout << "Display account" << endl;
                obj.display_account();
                break;
            case 5:
                exit(0);
            default:
                cout << "Invalid option. Please try again." << endl;
                break;
        }

        cout << "\nDo you want to select another option? (Y/N): ";
        cin >> x;
    } while (x == 'Y' || x == 'y');

    getch();
    return 0;
}
