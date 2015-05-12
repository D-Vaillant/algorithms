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

double * merge(double arr[], int size)
{
    double x = arr[size-1];
    int i = size - 2;
    while (i >= 0 && arr[i] > x)
    {
        arr[i+1] = arr[i];
        i--;
    }
    arr[i+1] = x;
    return arr;
}

double * sort(double arr[], int size)
{
    if (size == 1)
    {
        return arr;
    }
    else
    {
        merge(sort(arr, size-1), size);
    }
    return arr;
}
