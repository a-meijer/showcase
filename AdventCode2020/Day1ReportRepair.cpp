// Andrew Meijer
// Advent of Code 2020
// Entry Puzzle
// input: https://adventofcode.com/2020/day/1/input

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    int input[200];
    int i = 0; //input index

    string line;
    string::size_type sz;

    ifstream myfile ("Day1Input.txt");
    if (myfile.is_open()){
        while ( getline (myfile,line)){
            //convert the line to an integer in input array
            input[i] = stoi(line, &sz);
            //increment to the next slot of input array
            i++;

            //cout << line << '\n';
        }
        myfile.close();
    }
    else cout << "Unable to open file"; 

    int j = 0;
    int k = 0;
    for(i=0; i<200; i++){
        for(j=i+1; j<200; j++){
            for(k=j+1; k<200; k++){
                if(input[i] + input[j] + input[k] == 2020){           
                    cout << input[i] << ", " << input[j] << ", " << input[k] << '\n';
                }
            }
        }
    }



    return 0;
}