/*
 * =====================================================================================
 *
 *       Filename:  queue.cpp
 *
 *    Description:  It's a queue!
 *
 *        Version:  1.0
 *        Created:  03/07/2017 04:37:25 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  David Vaillant 
 *
 * =====================================================================================
 */
#include <iostream>

const int max = 5;


class Queue {
    private:
        int head;
        int tail;
        int arr[max];
    public:
        Queue() {
            head = 0;
            tail = 0;
        }

        void enqueue(int i) {
            if ((tail+1)%max == head) {
                throw "overflow";
            } else {
                arr[tail] = i;
                if (tail < max-1) {
                    tail++;
                } else {
                    tail = 0;
                }
            }
        }

        int dequeue() {
            if (head == tail) {
                throw "underflow";
            } else {
                int out = arr[head];
                if (head < max-1) {
                    head++;
                } else {
                    head = 0;
                }
                return out;
            }
        }
};

int main() {
    Queue q = Queue();

    try {
        q.dequeue();
    } catch (const char* msg) {
        std::cout << msg << std::endl;
    }

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    std::cout << q.dequeue() << std::endl;
    std::cout << q.dequeue() << std::endl;

    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(99);
    std::cout << q.dequeue() << std::endl;
    std::cout << q.dequeue() << std::endl;
    std::cout << q.dequeue() << std::endl;
    std::cout << q.dequeue() << std::endl;

    try {
        q.dequeue();
    } catch (const char* msg) {
        std::cout << msg << std::endl;
    }

    return 0;
}
