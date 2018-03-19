$("#form-input-siswa").submit(function() {
	event.preventDefault();
    file = $("input[name=pickExcel]").files;
    console.log(file);
});