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

      inputNumber: '',
    }
  },
  methods: {
    check() {
      this.checkCode();
    },
    toggleVisibility1() {
      this.isShowPassword = !this.isShowPassword;
      this.eyeOpen1 = !this.eyeOpen1

      if (this.isShowPassword) {
        this.showPassword = 'text'
        this.eyeImg1 = '/src/assets/svg-editor-image2.svg'
      } else {
        this.showPassword = 'password'
        this.eyeImg1 = eye_img
      }
    },
    toggleVisibility2() {
      this.isShowExPassword = !this.isShowExPassword;
      this.eyeOpen2 = !this.eyeOpen2

      if (this.isShowExPassword) {
        this.showExPassword = 'text'
        this.eyeImg2 = '/src/assets/svg-editor-image2.svg'
      } else {
        this.showExPassword = 'password'
        this.eyeImg2 = eye_img
      }
    },

    async checkCode() {
      let res = await axios.post('/new-password-email', {
        emailCode: this.CIFRY,
      });
      if(res.data.res == 'Error') {
        this.error = '*Ошибка отправки*';
      } else if(res.data.res == 'True') {
        this.$router.push('/EnterNewPassword');
      } else {
        this.error = 'Ошибка';
      }
    },
  }
}

</script>

<template>
  <div class="tototocontainer">
    <div class="background"></div>
    <div class="content">
      <p>Введите код доступа</p>
      <p class="toemail">На почту  {{ email }} вам был отправлен ключ доступа </p>
      <div class="regist">
        <form @submit.prevent="check">
          <div class="kostya_zahotel_po_gorizontali">
            <input class="numinp form-control" type="text" v-model="CIFRY">
            <button @click="check">Подтвердить</button>
          </div>
          <p v-if=this.error class="error">{{ error }}</p>
        </form>
      </div>
    </div>
  </div>
</template>

<style>
.tototocontainer {
  width: 100%;
  display: flex;
}

.background {
  width: 40%;
  height: 92vh;
  background: url(../../assets/Login/backgroundUp.png) center;
  background-repeat: no-repeat;
}

.content p {
  font-size: 42px;
  margin-bottom: 12px;
}

.content {
  margin-top: 219px;
  margin-left: 200px;
}

.regist form {

  flex-direction: row;
  gap: 20px;
  margin-bottom: 40px;
}

.toemail {
  font-size: 20px !important;
  color: #A4A4A4;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0; /* Удалить отступы */
}

.numinp {
  padding-left: 5px;

  width: 280px;
  height: 80px;
  font-size: 80px;
  border-radius: 10px !important;
  border: 1px solid #121212 !important;
}

.regist button {
  /* margin-top: 40px; */
  /* margin-bottom: 15px; */

  width: 220px;
  height: 50px;
  font-size: 24px;
  background: none;

  border: 1px solid #2D72D9;
  border-radius: 8px;
  color: #2D72D9;

  transition: all 100ms;
}

.regist button:active {
  background-color: #2D72D9;
  color: #fff;
}


.regist p {
  font-size: 26px;
  margin: 0;
}

.regist a {
  font-size: 26px;
  color: #2D72D9;
  font-weight: 500;
}

.regist a:hover {
  color: #1b54a9;
}

.regist a:active {
  color: #114189;
}

.error {
  font-size: 18px !important;
  color: #ff1f1f;
  margin-bottom: -30px !important;
  margin-top: -30px !important;
}


.kostya_zahotel_po_gorizontali {
  display: flex;
  gap: 40px;
  align-items: center;

}

@media (hover: hover) {
  .regist button:hover {
    background-color: #2D72D9;
    color: #fff;
  }

  .regist button:active {
    background-color: #1b54a9;
  }

}

@media (max-width: 1330px) {
  .content {
    margin-left: 50px;
  }
}


@media (max-width: 1140px) {
  .content p {
    font-size: 38px;
  }

  .inp {
    width: 550px;
  }

  .haveacc p {
    font-size: 22px;
  }

  .haveacc a {
    font-size: 22px;
  }
}

@media (max-width: 1000px) {
  .kostya_zahotel_po_gorizontali {
    gap: 20px;
  }
}

@media (max-width: 960px) {
  .kostya_zahotel_po_gorizontali {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (max-width: 830px) {
  .background {
    background: none;
    width: 0%;
  }

  .tototocontainer {
    justify-content: center;
  }

  .content {
    margin-left: 10px;
    margin-right: 10px;
  }

  .inp {
    width: 550px;
  }
}

@media(max-width: 600px) {
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .inp {
    width: 350px;
    margin-left: 0;
    margin-right: 0;
  }

  .regist button {
    width: 100%;
  }
}

@media (max-width: 440px) {
  .haveacc {
    flex-direction: column
  }

  .content p {
    text-align: center;
  }
}

</style>
