Python Random Sampling Tests

Statistically, over a long enough time and  of the random class, a RNG should hit each of its possible outcomes approximately evenly.
ie over 100k coin flips it should be roughly 50/50 h/t

Very early in my programming career, I made a simple Rock Paper Scissors game in Visual Basic. Regardless of the number of times which I reloaded the game, the Computer which was choosing an integer 1 to 3 for its own move always favored paper to the point which spamming scissors would always result in a win over a long enough game (didnt need to be THAT long either. Maybe 20 rounds.)

It could have been a quirk of VB, or the extremely locked down school computers, floating point rounding, literally anything; however, I need to ensure that random numbers in python ACTUALLY work as intended before relying on them.
Does scaling up the range reduce the amount of user perceived rounding error? ie 0:2 vs 0:8 vs 0:98


##########
Answer: it works well enough for my purposes. reference <Success.jpg>
##########
