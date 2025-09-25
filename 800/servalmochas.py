# #include<bits/stdc++.h>
# using namespace std;

# // Code Written By: Vikash Patel

# bool beautiful(int a[] , int n)
# {
#     int g=INT_MAX;
#     for(int i=0;i<n;i++)
#     {
#         for(int j=i+1;j<n;j++)
#         {
#             g=min(__gcd(a[i], a[j]), g);
#         }
#     }
#     if(g>2)
#     return false;
#     else
#     return true;
# }

# int main()
# {
#     int t;
#     cin>>t;
#     while(t--)
#     {
#         int n;
#         cin>>n;
#         int a[n];
#         for(int i=0;i<n;i++)
#         {
#             cin>>a[i];
#         }
#         if(beautiful(a,n))
#         cout<<"YES"<<endl;
#         else
#         cout<<"NO"<<endl;
#     }
# }

t = int(input())
from math import gcd
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = 10**9
    for i in range(n):
        for j in range(i+1, n):
            g = min(gcd(a[i], a[j]), g)
    if g > 2:
        print("NO")
    else:
        print("YES")