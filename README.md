Pig Game Project
Welcome to the Pig Game Project, a simple yet engaging game built in Python where players take turns to roll a die and accumulate points. The objective is to reach a target score before the opponent. The game can be played in two modes: Player vs Player (PvP) and Player vs Computer (PvC).

Files Description
game.py: Contains the Game class, which orchestrates the flow of the game. It manages the game states, including turns, rolls, scores, and the decision-making process for both human and computer players.
score.py: Manages the scoring system of the game. It keeps track of high scores and updates them based on game outcomes.
dice.py: Includes the Dice class responsible for simulating the rolling of a die, providing random outcomes as per dice rules.
game_settings.py: Contains settings and configurations for the game, such as target scores, modes, and any other customizable settings.
intelligence.py: Implements the Intelligence class, which defines the strategy used by the computer player in PvC mode. It decides whether the computer will roll or hold based on the current state of the game.
main.py: The entry point of the project. It initiates the game, processes user input for game settings, and starts the game loop.
menu.py: Provides the user interface for the game settings, allowing players to choose the game mode, set target scores, and start the game.
player.py: Contains the Player class that represents a player in the game. It holds the player's current score, manages the accumulation of points, and resets scores as necessary.

How to Play
Clone the repository to your local machine.
Navigate to the project directory.
Run python main.py to start the game.
Follow the on-screen instructions to configure your game and begin playing.

Game Modes
Player vs Player (PvP): Two human players take turns rolling the die, deciding to "roll" or "hold" to accumulate points towards the target score.
Player vs Computer (PvC): The human player competes against the computer, which uses a predefined strategy to make decisions.
Enjoy the game, and may the best player win!
