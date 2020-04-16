---
title: Data Analysis
authors: ['André Maia Chagas']

layout: post
categories: ['Software']
tags: ['Software']
---


In this section you&#8217;ll find tools for data analysis, such as statistical packages and tools for data visualization.

Some of the projects are:

[GNU Octave](http://openeuroscience.wordpress.com/software/data-analysis-and-visualization/gnu-octave/ "GNU Octave")

[R statistics software](http://openeuroscience.wordpress.com/software/statistics-r/ "Statistics: The R environment")

[Neural Ensemble](http://openeuroscience.wordpress.com/software/neuralensemble/ "NeuralEnsemble")

[FieldTrip: EEG and MEG toolbox](http://openeuroscience.wordpress.com/software/eeg-meg-toolbox-fieldtrip/ "EEG MEG Toolbox – Fieldtrip")

[Brain Browser](http://openeuroscience.wordpress.com/software/data-analysis-and-visualization/brainbrowser/)


<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Data analysis" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
