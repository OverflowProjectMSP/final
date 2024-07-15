<script setup>
import axios from "axios";
import { ref, onMounted, watch } from "vue";
import { useRoute } from 'vue-router'; 

const link = ref("");
const res = ref("");
const name = ref("")

const load = ref(true);
const ok = ref(false);
const notvalid = ref(false);
const notacc = ref(false);
const time = ref(false)
const error = ref(false)

const route = useRoute(); 

const authTg = async () => {
  link.value = route.params.id;

  try {
    const response = await axios.post('/auth-tg', { hash_id: link.value });
    res.value = response.data.res;
    name.value = response.data.name
    console.log(res.value);
  } catch (error) {
    console.error("Ошибка при авторизации:", error);
    res.value = "Error";
  }
};
const gotoProfile = () => {
  route.push("/ProfileSettings")
}
watch(res, (newRes) => {
  switch (newRes){
    case 'all ok':
      ok.value = true;
      load.value = false;

    case 'Невалидная ссылка':
      notvalid.value = true;
      load.value = false;
        
    case 'Пользователь не в аккаунте':
      notacc.value = true;
      load.value = false;   
    case 'Время жизни ссылки истекло':
      time.value = true;
      load.value = false;   
    case 'err':
      error.value = true;
      load.value = false;   
    }
});

onMounted(() => {
  authTg();
});
</script>




<template>
  <div class="window">
      <div class="main-container">
          <img class="mount" src="../../assets/Telegram/mounted.png" alt="">
          <div class="close" @click="gotoProfile">
              <img src="../../assets/Telegram/close-icon.svg" alt="">
          </div>
        <div class="link-cont" v-if="load">
          <img src="../../assets/Telegram/telegram-icon.svg" alt="">
          <h2>Привязка Telegram</h2>
          <div class="link-good">
            <p class="text-def">Телеграм привязывается, пожалуйста подаждите...</p>
          </div>
<!--          <div class="btns">-->
<!--            <a href="#!"><button class="bt more"><p class="text-def">Подробнее о привязки</p></button></a>-->
<!--            <a href="#!"><button class="bt next"><p class="text-def">Далее</p></button></a>-->
<!--          </div>-->
        </div>
          <div class="link-cont" v-else-if="ok">
              <img src="../../assets/Telegram/telegram-icon.svg" alt="">
              <h2>Привязка Telegram</h2>
              <div class="link-good">
                  <p class="text-def">Телеграм {{ name }} привязан к вашему аккаунту.</p>
              </div>
              <div class="btns">
                  <a href="#!"><button class="bt more"><p class="text-def">Подробнее о привязки</p></button></a>
                  <a href="#!"><button class="bt next"><p class="text-def">Далее</p></button></a>
              </div>
          </div>
          <div class="link-cont" v-else-if="notvalid">
              <img src="../../assets/Telegram/telegram-icon.svg" alt="">
              <h2>Привязка Telegram</h2>
              <div class="link-good">
                  <p class="text-def">Ссылка недействительна!</p>
              </div>
              <div class="btns" v-if="false">
                  <a href="#!"><button class="bt more"><p class="text-def">Подробнее о привязки</p></button></a>
                  <a href="#!"><button class="bt next"><p class="text-def">Далее</p></button></a>
              </div>
          </div>

          <div class="link-cont" v-else-if="notacc">
              <img src="../../assets/Telegram/telegram-icon.svg" alt="">
              <h2>Привязка Telegram</h2>
              <div class="link-good">
                  <p class="text-def">Войдите в аккаунт!</p>
              </div>
              <div class="btns" v-if="true">
                  <a href="#!"><button class="bt next"><p class="text-def">Войти</p></button></a>
              </div>
          </div>

          <div class="link-cont" v-else-if="time">
              <img src="../../assets/Telegram/telegram-icon.svg" alt="">
              <h2>Привязка Telegram</h2>
              <div class="link-good">
                  <p class="text-def">Время жизни ссылки истекло!</p>
              </div>
              <div class="btns" v-if="false">
                  <a href="#!"><button class="bt more"><p class="text-def">Подробнее о привязки</p></button></a>
                  <a href="#!"><button class="bt next"><p class="text-def">Войти</p></button></a>
              </div>
            <div class="link-cont" v-else-if="error">
              <img src="../../assets/Telegram/telegram-icon.svg" alt="">
              <h2>Привязка Telegram</h2>
              <div class="link-good">
                  <p class="text-def">Ошибка сервера!</p>
              </div>
              <div class="btns" v-if="false">
                  <a href="#!"><button class="bt more"><p class="text-def">Подробнее о привязки</p></button></a>
                  <a href="#!"><button class="bt next"><p class="text-def">Войти</p></button></a>
              </div>
            </div>

          <div class="link">
              <img src="../../public/link-icon.svg" alt="">
          </div>
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
text-align: center;
  font-size: 27px;
  font-weight: bold;
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
      top: 30px;
      right: 30px;
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
      //height: 80px;
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