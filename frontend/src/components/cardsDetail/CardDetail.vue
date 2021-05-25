<template>
  <card-layout>
    <template v-slot:cardBody>
      <b-table
        hover
        small
        caption-top
        stacked
        class="w-100"
        striped
        :items="info"
        :fields="columns"
        bordered
      >
        <template #cell(heroes)="data">
          {{ data.value.length ? data.value.join(", ") : "Neutral" }}
        </template>
        <template #cell(expansion)="data">
          {{ data.value.name }}
        </template>
      </b-table>
    </template>
  </card-layout>
</template>

<script>
import CardLayout from "@/layouts/CardLayout";

export default {
  name: "CardDetail",
  components: {
    CardLayout,
  },
  props: {
    cardId: {
      required: true,
    },
  },
  data() {
    return {
      info: [],
    };
  },

  computed: {
    columns() {
      let commonColumns = [
        "name",
        "card_type",
        "collection",
        "cost",
        "description",
        "expansion",
        "heroes",
        "quality",
        "race",
        "usage",
      ];
      if (this.info.length && this.info[0].card_type !== "spell") {
        commonColumns.push("attack");
        commonColumns.push("endurance");
      }
      return commonColumns;
    },
  },

  methods: {
    loadData(url) {
      this.$api.get(url).then((response) => {
        this.info = [response.data];
      });
    },
  },

  mounted() {
    this.loadData("/cards/" + this.cardId);
  },
};
</script>
<style scoped>
</style>