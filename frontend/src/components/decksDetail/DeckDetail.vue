<template>
  <deck-layout>
    <template v-slot:deckBody>
      <b-button v-if="user.id === info[0].user.id && !editMode" @click="editMode = true">
        Edit
      </b-button>
      <b-button v-if="user.id === info[0].user.id && editMode" @click="cancel">
        Cancel
      </b-button>
      <b-button v-if="user.id === info[0].user.id && editMode" @click="save">
        Save changes
      </b-button>
      <b-table
          hover
          small
          caption-top
          class="w-100"
          striped
          :fields="columns"
          :items="info"
          bordered
      >
      </b-table>
    </template>
    <template v-slot:cardContent>
      <b-table
          hover
          small
          caption-top
          class="w-100"
          striped
          :fields="cardColumns"
          :items="cardsInfo"
          bordered
          @row-clicked="rowClick"

      >
        <template #cell(card)="data">
          {{ data.value.name }}
        </template>
      </b-table>
    </template>
  </deck-layout>
</template>

<script>
import DeckLayout from "@/layouts/DeckLayout";
import {mapState} from "vuex";

export default {
  name: "DeckDetail",
  components: {
    DeckLayout
  },
  props: {
    deckId: {
      required: true,
    },
    cardId: {
      required: true,
    },
  },
  data() {
    return {
      info: [],
      cardsInfo: [],
      editMode: false,
      columns: [
        "id",
        "name",
        "hero_class",
        "standard",
        "complete",
        "size",
        "total_cards",
      ],
      cardColumns: [
        "card",
        "quantity",
        "golden",
      ]
    };
  },
  methods: {
    loadData(url) {
      this.$api.get(url)
          .then((response) => {
            this.info = [response.data];
            this.cardsInfo = response.data.cards;
          });

    },
    rowClick(row) {
      this.$router.push({
        name: "detail-card",
        params: {cardId: row.card.id},
      });
    },
    cancel() {
      this.editMode = false
    },
    save() {
      this.editMode = false
    },
  },
  computed: {
    ...mapState("userStore", ["user"])
  },
  mounted() {
    this.loadData("/decks/" + this.deckId);
  },
};
</script>
<style scoped>
</style>