#include <iostream>

using namespace std;

int main()
{
    int arr[1000];
    int dp[1000];
    int max[1000];
    int max1 = 0;
    int max2 = 0;
    int result = 0;
    int N;
    
    cin>> N;
    
    for(int i = 0; i<N; i++)    cin>>arr[i]; //input
    
    for(int i = 0; i<N; i++){
        for(int j = 0; j<i; j++){
            dp[j] = 1;
            for(int k = 0; k<j; k++){
                if(arr[k]<arr[j] && dp[k] >= dp[j]){
                    dp[j] = dp[k]+1;
                }
            }
        }//arr1
        
        for(int j = 0; j<i; j++){
            if(max1 < dp[j])
                max1 = dp[j];
        }//arr1 max1
        
       for(int j = i; j<N; j++){
            dp[j] = 1;
            for(int k = i; k<j; k++){
                if(arr[k]>arr[j] && dp[k] >= dp[j]){
                    dp[j] = dp[k]+1;
                }
            }
        }//arr2
        
        for(int j = i; j<N; j++){
            if(max2 < dp[j])
                max2 = dp[j];
        }//arr2 max2
        
        max[i] = max1 + max2;
        max1 = 0;
        max2 = 0;
        
    }
    
    for(int i = 0; i<N; i++){
        if(result < max[i])
            result = max[i];
    }
    
    cout<<result;
    

    return 0;
}