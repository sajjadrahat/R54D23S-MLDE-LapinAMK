import functions

while True:
    user_input= int(input("Select the operation (1-3), 0 stops the application: \n"))
    if user_input==0:
        print("Thank you for using our application!")
        break
    elif user_input==1:
        width=int(input("Give box width: \n"))
        height = int(input("Give box height: \n"))
        depth = int(input("Give box depth: \n"))
        result = functions.box_volume(width, height, depth)
        print(f"Box volume: {result} m3")
    elif user_input==2:
        radius=int(input("Give ball radius: \n"))
        result = functions.ball_volume(radius)
        print(f"Ball volume: {result} m3")
    elif user_input==3:
        radius=int(input("Give pipe radius: \n"))
        length = int(input("Give pipe length: \n"))
        result = functions.pipe_volume(radius, length)
        print(f"Pipe volume: {result} m3")