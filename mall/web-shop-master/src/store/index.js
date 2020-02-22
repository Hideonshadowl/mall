import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);
const store=new Vuex.Store({
  state: {
    foodlist: [],
    shopcartlist:[],
    adressinfo:{receiverName:'',receiverMobile:'',address:'',receiverZip:'',receiverAddress:''}
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
    delete_one(state,val) {
      state.shopcartlist.forEach((value,index) => {
        if (val===value){
          state.shopcartlist.splice(index,1)
        }

      })
    },
    addadressinfo(state,val){
      state.adressinfo.receiverName=val[0];
      state.adressinfo.receiverMobile=val[1];
      state.adressinfo.address=val[2];
      state.adressinfo.receiverZip=val[3];
      state.adressinfo.receiverAddress=val[4];
    }
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
    deleteone(context,val) {
      context.commit('delete_one',val)
    },
    addadress(context,val){
      context.commit('addadressinfo',val)
    }

  }
});
export default store
