<template>
  <article
    class="post-item columns is-multiline is-mobile"
    @click="toggleDesc"
    :title="formatedTime">
    <div class="column is-6-desktop is-12-mobile">
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
    <div class="column is-2-desktop is-6-mobile">
      <a
        class="tag"
        @click="filterGame">{{ post.game.name }}</a>
    </div>
    <div class="column is-1-desktop is-4-mobile is-offset-2-mobile">
      <a
        class="tag"
        @click="filterChar">{{ post.char.name }}</a>
    </div>
    <div class="column is-2-desktop is-12-mobile">
      <div
        class="post-link"
        v-for="link in post.links"
        :key="link.id">
        <a
          target="_blank"
          class="tag is-link"
          :href="link.url">{{ formatLink(link.url) }}
        </a>
      </div>
    </div>
    <div class="column is-1-desktop is-12-mobile">
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
    filterCat: function (evt) {
      this.$emit('updateCatIds', evt.target.dataset.id)
    },
    formatLink: function (link) {
      return link.split('/')[2]
    },
    toggleDesc: function (evt) {
      const classList = evt.target.classList
      if (!classList.contains('tag') && !classList.contains('desc')) {
        this.descHidden = !this.descHidden
      }
    }
  },
  computed: {
    formatedTime: function () {
      return 'Post #' + this.post.id + ' - Submitted on ' + new Date(this.post.timeCreated).toString()
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
.post-item {
  border-top: 1px solid #D3D3D3;
  padding-left: 0.75rem;
  overflow: hidden;
}
.post-item:hover {
  background-color: #F5F5F5;
}

@media screen and (max-width: 768px){
    .post-item {
      border-top: 2px solid black;
      padding: 0.75rem;
    }
    .column {
      padding: 0.25rem;
    }
    .post-link {
      text-align: center;
      padding: 0.5rem;
    }
  }
</style>
