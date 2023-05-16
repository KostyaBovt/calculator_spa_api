
window.onload = function() {	
	var countButton = document.getElementById('count');

	countButton.onclick = function(event) {
		let postObj = {"arg_1": 10, "arg_2": 20}
		let post = JSON.stringify(postObj)
		const url = "http://localhost:5000/add"
		let xhr = new XMLHttpRequest()
		xhr.open('POST', url, true)
		xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
		xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
		xhr.setRequestHeader('Access-Control-Allow-Methods', 'POST, PUT, PATCH, GET, DELETE, OPTIONS')
		xhr.setRequestHeader('Access-Control-Allow-Headers', 'Origin, X-Api-Key, X-Requested-With, Content-Type, Accept, Authorization')

		xhr.send(post);
		xhr.onload = function () {
			if(xhr.status === 200) {
				console.log("Post successfully created!") 
				console.log(xhr) 
			}
		}
	}
}