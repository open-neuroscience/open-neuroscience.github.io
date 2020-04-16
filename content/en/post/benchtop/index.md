---
title: Bench top

authors: ['André Maia Chagas']
layout: post
categories: ['Hardware']
tags: ['Hardware']
---



Bench top tools (centrifuges, thermocyclers, etc)



<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Benchtop" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
