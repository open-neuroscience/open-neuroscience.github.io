+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 150  # Order that this section will appear.

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
  color = ""
  
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

.section {
    display: grid;
    grid-template-columns: repeat(12, 7.042253521%);
    grid-column-gap: 1.408450704%;
    margin: auto 65px ;
    margin-top: 34px;
  
}

.section h3 {
    grid-column: 1 / 12;
    /* font-weight: regular; */
    font-size: 20px;
    line-height: 40px;
}

.card-curators {
    grid-column: 1 / 5;
}

.card-database {
    grid-column: 5 / 9;
}

.card-promoters{
    grid-column: 9 / 13;
}



.card {
  padding: 24px;
  background: #ffffff;
  box-sizing: border-box;
  box-shadow: 0px 8px 10px rgba(2, 3, 3, 0.03), 0px 3px 14px rgba(2, 3, 3, 0.02), 0px 5px 5px rgba(2, 3, 3, 0.04);
  border-radius: 8px;
  margin-top: 19px;
}

.card img {
    display: block;
    margin: auto;
    margin-bottom: 24px;
    width: 60%
    

}
</style>
  
  
<div class="section" id="what-we-do">
     <h3>What we do</h3>
     <!-- <div class="container"> -->
     <div class="card card-curators">
       <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-library-light.svg" alt="">
       <h4>Project curators</h4>
       <p>We curate projects from the web and allow creators to register their own</p>
     </div>
<div class="card card-database">
    <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-search-light.svg" alt="">
    <h4>Extensive database</h4>
    <p>We make it easy for researchers to find relevant projects to help their studies</p>
    </div>
    <div class="card card-promoters">
    <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-promote-light.svg" alt="">
                <h4>Project promoters</h4>
                <p>We help creators and promote their work through our network</p>
            </div>
        </div>

