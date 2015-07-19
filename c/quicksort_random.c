/*
 * =====================================================================================
 *
 *       Filename:  quicksort_random.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  07/17/2015 01:29:43 PM
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

#define ARR_SIZE 10


int partition(double A[], int initial, int final) {
    double tmp;
    int i = initial; 
    
    int n;
    for(n = initial; n < final; n++) {
        if(A[n] <= A[final]) {
            tmp = A[n];
            A[n] = A[i];
            A[i] = tmp;
            ++i;
        }
    }

    tmp = A[i];
    A[i] = A[final];
    A[final] = tmp;

    //printf("Initial is %d, partition is %d, final is %d.\n", initial, i, final);
    //d_printer(&(A[initial]), i-initial);
    //d_printer(&(A[i]), final - i + 1);
    //printf("\n");
    return i;
}


int random_partition(double A[], int initial, int final) {
    //int i = (rand()%(final-initial)) + initial;
    int i = final - (rand()%(final-initial));
    double tmp = A[final];
    A[final] = A[i];
    A[i] = tmp;
     
    
    return partition(A, initial, final);
}


void remain(double A[], int initial, int final) {
    if(initial < final) {
        int q = random_partition(A, initial, final);
        remain(A, initial, q-1);
        remain(A, q, final);
    }
    
    return;
}

void sort(double A[], int size) {
    remain(A, 0, size-1); }


void main(void) {
    srand(time(0));
    double arr[ARR_SIZE] = { 0 };
    
    int i;
    for(i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % 50;
    }

    d_printer(arr, ARR_SIZE);
    sort(arr, ARR_SIZE);
    d_printer(arr, ARR_SIZE);

    return;
}
