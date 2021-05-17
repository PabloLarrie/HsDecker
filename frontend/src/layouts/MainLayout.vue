<template>
  <b-container>
    <b-row>
      <slot name="header" />
    </b-row>
    <b-row>
      <slot name="body" />
    </b-row>
    <b-row>
      <slot name="footer" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "MainLayout",
};
</script>