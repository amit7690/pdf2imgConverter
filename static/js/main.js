console.log('Hello javascript')

const uploadForm = document.getElementById('upload_form')
const input_file = document.getElementById('id_image')
const progress_bar = document.getElementById('progress')
// console.log(progress_bar)
$("#upload_form").submit(function(e){
	e.preventDefault();
	$form = $(this)
	var formData = new FormData(this);
	const media_data = input_file.files[0];
	if(media_data != null){
		console.log(media_data);
		progress_bar.classList.remove("no-visible");
		console.log('Hello this is working')
	}


	$.ajax({
		type: 'POST',
		url:'/',
		data: formData,
		dataType: 'json',

		beforSend: function(){

		},

		xhr: function(){

		},

		error: function(){

		},

		cache: false,
		contentType: false,
		progressData: false,
	}); 



});
