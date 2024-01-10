$(document).ready(function() {
    $('#btn_translate').click(function() {
      const languageCode = $('#language_code').val();
  
      if (languageCode) {
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/hello/',
          method: 'GET',
          data: { lang: languageCode },
          success: function(data) {
            $('#hello').text(data.hello);
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error fetching translation:', errorThrown);
            $('#hello').text('Translation not found');
          }
        });
      } else {
        $('#hello').text('Please enter a language code');
      }
    });
  });
  