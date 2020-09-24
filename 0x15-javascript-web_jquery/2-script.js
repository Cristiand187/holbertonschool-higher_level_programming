#!/usr/bin/node
let header = $('header') 
let red_header = $('#red_header') 

red_header.click(function () {
    header.css('color', '#FF0000');
});
