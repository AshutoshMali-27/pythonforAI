student={"name":"ashutosh","age":27};
print(student["name"]);
print(student["age"]);

print(student.get("name"));
print(student.get("salary"));

## add new key
student["salary"]="58000";
print(student);

## update value of key
student["salary"]=41000
print(student);

## pop element
student.pop("salary");
print(student);
## del 
del student["age"];
print(student);

## clear
student.clear()
print(student);

employee={"name":"ashutosh","age":27,"salary":"45000"};
for key in employee:
    print(key);

for value in employee.values():
    print(value);

for key,value in employee.items():
    print(key,value);


if "name" in employee:
    print("found");

print(employee.keys());
print(employee.values());