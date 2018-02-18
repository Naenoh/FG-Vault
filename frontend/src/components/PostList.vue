<template>
  <div class="post-list">
    <post-searchbar
      :searchval.sync="searchValue"
      :games="allGames"
      :categories="allCategories"/>
    <table class="table">
      <post-header/>
      <tbody>
        <post-item
          v-for="post in filteredPosts.posts"
          :post="post"
          :key="post.id"/>
      </tbody>
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
      query: gql`query getFilteredPosts($title: String, $gameId: Int, $charId: Int, $catIds: [Int]){
           filteredPosts(title:$title,gameId:$gameId,charId:$charId, catIds:$catIds){posts{title game{name} char{name} categories{name} links{url}}}
        }`,
      variables () {
        return {
          title: this.searchValue.text,
          gameId: this.searchValue.gameId,
          charId: this.searchValue.charId,
          catIds: this.searchValue.catId !== '-1' ? [this.searchValue.catId] : []
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
      searchValue: {text: '', gameId: -1, charId: -1, catId: '-1'}
    }
  },
  components: { PostItem, PostHeader, PostSearchbar, PostForm }
}

</script>
