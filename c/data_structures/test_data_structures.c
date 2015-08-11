/*
 * =====================================================================================
 *
 *       Filename:  data_structures.c
 *
 *    Description:  Implementation of various data structs.
 *
 *        Version:  1.0
 *        Created:  07/03/2015 06:54:17 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Vaillant (mn), dvaillant@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdlib.h>
#include <stdio.h>

#include "linked_list.c"
#include "binary_tree.c"

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  binary_tree
 *  Description:  Unit test for binary tree implementation using struct Tree.
 * =====================================================================================
 */
void binary_tree(void) {
    Tree bt = malloc(sizeof(Tree));
    if(bt == NULL) {
        printf("Memory allocation failed.\n");
        exit(-1); }

    bt->value = 1;
    tree_add(bt, 'l', 2);
}

void linked_list(void) {
    Cell ll = malloc(sizeof(Cell));
    ll->value = 99;

    // Tests ll_append.
    int n = 0; 
    for(n; n < 15; n++) {
        ll_append(ll, n);
    }

    Cell ll2 = ll;
    int loop_stopper = 0; // Tired of pesky infinite loops? I got u fam
    do {
        printf("%d ", ll2->value);
        loop_stopper++;
    } while(ll_step(ll2) && loop_stopper < 50);
    printf("\n");

    // Tests ll_index.
    printf("At index %d: %d.\n", 5, ll_index(ll,5));

    free(ll);
}

/* Runs unit tests of various data structs. */
int main(void) {
    linked_list();
    return 0;
}    
