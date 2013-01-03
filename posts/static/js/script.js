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
function sizeCaptions() {
	$('.pointer').each(function() {
		var containerDOM = $(this).closest('li');
		var container = {
			width	: containerDOM.width(),
			height  : containerDOM.outerHeight()
		};
		
		var captionDOM = $(this).closest('.caption');

		var titleWidth = $(this).closest('li').find('.projectTitle').width();
		var newCaptionWidth;
		var captionDiff = container.width - titleWidth;

		if(captionDiff > 100) {
			newCaptionWidth = captionDiff;
		} else {
			newCaptionWidth = 150;
		}
		$(captionDOM).width(newCaptionWidth);

		var pointerHeight = $(this).outerHeight();
		$(this).css('margin-top', (container.height / 2) - (pointerHeight / 2));
	});

	//Extends white border when there's only a couple posts
	if($(window).width() > 699) {
		$('#left').css('min-height', $('#right').height() + 'px');
	} else {
		$('#left').css('min-height', 0);
	}
}

sizeCaptions();
$(window).resize(function() {
	sizeCaptions();
});

//separate tags by comma in detail view
var tag_list = $('.detail .tags li').text();
var tags = tag_list.split(',');
$('.detail .tags li').remove();
for (tag in tags) {
	$('.detail .tags').append('<li>' + tags[tag] + '</li>');
}

