<template>
  <tr
    class="post-item"
    @click="toggleDesc">
    <td>
      <div>{{ post.title }}</div>
      <div
        v-if="post.description"
        :hidden="descHidden"
        class="is-size-7 desc"><br> {{ post.description }}</div>
      <div
        v-if="post.description"
        :hidden="!descHidden"
        class="is-size-7 desc-preview">{{ post.description }}</div>
    </td>
    <td>
      <a
        class="tag"
        @click="filterGame">{{ post.game.name }}</a>
    </td>
    <td>
      <a
        class="tag"
        @click="filterChar">{{ post.char.name }}</a>
    </td>
    <td>
      <div
        v-for="link in post.links"
        :key="link.id">
        <a
          :href="link.url">[{{ formatLink(link.url) }}]
        </a>
      </div>
    </td>
    <td>
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
    </td>
  </tr>
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
