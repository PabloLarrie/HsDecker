<template>
  <home-layout>
    <template v-slot:homeBody>
      <div>
        <h1>Wellcome to HSDecker</h1>
        <b-button>
          <router-link to="/">Cards</router-link>
        </b-button>
        <b-button>
          <router-link to="/decks">Decks</router-link>
        </b-button>
      </div>
    </template>
  </home-layout>
</template>

<script>
import HomeLayout from "../layouts/HomeLayout";

export default {
  name: "Home",
  components: {
    HomeLayout,
  },
  data() {
    return {}
  },
}
</script>
<style scoped>
</style>