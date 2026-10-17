## A defaultdict automatically creates a default value for missing keys.
from collections import defaultdict


# students = {}

# students["Python"].append("John");
# print(students);
## above program give type error

employee=defaultdict(list);

employee["developer"].append("john");
employee["developer"].append("alice");
print(employee);