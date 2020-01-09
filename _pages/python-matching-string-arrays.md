---
layout: archive
title: "Python code Snippet"
excerpt: "Snippets for matching word in strings"
author_profile: true
redirect_from:
  - /python-matching-string-arrays/
  - /python-matching-string-arrays.html
---

## How to know if a word is inside of a string

This question come up in [StackOverflow](https://stackoverflow.com/questions/59658494/only-get-items-in-list-that-are-in-another-list) these days.

Some user is trying to find a word withing a string. Then, he want to use a list of words to find all of them in a list of strings.

My snippet code an easy way is written below:

```python
some_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

sentence_list = ["i'm going this friday", "i'm not going", "i plan to go saturday"]

new_list = []

for day in some_list:
    for sentence in sentence_list:
        if day in sentence:
            new_list.append(sentence)

print(new_list)
```

$ python lookingwordinlist.py
> ["i'm going this friday", 'i plan to go saturday']


[Download snippet here](http://nicorl.github.io/files/lookingwordinlist.py)
