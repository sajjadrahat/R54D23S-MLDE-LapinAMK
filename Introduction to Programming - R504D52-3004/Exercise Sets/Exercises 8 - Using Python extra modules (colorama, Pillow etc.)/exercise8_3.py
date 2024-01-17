from PIL import Image, ImageDraw, ImageFont

print("Enter a number for the color \n----------------\n1 = Blue, 2 = Red, 3 = Green,\n4 = Black, 5 = Purple, 6 = White\n----------------\n ")

color_dict = { 1: (0, 0, 255), 2: (255, 0, 0), 3: (0, 255, 0), 4: (0, 0, 0), 5: (128, 0, 128), 6: (255, 255, 255), }

width, height = 500, 300
background_color = color_dict.get(int(input("Enter Background Color: \n")))
image = Image.new("RGB", (width, height), background_color)
user_text = input("Enter text to be drawn: \n")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Set the font and size
font_path = "arial.ttf"
font_size = 16
font = ImageFont.truetype(font_path, font_size)

# Set text color
text_color = color_dict.get(int(input("Enter Text Color: \n")))

# Draw the text in the lower left corner
text_position = (10, height - font_size - 10)
draw.text(text_position, user_text, font=font, fill=text_color)

triangle_color = color_dict.get(int(input("Enter Triangular Color: \n")))
triangle_points = [(250, 50), (400, 250), (100, 250)]  # Coordinates of the triangle
draw.polygon(triangle_points, fill=triangle_color)

# Draw a blue circle inside the triangle
circle_color = color_dict.get(int(input("Enter Circle Color: \n")))
circle_center = (250, 150)  # Center coordinates of the circle
circle_radius = 50
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius],
             fill=circle_color)

# Save the image with a relative path
image.save("pil_picture.png")

image.show()
