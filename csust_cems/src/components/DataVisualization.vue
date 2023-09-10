<template>
  <div>
    <BonusPoints/>
    <ComprehensiveCapability/>
  </div>
</template>

<script>
import ComprehensiveCapability from './echarts/ComprehensiveCapability.vue'
import BonusPoints from './echarts/BonusPoints.vue'
export default{
  name: 'DataVisualization',
  components: {
    ComprehensiveCapability,
    BonusPoints,
  },
  data() {
    return {

    };
  },
  methods: {

  }
};
</script>

<style scoped>

</style>
