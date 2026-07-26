# lld

This project is a simplified Google Docs implementation designed to demonstrate Object-Oriented Programming (OOP) and Low-Level Design (LLD) concepts.

The editor allows users to:

Add text
Add images
Insert new lines
Insert tab spaces
Render the document
Save the document to a file

Instead of storing everything as plain strings, each document component is represented as a separate object, making the design extensible and maintainable.

🏗️ Architecture
                    User
                      │
                      ▼
              DocumentEditor
               /           \
              ▼             ▼
        Document      Persistence
             │             │
             ▼             ▼
     ----------------   FileStorage
     │   │   │   │      DBStorage
     ▼   ▼   ▼   ▼
   Text Image NewLine TabSpace
📂 Classes
1. DocumentElement (Abstract Class)
Base class for all document elements.
Declares the render() method.
Ensures every document element knows how to render itself.
2. TextElement
Represents plain text.
Stores a text string.
render() returns the stored text.
3. ImageElement
Represents an image.
Stores an image path.
render() returns [Image: imagePath].
4. NewLineElement
Represents a line break.
render() returns \n.
5. TabSpaceElement
Represents a tab space.
render() returns \t.
6. Document
Stores all document elements.
Responsible for rendering the complete document by combining the output of each element.
7. Persistence (Abstract Class)
Defines the save() method.
Represents different storage mechanisms.
8. FileStorage
Implements Persistence.
Saves the rendered document into document.txt.
9. DBStorage
Placeholder for future database storage.
Can be extended to save documents in a database.
10. DocumentEditor

Acts as the controller of the application.

Responsibilities:

Add document elements
Render the document
Save the document
🔄 Program Flow
User
   │
   ▼
DocumentEditor
   │
   ├── addText()
   ├── addImage()
   ├── addNewLine()
   ├── addTabSpace()
   ▼
Document
   │
Stores DocumentElement objects
   ▼
render()
   ▼
Combines all rendered elements
   ▼
Final Document
   ▼
Persistence
   ▼
FileStorage / DBStorage
🧠 OOP Concepts Used
Concept	Implementation
Abstraction	DocumentElement, Persistence
Inheritance	TextElement, ImageElement, NewLineElement, TabSpaceElement inherit from DocumentElement
Polymorphism	Each element implements its own render() method
Composition	Document contains multiple DocumentElement objects
Dependency Injection	DocumentEditor receives Document and Persistence through its constructor
📌 SOLID Principles
SRP (Single Responsibility): Each class has one responsibility.
OCP (Open/Closed): New document elements can be added without modifying existing classes.
LSP (Liskov Substitution): Any subclass of DocumentElement can replace the base class.
ISP (Interface Segregation): Small, focused abstractions (render() and save()).
DIP (Dependency Inversion): DocumentEditor depends on the Persistence abstraction rather than FileStorage.
✅ Features
Add text
Add images
Add new lines
Add tab spaces
Render the document
Save to a file
Easily extensible for new document elements (e.g., VideoElement, TableElement) and new storage types (e.g., Cloud, Database).
📄 Sample Output
Hello, world!
This is a real-world document editor example.
    Indented text after a tab space.
[Image: picture.jpg]
🎯 Learning Outcomes

This project demonstrates:

Object-Oriented Design
Low-Level Design fundamentals
Abstraction and Polymorphism
Separation of Concerns
Extensible architecture following SOLID principles
Real-world modelling of a document editor similar to Google Docs