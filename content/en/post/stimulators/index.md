---
title: Stimulators
authors: ['André Maia Chagas']

layout: post
categories: ['Hardware']
tags: ['Hardware']
---

In here are different type of stimulators. Visual (monitors, led panels), electric(tDCS, microstimulators), etc

---

## Electric

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Electric" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>


---


## Visual

In fields related to vision, stimulus presentation is always an issue due to slow refresh rates on commercial monitors/projectors. One way to circumvent this problem is to use LEDs  arranged in a matrix to present stimuli, that can be driven at much higher refresh rates, but have a worst resolution than monitors.

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Visual" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>

---

## optogenetics

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Visual" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
