jQuery(document).ready(function () {
    $("#loginBtn").click(function () {
            $(".one").css("display", "none")
            $(".two").css("display", "block")
            let main_background = document.getElementById("top-content").getAttribute('data-value');
            $('.top-content').backstretch(main_background);
            let contact_background = document.getElementById("section-2").getAttribute('data-value');
            $('.section-2-container').backstretch(contact_background);
    });
});
