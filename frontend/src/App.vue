<template>
  <main-layout>
    <template v-slot:header>
      <my-header />
    </template>

    <template v-slot:body>
      <router-view />
    </template>
  </main-layout>
</template>


<script>
import MyHeader from "./components/Header";
import MainLayout from "./layouts/MainLayout";

// import MyFooter from "./components/Footer";

export default {
  name: "App",
  components: {
    MainLayout,
    MyHeader,
    // MyFooter,
  },
  data() {
    return {};
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap");
</style>
