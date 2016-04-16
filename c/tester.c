/*
 * =====================================================================================
 *
 *       Filename:  tester.c
 *
 *    Description:  Yup.
 *
 *        Version:  1.0
 *        Created:  07/19/2015 12:37:49 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), dvaillant@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <check.h>
#include "insertsort.c"

int if_ordered(int * input, int input_len) {
    int n;
    for (n = 0; n < input_len-1; n++) {
        if (input[n] > input[n+1]) return 0; 
    }
    return 1;
}

START_TEST (test_insertsort)
{
    int z = 7;
    int x[7] = {8, 7, 6, 5, 4,3,2};
    int *y;
    y = insert_sort(x, z);
    ck_assert_int_eq(if_ordered(y, z), 1); 
}
END_TEST

int main(void) {
    return 0;
}    
