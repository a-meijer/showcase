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
 *      2021-Oct-10 - completed draft and unit tests; see activity log;
 *  Author: Andrew Meijer
 *  Purpose: Create backtracking recursion without datastructures
 */

#define N 16
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//return 1 if there is a collision; otherwise return 0
int check(char board[N][N], int x, int y){
    int i = x;
    int j = y;
    int gap = 0; //diagonal gap
    //nested for the squares in columns with queens
    for(i = x-1; i >= 0; i--){
        gap = x-i;
        for(j = 0; j < N; j++){
            //horizontal
            if(j == y){
                //collsion
                if(board[i][j] == '1'){
                    return 1;
                }
            }
            //diagonal NW
            if(j+gap == y && j >= 0){
                //if collision:
                if(board[i][j] == '1'){
                    return 1;
                }
            }
            //diagonal SW
            if(j-gap == y && j < N){
                //if collision:
                if(board[i][j] == '1'){
                    return 1;
                }
            }
        }
    }
    return 0;
}

//return the enumeration of all solutions from depth h recursively
int expand(char board[N][N], int h){
    //do not check for a proper input board: each column < h should have a queen placed
    //if h = N we filled the board with queens (thus found a solution); return 1
    if(h >= N){
        //printf("Found solution; board:\n");
        //printBoard(board);
        return 1;
    }
    int placedQueen = 0; //flag
    int i = 0; //loop index
    int j = 0; //loop index
    int k = 0; //loop index
    int cr = 0; //check result
    int runningTotal = 0;
    //for each square in column h, 
    for(i=0; i<N; i++){
        //check board[h][i]
        cr = check(board, h, i);
        //if check returns no-collision
        if(cr == 0){
            //make a new board
            char nextBoard[N][N];
            for(j=0; j<N; j++){
                for(k=0; k<N; k++){
                    nextBoard[j][k] = board[j][k];
                }
            }
            //place the new queen on the new board
            nextBoard[h][i] = '1';

            //increment h
            int h2 = h+1;

            //runningTotal += expand
            runningTotal = runningTotal + expand(nextBoard, h2);
        }
    }
    
    return runningTotal;

}

int main(){
    //initialize clock
    clock_t start, end;
    //check the clock
    start = clock();
    //initialize the root node
    char rootBoard[N][N];
    //The board for the root node is empty
    int i=0;
    int j=0;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            rootBoard[i][j] = '0';
        }  
    }
    //initialize results variable
    int result = 0;
    //start the recursion
    result = expand(rootBoard, 0);
    //jank
    int n = N;
    //print results
    printf("enumeration when N = %d yields %d solutions.\n", n, result);
    //check the clock
    end = clock();
    //calculate time
    int timeTaken = (int)(end-start);
    printf("Time taken: %d ticks.", timeTaken);
    return 0;
}