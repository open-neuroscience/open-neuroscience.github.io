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
      <h2>Um banco de dados de projetos de ciência aberta relacionados a neurociência</h2>

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
     <h3>O que fazemos</h3>
     <div class='card card-curators'>
       <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-library-light.svg' alt=''>
       <h4>Curadoria de Projetos</h4>
       <p>Fazemos curadoria de projetos da Web e permitimos que criadores registrem seus próprios</p>
     </div>
<div class='card card-database'>
    <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-search-light.svg' alt=''>
    <h4>Banco de dados</h4>
    <p>Facilitamos aos pesquisadores a localização de projetos relevantes para ajudar em seus estudos</p>
    </div>
    <div class='card card-promoters'>
    <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-promote-light.svg' alt=''>
                <h4>Divulgação de projetos</h4>
                <p>Ajudamos desenvolvedores a promover seu trabalho por meio de nossa rede</p>
            </div>
        </div>
 "

  - block: markdown
    content:
      title:
      subtitle:
      
      text: "

 <div class='section' id='how-you-can-contribute'>
   <h3>Como contribuir</h3>
   
   <div class='card' id='contribute-on-open-issues'>
   <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-contribute-light.svg' alt=''>
   {{< cta cta_text=Ajude&nbsp;com&nbsp;Github&nbsp;issues
        cta_link=https://github.com/open-neuroscience/open-neuroscience.github.io/issues cta_new_tab='true' >}}
   </div>

   <div class='card add-a-project' id='add-a-project'>
   <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-addProject-light.svg' alt=''>
     {{< cta cta_text=Faça&nbsp;upload&nbsp;de&nbsp;projetos
        cta_link=https://forms.office.com/e/5QtUtMc3hw cta_new_tab='true' >}}
   </div>
   <!--
   <div class='card add-a-seminar' id='add-a-project'>
   <img src='https://raw.githubusercontent.com/open-neuroscience/resources/master/images/img-addProject-light.svg' alt=''>
     {{< cta cta_text=give&nbsp;a&nbsp;seminar
        cta_link=https://forms.office.com/e/5QtUtMc3hw cta_new_tab='true' >}}
  </div>
-->


</div>
"

  - block: portfolio
    headless: true
    id: projects
    content:
      title: Projetos
      subtitle: Quer adicionar o seu? Clique abaixo!
      text: "{{< cta cta_text=Adicione&nbsp;meu&nbsp;projeto
        cta_link=https://forms.office.com/e/5QtUtMc3hw cta_new_tab='true' >}}"
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
        - name: Eletrofisiologia Animal
          tag: Animal ephys
        - name: Backlog
          tag: Topic
        - name: Bancada
          tag: Benchtop
        - name: Comportamento
          tag: Behaviour
        - name: Calcium Imaging
          tag: Calcium Imaging
        - name: Computadores
          tag: Computers
        - name: Cluster de computadores
          tag: Computer clusters
        - name: Analise de dados
          tag: Data analysis
        - name: Repositórios de dados
          tag: Database
        - name: Estimulação elétrica
          tag: Electric
        - name: Fluorescência
          tag: Fluorescence
        - name: Hardware
          tag: Hardware
        - name: Neurociência humana
          tag: Human Neuroscience
        - name: Eletrofisiologia Humana
          tag: Human ephys
        - name: Microscópios
          tag: Microscope
        - name: Software para Microscópios
          tag: Microscopes software
        - name: Optogenetics
          tag: Optogenetics
        - name: Próteses
          tag: Prosthetics
        - name: Simulações
          tag: Simulation
        - name: Software
          tag: Software
        - name: Tutorials e portais de aprendizagem
          tag: Learning
        - name: Seminários World Wide Series
          tag: worldwideseries
        - name: Outros
          tag: Other
    design:
      columns: "1"
      view: masonry
      flip_alt_rows: true
  - block: portfolio
    headless: true
    id: seminars
    content:
      title: Seminários
      subtitle:  Realizamos uma série de seminários em que ferramentas e métodos podem ser apresentados por
        seus desenvolvedores!
      text: "{{< cta cta_text=Eu&nbsp;gostaria&nbsp;de&nbsp;dar&nbsp;uma&nbsp;palestra&nbsp;sobre&nbsp;o&nbsp;meu&nbsp;projeto 
        cta_link=https://forms.office.com/e/xmkaapqVDg cta_new_tab=true >}}"
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
      email: info@open-neuroscience.com
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
