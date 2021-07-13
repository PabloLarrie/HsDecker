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
          <b-dropdown class="position-relative" v-if="token" text="username">
            <b-dropdown-item href="#" to="/settings">Settings</b-dropdown-item>
            <b-dropdown-item href="#">Log out</b-dropdown-item>
          </b-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

import {mapState} from "vuex";

export default {
  name: "MyHeader",
  data() {
    return {};
  },
  computed: {
    ...mapState("userStore", ["token", "user"])
  }
};
</script>
<style scoped>
</style>