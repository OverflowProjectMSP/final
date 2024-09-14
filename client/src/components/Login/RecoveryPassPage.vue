<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      error: "",
    };
  },
  methods: {
    check() {
      if (this.email === "") {
        this.error = "Вы не ввели Email!";
      } else {
        this.error = "";
        this.checkPassword();
      }
    },

    async checkPassword() {
      try {
        let res = await axios.post("/new-password-email", {
          email: this.email,
        });
        if (res.data.res == "Error") {
          this.error = "Ошибка email!";
        } else {
          this.error = "";
          this.$router.push("/EnterCodePage");
        }   
      } catch (err) {
        this.error = "Ошибка email!"
        console.error(err)
      }
    },
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
          <h1>Восстановить пароль</h1>
          <div class="inputs-cont">
            <div class="div-username">
              <input
                type="text"
                v-model="email"
                class="input"
                autofocus
                required
              />
              <span сlass="nick">Почта</span>
            </div>
          </div>
          <div class="btn-container">
            <button class="bt reg">Войти</button>
            <button type="submit" class="login" @click="check" :disabled="gre">
              Сбросить
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
  font-size: 43px;
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
  transition: background-color 0.3s ease; 
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
  transition: background-color 0.3s ease; 
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
.grey:hover {
  background: #d7d5d5;
  /* transition: all 0.3s; */
}
.login:hover {
  background: #3883fb;
  /* transition: all 0.3s; */
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
    font-size: 35px;
  }
}
@media (max-width: 670px) {
  .window {
    background: #fff;
  }
}

@media (max-width: 600px) {
  h1 {
    font-size: 28px;
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
