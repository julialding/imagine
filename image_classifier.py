# AI Code that will run on the image to see if it needs to be added to the database or not
generated = False
significant = False

# Microsoft code here
def classify():
    print("Classifying image")
    global generated
    generated = True

significant = True

# returns if image has been processed
def image_processed():
    return generated

# returns if image is seen as significant
def image_significant():
    return significant

def reset():
    global generated
    generated = False
    global significant
    significant = False