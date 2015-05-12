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
#include "insertsort.c"

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
    int output[2] = {(int) floor(min), (int) ceil(max)};
    return output;

double * bucket_sort(double arr[], int size)
{
   return general_sort(arr, size, find_interval(arr, size)); 
}

double * general_sort(double arr[], int size, int interval[2])
{
    double a = 1.0;
    return *a;
}

double * main(void)
{
    arr = {1, 2, 3};
    return bucket_sort(arr, 3);
}
