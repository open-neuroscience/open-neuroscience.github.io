---
title: A Cartesian Coordinate Robot for Dispensing Fruit Fly Food
date: 2020-07-10
authors: ['admin']
layout: post
categories: ['Hardware','Benchtop','Software']
tags: ['Hardware','Benchtop','Software']
---

"A mosca-da-fruta, ou Drosophila melanogaster, continua sendo um dos organismos modelo mais amplamente utilizados na pesquisa biomédica.
Embora escolhida por sua facilidade de manejo, a manutenção de um grande número de estoques de moscas, como é feito por muitos laboratórios, é uma tarefa que demanda muito trabalho.
Uma das  atividades que poderiam ser automatizadas, por exemplo, é a produção dos frascos de alimento para estes organismos, uma vez que os laboratorios geralmente precisam produzir vários milhares de frascos de alimento por semana para manter seus estoques.
O sistema apresentado aqui combina um robô de coordenadas cartesianas com uma bomba peristáltica. O design do robô é baseado em uma máquina CNC (controle numérico computadorizado) de acesso aberto, e utiliza atuadores de correia e polia para os eixos X e Y, e um atuador de fuso de avanço para o eixo Z.
O movimento da CNC e a operação da bomba peristáltica são controlados pelo grbl (https://github.com/gnea/grbl), um interpretador de G-code de acesso aberto e especifico, projetado para rodar diretament com este hardware, como um microcontrolador. O grbl é escrito em codigo C otimizado e roda diretamente em um Arduino. Um microcomputador ""Raspberry Pi"" é utilizado para gerar e transmitir as instruções em G-code para o grbl.
Uma tela sensível ao toque no Raspberry Pi fornece uma interface gráfica para o sistema. Embora o robô tenha sido construído com o propósito específico de encher frascos de alimento para as moscas, ele pode potencialmente ser utilizado para outras tarefas de manuseio de líquidos no laboratório."

## Autor(es)
Matt Wayland; Matthias Landgraf
## Links
https://github.com/WaylandM/fly-food-robot
## Video
https://doi.org/10.6084/m9.figshare.5175223.v1
***
Esse post foi criado por
Matt Wayland

E traduzido por
Steffen Keller
***
