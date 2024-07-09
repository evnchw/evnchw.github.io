---
layout: archive
title: "Other"
permalink: /other/
author_profile: true
---

This is a home for my other writings.

{% include base_path %}

{% for post in site.other reversed %}
  {% include archive-single.html %}
{% endfor %}
