// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import PostList from './components/PostList'

import {apolloProvider} from './apolloclient'
import('./assets/style.sass')

Vue.config.productionTip = false
Vue.use(VueRouter)

const routes = [
  {path: '/', component: PostList}
]

const router = new VueRouter({
  mode: 'history',
  routes
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  provide: apolloProvider.provide(),
  router
})
