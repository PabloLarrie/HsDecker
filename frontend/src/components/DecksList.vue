<template>
  <div>
    <table-pagination
      :next="next"
      :previous="previous"
      v-model="size"
      @nextPageClick="nextPage"
      @previousPageClick="previousPage"
    />

    <b-row>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>Type</th>
            <th>Quality</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in info" :key="'row' + item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.card_type }}</td>
            <td>{{ item.quality }}</td>
          </tr>
        </tbody>
      </table>
    </b-row>

    <table-pagination
      :next="next"
      :previous="previous"
      v-model="size"
      @nextPageClick="nextPage"
      @previousPageClick="previousPage"
    />
  </div>
</template>

<script>
import TablePagination from "@/components/table/TablePagination";
export default {
  name: "DecksList",
  components: {
    TablePagination,
  },
  data() {
    return {
      tipoInput: "number",
      index: "number",
      info: [],
      next: null,
      previous: null,
      size: 15,
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
    size(newSize) {
      this.loadData("/decks/?page_size=" + newSize);
    },
  },
  mounted() {
    this.loadData("/decks/?page_size=15");
  },
};
</script>
<style scoped>
</style>