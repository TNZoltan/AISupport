import Vue from 'vue'
import App from './application/App.vue'
import VueResource from 'vue-resource'
import VueChatScroll from 'vue-chat-scroll'

Vue.use(VueResource)
Vue.use(VueChatScroll)
// Should send requests with application/x-www-form-urlencoded (simple request)
Vue.http.options.emulateJSON = true;
new Vue({
    el: '#app',
    render: h => h(App)
})