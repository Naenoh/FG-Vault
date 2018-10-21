<template>
  <article
    class="post-item columns"
    @click="toggleDesc">
    <div class="column is-6">
      <div class="has-text-weight-bold">{{ post.title }}</div>
      <div
        v-if="post.description"
        :hidden="descHidden"
        class="is-size-7 desc"><br> {{ post.description }}</div>
      <div
        v-if="post.description"
        :hidden="!descHidden"
        class="is-size-7 desc-preview">{{ post.description }}</div>
    </div>
    <div class="column is-2">
      <a
        class="tag"
        @click="filterGame">{{ post.game.name }}</a>
    </div>
    <div class="column is-1">
      <a
        class="tag"
        @click="filterChar">{{ post.char.name }}</a>
    </div>
    <div class="column is-2">
      <div
        v-for="link in post.links"
        :key="link.id">
        <a
          :href="link.url">[{{ formatLink(link.url) }}]
        </a>
      </div>
    </div>
    <div class="column is-1">
      <div class="tags">
        <a
          v-for="cat in post.categories"
          :key="cat.id"
          class="tag"
          :data-id="cat.id"
          @click="filterCat">
          {{ cat.name }}
        </a>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  name: 'PostItem',
  props: {
    post: {
      type: Object,
      default: function () {
        return {}
      }
    }
  },
  data: function () {
    return {
      descHidden: true
    }
  },
  methods: {
    filterGame: function () {
      this.$emit('updateGameId', this.post.game.id)
    },
    filterChar: function () {
      this.$emit('updateCharId', { game: this.post.game.id, char: this.post.char.id })
    },
    filterCat: function (a) {
      this.$emit('updateCatIds', a.target.dataset.id)
    },
    formatLink: function (link) {
      return link.split('/')[2]
    },
    toggleDesc: function (a) {
      if (!a.target.classList.contains('tag')) {
        this.descHidden = !this.descHidden
      }
    }
  }
}
</script>
<style>
.desc {
  white-space: pre-line;
}
.desc-preview {
  opacity: 0.2;
  max-height: 1.7rem;
  overflow: hidden;
}
</style>
