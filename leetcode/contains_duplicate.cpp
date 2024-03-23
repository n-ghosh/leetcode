#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // make a hash table
        int lenth = nums.size();
        int table[lenth][2]; // [isFull, num]
        for (int i = 0; i < lenth; i++) {
            table[i][0] = (int) false;
            table[i][1] = 0;
        }

        // loop through input
        for (int e : nums) {
            // check if E in the table
            int idx;
            int k = 0;
            do {
                idx = (e+k) % nums.size(); // linear probe 
                // if e already here, return
                if (table[idx][0] == true && table[idx][1] == e) {
                    return true;
                }
                k ++;
            } while (table[idx][0] == true); // while idx full

            // if not, insert E
            table[idx][0] = (int) true;
            table[idx][1] = e;
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<vector<int> > tests = {
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, // false
        {1, 2, 3, 4, 1}, // true
        {1, 2, 3, 4, 1, 5}, // true
        {1,3,3,4,3,2,4,2}, // true
        {0}, // false
        {-1, 0, 1}, // false
        {-1, 0, -1}, // true
        {0, 1, 0}, // true
        {1000}, // false
        {3, 1}  // false
    };
    for (auto test : tests) {
        cout << sol.containsDuplicate(test) << endl;
    }
    return 0;
}
