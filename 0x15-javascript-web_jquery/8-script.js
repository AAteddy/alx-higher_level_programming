$(function() {

    var $movie_title = $('#list_movies');

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data) {
            $.each(data.results, function(index, movie) {
                $movie_title.append('<li>'+movie.title+'</li>'); 

            });
        }
    });
});
