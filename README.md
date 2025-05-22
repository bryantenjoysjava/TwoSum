# My thoughts
I thought of trying to use a set, originally, then switched to using a dictionary. Initially, I put the indexes of the list in the keys and the values in the list as the values in the 
dictionary. However, I realized that if I switched the places of the indexes and values in the dictionary, I could make the algorithm work. Instead of adding the values one by one in 
the dictionary and brute forcing the algorithm, I took the difference form the target number and the current value in the dictionary and checked if that difference was also another 
value in the dictionary. If so, we return the associated KEYS to those values in a new list in the form of [a.b]. Note, I realized that the algorithm has to check if the difference is
in the other values of the dictionary first, before we add the number in the list to the dictionary for comparison, or some edge cases occur that impact the algorithm.
