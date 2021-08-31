import VueRouter from "vue-router"
import CardsList from "@/components/CardsList";
import DecksList from "@/components/DecksList";
import CardDetail from "@/components/cardsDetail/CardDetail";
import DeckDetail from "@/components/decksDetail/DeckDetail";
import Login from "@/components/users/Login";
import CreateDeck from "@/components/decksDetail/CreateDeck";
import register from "@/components/users/register"
import { store } from "@/vuex"
import settings from "../components/users/settings";
import Home from "../components/Home";


export const router = new VueRouter({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "cards",
            component: CardsList,
        },
        {
            path: "/decks",
            name: "decks",
            component: DecksList,
        },
        {
            path: '/detail-card/:cardId/',
            name: 'detail-card',
            component: CardDetail,
            props: true,

        },
        {
            path: '/detail-deck/:deckId/',
            name: 'detail-deck',
            component: DeckDetail,
            props: true,
            meta: { requiresAuth: true }
        },
        {
            path: "/login",
            name: "login",
            component: Login,
        },
        {
            path: "/home",
            name: "home",
            component: Home,
        },
        {
            path: "/register",
            name: "register",
            component: register,
        },
        {
            path: "/settings",
            name: "settings",
            component: settings,
            props: true,

        },
        {
            path: "/create-deck",
            name: "createDeck",
            component: CreateDeck,
        },
    ],
})

router.beforeEach((to, from, next) => {
    if(to.meta.requiresAuth && !store.state.userStore.token) {
             next({
                name: "login"
            });
    } else {
        next();
    }
});