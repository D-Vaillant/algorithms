/*
 * =====================================================================================
 *
 *       Filename:  mergesort.c
 *
 *    Description:  Implementation of mergesort in C.
 *
 *        Version:  1.0
 *        Created:  03/28/2015 10:35:39 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), david@gmail.com
 *        Credits: LCRS
 *
 * =====================================================================================
 */

#include <stdio.h>
#include "arrprint.c"

void remain(double arr[], int first, int last);
void mergesort(double arr[], int size);
void merge(double arr[], int first, int middle, int last);
void main();

void remain(double arr[], int first, int last)
{
    if(first<last)
    {
        int middle = (first+last)/2;
        remain(arr, first, middle);
        remain(arr, middle, last);
        merge(arr, first, middle, last);
    }
    return;
}

void mergesort(double arr[], int size)
{
    remain(arr, 0, size-1);
    return;
}

void merge(double arr[], int first, int middle, int last)
{
    int a = middle - first + 1;
    int b = last - middle;
    double L[a];
    double R[b];
    int i, j = 0;
    for(i; i<a; i++){ L[i] = arr[first+i]; }
    for(j; j<b; j++){ R[j] = arr[middle+j+1]; }
    int k;
    i, j = 0;
    for(k = first; k <= last; k++)
    {
        if((a != 0)&&((b == 0)||(L[i] <= R[j])))
        {
            arr[k] = L[i];
            i++;
            a--;
        }
        else
        {
            arr[k] = R[j];
            j++;
            b--;
        }
    }
    return;
}

void main()
{
    int z = 7;
    double x[7] = {4, 6, 2, 3, 7, 3, 11};
    mergesort(x, z);
    
    d_printer(x, z);
    return;
}
