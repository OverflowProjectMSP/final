<script setup>

</script>

<template>
  <div class="window">
    <div class="main-container">
      <img class="mount" src="../../assets/Telegram/mounted.png" alt="">
      <div class="close" @click="gotoProfile">
        <img src="../../assets/Telegram/close-icon.svg" alt="">
      </div>
      <div class="link-cont">
        <img src="../../assets/Telegram/telegram-icon.svg" alt="">
        <h2>Привязка Telegram</h2>
        <div class="link-good">
          <p class="text-def">
            1. Зайдите в нашего телеграмм бота и получите ссулку на аунтификацию <br>
            2. Пройдите по ссылке (она действует 12 часов, какже необходимо войти в аккаунт)<br>
            3. Вы приявзяли свой телеграмм! <br>
            <br>
            С привязанным телеграмм Вы будете получать информацию о новых ответах и комментариях на Ваши публикации
          </p>
        </div>
      </div>

      <div class="link">
        <img src="../../public/link-icon.svg" alt="">
      </div>
    </div>
  </div>

</template>

<style scoped>
.window {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ECEDEE;

  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.main-container {
  display: flex;
  justify-content: space-between;

  align-items: center;
  width: 1245px;
  height: 715px;
  background-color: #ffffff;
  border-radius: 50px;
  padding: 0;
  position: relative;
}

.mount {
  /* position: absolute; */
  width: 502px;
  height: 715px;
}

.link-cont {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 916px;
  justify-content: center;
  align-items: center;
  gap: 30px;
}

.link-cont h2 {
  font-size: 50px;
  font-weight: bold;
  user-select: none;
}

.link-cont img {
  width: 150px;
}

.link-good {
  width: 500px;
  background-color: #EAE9E9;
  border-radius: 15px;

  padding: 25px 23px 25px 23px;
}

.text-def {
  text-align: left;
  font-size: 27px;
  font-weight: 450;
  line-height: 30px;
  margin: 0;
  color: #212529;
}

.bt {
  width: 230px;
  height: 78px;
  border-radius: 15px;
  background-color: #EAE9E9;
  border: none;

  transition: all 100ms;
}

.bt:hover {
  background-color: #cfcfcf;
}

.bt:active {
  background-color: #a5a5a5;
}

.btns {
  display: flex;
  flex-direction: row;
  gap: 40px;
}

.close img {
  width: 15px;
}

.close {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 50px;
  right: 60px;
  background-color: #EAE9E9;
  width: 50px;
  height: 50px;
  border-radius: 50px;
  cursor: pointer;
  user-select: none;
}

.close:hover {
  background-color: #cfcfcf;
}

.close:active {
  background-color: #a5a5a5;
}

.link img {
  width: 40px;
}

.link {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: 30px;
  right: 30px;
  width: 60px;
  height: 60px;
  background-color: #ffffff;
  border-radius: 50px;
  cursor: pointer;

  transition: all 100ms;
}

.link:hover {
  background-color: #cfcfcf;
}

.link:active {
  background-color: #a5a5a5;
}


/* АДАПТИВКА */


@media (max-width: 1280px) {
  .main-container {
    width: 1000px;
    height: 550px;
  }

  .mount {
    width: 370px;
    height: 550px;
  }

  .link-cont img {
    width: 100px;
  }

  .link-cont h2 {
    font-size: 40px;
  }

  .link-good {
    width: 400px;
    height: 90px;
    padding: 17px 10px 17px 10px;
  }

  .text-def {
    font-size: 22px;
    line-height: 25px;
  }

  .bt {
    width: 180px;
    height: 60px;
  }
}

@media (max-width: 1015px) {
  .main-container {
    width: 700px;
    height: 400px;
  }

  .mount {
    width: 280px;
    height: 400px;
  }

  .link-cont {
    gap: 10px;
  }

  .link-cont img {
    width: 70px;
  }

  .link-cont h2 {
    font-size: 30px;
  }

  .link-good {
    width: 300px;
    height: 60px;
    padding: 10px 6px 10px 6px;
  }

  .text-def {
    font-size: 17px;
    line-height: 20px;
  }

  .bt {
    width: 130px;
    height: 50px;
  }

  .close {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 5px;
    right: 5px;
    background-color: #EAE9E9;
    width: 40px;
    height: 40px;
    border-radius: 50px;
    cursor: pointer;
    user-select: none;
  }

  .link img {
    width: 30px;
  }

  .link {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    bottom: 15px;
    right: 15px;
    width: 50px;
    height: 50px;
    background-color: #ffffff;
    border-radius: 50px;
    cursor: pointer;

    transition: all 100ms;
  }
}

@media (max-width: 740px) {
  .mount {
    display: none;
  }

  .main-container {
    width: 500px;
    height: 600px;
  }

  .link-cont {
    gap: 20px;
  }

  .link-cont img {
    width: 120px;
  }

  .link-cont h2 {
    font-size: 40px;
  }

  .link-good {
    width: 400px;
    height: 80px;
    padding: 20px 17px 20px 17px;
  }

  .text-def {
    font-size: 20px;
    line-height: 23px;
  }

  .bt {
    width: 180px;
    height: 60px;
  }
}

@media (max-width: 520px) {
  .main-container {
    width: 350px;
    height: 500px;
  }

  .link-cont {
    gap: 10px;
  }

  .link-cont img {
    width: 80px;
  }

  .link-cont h2 {
    font-size: 30px;
  }

  .link-good {
    width: 300px;
    padding: 15px 5px 15px 5px;
  }

  .text-def {
    font-size: 18px;
    line-height: 22px;
  }

  .bt {
    width: 130px;
    height: 50px;
  }
}


</style>