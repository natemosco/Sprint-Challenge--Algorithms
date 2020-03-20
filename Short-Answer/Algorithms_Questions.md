# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

linear O(n) because the complexity of the problem never increases but based on the input can take longer despite being only a single variable check and a single operation. input such as 1,000,000 would still work quickly, but large factorials would slow this down

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(potentinever ending story) because J is redefined to 1 within the loop LOL

but in all seriousness this is polynomial because it is a nested loop O(n^c)
if n = 10,000
i=0, j=1 ,2,4,,8,16,32,64,... etc until we hit 10,000
then
i=1 j=1 ,2,4,,8,16,32,64,... etc until we hit 10,000

so the larger the number the worse the inner loop gets.. which is what slows this down

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(c^n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

and we say that b = breakpoint [0,1,2,3,4,5,6,7,8,9,10,b,12,13]
well if linear you get drops increasing until you get a broken egg
so linear = (whatever the floor threshold is +1) === 12

if you do a binary approach
and we say that b = breakpoint [0,1,2,3,4,5,6,7,8,9,10,b,12,13]
we check halfwaypoint; 7 (didnt break) so check next halfwaypoint between 7 and the top floor
check 10(didnt break) check between 10 and top floor
check 12(breaks) too far.. but we checked 10 already
meaning it was 11

total drops plus break === 3+break === 4
