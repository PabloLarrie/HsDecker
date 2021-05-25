<template>
  <b-container>
    <b-row>
      <slot name="cardBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "CardLayout",
};
</script>