/*
 * =====================================================================================
 *
 *       Filename:  countingsort.c
 *
 *    Description:  Implementation of the counting sort algorithm.
 *
 *        Version:  1.0
 *        Created:  07/23/2015 10:03:48 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), dvaillant@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include "arrprint.c"

#define ARR_SIZE 20
#define RANGE 50

void countingSort(int A[], int size, int *B)
{
    int C[RANGE] = {0};
    int a, b, c;

    for(a = 0; a < size; a++)
    {
        C[A[a]]++;
    }
    for(c = 1; c < RANGE; c++)
    {
        C[c] += C[c-1];
    }
    for(b = size-1; b >= 0; b--)
    {
        B[C[A[b]]] = A[b];
        C[A[b]]--;
    }
}

void main()
{
    srand(time(0));
    int arr[ARR_SIZE] = { 0 };
    
    int n;
    for(n = 0; n < ARR_SIZE; n++) { arr[n] = rand()%RANGE; }

    int sorted_arr[ARR_SIZE] = { 0 };
    printer(arr, ARR_SIZE);
    countingSort(arr, ARR_SIZE, sorted_arr);
    printer(sorted_arr, ARR_SIZE);
}

