import pgzrun  # Import the pgzrun library

alien = Actor('alien.png')  # Create an Actor instance with the image
alien.topright = 0, 10 # Set the position of the alien

WIDTH = 500
HEIGHT = alien.height + 20  # Set the height of the window based on the alien's height

def draw():
    screen.clear()  # Clear the screen
    alien.draw()  # Draw the alien on the screen

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")


pgzrun.go()  # Start the game loop
