<template>
  <div>
    <MyHeader></MyHeader>
    <MyBody></MyBody>
    <!-- <MyFooter></MyFooter> -->
  </div>
</template>


<script>
import MyHeader from "./components/Header";
import MyBody from "./components/Body";
// import MyFooter from "./components/Footer";

export default {
  name: "App",
  components: {
    MyHeader,
    MyBody,
    // MyFooter,
  },
  data() {
    return {};
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap");
* #app {
  scroll-behavior: smooth;
  margin: 0;
}
body {
  background: linear-gradient(#2b1055, #7597de);
  min-height: 100vh;
  text-align: center;
}
</style>
