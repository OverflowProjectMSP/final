<script>
export default {
  data() {
    return {
      username: "",
      surename: "",
      interests: "",
      aboutme: "",
    }
  },
  methods: {
    limit() {
      
    } 
  }

}
</script>

<template>
<div class="window">
  <div class="comp">
    <h1>Настройки профиля</h1>
    <div class="links">
      <p>Страница</p>
      <p>Аккаунт</p>
    </div>
    <div class="main-info">
      <div class="avatar">
        <img src="" alt="">
        <div class="btns">
          <button>Удалить</button>
          <button>Заменить</button>
        </div>
        <p>Размер загружаемого изображения <br> не должен превышать 10 мб</p>
      </div>
      <div class="name">
        <div class="name-sure">
          <div class="username">
            <input v-model="username" type="text" maxlength="50">
            <span>Имя</span>
          </div>
          <div class="surename">
            <input v-model="surename" type="text" maxlength="50">
            <span>Фамилия</span>
          </div>
        </div>
        
        <div class="interests">
          <textarea v-model="interests" id="" name="" cols="30" rows="10" maxlength="2000"></textarea>
          <span>Интересы</span>
        </div>

      </div>
    </div>
 
    <div class="action">
      <h2>Действия с аккаунтом</h2>
      <div class="btns-act">
        <button>Привязать Telegram</button>
        <button>Выйти из аккаунта</button>
        <button>Забыли пароль?</button>
      </div>
    </div>
    <div class="aboutme">
      <div class="about-comp">
        <textarea v-model="aboutme" id="" name="" cols="30" rows="10" maxlength="2000"></textarea>
        <span>О себе</span>
      </div>

      <div class="about-links">
        <div class="email bl">
          <h3>Email</h3>
          <input type="email">
        </div>
        <div class="github bl">
          <h3>GitHub</h3>
          <input type="text">
        </div>
        <div class="telegram-link bl">
          <h3>Telegram</h3>
          <input type="text">
        </div>
        <div class="discord bl">
          <h3>Discord</h3>
          <input type="text">
        </div>
        <div class="phone-number bl">
          <h3>Номер телефона</h3>
          <input type="number">
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
.window {
  width: 100%;
  height: auto;

  display: flex;
  justify-content: center;
  align-items: start;
}

.comp {
  width: 90%;
  display: flex;
  flex-direction: column;
  align-items: start;
}

.comp h1 {
  width: 100%;
  border-bottom: 2px solid #000;
  padding-bottom: 30px;
}

.comp h2 {
  color: #000;
}

.links {
  width: 100%;
  display: flex;
  gap: 40px;
  padding: 10px 0 6px 30px;
  border-bottom: 2px solid #000;
}

.links p {
  font-size: 20px;
}

.main-info {
  width: 100%;
  display: flex;
  padding-top: 50px;
  gap: 15%;
  padding-bottom: 40px;
  border-bottom: 2px solid #000;
}

.avatar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.avatar img {
  width: 300px;
  height: 300px;
  border: 2px solid #000;
  border-radius: 8px;
}

.avatar p {
  text-align: center;
  font-size: 18px;
  font-weight: 500;
}

.btns {
  display: flex;
  gap: 10px;
}

.btns button {
  background-color: #3b82f6;
  border: none;
  border-radius: 8px;
  color: #fff;
  width: 130px;
  height: 35px;
}

.name {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
}

.name-sure {
  display: flex;
  gap: 50px;
}

.username input {
  width: 450px;
  height: 50px;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 20px;
  padding: 0 10px;

}

.username {
  position: relative;
}

.username span {
  position: absolute;
  left: 10px;
  top: -25px;
  background-color: #3b82f6;
  padding: 3px 25px;
  color: #fff;
  font-size: 20px;
  font-weight: 500;
  border-radius: 8px;
}

.surename input {
  width: 450px;
  height: 50px;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 20px;
  padding: 0 10px;
}

.surename {
  position: relative;
}

.surename span {
  position: absolute;
  left: 10px;
  top: -25px;
  background-color: #3b82f6;
  padding: 3px 25px;
  color: #fff;
  font-size: 20px;
  font-weight: 500;
  border-radius: 8px;
}

.interests textarea{
  width: 950px;
  height: 200px;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 20px;
  padding: 10px 10px 10px 10px;
  resize: none;
}

.interests {
  position: relative;
}

.interests span {
  position: absolute;
  left: 10px;
  top: -25px;
  background-color: #3b82f6;
  padding: 3px 25px;
  color: #fff;
  font-size: 20px;
  font-weight: 500;
  border-radius: 8px;
}

.action {
  display: flex;
  flex-direction: column;
  gap: 90px;
  width: 100%;
  padding-top: 50px;
  padding-bottom: 80px;

  border-bottom: 2px solid #000;
}

.action h2 {
  font-size: 40px;
}

.btns-act {
  display: flex;
  justify-content: space-between;
}

.btns-act button {
  background-color: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 14px;
  width: 400px;
  height: 60px;
  font-size: 26px;
}

.aboutme {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding-top: 100px;
  padding-bottom: 100px;
  position: relative;
}

.about-comp {
  padding-bottom: 80px;
}

.aboutme textarea {
  width: 100%;
  border: 2px solid #000;
  border-radius: 12px;
  padding: 20px 10px;
  font-size: 30px;
  font-weight: 500;
  resize: none;
}

.aboutme span {
  position: absolute;
  left: 40px;
  top: 60px;

  background-color: #3b82f6;
  color: #fff;
  font-size: 28px;
  padding: 5px 30px;
  border-radius: 12px;
}

button {
  transition: all 200ms;
}

button:hover {
  background-color: #3d72d3;
}

button:active {
  background-color: #325fb1;
}

.about-links {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.bl {
  display: flex;
  gap: 10%;
}

.bl h3 {
  display: grid;
  place-items: center;
  width: 400px;
  height: 60px;
  border: 2px solid #3b82f6;
  border-radius: 8px;
  font-weight: 550;
  margin: 0;
}

.bl input {
  width: 70%;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 24px;
  font-weight: 500;
  padding: 0 10px;
}

/* Убираем кнопки увеличения счетчика у input*/

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}


/* Адаптивка */

@media (max-width: 1550px) {
  .main-info {
    gap: 5%;
  }
}

@media (max-width: 1400px) {
  .name-sure {
    flex-direction: column;
  }

  .interests textarea {
    width: 450px;
  }
  
}

@media (max-width: 1350px) {
  .btns-act button {
    width: 330px;
  }

  .btns-act {
    gap: 10px;
  }
}

@media (max-width: 1120px) {
  .btns-act button {
    width: 290px;
  }
}

@media (max-width: 860px) {
  .btns-act {
    flex-direction: column;
  }

  .action h2 {
    font-size: 30px;
    font-weight: 500;
  }

  .btns-act button {
    width: 100%;
    gap: 20px;
  }

  .avatar img {
    width: 200px;
    height: 200px;
  }

  .btns button {
    width: 95px;
  }
}

@media (max-width: 730px) {
  .main-info {
    flex-direction: column;
  }

  .avatar img {
    width: 300px;
    height: 300px;
  }
}

@media (max-width: 630px) {
  .bl {
    flex-direction: column;
    align-items: center;
  }

  .bl h3 {
    width: 450px;
  }

  .bl input {
    width: 450px;
    height: 60px;
  }
}

@media (max-width: 450px) {
  .bl h3 {
    width: 330px;
  }

  .bl input {
    width: 330px;
  }

  .main-info {
    gap: 30px;
  }

  .username {
    display: flex;
    justify-content: center;
  }

  .username span {
    left: 20px;
  }

  .username input {
    width: 330px;
  }

  .surename {
    display: flex;
    justify-content: center;
  }

  .surename span {
    left: 20px;
  }

  .surename input {
    width: 330px;
  }

  .interests {
    display: flex;
    justify-content: center;
  }

  .interests span {
    left: 20px;
  }

  .interests textarea {
    width: 330px;
  }
}
</style>

