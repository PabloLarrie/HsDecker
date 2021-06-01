import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const userState = {
    token: null,
}

const userMutations = {
    setToken(state, token) {
        state.token = token
    }
}

const userActions = {}

const userGetters = {
    token: state => {
        return state.token
    }
}

const userStore = {
    namespaced: true,
    userState,
    userActions,
    userGetters,
    userMutations,

}

export const store = new Vuex.Store({
    modules: {
        userStore
    }
})