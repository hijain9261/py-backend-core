## Object Oriented Programming

Why ? Reusability, Scalability, Readability of CODE

It has two important building blocks: Just 2 Class and Object! **Class** - It is a bundle which holds related functions and variables. It prepares a prototype for every object. (e.g. Car) **Object** - it has attributes (e.g. color, price )and features (e.g. mileage, peak speed) **Why Constructors?** - For dynamic use cases, they allow to set objects initial state and allocate memory at runtime.

**self** - It is the specific instance of the class that is currently calling the method. It is being used to access and manipulate that individual object's attribute.

**Difference Between Function and Method?** Function - Independent Block of Code Method - A function that is owned by a class

#### **The Four Pillars of OOPS**

1. **Encapsulation:** The Practice of bundling data and methods into a single unit and restricting direct access from outside. Access Modifiers are used to secure non-Accessible part inside the Class. There are three types of Access Modifiers - **Public, Private, Protected** ==Python doesn't have any of this rather it completely relies on the naming conventions.== So, the conventions are:
    
    <img width="694" height="375" alt="Image" src="https://github.com/user-attachments/assets/0ea6ea6e-e870-499b-86d7-fbd99f1d5123" />
    
    **Types of Methods** <table style="margin-left: 60px; text-align: center; vertical-align: middle;"> <tr style="text-align: center; vertical-align: middle;"> <th>Method Type</th> <th>First Parameter</th> <th>Decorator Required</th> <th>Access Level</th> <th>Best For?</th> </tr> <tr style="text-align: center; vertical-align: middle;"> <td>Instance Method</td> <td>self</td> <td>None</td> <td>Both Object and Class data</td> <td>Getter or setter for Objects. When you need to change or read information unique to a specific object.</td> </tr> <tr style="text-align: center; vertical-align: middle;"> <td>Class Method</td> <td>cls</td> <td>@classmethod</td> <td>Class data entry</td> <td>to manage global class variables or build custom object creators</td> </tr> <tr style="text-align: center; vertical-align: middle;"> <td>Static Method</td> <td>None</td> <td>@staticmethod</td> <td>No data entry</td> <td>Isolated utility function, just as a logic tool without accessing any object</td> </tr> </table>
    
    **Types of variables:**
    
    - **Class variables** - They are shared by **everyone**. They belong to the blueprint. Change it once, and every single object made from that blueprint sees the update.
    - **Instance variables** - They are private to **each object**. They belong to the individual. Change one, and only that specific object changes.
2. **Inheritance**: It allows a new class to adopt the attributes and methods of an existing class. The existing class is called the Parent class and the new class is called the child class. Usage - Writing common logic once and can be reused by multiple child classes. Using **super()** function.
    
3. **Polymorphism**: It allows objects of different classes to be treated as instances of a common parent class. It enables a single method or function to behave differently depending on the specific object calling it, usually achieved through method overriding or method overloading.
    
    **Method Overriding** - it allows a subclass to provide an implementation of a method which is already defined in its parent class. The priority depends on the type of object being called.
    
    **Method Overloading** - it allows the name of the function to be exactly same inside same class but the distinction point would be the number of arguments.
    
4. **Data Abstraction:** It is the process of hiding complex details, while exposing only the essential features of the data. Abstract Classes: Those classes which cannot be instantiated directly and act as a template. It acts as a contract for subclasses.
    
    Python actually enforces this strictly using the `abc` module, instead of just leaving it as a "convention". You inherit from `ABC` and mark the methods with `@abstractmethod`. If a child class forgets to implement that method, Python won't even let you create the object - it throws an error right away.
    
    ```python
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    
    class Circle(Shape):
        def area(self):
            return 3.14 * self.radius ** 2
    ```
    
    Try `Shape()` directly → instant `TypeError`. That's the contract actually being enforced at runtime, not just on paper.

## Decorators

It is a design pattern which is used to modify or extend the behavior of method, function or class without changing its source code. It extends the capability of the method such that it can do something more.

Decorators are simply the extra nested function implementation which need to be added to method, func, class.

Useful decorators:-

1. _**@functools.tru_cache**_ - Stores past outputs in memory (RAM). If the function is called with matching parameters again, it bypasses execution entirely and returns the cached result instantly.
2. _**@property**_ - Turns a method into a read-only variable attribute. Protects critical data from accidental corruption from outside scripts.
3. _**@staticmethod**_ - creates a class method that required zero knowledge of the object instance or class state.

## Multi-Threading

#### Process vs. Thread

- **Process:** An isolated execution environment spawned by the OS. A process acts like an independent factory. It has its own dedicated memory space (RAM) that other processes cannot touch. For Every installed Application, OS provides a specific Memory part which handle's all of its process.
- **Thread:** A lightweight worker unit _inside_ that process factory. A single process can contain thousands of threads. Crucially, **all threads inside a process share the exact same RAM space.**

#### How the CPU Executes Workers

A physical CPU core can only execute **one instruction stream at a time**.

- **True Parallelism:** If you have an 8-core CPU, the OS can place 8 completely separate execution paths onto those 8 physical cores, running them at the exact same millisecond.
- **Concurrency (The Illusion of Parallelism):** If you have 50 threads running on a single CPU core, the OS rapidly switches between them billions of times a second (Context Switching). It happens so fast it _looks_ simultaneous to humans, but the workers are actually taking turns.

#### **What is the GIL?**

In Python (specifically CPython), there is a master lock called the **GIL (Global Interpreter Lock)**. The GIL strictly dictates that **only one thread can control the Python interpreter and execute Python bytecode at any given microsecond.**

##### Why does Python have this restriction?

Because Python threads share memory, if two threads try to update the reference count of the exact same variable at the exact same time, memory gets corrupted or leaks. To keep Python completely stable and thread-safe, the creator implemented the GIL.

#### How do other languages bypass this?

Languages like **Java, C++, and Rust do not have a GIL**.

- They achieve true multi-threaded parallelism across multiple CPU cores simultaneously.
- **The Trade-Off:** The programmer is fully responsible for avoiding data corruption. If two threads modify a variable at the same time without manual safety gates (`mutexes`, `locks`, or strict ownership rules like Rust), the application crashes or corrupts data silently. Python traded away multi-core threading performance to guarantee developer simplicity and memory safety.

**Modules:**

#### 1. The Low-Level `threading` Module

- **What it is:** The old, raw, manual way to create threads (`threading.Thread`).
- **When to use it:** Almost never in modern production code. It forces you to manually manage starting, stopping, and joining threads, and it makes extracting returned values or handling errors incredibly complex.

```python
import threading
import time

def background_task(name: str):
    print(f"🧵 Thread {name}: starting background work...")
    time.sleep(5)
    print(f"🧵 Thread {name}: finishing work.")

# Initialization

thread_worker1 = threading.Thread(target=background_task, args=("Listener_01",))

thread_worker2 = threading.Thread(target=background_task, args=("Listener_02",))

thread_worker1.start()  # Starts the execution in the background
thread_worker2.start()  # Starts the execution in the background

thread_worker1.join()   # Forces the main script to wait until this thread finishes
thread_worker2.join()   # Forces the main script to wait until this thread finishes

print("🏁 Main script resumed.")
```

#### 2. The Modern `concurrent.futures` Module

- **What it is:** A high-level, production-grade abstraction layer. It introduces **Executors** which manage a pre-built pool of workers for you using a clean asynchronous interface.
- **When to use it:** Always. It completely replaces the manual `threading` module for standard data work.

##### 1. `ThreadPoolExecutor` (For I/O-Bound Work)

Use in Web scraping, downloading large datasets, calling external APIs (e.g., Vapi, Groq, Retell), reading/writing files to disk.

- **Why it works:** When a thread hits network or disk latency (waiting for data), **it voluntarily drops the GIL.** Another thread instantly takes the GIL and fires its own request. The CPU sits back and manages lines while the network does the heavy lifting.

##### 2. The Modern `ProcessPoolExecutor` (For CPU-Bound Work)

Use for Heavy data manipulation, machine learning model inference, matrix math (NumPy operations), processing images/video, parsing massive files.

- **Why it works:** It completely bypasses the GIL by **spawning entirely separate operating system processes**. Each process gets its own personal Python interpreter and its own GIL. The operating system spreads these heavy processes across **separate physical CPU cores** for true uninhibited parallel processing.

####  Race Conditions (the gotcha both threads AND async can have)

- Even though threads take turns (GIL) and async tasks take turns (event loop), two workers can still read-modify-write the **same variable or DB row** at the same moment - like both reading balance=100, both adding 10, both saving 110 instead of the correct 120.
- Fix: wrap that critical "read → change → save" bit with `threading.Lock()` (for threads) or `asyncio.Lock()` (for async tasks), so only one worker can touch that resource at a time.

## Pydantic Module

It is a module which enforces data Schemas and types using Python. It acts as a strict Gatekeeper for application: it validates incoming data, automatically converts types when possible, and throws descriptive reason when the data is invalid.

**It has:** `Base Model:` The foundation of Pydantic. You create classes that inherit from `BaseModel` and define your data fields using standard Python type annotations.

`Data Validation:` When you create an instance of your model, Pydantic checks if the provided inputs match the specified types. If they don't, it halts execution and raises a `ValidationError` with details on exactly what went wrong. It returns structural errors, making it incredibly easy to pipe these messages back to a frontend user or a data log.

`Field:` It is a utility Function which can be used to customize and add metadata to, Validation Rules and default values to the models Attribute.

`field_validator:` Type-checking alone isn't always enough - sometimes you need custom rules, like checking an email actually has an `@` in it, or a password is at least 8 characters. `field_validator` is a decorator that lets you write that extra logic yourself, on top of the basic type check.

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def check_email(cls, v):
        if "@" not in v:
            raise ValueError("Not a valid email")
        return v

    @field_validator("password")
    def check_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password too short")
        return v
```

`Serialization:` It can easily be converted to Standard data formats like dictionary or JSON.

**Pydantic v2 Performance Edge** If you look at modern benchmark testing, Pydantic is blindingly fast. In its recent rewrite (Pydantic V2), the creators rewrote the entire core validation framework in **Rust**. The data parsing logic occurs at the bare metal binary speed of Rust, while offering a beautiful, easy-to-use Python interface.

## Async Programming

**Difference Between Multi-threading and Async:** Multi-threading creates multiple threads to process tasks in parallel, making it idle for CPU-bound computations.

Async uses a single thread to manage multiple tasks, switching between them whenever one is waiting, making it idle for handling network or disc-bound operations efficiently. In Async Python, ==Everything runs on exactly one thread on one CPU core.== There is absolutely zero CPU switching overhead. It achieves massive speedups purely by avoiding sitting idle during I/O wait times.

### Event Loop

At the absolute center of async python sits a master coordinator called the Even loop. Event loop is an endless `While True` loop running your main thread that manages a queue of tasks.

1. When you flag a task as asynchronous, it gets registered with the Event Loop.
2. The Event Loop executes Task A until Task A hits an **I/O operation** (like waiting for a website database response or an API call payload).
3. Task A explicitly yields control back to the Event Loop, saying: _"I'm going to be waiting on the network for a bit. Go do other work."_
4. The Event Loop pauses Task A, looks at its queue, and jumps over to execute Task 2.
5. Once Task A’s network data arrives, the OS notifies the Event Loop, which schedules Task A to resume the second the current running task pauses.

### **async and await**

**`async def Couroutine()`**

- It is used to create co-routine (small tasks inside Thread) functions.
- To call async functions, you need to use await keyword.

`await api_call()`

- It can only be used inside async def.
- It acts a clear pause sign.
- It pauses the current task and instructs Event Loop to execute next task of the queue.

***Some things to Remember:**

```python
1. await async.sleep(2)  ## pauses code and lets other tasks run
```

```python
2. async.sleep(2) # By itself creates a coroutine and sleeps for 2s
```

## Calling APIs

#### **URL/Endpoints**

<img width="816" height="132" alt="Image" src="https://github.com/user-attachments/assets/f6a88034-f4da-4ab2-8539-4058982743fe" />

#### *Requests under HTTP

It contains 4 critical components:

1. **URL and Endpoints**: The destination address `https://api.domain.com/v1/users`
2. **Method:** Instructs the server on what action to take
3. **headers:** Metadata about the request
4. **Body:** Payload

#### *Response under HTTP

The external server processes the request and replies with

1. **Status Code:** ==2xx for success, 3xx for redirection, 4xx for client side Error, 5xx for server side error ==
2. **Response body:** The data payload returned by the database (almost always structured as a raw JSON string).

#### _CRUD Operations_

1. GET (Read Data)
2. POST (Create Data)
3. PUT (Update Data)
4. DELETE (Remove Data)

**Parameter:**

_Path Parameter:_ Mandatorily required to interact with a specific resource.

```python
		/users/{user_id}
```

_Query Parameter:_ Appended to the end of URL after ? to process tasks like sort, filter etc.

```python
		/users/299?lang=py
```

#### Authentication

In API communication, Authentication (Auth) is the security checkpoint at the gateway of a server. Because database contains sensitive business data, private user profiles, or expensive computing resources ( like OpenAI Tokens ), servers use authentication to verify your access.

If you send a request without a security clearance badge, the server instantly drops the connection and returns an **`HTTP 401 Unauthorized`** or **`HTTP 403 Forbidden`** status packet.

Types:

1. Bearer Tokens and API Keys (Modern Standard) Used in tools like OpenAI, Gemini, Stripe

```python
headers = { "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json" }
```

2. Query Parameter Keys (Simpler way) Platforms like Weather, mapping, financial ones

```python
query_params = { "city": "Kolkata", "key": API_KEY
```

3. Basic Auth (with username and pass)

```python
response = requests.get(url, auth=("my_admin_user", "secure_password_123"))
```

_**Multiple API calling**_ Implemented using Session()

```python

session = requests.Session()   # an instance

# locking authorization permanently
session.headers.update({ 
"Authorization": f"Bearer {API_KEY}", 
"Content-Type": "application/json" }) 

user_data = session.get("https://api.example.com/v1/user") 
order_data = session.get("https://api.example.com/v1/orders") analytics = session.post("https://api.example.com/v1/metrics", json={"status": "done"})
```

## PyTest

**Naming Convention:** Files: `test_*.py or *_test.py` Function: `test_*()` Assertion: `assert <condition>`

In real world testing is very very Important and that's where PyTest was developed to reduce the redundancy and scalability of the code. How it is used? Simply create a `test_file` which has all the functions each testing back flops which can be possible and handled once a go by running `pytest` in CMD.



