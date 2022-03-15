//NAME: birthdayBoy.cpp
//DATE: 2022/03/01 - 2022/03/02
//AUTH: Andrew Meijer
//      Put your shorts on backwards:          https://github.com/a-meijer/showcase
//      Watch me make this program on YouTube: https://youtu.be/u_UvX_vyqJk
//PURPOSE: The purpose of this program is to meet the requirements of the project description.

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
    printf("What year is it? ");
    scanf("%d", &currentYear);
    printf("What month is it? (1 - 12): ");
    scanf("%d", &currentMonth);
    printf("What day is it? (1 - 31): ");
    scanf("%d", &currentDay);
}

//calculate Age
int calculateAge(){
    //start with current date and pYear
    //currentYear - person's year is a tentative estimate of age
    result = currentYear - pYear;

    printf("What month of the year was the person born? (1-12): ");
    scanf("%d", &pMonth); 

    //if pMonth < currentMonth, result is age
    if(pMonth < currentMonth){
        return result;
    
    //if person's Month == current Month, ask for days
    }else if(pMonth == currentMonth){
        printf("What day of the month was the person born? (1-31): ");
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
    // cYear - age = bYear iff current dayOfYear is past (or equal to) birth dayOfYear. Else, bYear -= 1

    //estimate the birth year
    result = currentYear - pAge;

    //check month
    printf("What month of the year was the person born? (1-12): ");
    scanf("%d", &pMonth); 

    //if birthday has passed this year, the estimate is correct
    if(pMonth < currentMonth){
        return result;
    }else if(pMonth == currentMonth){
        //check days
        printf("What day of the month was the person born? (1-31): ");
        scanf("%d", &pDay);

        if(pDay <= currentDay){
            return result;
        }else{
            result = result-1;
            return result;
        }


    }else{
        //birthday has not yet passed this year.
        result = result-1;
        return result;
    }//if else

}

int main() {
    char c = 'a'; //input for user selection

    printf("This program calculates a person's age or birthyear.\n");

    //input current date
    currentDate();

    printf("Are you looking for (a)ge or (b)irthyear? ");
    getchar(); //eats up the newline character. I thought this would come after a/b, but it comes before.
    c = getchar(); //
    if(c == 'a'){
        //input birthyear
        printf("What year what the person born? ");
        scanf("%d", &pYear); 
        //calculate age
        result = calculateAge();

    } else if(c == 'b'){
        //input age
        printf("How old is the person? ");
        scanf("%d", &pAge);
        //calculate Birthyear
        result = calculateBirthyear();

    } else {
        printf("INPUT ERROR: %c. Press any key to continue. . .", c);
        getchar();
        exit(0);
    }//if else
    
    //print output
    printf("\nPROGRAM OUTPUT: %d \n", result);

    //Press any key to continue
    printf("Press any key to continue. . .");
    getchar();
    getchar();
}

