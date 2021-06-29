//enumerate nxnQueens using C++ vectors
// ~ June 28. 2021, Andrew Meijer
// - Replaced previous nxnQueens.cpp file from separate project
// - added horizontal and diagonal functions from unitTests.cpp

#define N 4
#include <vector>
#include <iostream>

using namespace std;

class BTNode {
    public:
        BTNode* children[N];
        vector<int> board;

        BTNode() {
            for(int i = 0; i<N; i++){
                board[i] = -1;
            }            
        }
        BTNode(vector<int> parentBoard) {
            //board deep copies parentBoard
            for(int i=0; i<N; i++){
                board[i] = parentBoard[i];
            }
        }
};

//place a queen in each row for each child node; 
//test if each node passes horizontal and diagonal; 
//expand each node that passes
vector<vector<int> > expand(BTNode root){
    for(int i=0; i<N; i++){

    }
}

//Return true if a queen on col is attacking queens horizontally on columns i where i < col, else return 0
//horizontal passes all tests in unitTests.cpp on June 28, 2021.
bool horizontal(vector<int> board, int col){
    //if any board values are equal other than -1, there is a horizontal collision
    for(int i=0; i<col; i++){
        if(board[col] == board[i] && board[col] != -1 && board[i] != -1){
            return true;
        }            
    }
    return false;
}


/*
diagonal(board, 2);
vector<int> {0, 2, 2, -1}
       |
   x   v
   0 1 2 3
0  x O O O
1  O x O O
2  O O 0 O
3  O O x O
b[col] = 2
if(b[col-1] == 1 || b[col-1] == 3){ that's diagonal}
*/

//Return true if a queen on col is attacking queens diagonally on columns i where i < col, else return 0
//diagonal passes all tests in unitTests.cpp on June 28, 2021.
bool diagonal(vector<int> board, int col){

    //the difference between two columns relates to whether the queens placed in those columns are diagonal to each other.
    int colDiff = 0;

    //for each column to the left of col
    for(int i = col-1; i >= 0; i--){

        colDiff = col-i;

        //according to the vector encoding of the boards,
        //if board[i] == board[col] +- colDiff, and neither column is empty, then the queen on column i is diagonal to the queen on column col 
        if(board[i] == board[col] + colDiff || board[i] == board[col] - colDiff){
            //if queen is placed on i column
            if(board[i] != -1 && board[col] != -1){
                return true;
            }//if
        }//if
    }//for
    return false;
}

int main(){
    // BTNode root = new BTNode();

    // vector<vector<int> > solutions = expand(root);
    vector<int> board;
    board.push_back(0);
    board.push_back(2);
    board.push_back(2);
    board.push_back(-1);
    bool v = diagonal(board, 3);

    cout << v << endl;

    return 0;
}
