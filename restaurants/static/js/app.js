(function($) {
    $( ".comment .expand" ).click(function() {
        var sub_comment = $(this).parents('.comment').find('.sub-comment-form');
        if ($(this).hasClass('glyphicon-plus')) {
            $(this).removeClass('glyphicon-plus').addClass('glyphicon-minus');
            sub_comment.slideDown( "fast");
        } else {
            $(this).removeClass('glyphicon-minus').addClass('glyphicon-plus');
            sub_comment.slideUp( "fast");
        }
    });

    $('.sub-comment-form form').on("submit", function(e){
        e.preventDefault();
        var form = $(this),
            message = form.find('.message'),
            url = form.attr('action'),
            csrf_token = form.find("input[name='csrfmiddlewaretoken']").val(),
            user = form.find("#id_user").val(),
            parent = form.find("#id_parent").val(),
            comment = form.find("textarea[name='comment']").val();


        $.post($(this).attr('action'), {csrfmiddlewaretoken: csrf_token, parent: parent, user: user, comment: comment}, function(response){
            //form.find("textarea[name='comment']").val('');
            message.html(response).fadeIn(500);
        });
    });

})(jQuery)
