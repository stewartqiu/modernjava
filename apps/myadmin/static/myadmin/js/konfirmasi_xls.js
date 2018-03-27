


$("form").submit(function() {
	event.preventDefault();
  var dataList = $("input[name=dataList]").val();
  console.log(typeof dataList);
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  var formData = new FormData();
  formData.append('dataList', dataList);
  formData.append('csrfmiddlewaretoken', csrftoken);
  $.ajax({
 		type: "POST",
  	url: $(this).attr('action'),
  	data: formData,
  	contentType: false,
 	 	cache: false,
  	processData: false,
  	success: function(response) { // on success..
      console.log(response)
    },
    error: function(e, x, r) { // on error..
      console.log(r);
    }
	});
	return false;
});


