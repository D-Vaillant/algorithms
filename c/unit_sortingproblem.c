/*
 * =====================================================================================
 *
 *       Filename:  unit_sortingproblem.c
 *
 *    Description:  Unit test for sorting algorithms. Requires that the sorting function
 *                  has prototype "sort(double arr[], int size)".
 *
 *        Version:  1.0
 *        Created:  03/31/2015 01:49:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), david@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/* Change this include to the source of the algorithm to be tested. */
#include "mergesort.c"

#define sz 10
typedef enum { false, true } bool;

/* Dummy function used for testing the unit test.
void sort(double arr[], int size)
{
    return;
} */

double * generator()
{
    static double ar[sz];
    int a;
    for (a = 0; a < sz; a++)
    {
        ar[a] = (double) rand();
    }
    return ar;
}

void main(int argc, char *argv[])
{
    int runs;
    if ( argc != 2 )
    {
        runs = 100;
        printf("Running 100 trials.\n");
    }
    else
    {
        runs = atoi(argv[1]);
        printf("Running %d trials.\n", runs);
    }
    bool glass = true;
    int a = 0;
    int b;
    int c = 0;
    srand(time(NULL));
    for (a; a < runs; a++)
    {
        double *arr;
        arr = generator();
        sort(arr, sz);
        for (b=0; b < sz-1; b++)
        {
            if (arr[b] > arr[b+1])
            {
                glass = false;

                // Stops printing information after a few errors. 
                if (++c < 20) 
                {
                    printf("%d: Error at indices %d, %d.\n", a, b, b+1);
                }
            }
        }
    }
    if (glass == true)
    {
        printf("No errors.\n");
    }
    else
    {
        printf("Sorting algorithm is flawed... somewhere.\n");
    }
    printf("Program finished running.\n");
    return;
}


