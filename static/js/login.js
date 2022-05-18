jQuery(document).ready(function () {
    const zalogowany = false;
    if (zalogowany) {
        $(".one").style.display = "none";
        $(".two").style.display = "block";
        console.log("witam33")
    }
    $(".loginBtn").click(function () {
        $(".one").style.display = "none";
        $(".two").style.display = "block";
        console.log("witam")
    });
    $(".loginBtnn").click(function () {
        $(".one").style.display = "block";
        $(".two").style.display = "none";
        console.log("wita2m")
    });
});