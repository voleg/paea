<template>
  <v-row justify="center" align="center" class="main-content">
    <v-col lg=6 sm="10">
      <div v-if="features">
        <Calculations
                v-for="feature in features.implementations"
                v-bind:key="feature.name"
                :config="feature"
                :title="feature.name"

        />
      </div>
    </v-col>
  </v-row>
</template>

<script>
import Vue from 'vue'
// @ is an alias to /src
import Calculations from '@/components/Calculations.vue'

export default {
  name: 'Home',
  components: {
    Calculations
  },
  data: () => ({
      features: null
  }),
  async beforeMount () {
    const features = await Vue.http.get('http://localhost:8000/calculate/algo/features/')
    console.log(features)
    this.features = features.data
  }
}
</script>
