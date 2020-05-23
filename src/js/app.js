require('./bootstrap');
import Vue from 'vue';


new Vue({
    el: '#app',
    data(){
        return{
            message: 'asdad',
            email: '',
            password: ''
        }
    },
    methods: {
        submit(){
            axios.post('/test',{email: this.email,password: this.password}).then(res=>console.log(res));
        }
    }
});
