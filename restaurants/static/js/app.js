(function($) {
    $( ".comment .glyphicon-plus" ).click(function() {
        var sub_comment = $(this).parents('.comment').find('.sub-comment-form');
        sub_comment.slideDown( "fast");
    });

    $('.sub-comment-form form').on("submit", function(e){
        e.preventDefault();
        test = $(this);
        var url = $(this).attr('action'),
            csrf_token = $(this).find("input[name='csrfmiddlewaretoken']").val(),
            //user = $(this).find("#id_user").val(),
            //parent = $(this).find("#id_parent").val(),
            comment = $(this).find("textarea[name='comment']").val();

        $.post($(this).attr('action'), {csrfmiddlewaretoken: csrf_token, comment: comment}, function(response){
            //$('.sub-comment-form').html("Thank You for your comment");
        });
    });

})(jQuery)
