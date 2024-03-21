# TITLE PROJECT: 8BALL PROJECT

MEMBERS:

Salvador F. Arches III - Business Analyst

Nino B. Garcia - Developer 1

Prince Ebora - Developer 2

Kristine Concordo - QA 1

Jan Yve Kyle L. Marquez - QA 2

(For Linux)
```
$ python -m venv .venv

$ source .venv/bin/activate

$ python -m pip install Django

$ cd eightBall

$ python manage.py runserver  
```

(For Windows)
```
PS> python -m venv venvW

PS> .\venvW\Scripts\activate

PS> python -m pip install Django

PS> cd eightBall

PS> python manage.py runserver  
```

# Assets:
## Images
Eight Ball Images
In our EightBall application, we feature an image of the iconic Eight Ball, symbolizing the fortune-telling aspect of the game. This image serves as the centerpiece of our interface, allowing users to click on it to ask their questions.

## Banner Images
To add visual interest to our application, we've included three banner images within the <div> element labeled links. These images are primarily decorative, featuring animated GIFs of a pony and an Eight Ball, adding a playful touch to the interface.

## Ball Active Image
Within the title bar of the "Ball Predictor" window, we display a dynamic image of an active Eight Ball. This image serves as a visual indicator associated with the title bar, providing a cohesive design element throughout the application.


# External Libraries
## 98.css
To achieve a retro aesthetic reminiscent of Windows 98, we've incorporated the 98.css library. This external CSS library offers pre-styled components that emulate the classic Windows interface, enhancing the nostalgic feel of our application.

## Vue.js
For dynamic behavior and interactivity, we've integrated Vue.js, a popular JavaScript framework. Vue.js enables us to create responsive user interfaces and handle user inputs effectively, enhancing the overall user experience of our application. Like making our ball levitating, moving up and down, and shaking.

# Fonts
## Micro 5 Font
To ensure consistency and readability across our interface, we've opted for the "Micro 5" font from Google Fonts. This font choice aligns with our design goals, providing a clean and modern look while maintaining legibility for users.

# Functionality
The EightBall app is all about having fun and seeking guidance, just like using a real Eight Ball toy! Or like playing the original one.

Asking Questions:

•	You can ask any question you want by typing it into the box labeled "Ask the 8-Ball!".

•	Simply click on the box, type in your question, and then either press the "Ask" button or click on the floating Eight Ball image.

Receiving Answers:

•	After asking your question, the app randomly picks an answer from its collection of responses.

•	You'll see the answer appear in the window titled "Ball Predictor v1.0", with a ">" symbol before it.

# Randomness of Responses:
The answers you get are totally random! It's like shaking a real Eight Ball and waiting for the answer to appear. But ours like already shaking and levitating waiting for the question.

# Response Handling:
The EightBall application provides responses to user questions based on predefined categories: "negative" and "neutral." These responses are stored in a text file named response.txt, which the application fetches asynchronously upon initialization.

# Response Categories:
Negative Responses: These responses indicate a negative outlook or outcome.
Neutral Responses: These responses are neither positive nor negative and may suggest uncertainty or varied possibilities.

# Response Structure:
Responses in the response.txt file are categorized by tags ([negative] and [neutral]) for easy identification.
Each response within a category is listed on separate lines.
