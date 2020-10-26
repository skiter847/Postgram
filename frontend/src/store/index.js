import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
    actions:{},
    mutations:{
        switchLoginModalStatus(state){
            state.LoginModal = !state.LoginModal
        }
    },
    state:{
        LoginModal : false,
    },
    getters:{
        getLoginModalStatus(state){
            return state.LoginModal
        }
    },

})