/*
 *  Name: nxnQueens.c
 *  Date: Started 2020-Nov-15
 *      2020-Dec-07:
 *          Adding nested structure; 
 *          Implementing algorithm - backtracking enumeration;
 *          This is a recursive algorithm.
 *      2021-Jan- see activity log.
 *      2021-June - see activity log.
 *      2021-July - see activity log. . . See activity log for further updates.
 *  Author: Andrew Meijer
 *  Purpose: Create backtracking recursion with datastructures
 */

#define N 4
#include <stdio.h>
#include <stdlib.h>

struct BTNode {
    int h; //the current column in the algorithm
    struct BTNode* c[N]; //pointers to child nodes
    struct ChessBoard* chess_struct; //in board[x][y]: x = h, y = c[i]. Character '0' is empty; character '1' has a queen on that square.
};

//this struct is a nifty workaround so I can pass a board pointer to functions because I was stuck on compilation warnings
struct ChessBoard {
    char b[N][N];
};

//Return '1' if the Queen on h column is attacking any Queens that have already been placed on columns i where i < h horizontally.
//else return '0'
char horizontal(struct ChessBoard * board, int h){
    //find the row on column h that has a Queen, and call it Q
    int Q = 0;
    for(Q = 0; Q < N; Q++){
        //if there is a queen on row Q, we're done: let's break out of here!
        if(board->b[h][Q] == '1'){
            break;
        }
    }
    //Now int Q is set to the row of the queen on column h

    int i = h-1;
    while(i >= 0){
        //if there is a path-ruining horizontal attack from the newly-paced queen
        if(board->b[i][Q] == '1'){
            //collision
            return '1';
        }

        //exit condition: i < 0
        i = i-1;
    }//while

    //no horizontal collision from column h row Q
    return '0';
}

//Return '1' if the Queen on column h is attacking any Queens that have already been placed on columns i where i < h diagonally.
//else return '0'
char diagonal(struct ChessBoard * board, int h){
    //find the row on column h that has a Queen, and call it Q
    int Q = 0;
    for(Q = 0; Q < N; Q++){
        //if there is a queen on row Q, we're done: let's break out of here!
        if(board->b[h][Q] == '1'){
            break;
        }
    }
    //Now int Q is set to the row of the queen on column h

    int i = h-1;
    int diff = h-i;
    while(i >= 0){
        //if row Q-diff is on the board, check for a queen on that row, column i
        if(Q-diff >= 0 && Q-diff <= 3){
            if(board->b[i][Q-diff] == '1'){
                //collision
                return '1';
            }
        }
        //if row Q+diff is on the board, check for a queen on that row, column i
        if(Q+diff >= 0 && Q+diff <= 3){
            if(board->b[i][Q+diff] == '1'){
                //collision
                return '1';
            }
        }

        //exit condition: i < 0
        i = i-1;
        //b(i,y) is diagonal to b(h,Q) when y = Q +- (h-i)
        diff = h-i;
    }//while

    //no diagonal collision from column h row Q
    return '0';


}

//include a parent node as an argument to initialize any child node
//Careful not to point to the parent board from the child; instead, DEEP COPY, or else it will ruin the algorithm
//paramenter x is the number of the child: 0 <= x < N s.t. board[h][x]='1';
//return the running enumeration total such that if the BTTree root is expanded, it would return the solution. ( In my first draft I am expanding the root in main)
//The root node is expanded in the main function, so all the roots expanded in here have a parent node.
int expand(struct BTNode * p, struct BTNode * n, int x){

    printf("Expanding. . .");

    //initialize node height
    n->h = 0;

    //initialize the empty board
    int i=0;
    int j=0;
    for(i=0; i<N; i=i+1){
        for(j=0; j<N; j=j+1){
            n->chess_struct->b[i][j] = '0';
        }
    }

    //allocate space for the child nodes
    i=0;
    for(i=0; i<N; i=i+1){
        n->c[i] = (struct BTNode *)malloc(sizeof(struct BTNode));
    }

    //Summate the return values for expansion of each child node
    int total = 0;
    for(i=0; i<N; i++){
        total = total + expand(n, n->c[i], i);
    }
    printf("Returning %d", total);
    return total;
}

//OLD EXPAND
//for reference
/*int expand(struct BTNode * p, struct BTNode * n, int x){

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
            tempoChar = p->ChessBoard->b[i][j];
            n->board[i][j] = tempoChar;
        }
    }
    
    //change the board by adding a new queen
    n->board[n->h][x] = '1';

    //test if the new queen is attacking any others
    char horizontalReturnVal = horizontal(n->board, n->h);
    char diagonalReturnVal = diagonal(n->board, n->h);

    if(horizontalReturnVal == '1'){
        printf("?");
    }else{
        printf("!");
    }

    //allocate space for the child nodes
    i=0;
    for(i=0; i<N; i=i+1){
        n->c[i] = (struct BTNode *)malloc(sizeof(struct BTNode));
    }
}*/

int main(){

    printf("Initializing. . .");

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
            root->chess_struct->b[i][j] = '0';
        }
    }

    printf("Allocating Space. . .");

    //allocate space for the child nodes
    i=0;
    for(i=0; i<N; i=i+1){
        root->c[i] = (struct BTNode *)malloc(sizeof(struct BTNode));
    }

    printf("Running. . .");

    //Summate the return values for expansion of each child node
    int total = 0;
    for(i=0; i<N; i++){
        total = total + expand(root, root->c[i], i);
    }

    printf("Result: %d", total);

    return 0;
}