# Bubble-Dragon-Game
2D platformer game with single player and multiplayer built in C meant to be run on Intel FPGA DE1-SoC board.

# GAME DESCRIPTION:

Bubble Dragons is a 2D game where the player controls a dragon that can shoot bubbles, jump, and walk on platforms. The player cannot drop through platforms, they must walk or jump off of them. There are 2 modes where the player can choose to play, either single-player or multiplayer.

### Single-player: ###
The object of the game is to hit all 5 enemies with a bubble in the shortest amount of time without dying.
The player has 3 lives. If an enemy touches the player, they lose a life, then they become immune for a moment so the player can reposition.
The player has 8 bubbles. Running out of bubbles before all enemies are eliminated results in a loss.
The enemies can also walk and jump on platforms.

### Multiplayer: ###
The object of the game is to eliminate the enemy player. If a player gets hit with a bubble, they lose a life. Each player has 3 lives.
Each player has 8 bubbles. If both players run out of bubbles, the player with more lives left wins, if they have the same amount of lives, the result is a draw.
Getting hit with a bubble provides the player with a brief shield to allow for safe repositioning. This feature is the same as the immunity feature in single-player mode.

















## HOW TO SET UP:

If you do not have an FPGA board, go to https://cpulator.01xz.net/?sys=arm-de1soc, choose C as the language, delete the assembly code in the text editor, and paste in the entire C code in Bubble_Dragon.c

If you do have the DE1-SoC board:
1. Create a directory on your computer containing the submitted “Bubble_Dragon.c” file.
2. Open Intel FPGA Monitor Program and create a new project. Select the directory you created in Step 1 containing the “Bubble_Dragon.c” file and create a name for your project. Select the “ARM Cortex-A9” option in the “Architecture” drop-down menu before proceeding to the next page.
3. Select the “DE1-SoC Computer” option in the “Select a system” drop-down menu before proceeding to the next page.
4. Select the “C Program” option in the “Program Type:” drop-down menu before proceeding to the next page.
5. Click “Add” and select the “Bubble_Dragon.c” file
6. In the “Additional compiler flags” field, enter “-g -O1 --std=gnu11”. In the “Additional linker flags” field, enter “-lm” before proceeding to the next page.
7. Keep clicking “Next” until the “Save” option.
8. If it asks you to download the board, do it once if this is the first time starting the Intel FPGA Monitor Program.
8. In “Actions” in the top left corner, choose “Compile & Load”
10. After the project has finished compiling and loading, click the symbol with the yellow bar and green play button. It should say “Continue program execution from current instruction” when hovering over it.

## HOW TO PLAY:

In the start screen, press ‘M’ for multiplayer and the ‘ENTER’ key for single-player.

<p align = "center">
  <img width="714" alt="Start Screen" src="https://github.com/JasonT6/Bubble-Dragon-Game/assets/97322813/746221ef-a262-4af9-8e2a-27218de41b29">
  <div align="center">Figure 1. Start Screen</div>
  
</p>








### Single-player: ###

<p align = "center">
  <img width="722" alt="SinglePlayer" src="https://github.com/JasonT6/Bubble-Dragon-Game/assets/97322813/eda6e2df-d001-4c78-9e3c-325e0af88d3b">
  <div align="center">Figure 2. Single Player</div>
  
</p>
Hit all 5 enemies with a bubble in the shortest amount of time without dying.
The player controls the green dragon.
The enemies are the purple characters.
The platforms are the brown lines.
The player can only jump if they are on a platform
Controls:
To jump, press ‘i’
To move right, press ‘l’
To move left, press ‘j’
To shoot, press ‘SPACE’. 
The player can not drop through a platform, they must walk or jump off.
The top left of the screen is the timer.
On the top right of the screen are the remaining bubbles, and remaining lives. 
Upon getting hit by an enemy, the player gains a temporary shield to safely reposition.
In Figure 2, there are 2 lives remaining, and 8 bullets remaining.
Upon winning or losing, the player can press ‘r’ to return to the start menu.















### Multiplayer: ###

<p align = "center">
  <img width="722" alt="Multiplayer" src="https://github.com/JasonT6/Bubble-Dragon-Game/assets/97322813/266fcd15-5389-4615-b6a4-74be9e778c5d">
  <div align="center">Figure 3. Multiplayer</div>
  
</p>

Eliminate the enemy player. If a player gets hit with a bubble, they lose a life. Each player has 3 lives.
Player 1 controls the green dragon:
To jump, press ‘i’
To move right, press ‘l’
To move left, press ‘j’
To shoot, press ‘SPACE’.
Player 2 controls the blue dragon:
To jump, press ‘w’
To move right, press ‘d’
To move left, press ‘a’
To shoot, press ‘s’.
Both players cannot drop through platforms, they must walk or jump off.
On the top right, are Player 2’s remaining bubbles and lives, On the top left, are Player 1’s remaining bubbles and lives.
Upon getting hit by a bubble, the player gains a temporary shield to safely reposition.
Upon winning or losing or drawing, you can press ‘r’ to return to the start menu.
