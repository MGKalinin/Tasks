# Challenge Nine
## Problem
Ada gives John a positive integer N. She challenges him to construct a new number (without leading zeros), that is a multiple of 9, by inserting exactly one digit (0 … 9) anywhere in the given number N. It is guaranteed that N
does not have any leading zeros.

As John prefers smaller numbers, he wants to construct the smallest such number possible. Can you help John? 

## Input
The first line of the input gives the number of test cases, T. 
T test cases follow.


Each test case has a single line containing a positive integer N: the number Ada gives John.
## Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the new number constructed by John. As mentioned earlier, y cannot have leading zeros.
## Sample Input
3

5

33

12121
## Sample Output
Case #1: 45

Case #2: 333

Case #3: 121212


In Sample Case #1, there are only two numbers that can be constructed satisfying the divisibility constraint: 45 and 54 . John chooses the smaller number.

In Sample Case #2, 333

is the only number possible.

In Sample Case #3, there are four possible options - 212121
, 122121, 121221 and 121212 - out of which the smallest number is 121212. 

## Analysis
For simplicity, let us use L to represent the number of digits in N, note the scale of L is actually O(log10N). And let us use {aL−1,aL−2,…,a1,a0} to represent the digits of N, where aL−1 is the most significant digit and a0 is the least significant digit (0≤ai≤9 for all i<L−1, and 1≤aL−1≤9). We can read N as a string, where the characters in the string {s[0],s[1],…,s[L−2],s[L−1]} represent {aL−1,aL−2,…,a1,a0}. Or, we can read N as an integer, whose value equals aL−1×10L−1+aL−2×10L−2+⋯+a1×10+a0. Inserting a new digit d in the k−th position in N means inserting it after the first L−k digits (on the left side) and before the last k digits (on the right side) of N. If N is string type, then the new number can be built by slicing and concatenating the string as s[0…L−k]+string(d)+s[L−k…L] in linear time, where s[i…j] means characters of string s from index i to index j. On the other hand, if N is integer type, then the new number can be calculated as (N−N%10k)×10+d×10k+(N%10k) in constant time. 