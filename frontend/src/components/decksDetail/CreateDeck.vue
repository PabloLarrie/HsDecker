<template>
  <edit-deck-layout>
    <template v-slot:deckBody>
      <b-form>

        <b-form-group label="Name:" >
          <b-form-input
              id="name"
              v-model="name"
              placeholder="Enter Deck Name"
              required
          ></b-form-input>
        </b-form-group>

        <b-form-group label="Hero Class:" >
          <b-form-select v-model="selectedHero" :options="heroOptions">
          </b-form-select>
        </b-form-group>

        <b-form-checkbox v-model="standard">Standard</b-form-checkbox>

        <b-button @click="submitDeck">Create</b-button>
        <b-button>
            <router-link to="/decks">Cancel</router-link>
        </b-button>

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
  data() {
    return {
      name: '',
      selectedHero: null,
      standard: false,
      heroOptions: [],
      heroClass: '',
    }
  },
  methods: {
    submitDeck() {
      let values = {
            "name": this.name,
            "hero_class_id": this.selectedHero,
            "standard": this.standard,
        }
    },
  },
  mounted() {
    this.$api.get("/hero-classes/").then((response) => {
      this.heroOptions = response.data.results.reduce(
          (options, hero) => {
            options.push({ value: hero.id, text: hero.name });
            return options;
          },
          [{ value: "", text: "All heroes" }]
      )
    });
  }
};
</script>
<style>
</style>