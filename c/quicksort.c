/*
 * =====================================================================================
 *
 *       Filename:  quicksort.c
 *
 *    Description:  Implementation of... you know. Quicksort algorithm.
 *                  Includes a randomized quicksort implementation as well.
 *
 *        Version:  1.0
 *        Created:  07/14/2015 09:33:39 PM
 *       Revision:  none
 *       Compiler:  gcc
 *ahold
 *         Author:  David Vaillant (mn), dvaillant@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include "arrprint.c"

#define ARR_SIZE 10

int partition(double A[], int initial, int final) {
    double tmp;
    int i = initial-1;
    
    int n;
    for(n = initial; n < final; n++) {
        if(A[n] <= A[final]) {
            ++i;
            tmp = A[n];
            A[n] = A[i];
            A[i] = tmp;
        }
    }
    ++i; 

    tmp = A[i];
    A[i] = A[final];
    A[final] = tmp;
    
    return i;
}

void remain(double A[], int initial, int final) {
    if(initial < final) {
        int q = partition(A, initial, final);
        remain(A, initial, q-1);
        remain(A, q, final);
    }
    
    return;
}

void sort(double A[], int size) {
    remain(A, 0, size-1); }

void main(void) {
    double arr[ARR_SIZE] = { 0 };
    
    int i;
    for(i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % 50;
    }

    sort(arr, ARR_SIZE);
    d_printer(arr, ARR_SIZE);
}
