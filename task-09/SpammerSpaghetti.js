function spam() {
  document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = "Hi";
	$('.im_submit').trigger('mousedown');	
}

setInterval(spam, 1000);
