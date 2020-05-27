#include <stdio.h> 
void swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
int bubbleSort(int arr[], int n) 
{ 
     int i, j,count=0; 
   int swapped; 
   for (i = 0; i < n-1; i++) 
   { 
     swapped = 0; 
     for (j = 0; j < n-i-1; j++) 
     { 
        if (arr[j] > arr[j+1]) 
        { 
           swap(&arr[j], &arr[j+1]); 
           swapped = 1; 
           count++;
        } 
     } 
     if (swapped == 0) 
        break; 
   }
   return count;
} 
void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
} 
int main() 
{ 
    int arr[50],num;
    printf("enter the number of elements");
    scanf("%d",&num);
    printf("enter the elements");
    for(int i=0;i<num;i++){
        scanf("%d",&arr[i]);
    }
    int c=bubbleSort(arr, num); 
    printf("Sorted array: \n"); 
    printArray(arr, num); 
    printf("Number of passes:%d\n",c);
    return 0; 
}
