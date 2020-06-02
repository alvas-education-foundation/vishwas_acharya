// Given an array of positive integers. Write a C Program to find the leaders in the array.
#include <stdio.h>
int main()
{
    int num,i,j,count=0;
    scanf("%d",&num);
    int arr[num];
    for(i=0;i<num;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    for(i=0;i<num;i++)
    {
       count=i;
       for(j=i+1;j<num;j++)
        {
            if(arr[i]>=arr[j])
            {
                count++;
            }
            if(count==num-1)
            {
                printf("%d ",arr[i]);
            }
        }
    }
    printf("%d",arr[num-1]);

    return 0;
}