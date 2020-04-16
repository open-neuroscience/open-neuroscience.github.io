---
title: Learning

authors: ['André Maia Chagas']
layout: post
categories: ['Topic']
tags: ['Topic']
---


Learning resources.



<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Learning" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
