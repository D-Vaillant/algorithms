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

typedef struct Tree *Tree;

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
