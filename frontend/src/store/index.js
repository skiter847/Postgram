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
            console.log(user)
            localStorage.setItem('user_id', user.id)
            localStorage.setItem('username', user.username)
            localStorage.setItem('first_name', user.first_name)
            localStorage.setItem('isAuthenticated', true)
        },

        logout() {
            localStorage.removeItem('user_id')
            localStorage.removeItem('username')
            localStorage.removeItem('first_name')
            localStorage.setItem('isAuthenticated', false)
        }
    },
    state: {
        LoginModal: false,
    },
    getters: {
        getLoginModalStatus(state) {
            return state.LoginModal
        },
        userIsAuthenticated() {
            return localStorage.getItem('isAuthenticated')
        },
        getUserData() {
            let user = {}
            user.user_id = localStorage.getItem('user_id')
            user.username = localStorage.getItem('username')
            user.first_name = localStorage.getItem('first_name')
            return user
        }
    },

})