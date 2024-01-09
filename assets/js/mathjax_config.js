window.MathJax = {
  // loader: {load: ['[tex]/commath']},
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    macros: {
      ensuremath: ["#1",1],
      textup: ["{\\mathrm{#1}}",1]
    },
    // packages: {'[+]': ['commath']}
  },
  svg: {
    fontCache: 'global'
  }
};

(function () {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-chtml.js';
  script.async = true;
  document.head.appendChild(script);
})();