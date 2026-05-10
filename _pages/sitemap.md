---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: false
---

{% include base_path %}

## Main pages

- [Home]({{ base_path }}/)
- [Publications]({{ base_path }}/publications/)
- [Talks]({{ base_path }}/talks/)
- [About me]({{ base_path }}/about-me/)
- [CV]({{ base_path }}/cv/)

## Publications

{% for post in site.publications reversed %}
- [{{ post.title }}]({{ base_path }}{{ post.url }})
{% endfor %}

## Talks

{% for post in site.talks reversed %}
- [{{ post.title }}]({{ base_path }}{{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}
