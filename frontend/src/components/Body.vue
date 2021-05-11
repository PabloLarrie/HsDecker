<template>
  <div>
    <h1>HSDECKER</h1>
    <h2>Best Deck Builder</h2>

    <div class="navbar">
      <!-- <div class="dropdown">
        <button class="dropbtn">
          Page
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a v-for="item in 26" :key="item.id">{{ item }}</a>
        </div>
      </div>

      <div class="dropdown">
        <button class="dropbtn">
          Card
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a v-for="item in info" :key="item.id">{{ item.name }}</a>
        </div>
      </div>

      <div class="dropdown">
        <button class="dropbtn">
          Type
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a v-for="item in info" :key="item.id">{{ item.card_type }}</a>
        </div>
      </div>

      <div class="dropdown">
        <button class="dropbtn">
          Collection
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a v-for="item in info" :key="item.id">{{ item.quality }}</a>
        </div>
      </div> -->
    </div>
    <div id="aplication" class="container">
      <div class="row">
        <button @click="previousPage" :disabled="previous === null">
          Página anterior
        </button>
        <button @click="nextPage" :disabled="next === null">
          Siguiente Página
        </button>
        <select v-model="size">
          <option value="15" selected>15</option>
          <option value="30">30</option>
          <option value="50">50</option>
        </select>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>ID</th>
              <th>Type</th>
              <th>Quality</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in info" :key="'row' + item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.card_type }}</td>
              <td>{{ item.quality }}</td>
            </tr>
          </tbody>
        </table>
        <button @click="previousPage" :disabled="previous === null">
          Página anterior
        </button>
        <button @click="nextPage" :disabled="next === null">
          Siguiente Página
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyBody",
  data() {
    return {
      tipoInput: "number",
      index: "number",
      info: [],
      next: null,
      previous: null,
      size: 15,
    };
  },
  methods: {
    loadData(url) {
      this.$api.get(url).then((response) => {
        this.info = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      });
    },
    nextPage() {
      this.loadData(this.next);
    },
    previousPage() {
      this.loadData(this.previous);
    },
  },
  mounted() {
    this.loadData("/cards/?page_size=30");
  },
};
</script>
<style scoped>
table {
  margin: auto;
  color: #fff;
}
p {
  color: black;
}
h1,
h2 {
  color: #fff;
  padding: 0px;
}
div .container {
  block-size: 0px;
}
select {
  padding-right: 30px;
  font-size: 20px;
  border-radius: 20px;
  width: 8%;
}
option {
  list-style: none;
  color: rgb(0, 0, 0);
  padding-right: 30px;
  font-size: 20px;
}
.navbar {
  overflow: hidden;
  background-color: transparent;
}

.navbar a {
  float: center;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover,
.dropdown:hover .dropbtn {
  background-color: rgb(255, 255, 255);
  color: #2e165b;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>