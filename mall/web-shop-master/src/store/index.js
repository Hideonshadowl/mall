import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions.js'
import * as type from './types';
Vue.use(Vuex);
const store=new Vuex.Store({
  actions,
  state:{
        cartlist:[],
        user:'',
        pw1:'',
    },
    mutations:{

        [type.ADDCART](state,val){
          state.cartlist.push(val)
        },
        [type.SAVEUSER](state,val){
            state.user=val
        },
        [type.SAVEPW](state,val){
          state.pw1=val
        },
        clearuser(state){
          state.user=''
        },
        clearpw(state){
          state.pw1=''
        },

    }


})
export default store
