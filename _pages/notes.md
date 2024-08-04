---
layout: archive
title: "Notes"
permalink: /notes/
author_profile: true
---

Here you can find my informal notes on academic papers, books, etc.

{% include base_path %}

{% for post in site.notes reversed %}
  {% include archive-single.html %}
{% endfor %}
