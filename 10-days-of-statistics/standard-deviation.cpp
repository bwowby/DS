#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n=0;
    float tot=0;
    float avg=0;
    cin>>n;

    vector<int> input(n,0);
    for(int i=0; i<n; i++)
    {
        cin>>input[i];
        tot+=input[i];
    }
    avg = tot/n;

    tot = 0;
    for(int i=0; i<n; i++)
    {   
        tot += pow(input[i]-avg,2);
    }
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(1);
    cout<< sqrt(tot/n);
    return 0;
}
