# Car Models

Use Python to build a console app that interacts with two files:
```
car-makes
car-models
```
## Car Makes

This file should contain just the names of several makes.

car-makes
```
Toyota
Nissan
...
```
## Car Models

This file should contain the names of several models for each make. The format will be as follows.

```{first letter of make}={model name}
```

car-models
```
T=Camry
N=Altima
...
```
## Requirements

1. Create a single class that implements all functionality.
2. Create a method for reading the car makes file.
3. Create a method for reading the car models file.
4. Create a method that invokes the previous two methods and generates a dictionary.
    i.The dictionary keys will be the make names.
    ii.The value for each key will be a list of model names.
```
{
    "Toyota": ["Camry"],
    ...
}
```# NSS-python-file_storage
