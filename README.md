
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

* I would like the website to be visually appealing.
* I would like to be able to navigate easily through the website.
* I would like to test my knowledge with an interactive quiz.
* I would like to be able to recieve feedback on correct and incorrect answers.

### Initial Concept

The initial concept was to create a website that features a simple interactive quiz for the purpose of testing existing electrical knowledge. 

### Website Structure

Bright Spark consists of two HTML pages. The layout of the website is simple and consistent. A start button on the first html page makes it simple and easy for the user to start the quiz.

The second page consists of the Javascript quiz which offers feedback on correct and incorrect answers throughout with the aid of colors to denote these. Green shows a correct answer and red shows an incorrect answer.

The website is fully responsive to different screen sizes and the layout adapts and changes as the screen sizes decrease. This was found to be the best option to keep a clear and concise website. Headings and buttons change size as the screen sizes get smaller, so as to not disform the layout. 

### Imagery

The background image has been chosen to highight the spark element of the title and allows a good contrast for headings and buttons.

## Features

### Existing Features

#### Start button and h1 element

Featured on the first HTML page, the start button allows the user to be linked to the start of the quiz, the h1 element shows the user the name of the website.

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

### Brower Compatibility

Appearance, functionality and responsiveness of the website were tested with the following browsers:

* Google Chrome
* Safari
* Microsoft Edge

As part of this testing, the following were tested and no issues were found:

* All internal links function as expected.
* All features function as expected.
* Responsiveness to different screen sizes - font sizes, margins, buttons and overall spacing.

The website was also manually tested on iPhone 12 pro, samsung galaxy tab e and HP pavillion laptop for the above. No issues were found.

### Resolved Bugs

* A bug was fixed where the questions and answers were not displayed in the quiz area, this was found to be a grammatical error in the element id for answer buttons and questions id in the script.js.

### Unresolved Bug

* Unfortunately i cannot get the favicon icon working, so this is an unresolved bug.

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

### Media

* Images used were sourced from [shutterstock.com](https://www.shutterstock.com/).

### Codes

* The question layout and function ideas were inspired by the [stackoverflow.com](https://stackoverflow.com/questions/75996907/trying-to-implement-a-scoring-system-to-a-web-based-trivia-game) forum submission.

* The container method was inspired by [linuxhint.com](https://linuxhint.com/how-to-make-html-container-box-in-html/#b1).

## Acknowledgements

This website was created as a portfolio 1 project for the Full Stack Software Development course at [Code Institute](https://codeinstitute.net/ie/). I would like to thank my mentor, [Harry Dhillon](https://github.com/Harry-Leepz), for the guidance and encouragement given throughout the project. Following his valuable feedback and advice, the website has been refined to be more intuitive and it has improved the overall user experience.

I would also like to thank the slack community at Code institute, the issues with functio