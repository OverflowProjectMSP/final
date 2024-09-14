<script>
import axios from "axios";
import eye_img from "@/assets/Login/eye-open.svg";

export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
      },

      error: "",
      eyeOpen1: true,
      eyeOpen2: true,
      eyeImg1: eye_img,
      eyeImg2: eye_img,
      isShowPassword: false,
      showPassword: "password",
      isShowExPassword: false,
      showExPassword: "password",
      a: "",
      button: true,
      gre: false,
      disabled: false,
    };
  },
  methods: {
    // check() {
    //   if (this.email === "") {
    //     this.error = "*Вы не ввели Email*";
    //   } else if (this.password === "") {
    //     this.error = "*Вы не ввели пароль*";
    //   } else {
    //     this.error = "";
    //     this.login();
    //   }

    //   // if (this.password !== this.exPassword) {
    //   //     this.error = '*Пароли не совпадают'
    //   // }
    // },
    toggleVisibility1() {
      this.isShowPassword = !this.isShowPassword;
      this.eyeOpen1 = !this.eyeOpen1;

      if (this.isShowPassword) {
        this.showPassword = "text";
        this.eyeImg1 = "/src/assets/Login/eye-close.svg";
      } else {
        this.showPassword = "password";
        this.eyeImg1 = eye_img;
      }
    },

    async login() {
      try {
        let res = await axios.post("/login", {
          email: this.form.email,
          password: this.form.password,
        });
        if (res.data.message == "ok") {
          this.$router.push("/");
        } else if (res.data.message == "wrong!") {
          this.error = "Пароль и почта не совпадают!";
        } else {
          this.error = "Неизвестная ошибка.";
        }   
      } catch (err) {
        this.error = "Ошибка сервера."
        console.error(err)
      }
    },

    passwordValidation($event) {
      this.button = false;
      this.gre = true;
      if ($event) {
        if (this.form.password.length == 0) {
          this.error = "Поле не должно быть пустым!";
          this.button = false;
          this.gre = true;
        } else {
          this.error = null;
          this.button = true;
          this.gre = false;
        }
      }
    },
    reg(){
      window.location.href = '/SignUp';
      console.log(0)
    }
  },
};
</script>

<template>
  <div class="all-container">
    <h6>UF 2.0</h6>
    <div class="login-container container">
      <div class="img-container">
        <img src="../../assets/Login/mounted.png" alt="" class="img" />
      </div>
      <div class="head">
        <h1>Войти</h1>
      </div>
      <form @submit.prevent="login()">
        <div class="input-container">
          <div class="div-nickname">
            <input
              type="text"
              v-model="form.email"
              class="input"
              autofocus
              required
            />
            <span сlass="nick">Почта</span>
          </div>
          <div class="password">
            <input
              :type="showPassword"
              v-model="form.password"
              class="input"
              required
              @input="passwordValidation($event)"
            />
            <span>Пароль</span>
            <img :src="eyeImg1" alt="" class="eye" @click="toggleVisibility1" />
          </div>
        </div>
        <div class="btn-container">
          <button class="bt reg" @click="reg" type="button">Регистрация</button>
          <button
            :class="{ 'login': button, 'bt': true, 'grey': gre }"
            :disabled="gre"
            type="submit"
          >
            Войти
          </button>
        </div>
      </form>
      <div class="mail">
        <!-- <a href=""><img src="/mail.svg" alt="" /></a> -->
      </div>
      <div class="pass-err">
        <a href="/EnterCodePage" class="a">Забыли пароль?</a> 
        <div class="errors">
          <p class="err">{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
:root {
  --font-family: "Rubik", sans-serif;
  --second-family: "Inter", sans-serif;
}
.login {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #fff;
  background: #3b82f6;
  text-align: center;
  cursor: pointer;
  cursor: pointer;
    border-radius: 15px;
  width: 200px;
  height: 60px;

  border: none;
  cursor: pointer;
  z-index: 7000;
}
.grey {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #5b5a5a;
  background: #eae9e9;
  text-align: center;
  cursor: pointer;
  cursor: pointer;
    border-radius: 15px;
  width: 200px;
  height: 60px;

  border: none;
  cursor: pointer;
  z-index: 7000;
}
.err {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 20px;
  color: #f00;
  position: absolute;
  top: 550px;
  left: 530px;
}
.a {
  position: absolute;
  top: 500px;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 20px;
  color: #3b82f6;
  text-decoration: none;
  z-index: 8000;
  left: 530px;
}
.mail {
  position: relative;
}
h6 {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #3b82f6;
  position: absolute;
  top: 10px;
  left: 10px;
  display: block;
}
.img-container {
  display: block;
}
.mail img {
  position: absolute;
  top: 550px;
  cursor: pointer;
  right: -130px;
}
.all-container {
  display: flex;
  background-color: #ecedee;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100%;
  position: relative;
}
.login-container {
  display: flex;
  border-radius: 50px;
  margin: 80px;
  width: 1100px;
  height: 620px;
  background: #fff;
  position: relative;
}
.img {
  height: 620px;
  transform: translateX(-50px);
  transition: all 0.3s;
}

.password {
  /* display: flex; */
  /* align-items: center; */
  position: relative;
  width: 30px;
}
.password span {
  position: absolute;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #5b5a5a;
  top: 14px;
  left: 18px;
  pointer-events: none;
  transition: 0.3s ease;
  border-radius: 15px;
}
h1 {
  font-weight: 700;
  font-size: 80px;
  color: #000;
  width: 100%;
  margin: 80px 0px 0px 40px;
}
.input-container {
  display: flex; /* Добавляем flexbox */
  flex-direction: column; /* Устанавливаем вертикальное направление */
  margin: 230px 0px 0px -250px; /* Меняем отступ */
  width: 400px; /* Добавляем ширину для блока инпутов */
  z-index: 300;
}

.input {
  margin-bottom: 40px;
  border-radius: 15px;
  width: 430px;
  height: 60px;
  background: #eae9e9;
  border: none;
  padding: 20px;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}
.btn-container {
  display: flex;
  justify-content: center; /* Выравниваем кнопки по центру */
  margin-top: -10px; /*  Вертикальный отступ */
  gap: 30px;
  margin-left: -250px;
}

.reg {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #5b5a5a;
  background: #eae9e9;
  cursor: pointer;
    border-radius: 15px;
  width: 200px;
  height: 60px;

  border: none;
  cursor: pointer;
  z-index: 7000;
}

.eye {
  position: absolute;
  width: 50px;
  height: 50px;
  z-index: 400;
  cursor: pointer;
  top: 7px;
  right: -380px;
}
.div-nickname {
  position: relative;
  width: 300px;
}
.div-nickname span {
  position: absolute;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #5b5a5a;
  top: 14px;
  left: 18px;
  pointer-events: none;
  transition: 0.3s ease;
  border-radius: 15px;
  width: 115px;
}
.reg:hover {
  color: #5b5a5a;
  background: #d7d5d5;
  transition: all 0.3s;
}
.input:focus {
  outline: none;
  border: none;
  border: 4px solid #3b82f6;
  transition: all 0.1s;
}
.login:hover {
  color: #fff;
  background: #2e77ed;
}
.input:focus ~ span,
.input:valid ~ span {
  transform: translateY(-115%);
  font-size: 20px;
  left: 25px;
  border: solid #3b82f6;
  background: #3b82f6;
  color: #fff;
  width: 110px;
  text-align: center;
  border-radius: 15px;
}
@media (max-width: 1260px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -110px;
  }
}
@media (max-width: 1235px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -70px;
  }
}

/* 
@media (max-width: 1199px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 20px;
  }
  .login-container {
    display: flex;
    border-radius: 50px;
    margin: 80px;
    width: 1550px;
    height: 600px;
    background: #fff;
    position: relative;
  }
} */

@media (max-width: 1175px) {
  .img-container {
    display: none;
  }
  .a {
    position: absolute;
    left: 50px;
  }
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -30px;
  }
  .login-container {
    display: flex;
    border-radius: 50px;
    margin: 80px;
    width: 550px;
    height: 600px;
    background: #fff;
    position: relative;
  }
  .err {
    width: 1000px;
    position: absolute;
    top: 550px;
    margin-left: -479px;
  }
}
@media (max-width: 705px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -40px;
  }
}
@media (max-width: 685px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 50px;
  }
  .a {
    position: absolute;
    left: 220px;
  }
  .input {
    margin-bottom: 40px;
    border-radius: 15px;
    width: 330px;
    height: 60px;
    background: #eae9e9;
    border: none;
    padding: 20px;
    font-family: var(--font-family);
    font-weight: 500;
    font-size: 20px;
    color: #000000;
  }
  .bt {
    border-radius: 15px;
    width: 150px;
    height: 60px;
    border: none;
    cursor: pointer;
    z-index: 7000;
  }
  .login-container {
    display: flex;
    border-radius: 50px;
    margin: 80px;
    width: 430px;
    height: 600px;
    background: #fff;
    position: relative;
  }
  .eye {
    position: absolute;
    width: 50px;
    height: 50px;
    z-index: 100;
    cursor: pointer;
    top: 7px;
    right: -280px;
  }
  .reg {
    font-family: var(--font-family);
    margin-left: -70px;
    font-weight: 700;
    font-size: 20px;
    text-align: center;
    color: #5b5a5a;
    background: #eae9e9;
    cursor: pointer;
  }
  .login {
    font-family: var(--font-family);
    font-weight: 700;
    font-size: 20px;
    text-align: center;
    color: #fff;
    background: #3b82f6;
    text-align: center;
    cursor: pointer;
  }
  .img {
  transform: translateX(-20px);
  transition: all 0.3s;
}
.input {
  margin-bottom: 30px;
}
}

/* @media (max-width: 567px) {
  .input {
    margin-bottom: 40px;
    border-radius: 15px;
    width: 300px;
    height: 60px;
    background: #eae9e9;
    border: none;
    padding: 20px;
    font-family: var(--font-family);
    font-weight: 500;
    font-size: 17px;
    color: #000000;
  }
  .eye {
    position: absolute;
    width: 50px;
    height: 50px;
    z-index: 100;
    cursor: pointer;
    top: 7px;
    right: -250px;
  }
  .bt {
    border-radius: 15px;
    width: 135px;
    height: 60px;
    border: none;
    cursor: pointer;
    z-index: 7000;
  }
  .login {
    font-family: var(--font-family);
    font-weight: 700;
    font-size: 20px;
    margin-right: 30px;
  }
  .mail img {
    right: 20px;
  }
  h6 {
    display: none;
  }
  .reg {
    font-family: var(--font-family);
    font-weight: 700;
    font-size: 18px;
  }
} */
@media (max-width: 505px) {
  .reg{
    background-color: white;
  }
.input{
  background: #ffffff;

}  
  .all-container {
    background: #fff;
  }
  .login-container {
  background: #f4f4f4;
}
  /* .login-container {
    -webkit-box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);
    box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);

    margin-left: 50px;
  } */
}
</style>
