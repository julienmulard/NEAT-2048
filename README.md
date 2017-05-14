# NEAT-2048
An evolving population of neural networks trying to solve 2048.

## NeuroEvolution of Augmenting Topologies (NEAT)

NEAT is a machine learning algorithm, where a population of basic neural networks evolves following genetic rules and have its individuals quite litterally grow in order to solve a given problem.

You can learn more about NEAT on the [user page](http://www.cs.ucf.edu/~kstanley/neat.html)

The original publication is available [here](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).

## 2048

2048 is a game where you have to merge tiles of the same value in order to form the biggest tile possible. The game is considered won if the player manage to form a 2048 tile, but the option to continue playing is given and bigger tiles can be achive.

You can play it [here](http://gabrielecirulli.github.io/2048/)

## The Project

It all started because of [this video](https://www.youtube.com/watch?v=qv6UVOQ0F44), where the Youtuber SethBling explains how he used the NEAT algorithm to automatically solve a level in Super Mario World, on the Super NES. 

After reading the orginal NEAT paper, I decided, given the rather simple logic behind it, to try and implement it for myself, and apply it on a different game, a simpler one I could code from scratch to have a simpler interface between the algorithm and the game.

I choose Python because I wanted to improve in that language.

## The Files

- LearningGamebord.py : the code behind my version of 2048
- NEATNode.py, NEATGene.py, NEATOrganism.py, NEATPopulation, NEATSpecies.py are all refering to the core elements of the NEAT Algorithm
- Any file  with "_test" in its name is a test file. So if you just want to run things, you can discrd those
- NEAT_XOR.py runs the NEAT algorithm to evolve into a XOR function. It's a basic test for this kind of algorithm..
- NEAT_2048.py and NEAT_2048_2.py both try to solve 2048. Note that those can take huge amout of time before converging into any kind of solution. I mean days. Optimisation was NOT my priority when working on this project.

## Overall Status

The algorithm converge slowly, or sometimes never. A lot of parameters are scattered between different classes, and a global parameter class will help tuning the algorithm. This is what I am working on. 
