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
      selectedType: null,
      searchInfo: null,
      typeOptions: [
        { value: null, text: "All card types" },
        { value: "minion", text: "Minion" },
        { value: "spell", text: "Spell" },
        { value: "weapon", text: "Weapon" },
        { value: "hero", text: "Hero" },
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
  },
  watch: {
    size() {
      this.loadData("/cards/?page_size=" + this.size);
    },
    searchInfo() {
      this.loadData("/cards/?search=" + this.searchInfo);
    },
  },
  mounted() {
    this.loadData("/cards/?page_size=15");
  },
};
</script>
<style scoped>
</style>