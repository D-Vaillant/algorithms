/*
 * =====================================================================================
 *
 *       Filename:  bucketsort.c
 *
 *    Description:  Implementation of bucketsort algorithm in c. Relies on insertsort.
 *
 *        Version:  1.0
 *        Created:  04/01/2015 06:43:08 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), david@gmail.com
 *        Credits : CLRS
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <math.h>

void insertsort(double arr[], size) {
    int m = 1;
    int k;
    double key;

    for(m; m<size; m++)
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
    
    return;
}

int * find_interval(double arr[], int size)
{
    int i = 0;
    double min = (10^15);
    double max = -(10^15);
    for(i; i++; i<size)
    {
        if(arr[i] < min)
        {
            min = arr[i];
        }
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    int output[2] = {(int) floor(min), (int) ceil(max)};
    return output;
}

void bucket_sort(double arr[], int size)
{
   general_sort(arr, size, find_interval(arr, size)); 
   return;
}

int surject(double value, int interval[2]){
    return (int) floor((value-interval[0])/(interval[1]-interval[0]))
}

double * general_sort(double arr[], int size, int interval[2])
{
    int n;
    double ** counter = malloc(size*sizeof(*double));
    for(n = 0; n < size; n++) { counter[n] = 0; }

    for(n = 0; n < size; n++) {
        ++counter[surject(arr[n])];
    }
}

double * main(void)
{
    arr = {4, 2, 6, 2, 3, 1, 6, 9, 5, 3};
    return bucket_sort(arr, 10);
}
