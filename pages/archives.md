---
layout: default
---

<h1>Archives</h1>
<hr>
{% assign sorted_posts = site.posts | sort: 'date' %}
{% assign total_posts = sorted_posts.size %}

{% assign range_start = 1 %}
{% assign range_end = 100 %}
{% assign post_count = 0 %}

<!-- Flex container for the archive and the table of contents -->
<div class="archives-container">

  <!-- Main Archives List on the Left -->
  <div class="archives-list">
    {% for post in sorted_posts %}
      {% assign post_number = forloop.index %}

      {%- if post_number == range_start -%}
      <h2 class="custom-heading" id="range-{{ range_start }}">{{ range_start }}-{% if range_end <= total_posts %}{{ range_end }}{% else %}{{ total_posts }}{% endif %}</h2>
      {%- endif -%}

      <p><a href="{{ post.url }}">{{ post.title }}</a></p>

      {%- if post_number == range_end or post_number == total_posts -%}
        {% assign range_start = range_end | plus: 1 %}
        {% assign range_end = range_start | plus: 99 %}
      {%- endif -%}
    {% endfor %}
  </div>

  <!-- Table of Contents on the Right -->
  <div class="toc">
    <h4>Table of Contents</h4>
    <ul>
      {% assign range_start = 1 %}
      {% assign range_end = 100 %}
      
      {% for post in sorted_posts %}
        {% assign post_number = forloop.index %}

        {%- if post_number == range_start -%}
          <li><a href="#range-{{ range_start }}">{{ range_start }}-{% if range_end <= total_posts %}{{ range_end }}{% else %}{{ total_posts }}{% endif %}</a></li>
        {%- endif -%}

        {%- if post_number == range_end or post_number == total_posts -%}
          {% assign range_start = range_end | plus: 1 %}
          {% assign range_end = range_start | plus: 99 %}
        {%- endif -%}
      {% endfor %}
    </ul>
  </div>

</div>
