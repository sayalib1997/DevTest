$(function () {

    $('#id_start_date').datepicker();
    $('#id_end_date').datepicker();

    var keywords = $('#id_keywords');
    keywords.select2({
      tags: true,
      tokenSeparators: [",", " "],
      multiple: true,

      createSearchChoice: function(term, data) {
        if ($(data).filter(function() {
          return this.text.localeCompare(term) === 0;
        }).length === 0) {
          return {
            id: term,
            text: term
          };
        }
      },

      ajax: {
        url: keywords.data('api-url'),
        dataType: 'json',
        data: function(term, page) {
          return {
            q: term
          };
        },
        results: function(data, page) {
          return {
            results: data.results
          };
        }
      }

    });

});
