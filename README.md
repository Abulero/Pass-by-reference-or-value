# Pass-by-reference-or-value
Simple Python code to show how variables are treated once they enter a method as arguments.  

The output of the script is:  

```
1/2/1
```

But why? 

The explanation might be confusing, but reflects how many programming languages work (Python, C++, C# and Java if I'm not mistaken):  

When you pass a variable to a method as an argument, it can be "Passed by value", which means only a copy of it is used, or it can be "Passed by reference", where the variable itself is used. That being said, only the objects are passed both by reference and value, while the integer is passed only by value.  

```
a: Passed by value
b: Passed by reference and value
c: Passed by reference and value
```

Depending on how you use these objects, you can be using their reference or their value. When you use the whole object, you access its value. But when you use its attributes directly, you access its reference. It's important to keep that in mind when working with classes if you don't want whole operations on objects to be discarded only because they were passed by value.