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
        placeholder="Search by card name"
        v-model="searchInfo"
        debounce="500"
      ></b-input>

      <b-form-select v-model="selectedType" :options="typeOptions">
      </b-form-select>

      <b-form-select v-model="selectedQuality" :options="qualityOptions">
      </b-form-select>

      <b-form-select v-model="selectedFormat" :options="formatOptions">
      </b-form-select> 

      <b-form-select v-model="selectedHero" :options="heroOptions">
      </b-form-select> 
      
      <b-form-select v-model="selectedRace" :options="raceOptions">
      </b-form-select> 

      <b-input
        size="sm"
        class="mr-sm-5"
        placeholder="Cost"
        v-model="selectedCost"
        debounce="500"
      ></b-input>

    </template>

    <template v-slot:table>
      <b-table class="w-100" striped hover :items="info" />
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
      magicFilter: "",
      selectedType: "",
      searchInfo: null,
      selectedQuality: "",
      selectedFormat: "",
      selectedHero: "",
      selectedRace: "",
      selectedCost: "",
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
      raceOptions: [
        {value: "", text: "All races"},
        {value: "beast", text: "Beast"},
        {value: "murloc", text: "Murloc"},
        {value: "dragon", text: "Dragon"},
        {value: "demon", text: "Demon"},
        {value: "totem", text: "Totem"},
      ]
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

  },
  watch: {
    magicFilter () {
      this.loadData("/cards/?standard=" + this.selectedFormat + 
      "&hero=" + this.selectedHero +
      "&card_type=" + this.selectedType + 
      "&quality=" + this.selectedQuality + 
      "&race=" + this.selectedRace + 
      "&expansion=" +
      "&cost=" + this.selectedCost);
    },
    size() {
      this.loadData("/cards/?page_size=" + this.size);
    },
    searchInfo() {
      this.loadData("/cards/?search=" + this.searchInfo);
    },
    selectedType () {
      this.loadData("/cards/?card_type=" + this.selectedType);
    },
    selectedQuality () {
      this.loadData("/cards/?quality=" + this.selectedQuality);
    },
    selectedFormat () {
      this.loadData("/cards/?standard=" + this.selectedFormat);
    },
    selectedHero () {
      this.loadData("/cards/?hero=" + this.selectedHero);
    },
    selectedRace () {
      this.loadData("/cards/?race=" + this.selectedRace);
    },
    selectedCost () {
      this.loadData("/cards/?cost=" + this.selectedCost);
    },

  },
  mounted() {
    this.loadData("/cards/?page_size=15");
  },
};
</script>
<style scoped>
</style>