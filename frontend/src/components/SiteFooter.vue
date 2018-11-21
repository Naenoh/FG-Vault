<template>
  <div class="site-footer">
    <p class="is-size-7">Made by
      <a href="https://twitter.com/Naen0">Naeno</a>
      -
      <a
        href="#"
        @click="toggleModal"> What is this ? </a>
    </p>
    <div
      class="modal"
      :class="{ 'is-active': visible }">
      <div
        class="modal-background"
        @click="toggleModal"/>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">FAQ</p>
          <button
            class="delete"
            aria-label="close"
            @click="toggleModal"/>
        </header>
        <section class="modal-card-body">
          Hi guys
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteFooter',
  data: function () {
    return {
      visible: false
    }
  },
  methods: {
    toggleModal: function () {
      this.visible = !this.visible
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .site-footer{
    text-align: center;
    margin-top: 10px;
  }
</style>
