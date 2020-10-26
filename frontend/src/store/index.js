import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
    actions: {},
    mutations: {
        switchLoginModalStatus(state) {
            state.LoginModal = !state.LoginModal
        },
        login(state, user) {
            localStorage.setItem('user_id', user.id)
            localStorage.setItem('username', user.username)
            localStorage.setItem('first_name', user.first_name)
            state.isAuthenticated = true
        },

        logout(state) {
            localStorage.removeItem('user_id')
            localStorage.removeItem('username')
            localStorage.removeItem('first_name')
            state.isAuthenticated = false
        }
    },
    state: {
        LoginModal: false,
        isAuthenticated: false,
    },
    getters: {
        getLoginModalStatus(state) {
            return state.LoginModal
        },
        userIsAuthenticated(state) {
            return state.isAuthenticated
        }
    },

})