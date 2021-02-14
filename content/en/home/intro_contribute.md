+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 170  # Order that this section will appear.

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

@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Roboto", sans-serif;
}

body {
  background: #f8f9fa;
}

.main {
    max-width: 1136px;
    margin: auto;
    
    /* Background image */
    background-image: url('https://raw.githubusercontent.com/open-neuroscience/resources/master/images/on-watermark.svg');
    background-repeat: no-repeat;
    background-size: 30% auto;
    background-position: 95% 96%;
}



.logo img {
    height: 24px;
    cursor: pointer;
}

h3 {
  font-family: Roboto;
  font-style: normal;
  /* font-weight: bold; */
  font-size: 28px;
  line-height: 42px;
  color: #495057;
}

p {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 28px;
  color: #868e96;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  padding-left: 108px;
  padding-right: 108px;
  /* z-index: 2; */
  background-color: white;
  box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.25);
}
.nav-links ul {
  display: flex;
  justify-content: space-around;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 19px;
  color: #495057;
}
.nav-links a {
  text-decoration: none;
  color: #495057;
}
.nav-links li {
  margin-left: 24px;
  list-style: none;
}

.hamburger {
    display: none;
}

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

h4 {
    /* margin-top: 31px; */
    margin-bottom: 8px;
    font-style: normal;
    font-weight: 900;
    font-size: 14px;
    line-height: 23px;
    text-align: center;
    color: #495057;

}

.card p {
    font-weight: normal;
    font-size: 14px;
    line-height: 19px;
    text-align: center;
    color: #868E96;

}

.full-width {
    grid-column: 1 / 7;
    
}
.full-width2 {
    grid-column: 7 / 13;
}

.full-width2 h4{
    
    text-align: left;
}

.full-width2 p{
    
    text-align: left;
}


/* .full-width p {
    width: 566px;
    margin-top: 34px;
    margin-bottom: 34px;
    text-align: left;
} */

.full-width h4 {
    text-align: left;
}

button {
border-radius: 4px;
padding-left: 12px;
padding-right: 12px;
padding-top: 6px;
padding-bottom: 6px;
text-transform: uppercase;
font-weight: bold;
font-size: 12px;
margin-right: 8px;
font-variant: small-caps;
}

.primary {
    background: #3A9CED;
    color: white;
    border: 3px solid #3A9CED;
    
}

.secondary {
    background-color: white;
    color: #3A9CED;
    border: 2px solid #3A9CED;
}

#add-a-project {
    grid-column: 1 / 5;
}

#contribute-on-open-issues {
    grid-column: 5 / 9;
}

#get-in-touch form {
    grid-column: 1 / 9;
    margin-top: 19px;
}

label {
    font-size: 16px;
    line-height: 19px;
/* identical to box height */
    letter-spacing: -0.333333px;
    color: #818181;
}

input {
    display: block;
    height: 44px;
    width: 100%;
    margin-top: 7px;
    margin-bottom: 32px;
    border: 1px solid #C1C1C1;
    border-radius: 4px;
}

textarea {
    width: 100%;
    margin-top: 7px;
    margin-bottom: 20px;
    border: 1px solid #C1C1C1;
    border-radius: 4px;
}

input #message {
    height: 300px;
}

.full-width-container {
    
    width: 100%;
    /* 6 columns inside a component with a 1136px (wide) grid (36px padding excluded */
    grid-template-columns: repeat(6, 1fr); 
    /* 16px gap = 16/1136 = 1.408450704% */
    grid-column-gap: 1.408450704%;
    margin-bottom: 24px;
}

.full-width p {
    margin: 0;
    text-align: left;
    grid-column: 1 / 4;
}


.full-width-container img {
    
    width: 100%;
    height: 200px;
    object-fit: cover;
    margin: 0;
    border-radius: 4px;
    justify-items: stretch;
    margin-bottom: 11px;
}

.full-width-container h4 {
    margin-top: 0;
    grid-column: 1 / 4;
}

.centered {
    margin: 0;
  -ms-transform: translate(-50%, -50%);

}

@media screen and (max-width: 770px) {
    /* do something about the nav bar */
    .hamburger {
        display: block;
        cursor: pointer;
    }
    .nav-links a {
        display: none;
    }


    /* make sure contribute card buttons stay in one line  */
    #add-a-project {
        grid-column: 1/6;
    }

    #contribute-on-open-issues {
        grid-column: 6/11;
    }
}

/* MOBILE LAYOUT */

@media screen and (max-width: 600px){
    .nav {
        padding: 20px;
    }

    .section {
        margin-left: 24px;
        margin-right: 24px;
    }

    .hero h2 {

        font-size: 32px;

    }
    .card-curators {
        grid-column: 1/13;
    }

    .card-database {
        grid-column: 1/13;
    }

    .card-promoters {
        grid-column: 1/13;
    }

    .full-width {
        grid-column: 1/13;
    }
    .full-width2 {
        grid-column: 1/13;
    }

    .add-a-project {
        grid-column: 1/13;
    }
    .contribute-on-open-issues {
        grid-column: 1/13;
    }

    #get-in-touch form {
        grid-column: 1/13;
        margin-bottom: 200px;
    }


    .main {
        max-width: 1136px;
        margin: auto;
        
        /* Background image */
        background-image: url('https://raw.githubusercontent.com/open-neuroscience/resources/master/images/on-watermark.svg');
        background-repeat: no-repeat;
        background-size: 50% auto;
        background-position: 50% 100%;

    }

    .section h3 {
        text-align: center;
    }
    
}

@media screen and (max-width: 979px) {
    .single-line {
        height: 46px;
    }
}

</style>

 <div class="section" id="how-you-can-contribute">
   <h3>How you can contribute</h3>

 
   <div class="card add-a-project" id="add-a-project">
   <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-addProject-light.svg" alt="">
   <button class="primary centered" onclick="window.location.href='https://bit.ly/uploadON';">add a project</button>
 </div>
    
 <div class="card" id="contribute-on-open-issues">
  <img src="https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-contribute-light.svg" alt="">
  <button class="primary centered" onclick="window.location.href='https://github.com/open-neuroscience/open-neuroscience.github.io/issues';"> work on open issues</button>
 </div>
        

</div>


