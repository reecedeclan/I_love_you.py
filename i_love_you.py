import tkinter as tk
import math

def draw_heart_step(canvas, x, y, size, color, points, index):
    if index >= len(points):
        return
    
    #Drawing the current piece
    canvas.create_line(points[index - 1], points[index], fill=color, width=2)
    canvas.update()
    
    #Setting time for when to draw next heart
    canvas.after(10, draw_heart_step, canvas, x, y, size, color, points, index + 1)

def draw_heart(canvas, center_x, center_y, size, color):
    scale = size / 15
    points = []
    for angle in range(0, 360):
        angle_rad = math.radians(angle)
        px = center_x + scale * (16 * math.sin(angle_rad) ** 3)
        py = center_y - scale * (13 * math.cos(angle_rad) - 5 * math.cos(2 * angle_rad) - 2 * math.cos(3 * angle_rad) - math.cos(4 * angle_rad))
        points.append((px, py))
    
    # Draw the heart gradually using the after method
    canvas.after(10, draw_heart_step, canvas, center_x, center_y, size, color, points, 1)

def draw_hearts(canvas, width, height, size, depth=5, color_index=0):
    if size <= 2 or depth <= 0:
        return

    #Shades of pink used
    pink_shades = [
        "#ff69b4",  #Hot Pink
        "#ff1493",  #Deep Pink
        "#ff69b4",  #Hot Pink
        "#ff1493",  #Deep Pink
        "#ff69b4"   #Hot Pink
    ]
    
    # Centering the heart in the middle of application
    center_x = width // 2
    center_y = height // 2
    
    #alternate throughout colours
    color = pink_shades[color_index % len(pink_shades)]
    draw_heart(canvas, center_x, center_y, size, color)

    #Schedule the next heart drawing with the next pink shade
    next_color_index = (color_index + 1) % len(pink_shades)
    canvas.after(500, draw_hearts, canvas, width, height, size - 15, depth - 1, next_color_index)

#Clear canvas and restart the app
def restart_animation():
    canvas.delete("all")  
    draw_hearts(canvas, width, height, 200, depth=10) 

def main():
    global canvas, width, height

    #App name in top bar
    root = tk.Tk()
    root.title("i love you")

    #Size of the canvas
    width, height = 600, 600
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    #Start drawing the hearts centered with different shades of pink
    draw_hearts(canvas, width, height, 200, depth=10)

    #Button to restart app animation
    restart_button = tk.Button(root, text="Play again", command=restart_animation)
    restart_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()