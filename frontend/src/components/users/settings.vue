<template>
  <settings-layout>
    <template v-slot:settingsBody>
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
        <template #cell(profile)="data">
          {{ data.value.name }}
        </template>
      </b-table>
    </template>
  </settings-layout>
</template>

<script>
import SettingsLayout from "@/layouts/SettingsLayout";

export default {
  name: "Settings",
  components: {
    SettingsLayout
  },
  props: {
    userId: {
      required: true,
    },
  },

  data() {
    return {
      info: [],
      userSettings: [],
      columns: [
          "id",
          "name",
          "hero_class",
          "standard",
          "complete",
          "size",
          "total_cards",
      ],
      settingColumns: [
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
            this.userSettings = response.data.profile;
          });

    },
  },
  mounted() {
    this.loadData("/profiles/" + this.userId);
  },
};
</script>
<style scoped>
</style>