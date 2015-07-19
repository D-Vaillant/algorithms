/*
 * =====================================================================================
 *
 *       Filename:  selection_sort.c
 *
 *    Description: Implementation of the selection sort algorithm. 
 *
 *        Version:  1.0
 *        Created:  07/13/2015 09:20:25 PM
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

void sort(double arr[], long size)
{
    int m;
    int n;
    double key;

    for(n = 0; n < size; n++) {
        key = arr[n];
        for(m = n+1; m < size; m++) {
            if(arr[m] < key) {
                double tmp = key;
                key = arr[m];
                arr[m] = tmp;
            }
        }

        arr[n] = key; }
}

void main()
{
    double x[ARR_SIZE] = {0};

    int n;
    for(n = 0; n < ARR_SIZE; n++) { x[n] = rand()%50; }
    d_printer(x, ARR_SIZE);

    sort(x, ARR_SIZE);
    d_printer(x, ARR_SIZE);
}
