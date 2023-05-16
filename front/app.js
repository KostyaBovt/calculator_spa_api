
window.onload = function() {	
	var countButton = document.getElementById('count');

	countButton.onclick = function(event) {
		let arg_1 = document.getElementById('arg_1');
		let arg_2 = document.getElementById('arg_2');
		let post = JSON.stringify({"arg_1": arg_1.value, "arg_2": arg_2.value})
		selected = document.getElementById('operation');
        selectedOperation = selected.value;
		const url = "http://localhost:5000/" + selectedOperation
		let xhr = new XMLHttpRequest()
		xhr.open('POST', url, true)
		xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
		xhr.setRequestHeader('Access-Control-Allow-Origin', '*')
		xhr.setRequestHeader('Access-Control-Allow-Methods', 'POST, PUT, PATCH, GET, DELETE, OPTIONS')
		xhr.setRequestHeader('Access-Control-Allow-Headers', 'Origin, X-Api-Key, X-Requested-With, Content-Type, Accept, Authorization')

		xhr.send(post);
		xhr.onload = function () {
			if(xhr.status === 200) {
				document.getElementById('result').value = xhr.responseText;

			}
		}
	}
}