  var $animate = $('.animate');

  $animate.waypoint(function (direction) {
    if (direction == 'down') {
        $animate.addClass('js-animated');
    }else {
        $animate.removeClass('js-animated');
    }
  }, {offset:'90%'});