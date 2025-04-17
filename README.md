# PokemonBreedingCalculator
Simulate the outcome of breeding pokemon who are holding the Destiny Knot

## What is this thing?
This application allows the user to specify Pokemon IVs for two parents (one of which is holding the Destiny Knot) and generate the IVs of a resulting child.  This can be done as many times as desired and the results can be pasted into excel / google sheets for analysis.

Basically it helps you determine the odds of breeding specific IVs.

### The calc in action
![Just look at that fancy GUI!!!](/images/sample.png)
* Set parent IVs via spinner buttons or manually typing them.
* CSV / TAB to toggle output format
* RND to randomize parent IVs
* MAX to set all IVs to maximum (31) "Best!"
* GEN to generate a new row of stats for a single poke-child.
* Copy / Paste results into your favorite number cruncher.

### Paste your results into excel / google sheets for number crunching
![Yaay numbers!](/images/sample_excel.png)

## Features
* Easily generate hundreds of simulated uh... poke-children
* Highlights perfect IVs
* Options to quickly maximize, manually set, or randomize parent IVs
* Toggle between CSV or TAB separated outputs
* Includes the parent IVs and headers in the output each time parent IVs change.
* Uses a fancy GUI!!!
* Not written using AI - I can write bad code all by myself.
* No animals were harmed during the construction of this software, but a whole lot of electrons were inconvenienced.

## Installation
Download or clone the pokemonBreedingCalc.py file

## Requirements
Python

## Running 
In the command line / terminal type: 
>python pokemonBreedingCalc.py

Or just double click the pokemonBreedingCalc.py file

## Forward Work

* Option to pre-define the number of simulated poke-children to generate.
* Option to Generate running total / summary of current simulation.
* Option to output to a file rather than paste results.
* Option to specify gender ratio and include gender in results.
* Option to save parent IVs for later use.
* Add a Help menu
