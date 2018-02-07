<template>
  <div class="post-list">
    <h1>{{ searchValue.text }} {{ searchValue.gameId}}</h1>
    <post-searchbar
      :searchval.sync="searchValue"
      :games="allGames"/>
    <table>
      <post-header/>
      <post-item
        v-for="post in allPosts.posts"
        :post="post"
        :key="post.id"/>
    </table>
  </div>
</template>

<script>
import PostItem from './PostItem.vue'
import PostHeader from './PostHeader.vue'
import PostSearchbar from './PostSearchbar.vue'
import gql from 'graphql-tag'

export default {
  name: 'PostList',
  apollo: {
    allPosts: gql`{allPosts{posts{title game{name} char{name} categories{name} links{url}}}}`,
    allGames: gql`{allGames{id name chars{id name}}}`
  },
  data () {
    return {
      allPosts: {},
      allGames: [],
      searchValue: {text: '', gameId: -1}
    }
  },
  components: { PostItem, PostHeader, PostSearchbar }
}

</script>
