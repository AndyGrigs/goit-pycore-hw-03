# file = open("db.txt", "r")
try:
    with open("db.txt", "r+") as file:  # Open in write mode
       print( file.read(10))
       print( file.tell())
       print( file.read(12))
       print( file.tell())
except FileNotFoundError:
    print("Error: db.txt was not found.")

"""
Reading and writing files in Python is straightforward thanks to the built-in `open()` function. Here's a basic overview:

### Reading Files

To read a file, you use the `open()` function with the `"r"` mode, which stands for "read". After opening the file, you can use methods like `.read()`, `.readline()`, or `.readlines()` to read its content.

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
```

### Writing to Files

To write to a file, you use the `open()` function with the `"w"` mode, which stands for "write". If the file already exists, it will be overwritten. To append to a file without overwriting existing content, use `"a"` mode for "append".

```python
try:
    with open('example.txt', 'w') as file:
        file.write("Hello, world!")
except FileNotFoundError:
    print("File not found.")
```

### Reading and Writing Together

You can also read and write to the same file within the same block. Just remember to set the file pointer back to the beginning after writing if you want to read what you just wrote.

```python
try:
    with open('example.txt', 'r+') as file:
        content = file.read()
        print(content)
        
        file.seek(0)  # Move the file pointer back to the beginning
        
        file.write("New content added.\n")
        file.write("More content.\n")
        
        file.truncate()  # Truncate the file to the current position of the file pointer
        
except FileNotFoundError:
    print("File not found.")
```

### Important Notes

- When writing to a file, always ensure that the file is closed properly to avoid data corruption. Using `with` statement ensures this automatically.
- Be cautious when truncating a file (`file.truncate()`), as it removes all content beyond the current file pointer position.
- Always handle exceptions like `FileNotFoundError` to gracefully manage situations where the file does not exist.
"""