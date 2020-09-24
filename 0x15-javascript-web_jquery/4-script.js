#!/usr/bin/node
const header = $('header');
const toggle_header = $('#toggle_header');

toggle_header.click(function fn () {
  header.toggleClass('red green');
});
