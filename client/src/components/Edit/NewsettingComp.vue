<script>
export default {
  data() {

  },
  methods: {
    
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
            <input type="text">
            <span>Имя</span>
          </div>
          <div class="surename">
            <input type="text">
            <span>Фамилия</span>
          </div>
        </div>
        
        <div class="interests">
          <textarea id="" name="" cols="30" rows="10"></textarea>
          <span>Интересы</span>
        </div>

      </div>
    </div>
  </div>
</div>
</template>

<style>
.window {
  width: 100%;
  height: 100vh;

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
  gap: 260px;
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
  height: 50px;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 20px;
  padding: 10px 10px 10px 10px;
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

</style>
