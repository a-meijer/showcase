// Copied from nxnQueens.cpp and modified on Mar. 31, 2021
// use main function to run tests for different methods.
// to run this program, enter the following command:
// g++ unitTests.cpp -o test
// to run this program, enter the following command:
//  



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

//return true if a new queen (is attacking  )
bool horizontal(vector<int> board, int col){
    //if any board values are equal, there is a horizontal collision
    for(int i=0; i<col; i++){
        if(board[col] == board[i]){
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
if(b[col-1] == 1 || b[col-1] == 3){ that's bad}
*/

//return true if queen on col is attacking each other diagonally

bool diagonal(vector<int> board, int col){

    int check = col-1;
    int expectedDifference = 0;
    for (int j = 0; j <= check; j++){
        expectedDifference = check-j;
        if (board[j] == check-expectedDifference || board[j] == check-expectedDifference){
            return true;
        }
    }
    return false;
    //board[col];
}

//Main is for unit testing; see comments
int main(){
    // For each function and class to test, use an answer key for several hard-coded test cases.
    

    // variables for testing horizontal and diagonal functions
    int number_of_tests = 8; //precise hard-code corresponds to hardcoded test values.
    //vectors are basically just a workaround to do pass-by-value imo
    //note in each of these tests, each test board should be passed along with every column to test; testing the 0th column should never return true
    //testing a negative one column should return error
    vector<vector<int>> tests = {{3,0,2,-1},
                                {0,0,0,0},
                                {0,0,0,1},
                                {1,0,0,0},
                                {0,2,0,0},
                                {-1,0,3,0},
                                {0,1,-1,-1},
                                {0,0,-1,-1}};
    //Answer Key, Horizontal:
    /*  
        {{0, 0, 0, 0},
        {0, 1, 1, 1},
        {0, 1, 1, 0},
        {0, 0, 1, 1},
        {0, 0, 1, 1},
        {0, 0, 0, 1},
        {0, 0, 0, 0},
        {0, 1, 0, 0}};
        
               */
    //Answer Key, Diagontal:
    /*  ~ 0 ~ 0 ~ 0 ~ 0 ~ 
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 1 ~ 1 ~ 0 ~
        ~ 0 ~ 0 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 1 ~
        ~ 0 ~ 1 ~ 0 ~ 1 ~       */

    // 5/20/2021 test results for horizontal
    /*  ~ 0 ~ 0 ~ 0 ~ 0 ~ 
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 1 ~ 1 ~ 0 ~
        ~ 0 ~ 0 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 1 ~
        ~ 0 ~ 1 ~ 0 ~ 1 ~       */
    // 5/20/2021 test results for diagonal
    /*  ~ 0 ~ 0 ~ 0 ~ 1 ~ 
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 0 ~
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 0 ~ 0 ~ 0 ~
        ~ 0 ~ 1 ~ 1 ~ 1 ~
        ~ 0 ~ 1 ~ 1 ~ 1 ~     */
    

    int col = 1;
    vector<bool> results;
    
    int i = 0;
    for(i=0; i < number_of_tests; i++){
        //4x4 Board
        for(col=0; col<4; col++){
            // Hard-coded horizontal/diagonal for test results in comments (5/20/2021 lines 102-119)
            results.push_back(diagonal(tests[i], col));
            //results.push_back(horizontal(tests[i], col));
        }
    }

    //printing
    i=0;
    for(int n : results){
        cout << " ~ " << n;
        i++;
        if(i==4){
            i=0;
            cout << " ~ " << endl;
        }
    }

    //BTNode

    //expand


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
