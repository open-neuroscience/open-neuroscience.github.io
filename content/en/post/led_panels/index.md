---
title: LED Panels
authors: ['André Maia Chagas']

layout: post
categories: ['Visual']
tags: ['Visual']
---

In fields related to vision, stimulus presentation is always an issue due to slow refresh rates on commercial monitors/projectors. One way to circumvent this problem is to use LEDs  arranged in a matrix to present stimuli, that can be driven at much higher refresh rates, but have a worst resolution than monitors.

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">

      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "LED panels" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>


<p style="font-size: 0.9rem;font-style: italic;"><a href="https://www.flickr.com/photos/169136682@N02/32666262257">"CSR00089"</a><span>by <a href="https://www.flickr.com/photos/169136682@N02">tvluke_</a></span> is licensed under <a href="https://creativecommons.org/licenses/CC0/1.0/?ref=ccsearch&atype=html" style="margin-right: 5px;">CC0 1.0</a><a href="https://creativecommons.org/licenses/CC0/1.0/?ref=ccsearch&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;opacity: .7;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-cc0_icon.svg" /></a></p>
