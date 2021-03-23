import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueEvaInput from "vue-eva-input";
import VueSimpleAlert from "vue-simple-alert";
import VueCarousel from 'vue-carousel';

Vue.use(VueCarousel);
Vue.use(VueSimpleAlert);
Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(VueEvaInput);


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
