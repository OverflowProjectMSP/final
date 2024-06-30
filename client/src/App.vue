<script>
import FooterComp from "./components/ReuseComponets/FooterComp.vue";
import HeaderComp from "./components/ReuseComponets/HeaderComp.vue";
import PreloaderComp from "./PreloaderComp.vue";
import add from './AddComp.vue'
export default {
  components: {
    HeaderComp,
    FooterComp,
    PreloaderComp,
    add
  },
  data() {
        return {
            show: true,
        }
    },
    methods: {
        setShow() {
            setTimeout(() => {
                this.show = false
            }, 1000)
        }
    },
    mounted() {
        this.setShow();
        // setInterval(()=> {this.$emit('setShow', this.show)}, 1000)
    }
};
</script>

<template>
<header-comp />

<div class="co" v-if="this.show">
        <div class="load-item item1"></div>
        <div class="load-item item2"></div>
        <div class="load-item item3"></div>
        <div class="load-item item4"></div>
        <div class="load-item item5"></div>
</div>


  <div class="app" v-if="!this.show">
  <RouterView class="RouterView"/>
  <footer-comp />
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

.RouterView {
  min-height: 60.7vh !important;
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
    background-color: #4200FF;
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

@keyframes expand {
  0% {
    height: 15px;
  }
  100% {
    height: 40px;
  }
}
</style>
