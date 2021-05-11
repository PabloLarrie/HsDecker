<template>
  <div>
    <a href="#" class="logo">Empresa</a>
    <ul>
      <li>
        <a href="#" class="active">This is a Larrie&Aitor S.A. production</a>
      </li>
      <li>
        <a href="#" class="active"
          >0 animales han sido heridos durante la creación de esta web</a
        >
      </li>
      <li>
        <a href="#" class="active">Emisión Neutra de Carbono desde 2021</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Myfooter",
  data() {
    return {};
  },
};
</script>
<style scoped>
div {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 30px, 100px;
  /* display: flex;
  justify-content: space-between;
  align-items: center; */
  z-index: 10000;
}
div .logo {
  color: #fff;
  font-weight: 700;
  text-decoration: none;
  font-size: 15px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-left: 20px;
}
div ul {
  display: flex;
  justify-content: center;
  align-items: center;
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