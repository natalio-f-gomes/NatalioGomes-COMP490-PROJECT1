# Author: Natalio Gomes
#### Date: Jan 29, 2026
#### Class: COMP 490

## Project 1 Sprint 1

### Summary
This multi-part project will provide you an chance to practice your programming skills and practice with the agile software development methodology, continuous integration, automated testing and other more industry oriented practices that we don't often use in academia.

### Agile
This project will be done in the agile methodology in that it will be done in a series of sprints. week there will be a 3-6 hour (estimated – this assumes you start early enough to walk away when things get complected) assignment which builds on the previous assignment. So be sure to be careful to practice good software development techniques so that you don't make life difficult for yourself later.

### Individual work
Later in the semester we will work on group work. For this project you will work individually. You may ask your classmates for pointers on getting your git/github/jetbrains toolchain setup, but each student should be doing their own work. You can of course use my "as long as you are just talking and no one is on a recording device like a computer" guidelines to point each other at good libraries to do this work.

### Tools
Use the the correct Jetbrains IDE for your language of choice (see below) - alternatively, in a later sprint I plan ask you to use google antigravity so you might use it. If you have not yet done so, activate your jetbrains student account to get one year of academic use of the jetbrains professional development tools. For those who really know vsCode and can make everything work on their own, feel free to use that toolchain, as long as the result works on my machine.

### Version Control
In this class we will use git for version control.

### Programming languages
You may use one of several programming languages for this first project so long as you make "it works on my machine" (not just yours). With that in mind the following language are supported in this class.
I don't have any access to MS Windows machines. All of my grading will be done on linux - which is also what the Automated testing systems on github use

#### Python
use Python versions 3.10-3.14. I have different defaults on my three linux machines, so mention which version you are sure works. Use requirements.txt or uv with pyproject.toml to manage external dependancies.

#### Java
Java 21or 25, 25 is the current LTS (Long Term Service) version of Java, that's what I'll run/test your work on. If you are using java, use maven (or gradle) to manage your dependencies in intellij. Be sure to check in the entire project with the build.gradle files when committing/pushing your version control

#### Go
if you use go, use a go mod file and use  at least go 1.21, which allows auto update of go in the go.mod file

#### Rust
If you use rust, be sure to have all your dependencies properly in your cargo.toml

#### C or C++
if you want to do C or C++ be sure to have a configure file and a makefile so it builds properly.

#### Other languages
if you want to use other languages, see me to make sure I can support them. The main issue is the "Works on My machine" issue. Your program has to work on a standard server (which runs linux) with minimal additional setup from me. If you provide a set of automation files that take a while to run while I'm away from my machine that will work.

### The Project Overview
Currently, the industry is falling all over itself to build voice driven applications - especially if it can keep the AI bubble going a little longer. We shall see if this trend lasts, but since it is very popular today, we will explore the idea of a voice driven scheduling application in the first half of the semester.

You are going to build something working, you will find in doing so, that the code is just one part of a much larger project.

**Due:** Wed Feb 4th at 11:59pm

### Deliverable/Assignment for Sprint1

- Make a new github project with your name somewhere in the project name; This project will hold all sprints of project1

- Write a program which will listen to a microphone and using a local AI model do speech to text on the microphone audio.

- print the audio to the command line and add it to a file
    - each run should have its own file, you can reuse the file
    - all text from a particular run much be in the file, even if the speaker pauses for a bit and then resumes talking

- Your program must have at least two functions/methods. and all code must be in functions/method.

#### Automated Tests

- Write an automated test to test your function that takes sounds and returns text in that sound.
    - Put a github actions yaml file which will
        - install all requirements on the docker container (this might be non-trivial)
        - run a linter on your code
        - run your automated test
        - Usually you will need a sound file to use for your automated test since your other option is to run speech to text and then back again, be sure that the sound file is in a format that your speech to text engine can work with.
    - your code should pass the test and pass the linting

### Hints

There are a lot of speech to text tutorials out there. Begin with one of them. (most of the ones that I found stripped this down to its smallest easiest forms, you will have to build the structure to make it testable)

For those few of you who do not have a working microphone on your laptop, I've left a few small mics in DMF363 in the radiators near the window. please use them in the room and return them to the radiator area for the next student when you leave.

For python and java users, look at https://alphacephei.com/vosk/install I found it useful

There are also third party vosk bindings for most other interesting languages in 2026: https://github.com/alphacep/vosk-api

you don't have to use this solution if you have another one, but those of you who have never done this sort of work, have a look at this solution.

**Do NOT!!!!** try to upload an entire model file to github when using the AI models for the speech recognition. Github will error out and you won't be able to easily recover unless you have a lot of experience with git squash or something similar.

## Submitting this assignment

- To Submit this assignment, push it to a private github repository for the github account whose name you sent me earlier.

- Make/invite me to be a collaborator on this project.