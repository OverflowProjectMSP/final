<script>
export default {
  data() {
    return {
      show: true,
    };
  },
  methods: {
    setShow() {
      setTimeout(() => {
        this.show = false;
      }, 1000);
    },
  },
  mounted() {
    this.setShow();
    // setInterval(()=> {this.$emit('setShow', this.show)}, 1000)
  },
};
</script>

<template>
  <div class="container">
    <img src="../assets/preloader.svg" alt="" class="img" />
  </div>
</template>

<style scoped>
.img {
  width: 100px;
  height: 100px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 60vh;
}

.load-item {
  width: 15px;
  height: 15px;
  background-color: #4200ff;
}
</style>
