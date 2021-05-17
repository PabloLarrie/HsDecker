<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">HSCARDS</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="Search by card name"
            ></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit"
              >Search</b-button
            >
          </b-nav-form>

          <b-nav-item-dropdown text="Type" right>
            <b-dropdown-item href="#">Creature</b-dropdown-item>
            <b-dropdown-item href="#">Spell</b-dropdown-item>
            <b-dropdown-item href="#">Weapon</b-dropdown-item>
            <b-dropdown-item href="#">Quest</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="Quality" right>
            <b-dropdown-item href="#">Free</b-dropdown-item>
            <b-dropdown-item href="#">Common</b-dropdown-item>
            <b-dropdown-item href="#">Rare</b-dropdown-item>
            <b-dropdown-item href="#">Epic</b-dropdown-item>
            <b-dropdown-item href="#">Legendary</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown text="Class" right>
            <b-dropdown-item href="#">Hunter</b-dropdown-item>
            <b-dropdown-item href="#">Priest</b-dropdown-item>
            <b-dropdown-item href="#">Warrior</b-dropdown-item>
            <b-dropdown-item href="#">Paladin</b-dropdown-item>
            <b-dropdown-item href="#">Mage</b-dropdown-item>
            <b-dropdown-item href="#">Druid</b-dropdown-item>
            <b-dropdown-item href="#">Warlock</b-dropdown-item>
            <b-dropdown-item href="#">Demon Hunter</b-dropdown-item>
            <b-dropdown-item href="#">Rogue</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-form-checkbox
            id="checkbox-1"
            v-model="status"
            name="checkbox-1"
            value="Standard"
            unchecked-value="Savage"
          >
            Standard?
          </b-form-checkbox>

          <div>
            Format: <strong>{{ status }}</strong>
          </div>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "CardsBar",
  data() {
    return {
      status: "Savage",
    };
  },
};
</script>
<style scoped>
</style>