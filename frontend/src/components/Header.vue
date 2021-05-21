<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">HSDECKER</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <router-link to="/">Cards</router-link>
          <router-link to="/decks">Decks</router-link>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
  data() {
    return {};
  },
};
</script>
<style scoped>
</style>