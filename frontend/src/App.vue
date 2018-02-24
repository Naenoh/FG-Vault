<template>
  <div id="app">
    <site-header/>
    <post-list/>
    <site-footer/>
  </div>
</template>

<script>
import PostList from './components/PostList'
import SiteHeader from './components/SiteHeader.vue'
import SiteFooter from './components/SiteFooter.vue'

export default {
  name: 'App',
  components: {
    SiteHeader,
    PostList,
    SiteFooter
  }
}
</script>

<style type="text/scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}
</style>
