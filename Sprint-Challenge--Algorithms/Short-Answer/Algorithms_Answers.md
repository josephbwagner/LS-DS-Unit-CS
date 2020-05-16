#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) and I'll use an example to explain my answer. Assume n=10, while (a < 1000): a = 100 after the first iteration. For the second iteration, a = 200. So, even though the conditional for the while loop is a < n^3, a still increases at a rate of n^2. (n^3/n^2) = n = O(n).


b) O(nlog(n)) and I'll show this with a calculation of total operations. When n=10 sum results in 40. 10(log(10)) = 33.219. When n=20 sum results in 100, and 20(log(20))= 86.438. 


c) O(n) because the function will continue to be called recursively until bunnies==0, starting at n number of bunnies, so it is decrementing bunnies by 1.

## Exercise II


To determine the floor f from which dropped eggs won't be broken I would use binary search (assuming Euclidean geometry) and start on the middle floor. The runtime complexity of this method is O(log(n)), and if the building was 100 stories tall I would break, in the worst case scenario, 7 eggs before finding the floor f.
