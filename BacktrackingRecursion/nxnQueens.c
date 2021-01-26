/*
 *  Name: nxnQueens.c
 *  Date: Started 2020-Nov-15
 *      2020-Dec-07:
 *          Adding nested structure; 
 *          Implementing algorithm - backtracking enumeration;
 *          This is a recursive algorithm.
 *      2021-Jan-
 *  Author: Andrew Meijer
 *  Purpose: Create backtracking recursion with datastructures
 */

#define N 4
#include <stdio.h>

struct BTNode {
    int h; //the current row in the algorithm
    struct BTNode* c[N]; //pointers to child nodes
    char board[N][N]; //in board[x][y]: x = h, y = c[i]. Character '0' is empty; character '1' has a queen on that square.
};

//Return '1' if the board is sound diagonally(not attaching any other queens)
//else return '0'
char horizontal(char * b[N][N]){
    
}

//Return '1' if the board is sound diagonally(no queens attacking each other)
//else return '0'
char diagonal(char * b[N][N]){

}

//include a parent node as an argument to initialize any child node
//Careful not to point to the parent board, that would ruin the algorithm
//paramenter x is the number of the child: 0 <= x < N s.t. board[h][x]='1';
//return the running enumeration total such that if the BTTree root is expanded, it would return the solution. ( In my first draft I am expanding the root in main)
int expand(struct BTNode * p, struct BTNode * n, int x){

    //allocate space for the new node
    n = (struct BTNode *)malloc(sizeof(struct BTNode));

    //increment height
    //does this copy the pointer? I don't think so. . .
    n->h = p->h + 1;

    //temporary variable to transfer data between boards
    char tempoChar = '0';
    //initialize the board
    //be careful to not point to the same board as parent
    int i=0;
    int j=0;
    for(i=0; i<N; i=i+1){
        for(j=0; j<N; j=j+1){
            tempoChar = p->board[i][j];
            n->board[i][j] = tempoChar;
        }
    }
    
    //change the board by adding a new queen
    n->board[n->h][x] = '1';

    //test if the new queen is attacking any others


    //allocate space for the child nodes
    int i=0;
    for(i=0; i<N; i=i+1){
        n->c[i] = (struct BTNode *)malloc(sizeof(struct BTNode));
    }
}

int main(){
    //In the main function I expand the root node

    //initialize the root node pointer
    struct BTNode * root;
    //allocate space for the root node
    root = (struct BTNode *)malloc(sizeof(struct BTNode));

    //initialize root height
    root->h = 0;

    //initialize the empty board
    int i=0;
    int j=0;
    for(i=0; i<N; i=i+1){
        for(j=0; j<N; j=j+1){
            root->board[i][j] = '0';
        }
    }

    //allocate space for the child nodes
    int i=0;
    for(i=0; i<N; i=i+1){
        root->c[i] = (struct BTNode *)malloc(sizeof(struct BTNode));
    }

    //Summate the return values for expansion of each child node
    int total = 0;
    for(i=0; i<N; i++){
        total = total + expand(root, root->c[i], i);
    }

    printf("%d", total);

    return 0;
}

/*
 *** LINKED LIST SYNTAX FOR REFERENCE***

    int data[dataSize] = {12, 1, 4, 6, 18, 23, 2, 10, 9, 0}; 

    struct LLNode *nodes[dataSize];

    int i=0;
    for(i=0; i<10; i=i+1){
        nodes[i] = NULL;
        nodes[i] = (struct LLNode *)malloc(sizeof(struct LLNode));
        nodes[i]->datum = data[i];
    }

    //Two loops  is still linear time
    for(i=0; i<9; i=i+1){
        nodes[i]->next = nodes[i+1];
    }
    nodes[9]->next = NULL;

    traverse(nodes[0]);
*/