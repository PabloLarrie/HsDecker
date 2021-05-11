<template>
  <div>
    <a href="#" class="logo">hsd</a>
    <ul>
      <li><a href="#" class="active">Decks</a></li>
      <li><a href="#">Cards</a></li>
      <li><a href="#">top10</a></li>
      <li><a href="#">Register</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
  data() {
    return {};
  },
};
</script>
<style scoped>
div {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
div .logo {
  color: #fff;
  font-weight: 700;
  text-decoration: none;
  font-size: 2em;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-left: 20px;
}
div ul {
  display: flex;
}
div ul li {
  list-style: none;
  margin-left: 20px;
}
div ul li a {
  text-decoration: none;
  padding: 6px 15px;
  color: #fff;
  border-radius: 20px;
}
div ul li a:hover,
div ul li a.active {
  background: #fff;
  color: #2b1055;
}
</style>