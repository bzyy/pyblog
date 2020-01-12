$(document).ready(function(){
     $(window).scroll(function () {
            if ($(this).scrollTop() > 50) {
                $('#back-to-top').fadeIn();
            } else {
                $('#back-to-top').fadeOut();
            };
            if ($(window).scrollTop() == $("header").height() || $(window).scrollTop() >= $("header").height()) {
             $('#menu').addClass('sps');
            } else {
                $('#menu').removeClass('sps');
            };
        });
        // scroll body to 0px on click
        $('#back-to-top').click(function () {
            $('body,html').animate({
                scrollTop: 0
            }, 600);
            return false;
        });
        $( '#navbars-blog a' ).on('click', function () {
            $('#navbars-blog').find('li.active').removeClass('active');
            $(this).parent('li').addClass('active');
        });

});