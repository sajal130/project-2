#include <iostream>
using namespace std;

int main() {
    int num1, num2, choice;
    float result;

    // Display menu to the user
    cout << "Select an operation to perform:\n";
    cout << "1. Addition\n";
    cout << "2. Subtraction\n";
    cout << "3. Multiplication\n";
    cout << "4. Division\n";
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    // Get the numbers from the user
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    // Perform the operation based on user choice
    switch(choice) {
        case 1:
            result = num1 + num2;
            cout << "Result: " << num1 << " + " << num2 << " = " << result << endl;
            break;
        case 2:
            result = num1 - num2;
            cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
            break;
        case 3:
            result = num1 * num2;
            cout << "Result: " << num1 << " * " << num2 << " = " << result << endl;
            break;
        case 4:
            if (num2 != 0) {
                result = (float)num1 % num2;
                cout << "Result: " << num1 << " % " << num2 << " = " << result << endl;
            } else {
                cout << "Error: Division by zero is not allowed." << endl;
            }
            break;
        default:
            cout << "Invalid choice. Please select a number between 1 and 4." << endl;
            break;
    }

    return 0;
}

