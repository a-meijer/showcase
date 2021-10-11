// Copied from nxnQueens.cpp and modified on Mar. 31, 2021
// use main function to run tests for different methods.
// May 28, 2021, Andrew Meijer
// - Updated descriptions for horizontal and diagonal functions
// - This program will test the BTNode class, and the 3 functions
// June 2, 2021, Andrew Meijer
// - The idea behind unitTests.cpp is that segments of the project can be tested at a time, and then copied over to nxnQueens.cpp
// - I am planning to create four segments: Horizontal, Diagonal, BTNode, and Expand
// - renamed project to nxnQueens
// - (no upload)
// June 12, 2021, Andrew Meijer
// - Updated comment(s) 
// - (no upload)
// June 15, 2021, Andrew Meijer
// - wrote answer key for diagonal function; I already wrote the one for horizontal previously sometime
// - Added tests for diagonal and horizontal, to compare the results with my answer keys! Compiling. . .
// - . . .corrected compile error, typo: "diagontal" . . .
// - . . .compiled! Failed first test. Fixed coding error, changed "==" to "!=" when comparing results with answer key
// Finally useful results?:
//      Failed Diagonal Test 0 column 3
//      No match: 1 , 0
// I believe the answer key is correct, so now I get to fix the function, "diagonal"
// June 28, 2021, Andrew Meijer
// - Completed second draft of diagonal function, forgotten return statement.
//      Failed Horizontal Test 6 column 3
//      No match: 1 , 0
// - CooL! Determined that the function was testing for board[i] != -1, but not board[col] != -1.
// - Horizontal and Diagonal functions pass all unit tests; complete!
// - Copying diagonal and horizontal functions back into nxnQueens.cpp
// - Added into main project directory. . . See main activity log for further updates.

// Board size for NxN queens: harcoded!
#define N 4

#include <vector>
#include <iostream>

using namespace std;
/*
class BTTree {
    public:
        BTNode* root;
        
        BTTree(){
            BTNode* root = new BTNode();
        }
};*/

class BTNode {
    public: 
        BTNode* nextChild;
        vector<int> board;

        BTNode() {
            for(int i = 0; i<N; i++){
                board.push_back(-1);
            }            
        }
        BTNode(vector<int> parentBoard) {
            //board deep copies parentBoard
            for(int i=0; i<N; i++){
                board[i] = parentBoard[i];
            }
        }
};

//Main is for unit testing; see comments
int main(){
    // ***** TESTS FOR BTNode and BTTree constructors *****

    //testing the BTNode class constructors:
    //to test BTNode class, create a BTNode using each constructor, change the value of one of the columns on one of the boards, and then compare the boards.
    BTNode* node1 = new BTNode();
    BTNode* node2 = new BTNode(node1->board);

    int i=0;
    for(i=0; i<N; i++){
            if(node1->board[i] != node2->board[i]){
                cout << "test successful." << endl;
                exit(0);
            }
    }
    cout << "boards identical." << endl;
    exit(0);

    //testing the BTTree class:
    //BTTree* tree = new BTTree();

    //testing the BTTree.build function:

    //testing the BTTree.enumerate function:

    // vector<vector<int> > solutions = expand(root);
    //vector<int> board;
    //board.push_back(0);
    //board.push_back(2);
    //board.push_back(2);
    //board.push_back(-1);

    return 0;




    // ***** TESTS FOR HORIZONTAL AND DIAGONAL FUNCTIONS *****
    /*
    // For each function and class to test, use an answer key for eight (8) hard-coded test cases.
    int number_of_tests = 8; //precise hard-code corresponds to hardcoded test values.

    //vectors are basically just a workaround to do pass-by-value imo

    //testing both horizontal and diagonal functions can be done with the same set of test data
    //for each of the 8 test cases/boards numbered from 0 to 7, each function will be tested for each column, for a total of 32 tests for each horizontal and diagonal.
    //..........................//DATA........test0..........test1..........test2..........test3..........test4..........test5..........test6..........test7.......
    vector<vector<int>> tests_horidiag =   { { 3, 0, 2,-1}, { 0, 0, 0, 0}, { 0, 0, 0, 1}, { 1, 0, 0, 0}, { 0, 2, 0, 0}, {-1, 0, 3, 0}, { 0, 1,-1,-1}, { 0, 0,-1,-1}};
    //Answer Key, Horizontal:
    vector<vector<int>> ans_horizontal =    { { 0, 0, 0, 0}, { 0, 1, 1, 1}, { 0, 1, 1, 0}, { 0, 0, 1, 1}, { 0, 0, 1, 1}, { 0, 0, 0, 1}, { 0, 0, 0, 0}, { 0, 1, 0, 0}};
    //Answer Key, Diagontal:
    vector<vector<int>> ans_diagonal =      { { 0, 0, 0, 0}, { 0, 0, 0, 0}, { 0, 0, 0, 1}, { 0, 1, 0, 0}, { 0, 0, 0, 1}, { 0, 0, 0, 0}, { 0, 1, 0, 0}, { 0, 0, 0, 0}};
        
    //Nested loop: compare the test output for each column of each test board and compare with the answer keys.

    //nested loop variables
    int i = 0;
    int j = 0;
    vector<bool> results; //pushpop stack
    
    //outer loop uses variable i to index the test
    for(i=0; i < number_of_tests; i++){
        // inner loop uses variable j to index column (to pass as an argument to diagonal and horizontal)
        for(j=0; j<N; j++){
            //store test results on stack (by running the function to test)
            results.push_back(horizontal(tests_horidiag[i], j));
            //branch if the test results do not match the answer key
            if(results[0] != ans_horizontal[i][j]){
                cout << "Failed Horizontal Test " << i << " column " << j << endl;
                cout << "No match: " << results[0] << " , " << ans_horizontal[i][j] << endl;
                exit(0);
            }
            //remove the results from the stack
            results.pop_back();

            //store test results on stack (by running the function to test)
            results.push_back(diagonal(tests_horidiag[i], j));
            //branch if the test results do not match the answer key
            if(results[0] != ans_diagonal[i][j]){
                cout << "Failed Diagonal Test " << i << " column " << j << endl;
                cout << "No match: " << results[0] << " , " << ans_horizontal[i][j] << endl;
                exit(0);
            }
            //remove the results from the stack
            results.pop_back();

        }//for each column
    }//for each test
    */
}
