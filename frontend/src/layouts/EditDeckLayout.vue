<template>
  <b-container>
    <b-row>
      <slot name="deckBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "EditDeckLayout",
};
</script>