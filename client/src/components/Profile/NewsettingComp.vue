<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        name: ``,
        surname: ``,
        interestings: ``,
        about: ``,
        country: ``,
        region: ``,
        city: ``,
        email: ``,
        telegram: ``,
        discord: ``,
        phonenumber: ``,
        github: ``,
        avatar: null,
        filename: '',
      },
      defaultAvatar: `src/assets/Header/AvatarDef.svg`,
      id: "",
      isUploading: true,
      percentCompleted: 0,
      isLoading: false,
      isAllLoad: false,
    };
  },

  mounted() {
    this.getUser();
  },

  methods: {
    async putInfo() {
      this.form.interestings = this.form.interestings.substr(0, 48);
      this.isLoading = true;
      this.isUploading = true; // Включаем индикатор загрузки
      try {
        await axios.put(
          "/user-info",
          {
            form: this.form,
          },
          {
            onUploadProgress: (progressEvent) => {
              const percentCompleted = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
              this.percentCompleted = percentCompleted;
            },
          }
        );
        this.isUploading = true; // Выключаем индикатор загрузки
        // this.$router.push(`/Profile/${this.id}`)
      } catch (error) {
        console.error("Ошибка при отправке данных:", error);
        this.isUploading = false; // Выключаем индикатор загрузки
        // Добавьте обработку ошибки
      }
    },

    triggerFileInput() {
      const fileInput = document.getElementById('fileInput');
      fileInput.click();
    },

    convertFileAvatar(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      const filename = event.target.files[0].name;
      this.form.filename = filename;
      reader.onload = () => {
        this.form.avatar = reader.result;
        console.log(reader.result);
      };
      reader.readAsDataURL(file);
    },
    async getUser() {
      let res = await axios.get("/session");
      this.id = res.data.id;

      this.getUserInfo(this.id);
    },
    async getUserInfo(id) {
      let res = await axios.get("/user-info-r", {
        params: {
          id: id,
        },
      });
      this.form = res.data.all;
      this.preloader();
    },
    deleteAvatar() {
      this.form.avatar = this.defaultAvatar;
    },
    async logout() {


      this.$router.push("/Login");
      let res = await axios.get("/");
      this.$router.go(0);
    },
    forgot() {
      this.$router.push("/RecoveryPassPage");
    },
    des() {
      this.$router.push("/auth-tg-desription");
    },

    async preloader() {
      if (this.form) {
        this.isAllLoad = true;
      }
    },
  },
};
</script>


<template>
  <form @submit.prevent="putInfo" v-if='this.isAllLoad'>
    <div class="window">

      <div class="comp">
        <h1>Настройки профиля</h1>

        <div class="ancet d-flex" style="display: flex; gap: 40px">
          <h5 role="button" class="mb-0 border-bottom border-2 border-dark">
            <a href="/NewSetting">Анкета</a>
          </h5>
          <h5 role="button" class="mb-0" style="color: gray; font-weight: 400">
            <a href="/Changepass">Аккаунт</a>
          </h5>
        </div>

        <div class="main-info">
          <div class="avatar">
            <div class="cscscsc">
              <img v-if='this.id' :src="form.avatar" alt="Фото профиля"> 
            </div>
            <div class="btns">
              <button @click="deleteAvatar">Удалить</button>
              <button @click="triggerFileInput">Заменить</button>
              <input type="file" id="fileInput" @change="convertFileAvatar" style="display: none;">
            </div>
            <p>Размер загружаемого изображения <br> не должен превышать 10 мб</p>
          </div>
          <div class="name">
            <div class="name-sure">
              <div class="username">
                <input v-model="form.name" type="text" maxlength="50">
                <span>Имя</span>
              </div>
              <div class="surename">
                <input v-model="form.surname" type="text" maxlength="50">
                <span>Фамилия</span>
              </div>
            </div>

            <div class="interests">
              <textarea v-model="form.interestings" id="" name="" cols="30" rows="10" maxlength="2000"></textarea>
              <span>Интересы</span>
            </div>

          </div>
        </div>

        <div class="action">
          <h2>Действия с аккаунтом</h2>
          <div class="btns-act">
            <button @click="des">Привязать Telegram</button>
            <button @click="logout">Выйти из аккаунта</button>
            <button @click="forgot">Забыли пароль?</button>
          </div>
        </div>
        <div class="aboutme">
          <div class="about-comp">
            <textarea v-model="form.about" id="" name="" cols="30" rows="10" maxlength="2000"></textarea>
            <span>О себе</span>
          </div>

          <div class="about-links">
            <div class="email bl">
              <h3>Email</h3>
              <input type="email" v-model="form.email">
            </div>
            <div class="github bl">
              <h3>GitHub</h3>
              <input type="text" v-model="form.github">
            </div>
            <div class="telegram-link bl">
              <h3>Telegram</h3>
              <input type="text" v-model="form.telegram">
            </div>
            <div class="discord bl">
              <h3>Discord</h3>
              <input type="text" v-model="form.discord">
            </div>
            <div class="phone-number bl">
              <h3>Номер телефона</h3>
              <input type="number" v-model="form.phonenumber">
            </div>
            <div class="save">
              <button type="submit">Сохранить изменениия</button>
            </div>
          </div>
        </div>

      </div>
    </div>
    <div v-if='this.id == null' class='w-100 h-100 d-flex justify-content-center align-items-center'>
      <div class="bg-black1"></div>
      <div class="modal-cenel d-flex flex-column align-items-center">
        <img src="../../assets/Lending/bookModal.png" alt="Грусть(">
        <h6>У вас недостаточно прав доступа, войдите в аккаунт</h6>
        <button @click='this.$router.push("/Login")'>Войти</button>
      </div>
    </div>
  </form>
</template>

<style scoped>
.cscscsc {
  width: 250px;
  height: 250px;
  border: 2px solid #000;
  border-radius: 8px;
}

.modal-cenel {
  opacity: 1 !important;
  position: fixed;
  top: calc(50% - 160px);
  z-index: 52 !important;
  background: rgba(59, 130, 246, 0.65);
  padding: 24px;
  border-radius: 10px;
  color: #fff;
  gap: 20px;
}

@media (max-width: 900px) {
  .modal-cenel {
    margin: 0 32px !important;
  }
}

.modal-cenel button {
  border-radius: 10px;
  border: 1px solid#fff;
  padding: 4px 24px;
  background: none;
  color: #fff;
  opacity: 1 !important;
}

.modal-cenel h6 {
  opacity: 1 !important;
}

.modal-cenel img {
  border-radius: 0% !important;
  width: 150px;
  opacity: 1 !important;
}

.bg-black1 {
  background: rgba(41, 41, 41, 0.7) !important; /* Полупрозрачный фон */
  z-index: 1;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  backdrop-filter: blur(5px) !important;
}

.save {
  display: flex;
  justify-content: center;
  width: 100%;
}

.save button {
  background-color: rgb(255, 255, 255);
  font-size: 22px;
  font-weight: 550;
  color: #7ac97a;
  border: 2px solid #7ac97a;
  border-radius: 5px;
  width: 360px;
  padding: 5px 15px;
  text-align: center;
  transition: all 200ms;
}

.save button:hover {
  background-color: #7ac97a;
  color: #ffffff;
}

.save button:active {
  background-color: #5ba35b;
}

.window {
  width: 100%;
  height: auto;

  display: flex;
  justify-content: center;
  align-items: start;
}

.comp {
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: start;
}

.comp h1 {
  width: 100%;
  font-size: 30px;
  border-bottom: 2px solid #000;
  padding-bottom: 30px;
}

.comp h2 {
  color: #000;
  font-size: 30px !important;
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
  justify-content: center;
  gap: 60px;
  padding-top: 50px;
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
  width: 250px;
  height: 250px;
  border: 2px solid #000;
  border-radius: 8px;
  object-fit: cover;
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
  width: 300px;
  height: 40px;
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
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

.surename input {
  width: 300px;
  height: 40px;
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
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

.interests textarea {
  width: 650px;
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
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

.action {
  display: flex;
  flex-direction: column;
  gap: 60px;
  width: 100%;
  padding-top: 50px;
  padding-bottom: 80px;

  border-bottom: 2px solid #000;
}

.btns-act {
  display: flex;
  justify-content: space-evenly;
}

.btns-act button {
  background-color: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 14px;
  width: 230px;
  height: 46px;
  font-size: 20px;
}

.aboutme {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding-top: 100px;
  padding-bottom: 100px;
}

.about-comp {
  width: 85%;
  padding-bottom: 80px;
  display: flex;
  justify-content: center;
  position: relative;
}

.aboutme textarea {
  width: 100%;
  border: 2px solid #000;
  border-radius: 12px;
  padding: 20px 10px;
  font-size: 20px;
  font-weight: 400;
  resize: none;
}

.aboutme span {
  position: absolute;
  left: 50px;
  top: -22px;

  background-color: #3b82f6;
  color: #fff;
  font-size: 18px;
  padding: 1px 20px;
  border-radius: 8px;
  font-weight: 500;
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
  align-items: center;

  gap: 40px;
}

.bl {
  display: flex;
  gap: 10%;
}

.bl h3 {
  display: grid;
  place-items: center;
  width: 260px !important;
  height: 50px;
  border: 2px solid #3b82f6;
  border-radius: 8px;
  font-size: 22px;
  font-weight: 550;
  margin: 0;
}

.bl input {
  width: 800px;
  border: 2px solid #000;
  border-radius: 8px;
  font-size: 20px;
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
  .main-info {}
}

@media (max-width: 1400px) {
  .main-info {}

  .name-sure {
    flex-direction: column;
  }

  .username input {
    width: 350px;
  }

  .surename input {
    width: 350px;
  }

  .interests textarea {
    width: 350px;
  }

}

@media (max-width: 1350px) {
  .btns-act button {
    width: 330px;
  }

  .btns-act {
    gap: 10px;
  }

  .bl input {
    width: 550px;
  }

  .bl {
    gap: 5%;
  }

  .bl h3 {
    width: 250px !important;
  }
}

@media (max-width: 1120px) {
  .btns-act button {
    width: 290px;
  }

  .username input {
    width: 300px;
  }

  .surename input {
    width: 300px;
  }

  .interests textarea {
    width: 300px;
  }
}

@media (max-width: 1000px) {
  .bl input {
    width: 350px;
  }

  .bl h3 {
    width: 200px !important;
    font-size: 18px;
  }
}

@media (max-width: 970px) {
  .main-info {
    gap: 5%;
  }
}

@media (max-width: 860px) {
  .btns-act {
    flex-direction: column;
    align-items: center;
  }

  .action h2 {
    font-size: 30px;
    font-weight: 500;
  }

  .btns-act button {
    width: 65%;
    gap: 20px;
  }

  .avatar img {
    width: 200px;
    height: 200px;
  }

  .btns button {
    width: 95px;
  }

  .about-comp {
    width: 100%;
  }
}

@media (max-width: 750px) {
  .comp {
    width: 90%;
  }
}

@media (max-width: 730px) {
  .comp {
    margin-top: -20px;
  }

  .main-info {
    flex-direction: column;
    gap: 30px;
    align-items: center;
    justify-content: start;
  }

  h1 {
    font-size: 26px !important;
  }

  .action h2 {
    font-size: 26px !important;
  }

  .links p {
    font-size: 18px;
  }

  .username input {
    width: 600px;
  }

  .surename input {
    width: 600px;
  }

  .interests textarea {
    width: 600px;
  }

  .avatar img {
    width: 250px;
    height: 250px;
  }

  .btns-act {
    align-items: center;
  }

  .btns-act button {
    width: 80%;
  }
}

@media (max-width: 630px) {
  .bl {
    flex-direction: column;
    align-items: center;
  }

  .bl h3 {
    width: 350px !important;
  }

  .bl input {
    width: 350px;
    height: 50px;
  }

  .username input {
    width: 400px;
  }

  .surename input {
    width: 400px;
  }

  .interests textarea {
    width: 400px;
  }

}

@media (max-width: 450px) {
  .bl h3 {
    width: 330px !important;
  }

  .save button {
    font-size: 18px;
    width: 250px;
  }

  .btns-act button {
    width: 90%;
    font-size: 20px;

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
