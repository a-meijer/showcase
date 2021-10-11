/*
 *  Name: unitTests.c
 *  Date: Started 2021-Sept-20
 *      - Copied elements from nxnQueens.c
 *  Author: Andrew Meijer
 *  Purpose: Test functions to be used in nxnQueens.c
 *           Completed October 10, 2021.
 */

#define N 4
#include <stdio.h>
#include <stdlib.h>

//output for manual testing
void printBoard(char board[N][N]){
    int i=0;
    int j=0;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

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

//run hard-coded unit tests in main
int main(){
    //initialize the root node
    //char rootBoard[N][N];
    //The board for the root node is empty
    //int i=0;
    //int j=0;
    //for(i=0; i<N; i++){
    //    for(j=0; j<N; j++){
    //        rootBoard[i][j] = '0';
    //    }  
    //}
    //int result = 0;
    //result = expand(rootBoard, 0);
    //printBoard(rootBoard);
    
    /******************UNIT TESTS FOR EXPAND FUNCTION******************/
    //4 Test cases include:
    //                      external node with no solutions, 
    //                      external node with one or more solutions, 
    //                      internal node that yields no solutions,
    //                  and internal node that yields one or more solutions.
    /*
    //Hard-coding tests with N=4
    // ALL TESTS PASS FOR EXPAND FUNCTION, OCT.10, 2021

    //initialize boards
    char testBoard0[N][N];
    char testBoard1[N][N];
    char testBoard2[N][N];
    char testBoard3[N][N];

    //set values of each test board
    
    //external node with no solutions:
    int h0 = 3;
    int ans0 = 0;
    testBoard0[0][0] = '0'; testBoard0[1][0] = '1'; testBoard0[2][0] = '0'; testBoard0[3][0] = '0';
    testBoard0[0][1] = '0'; testBoard0[1][1] = '0'; testBoard0[2][1] = '0'; testBoard0[3][1] = '0';
    testBoard0[0][2] = '0'; testBoard0[1][2] = '0'; testBoard0[2][2] = '1'; testBoard0[3][2] = '0';
    testBoard0[0][3] = '1'; testBoard0[1][3] = '0'; testBoard0[2][3] = '0'; testBoard0[3][3] = '0';

    //external node with one or more solutions:
    int h1 = 3;
    int ans1 = 1;
    testBoard1[0][0] = '0'; testBoard1[1][0] = '0'; testBoard1[2][0] = '1'; testBoard1[3][0] = '0'; 
    testBoard1[0][1] = '1'; testBoard1[1][1] = '0'; testBoard1[2][1] = '0'; testBoard1[3][1] = '0'; 
    testBoard1[0][2] = '0'; testBoard1[1][2] = '0'; testBoard1[2][2] = '0'; testBoard1[3][2] = '0'; 
    testBoard1[0][3] = '0'; testBoard1[1][3] = '1'; testBoard1[2][3] = '0'; testBoard1[3][3] = '0'; 

    //internal node with no solutions:
    int h2 = 1;
    int ans2 = 0;
    testBoard2[0][0] = '1'; testBoard2[1][0] = '0'; testBoard2[2][0] = '0'; testBoard2[3][0] = '0'; 
    testBoard2[0][1] = '0'; testBoard2[1][1] = '0'; testBoard2[2][1] = '0'; testBoard2[3][1] = '0'; 
    testBoard2[0][2] = '0'; testBoard2[1][2] = '0'; testBoard2[2][2] = '0'; testBoard2[3][2] = '0'; 
    testBoard2[0][3] = '0'; testBoard2[1][3] = '0'; testBoard2[2][3] = '0'; testBoard2[3][3] = '0'; 

    //internal node with one or more solutions:
    int h3 = 2;
    int ans3 = 1;
    testBoard3[0][0] = '0'; testBoard3[1][0] = '0'; testBoard3[2][0] = '0'; testBoard3[3][0] = '0'; 
    testBoard3[0][1] = '1'; testBoard3[1][1] = '0'; testBoard3[2][1] = '0'; testBoard3[3][1] = '0'; 
    testBoard3[0][2] = '0'; testBoard3[1][2] = '0'; testBoard3[2][2] = '0'; testBoard3[3][2] = '0'; 
    testBoard3[0][3] = '0'; testBoard3[1][3] = '1'; testBoard3[2][3] = '0'; testBoard3[3][3] = '0'; 

    //expand each board and compare the results with each answer
    int result = 0;
    
    //test board 0
    result = expand(testBoard0, h0);
    if(result != ans0){
        printf("test 0 failed.");
        exit(0);
    }

    //test board 1
    result = expand(testBoard1, h1);
    if(result != ans1){
        printf("test 1 failed.");
        exit(0);
    }

    //test board 2
    result = expand(testBoard2, h2);
    if(result != ans2){
        printf("test 2 failed. %d != %d", ans2, result);
        exit(0);
    }

    //test board 3
    result = expand(testBoard3, h3);
    if(result != ans3){
        printf("test 3 failed.");
        exit(0);
    }

    printf("All tests passed.");
    // ALL TESTS PASS FOR EXPAND FUNCTION, OCT.10, 2021
    */


    /******************UNIT TESTS FOR CHECK FUNCTION******************/
    /* all check function tests pass, OCT.4, 2021
    //8 test boards:
    //0100   1111   1110   1000   1011   0101   1000   0000
    //0000   0000   0001   0111   0000   0000   0100   0001
    //0010   0000   0000   0000   0100   0000   0010   0010
    //1000   0000   0000   0000   0000   0010   0001   1100
    //Answer Key:
    //000    0111   0111   0111   0011    001   0111   0111

    //I'll tests each square on each board that has a queen placed, for a total of 30 tests

    //initialize boards
    char testBoard0[N][N];
    char testBoard1[N][N];
    char testBoard2[N][N];
    char testBoard3[N][N];
    char testBoard4[N][N];
    char testBoard5[N][N];
    char testBoard6[N][N];
    char testBoard7[N][N];

    //set values of each test board ~ easy hardcoding with VS Code
    testBoard0[0][0] = '0'; testBoard0[1][0] = '1'; testBoard0[2][0] = '0'; testBoard0[3][0] = '0';
    testBoard0[0][1] = '0'; testBoard0[1][1] = '0'; testBoard0[2][1] = '0'; testBoard0[3][1] = '0';
    testBoard0[0][2] = '0'; testBoard0[1][2] = '0'; testBoard0[2][2] = '1'; testBoard0[3][2] = '0';
    testBoard0[0][3] = '1'; testBoard0[1][3] = '0'; testBoard0[2][3] = '0'; testBoard0[3][3] = '0';

    testBoard1[0][0] = '1'; testBoard1[1][0] = '1'; testBoard1[2][0] = '1'; testBoard1[3][0] = '1'; 
    testBoard1[0][1] = '0'; testBoard1[1][1] = '0'; testBoard1[2][1] = '0'; testBoard1[3][1] = '0'; 
    testBoard1[0][2] = '0'; testBoard1[1][2] = '0'; testBoard1[2][2] = '0'; testBoard1[3][2] = '0'; 
    testBoard1[0][3] = '0'; testBoard1[1][3] = '0'; testBoard1[2][3] = '0'; testBoard1[3][3] = '0'; 

    testBoard2[0][0] = '1'; testBoard2[1][0] = '1'; testBoard2[2][0] = '1'; testBoard2[3][0] = '0'; 
    testBoard2[0][1] = '0'; testBoard2[1][1] = '0'; testBoard2[2][1] = '0'; testBoard2[3][1] = '1'; 
    testBoard2[0][2] = '0'; testBoard2[1][2] = '0'; testBoard2[2][2] = '0'; testBoard2[3][2] = '0'; 
    testBoard2[0][3] = '0'; testBoard2[1][3] = '0'; testBoard2[2][3] = '0'; testBoard2[3][3] = '0'; 

    testBoard3[0][0] = '1'; testBoard3[1][0] = '0'; testBoard3[2][0] = '0'; testBoard3[3][0] = '0'; 
    testBoard3[0][1] = '0'; testBoard3[1][1] = '1'; testBoard3[2][1] = '1'; testBoard3[3][1] = '1'; 
    testBoard3[0][2] = '0'; testBoard3[1][2] = '0'; testBoard3[2][2] = '0'; testBoard3[3][2] = '0'; 
    testBoard3[0][3] = '0'; testBoard3[1][3] = '0'; testBoard3[2][3] = '0'; testBoard3[3][3] = '0'; 

    testBoard4[0][0] = '1'; testBoard4[1][0] = '0'; testBoard4[2][0] = '1'; testBoard4[3][0] = '1';
    testBoard4[0][1] = '0'; testBoard4[1][1] = '0'; testBoard4[2][1] = '0'; testBoard4[3][1] = '0';
    testBoard4[0][2] = '0'; testBoard4[1][2] = '1'; testBoard4[2][2] = '0'; testBoard4[3][2] = '0';
    testBoard4[0][3] = '0'; testBoard4[1][3] = '0'; testBoard4[2][3] = '0'; testBoard4[3][3] = '0';

    testBoard5[0][0] = '0'; testBoard5[1][0] = '1'; testBoard5[2][0] = '0'; testBoard5[3][0] = '1';
    testBoard5[0][1] = '0'; testBoard5[1][1] = '0'; testBoard5[2][1] = '0'; testBoard5[3][1] = '0';
    testBoard5[0][2] = '0'; testBoard5[1][2] = '0'; testBoard5[2][2] = '0'; testBoard5[3][2] = '0';
    testBoard5[0][3] = '0'; testBoard5[1][3] = '0'; testBoard5[2][3] = '1'; testBoard5[3][3] = '0';

    testBoard6[0][0] = '1'; testBoard6[1][0] = '0'; testBoard6[2][0] = '0'; testBoard6[3][0] = '0';
    testBoard6[0][1] = '0'; testBoard6[1][1] = '1'; testBoard6[2][1] = '0'; testBoard6[3][1] = '0';
    testBoard6[0][2] = '0'; testBoard6[1][2] = '0'; testBoard6[2][2] = '1'; testBoard6[3][2] = '0';
    testBoard6[0][3] = '0'; testBoard6[1][3] = '0'; testBoard6[2][3] = '0'; testBoard6[3][3] = '1';

    testBoard7[0][0] = '0'; testBoard7[1][0] = '0'; testBoard7[2][0] = '0'; testBoard7[3][0] = '0';
    testBoard7[0][1] = '0'; testBoard7[1][1] = '0'; testBoard7[2][1] = '0'; testBoard7[3][1] = '1';
    testBoard7[0][2] = '0'; testBoard7[1][2] = '0'; testBoard7[2][2] = '1'; testBoard7[3][2] = '0';
    testBoard7[0][3] = '1'; testBoard7[1][3] = '1'; testBoard7[2][3] = '0'; testBoard7[3][3] = '0';

    char answerKey[30] = {0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,1};
    char results[30];
    int resultsIndex = 0;
    
    //Run tests for each test board
    //Board 0
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard0[i][j] == '1'){
                results[resultsIndex] = check(testBoard0, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 1
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard1[i][j] == '1'){
                results[resultsIndex] = check(testBoard1, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 2
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard2[i][j] == '1'){
                results[resultsIndex] = check(testBoard2, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 3
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard3[i][j] == '1'){
                results[resultsIndex] = check(testBoard3, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 4
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard4[i][j] == '1'){
                results[resultsIndex] = check(testBoard4, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 5
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard5[i][j] == '1'){
                results[resultsIndex] = check(testBoard5, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 6
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard6[i][j] == '1'){
                results[resultsIndex] = check(testBoard6, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Board 7
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            //run test if queen is on i,j
            if(testBoard7[i][j] == '1'){
                results[resultsIndex] = check(testBoard7, i, j);
                resultsIndex = resultsIndex + 1;
            }  
        }  
    }
    //Compare the results with the answer key. . .
    for(i=0; i<30; i++){
        if(answerKey[i] != results[i]){
            printf("Failed test number %d.", i);
            exit(0);
        }
        //printf("%d:\tans: %d.\tres: %d.\n", i, answerKey[i], results[i]);
    }
    printf("All tests passed.");
    //ALL CHECK FUNCTION TESTS PASS, OCT.4, 2021*/ 
}
