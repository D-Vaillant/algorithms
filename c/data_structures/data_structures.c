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

typedef struct Cell *Cell;
typedef struct Tree *Tree;

struct Cell {
    int value;
    Cell n;
};

struct Tree {
    int value;
    Tree left;
    Tree right;
};


/// Binary Search Tree Functions
void bst_print(Tree base, char * buffer, int buffer_size) {
    
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  node_add
 *  Description:  Takes a tree, a direction, and integer value and makes it so the tree 
 *                points to a new tree containing that integer value.
 * =====================================================================================
 */
void tree_add(Tree base, char dir, int val) {
    Tree nouveau = malloc(sizeof(Tree));
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

/*-----------------------------------------------------------------------------
 *  Linked List Functions
 *-----------------------------------------------------------------------------*/


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  ll_step
 *  Description:  
 * =====================================================================================
 */
int ll_step(Cell linked) {
    if(linked->n) {
        linked = linked->n;
        return 1;
    } else { return 0; }
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  ll_index
 *  Description:  Accesses the value stored in the index'd cell.
 * =====================================================================================
 */
int ll_index(Cell linked, int index) {
    Cell copy_linked = linked;
    int i = 0;
    while(i > index) {
        if(ll_step(copy_linked)) {
            ++i;    
        } else {
            printf("WARNING: Overflow error.\n");
            break;
        }
    }
    return linked->value;
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  ll_append
 *  Description:  Append a value to a linked list. 
 * =====================================================================================
 */
void ll_append(Cell linked, int val) {
    Cell target = linked;
    while(target->n != NULL) {
        target = (Cell) target->n; }

    target->n = (Cell) malloc(sizeof(Cell));
    if(target->n) { (target->n)->value = val; }
    else {
        printf("WARNING: Overflow error.\n");
        exit(-1);
    }
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
