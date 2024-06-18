# BIRTHDAY BOY
## Introduction
Hello and welcome to my Birthday Boy project.
I call this project BirthdayBoy2 just to get out of the way of other people who already have projects named "Birthday Boy."
Today is February 28, 2022.
This project is a threefold test of my abilities:
 - I am testing my ability to contribute to my Github repository from this reimaged computer.
 - I am testing my ability to use Draw.io to make a flow diagram to act as a pseudocode for the project.
 - I am testing my ability to record the process of making this project and posting it to YouTube.

## Project Description
Create a program with two functions. 
Firstly, given a person's birth date, and a date representing the current day, calculate their age. 
Secondly, given a person's age & birthday, and a date representing the current day, calculate their birth year.
Notice the difference between birth date and birthday is that birthday excludes the year.

## Corpus Hermetica
 - I will be taking all my notes here with no initial form of organization, just my notes. This is a fairly small project, so I don't expect the documentation to develop much further. I am planning to make a video with content of me making the code for it and the diagram or whatever. I think I will record the diagram-making separately and 
 - I sketched up a diagram of how I want the program to be formed.
 - Now I am going into Diagrams.net (formerly Draw.io) to make a tidier version. I will screenshot the result to include in this project directory.
 - Testing OBS with with Firefox and VSCode. I will be using OpenShot for editing the videos. I ended up switching to a downloaded version of Diagrams.net instead of using Firefox.
 - I recorded a video of myself creating the diagram. I should include a copy of the screenshot in the github directory.
 - I want to write this solution in C++ so that I can easily create an executable. Googling snippets for I/O.
 - Starting video. . . let's build this live!
 - ...Cowboy coding ensues. I should remember to include the link to the video when I finally post this on GitHub.
 - I had to pause to download and install gcc.
 - Found source: https://www.programiz.com/c-programming/c-input-output
 - Found source: https://docs.microsoft.com/en-us/cpp/build/walkthrough-compile-a-c-program-on-the-command-line?view=msvc-170
 - Found source: https://www.tutorialspoint.com/cprogramming/c_input_output.htm
 - Things took a turn. I am not sure if the video recorded properly.
 - I am getting strange functionality:
    This program calculates a person's age or birthyear.
    What year is it?2022
    What month is it? (1 - 12)3
    What day is it? (1 - 31)1
    Are you looking for (a)ge or (b)irthyear?INPUT ERROR. Press any key to continue. . .a
    PS C:\PROG\showcase\BirthdayBoy2> 
 - March 2, let's go. I think the strange functionality is due to my getchar leaving a newline character behind. Use 2 getchars.
 - Fiddled with getchar cause it made no sense, but I got it working.
 - Tested age function manually with known use cases.
 - Wrote up birthyear function (similar to age function).
 - Tested birthyear function with basic use cases.
 - Renamed executable to birthdayBoy.
 - Project complete!
 - Testing from executable. . .Updating I/O tidiness. . .
 - Renamed executable to BirthdayBoy.
 - I still need to add the link to the video once it is posted. It will be in this file and in the comments of the source.
 - The video will be up soon:  https://youtu.be/u_UvX_vyqJk