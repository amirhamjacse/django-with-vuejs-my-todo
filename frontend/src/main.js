import { createApp } from 'vue'
import App from './App.vue'
// main.js (Vue 2 and Vue 3)
import 'bootstrap/dist/css/bootstrap.css';

// Import Bootstrap's JavaScript only if needed (Vue 3)
import 'bootstrap';

import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
