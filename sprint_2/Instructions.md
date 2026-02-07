# Project 1 Sprint 2

This agile sprint is a continuation of sprint1 found here. An instructor's solution for sprint1 will be published shortly after this assignment, at which time I will be unable to accept any late sprint1 submissions.

## Summary

In this second of several sprints which build a larger software solution you will build the AI 'skills' (a fancy way of saying functions that the AI will be allowed to use) that our voice controlled AI agent will begin to use in sprint 3.

**Due:** Fri Feb 13th

**Important:** Do all of your work in the same github project as sprint1.

## Deliverable for Sprint 2

- You will write AI 'skills' – functions that the AI will call later.
- I'm running https://github.com/jsantore/Room_booking_serve as a server
  - write a program which will have at least six functions, one as a main then one for each of the fix end points. listed in the readme.
  - I've improved the documentation considerably from the original that I forked it from, but exploration and discovering what you get will still be an important part of this project.
  - your main function should run each of your functions at least once to show that they work
    - all code should be in functions (in python only the if __name__== "__main__" part should be out of functions, Java, Go etc already enforce this
    - you will need the authentication token from the login to use any of the remaining endpoints.

- update the appropriate github actions yaml to do anything else it needs to in order to run new tests properly

- Write three automated tests
  - one test should try to login with correct credentials and get an access token
  - The second test should retrieve the available rooms - make sure you get the correct rooms
  - The third test should make a reservation, and examine the results (it should succeed) then try to make a reservation for the same room and the same time, and it should fail. Make your reservation for 15 minutes so that students don't stomp all over all the rooms.

- Make sure your automated tests run on github and pass those tests (along with the compile and linting)

- I'll send user credentials via slack or email for a user account to use for this server.
  - and the address of the running meeting scheduling server.

- Make sure to use one of the secrets approaches we talk about in class to use the server program

- Don't put any of the following on github other than using github secrets and recreating your secrets file in the ephemeral docker container.
  - the email
  - the username (if needed - I think all of the endpoints use the email)
  - the password
  - the server address and port.

## Submitting this assignment

At the due date (or since it is midnight - probably the next morning) I will repull your project from the original repository.