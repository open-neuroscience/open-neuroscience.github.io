---
title: Software
authors: ['André Maia Chagas']
layout: post

categories: ['Topic']
tags: ['Topic']
---



But what is open source software? and why should I use it?

-To put it in a short, short way, open source software are pieces programs that are free (as in liberty). Anyone can look at the program's code, study it, make custom changes to it or even improve it, finding bugs and so on.

Open source software is present in almost all areas of computation, from wide use operational systems (such as [Linux](http://en.wikipedia.org/wiki/Linux), [FreeBSD](http://www.freebsd.org/about.html)), 3D modelling ([Blender](http://www.blender.org/), [Freecad](http://sourceforge.net/projects/free-cad/)), office suites ([Open office](http://www.openoffice.org/), [Libre office](http://www.libreoffice.org/#0)), vectorized image suites ([Inkscape](http://inkscape.org/)), photoshop like suites ([Gimp](http://www.gimp.org/)), programming languages with scientific computing add-ons ([python](http://www.python.org/) and [numPy](http://www.numpy.org/)), high level programming languages for numerical computation ([GNU Octave](http://www.gnu.org/software/octave/)). Basically for most commercially available piece of software out there, there is a free, similar or even better quality piece of open software a click of a button away.

### software

<section class="blog">
  <div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
      {% for page in site.pages %}
        {% for category in page.categories %}
          {% if category == "Software" %}
            {% include card_page.html %}
          {% endif %}
        {% endfor %}
      {% endfor %}


    </div>
  </div>
</section>
