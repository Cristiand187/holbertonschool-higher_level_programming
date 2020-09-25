#!/usr/bin/node
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, data => {
  $('#hello').append(`<p>${data.hello}</p>`);
});
