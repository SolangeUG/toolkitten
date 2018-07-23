# Homework

Upload a single file named as `soc01hw-firstname-lastname.py`, with all exercises from **A Few Things to Try** sections.

If it says *Optional*, then the homework is of course optional, it is for those who would like more exercise,
or more advanced exercises.

## Day - 01

**Write a program that tells you the following:**
- Hours in a year. How many hours are in a year?
- Minutes in a decade. How many minutes are in a decade?
- Your age in seconds. How many seconds old are you? I'm not going to check your answer, so be as accurate—or not—as you want.
- Andreea Visanoiu​: I'm 48618000 seconds old. Calculate Andreea Visanoiu's age.

**Here are some tougher questions:**
- How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
- How about a 64-bit system?
- Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday).
You will need Python modules.

## Day - 03

**Full name greeting:**
- Write a program that asks for a person’s first name, then middle, and then last.
- Finally, it should greet the person using their full name.

**Bigger, better favorite number:**
- Write a program that asks for a person’s favorite number.
- Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. Do be tactful about it, though.

**Angry boss:**
- Write an angry boss program that rudely asks what you want.
- Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
> WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

**Table of contents:**
- Here’s something for you to do in order to play around more with `center`, `ljust`, and `rjust`.
- Write a program that will display a table of contents so that it looks like this:

````
Table of Contents

Chapter 1:      Getting Started        page 1

Chapter 2:      Numbers                page 9

Chapter 3:      Letters                page 13
````

## Day - 04

**99 Bottles of Beer on the Wall:** 
- Write a program that prints out the lyrics to that beloved classic, [99 Bottles of Beer on the Wall][1].

**Deaf grandma:** 
- Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
- Unless you shout it (type in all capitals). 
- If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938!
- To make your program really believable, have Grandma shout a different year each time. Maybe any year at random between 1930 and 1950. 
- You can’t stop talking to Grandma until you shout BYE.

**Leap years:**
- Write a program that asks for a starting year and an ending year and then puts all the leap years between them 
(and including them, if they are also leap years).
- Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years 
(such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000).

**Looping and sorting:**
- Write a program that asks us to type as many words as we want, one word per line, continuing until we just press 
`Enter` on an empty line. 
- The program then repeats the words back to us in alphabetical order. 
- Make sure to test your program thoroughly; for example, does hitting `Enter` on an empty line always exit your program? 
Even on the first line? And the second?

**Old-school Roman numerals:**
- Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral.
- Old-school Roman numeral means that 4 should return `IIII`.
- For reference, these are the values of the letters used: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.

**Modern Roman numerals:**
- Rewrite the previous method to return the **new-style** Roman numerals. 
- When someone calls your program with 4 as a parameter, it should return `IV`, 90 should be `XC`, etc.


[1]: http://www.99-bottles-of-beer.net/lyrics.html
