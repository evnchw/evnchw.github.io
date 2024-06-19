---
layout: archive
title: "Quant"
permalink: /quant/
author_profile: true
---

Here you can find my writings on a range of quant topics, mostly informal and less academic.

DEBUG:
{{ site }}
{{ site.quant }}


{% include base_path %}

{% for post in site.quant reversed %}
  {% include archive-single.html %}
{% endfor %}
