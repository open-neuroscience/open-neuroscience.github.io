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
      
      text: "
<div class='section' id='what-we-do'>
     <h3>What we do</h3>
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
 "


  - block: markdown
    content:
      title:
      subtitle:
      
      text: "

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