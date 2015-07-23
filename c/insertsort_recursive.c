/*
 * =====================================================================================
 *
 *       Filename:  insertsort_recursive.c
 *
 *    Description:  Recursive implementation of insertion sort.
 *
 *        Version:  1.0
 *        Created:  03/31/2015 01:37:54 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), david@gmail.com
 *        Credits: CLRS
 *
 * =====================================================================================
 */

#include <stdio.h>
#include "arrprint.c"

#define ARR_SIZE 10

void merge(double arr[], int size)
{
    double x = arr[size-1];
    int i = size - 2;
    while (i >= 0 && arr[i] > x)
    {
        arr[i+1] = arr[i];
        i--;
    }
    arr[i+1] = x;

    return;
}

void sort(double arr[], int size)
{
    if (size == 1)
    {     }
    else
    {
        sort(arr, size-1);
        merge(arr, size);
    }
    return;
}

void main(void)
{
    srand(time(0));
    double arr[ARR_SIZE];
    int n;

    for(n = 0; n < ARR_SIZE; n++)
    {
        arr[n] = rand()%50;
    }

    d_printer(arr, ARR_SIZE);
    sort(arr, ARR_SIZE);
    d_printer(arr, ARR_SIZE);
}
