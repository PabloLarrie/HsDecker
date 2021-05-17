<template>
  <main-layout>
    <template v-slot:header>
      <my-header />
      <hr />
    </template>

    <template v-slot:body>
      <cards-bar />
      <cards-list />
      <hr />
      <decks-bar />
      <decks-list />
    </template>
  </main-layout>
</template>


<script>
import MyHeader from "./components/Header";
import CardsList from "./components/CardsList";
import DecksList from "./components/DecksList";
import MainLayout from "./layouts/MainLayout";
import DecksBar from "./components/bars/DecksBar";
import CardsBar from "./components/bars/CardsBar";

// import MyFooter from "./components/Footer";

export default {
  name: "App",
  components: {
    MainLayout,
    MyHeader,
    CardsList,
    DecksList,
    CardsBar,
    DecksBar,
    // MyFooter,
  },
  data() {
    return {};
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap");

body {
  background: linear-gradient(#2b1055, #7597de);
}
</style>
