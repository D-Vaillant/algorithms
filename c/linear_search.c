/*
 * =====================================================================================
 *
 *       Filename:  linear_search.c
 *
 *    Description: Implementation of the linear search algorithm. 
 *
 *        Version:  1.0
 *        Created:  07/02/2015 11:03:43 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), dvaillant@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>

int search(int arr[], int arr_len, int target) {
    int n;
    for(n = 0; n < arr_len; n++) {
        if(arr[n] == target) { return n; }
    }
    return -1;
}

void main(void)
{
    int arr[] = {1, 2, 5, 6, 7, 8, 3, 4, 2, 6, 7, 3, 1, 0};
    int found = search(arr, 14, 0);

    if(found > -1)
    {
        printf("Index of 0 was %d.\n", found);
    } else {
        printf("0 not found.\n");
    }
}
