#!/usr/bin/node
const add_item = $('#add_item');
const ul = $('ul.my_list');

add_item.click(function fn () {
  ul.append('<li>Item</li>');
});
