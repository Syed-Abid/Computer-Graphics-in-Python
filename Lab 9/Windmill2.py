from pyleap import *

# Set the window size
window.set_size(640, 600)

# Create the background sky
sky = Rectangle(0, 0, 640, 600, 'blueberry')

# Create text
txt = Text('Windmill Project in pyleap', 130, 540, 20, 'black')

# Create the windmill components
body = Polygon(200, 100, 240, 297, 345, 297, 383, 100, 'gray')
sun = Circle(100, 440, 35, 'yellow')
top = Triangle(240, 331, 293, 434, 345, 331, 'orange')
mid = Circle(292, 372, 20, 'red')

# Create the airplane sprite
plane = Sprite('E:\CG Python\Airplane.png', 543,437)

# Create the windmill handles
handles = []

for rotation in range(0, 360, 90):
    handle = Triangle(293, 374, 392, 460, 403, 440, 'purple')
    handle.rotation = rotation
    handle.set_anchor(292, 372)
    handles.append(handle)

def windmill(dt):
    sky.draw()
    txt.draw()
    body.draw()
    sun.draw()
    top.draw()
    mid.draw()

    # Update airplane position
    plane.x -= 1
    plane.y -= 1

    # Check if the airplane has reached the bottom left corner and reset its position
    if plane.x < 84 and plane.y > 40:
        plane.x = 543
        plane.y = 437

    # Draw the airplane
    plane.draw()

    for handle in handles:
        handle.draw()
        handle.rotation += 1

repeat(windmill)
run()
