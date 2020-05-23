try {
    require('popper.js');
    window.$ = window.jQuery = require('jquery');
    require('bootstrap');
} catch (error) {
    
}

window.axios = require('axios');
let token = jQuery("[name=csrfmiddlewaretoken]").val();
// console.log(token);
if(token){
    
    window.axios.defaults.headers["X-CSRFToken"] = token;
}