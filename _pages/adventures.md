---
layout: page
title: adventures
permalink: /adventures/
description: A growing collection of nice adventures.
---

{% assign sorted = site.adventures | sort: 'date' | reverse %}

{% for adventure in sorted %}
{% if adventure.redirect %}
<div class="adventure">
    <div class="thumbnail">
        <a href="{{ adventure.redirect }}" target="_ blank">
        {% if adventure.img %}
        <img src="{{ adventure.img }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ adventure.title }}</h1>
            <!-- <br/> -->
            <p>{{ adventure.description }}</p>
        </span>
        </a>
    </div>
</div>
{% else %}

<div class="adventure ">
    <div class="thumbnail">
        <a href="{{ adventure.url | prepend: site.baseurl | prepend: site.url }}">
        {% if adventure.img %}
        <img src="{{ adventure.img }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <span>
            <h1>{{ adventure.title }}</h1>
            <!-- <br/> -->
            <p>{{ adventure.description }}</p>
        </span>
        </a>
    </div>
</div>

{% endif %}

{% endfor %}
