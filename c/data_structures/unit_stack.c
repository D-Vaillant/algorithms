/*
 * =====================================================================================
 *
 *       Filename:  unit_stack.c
 *
 *    Description:  Tests for stack.c.
 *
 *        Version:  1.0
 *        Created:  08/10/2015 10:27:13 PM
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
#include <check.h>

#include "stack.c"

void main(void) {
    Stack S = create_stack(5);

    /* Testing pushing. */
    push(S, 5);
    printf("Push success: %d\n", (S->arr)[0] == 5);
    
    /* Testing popping. */
    printf("Pop success: %d\n", pop(S) == 5);
    
    printf("Has max capacity %d.\n", S->max_capacity);
    return;
}
