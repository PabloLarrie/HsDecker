<template>
  <table-layout>
    <template v-slot:pagination-top>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="filters.size"
        @nextPageClick="nextPage"
        @previousPageClick="previousPage"
      />
    </template>
    <template v-slot:filters>
      <b-button-toolbar>
        <b-input
          size="sm"
          class="mr-sm-2"
          placeholder="Search by card name"
          v-model="filters.searchInfo"
          debounce="500"
        ></b-input>
        <b-form-select v-model="filters.selectedType" :options="typeOptions">
        </b-form-select>

        <b-form-select
          v-model="filters.selectedQuality"
          :options="qualityOptions"
        >
        </b-form-select>

        <b-form-select
          v-model="filters.selectedFormat"
          :options="formatOptions"
        >
        </b-form-select>

        <b-form-select v-model="filters.selectedHero" :options="heroOptions">
        </b-form-select>

        <b-form-select v-model="filters.selectedRace" :options="raceOptions">
        </b-form-select>
        <b-input
          size="sm"
          class="mr-sm-5"
          placeholder="Cost"
          v-model="filters.selectedCost"
          debounce="500"
        ></b-input>
        <b-button @click="resetFilter"> Reset </b-button>
      </b-button-toolbar>
    </template>

    <template v-slot:table>
      <b-table class="w-100" striped hover :items="info" :fields="columns">
        <template #cell(heroes)="data">
          {{ data.value.length ? data.value.join(", ") : "Neutral" }}
        </template>
      </b-table>
    </template>

    <template v-slot:pagination-bottom>
      <table-pagination
        :next="next"
        :previous="previous"
        v-model="filters.size"
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
      savedFilters: {},
      columns: ["name", "card_type", "quality", "heroes", "standard", "race"],
      filters: {
        selectedQuality: "",
        selectedFormat: "",
        selectedHero: "",
        selectedRace: "",
        selectedCost: "",
        selectedType: "",
        searchInfo: null,
        size: 15,
      },
      typeOptions: [
        { value: "", text: "All card types" },
        { value: "minion", text: "Minion" },
        { value: "spell", text: "Spell" },
        { value: "weapon", text: "Weapon" },
        { value: "hero", text: "Hero" },
      ],
      qualityOptions: [
        { value: "", text: "All frequencies" },
        { value: "free", text: "Free" },
        { value: "common", text: "Common" },
        { value: "rare", text: "Rare" },
        { value: "epic", text: "Epic" },
        { value: "legendary", text: "Legendary" },
      ],
      formatOptions: [
        { value: "", text: "All Formats" },
        { value: true, text: "Standard" },
        { value: false, text: "Wild" },
      ],
      heroOptions: [
        { value: "", text: "All Heroes" },
        { value: 1, text: "Demon Hunter" },
        { value: 2, text: "Druid" },
        { value: 3, text: "Hunter" },
        { value: 4, text: "Mage" },
        { value: 5, text: "Paladin" },
        { value: 6, text: "Priest" },
        { value: 7, text: "Rogue" },
        { value: 8, text: "Shaman" },
        { value: 9, text: "Warlock" },
        { value: 10, text: "Warrior" },
      ],
      raceOptions: [
        { value: "", text: "All races" },
        { value: "beast", text: "Beast" },
        { value: "murloc", text: "Murloc" },
        { value: "dragon", text: "Dragon" },
        { value: "demon", text: "Demon" },
        { value: "totem", text: "Totem" },
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
    magicFilter() {
      this.loadData(
        `/cards/?standard=${this.filters.selectedFormat}` +
          `&hero=${this.filters.selectedHero}` +
          `&card_type=${this.filters.selectedType}` +
          `&quality=${this.filters.selectedQuality}` +
          `&race=${this.filters.selectedRace}` +
          `&expansion=&cost=${this.filters.selectedCost}` +
          `&page_size=${this.filters.size}`
      );
    },
    resetFilter() {
      Object.entries(this.filters).forEach(([key]) => {
        this.filters[key] = this.savedFilters[key];
      });
    },
  },
  watch: {
    size() {
      this.magicFilter();
    },
    filters: {
      handler() {
        this.magicFilter();
      },
      deep: true,
    },
  },
  mounted() {
    this.loadData("/cards/?page_size=15");
    this.savedFilters = JSON.parse(JSON.stringify(this.filters));
  },
};
</script>
<style scoped>
</style>