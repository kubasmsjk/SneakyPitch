$(function() {
    var count = 0;
    var a = 0;
    $("#add-home-team").on('click', function () {
        a++;
        var source = $('.clone-home-team:first'),
            clone = source.clone();
        clone.find('label').hide();
        clone.find(':input').attr('name', function (i, val) {
            return val + count;
        });

        clone.insertBefore(this);


        count++;
    });
});(jQuery)

$(function() {
    var count = 0;
    var a = 0;
    $("#add-away-team").on('click', function () {
        a++;
        var source = $('.clone-away-team:first'),
            clone = source.clone();
        clone.find('label').hide();
        clone.find(':input').attr('name', function (i, val) {
            return val + count;
        });
        clone.insertBefore(this);


        count++;
    });
});(jQuery)