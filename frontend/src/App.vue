<template>
  <div id="app">
    <PostList :posts="posts"/>
  </div>
</template>

<script>
import PostList from './components/PostList'
import sampledata from './assets/sampledata'

export default {
  name: 'App',
  components: {
    PostList
  },
  data: function () {
    return {
      posts: sampledata.data.allPosts.posts
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
