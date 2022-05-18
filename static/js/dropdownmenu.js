jQuery(document).ready(function () {
    $(".more").click(function () {
        $('.details-list').toggle();
        $(".footer-container").css("bottom", "auto")
        $(".more").off().on('click', function () {
            $('.details-list').toggle();
            $(".footer-container").css("bottom", "0")
        });
    });




});


