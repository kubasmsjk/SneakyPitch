jQuery(document).ready(function () {
    $("#loginBtn").click(function () {
        $(".one").css("display", "none")
        $(".two").css("display", "block")
    });
    $("#registerBtn").click(function () {
        $(".one").css("display", "block")
        $(".two").css("display", "none")
    });
});