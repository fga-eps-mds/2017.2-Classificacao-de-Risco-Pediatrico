  var $animate = $('.animate');

  $animate.waypoint(function (direction) {
    if (direction == 'down') {
        $animate.addClass('fadeInUp');
    }else {
        $animate.removeClass('fadeInUp');
    }
  }, {offset:'90%'});