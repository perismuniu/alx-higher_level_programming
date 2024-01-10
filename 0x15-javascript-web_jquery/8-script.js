$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      success: function(data) {
        $.each(data.results, function(index, movie) {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error fetching movie data:', errorThrown);
      }
    });
  }); 