+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 100  # Order that this section will appear.

#title = 
#subtitle = 

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  color = "#3a9ced"
  
  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"
  
  # Background image.
  #image = "headers/bubbles-wide.jpg"  # Name of image in `static/img/`.
  #image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
  #image_size = "cover"  #  Options are `cover` (default), `contain`, or `actual` size.
  #image_position = "center"  # Options include `left`, `center` (default), or `right`.
  #image_parallax = true  # Use a fun parallax-like fixed background effect? true/false

  # Text color (true=light or false=dark).
  #text_color_light = true

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]



[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""

### this is alert note that should be used in the markdown part of the document
#{{% alert note %}}
#This homepage section is an example of adding [elements](https://sourcethemes.com/academic/docs/writing-markdown-latex/) to #the [*Blank* widget](https://sourcethemes.com/academic/docs/widgets/).

#Backgrounds can be applied to any section. Here, the *background* option is set give an *image parallax* effect.
#{{% /alert %}}


+++

<style>

.hero {
    display: grid;
    grid-template-columns: repeat(12, 7.042253521%);
    grid-column-gap: 1.408450704%;
    /* margin: auto 65px ; */

  /* z-index: 1; */
  /* height: 417px; */
  background-color: #3a9ced;
  /* padding-left: 108px; */
  /* padding-top: 100px; */
  padding-bottom: 112px;
}

.smiley {
    grid-column: 1 / 13 ;
    margin: auto;
    margin-top: 48px;
}

.hero h2 {
    grid-column: 3 / 11 ;
    text-align: center;
  font-style: normal;
  font-weight: normal;
  font-size: 40px;
  line-height: 47px;
  color: #ffffff;
  /* max-width: 695px; */
  margin-top: 36px;
}

</style>


<div class="hero">
  <div class="smiley">
  <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/on-logo-lightBlue.svg" alt="">
  </div>
        
  <h2>We are a user-driven database of open neuroscience projects</h2>
        
</div>
  
  
 
