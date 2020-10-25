#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n = 0;
    cin >> n;

    vector<float> input(n,0);
    for(int i = 0; i < input.size(); i++)
        cin >> input[i];

    sort(input.begin(), input.end());
    
    for(int i:input)
        cout<<i<<" ";
    int mid = n/2;
    
    if(n%2==1)
    {
        cout<< round((input[mid/2] + input[mid/2-1])/2) <<endl ;
        cout<< input[mid] <<endl;
        cout<< round((input[mid+mid/2] + input[mid+mid/2+1])/2) <<endl;
    }
    else {
        if(mid%2==0)
            cout<< round((input[mid/2] + input[mid/2-1])/2) <<endl ;
        else 
            cout<< input[mid/2] <<endl ;
        cout<< round((input[mid] + input[mid-1])/2) <<endl;
        
        if(mid%2==0)
             cout<< round((input[mid+mid/2] + input[mid+mid/2-1])/2) <<endl;
        else 
             cout<< input[mid+mid/2]<<endl;
        // cout<< input[mid+mid/2]<<endl;
    }
    return 0;
}
