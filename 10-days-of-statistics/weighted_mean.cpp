#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    float mean = 0,tot=0,w_tot= 0;

    cin>>n;
    vector<float> input(n,0);
    vector<float> weight(n,0);

    for(int i =0; i<n; i++)
        cin>>input[i];

    for(int i=0; i<n; i++)
    {
        cin>>weight[i];
    //     cout<<"i "<<i<<" : "<<tot<<endl;
        tot += input[i]*weight[i];
        w_tot += weight[i];
    }
    
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(1);

    // cout<<tot<<"  "<<w_tot<<endl;
    mean = tot/w_tot;
    cout<<mean<<endl;

    return 0;
}
