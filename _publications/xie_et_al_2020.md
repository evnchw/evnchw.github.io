---
title: "How to Measure Your App: A Couple of Pitfalls and Remedies in Measuring App Performance in Online Controlled Experiments"
collection: publications
permalink: /publication/xie_et_al_2020
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2020-11-29
venue: 'WSDM 2021: Proceedings of the 14th ACM International Conference on Web Search and Data Mining'
paperurl: 'https://dl.acm.org/doi/abs/10.1145/3437963.3441742'
citation: 'Xie, Yuxiang, et al. "How to measure your app: a couple of pitfalls and remedies in measuring app performance in online controlled experiments." Proceedings of the 14th ACM International Conference on Web Search and Data Mining. 2021.'
---

# Abstract

Effectively measuring, understanding, and improving mobile app performance is of paramount importance for mobile app developers. Across the mobile Internet landscape, companies run online controlled experiments (A/B tests) with thousands of performance metrics in order to understand how app performance causally impacts user retention and to guard against service or app regressions that degrade user experiences. To capture certain characteristics particular to performance metrics, such as enormous observation volume and high skewness in distribution, an industry-standard practice is to construct a performance metric as a quantile over all performance events in control or treatment buckets in A/B tests. In our experience with thousands of A/B tests provided by Snap, we have discovered some pitfalls in this industry-standard way of calculating performance metrics that can lead to unexplained movements in performance metrics and unexpected misalignment with user engagement metrics. In this paper, we discuss two major pitfalls in this industry-standard practice of measuring performance for mobile apps. One arises from strong heterogeneity in both mobile devices and user engagement, and the other arises from self-selection bias caused by post-treatment user engagement changes. To remedy these two pitfalls, we introduce several scalable methods including user-level performance metric calculation and imputation and matching for missing metric values. We have extensively evaluated these methods on both simulation data and real A/B tests, and have deployed them into Snap's in-house experimentation platform.
