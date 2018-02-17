<template>
  <div class="post-list">
    <h1>{{ searchValue.text }} {{ searchValue.gameId }} {{ searchValue.charId }}</h1>
    <post-searchbar
      :searchval.sync="searchValue"
      :games="allGames"/>
    <table>
      <post-header/>
      <post-item
        v-for="post in filteredPosts.posts"
        :post="post"
        :key="post.id"/>
    </table>
    <post-form
      :games="allGames"
      :categories="allCategories"/>
  </div>
</template>

<script>
import PostItem from './PostItem.vue'
import PostHeader from './PostHeader.vue'
import PostSearchbar from './PostSearchbar.vue'
import PostForm from './PostForm.vue'
import gql from 'graphql-tag'

export default {
  name: 'PostList',
  apollo: {
    allPosts: gql`{allPosts{posts{title game{name} char{name} categories{name} links{url}}}}`,
    allGames: gql`{allGames{id name chars{id name}}}`,
    allCategories: gql`{allCategories{id name}}`,
    filteredPosts: {
      query: gql`query getFilteredPosts($title: String, $gameId: Int, $charId: Int){
           filteredPosts(title:$title,gameId:$gameId,charId:$charId){posts{title game{name} char{name} categories{name} links{url}}}
        }`,
      variables () {
        return {
          title: this.searchValue.text,
          gameId: this.searchValue.gameId,
          charId: this.searchValue.charId
        }
      }
    }
  },
  data () {
    return {
      allPosts: {},
      allGames: [],
      allCategories: [],
      filteredPosts: {},
      searchValue: {text: '', gameId: -1, charId: -1}
    }
  },
  components: { PostItem, PostHeader, PostSearchbar, PostForm }
}

</script>
