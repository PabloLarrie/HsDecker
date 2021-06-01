<template>
  <login-layout>
    <template v-slot:loginBody>
      <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">

          <b-form-group id="input-group-1" label="Username:" label-for="input-1">
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

          <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group
                v-model="form.checked"
                id="checkboxes-4"
                :aria-describedby="ariaDescribedby"
            >
              <b-form-checkbox value="Remember">Remember me</b-form-checkbox>
              <b-form-checkbox value="Show">Show Password</b-form-checkbox>
            </b-form-checkbox-group>
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
  name: "Login",
  components: {
    LoginLayout,
  },
  props: {},
  data() {
    return {
      form: {
        username: '',
        password: '',
        checked: []
      },
      show: true,
    }
  },

  methods: {
    ...mapMutations("userStore", ["setToken", "setUser"]),
    login() {
      this.$api.post("/token/", {
        "username": this.form.username,
        "password": this.form.password,
      })
          .then((response) => {
            this.setToken(response.data.access);
            this.$api.get("/user/").then((response) => {
              this.setUser(response.data)
              this.$router.push({
                name: "cards",
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