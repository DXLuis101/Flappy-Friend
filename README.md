# Flappy-Friend
This is a recreated famous game called Flappy Bird. Equally to the game, the goal is to avoid obstacles as the player moves and gain a score. It took a while to implement all the functionality for the player to jump, the collisions on the obstacles, and update the score. The least variables to implement the game is the main menu, the icons and pictures to the game, and the personal score on the main menu.

# Here are my aspects and define functions on my script of this project:
- def init_game()
The game opens up the screen with its regular (width,height) and captioned the title "Flappy Friends".

- def create_pipes()
The obstacles, rather the pipes, define the random height of the pipes. They can be high up or lower, so the player must know how to proceed. The top pipe and lower pipe have their parameters to define how high they should be.

- def draw_game(screen, bird, pipes, score)
This is basically how the game is represented. The screen is filled with blue as the background, the player is a white square, the pipes are green, and the font is located at the upper right screen.

- def_main()
This is all the functionality for the game. It controls the FPS limit of the game, the gravity and speed of the player, the update score functionality, and the pipe randomization height.

To run this game, install pygame.

Enjoy and have fun playing this!
