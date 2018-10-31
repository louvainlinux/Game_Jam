# Memory Puzzle

## Rules of the game

A board is set with pair of tokens (two tokens are in the same pair if the color and the shape is the same).

At the beginning the game uncover randoms tiles to show the token under it and cover them again after a few amount of time. When all the tiles has been uncover, the showing phase is done.

During the game, the player can choose two tiles.The two tiles uncover the tokens. If both of them aren't from the same pair, the tiles cover the tokens again, if not, they don't.

The game is won when all the tokens are uncover.

## Structure

### Paramaters of the map

* FPS (frame per second)
* Widow size for the game
* Box size
* Space between boxes
* Numbers of boxes (per rows and columns)
* Color for the game
* Shapes for the tokens
* Speed of cover/uncover

### Main

* Initialisation of the map
* Showing all tokens
* Detecting the events and action -> reacting to action
  * Exiting the game
  * Pressing a tiles
* Test for the win condition
* Update the board
