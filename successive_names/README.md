# Problem

Given an alphabet of $N$ symbols (here identified with integers), what is the chance that your $l$ closest friends have successive names? I.e. what is the chance the first symbols can be sorted to be
$$i,i+1,\dots,i+l-1,$$. 

In particular consider $N=5, l=4$.

## Calculation

$$\frac{(N-l+1)\cdot l!}{N^l}=0.0012079408984279263$$

Why? $N^l$ possible combinations, out of them we have $N-l+1$ choices for the first name and no other choices after that. In addition for each of these choices every permutation is a valid combination, so we get 
$\frac{(N-l+1)\cdot l!}{N^l}$, since there are $l!$ permutations for $l$ items

### In Reality
This assumes first symbols are independent (they are not) and each symbol is equally likely to appear.

In general the probability is
$$p=\sum_{i=1}^{N-l+1}\mathbb{P}(\alpha_1=i)\cdot l!$$
sadly, depending on the joint distribution over the first symbols, this has no closed form :(

## Simulation

Simulation result: $$p\approx 0.0012$$