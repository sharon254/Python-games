# Basic games with Python. 

## BMI calculator
## Step 1
In this step,we are egtting the inputs for the height and weight from an individual.
## Step 2
In this step, we calculate the BMI using the formula BMI = weight / height **2.
 ** operator is used to calculating the power of the height.
 ## Step 3
In this step, using python if loop if BMI <15 print severely underweight.
## Step 4
In this step, using python if loop if BMI <16 print severely underweight.
## step 5
In this step, using python if loop if BMI <18.5 print underweight.
## Step 6
In this step, using python if loop if BMI  <25 print healthy.
## Step 7
In this step, using python if loop if BMI <30  print overweight.
## Step 8
In this step, using python if loop if BMI <40 print Obese Class II (Severely obese).
## Step 9
In this step, using python if loop if BMI is greater than 40 print Obese Class III (Very severely obese).

## Rock,Paper,Scissors game

## Guessing a number game

* We firt import the random module that  generate a random number.
 * Then will prompt the user to enter his name and store it to a variable named myname
  * We also prompt the user to choose the level of difficulty which will determine the number of guesses 
Constructing the while loop 
 we are taking the input from the user and storing it in the guess variable.
 However, the user input we are getting from the user is a string object in order to perform a mathematical operations,
 we first need to convert it to an integer which is done by the inbuilt int() method.
 *In the next line, we are incrementing the value of number_of_guesses variable by 1.
* Next we have 3 conditional statements.
*In the first, if statement we are comparing if the guess is less than the generated number if this statement evaluates to true, we print the corresponding Guess.
*Similarly, we are checking if the guess is greater than the generated number.
*The final if statement has the break keyword, which will terminate the loop entirely, So when the guess is equal to the generated number loop gets terminated.
*The game continues to play until the player picks the number you had originally picked or they have ran out of guesses.
