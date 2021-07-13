-<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">HSDECKER</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-button>
            <router-link to="/">Cards</router-link>
          </b-button>
          <b-button>
            <router-link to="/decks">Decks</router-link>
          </b-button>
        </b-navbar-nav>
        <b-navbar-nav class="position-absolute top-0 end-0">
          <b-button v-if="!token">
            <router-link v-b-tooltip.hover.down="'Click to login!'" to="/login">Login</router-link>
          </b-button>
          <b-button v-if="!token">
            <router-link v-b-tooltip.hover.down="'Click to Register!'" to="/register">Register</router-link>
          </b-button>
          <b-dropdown class="position-relative" v-if="token" :text="user.username">
<!--            <b-dropdown-item href="#" to="/settings">Settings</b-dropdown-item>-->
            <b-dropdown-item @click="logOut">Log out</b-dropdown-item>
          </b-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

import {mapMutations, mapState} from "vuex";
import {TOKEN_STORAGE_KEY} from "@/constants";
import {PUBLIC_PAGES} from "@/constants";

export default {
  name: "MyHeader",
  data() {
    return {};
  },
  methods: {
    ...mapMutations("userStore", ["setToken", "setUser"]),
    logOut() {
      localStorage.removeItem(TOKEN_STORAGE_KEY)
      this.setToken(null);
      this.setUser(null);
      const currentRoute = this.$router.currentRoute.name
      if (!PUBLIC_PAGES.includes(currentRoute)) {
        this.$router.push({
          name: "cards",
        });
      }
    }
  },
  computed: {
    ...mapState("userStore", ["token", "user"])
  }
};
</script>
<style scoped>
</style>