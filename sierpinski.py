import turtle
import random
import time

def set_full_screen(screen):
    # Get the tkinter window associated with the turtle screen
    t_screen = screen._root

    # Set the window to full screen
    t_screen.attributes('-fullscreen', True)

def sierpinski_triangle_turtle(iterations, duration=15, size=616):
    # Set up the turtle window
    screen = turtle.Screen()
    set_full_screen(screen)  # Set the screen to full screen
    screen.title("Sierpiński Triangle")
    screen.tracer(0)  # Turn off animation for smoother updates

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()

    # Define the three vertices of the triangle
    vertices = [(0, 0), (size, 0), (size / 2, size * (3**0.5) / 2)]
    
    # Move the starting position to the center of the screen
    screen_x_offset = -size / 2
    screen_y_offset = -size / 3

    # Choose a random starting point inside the triangle
    x, y = random.uniform(0, size), random.uniform(0, size)

    # Calculate the time delay to complete within the duration
    delay = duration / iterations

    start_time = time.time()
    for _ in range(iterations):
        # Randomly select one of the three vertices
        vx, vy = random.choice(vertices)

        # Move halfway towards the chosen vertex
        x = (x + vx) / 2
        y = (y + vy) / 2

        # Move the turtle to the new position and place a dot
        pen.goto(x + screen_x_offset, y + screen_y_offset)
        pen.dot(12, "black")

        # Update the screen
        screen.update()

        # Add delay to match the desired duration
        elapsed_time = time.time() - start_time
        remaining_time = max(0, (duration - elapsed_time) / (iterations - _))
        time.sleep(remaining_time)

    screen.mainloop()  # Keep the window open

# Run the function with 5000 dots to finish in around 15 seconds
sierpinski_triangle_turtle(iterations=5000, duration=15)
