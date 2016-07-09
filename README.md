# dokky
Python client for Docsbox

# Usage
```python
import dokky

docsbox = dokky.Docsbox(hostname="you.docsbox.hostname:66")

with open("kittens.docx", "rb") as source:
    document = docsbox.proccess(source, formats=["pdf"])
    document.id # => {}
    document.status # => queued
    document.get_status() # => started
    document.get_status() # => finished
    result = document.get_result() # => zipfile.ZipFile object
    pdf = result.read("pdf") # => file-like obj
