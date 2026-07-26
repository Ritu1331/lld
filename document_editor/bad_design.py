class DocumentEditor:

    def __init__(self):
        self.documentElements = []
        self.renderedDocument = ""

    # Adds text as a plain string
    def addText(self, text):
        self.documentElements.append(text)

    # Adds an image represented by its file path
    def addImage(self, imagePath):
        self.documentElements.append(imagePath)

    # Renders the document by checking the type of each element at runtime
    def renderDocument(self):
        if self.renderedDocument == "":
            result = ""

            for element in self.documentElements:

                if len(element) > 4 and (
                    element[-4:] == ".jpg" or
                    element[-4:] == ".png"
                ):
                    result += "[Image: " + element + "]\n"

                else:
                    result += element + "\n"

            self.renderedDocument = result

        return self.renderedDocument

    def saveToFile(self):
        try:
            file = open("document.txt", "w")
            file.write(self.renderDocument())
            file.close()
            print("Document saved to document.txt")
        except:
            print("Error: Unable to open file for writing.")


editor = DocumentEditor()

editor.addText("Hello, world!")
editor.addImage("picture.jpg")
editor.addText("This is a document editor.")

print(editor.renderDocument())

editor.saveToFile()