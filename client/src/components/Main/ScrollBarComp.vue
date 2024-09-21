<script>
import DeveloperProfile from './DeveloperProfile.vue';
import kosty_py_img from "@/assets/Main/kostya.jpg";
import kinestrik_img from "@/assets/Main/jenya8.png";
import sanya_img from "@/assets/Main/sanya.png";
import vanya_img from "@/assets/Main/vanya.jpg";
import maxim_img from "@/assets/Main/maksym.jpg";
import egor_img from "@/assets/Main/therisingdream.png";
import nekit_img from "@/assets/Main/nekit.jpg";


export default {
  components: { DeveloperProfile,},
  data() {
    return {
      devolepers: [
        {
          name: `Суров Константин`,
          role: `Тимлид/Старший Бэкенд разработчик`,
          imageProfileDS: kosty_py_img,
          dsProfile: `kosty_py`
        },
        {
          name: `Шадловский Евгений`,
          role: `Заместитель тимлида/Старший Фронтенд разработчик`,
          imageProfileDS: kinestrik_img,
          dsProfile: `kinestrik`
        },
        {
          name: `Корецкий Александр`,
          role: `Заместитель ведущего Бэкенд разработчика`,
          imageProfileDS: sanya_img,
          dsProfile: `febolo`,
          tgProfile: `febolo`,
          vkProfile: `febolo`,
        },
        {
          name: `Горбенко Иван`,
          role: `Заместитетель ведущего Фронтенд разработчика`,
          imageProfileDS: vanya_img,
          dsProfile: `garleenn`,
          tgProfile: `Garleen`,
        },
        {
          name: `Сары Максим`,
          role: `Фронтенд разработчик`,
          imageProfileDS: maxim_img,
          dsProfile: `habbock`,
          tgProfile: `HaBBeRL`,
        },
        {
          name: `Лазутин Егор`,
          role: `Фронтенд разработчик`,
          imageProfileDS: egor_img,
          dsProfile: `therisingdream`
        },
        {
          name: `Маврин Никита`,
          role: `Главный дизайнер`,
          imageProfileDS: nekit_img,
          dsProfile: `nikit0_17`
        },
        // {
        //     name: `Беднин Арсений`,
        //     role: `Дизайнер`,
        //     imageProfileDS: `kenma-CP1HimCf.gif`,
        //     dsProfile: `kenmaxd`
        // },
      ],

      index: 0,
      index1: 1,
      index2: 2,
      index3: 3,

      names: [],
      roles: [],
      images: [kosty_py_img, kinestrik_img, sanya_img, vanya_img, maxim_img, egor_img, nekit_img],

      isHide: false,
      indexOfDev: null,

      isAllLoad: false,
    }
  },
  mounted() {
    this.resImage();
  },
  methods: {
    resImage() {
      for (let i = 0; i < this.devolepers.length; i++) {
        this.names.push(this.devolepers[i].name);
        this.roles.push(this.devolepers[i].role);
        this.preloader();
      }
    },
    nextDev() {
      this.index++;
      this.index1++;
      this.index2++;
      this.index3++;
      if (this.index == this.roles.length) {
        this.index = 0;
      } else if (this.index1 == this.roles.length) {
        this.index1 = 0;
      } else if (this.index2 == this.roles.length) {
        this.index2 = 0;
      } else if (this.index3 == this.roles.length) {
        this.index3 = 0;
      }

    },
    prevDev() {
      this.index--;
      this.index1--;
      this.index2--;
      this.index3--;
      if (this.index < 0) {
        this.index = this.roles.length - 1;
      }
      if (this.index1 < 0) {
        this.index1 = this.roles.length - 1;
      }
      if (this.index2 < 0) {
        this.index2 = this.roles.length - 1;
      }
      if (this.index3 < 0) {
        this.index3 = this.roles.length - 1;
      }
    },

    showDev(index) {
      this.isHide = !this.isHide;
      this.indexOfDev = index;
    },

    async preloader() {
        if (this.images.length && this.names.length && this.roles.length) {
          this.isAllLoad = true;
        }
    },
  }
}
</script>

<template>
  <div>
    <hr class="hr-end">
    <div class="develop d-flex gap-3 align-items-center gap-2 flex-column">
      <h1>Команда разработчиков</h1>
      <div class="dev-container d-flex flex-row">
        <div @click="prevDev" role="button"
             class="arrow arrow-left mx-5 d-flex justify-content-center align-items-center gap-2 fs-1 fw-bold user-select-none">
          <
        </div>
        <div class="collaps-container d-flex justify-content-center flex-wrap gap-4" v-if='this.isAllLoad'>
          <div class="dev-card d-flex flex-column gap-0 align-items-center" @click="showDev(this.index)">
            <img class="rounded-2 user-select-none" :src="images[index]"
                 :alt="names[index]">
  
            <h4 class="mt-2 text-center">{{ names[index] }}</h4>
            <span class="text-center">{{ roles[index] }}</span>
          </div>
          <div class="dev-card dev-card-2 d-flex flex-column gap-0 align-items-center" @click="showDev(this.index1)">
            <img class="rounded-2 user-select-none" :src="images[index1]"
                 :alt="names[index1]">
            <h4 class="mt-2 text-center">{{ names[index1] }}</h4>
            <span class="text-center">{{ roles[index1] }}</span>
          </div>
          <div class="dev-card dev-card-3 d-flex flex-column gap-0 align-items-center" @click="showDev(this.index2)">
            <img class="rounded-2 user-select-none" :src="images[index2]"
                 :alt="names[index2]">
            <h4 class="mt-2 text-center">{{ names[index2] }}</h4>
            <span class="text-center">{{ roles[index2] }}</span>
          </div>
          <div class="dev-card dev-card-4 d-flex flex-column gap-0 align-items-center" @click="showDev(this.index3)">
            <img class="rounded-2 user-select-none" :src="images[index3]"
                 :alt="names[index3]">
            <h4 class="mt-2 text-center">{{ names[index3] }}</h4>
            <span class="text-center">{{ roles[index3] }}</span>
          </div>
        </div>
        <div @click="nextDev" role="button"
             class="arrow arrow-right mx-5 d-flex justify-content-center align-items-center gap-2 fs-1 fw-bold user-select-none">
          >
        </div>
      </div>
    </div>
  
    <DeveloperProfile v-if="this.isHide" :developer="devolepers[indexOfDev]" @showDev="showDev"/>
  </div>
  <div v-if='!this.isAllLoad'>
    <div class="co">
    <div class="load-item item1"></div>
    <div class="load-item item2"></div>
    <div class="load-item item3"></div>
    <div class="load-item item4"></div>
    <div class="load-item item5"></div>
</div>
  </div>

</template>

<style scoped>
.d-none {
  display: none;
}

.arrow {
  margin-top: -90px;
}

.develop {
  height: 500px;
  margin-bottom: 0;
  justify-content: start !important;
  /* margin-bottom: 30px; */
}


.dev-card {
  max-width: 250px;
  height: 342.8px;
  transition: all 300ms;
  cursor: pointer;
}

@media (hover: hover) {
  .dev-card:hover {
    transform: translateY(-10px)
  }
}

.dev-card img {
  max-width: 250px;
  max-height: 250px;
  width: fit-content;
}

@media (max-width: 1624px) {
  .dev-card-4 {
    display: none !important;
  }
}

@media (max-width: 1224px) {

  .dev-card-3,
  .dev-card-4 {
    display: none !important;
  }
}

@media (max-width: 880px) {

  .dev-card-2,
  .dev-card-3,
  .dev-card-4 {
    display: none !important;
  }

  /* hr {
      margin-top: 50px !important;
  } */
  .develop {
    margin: 30px 10px !important;
  }

  .arrow {
    margin-left: 30px !important;
    margin-right: 30px !important;
  }
}

@media (max-width: 829px) {
  hr {
    margin-top: 100px;
  }
}

@media (max-width: 539px) {
  hr {
    margin-top: 150px;
  }
}

@media (max-width: 453px) {
  hr {
    margin-top: 200px;
  }
}

@media (min-width: 2100px) {
  .develop {
    height: 600px;
  }

  .dev-card {
    max-width: 300px;
  }
  
  .dev-card img {
    max-width: 300px;
    max-height: 300px;
  }
  
  .dev-card h4 {
    font-size: 33px;
  }

  .dev-card span {
    font-size: 25px;
  }
  
}

@media (min-width: 3400px) {
  .develop {
    height: 700px;
  }
  
  .dev-card {
    max-width: 400px;
  }

  .dev-card img {
    max-width: 370px;
    max-height: 370px;
  }

  .dev-card h4 {
    font-size: 38px
  }

  .dev-card span {
    font-size: 26px;
  }
}

@media (min-width: 4200px) {
  .develop {
    height: 800px;
    position: relative;
  }

  .dev-card {
    max-width: 600px !important;
  }

  .dev-card img {
    max-width: 460px;
    max-height: 460px;
  }

  .dev-card h4 {
    font-size: 50px;
  }
  
  .dev-card span {
    font-size: 34px;
    font-weight: 400;
  }

  .hr-end {
    margin-top: 140px;
  }

  .arrow {
    margin-top: 120px;
    font-size: 50px !important;
  }

  .dev-container {
    max-width: 3000px;
  }
}


</style>
