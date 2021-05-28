import VueRouter from "vue-router"
import CardsList from "@/components/CardsList";
import DecksList from "@/components/DecksList";
import CardDetail from "@/components/cardsDetail/CardDetail";
import Login from "@/components/users/Login";

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
            path: "/login",
            name: "login",
            component: Login,
        },
    ]
})