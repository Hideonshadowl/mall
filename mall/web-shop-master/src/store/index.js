import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);
const store=new Vuex.Store({
  state: {
    foodlist: [],
    shopcartlist:[],
  },
  mutations: {
    addfood(state, val) {
      state.foodlist = val
    },
    addcartlist(state, val) {
      state.shopcartlist.push(val)
    },
    clearcartlist(state) {
      state.shopcartlist=[]
    },
    reduce_count(state,val) {
      state.shopcartlist.forEach(value => {
        if (val===value && value[1]>1){
          value[1]--
        }
      })
    },
    add_count(state,val) {
      state.shopcartlist.forEach(value => {
        if (val===value){
          value[1]++
        }
      })
    },
  },
  actions: {
    adddata(context, val) {
      context.commit('addfood', val)
    },
    addshoplist(context, val) {
      context.commit('addcartlist', val)
    },
    clearshoplist(context) {
      context.commit('clearcartlist')
    },
    reducecount(context,val) {
      context.commit('reduce_count',val)
    },
    addcount(context,val) {
      context.commit('add_count',val)
    },

  }
});
export default store
