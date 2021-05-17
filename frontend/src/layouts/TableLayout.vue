<template>
  <b-container>
    <b-row>
      <b-col>
        <slot name="filters" />
      </b-col>
      <b-col>
        <slot name="pagination-top" />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <slot name="table" />
      </b-col>
    </b-row>
    <b-row class="d-flex justify-content-end">
      <b-col> <slot name="pagination-bottom" /> </b-col
    ></b-row>
  </b-container>
</template>

<script>
export default {
  name: "TableLayout",
};
</script>