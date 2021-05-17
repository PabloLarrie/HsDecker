<template>
  <div class="d-flex justify-content-end">
    <b-button
      @click="$emit('previousPageClick')"
      class="me-2"
      :disabled="previous === null"
    >
      Prev
    </b-button>
    <b-button
      @click="$emit('nextPageClick')"
      class="me-2"
      :disabled="next === null"
      >Next</b-button
    >
    <select v-model="innerValue" class="me-5">
      <option value="15" selected>15</option>
      <option value="30">30</option>
      <option value="50">50</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "TablePagination",
  props: {
    previous: {
      required: true,
    },
    next: {
      required: true,
    },
    value: {},
  },
  data() {
    return {
      innerValue: 0,
    };
  },
  watch: {
    innerValue(newVal) {
      this.$emit("input", newVal);
    },
    value(newVal) {
      this.innerValue = newVal;
    },
  },
  created() {
    if (this.value) {
      this.innerValue = this.value;
    }
  },
};
</script>
