<script>
export default {
  data() {
    return {
      count: 0,
      isHidden: true, // Управляем показом/скрытием блока
    };
  },
  methods: {
    clickpas() {
      this.count++;
      
      if (this.count === 10) {
        this.isHidden = !this.isHidden;
        this.count = 0; // Сбрасываем счетчик
      }
    }
  }
};
</script>

<template>
    <div class="background">
        <h1 @click="clickpas">404</h1>
        <a href="/"><button>На главную</button></a>
        <div class="pashal"  :class="{ 'hide': isHidden }">
          <img src="../../assets/Main/arrow-top.svg" alt="">
          <h3>Дурак? Сюда кликать надо</h3>
        </div>
        
    </div>
</template>

<style scoped>
.background {
    width: 100%;
    height: 92vh;

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 70px;

    user-select: none;
}

.hide {
    display: none !important;
}

.pashal {
    margin-top: -30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

img {
    width: 70px;
}

h1 {
    font-size: 130px;
    font-weight: 500;
    color: #161616;
}

button {
    width: 190px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;

    font-weight: 600;
    font-size: 20px;

    transition: all 100ms;
}


button:active {
    background-color: #4200FF;
    color: #fff;
}

@media (hover: hover) {
    button:hover {
        background-color: #2d00aa;
        border-radius: 25px 5px;
    }
    
    button:active {
        background-color: #240088;
    }
}

@media(max-width: 600px) {
    h1 {
        font-size: 90px;
    }
}

</style>
