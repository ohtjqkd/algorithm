#include<iostream>
#include<climits>
#include<cstdlib>
#include<vector>

using namespace std;

int in[20][20];
int n;
int diff = INT_MAX;
vector<int> a_list;
vector<int> b_list;

void go(int index)
{
    if(index>=n)
    {
        if(a_list.size() != n/2)    return;

        int a=0;
        int b=0;

        for(int i=0; i<a_list.size(); i++)
            for(int j=0; j<a_list.size(); j++)
                a+= in[a_list[i]][a_list[i]];

        for(int i=0; i<b_list.size(); i++)
            for(int j=0; j<b_list.size(); j++)
                a+= in[b_list[i]][b_list[i]];

        int current=abs(a-b);
        if(current<diff)
            diff=current;
        return;
    }
    a_list.push_back(index);
    go(index+1);

    a_list.pop_back();
    b_list.push_back(index);
    go(index+1);
    b_list.pop_back();
}

int main()
{
    cin>>n;
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cin>>in[i][j];

    go(0);
    cout<<diff<<'\n';
}