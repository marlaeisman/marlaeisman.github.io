---
layout: default
title: "Blog"
permalink: /blog/
---

# Blog

<div class="projects-scroll">
{% for post in site.data.blog %}
  <div class="project-card">
  <img src="{{ post.image }}" alt="{{ post.title }}" />
  <h3>{{ post.title }}</h3>
  <p>{{ post.summary }}</p>
    <div class="project-meta">
      <span class="project-date">{{ post.date }}</span>
  <a class="read-more" href="{{ post.url | relative_url }}">Read →</a>
    </div>
  </div>
{% endfor %}
</div>
