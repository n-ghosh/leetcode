#include <iostream>
#include <stack>
using namespace std;

class MyQueue {
public:
    MyQueue() {
        
    }
    stack<int> s1;
    stack<int> s2;
    
    void push(int x) {
        if (s2.empty()) {
            s2.push(x);
        }
        else {
            s1.push(x);
        }
    }
    
    int pop() {
        int x = s2.top();
        s2.pop(); // now s2 is empty
        s1.swap(s2); // now s1 is empty, s2 is reverse-queue
        int temp;
        while (s2.size() > 1) { // reverse it
            temp = s2.top();
            s2.pop();
            s1.push(temp);
        }
        return x;
    }
    
    int peek() {
        return s2.top();
    }
    
    bool empty() {
        return s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */