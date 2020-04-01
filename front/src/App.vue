<template>
  <v-app>
    <v-app-bar app color="#FFF" flat>
      Calculate
      <div class="d-flex align-center"></div>
      <v-spacer></v-spacer>
      anonymous
    </v-app-bar>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<style lang="sass" scoped>
  .main-content
    margin-top: 30px
</style>

<script>
// import Calculations from '@/components/Calculations';

export default {
  name: 'App',
  components: {
    // Calculations,
  },
  data: () => ({
    //
  }),
};
</script>
