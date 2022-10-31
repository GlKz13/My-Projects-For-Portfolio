
let dropdownBtn = document.getElementById('dropdownBtn')
let dropdownMenu = document.getElementById('dropdownMenu')

dropdownBtn.onclick  = () => {
	if (dropdownMenu.style.opacity == '0') {
		dropdownMenu.style.opacity = '1'
	}
	else if (dropdownMenu.style.opacity == '1') {
		dropdownMenu.style.opacity = '0'
	}
}




