/*
 * =====================================================================================
 *
 *       Filename:  stack.c
 *
 *    Description:  Implementation of a stack.
 *
 *        Version:  1.0
 *        Created:  08/10/2015 10:17:28 PM
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

typedef struct Stack *Stack;

struct Stack {
    int max_capacity; // Max size of stack.

    int *arr; // Array which contains data.
    int size; // Amount of elements in the stack.
};


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  create_stack
 *  Description:  Takes a size and returns a pointer to a Stack of specified size.
 * =====================================================================================
 */
Stack create_stack(int sz) {
    Stack nouveau = malloc(sizeof(Stack));
    int *new_arr = malloc(sz*sizeof(int));

    if(nouveau == NULL) {
        printf("Memory allocation failed.\n");
        exit(-1); }

    nouveau->arr = new_arr;
    nouveau->max_capacity = sz;
    nouveau->size = 0;

    return nouveau;
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  push
 *  Description: Adds an element to the top of the stack.
 * =====================================================================================
 */
void push(Stack S, int ele) {
    if(S->size == S->max_capacity) {
        printf("Overflow error.\n");
        exit(-1);
    } else {
        (S->arr)[(S->size)++] = ele;
    }
    return;    
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  pop
 *  Description: Removes and returns an element from the top of the stack.  
 * =====================================================================================
 */
int pop(Stack S) {
    int tmp;

    if(S->size) {
        tmp = (S->arr)[--(S->size)];
    } else {
        printf("Underflow error.\n");
        exit(-1);
    }
    return tmp;
}
