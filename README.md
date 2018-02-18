[![Build Status](https://travis-ci.org/pozar87/apts.svg?branch=master)](https://travis-ci.org/pozar87/apts) [![Join the chat at https://gitter.im/apts-core/Lobby](https://badges.gitter.im/apts-core/Lobby.svg)](https://gitter.im/apts-core/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# APTS - AstroPhotography Tool Set

Set of tools for automatic astrophotography images acquisition and processing. This project has started as **Astro-Pożar Tool Set**.

## Features
* Register your optical equipment and compute all possible magnifications (including DSLR)
* Plot avaliable zoom and fov
* Register locations and check the weather at night - acording to configurable tresholds 
* Plot summary of weather conditions on a chart
* Send email with notification about weather

## Configuration 

Create a *~/.config/apts/apts.ini* file with following content:

```
[weather]
# Settings for weather API 
api_url = <api_url>
api_key = <api_key>

[notification]
# Gmail address
email_address = <email>
# Gmail pass - use google application passwords!
email_password = <password>

```
