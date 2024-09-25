<script>
export default {
  data() {
    return {

    }
  },
  props: {
    developer: Object,
  }
}
</script>

<template>
  <div name="modal-fade" class="d-flex justify-content-center align-items-center">
    <div class="modal-backdrop" role="button" @click="$emit('showDev')"></div>
    <div class="window">
      <span class="close opacity-50 fs-2" @click="$emit('showDev')"><img src="../../assets/FAQ/close.svg" alt="Close"></span>
      <div class="info-block d-flex gap-5 align-items-center">
        <img class="rounded-5 user-select-none max-h-50" :src="developer.imageProfileDS"
             :alt="developer.name">
        <!-- НЕ ТРОГАТЬ!!!!!!!!!!!!!! -->
        <!-- <img class="rounded-2 user-select-none d-none" src="../../assets/Main/kostya.jpg">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/jena.png">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/sanya.png">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/vanya.jpg">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/maksym.jpg">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/therisingdream.png">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/nekit.jpg">
        <img class="rounded-2 user-select-none d-none" src="../../assets/Main/kenma.gif"> -->
        <div class="about-block d-flex flex-column gap-1">
          <h2 class="fw-bold">{{ developer.name }}</h2>
          <span class="text-muted">{{ developer.role }}</span>
          <b class="mt-3">Как найти: </b>
          <ul class="ps-0">
            <li v-if="developer.dsProfile">Дискорд: @{{ developer.dsProfile }}</li>
            <li v-if="developer.tgProfile">Телеграм: @{{ developer.tgProfile }}</li>
            <li v-if="developer.vkProfile">ВК: @{{ developer.vkProfile }}</li>
            <li v-if="developer.upFollow">Аккаунт UpFollow: <a class='upf-link' :href="`/Profile/${developer.upFollow}`">Клик</a></li>
          </ul>
        </div>
      </div>
    </div>
    <!-- </div> -->
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: #fff;
}

.upf-link {
  color: #000;
}

.close {
  font-size: 40px;
  padding: 0 20px;
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
  transition: 300ms;
}


.parent {
  z-index: 52;
}

.window {
  position: fixed;
  top: 25%;
  z-index: 33333;
  border-radius: 30px;
  background-color: #ffffff;
  border: 4px solid #2a2a2a;


  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  padding: 30px;

  font-family: "Rubik", sans-serif;
}

img {
  max-height: 400px;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
}

@media (hover: hover) {
  .close:hover {
    opacity: 1 !important;
  }
}

@media (max-width: 800px) {
  .info-block {
    flex-direction: column !important;
    padding: 5px;
  }

  img {
    max-width: 90%;
  }

  .window {
    top: 15%;
    width: 90%;
    padding: 20px !important;
    gap: 0 !important;
  }

  .close {
    top: 5px;
    right: 5px;
  }
}

@media (min-width: 3400px) {
  img {
    max-width: 500px;
    max-height: 500px;
  }

  .about-block h2 {
    font-size: 50px;
  }

  .about-block span {
    font-size: 30px;
  }

  .about-block b {
    font-size: 26px;
  }

  .about-block li {
    font-size: 26px;
  }
}

@media (min-width: 4200px) {
  img {
    max-width: 600px;
    max-height: 600px;
  }

  .about-block h2 {
    font-size: 60px;
  }

  .about-block span {
    font-size: 40px;
  }

  .about-block b {
    font-size: 48px;
  }

  .about-block li {
    font-size: 48px;
  }

  .close {
    font-size: 70px !important;
  }
}
</style>
