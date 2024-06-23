---
title: "[in-progress] Quick refresher on Fokker-Planck"
collection: quant
type: "Post"
permalink: /quant/20240630_refresher_fokker_planck
date: 2024-06-30
---

These are my quick refresher notes on Fokker-Planck equation(s) for the evolution of a probability density over time. Like my notes on [Hamilton-Jacobi-Bellman](https://evnchw.github.io/quant/20240623_refresher_hjb), I focus on the main analytical aspects and intuitive understanding rather than the detailed proofs. I follow a similar format as well.

- I prioritize intuition/readability linking to references where appropriate.
- We will focus on the key equations, not go too deeply into proofs and may skip some parts for brevity.
- All feedback and corrections are welcome.

There are various ways to look at Fokker-Planck (see [1] for a fairly recent survey), but we are going to work through the view of Fokker-Planck sketched in [2] in the context of mean field games (MFG). Specifically:

1. We want to understand a particular forward Fokker-Planck equation that appears in mean field games
2. We want to characterise and understand the solution(s) to this equation

In other words, we go backward: we have the the FP equation for how a probability density evolves, and then we want to understand which probability densities can satisfy this. This is important because it tells us what our theoretical (distributional) boundaries are for modeling many-agent behavior in MFG and what is required to take advantage of MFG results.

# In a nutshell: the FP equation is a way to model the evolution of a probability density over time

From [Wikipedia](https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation):

> In statistical mechanics and information theory, the Fokker–Planck equation is a partial differential equation that describes the time evolution of the probability density function of the velocity of a particle under the influence of drag forces and random forces, as in Brownian motion. The equation can be generalized to other observables as well. The Fokker-Planck equation has multiple applications in information theory, graph theory, data science, finance, economics etc.

## The main result we want to show

The Fokker-Planck 

## Links to the Kolmogorov Forward/Backward Equations





# References

[1] Bogachev, Vladimir I., et al. Fokker–Planck–Kolmogorov Equations. Vol. 207. American Mathematical Society, 2022.

[2] [Ryzhik (2018)](https://math.stanford.edu/~ryzhik/STANFORD/MEAN-FIELD-GAMES/notes-mean-field.pdf)
