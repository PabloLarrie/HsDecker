<template>
  <edit-deck-layout>
    <template v-slot:deckBody>
      <b-form>

        <b-form-group label="Name:" >
          <b-form-input
              id="input-1"
              v-model="name"
              placeholder="Enter Deck Name"
              required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Hero Class:" >
          <b-form-input
              id="input-2"
              v-model="hero_class"
              placeholder="Enter Hero"
              required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Standard:" >
          <b-form-input
              id="input-3"
              v-model="standard"
              placeholder="Enter Standard"
              required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Cards:" >
          <b-form-input
              id="input-4"
              v-model="cards"
              placeholder="Enter Cards"
              required
          ></b-form-input>
        </b-form-group>

      </b-form>

    </template>
  </edit-deck-layout>
</template>

<script>
import EditDeckLayout from "@/layouts/EditDeckLayout";

export default {
  name: "Login",
  components: {
    EditDeckLayout,
  },
  props: {},
  data() {
    return {
      name: '',
      hero_class: '',
      standard: '',
      cards: [],
      }

    },

  methods: {
  },
};
</script>
<style>
</style>