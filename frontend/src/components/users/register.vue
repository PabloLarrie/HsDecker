<template>
  <login-layout>
    <template v-slot:loginBody>
      <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">

          <b-form-group
              id="input-group-1"
              label="Username:"
              label-for="input-1"
          >
            <b-form-input
                id="input-1"
                v-model="form.username"
                placeholder="Enter username"
                icon="envelope"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              id="input-group-2"
              label="Password:"
              label-for="input-2"
          >
            <b-form-input
                id="input-2"
                v-model="form.password"
                type="password"
                placeholder="Enter password"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              id="input-group-3"
              label="e-mail:"
              label-for="input-3"
          >
            <b-form-input
                id="input-3"
                v-model="form.email"
                type="email"
                placeholder="Enter email"
                required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>

      </div>
    </template>
  </login-layout>
</template>

<script>
import LoginLayout from "@/layouts/LoginLayout";
import {mapMutations} from "vuex";

export default {
  name: "Register",
  components: {
    LoginLayout,
  },
  props: {},
  data() {
    return {
      form: {
        username: '',
        password: '',
        email: '',
      },
      show: true,
    }
  },

  methods: {
    ...mapMutations("userStore", ["setToken", "setUser"]),
    register() {
      this.$api.post("/token/", {
        "username": this.form.username,
        "password": this.form.password,
        "email": this.form.email,
      })
          .then((response) => {
            this.setToken(response.data.access);
            this.$api.get("/user/").then((response) => {
              this.setUser(response.data)
              this.$router.push({
                name: "login",
              });
            })
            // .catch
          });
    },
    onSubmit(event) {
      event.preventDefault()
      this.login()
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.username = ''
      this.form.password = ''
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  },
};
</script>
<style>
</style>