---
title: Simulations
authors: ['André Maia Chagas']

layout: post
categories: ['Software']
tags: ['Software']
panels_data:
  - 'a:3:{s:7:"widgets";a:1:{i:0;a:5:{s:6:"filter";s:1:"1";s:4:"text";s:746:"<p>Ever thought about playing with a virtual worm? or interacting with a simulated bee brain? Sounds interesting no? These are just two projects that offer anyone the opportunity to play around with brain/neuronal simulations and models. Some of them are hardware based, and some completely software:</p><p><a href="http://openeuroscience.com/open-source-simulations-and-models/open-worm/">OpenWorm</a></p><p><a href="http://openeuroscience.com/open-source-simulations-and-models/green-brain/">GreenBrain</a></p><p><a href="http://openeuroscience.com/open-source-simulations-and-models/neuronsneuronsneurons/">Neurons,Neurons,Neurons</a></p><p><a href="http://openeuroscience.com/open-source-simulations-and-models/big-neuron/">Big Neuron</a></p>";s:5:"title";s:0:"";s:4:"type";s:6:"visual";s:11:"panels_info";a:7:{s:5:"class";s:31:"SiteOrigin_Widget_Editor_Widget";s:3:"raw";b:0;s:4:"grid";i:0;s:4:"cell";i:0;s:2:"id";i:0;s:9:"widget_id";s:36:"ef443d2e-a939-45a1-a8dc-14a6846c0356";s:5:"style";a:0:{}}}}s:5:"grids";a:1:{i:0;a:2:{s:5:"cells";i:1;s:5:"style";a:0:{}}}s:10:"grid_cells";a:1:{i:0;a:4:{s:4:"grid";i:0;s:5:"index";i:0;s:6:"weight";i:1;s:5:"style";a:0:{}}}}'
---

<div id="pl-1067"  class="panel-layout" >
  <div id="pg-1067-0"  class="panel-grid panel-no-style" >
    <div id="pgc-1067-0-0"  class="panel-grid-cell" >
      <div id="panel-1067-0-0-0" class="so-panel widget widget_sow-editor panel-first-child panel-last-child" data-index="0" >
        <div class="so-widget-sow-editor so-widget-sow-editor-base">
          <div class="siteorigin-widget-tinymce textwidget">
            <p>
              Ever thought about playing with a virtual worm? or interacting with a simulated bee brain? Sounds interesting no? These are just two projects that offer anyone the opportunity to play around with brain/neuronal simulations and models. Some of them are hardware based, and some completely software:
            </p>

            <p>
              <a href="http://openeuroscience.com/open-source-simulations-and-models/open-worm/">OpenWorm</a>
            </p>

            <p>
              <a href="http://openeuroscience.com/open-source-simulations-and-models/green-brain/">GreenBrain</a>
            </p>

            <p>
              <a href="http://openeuroscience.com/open-source-simulations-and-models/neuronsneuronsneurons/">Neurons,Neurons,Neurons</a>
            </p>

            <p>
              <a href="http://openeuroscience.com/open-source-simulations-and-models/big-neuron/">Big Neuron</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>



<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Simulation" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
