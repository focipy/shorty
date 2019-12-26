$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : JSON.stringify({
                url : $('#inputUrl').val(),
                custom : $('#inputCustom').val()
            }),
            type : 'POST',
            url : '/shorty/',
            contentType : "application/json",
            dataType : "json"
        })
        .done(function(data) {
            if (data.error) {
                $('#alertError').text(data.error).show();
                $('#alertSuccess').hide();
            } else {
                $('#alertSuccess').text(data.link).show();
                $('#alertError').hide();
            }
        });
        event.preventDefault();
    });
});
