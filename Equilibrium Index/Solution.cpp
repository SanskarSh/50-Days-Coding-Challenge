#include <iostream>
#include <vector>

using namespace std;

int findEquilibriumIndex(const vector<int>& Arr) {
    int n = Arr.size();
    if (n == 0) {
        return -1;
    }

    vector<int> prefixSum(n, 0);
    vector<int> suffixSum(n, 0);

    prefixSum[0] = Arr[0];
    suffixSum[n - 1] = Arr[n - 1];

    for (int i = 1; i < n; ++i) {
        prefixSum[i] = prefixSum[i - 1] + Arr[i];
    }

    for (int i = n - 2; i >= 0; --i) {
        suffixSum[i] = suffixSum[i + 1] + Arr[i];
    }

    for (int i = 0; i < n; ++i) {
        if (prefixSum[i] == suffixSum[i]) {
            return i;
        }
    }

    return -1;
}

int main() {
    
    vector<int> Arr = {-7, 1, 5, 2, -4, 3, 0};

    int equilibriumIndex = findEquilibriumIndex(Arr);

    if (equilibriumIndex != -1) {
        cout << "Equilibrium index: " << equilibriumIndex << endl;
    } else {
        cout << "No equilibrium index found." << endl;
    }

    return 0;
}