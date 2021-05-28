<template>
  <b-container>
    <b-row>
      <slot name="loginBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "LoginLayout",
};
</script>