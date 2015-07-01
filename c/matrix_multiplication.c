/*
 * =====================================================================================
 *
 *       Filename:  matrix_multiplication.c
 *
 *    Description:  Creates two matrices and returns the product.
 *
 *        Version:  1.0
 *        Created:  04/22/2015 08:13:04 PM
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

typedef struct matrix {
    unsigned int rows;
    unsigned int cols;
    int * body;
} matrix;

matrix matrix_mult(matrix F, matrix G)
{
    matrix C;
    C.rows = F.rows;
    C.cols = G.cols;
    C.body = (int *)malloc(C.rows * C.cols * sizeof(int));
    
    int i, j, k;
    for(i = 0; i < C.rows; i++)
    {
        for(j = 0; j < C.cols; j++)
        {
            C.body[(i*C.rows)+j] = 0;
            for(k = 0; k < F.cols; k++)
            {
                C.body[(C.rows*i)+k] += (F.body[(F.rows*i)+k]*G.body[(G.rows*k)+j]);
            }
        }
    }
    return C;
}

void main(void)
{
    printf("Matrix multiplier; takes an n by m matrix and an m by k matrix, returns the n by k product matrix.\n");
    matrix A;
    matrix B;
    printf("Enter the number of rows for the first matrix: ");
    scanf("%d", &A.rows);
    printf("Enter the number of columns for the first matrix: ");
    scanf("%d", &A.cols);
    printf("Enter the number of rows for the second matrix: ");
    scanf("%d", &B.rows);
    printf("Enter the number of columns for the second matrix: ");
    scanf("%d", &B.cols);
 
    int i, j;
    if(A.cols != B.rows)
    {
        printf("Invalid matrices; A must have the same number of columns as B has rows.\n");
        return;
    }
    else {}

    if((A.body = (int *)malloc(A.rows * A.cols * sizeof(int))) == NULL)
    {
        printf("Memory allocation for A failed.");
        return;
    }
    else { printf("Memory allocated for A.\n"); }

    if((B.body = (int *)malloc(B.rows * B.cols * sizeof(int))) == NULL)
    {
        printf("Memory allocation for B failed.");
        return;
    }
    else { printf("Memory allocated for B.\n"); }

    printf("Successfully allocated A, B bodies.\n");

    for(i = 0; i < A.rows; i++)
    {
        //printf("Populating row %d of A.",i);
        for(j = 0; j < A.cols; j++)
        {
            printf("Populating A[%d][%d].\n",i,j);
            A.body[(A.rows*i)+j] = (rand() % 100);
        }
    }
    printf("Successfully populated A.");

    for(i = 0; i < B.rows; i++)
    {
        for(j = 0; j < B.cols; j++)
        {
            B.body[(B.rows*i)+j] = rand() % 100;
        }
    }
    printf("Successfully populated B.\n");

    matrix C = matrix_mult(A, B);

    for(i = 0; i < C.rows; i++)
    {
        for(j = 0; j < C.cols; j++)
        {
            printf("%d\t", C.body[(C.rows*i)+j]);
        }

        printf("\n");
    }

//    free(A.body);
//    free(B.body);
//    free(C.body);
    return;
}
