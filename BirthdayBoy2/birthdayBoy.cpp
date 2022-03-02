#include <stdio.h>
#include <stdlib.h>

// Global Variables 
int currentYear = 2022; //current year
int currentMonth = 3; //month of the year
int currentDay = 1; //day of the month
int pAge = 0; //person's age
int pYear = 0; //person's birth year
int pMonth = 1; //person's birth month of year
int pDay = 1; //person's birth day (of month)
int result; //calculated birthyear or age for output

//Input year, month of year, and day of month.
void currentDate(){
    printf("What year is it?");
    scanf("%d", &currentYear);
    printf("What month is it? (1 - 12)");
    scanf("%d", &currentMonth);
    printf("What day is it? (1 - 31)");
    scanf("%d", &currentDay);
}

//calculate Age
int calculateAge(){
    //start with current date and pYear
    //currentYear - person's year is a tentative estimate of age
    result = currentYear - pYear;

    printf("What month of the year was the person born? (1-12):");
    scanf("%d", &pMonth); 

    //if pMonth < currentMonth, result is age
    if(pMonth < currentMonth){
        return result;
    
    //if person's Month == current Month, ask for days
    }else if(pMonth == currentMonth){
        printf("What day of the month was the person born? (1-31):");
        scanf("%d", &pDay);

        //same idea as months
        if(pDay <= currentDay){
            return result;

        }else{
            //pDay > currentDay
            result = result - 1;
            return(result);
        }
    
    //if person's month ? currentMonth, person is one year younger than estimate
    }else{
        //pMonth > currentMonth
        result = result - 1;
        return(result);
    }
}

//calculate Birthyear
int calculateBirthyear(){
    //start with current date and pAge

}

int main() {
    char c = 'a'; //input for user selection

    printf("This program calculates a person's age or birthyear.\n");

    //input current date
    currentDate();

    printf("Are you looking for (a)ge or (b)irthyear?");
    c = getchar();
    if(c == 'a'){
        //input birthyear
        printf("What year what the person born?");
        scanf("%d", &pYear); 
        //calculate age
        result = calculateAge();

    } else if(c == 'b'){
        //input age
        printf("How old is the person?");
        scanf("%d", &pAge);
        //calculate Birthyear
        result = calculateBirthyear();

    } else {
        printf("INPUT ERROR. Press any key to continue. . .");
        getchar();
        exit(0);
    }//if else
    
    //print output
    printf("%d", result);

    //Press any key to continue
    printf("Press any key to continue. . .");
    getchar();
}

