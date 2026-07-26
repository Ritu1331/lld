# lld

# 📄 Google Docs - Document Editor (Low-Level Design)

## 📌 Overview

This project is a simplified **Google Docs** implementation designed to demonstrate **Object-Oriented Programming (OOP)** and **Low-Level Design (LLD)** concepts.

The editor allows users to:
- Add text
- Add images
- Insert new lines
- Insert tab spaces
- Render the document
- Save the document to a file

Instead of storing everything as plain strings, each document component is represented as a separate object, making the design **extensible**, **maintainable**, and **scalable**.

---

## 🏗️ Architecture

```text
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
```

---

# 📂 Class Responsibilities

## 1. DocumentElement (Abstract Class)
**Purpose:** Serves as the base class for all document elements.

**Responsibilities:**
- Declares the `render()` method.
- Ensures every document element knows how to render itself.

---

## 2. TextElement
**Purpose:** Represents plain text in the document.

**Responsibilities:**
- Stores a text string.
- `render()` returns the stored text.

---

## 3. ImageElement
**Purpose:** Represents an image in the document.

**Responsibilities:**
- Stores an image path.
- `render()` returns the formatted image representation.

**Example Output:**
```text
[Image: picture.jpg]
```

---

## 4. NewLineElement
**Purpose:** Represents a line break.

**Responsibilities:**
- `render()` returns a newline character (`\n`).

---

## 5. TabSpaceElement
**Purpose:** Represents a tab space.

**Responsibilities:**
- `render()` returns a tab character (`\t`).

---

## 6. Document
**Purpose:** Represents the complete document.

**Responsibilities:**
- Stores all document elements.
- Renders the complete document by combining the output of every element.

---

## 7. Persistence (Abstract Class)
**Purpose:** Defines different ways to save a document.

**Responsibilities:**
- Declares the `save()` method.
- Acts as a common interface for all storage implementations.

---

## 8. FileStorage
**Purpose:** Saves the document to a text file.

**Responsibilities:**
- Implements the `Persistence` interface.
- Saves the rendered document into `document.txt`.

---

## 9. DBStorage
**Purpose:** Placeholder for database storage.

**Responsibilities:**
- Can be extended to save the document into databases such as MySQL, PostgreSQL, or MongoDB.

---

## 10. DocumentEditor
**Purpose:** Acts as the controller between the user, document, and storage.

**Responsibilities:**
- Add text
- Add images
- Add new lines
- Add tab spaces
- Render the document
- Save the document

---

# 🔄 Program Flow

```text
User
 │
 ▼
DocumentEditor
 │
 ├── addText()
 ├── addImage()
 ├── addNewLine()
 ├── addTabSpace()
 │
 ▼
Document
 │
Stores DocumentElement objects
 │
 ▼
render()
 │
 ▼
Combines all rendered elements
 │
 ▼
Final Rendered Document
 │
 ▼
Persistence
 │
 ▼
FileStorage / DBStorage
```

---

# 🧠 OOP Concepts Used

| Concept | Implementation |
|----------|----------------|
| **Abstraction** | `DocumentElement`, `Persistence` |
| **Inheritance** | `TextElement`, `ImageElement`, `NewLineElement`, and `TabSpaceElement` inherit from `DocumentElement` |
| **Polymorphism** | Each document element implements its own `render()` method |
| **Composition** | `Document` contains multiple `DocumentElement` objects |
| **Dependency Injection** | `DocumentEditor` receives `Document` and `Persistence` through its constructor |

---

# 📌 SOLID Principles Followed

### ✅ Single Responsibility Principle (SRP)
Each class has a single responsibility.

### ✅ Open/Closed Principle (OCP)
New document elements (e.g., `VideoElement`, `TableElement`) can be added without modifying existing classes.

### ✅ Liskov Substitution Principle (LSP)
Every subclass of `DocumentElement` can be used wherever a `DocumentElement` is expected.

### ✅ Interface Segregation Principle (ISP)
Small and focused abstractions are provided through `render()` and `save()`.

### ✅ Dependency Inversion Principle (DIP)
`DocumentEditor` depends on the abstraction (`Persistence`) instead of a concrete implementation (`FileStorage`).

---

# ✅ Features

- Add text to the document
- Insert images
- Add new lines
- Insert tab spaces
- Render the complete document
- Save the document to a file
- Easily extendable with new document elements (e.g., Video, Table, Hyperlink)
- Supports multiple storage mechanisms (File, Database, Cloud, etc.)

---

# 📄 Sample Output

```text
Hello, world!
This is a real-world document editor example.
    Indented text after a tab space.
[Image: picture.jpg]
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Low-Level Design (LLD) fundamentals
- Abstraction
- Inheritance
- Polymorphism
- Composition
- Dependency Injection
- SOLID Principles
- Separation of Concerns
- Extensible and maintainable software architecture
- Real-world modelling of a document editor similar to Google Docs