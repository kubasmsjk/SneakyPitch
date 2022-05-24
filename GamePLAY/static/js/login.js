jQuery(document).ready(function () {
    const zalogowany = false;
    if (zalogowany) {
        $(".one").css("display", "none")
        $(".two").css("display", "block")
    }
    $("#loginBtn").click(function () {
        $(".one").css("display", "none")
        $(".two").css("display", "block")
    });
    $("#registerBtn").click(function () {
        $(".one").css("display", "block")
        $(".two").css("display", "none")
    });
});