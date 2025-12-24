# How to work with Python dictionary
```bash 
1️⃣ Creating Dictionaries
d = {}
d = dict()
d = dict(a=1, b=2)
d = dict([("a", 1), ("b", 2)])

2️⃣ Accessing Values
dict[key]
d["a"]


❌ Raises KeyError if missing

get()
d.get("a")
d.get("a", 0)   # default value


✅ Safe access

3️⃣ Adding & Updating Items
Assign value
d["c"] = 3

update()
d.update({"d": 4})
d.update(e=5)

4️⃣ Removing Items
pop()
d.pop("a")
d.pop("x", 0)   # safe pop

popitem()
d.popitem()     # removes last inserted item (LIFO)

del
del d["b"]

clear()
d.clear()

5️⃣ Dictionary Views (Iterating)
keys()
d.keys()

values()
d.values()

items()
d.items()


Example:

for k, v in d.items():
    print(k, v)

6️⃣ Copying Dictionaries
Shallow copy
d.copy()

Deep copy
import copy
copy.deepcopy(d)

7️⃣ Checking Existence
in operator
"a" in d

8️⃣ Default & Conditional Operations
setdefault()
d.setdefault("a", 10)


Returns value if key exists

Inserts key if missing

9️⃣ Dictionary Length
len(d)

🔟 Sorting Dictionaries
Sort by keys
dict(sorted(d.items()))

Sort by values
dict(sorted(d.items(), key=lambda x: x[1]))

sort values according particular field in nested dictionary
sorted_data = sorted(data.values(),key=lambda  x : x.get(sortby,0), reverse=sort_order)

1️⃣1️⃣ Dictionary Comprehension
squares = {x: x*x for x in range(5)}


With condition:

{x: v for x, v in d.items() if v > 10}

1️⃣2️⃣ Merging Dictionaries (Python 3.9+)
Using |
d3 = d1 | d2

Update in-place
d1 |= d2

1️⃣3️⃣ Built-in Functions That Work with Dicts
Function	Use
len(d)	Number of keys
min(d)	Smallest key
max(d)	Largest key
sum(d.values())	Sum of values
any(d.values())	Any True
all(d.values())	All True
1️⃣4️⃣ Converting Dictionary
To list
list(d)
list(d.keys())
list(d.values())
list(d.items())

To JSON
import json
json.dumps(d)

1️⃣5️⃣ Nested Dictionary Access (Common)
d["a"]["b"]
d.get("a", {}).get("b")


```