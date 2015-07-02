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

void main(int arr[], int arr_len, int target) {
    int n;
    for(n = 0; n < arr_len; n++) {
        if(arr[n] == target) { return n; }
    }
    return -1;
}
