#!/usr/bin/node
let header = $('header') 
let red_header = $('#red_header') 

red_header.click(function fn() {
    header.addClass('red');
});
