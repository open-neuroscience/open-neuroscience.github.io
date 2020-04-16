---
title: Computers
authors: ['André Maia Chagas']
layout: post

categories: ['Hardware']
tags: ['Hardware']
---

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Computers" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>

&nbsp;

Single board computers are small all-in-one computers, normally equipped with an ARM processor (due to their low power consumption) the same used on most of the smartphones nowadays. They usually run a linux distribution of an SD card and have most of the connectivity of a desktop computer (Ethernet, HDMI video, USB ports, audio out). Due to their small size and cost, are great for customization and mobile applications and some of them even feature microcontroller properties, being able to input/output TTL pulses.



[Raspberry Pi](http://openeuroscience.com/hardware-projects/computers/raspberry-pi/ "Raspberry Pi")

[Beagle boards](http://openeuroscience.com/hardware-projects/computers/the-beagles/ "The “Beagles”")


<p style="font-size: 0.9rem;font-style: italic;"><a href="http://www.flickr.com/photos/7266674@N06/2297274671">"RAM Sticks"</a><span>by <a href="http://www.flickr.com/photos/7266674@N06">Onio-n</a></span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/2.0/?ref=ccsearch&atype=html" style="margin-right: 5px;">CC BY-NC-ND 2.0</a><a href="https://creativecommons.org/licenses/by-nc-nd/2.0/?ref=ccsearch&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;opacity: .7;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-by_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nd_icon.svg" /></a></p>
