# Get number of pyramids and the height from the user as a comma-separated input

numCheck = False
while not numCheck:
    try:
        input_str = input("Input Level tree: ")
        num_pyramids, height= map(int, input_str.split(','))
        numCheck = True
    except:
        print("Please put number ex. 1,2")

for i in range(num_pyramids):
    # Iterate over each row of the pyramid
    for j in range(height):
        # Print the spaces before the asterisks
        print(" " * (height - j - 1), end="")
        # Print the asterisks for this row
        print("*" * (2 * j + 1))

