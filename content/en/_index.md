---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle:
      text: "      
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
      <div class='hero'>
      <div class='smiley'>
      <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/on-logo-lightBlue.svg' alt=''>
      </div>
      <h2>We are a user-driven database of open neuroscience projects</h2>
      </div>
    "
    design:
      # Choose an optional background color, gradient, image, or video
      background:
        color: '#3a9ced'
        text_color_light: true
  - block: markdown
    content:
      title:
      subtitle:
      
      text: "<style>
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
<div class='section' id='what-we-do'>
     <h3>What we do</h3>
     <!-- <div class='container'> -->
     <div class='card card-curators'>
       <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-library-light.svg' alt=''>
       <h4>Project curators</h4>
       <p>We curate projects from the web and allow creators to register their own</p>
     </div>
<div class='card card-database'>
    <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-search-light.svg' alt=''>
    <h4>Extensive database</h4>
    <p>We make it easy for researchers to find relevant projects to help their studies</p>
    </div>
    <div class='card card-promoters'>
    <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-promote-light.svg' alt=''>
                <h4>Project promoters</h4>
                <p>We help creators and promote their work through our network</p>
            </div>
        </div>

      </style>  "


  - block: markdown
    content:
      title:
      subtitle:
      
      text: "
<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
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
 <div class='section' id='how-you-can-contribute'>
   <h3>How you can contribute</h3>
   <div class='card add-a-project' id='add-a-project'>
   <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-addProject-light.svg' alt=''>
     {{< cta cta_text=Upload&nbsp;a&nbsp;project
        cta_link=https://bit.ly/uploadON cta_new_tab='true' >}}
 </div>    
 <div class='card' id='contribute-on-open-issues'>
  <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-contribute-light.svg' alt=''>
  {{< cta cta_text=Work&nbsp;on&nbsp;open&nbsp;issues
        cta_link=https://github.com/open-neuroscience/open-neuroscience.github.io/issues cta_new_tab='true' >}}
 </div>
</div>
"

  - block: portfolio
    headless: true
    id: projects
    content:
      title: Projects
      subtitle: Want to add your own? Click below!
      text: "{{< cta cta_text=Add&nbsp;my&nbsp;project
        cta_link=https://forms.gle/T7FVzhWEq9CToWUN8 cta_new_tab='true' >}}"
      filters:
        folders:
          - post
        kinds:
          - page
      sort_by: Date
      sort_ascending: false
      default_button_index: 0
      buttons:
        - name: All
          tag: "*"
        - name: Deep Learning
          tag: Deep Learning
        - name: Animal electrophysiology
          tag: Animal ephys
        - name: Backlog
          tag: Topic
        - name: Benchtop
          tag: Benchtop
        - name: Behaviour
          tag: Behaviour
        - name: Calcium Imaging
          tag: Calcium Imaging
        - name: Computers
          tag: Computers
        - name: Computer Clusters
          tag: Computer clusters
        - name: Data Analysis
          tag: Data analysis
        - name: Data Repositories
          tag: Database
        - name: Electric Stimulation
          tag: Electric
        - name: Fluorescence
          tag: Fluorescence
        - name: Hardware
          tag: Hardware
        - name: Human Neuroscience
          tag: Human Neuroscience
        - name: Human electrophysiology
          tag: Human ephys
        - name: Microscopes
          tag: Microscope
        - name: Microscopes software
          tag: Microscopes software
        - name: Optogenetics
          tag: Optogenetics
        - name: Prosthetics
          tag: Prosthetics
        - name: Simulations
          tag: Simulation
        - name: Software
          tag: Software
        - name: Tutorials and learning portals
          tag: Learning
        - name: World Wide Series Seminars
          tag: worldwideseries
        - name: Other
          tag: Other
    design:
      columns: "1"
      view: masonry
      flip_alt_rows: true
  - block: portfolio
    headless: true
    id: seminars
    content:
      title: Seminars
      subtitle: We run a seminar series where tool and methods can be showcased by
        their developers!
      text: "{{< cta cta_text=I&nbsp;would&nbsp;like&nbsp;to&nbsp;give&nbsp;a&nbsp;seminar
        cta_link=https://forms.gle/vhUBTwygFnRA1B7y9 cta_new_tab=true >}}"
      filters:
        folders:
          - post
        tags:
          - worldwideseries
        kinds:
          - page
      sort_by: Date
      sort_ascending: false
      default_button_index: 0
    design:
      columns: "1"
      view: masonry
      flip_alt_rows: true
  - block: people
    id: team
    content:
      title: Meet the Team
      user_groups:
        - Current
        - Previous collaborators
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_social: true
      show_interests: true
      show_role: true
      show_organizations: true
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle: ""
      text: ""
      email: openeuroscience@gmail.com
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: DM Me
          link: https://x.com/openneurosci
      autolink: true
      form:
        provider: formspree
        formspree:
          id: "openeuroscience@gmail.com"
        netlify:
          captcha: false
    design:
      columns: "1"
---