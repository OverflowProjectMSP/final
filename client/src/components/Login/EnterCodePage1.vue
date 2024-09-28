<script>
import axios from 'axios';
import eye_img from "@/assets/Login/eye-open.svg"

export default {
  data() {
    return {
      CIFRY: "",

      error: '',
      eyeOpen1: true,
      eyeOpen2: true,
      eyeImg1: eye_img,
      eyeImg2: eye_img,
      isShowPassword: false,
      showPassword: 'password',
      isShowExPassword: false,
      showExPassword: 'password', 
      src: 'src/assets/Login/23.png',
      inputNumber: '',
      button: true,
      gre: false,
      disabled: false,

    }
  },
  methods: {
    check() {
      this.checkCode();
    },
    async checkCode() {
      try {
        let res = await axios.post('/reg-code-send', {
          emailCode: this.CIFRY,
        });
        if(res.data.res == 'Error') {
          this.error = 'Ошибка отправки.';
        } else if(res.data.res == 'True') {
          this.$router.push('/Login');
        } else if(res.data.res == 'Некорректный код') {
            this.error = 'Неверный код.';
        } else {
          this.error = 'Ошибка';
        }
      } catch (err) {
        this.error = "Ошибка сервера"
        console.error(err)
      }
    },
    validateInput($event) {
      this.button = false
      this.gre = true
      if ($event) {

        if (this.CIFRY.length > 4) {
          this.error = "Не больше 4-х символов."
          this.button = false
          this.gre = true
          this.src = 'src/assets/Login/arrow_forward.png'
        } else if (this.CIFRY.length == 4) {
          this.error = null;
          this.button = true
          this.gre = false
          this.src = 'src/assets/Login/23.png'
        } else if (this.CIFRY.length <= 4) {
          this.error = null;
          this.button = false
          this.gre = true
          this.src = 'src/assets/Login/arrow_forward.png'
        }
      }
    },
    pushtoFAQ() {
      this.$router.push("/FAQ")
    },
  }
}

</script>


<template>
  <div class="all-container">
    <h6>UF 2.0</h6>
    <div class="login-container container">
      <div class="img-container">
        <img src="../../assets/Login/mounted.png" alt="" class="img" />
      </div>
      <div class="head mt-4">
        <h1>Код подтверждения</h1>
        <p>На вашу почту был направлен код подтверждения</p>
      </div>
      <form @submit.prevent="checkCode">
      <div class="input-container">
        <div class="div-nickname">
          <input type="text" v-model="CIFRY" class="input" autofocus required @input="validateInput($event)"/>
          <span сlass="nick">Код</span>
        </div>
        <div class="btn-container">
          <button :class="{'login': button, 'bt': true, 'grey': gre} " :disabled="gre" type="submit" ><img :src="src" alt="" class="str"></button>
        </div>
      </div>
    </form>
      <div class="mail" @click="pushtoFAQ">
        <img src="/mail.svg" alt="" />
      </div>
      <div class="pass-err">
        <a href="" class="a mt-3">Не приходит код?</a>
        <div class="errors" v-if="error"><p class="err">{{error}}</p></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
:root {
  --font-family: 'Rubik', sans-serif;
  --second-family: 'Inter', sans-serif;
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
  top: 350px;
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
  z-index: 6;
}
.img-container {
  display: block;
}
.mail img {
  position: absolute;
  top: 550px;
  cursor: pointer;
  right: 10px;
}
.all-container {
  display: flex;
  background-color: #fff;
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
  margin-top: -80px;
  width: 1100px;
  height: 620px;
  background: #fff;
  position: relative;
  -webkit-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
}
.img {
  height: 620px;
  transform: translateX(-50px);
  transition: all 0.3s;
}
.head {
  height: 50px;
}
.head h1 {
    font-size: 40px;
    margin-bottom: 20px;
}
.head p {
    font-size: 30px;
    font-weight: bold;
    color: #5B5A5A;
    margin-left: 40px;
    margin-bottom: 20px;
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
  margin: 290px 0px 0px;/* Меняем отступ */
  position: absolute;
  left: 525px;
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
  position: absolute;
  top: 0;
  left: 450px;
  display: flex;
  justify-content: center; /* Выравниваем кнопки по центру */
  /* margin-top: -10px;  */
  gap: 30px;
  /* margin-left: -250px; */
}

.bt {
  border-radius: 15px;
  width: 60px;
  height: 60px;
  background: blue;
  border: none;
  cursor: pointer;
  z-index: 7000;
}
.reg {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #5b5a5a;
  background: #eae9e9;
  cursor: pointer;
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
}
.grey {
  font-family: var(--font-family);
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  color: #fff;
  background: #EAE9E9;
  text-align: center;
  cursor: pointer;
}
.str {
  width: 30px;
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
  /* .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -110px;
  } */

  .btn-container {
    position: absolute;
    top: 80px;
    left: 0;
  }

  .a {
    top: 420px;
  }

  
}
@media (max-width: 1235px) {
  /* .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: -70px;
  } */
}

@media (max-width: 1199px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 30px;
  }

  .input {
    width: 360px;
  }

}

@media (max-width: 1175px) {
  .img-container {
    display: none;
  }

  .head h1 {
    font-size: 30px;
  }

  .head p {
    font-size: 30px;
  }

  .a {
    position: absolute;
    top: 370px;
    left: 50px;
  }
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 10px;
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
    margin-left: -479px
  }
  
  .input-container {
    top: 0px;
    left: 50px;
  }

  .btn-container {
    top: 0;
    left: 400px;
  }
}
@media (max-width: 705px) {
  /* .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 20px;
  } */
}
@media (max-width: 685px) {
  .mail img {
    position: absolute;
    top: 550px;
    cursor: pointer;
    right: 50px;
  }
  
  .head h1 {
    font-size: 25px;
  }

  .head p {
    font-size: 25px;
  }

  .a {
    position: absolute;
    left: 55px;
    top: 430px
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

  .input-container {
    top: 0px;
    
  }

  .input {
    width: 300px;
  }


  .btn-container {
    top: 80px;
    left: 0;
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

  .bt {
    border-radius: 15px;
    width: 300px;
    height: 60px;
    border: none;
    cursor: pointer;
    z-index: 7000;
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
}

@media (max-width: 567px) {
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

  .a {
    font-size: 18px;
  }
}
@media (max-width: 505px) {
  .all-container {
    background: #fff;
  }

  .login-container {
    margin: 0;
  }
  /* .login-container {
    -webkit-box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);
    box-shadow: 4px 4px 100px 0px rgba(34, 60, 80, 0.2);

    margin-left: 50px;
  } */
}
</style>
