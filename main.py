from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
import json
import os
from fastapi.middleware.cors import CORSMiddleware

class Book(BaseModel):
    title: str = Field(...,min_length=3, max_length=100)
    author: str = Field(...,min_length=3, max_length=100)
    publisher: str = Field(...,min_length=3, max_length=100)
    image_url: str


#class QueryParams(BaseModel):
#    q: str = Field(min_length=3, max_length=100)
#    page: int = 1
#    size: int = 3 # for limiting query params
# def search_books(q: QueryParams = depends())

if os.path.exists("books.json"):
    with open("books.json") as file:
        books = json.load(file)
else:
    books = [
        {"title":"Clean Code","author":"Robert C. Martin","publisher":"Prentice Hall","image_url":"https://covers.openlibrary.org/b/isbn/9780132350884-L.jpg"},
        {"title":"The Pragmatic Programmer","author":"Andrew Hunt","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201616224-L.jpg"},
        {"title":"Introduction to Algorithms","author":"Thomas H. Cormen","publisher":"MIT Press","image_url":"https://covers.openlibrary.org/b/isbn/9780262033848-L.jpg"},
        {"title":"Design Patterns","author":"Erich Gamma","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201633610-L.jpg"},
        {"title":"Refactoring","author":"Martin Fowler","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201485677-L.jpg"},
        {"title":"You Don't Know JS","author":"Kyle Simpson","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491904244-L.jpg"},
        {"title":"Eloquent JavaScript","author":"Marijn Haverbeke","publisher":"No Starch Press","image_url":"https://covers.openlibrary.org/b/isbn/9781593279509-L.jpg"},
        {"title":"Python Crash Course","author":"Eric Matthes","publisher":"No Starch Press","image_url":"https://covers.openlibrary.org/b/isbn/9781593276034-L.jpg"},
        {"title":"Automate the Boring Stuff with Python","author":"Al Sweigart","publisher":"No Starch Press","image_url":"https://covers.openlibrary.org/b/isbn/9781593275990-L.jpg"},
        {"title":"Fluent Python","author":"Luciano Ramalho","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491946008-L.jpg"},
        {"title":"Learning Python","author":"Mark Lutz","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781449355739-L.jpg"},
        {"title":"Effective Java","author":"Joshua Bloch","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780134685991-L.jpg"},
        {"title":"Java Concurrency in Practice","author":"Brian Goetz","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780321349606-L.jpg"},
        {"title":"Head First Design Patterns","author":"Eric Freeman","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9780596007126-L.jpg"},
        {"title":"Head First Java","author":"Kathy Sierra","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9780596009205-L.jpg"},
        {"title":"Grokking Algorithms","author":"Aditya Bhargava","publisher":"Manning","image_url":"https://covers.openlibrary.org/b/isbn/9781617292231-L.jpg"},
        {"title":"Deep Learning","author":"Ian Goodfellow","publisher":"MIT Press","image_url":"https://covers.openlibrary.org/b/isbn/9780262035613-L.jpg"},
        {"title":"Hands-On Machine Learning with Scikit-Learn & TensorFlow","author":"Aurelien Geron","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491962299-L.jpg"},
        {"title":"Pattern Recognition and Machine Learning","author":"Christopher Bishop","publisher":"Springer","image_url":"https://covers.openlibrary.org/b/isbn/9780387310732-L.jpg"},
        {"title":"Artificial Intelligence: A Modern Approach","author":"Stuart Russell","publisher":"Pearson","image_url":"https://covers.openlibrary.org/b/isbn/9780136042594-L.jpg"},
        {"title":"Computer Networking: A Top-Down Approach","author":"James Kurose","publisher":"Pearson","image_url":"https://covers.openlibrary.org/b/isbn/9780133594140-L.jpg"},
        {"title":"Operating System Concepts","author":"Abraham Silberschatz","publisher":"Wiley","image_url":"https://covers.openlibrary.org/b/isbn/9781118063330-L.jpg"},
        {"title":"Modern Operating Systems","author":"Andrew S. Tanenbaum","publisher":"Pearson","image_url":"https://covers.openlibrary.org/b/isbn/9780133591620-L.jpg"},
        {"title":"Computer Organization and Design","author":"David Patterson","publisher":"Morgan Kaufmann","image_url":"https://covers.openlibrary.org/b/isbn/9780124077263-L.jpg"},
        {"title":"Clean Architecture","author":"Robert C. Martin","publisher":"Prentice Hall","image_url":"https://covers.openlibrary.org/b/isbn/9780134494166-L.jpg"},
        {"title":"Domain-Driven Design","author":"Eric Evans","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780321125217-L.jpg"},
        {"title":"Building Microservices","author":"Sam Newman","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491950357-L.jpg"},
        {"title":"Site Reliability Engineering","author":"Betsy Beyer","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491929124-L.jpg"},
        {"title":"Docker Deep Dive","author":"Nigel Poulton","publisher":"Independently published","image_url":"https://covers.openlibrary.org/b/isbn/9781521822807-L.jpg"},
        {"title":"Kubernetes Up and Running","author":"Kelsey Hightower","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781491935671-L.jpg"},
        {"title":"Linux Command Line","author":"William Shotts","publisher":"No Starch Press","image_url":"https://covers.openlibrary.org/b/isbn/9781593273897-L.jpg"},
        {"title":"How Linux Works","author":"Brian Ward","publisher":"No Starch Press","image_url":"https://covers.openlibrary.org/b/isbn/9781593275679-L.jpg"},
        {"title":"The Art of Computer Programming","author":"Donald Knuth","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201896831-L.jpg"},
        {"title":"Code Complete","author":"Steve McConnell","publisher":"Microsoft Press","image_url":"https://covers.openlibrary.org/b/isbn/9780735619678-L.jpg"},
        {"title":"The Mythical Man-Month","author":"Frederick P. Brooks Jr.","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201835953-L.jpg"},
        {"title":"Working Effectively with Legacy Code","author":"Michael Feathers","publisher":"Prentice Hall","image_url":"https://covers.openlibrary.org/b/isbn/9780131177055-L.jpg"},
        {"title":"Programming Pearls","author":"Jon Bentley","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780201657883-L.jpg"},
        {"title":"Structure and Interpretation of Computer Programs","author":"Harold Abelson","publisher":"MIT Press","image_url":"https://covers.openlibrary.org/b/isbn/9780262510875-L.jpg"},
        {"title":"Compilers: Principles, Techniques, and Tools","author":"Alfred Aho","publisher":"Pearson","image_url":"https://covers.openlibrary.org/b/isbn/9780321486813-L.jpg"},
        {"title":"Computer Graphics: Principles and Practice","author":"John F. Hughes","publisher":"Addison-Wesley","image_url":"https://covers.openlibrary.org/b/isbn/9780321399526-L.jpg"},
        {"title":"Real-Time Rendering","author":"Tomas Akenine-Moller","publisher":"A K Peters","image_url":"https://covers.openlibrary.org/b/isbn/9781568814247-L.jpg"},
        {"title":"Game Engine Architecture","author":"Jason Gregory","publisher":"CRC Press","image_url":"https://covers.openlibrary.org/b/isbn/9781138035454-L.jpg"},
        {"title":"AI for Games","author":"Ian Millington","publisher":"CRC Press","image_url":"https://covers.openlibrary.org/b/isbn/9780123747310-L.jpg"},
        {"title":"Unity in Action","author":"Joe Hocking","publisher":"Manning","image_url":"https://covers.openlibrary.org/b/isbn/9781617294969-L.jpg"},
        {"title":"Learning React","author":"Alex Banks","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9781492051725-L.jpg"},
        {"title":"Fullstack Vue","author":"Hassan Djirdeh","publisher":"Fullstack.io","image_url":"https://covers.openlibrary.org/b/isbn/9780991344628-L.jpg"},
        {"title":"HTML and CSS: Design and Build Websites","author":"Jon Duckett","publisher":"Wiley","image_url":"https://covers.openlibrary.org/b/isbn/9781118008188-L.jpg"},
        {"title":"JavaScript: The Good Parts","author":"Douglas Crockford","publisher":"O'Reilly Media","image_url":"https://covers.openlibrary.org/b/isbn/9780596517748-L.jpg"},
        {"title":"Secrets of the JavaScript Ninja","author":"John Resig","publisher":"Manning","image_url":"https://covers.openlibrary.org/b/isbn/9781617292859-L.jpg"}
    ]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create")
def add_book(book: Book):
    books.append(book.model_dump())
    #in order to save new added books permanently:
    with open ("books.json", "w") as file:
        json.dump(books, file)
    return{ "message":"New book added succesfully!", "New Book":book }


@app.get("/search")
def search_books(q: str = Query(...,min_length=3, max_length=100), page: int = 1, size: int = 3):
    filtered_books = []
    for book in books:
        if (q.lower() in book["title"].lower() or q.lower() in book["author"].lower() or q.lower() in book["publisher"].lower()):
            filtered_books.append(book)
        
    start = (page - 1) * size
    end = start + size
    pagination = filtered_books[start:end]

    return{ 
        "message":"Searching was done succesfuly!",
        "Total Results": len(filtered_books),
        "page": page,
        "size":size,
        "Results":pagination
     }
