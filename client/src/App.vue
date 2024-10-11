<script>
import FooterComp from "./components/ReuseComponets/FooterComp.vue";
// import HeaderComp from "./components/ReuseComponets/HeaderComp.vue";
import HeaderComp from "./components/ReuseComponets/NewnavBar.vue";
import PreloaderComp from "./PreloaderComp.vue";

export default {
  components: {
    HeaderComp,
    FooterComp,
    PreloaderComp,
  },
  data() {
    return {
      show: true,
      load: true,
      onload: false,
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
    window.onload = () => { 
      // Используем стрелочную функцию
      setTimeout(() => {
        console.log("Страница полностью загружена!");
        this.load = false;
        this.onload = true;
        console.log(this.load);
      }, 1000);
    };
  },
};
</script>

<template>
  <preloader-comp v-if="load"></preloader-comp>
  <div v-if="onload">
    <div class="headernew" style="margin-bottom: 80px" v-if='this.$route.path != `/`'>
      <header-comp class="header" />
    </div>
    <div class="f" style="display: flex; flex-direction: column">
      <RouterView class="RouterView" style="padding-top: 45px; flex-grow: 1" />
      <footer-comp v-if="onload" />
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.cdnfonts.com/css/rubik");

html {
  margin: 0;
  background-color: #eef1f4;
}

main {
  margin: 10px;
}

template {
  font-family: Rubik !important;
  margin: 0;
}

.f {
  display: flex;
}

.RouterView {
  min-height: 10 0vh !important;
}

/* прелоудер */
.co {
  width: 90px;
  height: 30px;
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  margin-left: auto;
  margin-right: auto;
}

.load-item {
  width: 15px;
  height: 15px;
  background-color: #4200ff;
}

.item1 {
  animation: expand 0.4s infinite alternate;
}

.item2 {
  animation: expand 0.4s infinite alternate;
}

.item3 {
  animation: expand 0.4s infinite alternate;
}

.item4 {
  animation: expand 0.4s infinite alternate;
}

.item5 {
  animation: expand 0.4s infinite alternate 200ms;
}
.header {
  position: fixed;
  top: 10px;
  z-index: 15000;
}
.headernew {
  display: flex;
  justify-content: center;
  width: 100%;
}

@keyframes expand {
  0% {
    height: 15px;
  }
  100% {
    height: 40px;
  }
}
</style>
