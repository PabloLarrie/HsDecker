import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import { api } from './axios/axios'
import { router } from './router/router'
import App from './App.vue'
import VueRouter from "vue-router"
import { store } from "./vuex/index"

Vue.config.productionTip = false
Vue.use(api)
Vue.use(VueRouter)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
