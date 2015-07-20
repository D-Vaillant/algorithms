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
#include <stdlib.h>
#include "arrprint.c"

#define ARR_SIZE 10

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
        remain(arr, middle+1, last);
        //printf("Merging %d, %d, and %d.\n", first, middle, last);
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
    double *L = malloc(a*sizeof(double));
    double *R = malloc(b*sizeof(double));

    if(L == NULL || R == NULL) {
        printf("NULL RETURNED!\n");
        return;
    }

    int i, j;
    i = j = 0;
    for(i; i<a; i++){ L[i] = arr[first+i]; }
    for(j; j<b; j++){ R[j] = arr[middle+j+1]; }

    int k;
    i = 0;
    j = 0;

    for(k = first; k <= last; k++)
    {
        //printf("Beginning of loop.\n");
        //printf("Left: "); d_printer(&L[i], a);
        //printf("Right: "); d_printer(&R[j], b);

        //printf("a: %d, b: %d\n", a, b); 

        if((a > 0) && (b == 0 || L[i] <= R[j]))
        {
            //printf("L[i] assignment, value at %lf.\n", L[i]);
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

    //d_printer(arr, ARR_SIZE);
    }

    free(L);
    free(R);

    return;
}

void main()
{
    srand(time(0));

    double x[ARR_SIZE] = { 0 };
    int n;
    for(n = 0; n < ARR_SIZE; n++)
    {
        x[n] = rand() % 50;
    }

    d_printer(x, ARR_SIZE);
    mergesort(x, ARR_SIZE);
    d_printer(x, ARR_SIZE);
    return;
}
