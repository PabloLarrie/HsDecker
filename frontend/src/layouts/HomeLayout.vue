<template>
  <b-container>
    <b-row>
      <slot name="homeBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "HomeLayout",
};
</script>