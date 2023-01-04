# freeCodeCamp-Probability-Calculator

## Instructions:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

<br>

## Purpose
First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

    ```python
        hat1 = Hat(yellow=3, blue=2, green=6)
        hat2 = Hat(red=5, orange=4)
        hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

    ```

Second, create an experiment function that should return a probability. Here is how you would call the experiment function based on the example above with 2000 experiments:

    ```python
        hat = Hat(black=6, red=4, green=3)
        probability = experiment(hat=hat,
                        expected_balls={"red":2,"green":1},
                        num_balls_drawn=5,
                        num_experiments=2000)
    ```


<br>

## Preview:
<img src="https://github.com/iVuDang/freeCodeCamp-Probability-Calculator/blob/main/probability%20print.png" width=100% height=100%>

<br>

## Technologies: 
* Python

<br>

## Outcome :white_check_mark: :
| Website | Link | 
| ------------- | ------------- | 
| Replit demo | https://replit.com/@iVuDang/boilerplate-probability-calculator#prob_calculator.py | 

<br>

- - - -

## My Notes - stuff I learned:  
1) Arbitrary Keyword Arguments, **kwargs

    Keyword Arguments are often shortened to kwargs.

    If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

    This way the function will receive a dictionary of arguments, and can access the items accordingly.

    **kwargs allows us to pass a variable number of keyword arguments to a Python function.

    Example 

        ```Python 
            def total_fruits(**kwargs):
                print(kwargs, type(kwargs))

            total_fruits(banana=5, mango=7, apple=8)
        ```

    Output:
        ```Python 
            {'banana': 5, 'mango': 7, 'apple': 8} <class 'dict'>

            total_fruits(banana=5, mango=7, apple=8)
        ```

        ```Python 
            def total_fruits(**fruits):
                total = 0
                for amount in fruits.values():
                    total += amount
                return total

            print(total_fruits(banana=5, mango=7, apple=8))
            print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
            print(total_fruits(banana=5, mango=7))
        ```

    Output:

        ```Python 
        20
        30
        12
        ```

    Note that the name of the argument need not necessarily be kwargs – again, it can be anything. In this case, it's fruits. But it's generally a standard way to use **kwargs as the name.



2. items() method
    items() method returns a view object. 
    The view object contains the key-value pairs of the dictionary, as tuples in a list.
    (Object [List (Tuples key-value) ] )

    Syntax
    dictionary.items()

    Example:

        ```Python 
            car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }

            x = car.items()

            print(x)
        ```

    Output:

        ```Python 
            dict_items(
                        [
                        ('brand', 'Ford'), 
                        ('model', 'Mustang'), 
                        ('year', 1964)
                        ]
                    )
        ```

3) random.randrange() method

    Syntax:
    module.method
    random.randrange(start, stop, step)

        ```Python 
            import random
            print(random.randrange(3, 9))

            #returns a number between 3 (included) and 9 (not included)
        ```


4) pop() method removes the specified index.

    Useful to clean up 'dirty data' (trailing items) resulting from a loop.  


5) copy.deepcopy(list)
    Assignment statements do not copy objects, they create bindings between a target and an object. When we use the = operator, It only creates a new variable that shares the reference of the original object. In order to create “real copies” or “clones” of these objects, we can use the copy module in Python.

    In the case of deep copy, a copy of the object is copied into another object. It means that any changes made to a copy of the object do not reflect in the original object. 



    Syntax: 
    module.method
    copy.deepcopy(list)

        ```Python 
            # importing copy module
            import copy
            
            # initializing list 1
            li1 = [1, 2, [3, 5], 4]
            
            # using copy for shallow copy
            li2 = copy.copy(li1)
            print("li2 ID: ", id(li2), "Value: ", li2)
            # using deepcopy for deepcopy
            li3 = copy.deepcopy(li1)
            print("li3 ID: ", id(li3), "Value: ", li3)
        ```


    Output:

        ```Python 
            li2 ID:  2521878674624 Value:  [1, 2, [3, 5], 4]
            li3 ID:  2521878676160 Value:  [1, 2, [3, 5], 4]
        ```



6. count() Method

    Example
    Return the number of times the value "cherry" appears in the fruits list:

    ```Python 
        fruits = ["apple", "banana", "cherry", "cherry"]

        x = fruits.count("cherry")

        print(x)
        # 2
    ```


7. The keys() method 

    The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

    The view object will reflect any changes done to the dictionary, see example below.

Syntax
dictionary.keys()

    ```Python 
        car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }

        x = car.keys()

        print(x)

        dict_keys(['brand', 'model', 'year'])
    ```

8. ;print(variable)

    At the end of each line to trace and debug. 


<br>

## Citations:

* Ideas on how to solve project inspired by ZeynebBechiri 

* https://www.w3schools.com/python/python_functions.asp
* https://www.freecodecamp.org/news/args-and-kwargs-in-python/#:~:text=**kwargs%20allows%20us%20to,* denote%20this%20type%20of%20argument.


* https://www.w3schools.com/python/ref_dictionary_items.asp


* https://www.w3schools.com/python/ref_random_randrange.asp
* https://www.w3schools.com/python/python_lists_remove.asp

* https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

* https://www.w3schools.com/python/ref_list_count.asp












