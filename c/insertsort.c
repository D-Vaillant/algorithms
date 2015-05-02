/* File: insertsort.c
    Implementation of the insertion sort algorithm. */

#include <stdio.h>
//#include "arrprint.c"

double * sort(double arr[], int size){
    int m=1;
    int k;
    double key;

    for (m; m<size; m++)
    {
        k = m-1;
        key = arr[m];
        while (k > -1 && arr[k] > key)
        {
            arr[k+1] = arr[k];
            k--;                      
        }
        arr[k+1] = key;
    }
   return arr;
}

/*
void printer(int arr[], int size){
    printf("[");
    int a;
    for (a = 0; a < size-1; a++){
        printf("%d, ", arr[a]);
                                    }
    printf("%d", arr[size-1]);
    printf("]\n");
}


int test(){
    int z = 7;
    int x[7] = {8, 7, 6, 5, 4,3,2};
    int *y;
    y = insertsort(x, z);
    
    printer(x, z);
    return 0;
}
*/

