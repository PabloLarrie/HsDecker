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
import {TOKEN_STORAGE_KEY} from "@/constants";
import {mapMutations} from "vuex";

// import MyFooter from "./components/Footer";

export default {
  name: "App",
  components: {
    MainLayout,
    MyHeader,
    // MyFooter,
  },
  methods: {
    ...mapMutations("userStore", ["setToken", "setUser"]),
  },
  data() {
    return {};
  },
  mounted() {
    const token_check = localStorage.getItem(TOKEN_STORAGE_KEY)
    if (token_check) {
      this.setToken(token_check);
      this.$api.get("/user/").then((response) => {
        this.setUser(response.data)
      })
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap");
</style>
