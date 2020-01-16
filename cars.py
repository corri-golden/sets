# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("model x")
showroom.add("model y")
showroom.add("model z") 
showroom.add("cybertruck")
# print(showroom)

# Print the length of your set.
# print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("cybertruck")
# print(showroom)

# Using update(), add two more car models to your showroom with another set.
another_set = set(["camry", "corrolla"])
showroom.update(another_set)
# print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("camry")
# print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = {"BMW", "Mercedes", "Prius", "cybertruck", "model z"}
# print(junkyard)

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
new_inv = showroom.intersection(junkyard)
# print(new_inv)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
new_showroom = showroom.union(junkyard)
# print(new_showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
new_showroom.discard("cybertruck")
print(new_showroom)

