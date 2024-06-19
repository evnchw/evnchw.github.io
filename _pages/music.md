---
layout: archive
title: "Music"
permalink: /music/
author_profile: true
---

Here you can find my writings on a range of music topics, from music itself to quantitative work in music.

{% include base_path %}

{% for post in site.quant reversed %}
  {% include archive-single.html %}
{% endfor %}
