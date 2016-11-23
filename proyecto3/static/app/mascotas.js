$(function(){

    var url = '/mascotas/nueva_mascota/upload/';

    $('#fileupload').fileupload({

        url: url,
        dataType: 'json',

        add: function (e, data) {

            // enable the upload button
            $('#upload_button').removeProp('disabled');

            // Clean the messages
            $('.result').html("");

            // remove the color classes
            $('.result').removeClass('result-sucess');
            $('.result').removeClass('result-error');

            // Click event on the upload button
            $('#upload_button').unbind('click').bind('click', function(event){
                // Stop the propagation of the click event
                event.preventDefault();

                // disable the upload button while uploading
                $('#upload_button').prop('disabled', true);

                // Hide the input
                $('#foto_mascota').hide();
                $('.help-message-block').hide();

                // Show the progress bar
                $("#upload_progress").show();

                // Submit the form
                data.submit();

            });
        },
        done: function (e, data) {

            result = data.result;
            messages = ""

            // Check if we have errors
            if (  result.foto_mascota )
            {

                // Get all the messages
                for(i=0; i<result.foto_mascota.length; i++){
                    messages += '<p>' + result.foto_mascota[i] + '</p>';
                }

                // show the messages
                $('.result').append(messages);
                $('.result').addClass('result-error');

                // Show the input
                $('#foto_mascota').show();

                // hide progressbar and set it to 0
                $("#upload_progress").hide();
                $('#upload_progress .progress-bar-success').css('width','0%');

            }
            else
            {
                // disable the next button
                // $('#next_button').removeAttr('disabled');
                $('#next_button').removeAttr('disabled');
                $('#next_button').unbind('click', false);

                // Show an Ok message
                if (result.status == 'OK'){
                    var message = '<p>' + result.message + '</p>'
                    //$('.result').html(message);
                    //$('.result').addClass('result-sucess');
                    $("#upload_progress").hide();
                    $('.delete_file_form_container').show();
                }

                // Hide the upload button
                $('#upload_button').hide();
                $('.help-message-block').hide();

            }
        },
        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('#upload_progress .progress-bar-success').css(
                'width',
                progress + '%'
            );
        }
    })
    .bind('fileuploadfail', function (e, data) {

        // Show an error message
        var message_en = 'An Server error has occurred, please try later.';
        var message_es = 'Ha ocurrido un error en el servidor por favor intente de nuevo.';
        $('.result').html('<p>' + message_es +'</p>');
        $('.result').addClass('result-error');

        // Show the input
        $('#foto_mascota').show();
        $('.help-message-block').show();

        // hide progressbar and set it to 0
        $("#upload_progress").hide();
        $('#upload_progress .progress-bar-success').css(
            'width','0%'
        );

    });


});
