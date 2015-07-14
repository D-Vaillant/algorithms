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

typedef struct Node {
    int value;
    struct Node * left;
    struct Node * right;
} *node;


void bst_print(node base, char * buffer, int buffer_size) {
    
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  node_add
 *  Description:  Takes a node, a direction, and integer value and makes it so the node
 *                points to a new node containing that integer value.
 * =====================================================================================
 */
void node_add(node base, char dir, int val) {
    node nouveau = malloc(sizeof(struct Node));
    if(nouveau == NULL) {
        printf("Memory allocation failed.\n");
        exit(-1); }

    nouveau->value = val;

    if(dir == 'r') {
        base->right = nouveau;
    } else if(dir == 'l') {
        base->left = nouveau;
    } else {
        printf("Invalid direction entered: %c\n", dir);
        free(nouveau);
        return; 
    }
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  binary_tree_node
 *  Description:  Unit test for binary tree implementation using struct Node.
 * =====================================================================================
 */
void binary_tree_node(void) {
    node bt = malloc(sizeof(struct Cell));
    if(bt == NULL) {
        printf("Memory allocation failed.\n");
        exit(-1); }

    bt->value = 1;
    node_add(bt, 'l', 2);
}

int ll_step(cell linked) {
    if(linked->n) {
        *linked = *(linked->n); 
        return 1;
    } else { return 0; }
}

cell ll_index(cell linked, int index) {
    int i = 0;
    while(i < 0) {
        if(linked->n == NULL) {
            linked = (cell) linked->n;
            ++i;    
        } else {
            printf("WARNING: Overflow error.\n");
            break;
        }
    }
    return linked;
}

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
    if(target->) { (target->n)->value = val; }
    else {
        printf("WARNING: Overflow error.\n");
        exit(-1);
    }
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

    int loop_stopper = 0; // Tired of pesky infinite loops? I got u fam
    do {
        printf("%d\n", ll->value);
        loop_stopper++;
    } while(ll_step(ll) && loop_stopper < 50);

    /*
    printf("Linked List Contents: %d %d %d %d %d %d %d\n", ll->value, ll->n->value, 
                                  ll->n->n->value, ll->n->n->n->value,
                                  ll->n->n->n->n->value, ll->n->n->n->n->n->value,
                                  ll->n->n->n->n->n->n->value); 
    */
}

/* Runs unit tests of various data structs. */
int main(void) {
    linked_list();
    return 0;
}    
