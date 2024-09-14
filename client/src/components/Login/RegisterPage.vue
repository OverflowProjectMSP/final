<script>
import axios from "axios";
import eye_img from "@/assets/Login/eye-open.svg";

export default {
  data() {
    return {
      form: {
        nickname: "",
        email: "",
        password: "",
        exPassword: "",
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
      button: true,
      gre: false,
      disabled: false,
    };
  },
  methods: {
    check() {
      if (this.form.username === "") {
        this.error = "Вы не ввели Никнейм!";
      } else if (this.form.email === "") {
        this.error = "Вы не ввели Email!";
      } else if (this.form.password === "") {
        this.error = "Вы не ввели Пароль!";
      } else if (this.form.exPassword === "") {
        this.error = "Вы не Повторили Пароль!";
      } else if (this.form.password != this.form.exPassword) {
        this.error = "Повторно введенный пароль неверный!";
      } else if (this.password< 5) {
        this.error = "* Пароль должен включать 5 символов *";
      } else {
        this.error = "";
        this.register()
      }
    },
    async register() {
        try{
      const res =  await axios.post("/registration", {
          name: this.form.nickname,
          email: this.form.email,
          password: this.form.password,
        });
          if (res.data.res == 'Пользователь с таким именем или почтой уже существует!') {
          this.error = 'Пользователь с таким именем или почтой уже существует!'
          } else if("Ok"){
            this.$router.push("/Login");
        }
      } catch(err) {
          console.error(err)
          this.error = "Ошибка сервера"
      }
      },
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

    toggleVisibility2() {
      this.isShowExPassword = !this.isShowExPassword;
      this.eyeOpen2 = !this.eyeOpen2;

      if (this.isShowExPassword) {
        this.showExPassword = "text";
        this.eyeImg2 = "/src/assets/Login/eye-close.svg";
      } else {
        this.showExPassword = "password";
        this.eyeImg2 = eye_img;
      }
    },

    //   async login() {
    //     try {
    //       let res = await axios.post("/login", {
    //         email: this.form.email,
    //         password: this.form.password,
    //       });
    //       if (res.data.message == "ok") {
    //         this.$router.push("/");
    //       } else if (res.data.message == "wrong!") {
    //         this.error = "Пароль и почта не совпадают!";
    //       } else {
    //         this.error = "Неизвестная ошибка.";
    //       }
    //     } catch (err) {
    //       this.error = "Ошибка сервера."
    //       console.error(err)
    //     }
    //   },

    passwordValidation($event) {
      this.button = false;
      this.gre = true;
      if ($event) {
        if (!this.form.email.includes("@") && !this.form.email.includes(".")) {
          this.error = "Некорректный Email!";
          this.button = false;
          this.gre = true;
        } else if (this.form.password.length < 5) {
          this.error = "Пароль должен включать минимум 5 символов!";
          this.button = false;
          this.gre = true;
        } else if (this.form.password !== this.form.exPassword) {
          this.error = "Пароли не совпадают!";
          this.button = false;
          this.gre = true;
          this.error = null;
          this.button = true;
          this.gre = false;
        }
      }
    },
    login() {
      this.$router.push("/Login")
    }
  },
};
</script>

<template>
  <div class="window">
    <div class="main-cont">
      <div class="image">
        <img src="../../assets/Login/mounted.png" alt="" class="img" />
      </div>
      <div class="main-content">
        <div class="main-ccc">
          <h1>Регистрация</h1>
          <div class="inputs-cont">
            <div class="div-username">
              <input
                type="text"
                v-model="form.nickname"
                class="input"
                autofocus
                required
              />
              <span сlass="nick">Никнейм</span>
            </div>

            <div class="div-nickname">
              <input
                type="text"
                class="input"
                v-model="form.email"
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
              <img
                :src="eyeImg1"
                alt=""
                class="eye"
                @click="toggleVisibility1"
              />
            </div>

            <div class="rep-password">
              <input
                :type="showExPassword"
                v-model="form.exPassword"
                class="input"
                required
              />
              <span>Повторите пароль</span>
              <img
                :src="eyeImg2"
                alt=""
                class="eye"
                @click="toggleVisibility2"
              />
            </div>
          </div>
          <div class="btn-container">
            <button class="bt reg" @click="login">Войти</button>
            <button
              type="submit"
              :class="{ login: button, grey: gre }"
              @click="check"
              :disabled="gre"
            >
              Зарегистрироваться
            </button>
          </div>
          <div class="errors">
            <p class="err">{{ error }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.err {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 17px;
  color: #f00;
}
.window {
  display: flex;
  justify-content: center;
  align-items: center;

  background-color: #ecedee;

  width: 100%;
  height: 100vh;
}

h1 {
  text-align: center;
  font-weight: 700;
  font-size: 79px;
  color: #000;
  width: 100%;
}

.main-cont {
  display: flex;

  width: 1200px;
  height: 670px;
  background-color: #fff;
  border-radius: 50px;
}

.main-ccc {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.img {
  height: 670px;
}

.main-content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.inputs-cont {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.input {
  border-radius: 15px;
  width: 480px;
  height: 60px;
  background: #eae9e9;
  border: none;
  padding: 20px;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}

.div-nickname {
  position: relative;
  /* width: 300px; */
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

.div-username {
  position: relative;
  /* width: 300px; */
}

.div-username span {
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

input:focus {
  outline: none;
  border: none;
  border: 4px solid #3b82f6;
  transition: all 0.1s;
}

.password {
  position: relative;
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

.eye {
  position: absolute;
  width: 45px;
  height: 45px;
  z-index: 400;
  cursor: pointer;
  top: 7px;
  right: 60px;
}

.rep-password {
  position: relative;
}

.rep-password span {
  position: absolute;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  color: #5b5a5a;
  top: 14px;
  left: 18px;
  width: 240px !important;
  pointer-events: none;
  transition: 0.3s ease;
  border-radius: 15px;
}

.login {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 22px;
  color: #fff;
  background: #3b82f6;
  cursor: pointer;
  border-radius: 15px;
  width: 250px;
  height: 60px;
  border: none;
  z-index: 7000;
}
.login:disabled {
  color: #5b5a5a;
  background: #eae9e9;
  border-radius: 15px;
  width: 250px;
  height: 60px;
  border: none;
  z-index: 7000;
  font-family: var(--font-family);
  font-weight: 700;
}
.grey {
  color: #5b5a5a;
  background: #eae9e9;
  border-radius: 15px;
  width: 250px;
  height: 60px;
  border: none;
  z-index: 7000;
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 22px;
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

.btn-container {
  width: 480px;
  display: flex;
  justify-content: center;
  margin-top: 10px;
  /* gap: 30px; */
  justify-content: space-between;
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

.err {
  color: #f00;
  font-size: 17px;
}

@media (max-width: 1230px) {
  .login {
    font-size: 18px;
  }
  .image {
    display: none;
  }

  .a {
    position: absolute;
    left: 50px;
  }

  .inputs-cont {
    align-items: center;
  }

  .input {
    width: 430px;
  }

  .eye {
    right: 10px;
  }

  .btn-container {
    width: 430px;
  }

  .login {
    width: 210px;
  }
  .grey {
    font-size: 18px;

    width: 210px;
  }
  .main-cont {
    display: flex;
    border-radius: 50px;
    margin: 80px;
    width: 550px;
    height: 600px;
    background: #fff;
    position: relative;
  }

  h1 {
    margin-top: 30px;
    margin-bottom: 10px;
    font-size: 42px;
  }
}
@media (max-width: 670px) {
  .window {
    background: #fff;
  }
}

@media (max-width: 600px) {
  h1 {
    font-size: 34px;
  }

  .input {
    width: 340px;
    height: 55px;
  }

  input {
    font-size: 22px !important;
  }

  span {
    font-size: 18px !important;
  }

  .btn-container {
    width: 340px;
    gap: 20px;
  }
  .grey {
    font-size: 13px;
    height: 50px;
    width: 150px;
  }
  .reg {
    font-size: 22px;
    height: 50px;
    width: 150px;
  }

  .login {
    font-size: 16px;
    height: 50px;
  }
  .window {
    background: #fff;
  }
}

@media (max-width: 505px) {
  .window {
    background: #fff;
  }
}
</style>
