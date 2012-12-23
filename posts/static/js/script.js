//Show caption on hover
$('ul li').hover(function() {
	$(this).find('.caption').addClass('showCaption');
}, function() {
	$(this).find('.caption').removeClass('showCaption');
});

//Show tag quantity on hover
$('#tags ul li').hover(function() {
	$(this).find('div').addClass('tagOver');
}, function() {
	$(this).find('div').removeClass('tagOver');
});

//Put each pointer in the center of its project title
$('.pointer').each(function() {
	var containerDOM = $(this).closest('li');
	var container = {
		width	: containerDOM.width(),
		height  : containerDOM.outerHeight()
	};
	
	var captionDOM = $(this).closest('.caption');

	var titleWidth = $(this).closest('li').find('.projectTitle').width();
	var newCaptionWidth;
	if(titleWidth < 200) {
		newCaptionWidth = container.width - titleWidth;
	} else {
		newCaptionWidth = 150;
	}

	$(captionDOM).width(newCaptionWidth);

	var pointerHeight = $(this).outerHeight();
	$(this).css('margin-top', (container.height / 2) - (pointerHeight / 2));
});

