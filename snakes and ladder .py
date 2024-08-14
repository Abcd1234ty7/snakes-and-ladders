import tkinter as tk  # Import the tkinter library for GUI development
import random  # Import the random library to generate random numbers (for dice rolls)

# Snakes and Ladders Board
# The dictionary represents the board where keys are positions with snakes or ladders,
# and values are the new positions after encountering a snake or ladder.
board = {
    2: 38, 7: 14, 8: 31, 15: 26, 16: 6,
    21: 42, 28: 84, 36: 44, 46: 25, 49: 11,
    51: 67, 62: 19, 64: 60, 71: 91, 74: 53,
    78: 98, 87: 94, 89: 68, 92: 88, 95: 75,
    99: 80
}


class SnakesAndLaddersGame:
    def __init__(self, root):
        self.root = root  # Store the root window
        self.root.title("Snakes and Ladders")  # Set the title of the window

        # Initialize player positions
        self.player1_position = 0
        self.player2_position = 0
        self.current_player = 1  # Player 1 starts first

        # Create a label for the game title
        self.label = tk.Label(root, text="Snakes and Ladders", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Create labels to show Player 1 and Player 2's positions
        self.player1_label = tk.Label(root, text="Player 1: 0", font=("Helvetica", 14))
        self.player1_label.pack(pady=10)

        self.player2_label = tk.Label(root, text="Player 2: 0", font=("Helvetica", 14))
        self.player2_label.pack(pady=10)

        # Create a button to roll the dice
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack(pady=20)

        # Create a label to display messages
        self.message_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.message_label.pack(pady=10)

    # Function to handle dice roll and update the game state
    def roll_dice(self):
        dice_roll = random.randint(1, 6)  # Roll the dice (random number between 1 and 6)
        self.message_label.config(text=f"Player {self.current_player} rolled a {dice_roll}")

        if self.current_player == 1:
            # Update Player 1's position
            self.player1_position += dice_roll
            self.player1_position = self.check_snakes_ladders(self.player1_position)
            self.player1_label.config(text=f"Player 1: {self.player1_position}")

            # Check if Player 1 wins
            if self.check_win(self.player1_position):
                self.message_label.config(text="Player 1 wins!")
                self.roll_button.config(state=tk.DISABLED)  # Disable the roll button if the game is over
            else:
                self.current_player = 2  # Switch to Player 2

        elif self.current_player == 2:
            # Update Player 2's position
            self.player2_position += dice_roll
            self.player2_position = self.check_snakes_ladders(self.player2_position)
            self.player2_label.config(text=f"Player 2: {self.player2_position}")

            # Check if Player 2 wins
            if self.check_win(self.player2_position):
                self.message_label.config(text="Player 2 wins!")
                self.roll_button.config(state=tk.DISABLED)  # Disable the roll button if the game is over
            else:
                self.current_player = 1  # Switch to Player 1

    # Function to check for snakes or ladders
    def check_snakes_ladders(self, position):
        if position in board:
            new_position = board[position]
            # Display a message if the player encounters a ladder or a snake
            if position < new_position:
                self.message_label.config(text=f"Ladder! Climb from {position} to {new_position}")
            else:
                self.message_label.config(text=f"Snake! Slide from {position} to {new_position}")
            return new_position
        return position

    # Function to check if a player has won
    def check_win(self, position):
        return position >= 100


# Create the main window
root = tk.Tk()
# Create an instance of the game
game = SnakesAndLaddersGame(root)
# Start the main event loop
root.mainloop()
