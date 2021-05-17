import VueRouter from "vue-router"
import CardsList from "@/components/CardsList";
import DecksList from "@/components/DecksList";

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
        }
    ]
})