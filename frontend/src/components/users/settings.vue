<template>
  <settings-layout>
    <template v-slot:settingsBody>
      <b-table
        hover
        small
        caption-top
        class="w-100"
        striped
        :items="info"
        :fields="columns"
        bordered

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
import { store } from "@/vuex"


export default {
  name: "Settings",
  components: {
    SettingsLayout
  },

  data() {
    return {
      info: [],
      userSettings: [],
      columns: [
        "username",
        "user",
        "email",
        "bio" ,
        "avatar"
      ],
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
    this.loadData("/profiles/" + store.state.userStore.user.id);
  },
};
</script>
<style scoped>
</style>