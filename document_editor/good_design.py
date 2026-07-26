from abc import ABC, abstractmethod


# Abstraction for document elements
class DocumentElement(ABC):

    @abstractmethod
    def render(self):
        pass


# Concrete implementation for text elements
class TextElement(DocumentElement):

    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


# Concrete implementation for image elements
class ImageElement(DocumentElement):

    def __init__(self, imagePath):
        self.imagePath = imagePath

    def render(self):
        return "[Image: " + self.imagePath + "]"


# NewLineElement represents a line break in the document.
class NewLineElement(DocumentElement):

    def render(self):
        return "\n"


# TabSpaceElement represents a tab space in the document.
class TabSpaceElement(DocumentElement):

    def render(self):
        return "\t"


# Document class responsible for holding a collection of elements
class Document:

    def __init__(self):
        self.documentElements = []

    def addElement(self, element):
        self.documentElements.append(element)

    # Renders the document by concatenating the render output of all elements.
    def render(self):
        result = ""

        for element in self.documentElements:
            result += element.render()

        return result


# Persistence abstraction
class Persistence(ABC):

    @abstractmethod
    def save(self, data):
        pass


# FileStorage implementation of Persistence
class FileStorage(Persistence):

    def save(self, data):
        try:
            with open("document.txt", "w") as outFile:
                outFile.write(data)

            print("Document saved to document.txt")

        except:
            print("Error: Unable to open file for writing.")


# Placeholder DBStorage implementation
class DBStorage(Persistence):

    def save(self, data):
        # Save to DB
        pass


# DocumentEditor class managing client interactions
class DocumentEditor:

    def __init__(self, document, storage):
        self.document = document
        self.storage = storage
        self.renderedDocument = ""

    def addText(self, text):
        self.document.addElement(TextElement(text))

    def addImage(self, imagePath):
        self.document.addElement(ImageElement(imagePath))

    # Adds a new line to the document.
    def addNewLine(self):
        self.document.addElement(NewLineElement())

    # Adds a tab space to the document.
    def addTabSpace(self):
        self.document.addElement(TabSpaceElement())

    def renderDocument(self):

        if self.renderedDocument == "":
            self.renderedDocument = self.document.render()

        return self.renderedDocument

    def saveDocument(self):
        self.storage.save(self.renderDocument())


# Client usage example
def main():

    document = Document()

    persistence = FileStorage()

    editor = DocumentEditor(document, persistence)

    # Simulate a client using the editor with common text formatting features.
    editor.addText("Hello, world!")

    editor.addNewLine()

    editor.addText("This is a real-world document editor example.")

    editor.addNewLine()

    editor.addTabSpace()

    editor.addText("Indented text after a tab space.")

    editor.addNewLine()

    editor.addImage("picture.jpg")

    # Render and display the final document.
    print(editor.renderDocument())

    editor.saveDocument()


if __name__ == "__main__":
    main()