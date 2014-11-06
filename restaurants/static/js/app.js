(function($) {
    $('a.add').on('click', function(e){
        e.preventDefault();
        $.get($(this).attr('href'), function(data){
            console.log(data);
        });
    });
})(jQuery)
