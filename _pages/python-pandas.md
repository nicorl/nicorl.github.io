---
layout: archive
title: "Pandas Snippets"
excerpt: "Snippets for pandas"
author_profile: true
redirect_from:
  - /python-pandas/
  - /python-pandas.html
---

## Loading CSV file with unknowns sepparators:

```python
csv_file = pd.read_csv('file.csv', sep = None, engine = 'python')
```

## Problems

### UnicodeEncodeError: 'charmap' codec can't encode character

type in console:
> chcp 65001
