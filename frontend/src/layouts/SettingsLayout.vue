<template>
  <b-container>
    <b-row>
      <slot name="settingsBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "SettingsLayout",
};
</script>