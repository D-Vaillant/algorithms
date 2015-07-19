/*
 * =====================================================================================
 *
 *       Filename:  bubblesort.c
 *
 *    Description:  Implementation of the bubblesort algorithm in C.
 *
 *        Version:  1.0
 *        Created:  03/18/2015 05:34:39 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant
 *         Credits: CLRS
 *
 * =====================================================================================
 */

#include <stdio.h>
#include "arrprint.c"

void sort(double arr[], long size)
{
    int m;
    int s; 
    for (m=0; m<size; m++)
    {    
        s = size-1;
        for (s; s > m; s--)
        {
            if (arr[s]  < arr[s-1])
            {
                double tmp = arr[s];
                arr[s] = arr[s-1];
                arr[s-1] = tmp;
            }
        }
    }
    return;
}


void main()
{
    int z = 7;
    double x[7] = {4, 2, 5, 3, 6, 1, 5.2};
    sort(x, z);

    d_printer(x, z);
    return;
}

