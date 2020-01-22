---
layout: archive
title: "Duolingo Date Snippet"
excerpt: "Snippets for calculate dates"
author_profile: true
redirect_from:
  - /python-dates/
  - /python-dates.html
---

Last week I had achieved 1200 days on duolingo! That's a great mark but I wonder know when I started my way with that.

<center>
<img src="/images/duolingo-streak.png" alt="Duolingo" style="width:170px;height:80px;">
</center> <br>

So, I thought about creating a small snippet code for sharing!


## Code

```python
# Usage
# python number_of_days_to_date.py -d number_of_days
import argparse
from datetime import datetime, date, time, timedelta

# This code is to catch the argument as 'dias' variable.
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dias",
	help="numero de dias para convertir")
args = vars(ap.parse_args())
dias = int(args["dias"])

# The importance between / and //.
años = dias // 365
meses = int( (dias / 365 - dias // 365)*12 // 1 )
diasenmes = int( ((dias / 365 - dias // 365)*12 / 1 - (dias / 365 - dias // 365)*12 // 1)*30 // 1 )

print('{} días son: {} años, {} meses, {} días'.format(dias, años, meses, diasenmes, ))

fecha_origen = date.today() - timedelta(days=dias)
print('Todo esto empezó el {}'.format(fecha_origen))

```

## The keypoint

The importance of the operator `/` and `//`:
* `/` returns the complete division  
> 5.3451 / 1 =  5.3451

* `//` returns the entire part.
> 5.3451 // 1 = 5.0

## Usage
The usage is through and argument
> python number_of_days_to_date.py -d 1200

[Download snippet here](http://nicorl.github.io/files/number_of_days_to_date.py)
