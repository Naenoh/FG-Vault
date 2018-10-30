<template>
  <header class="post-header has-text-weight-bold columns">
    <div class="column is-6">Title</div>
    <div class="column is-2">Game</div>
    <div class="column is-1">Character</div>
    <div class="column is-2">Links</div>
    <div class="column is-1">Categories</div>
  </header>
</template>

<script>
export default {
  name: 'PostHeader'
}
</script>
<style>
  .post-header {
    border-top: 3px solid #00c4a7;
    border-bottom: 1px solid black;
    padding-left: 0.75rem;
  }
  @media screen and (max-width: 768px){
    .post-header {
      display: none;
    }
  }
</style>
