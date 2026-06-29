# py-backend-core
Exploring structural Python backend mechanics, data validation, and concurrent processing pipelines.

A personal sandbox where I'm learning how Python backends actually work under the hood, moving past just standard high-level frameworks. 
I built these files to experiment with data validation, concurrency, security, and testing from first principles.

## What's in here?

* **01-05 OOP Basics:** Playing with inheritance and polymorphic classes.
* **06 Decorators:** Custom wrappers to log how long functions take to run.
* **07-09 Concurrency:** Testing multi-threading and `asyncio` to handle non-blocking operations.
* **10 & 12 APIs & Data:** Validation with Pydantic, calling the Gemini API safely with environment variables, and setting up a local JSON cache to save token usage.
* **11 Pytest:** Writing test suites and using Mock patching so I don't hit live APIs during tests.

**Read My Complete Backend Engineering [NOTES.md](/NOTES.md)**

## 💖 Credits

Building things from scratch is cool, but standing on the shoulders of giants is way cooler. 

* **Open Source Community:** Huge respect to the human beings behind `pydantic`, `requests`, `httpx`, and `pytest`. You guys are the unsung heroes saving developers from writing thousands of lines of manual validation and raw network socket code.
* **[Ansh Lamba: ](https://www.youtube.com/watch?v=M-UtKxgtKag)** For mapping out the intermediate backend curriculum.

## How to run it

If you want to poke around or run the tests locally:

``bash
pip install -r requirements.txt``

