function check_box(max){
	const checkbox = document.querySelectorAll('input[name="options"]');
	const checkedCount = Array.from(checkbox).filter(checkbox => checkbox.checked).length;

	console.log(checkbox);

	checkbox.forEach(checkbox => {
		if (checkedCount >= max && !checkbox.checked){
			checkbox.disabled = true;
		} else {
			checkbox.disabled = false;
		}
	});
}
