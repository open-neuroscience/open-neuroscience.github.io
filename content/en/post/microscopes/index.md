---
title: Microscopes
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
          {% if category == "Microscope" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>

In this section are listed amazing projects that actually managed to build entire microscopes from scratch, or modify them for specific needs. Most of the times drastically reducing the implementation costs of such devices.

[Scanning electron microscope.](http://openeuroscience.wordpress.com/hardware-projects/scanning-electron-microscope/ "Scanning electron microscope")

[Ten dollar assembly to turn your smartphone into a microscope.](http://openeuroscience.wordpress.com/hardware-projects/microscopy-hardware/10-microscope-using-a-smartphone/ "10$ microscope using a smartphone")

[DIY adaptations to enhance a stereo microscope.](http://openeuroscience.wordpress.com/hardware-projects/microscopy-hardware/stereo-microscope-the-steve-richardson-way/ "Stereo microscope – The Steve Richardson way.")

[OpenStage](http://openeuroscience.com/hardware-projects/microscopy-hardware/openstage/ "OpenStage")

<p style="font-size: 0.9rem;font-style: italic;"><a href="http://www.flickr.com/photos/34251884@N00/341191827">""</a><span>by <a href="http://www.flickr.com/photos/34251884@N00">Demonicuss</a></span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/2.0/?ref=ccsearch&atype=html" style="margin-right: 5px;">CC BY-NC-ND 2.0</a><a href="https://creativecommons.org/licenses/by-nc-nd/2.0/?ref=ccsearch&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;opacity: .7;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-by_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nd_icon.svg" /></a></p>
