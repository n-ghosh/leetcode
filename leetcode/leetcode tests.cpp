/* For testing */

#include <iostream>
// other includes as needed

using namespace std;

class Solution {

};


int main() {
    Solution sol;
    vector<vector<int> > tests = {
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
        {1, 2, 3, 4, 1},
        {1, 2, 3, 4, 1, 5},
        {1,3,3,4,3,2,4,2},
        // {},
        {0},
        {-1, 0, 1}, 
        {1000}
    };
    for (auto test : tests) {
        // cout << sol.func(test) << endl;
    }

    return 0;
}
