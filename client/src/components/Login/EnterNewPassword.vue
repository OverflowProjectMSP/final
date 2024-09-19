<script>
import axios from "axios";
import eye_img from "@/assets/Login/eye-open.svg";

export default {
  data() {
    return {
      exPassword: "",
      exPassword2: ``,

      error: "",
      eyeOpen1: true,
      eyeOpen2: true,
      eyeImg1: eye_img,
      eyeImg2: eye_img,
      isShowPassword: false,
      showPassword: "password",
      isShowExPassword: false,
      showExPassword: "password",
      button: true,
      gre: false,
      disabled: false,
    };
  },
  methods: {
    check() {
      if (this.exPassword != this.exPassword2) {
        this.error = "Пароли не совпадают.";
        this.button = false;
        this.gre = true;
      } else {
        this.error = null;
        this.button = true;
        this.gre = false;
        this.newPassword();
      }
    },
    toggleVisibility() {
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
    async newPassword() {
      try {
        let res = await axios.put("/new-password-email", {
          password: this.exPassword,
        });
        if (res.data.res == "Error") {
          this.error = "Ошибка отправки";
        } else if (res.data.res == "True") {
          this.$router.push("/Login");
        } else {
          this.error = "Неизвестная ошибка";
        }
      } catch (err) {
        this.error = "Ошибка сервера.";
        console.error(err);
      }
    },
    pushtoLogin() {
      this.$router.push("/login");
    },
    validateInput1($event) {
      this.button = false;
      this.gre = true;
      if ($event) {
        if (this.exPassword.length < 5) {
          console.log(this.error);
          this.error = "Не меньше 5-ти символов.";
          this.button = false;
          this.gre = true;
        } else if (this.exPassword.length >= 5) {
          this.error = null;
          this.button = true;
          this.gre = false;
        }
      }
    },
    input2($event) {
      this.button = false;
      this.gre = true;
      if ($event) {
        if (this.exPassword2.toString() == this.exPassword1.toString()) {
          this.error = null;
          this.button = true;
          this.gre = false;
        } else {
          this.error = "Пароли не  совпадают!";
          this.button = false;
          this.gre = false;
        }
      }
    },
  },
};
</script>
<template>
  <div class="all-container">
    <h6>UF 2.0</h6>
    <div class="login-container">
      <img class="mount" src="../../assets/Login/mounted.png" alt="" />
      <div class="cont-repass">
        <h3>Смена пароля</h3>
        <form @submit.prevent="check()">
          <div class="input-container">
            <div class="new-pass">
              <input
                :type="showPassword"
                v-model="exPassword"
                class="input"
                maxlength="35"
                @input="validateInput1($event)"
                autofocus
                required
              />
              <span class="pass">Новый пароль</span>
              <img
                :src="eyeImg1"
                alt=""
                class="eye"
                @click="toggleVisibility"
              />
            </div>
            <div class="c-pass">
              <input
                :type="showPassword"
                v-model="exPassword2"
                class="input"
                @input="validateInput2($event)"
                required
              />
              <span class="pass">Подтвердите пароль</span>
              <img
                :src="eyeImg1"
                alt=""
                class="eye"
                @click="toggleVisibility"
              />
            </div>
          </div>
          <div class="btn-container">
            <button class="bt reg" @click="pushtoLogin">Войти</button>
            <button
              :class="{ login: button, bt: true, grey: gre }"
              :disabled="gre"
              type="submit"
            >
              Подтвердить
            </button>
          </div>
        </form>
        <div class="erros">
          <p>{{ error }}</p>
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
.erros p {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 20px;
  color: red;
}
.bt {
  border-radius: 15px;
  border: none;
  cursor: pointer;
  width: 240px;
  height: 70px;
  padding: 15px;
  z-index: 7000;
}
.reg {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #5b5a5a;
  background: #efefef;
  cursor: pointer;
  transition: background-color 0.3s ease; 
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
  transition: background-color 0.3s ease; 
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
  transition: background-color 0.3s ease; 
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

.all-container {
  display: flex;
  background-color: #ecedee;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  position: relative;
}

.login-container {
  display: flex;
  gap: 40px;
  border-radius: 50px;
  margin: 80px 80px 80px 80px;
  width: 1100px;
  height: 620px;
  background: #fff;
  position: relative;
}

.cont-repass {
  width: 100%;
  margin-right: 40px;
  height: 620px;

  /* ОТЛАДЧИК */
  /* border: 3px solid #3b82f6; */
  /* ОТЛАДЧИК */

  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 60px;
}

.cont-repass h3 {
  width: 100%;
  font-size: 50px;
  text-align: start;

  /* ОТЛАДЧИК */
  /* outline: 1px solid #3b82f6; */
  /* ОТЛАДЧИК */
}

.input-container {
  display: flex;
  flex-direction: column;
  width: 100%;

  /* ОТЛАДЧИК */
  /* border: 1px solid #3b82f6; */
  /* ОТЛАДЧИК */

  z-index: 300;
}

.new-pass {
  position: relative;
  width: 100%;
}

.c-pass {
  position: relative;
  width: 100%;
}

.pass {
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
  width: 415px;
}

.input {
  margin-bottom: 30px;
  border-radius: 15px;
  width: 100%;
  height: 60px;
  background: #eae9e9;
  border: none;
  padding: 15px;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}

.input:focus {
  outline: none;
  border: none;
  border: 4px solid #3b82f6;
  transition: all 0.1s;
}

.input:focus ~ span,
.input:valid ~ span {
  transform: translateY(-110%);
  font-size: 20px;
  left: 25px;
  border: solid #3b82f6;
  background: #3b82f6;
  color: #fff;
  width: 240px;
  text-align: center;
  border-radius: 15px;
}

.eye {
  position: absolute;
  width: 40px;
  height: 40px;
  z-index: 400;
  cursor: pointer;
  top: 10px;
  right: 10px;
}

.btn-container {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

.butt {
  border: none;
  border-radius: 15px;
  width: 240px;
  height: 70px;

  font-size: 25px;
  font-weight: bold;
}
.reg:hover {
  background: #e4e3e3;
  /* transition: all 0.3s; */
}
.grey:hover {
  background: #d7d5d5;
  /* transition: all 0.3s; */
}

/* .btn-enter, .reg, .grey:active {
  background-color: #aeaeae;
} */

.btn-confirm {
  background-color: #3b82f6;
  color: #ffffff;
}

.login:hover {
  background: #2d6fda;
  /* transition: all 0.3s; */
}
.login:active {
  background-color: #164691;
}

.mail {
  position: absolute;
  bottom: 20px;
  right: 20px;
}

/* АДАПТИВКА */

@media (max-width: 1140px) {
  .mount {
    display: none;
  }

  .login-container {
    width: 700px;
    padding-left: 30px;
  }

  .cont-repass h3 {
    font-size: 70px;
    text-align: center;
  }

  .input {
    height: 80px;
  }

  .pass {
    margin-top: 8px;
    font-size: 30px;
  }

  .eye {
    top: 20px;
  }

  .butt {
    font-size: 30px;
  }
}

@media (max-width: 635px) {
  .reg {
    font-size: 20px;
    vertical-align: center;
  }

  .login {
    font-size: 20px;
    vertical-align: center;
  }
  .grey {
    font-size: 20px;
    vertical-align: center;
  }
  .bt {
    border-radius: 15px;
    border: none;
    cursor: pointer;
    width: 200px;
    height: 70px;
    padding: 20px;
  }
  .butt {
    width: 100%;
  }

  .all-container {
    background-color: #fff;
  }

  .login-container {
    margin: 0;
    padding-left: 10px;
    border-radius: 0;
  }

  .mail {
    right: 20px;
  }

  .cont-repass {
    margin: 0;
    padding-right: 10px;
  }

  .cont-repass h3 {
    font-size: 50px;
  }

  .pass {
    font-size: 22px;
  }

  .butt {
    font-size: 22px;
  }
}
</style>
