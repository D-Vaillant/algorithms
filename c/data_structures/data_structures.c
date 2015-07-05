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

typedef struct Cell {
    int value;
    struct Cell * n;
} *cell;


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  ll_add
 *  Description:  Adds a value to a linked list. 
 * =====================================================================================
 */
void ll_add(cell linked, int val) {
    cell target = linked;
    while(target->n != NULL) {
        target = (cell) target->n; }

    target->n = (cell) malloc(sizeof(struct Cell));
    (target->n)->value = val;
}

void linked_list(void) {
    cell ll = malloc(sizeof(struct Cell));
    ll->value = 1;
    ll_add(ll, 2);
    ll_add(ll, 3);
    ll_add(ll, 4);
    ll_add(ll, 5);
    ll_add(ll, 6);
    ll_add(ll, 7);

    printf("Linked List Contents: %d %d %d %d %d %d %d\n", ll->value, ll->n->value, 
                                  ll->n->n->value, ll->n->n->n->value,
                                  ll->n->n->n->n->value, ll->n->n->n->n->n->value,
                                  ll->n->n->n->n->n->n->value); 
}

/* Runs unit tests of various data structs. */
void main(void) {
    linked_list();
}    
