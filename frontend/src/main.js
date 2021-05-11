import Vue from 'vue'
import { api } from './axios/axios'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(api)

new Vue({
  render: h => h(App),
}).$mount('#app')
