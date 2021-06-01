import VueRouter from "vue-router"
import CardsList from "@/components/CardsList";
import DecksList from "@/components/DecksList";
import CardDetail from "@/components/cardsDetail/CardDetail";
import DeckDetail from "@/components/decksDetail/DeckDetail";
import Login from "@/components/users/Login";
import EditDeck from "@/components/decksDetail/EditDeck";
import CreateDeck from "@/components/decksDetail/CreateDeck";

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
        },
        {
            path: "/login",
            name: "login",
            component: Login,
        },
        {
            path: "/edit-deck",
            name: "editDeck",
            component: EditDeck,
        },
        {
            path: "/create-deck",
            name: "createDeck",
            component: CreateDeck,
        },
    ]
})