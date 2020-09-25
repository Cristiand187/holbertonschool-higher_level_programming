#!/usr/bin/node
const update_header = $('#update_header');
const header = $('header');

update_header.click(function fn () {
  header.text('New Header!!!');
});
