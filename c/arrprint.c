/* File: arrprint.c
    Takes an array and the size of that array and prints the contents of the array. */

#include <stdio.h>

int main(int arr[], int size){
    printf("[");
    for (int a = 0; a < size-1; a++){
        printf("%d, ", arr[a]);
                                  }
    printf("%d", arr[size-1]);
    printf("]\n");
    return 0;
}
