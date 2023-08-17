
# Brilliant Blackjack

Brilliant Blackjack is a python terminal game, which runs in a mock terminal through Heroku.

Users will play against the computer to get blackjack or as close to it as they dare. Each round will add to a total score bewtween player and computer. The aim of the game is to beat the computer.

![Responsive view of Brilliant Blackjack on large devices](documentation/brilliant-blackjack-mockup.png)

## Live Website

[Brilliant Blackjack](https://brilliant-blackjack-94e6e2e8e263.herokuapp.com/)

## Repository

[Repository Link](https://github.com/Daniel009891/brilliant-blackjack)

## UX: User Experience

### User Stories

As a user,

* I would like the game to be fun.
* I would like to be able to navigate easily through the game.
* I would like to compete against a computer.
* I would like to be able to recieve feedback on scores and cards dealt.

### Initial Concept

The initial concept was to create a fun terminal based game of blackjack, which enables users to compete against the computer, to see their scores for their hand and see the total scores of games won. 

## Features

### Existing Features

#### Landing Page

![Landing Page](documentation/brilliant-blackjack-welcome.png)

The landing page displays a welcome message to the user and asks them to enter their name before playing.

#### Enter Name

Beneath the welcome message the game asks the user to enter a name, this can be seen in the image above. 

The enter name has validation to stop the user entering a blank name and entering "computer" as a name. An error message is displayed prompting the user to try again. 

[Enter Name](documentation/error-message-no-name.png)
[Enter Name](documentation/error-message-no-name.png)

#### Game Rules

Before starting the game, the user has the option to review the game rules or play without.

[Game Rules](documentation/brilliant-blackjack-rules-input.png)

The game rules options have validation to ensure the user only selects "Y" or "N". If the user enters anything other than that, the error message Sorry you can only select Y for (yes) or N for (no), please try again!" 

[Game Rules](documentation/error-message-invalid-selection-rules.png)
[Game Rules](documentation/error-message-no-selection-rules.png)

When the user enters the correct input of "Y" a display of the rules is brought up for the user to read.
[Game Rules](documentation/brilliant-blackjack-rules-heading.png)
[Game Rules](documentation/brilliant-blackjack-rules.png)

If the user decides not to read the rules the game will begin.

#### Main Game

After the user has selected to start the game, the game will begin to shuffle the deck of cards, and deal out cards to the computer and user. The user will be informed of their cards and score and will be given the option to stick or twist. Again this has validation so the users can only select "S" or "T".

[Game Play](documentation/brilliant-blackjack-game-play.png)



### Features Left to Implement

* I would like to add a countdown timer for each question, this would create a more competetive quiz as users would need to think fast before selecting an answer.

* I would also like to add a create account feature, so users can store their scores against theirr login details.

## Technologies Used

* The website was created with [HTML](https://html.spec.whatwg.org/).
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) was used to add styling to the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to create the quiz functionality.
* [Codeanywhere](https://codeanywhere.com/) was used to create, edit and preview the codes.
* [Git](https://git-scm.com/) was used for version control and tracked changes in the codes.
* [GitHub](https://github.com/) was used to store the codes and deploy the website.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) were used extensively while adjusting the objects in the website for different screen sizes.
* The website was fully validated using [W3C HTML Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
* [Am I responsive?](https://ui.dev/amiresponsive) was used to generate the mockup image showing the website on various screen sizes.
* The fonts used in the website are imported from [Google Fonts](https://fonts.google.com/).
* [Shutterstock](https://www.shutterstock.com/) was used to source royalty free images.

## Testing

### Code Validation

The website was fully validated to ensure there were no syntax errors. The official [W3C HTML Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) were used for the validation and no errors were found. [JSHint](https://jshint.com/) was used to ensure no errors were found within the JavaScript. 15 warnings were detected but these relate to some syntaxes only being available in ES6. 

### Resolved Bugs

* 

### Unresolved Bug

* 

## Deployment

### Version Control

The version control was maintained using git within Visual Studio Code to push code to the main repository.

 * From the VS Code terminal type `"git add ."`, to make changes and/or updates to the files.

 * Type `"git commit -m (insert a short descriptive text)"`, which commits the changes and updates the files.

 * Use the `"git push"` command, which pushes the committed changes to the main repository. 

 ### Page Deployment
 The app was deployed to Heroku CLI. The steps to deploy are as follows:

 * After creating an account and logging in, click `"New"` to create a new app from the dashboard.
 * Create a unique name for the app and select my region; press `"Create app"`.
 * Go to `"Settings"` and navigate to `Config Vars`.
 * Add Config Vars. 
   * For this app was only used: `KEY` = `PORT` : `VALUE` = `8000`.
 * Add buildpacks `Python` and `NodeJS` - in this order.
 * Click the `Deploy Branch`.
 * Scroll Down to Deployment Method and select GitHub.
 * Select the repository to be deployed and connect to Heroku.
 * Scroll down to deploy: 
    * `Option 1` is selecting Automatic deploys (Will Update Automatically with every "git push"). This was chosen for this project.

* Live deployment [Brilliant Blackjack] (https://brilliant-blackjack-94e6e2e8e263.herokuapp.com/)


## Credits

### Contents

### Codes

* The question layout and function ideas were inspired by the [stackoverflow.com](https://stackoverflow.com/questions/75996907/trying-to-implement-a-scoring-system-to-a-web-based-trivia-game) forum submission.


## Acknowledgements

This website was created as a portfolio 1 project for the Full Stack Software Development course at [Code Institute](https://codeinstitute.net/ie/). I would like to thank my mentor, [Harry Dhillon](https://github.com/Harry-Leepz), for the guidance and encouragement given throughout the project. Following his valuable feedback and advice, the website has been refined to be more intuitive and it has improved the overall user experience.

I would also like to thank the slack community at Code institute, the issues with functio