# Pig Game Project
Welcome to the Pig Game Project, a simple yet engaging game built in Python where players take turns to roll a die and accumulate points. The objective is to reach a target score before the opponent. The game can be played in two modes: Player vs Player (PvP) and Player vs Computer (PvC).

# Table of Contents
- Features
- Installation
- Run game
- Game Description
- Run Test and Analysis
- Get docs
- Bug reports
- Contributing


## Features
- Colorful design: The game interface is colorful, even in the terminal environment.
- Two Game Modes: Enjoy both Player vs Player (PvP) and Player vs Computer (PvC) modes.
- Adjustable Difficulty: Tailor the game to your preference by adjusting the probability of the dice and the computer's strategy in PvC mode.
- Quit Anytime: Players have the freedom to quit the game at any point during gameplay.
- Game Rules: Access and review the game rules from the menu.
- Score record: Player can check their recoord in a ranking list.
- Searchable Records: Easily find and access player records by searching for their name.
- Name Customization: Personalize your gaming experience by setting or changing your player name.


## Installation
Before getting started, ensure that you have Git Bash or Cygwin installed on your system. Additionally, you'll need to have Make installed to execute the provided commands seamlessly.

If you haven't installed Git Bash or Cygwin yet, please refer to the course website for detailed instructions on how to do so. You can find the installation guide at the course page: [Lab Environment and Tools](https://hkr.instructure.com/courses/6796/pages/lab-environment-and-tools?module_item_id=352239)

After completing the requirements outlined above, proceed with the following steps:
1. Clone the repository: git clone https://github.com/ysw-michaelia/pig-dice-game
2. Navigate to the project directory: Open Git Bash or Cygwin and navigate to the directory where you cloned the repository.
3. Create a virtual environment (recommended): In Git Bash or Cygwin, execute the command "make venv"(No double quotes). This command will set up a virtual environment for the project, which we would use in the whole Readme. 
4. Install all the packages: Once the virtual environment is created, install all the required packages by running "make install". This command will install all the necessary dependencies for the project.
5. Check the installed packages: You can verify the installed packages by typing the following command in Git Bash "make installed". This will display a list of installed packages.


## Run Game
You have two options for running the game:

### Option 1: Using gitbash/Cygwin
1. Open Git Bash or Cygwin.
2. Navigate to the root directory of the game (where you cloned the repository).
3. Run the following command: make run

### Option 2: Using Command Prompt (recommended)
The reason for recommending the Command Prompt is that it's the only terminal environment that can accurately display the color scheme designed for the game.

1. Open Command Prompt.
2. Navigate to the root directory of the game (where you cloned the repository).
3. Activate the virtual environment by executing the following commands: cd .venv\Scripts
                                                                        activate
4. Navigate back to the root directory of the game by using: cd ..\..
5. Navigate to the pigGame directory by executing: cd pigGame
6. Finally, run the game by typing: python main.py


## Game Description
Upon running the game, you will be presented with a main menu where you can choose various options:

### Start game: 
1. Initiate a new game by selecting the mode (PvP or PvC). In PvC mode, you can adjust the difficulty settings,the probability of dice and strategy.
2. Players can personalize their names.
3. Cheating is possible in the game, granting a direct gain of 1000 points.
4. At any point during gameplay, players have the option to quit.

### Game rules:
- Review the rules governing the Pig Dice Game:
    Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold": If the player rolls a 1, they score nothing and it becomes the next player's turn. If the player rolls any other number, it is added to their turn total and the player's turn continues.

    If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn. The first player to score 100 or more points wins.

    If the mode selected is PvC, players must specify the difficulty level, including the probability of dice
    and the computer's strategy. These parameters are exclusive to computer players:
    - Probability of dice: Ranges from 1 to 5. A value of 1 indicates a standard dice roll rate. As the value increases, the computer's chances of obtaining higher points also increase.

    - Strategy: Also ranging from 1 to 5. A value of 1 represents a conservative strategy, where the computer plays it safe. Higher values reflect a more adventurous approach, with the computer taking greater risks.

### Scores: 
- View the high scores for both PvP and PvC modes.
- Search for player records.
- Modify a player's name.

### Exit:
- Quit the game.

Follow the prompts on the screen to navigate the menu and enjoy the game.


## Run Test and Anlysis

### Test and Coverage
To run tests and check coverage, follow these steps:
1. Navigate to the project directory: Open Git Bash or Cygwin and navigate to the directory where you cloned the repository.
2. To run tests only, type: make test.
3. To check coverage only, type: make coverage.

### Pylint and Flake8
To run pylint and flake8 for code analysis, follow these steps:
1. Navigate to the project directory: Open Git Bash or Cygwin and navigate to the directory where you cloned the repository.
2. To run pylint only, type: make pylint.
3. To run flake8 only, type: make flake8.
4. To run both pylint and flake8, type: make lint.


## Get docs

### Generate documentation from the code
To generate documentation from the code, follow these steps:
1. Navigate to the project directory: Open Git Bash or Cygwin and navigate to the directory where you cloned the repository.
2. To generate documentation using pdoc, type: make pdoc.
3. The generated documentation will be available in the doc/api directory.
4. Additionally, you can view the documentation directly in your web browser by typing: make pydoc

### Generate UML
1. Navigate to the project directory: Open Git Bash or Cygwin and navigate to the directory where you cloned the repository.
2. To generate UML, type: make pyreverse
3. The generated documentation will be available in the doc/uml directory.


## Bug reports
If you encounter any bugs, please report them to us by submitting an issue on our [Github repository](https://github.com/ysw-michaelia/pig-dice-game).


## Contributing
At this point the project is not open for community contribution. If that changes this section will be updated accordingly.
