/* File: arrprint.c
    Takes an array and the size of that array and prints the contents of the array. */

#include <stdio.h>

void printer(int arr[], int size);
void d_printer(double arr[], int size);

void printer(int arr[], int size)
{
    printf("[");
    int a;
    for (a = 0; a < size-1; a++)
    {
        printf("%d, ", arr[a]);
    }
    printf("%d", arr[size-1]);
    printf("]\n");
}

void d_printer(double arr[], int size)
{
    printf("[");
    int a = 0;
    for (a; a < size-1; a++)
    {
        printf("%.3lf, ", arr[a]);
    }
    printf("%.3lf", arr[size-1]);
    printf("]\n");
    return;
}
