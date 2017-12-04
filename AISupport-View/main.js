import Vue from 'vue'
import App from './application/App.vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)
// Should send requests with application/x-www-form-urlencoded (simple request)
Vue.http.options.emulateJSON = true;
new Vue({
    el: '#app',
    render: h => h(App)
})