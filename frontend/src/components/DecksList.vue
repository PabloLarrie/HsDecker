<template>
  <table-layout>
    <template v-slot:pagination-top>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="size"
        @nextPageClick="nextPage"
        @previousPageClick="previousPage"
      />
    </template>
    <template v-slot:filters>
      <b-input
        size="sm"
        class="mr-sm-2"
        placeholder="Search by deck name"
        v-model="searchInfo"
        debounce="500"
      ></b-input>

      <b-form-select v-model="selectedFormat" :options="formatOptions">
      </b-form-select> 

      <b-form-select v-model="selectedHero" :options="heroOptions">
      </b-form-select> 

    </template>

    <template v-slot:table>
      <b-table
          class="w-100"
          striped hover
          :items="info"
          @row-clicked="rowClick"
      />
      <b-button>
        <router-link to="/create-deck">Create new Deck</router-link>
      </b-button>
    </template>

    <template v-slot:pagination-bottom>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="size"
        @nextPageClick="nextPage"
        @previousPageClick="previousPage"
      />
    </template>
  </table-layout>
</template>

<script>
import TablePagination from "@/components/table/TablePagination";
import TableLayout from "@/layouts/TableLayout";

export default {
  name: "CardsList",
  components: {
    TablePagination,
    TableLayout,
  },
  data() {
    return {
      tipoInput: "number",
      index: "number",
      info: [],
      next: null,
      previous: null,
      size: 15,
      searchInfo: null,
      selectedFormat: "",
      selectedHero: "",
      formatOptions: [
        {value: "", text: "All Formats"},
        {value: true, text: "Standard"},
        {value: false, text: "Wild"},
      ],
      heroOptions: [
        {value: "", text: "All Heroes"},
        {value: 1, text: "Demon Hunter"},
        {value: 2, text: "Druid"},
        {value: 3, text: "Hunter"},
        {value: 4, text: "Mage"},
        {value: 5, text: "Paladin"},
        {value: 6, text: "Priest"},
        {value: 7, text: "Rogue"},
        {value: 8, text: "Shaman"},
        {value: 9, text: "Warlock"},
        {value: 10, text: "Warrior"},
      ],
    };
  },

  methods: {
    loadData(url) {
      this.$api.get(url).then((response) => {
        this.info = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      });
    },
    nextPage() {
      this.loadData(this.next);
    },
    previousPage() {
      this.loadData(this.previous);
    },
    rowClick(row) {
      this.$router.push({
        name: "detail-deck",
        params: { deckId: row.id },
      });
    },

  },
  watch: {
    size() {
      this.loadData("/decks/?page_size=" + this.size);
    },
    searchInfo() {
      this.loadData("/decks/?search=" + this.searchInfo);
    },
    selectedFormat () {
      this.loadData("/decks/?standard=" + this.selectedFormat);
    },
    selectedHero () {
      this.loadData("/decks/?hero_class=" + this.selectedHero);
    },
  },
  mounted() {
    this.loadData("/decks/?page_size=15");
  },
};
</script>
<style>
</style>