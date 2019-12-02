// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/'
import 'lib-flexible'   //rem布局
//import http from './service/ajax'
import fastclick from 'fastclick'
import VueScroller from 'vue-scroller'
import VueAwesomeSwiper from 'vue-awesome-swiper'
Vue.use(VueAwesomeSwiper)
Vue.use(VueScroller)
fastclick.attach(document.body) //解决移动端点击300ms延时
Vue.config.productionTip = false
import VueAxios from 'vue-axios'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//import http from "./service/ajax"


Vue.use(ElementUI);
Vue.prototype.axios=axios;
// 引入mockjs
// require('./mock/mock.js')
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed'

Vue.directive('focus', {
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function (el) {
        // 聚焦元素
        el.focus()
    }
})



/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>',
    render: h => h(App)
})




