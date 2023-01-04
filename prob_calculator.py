import copy
import random
# Consider using the modules imported above.

# First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. 
class Hat:

# A hat will always be created with at least one ball. The arguments passed into the hat object upon creation should be converted to a contents instance variable. contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color. For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].
  def __init__(self, ** kwargs):
    self.contents = [] 

    for key, value in kwargs.items():
    # for red,3 in (red = 3, green = 1, blue = 2)
      for increment in range(value): 
        # red = 3, so range(value) will be 3, increment will go 0, 1, 2
        # green = 1, range(value) will be 1, increment will go 0
        # blue = 2, range(value) will be 2, increment will go 0, 1 
        self.contents.append(key)
        # for each increment, we append the 'key'
        # increments for red             = 0,   1,   2
        # .append(key) at each increment = red, red, red 
        
    # print(self.contents)
    # hat = Hat(blue = 3,red = 2,green = 6)
    # ['blue', 'blue', 'blue', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'green']
    

# The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.
  def draw(self, number_balls):
    balls_drawn = []

    if (number_balls > len(self.contents)):
      # len(['red', 'red', 'red', 'green', 'blue', 'blue'])
      # 6 
      return self.contents
      # returns all the balls, the entire self.contents list. 
    else:
      for ball in range(number_balls):
        random_index = random.randrange(len(self.contents))
        # returns an integer between 0 to 6, randomize index for the list of balls in our Hat class
        # 6 is the length of our self.contents list
        balls_drawn.append(self.contents[random_index])
        # applies random index to our list of balls in Hat class, and appends to our new list of balls_drawn
        self.contents.pop(random_index)
        # For each ball we withdraw, we also want to remove it from the current self.contents list so it doesn't get withdrawn again. 
        # pop(index) references random_index, the same index position and ball that we appended in previous line. 
        
      return balls_drawn
      # e.g. ['green', 'red', 'green', 'blue']




# Create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:
# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  times_getting_expected_balls = 0 
  # IMPORTANT - this needs to be OUTSIDE the for loop. Does not iterate per experient. We accumulate over all the experiments.
  # 274 (changes each run, usually between 200 - 300)
  
  # STEP 1 - creates a list for each instance based on num_experiments, each list withdrawing the specified num_balls_drawn
  for experiment in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    # makes a copy of our list in Hat class
    # ['red', 'red', 'red', 'green', 'blue', 'blue']
    
    new_balls_withdrawn_list = []
    new_balls_withdrawn_dict = {}
    # a list will accumulate the colors e.g. ['blue', 'red', 'red']
    # a dictionary will keep count of EACH color e.g. ['blue': 1, 'red': 2]
    
    new_balls_withdrawn_list = new_hat.draw(num_balls_drawn) 
    # ['blue', 'red', 'red']

    # STEP 2 - create a dictionary to keep count of the colors that are generated from our lists previously. 
    for color in new_balls_withdrawn_list: # we loop through  # ['blue', 'green', 'red']
      if color not in new_balls_withdrawn_dict:
        new_balls_withdrawn_dict[color] = 1 # IF it's the first time in our dictionary per experiment iteration, we assign it a value of = 1
      else:
        new_balls_withdrawn_dict[color] += 1 # OTHERWISE, if it's already in our dictionary, we accumulate by adding += 1
    # print(new_balls_withdrawn_dict)
    # {'blue': 1, 'green': 1, 'red': 1}
      
    # STEP 3 - Compare/check if the color and values from our expected dictionary exists in our withdrawn dictionary
    # A match is found when for each experiment aka for each list, the balls that were drawn e.g. ['red', 'red', 'green']
    # AGREES with our argument expected_balls = {"red": 2,"green": 1} == ['red', 'red', 'green'], no order, as long as it is IN the LIST
    dict_items_matches_found = 0
    expected_balls_list_of_tuples = expected_balls.items() # dict_items ( [ ('red', 2), ('green', 1) ] )
        
    for key, value in expected_balls_list_of_tuples:
    # keys, value
    # red, 2, 
    # green, 1
      
      key_list = new_balls_withdrawn_dict.keys() # dict_keys( ['blue', 'green', 'red'] )
      # For each loop through the keys of the expected_balls dictionary, 
      # IF the key color from our expected_balls dictionary is IN our withdrawn list of colors
      # AND the value of that color from our expected_balls EXISTS (less or equal) in our withdrawn values
      # expected_balls = {"red": 2,"green": 1},
      # new_balls_withdrawn_dict = {'blue': 2, 'green': 1, 'red': 3}
      
      if (key in key_list) and (value <= new_balls_withdrawn_dict[key]):
      # red in {'blue': 2, 'green': 1, 'red': 3}? Yes
      # and 2 <= 3? Yes

      # green in {'blue': 2, 'green': 1, 'red': 3}? Yes
      # and 1 <= 1? Yes
        
        dict_items_matches_found += 1
    # print(dict_items_matches_found)

    # STEP 4 - if all the items within our withdraw dictionary matches, then it would agree to the total # of items in the expected dictionary
    if (dict_items_matches_found == len(expected_balls)): # len of expected_balls = {"red": 2,"green": 1} is 2
        times_getting_expected_balls += 1

  # STEP 5 - The experiment function should return a probability.
  the_probability = (times_getting_expected_balls / num_experiments)

  return the_probability


# TEST
# hat = Hat(red = 3, green = 1, blue = 2)
# hat_draw = hat.draw(2)

# probability = experiment(hat = hat,
#                  expected_balls = {"red": 2,"green": 1},
#                  num_balls_drawn = 3,
#                  num_experiments = 2)

# print(probability)



hat = Hat(blue=3,red=2,green=6)
hat_draw = hat.draw(4)
print(hat)
print(hat_draw)

probability = experiment(hat = hat, 
                          expected_balls={"blue":2,"green":1}, 
                          num_balls_drawn=4, 
                          num_experiments=1000)
expected = 0.272
print(probability)

