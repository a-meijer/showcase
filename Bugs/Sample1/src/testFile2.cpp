//  NAME: testFile2.cpp
//  DATE: October 10, 2021
//  AUTHOR: Andrew Meijer
//  PURPOSE: This file is identical to testFile1.cpp, except lines 32, 33, 37, 39, and 40 are commented out.
//           This file will print, but the other file will not.

#define N 4

#include <vector>
#include <iostream>

using namespace std;

class Node {
    public: 
        Node* next;
        vector<int> board;

        Node() {
            for(int i = 0; i<N; i++){
                board.push_back(-1);
            }            
        }
        Node(vector<int> parentBoard) {
            //board deep copies parentBoard
            for(int i=0; i<N; i++){
                board[i] = parentBoard[i];
            }
        }
};

int main(){
    //Node* node1 = new Node();
    //Node* node2 = new Node(node1->board);

    int i=0;
    for(i=0; i<N; i++){
            //if(node1->board[i] != node2->board[i]){
                cout << "test successful." << endl;
                //exit(0);
            //}
    }
    cout << "boards identical." << endl;
    exit(0);
    return 0;
}