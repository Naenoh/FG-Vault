<template>
  <div class="site-header">
    <div class="top-line"/>
    <div class="title-cont">
      <p class="title is-1">FG <span class="emphasized">V</span>ault</p>
      <p class="subtitle">A Fighting Game Links Directory</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteHeader'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .top-line {
    width: 100%;
    height: 5px;
    background-color: #00c4a7;
  }
  .site-header {
    margin-bottom: 10px;
  }
  .title-cont {
    text-align: center;
  }
  .emphasized {
    color: #00c4a7;
  }
</style>
