---
layout: archive
title: "Research"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

In progress:

<ul>
    <li><i>Mean field congestion in dry bulk shipping</i>, with <a href="https://sylviatian.github.io/research/">Sylvia Tian</a></li>
</ul>

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
