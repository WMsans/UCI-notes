Group Members: 
1. Vincent Chen
2. Armando Martinez
3. Jeremy Zhao
4. Ashton Lin
# Problem 1
We have 4 cards which have a number on one side and a color on the other side. We also have a condition: if the number is even, then the other side is blue. Given the 4 cards below, which of them do we need to turn around to check whether our condition is true for all these cards? Select all cards that should be flipped. Please, only turn around the card(s) when absolutely necessary.
![[Pasted image 20260930112001.png|255]]

## Solution
Only `8` and `red` need to be flipped.

# Problem 2

Express the following statements in the form: _If p then q_. Find out what will make the statement false and use it to figure out the right direction for this conditional.

- I'll eat vegetable soup only if you give me sour cream.
- Learning assistants must register for UNI STU 176 unless they are CLAP-certified.

**Example**: Honey is necessary for the honey cake.

This statement is false if you manage to bake a honey cake without honey.
If this is a honey cake, honey is an ingredient.
p = This is a honey cake
q = Honey is an ingredient

## Solution
### I'll eat vegetable soup only if you give me sour cream.

This statement is false if you don't give me sour cream while eating the soup. 
p = You give me sour cream
q = I'll eat vegetable

P -> q
### Learning assistants must register for UNI STU 176 unless they are CLAP-certified.

This statement is false if LA are not clap certified while not registering for UNI STU 176. 

p = LA are not clap certified
q = LA must register for Uni STU 176

P -> q

# Problem 3

In one of the previous editions of this handbook, car seats are mentioned in two places.
The first time it's formulated like this:
**Children who don't have to use a car seat**

**・p: Children who are 8 years old or older OR** 

**・q: who have reached at least 4 feet 9 inches in height**

The second time they discuss cases when children **must use a car seat**. 
In California Driver's Handbook, this condition is given as

**Children who must use a car seat**

**・p: child 8 years old or younger OR**

**・q: child less than 4 feet 9 inches tall**

Assuming the first statement is correct, the second statement is wrong.
How many mistakes did they make? List all mistakes.
## Solution

A child who don't use a car seat:
p  = Children who are 8 years old or older 
q = who have reached at least 4 feet 9 inches in height

¬(p ∨ q): *Children who are 8 years old or older* or *who have reached at least 4 feet 9 inches in height* **don't have to use a car seat**. 

Apply De Morgans Law: 
(¬p ∧ ¬q): *child 8 years old or younger* **And** *child less than 4 feet 9 inches tall* **must use a car seat**. 

Mistakes: 
1. Use **And** instead of **Or**
2. Use **At Most** instead of **less than**

# Problem 4
I'm really confused

W = p -> ¬q
P = One is with us
Q = One is against us

A = ¬p -> q = p -> ¬q
Proven