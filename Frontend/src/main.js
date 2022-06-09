import Vue from 'vue'
import App from './App.vue'
import router from './router'
import LazyYoutube from "vue-lazytube";


Vue.component("LazyYoutube", LazyYoutube);

Vue.config.productionTip = false

new Vue({
  /* eslint-disable */
  router,
  render: h => h(App)
}).$mount('#app')
