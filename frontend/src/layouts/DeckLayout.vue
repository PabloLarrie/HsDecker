<template>
  <b-container>
    <b-row>
      <slot name="deckBody" />
    </b-row>
    <b-row>
      <slot name="cardContent" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "DeckLayout",
};
</script>