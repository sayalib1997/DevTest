(function ($, app) {

$(function () {
    $(".modal").on("click", ".btn-cancel", function () {
        $(".modal").modal("hide");
    });

    $("#delete-modal").on("click", ".btn-primary", function (e) {
        e.preventDefault();
        var redirect_url = $(this).data("url");
        var url = $(this).attr("href");
        $.ajax({
            type: "DELETE",
            url: url
        }).done(function () {
            document.location = redirect_url;
        });
    });

});

})($, app);
