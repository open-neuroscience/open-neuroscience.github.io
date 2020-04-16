---
title: Computer clusters
authors: ['André Maia Chagas']

layout: post
categories: ['Hardware']
tags: ['Hardware']
---
With the advance of miniaturization, computers have been downsized to credit card sizes being very cheap (50+ dollars), which allows for some DIY computing clusters and even for a whole supercomputer to be packed in a card sized layout, below are some examples:


<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Computer clusters" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>

<p style="font-size: 0.9rem;font-style: italic;"><a href="https://www.flickr.com/photos/38308378@N05/5187929357">"Closeted cluster"</a><span>by <a href="https://www.flickr.com/photos/38308378@N05">J. Paxon Reyes</a></span> is licensed under <a href="https://creativecommons.org/licenses/by-nc/2.0/?ref=ccsearch&atype=html" style="margin-right: 5px;">CC BY-NC 2.0</a><a href="https://creativecommons.org/licenses/by-nc/2.0/?ref=ccsearch&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;opacity: .7;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-by_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nc_icon.svg" /></a></p>
