# AI Code that will run on the image to generate a description
global descriptioned
# Microsoft code here
def generate_description():
    print("Classifying image")
    global descriptioneds
    descriptioned = True


# returns if image has a description ready
def image_decriptioned():
    return descriptioned

def reset():
    global descriptioned
    descriptioned = False