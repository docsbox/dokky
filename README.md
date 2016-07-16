# dokky [![Build Status](https://travis-ci.org/docsbox/dokky.svg?branch=master)](https://travis-ci.org/docsbox/dokky)
Python client for Docsbox

# Install

```bash
$ pip install dokky
```

# Usage
```python
import dokky

docsbox = dokky.Docsbox(hostname="you.docsbox.hostname:66")

with open("kittens.docx", "rb") as source:
    document = docsbox.process(source, formats=["pdf"])
    document.id # => 8e6f5e26-77fb-4b4f-975d-c8147f009885
    document.status # => queued
    document.get_status() # => started
    document.get_status() # => finished
    result = document.get_result() # => zipfile.ZipFile object
    pdf = result.read("pdf") # => file-like obj
