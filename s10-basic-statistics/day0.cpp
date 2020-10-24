#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n =0;
    cin>>n;

    vector<int> input(n,0);
    float tot = 0;

    for(int i=0; i<n; i++)
    {
        cin>>input[i];
        tot += input[i];
    }   
    
    sort(input.begin(),input.end());

    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(1);
    
    //mean
    cout<<tot/n<<endl;

    //median

    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(1);
    cout<< (float)(input[n/2] + input[n/2-1]) /2<<endl;
    
    //mode
    int mode = 0;
    int mx = -1;
    int idx = 0;
    int prev = -1;

    for(int i=0; i<input.size(); i++)
    {
        if(prev == input[i]) 
        {
            mode+=1;
        }
        else 
            mode = 1;
        if(mode > mx)
        {
            idx = i;
            mx = mode;
        }
        prev = input[i];
    }

    if(mx==1) cout<<input[0];
    else cout<<input[idx];

    return 0;
}
