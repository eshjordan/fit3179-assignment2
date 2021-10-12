const fs = require('fs');
const sass = require('sass');

const result = sass.renderSync({file: "./css/styles.scss"});

fs.writeFile('./css/styles.css', result.css.toString(), err => {});
