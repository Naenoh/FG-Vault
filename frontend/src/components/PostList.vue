<template>
  <div class="post-list">
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
import gql from 'graphql-tag'

export default {
  name: 'PostList',
  props: {
    posts: {
      type: Array,
      default: function () {
        return {}
      }
    }
  },
  apollo: {
    allPosts: gql`{allPosts{posts{title game{name} char{name} categories{name} links{url}}}}`
  },
  data () {
    return {
      allPosts: ''
    }
  },
  components: { PostItem, PostHeader }
}

</script>
