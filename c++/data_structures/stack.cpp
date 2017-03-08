/*
 * =====================================================================================
 *
 *       Filename:  stack.cpp
 *
 *    Description:  It's a stack!
 *
 *        Version:  1.0
 *        Created:  03/07/2017 04:05:14 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  David Vaillant 
 *
 * =====================================================================================
 */
#include <iostream>

const int max = 5;  // This is arbitrary.

class Stack {
    private:
        int top;
        int arr[max];
    public:
        Stack() {
            top = 0;
        }

        void push(int i) {
            if (top < max) {
                arr[top++] = i;
            } else {
                throw "overflow";
            }
        }

        int pop() {
            if (top == 0) {
                throw "underflow";
            } else {
                int out = arr[--top];
                arr[top+1] = 0;
                return out;
            }
        }

        bool is_empty() {
            return (top == 0);
        }
};

int main() {
    Stack a;
    a.push(1);
    a.push(2);
    a.push(4);
    a.push(10);
    a.push(11);

    try {
        a.push(51);  // Should error.
    } catch (const char* msg) {
        std::cout << msg << std::endl;
    }

    while(!a.is_empty()) {
        std::cout << a.pop() << std::endl;
    }

    try {
        a.pop();
    } catch (const char* msg) {
        std::cout << msg << std::endl;
    }

    return 0;
}




