import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const userStore = {
    namespaced: true,
    state: {
        token: null,
        user: {},
    },
    actions: {},
    getters: {
        token: state => {
            return state.token
        },
    },
    mutations: {
        setToken(state, token) {
            state.token = token
        },
        setUser (state, user) {
            state.user = user
        },
    },


}

export const store = new Vuex.Store({
    modules: {
        userStore
    }
})