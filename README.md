# Connected Components

## About

This hobby-project is an implementation of an algorithm for finding connected components in a 2D map. The algorithm is based on the Depth-First Search algorithm.

I have encountered this problem twice in my life - both for interviews. Although I knew the basic logic to solve the problem, that is to start with a node, and look for adjacent nodes that are connected to it, I did not have clear idea on how to implement it. I have implemented the solution in Python. I have also made some optimisations to improve the speed and robustness.

The problem statement is as follows:

    Imagine you are working for the local government as a land surveyor. It is your job to find out how much more space there is on the city's current industrial site for new buildings. To that end, you need to measure how many buildings there are today. 

    The industrial site is represented by a 2D array, where "B" represents (part of) a building and "E" represents an empty space. If Bs are horizontally or vertically connected to other Bs, then those Bs are part of one building. If two Bs are only diagonally connected, regard them as separate buildings. 

    Write a function: find_building(input_map)  that returns the number of buildings on the industrial site. If any of the elements in the array are not "B" or "E", the function should return -1.

The same code/logic can be used to find the solution to the island problem.
