// Populate the h1 and h2 after pseudoelements with the content `'from Engineering Mathematics chapter ' attr(data-0-ch) ', p. ' attr(data-0-p) ', code: ' attr(data-0-hash)` using the css var `--after-content`
document.querySelectorAll("h1, h2").forEach(function(element) {
	if (element.classList.contains('real-section') && !element.classList.contains('faux')) {
		const chapter = element.getAttribute('data-0-ch');
		const page = element.getAttribute('data-0-p');
		var hash = element.getAttribute('data-0-hash');
		if (hash !== null) {
			hash = hash.toUpperCase();
		}
		const content = `'from Engineering Mathematics chapter ${chapter}, p. ${page}, code: ${hash}'`;
		element.style.setProperty('--after-content', content);
	}
});