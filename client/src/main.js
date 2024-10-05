import '../style.css';

import axios from 'axios';
axios.defaults.baseURL = 'http://192.168.0.137:80';
axios.defaults.withCredentials = true;

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)
app.mount('#app')

function print(s){
    console.log(s)
}
