---

title: Electrophysiology
authors: ['André Maia Chagas']
layout: post
categories: ['Hardware']
tags: ['Hardware']

---


Electrophysiology systems are developed to record very small signals (action potentials or local field potentials) neurons use to communicate. Normally they cost in the range of 50 up to hundreds of thousands of euros, which make them prohibitive for most labs and also confined to lab space

---

## Animal electrophysiology

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Animal ephys" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>


---


## Human electrophysiology

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Human ephys" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
