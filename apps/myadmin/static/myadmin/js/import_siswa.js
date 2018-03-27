



$("#form-input-xls-siswa").submit(function() {
	event.preventDefault();
  var file = $('input[name=pickExcel]').prop('files')[0];
  var formData = new FormData();
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  formData.append('pickExcel', file);
  formData.append('csrfmiddlewaretoken', csrftoken);
  $.ajax({
 		type: "POST",
  	url: $(this).attr('action'),
  	data: formData,
  	contentType: false,
 	 	cache: false,
  	processData: false,
  	success: function(response) { // on success..
      if (response === "wrong extension") {
        console.log('wrong extension');
      }
      else if (response === "wrong format") {
        console.log('wrong format');
      } else {
        console.log(response);
        // window.location.href = 'konfirmasi/'; 
      }
      
    },
    error: function(e, x, r) { // on error..
      console.log(r);
    }
	});
	return false;
    //console.log(file);
});







