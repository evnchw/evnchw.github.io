---
title: "[under construction] Stochastic orders of magnitude"
collection: quant
type: "Post"
permalink: /quant/20240714_stochastic_orders_of_magnitude
date: 2024-07-14
---

In your core compute science curriculum, you likely studied computational "Big-O" notation: orders of magnitude to compare the efficiency of computer programs. [(Wiki)](https://en.wikipedia.org/wiki/Big_O_notation)

> In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem. Big O notation is also used in many other fields to provide similar estimates.

I'll assume you are familiar with this concept (you can study it many places online). If not, the basic idea is that you characterize the runtime or space of an algorithm by how many operations it performs. For instance, if you have an algorithm that simply iterates through an $$N$$-length list a fixed number of times, we call this $$O(N)$$ runtime; if you compare each element to every other element that requires $$N^2=N \times N$$ operations and so is $$O(N^2)$$, etc.


> Given an algorithm, what is the growth rate of its time and/or space requirements?

Now in econometric graduate school, we studied 

Now in econometrics graduate school, we covered the *probabilistic* approach toward this, informally called *stochastic orders of magnitude.* Fundamentally the question is:

> Given a (possibly stochastic) sequence of numbers

