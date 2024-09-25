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
        avatar: ``,
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
        this.$router.push(`/Profile/${this.id}`)
      } catch (error) {
        console.error("Ошибка при отправке данных:", error);
        this.isUploading = false; // Выключаем индикатор загрузки
        // Добавьте обработку ошибки
      }
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
  <form class="container mb-3" @submit.prevent="putInfo" v-if='this.isAllLoad'>
    <div class="row pt-5">
      <div class="col-3">
        <h3>Настройки профиля</h3>
      </div>
    </div>
    <hr />
    <div class="ancet d-flex" style="display: flex; gap: 40px">
      <h5 role="button" class="mb-0 border-bottom border-2 border-dark">
        <a href="/ProfileSettings">Анкета</a>
      </h5>
      <h5 role="button" class="mb-0" style="color: gray; font-weight: 400">
        <a href="/ChangePassword">Аккаунт</a>
      </h5>
    </div>
    <hr />
    <div class="main-block d-flex flex-row gap-4 mt-2">
      <hr class="hr-down" />
      <div class="image-block">
        <div class="d-flex flex-column justify-content-center">
          <div style="text-align: center">
            <img
              v-if="this.form.avatar == ``"
              :src="defaultAvatar"
              class="mb-2"
              alt="Фото профиля"
              style="height: 100px;"
            />
            <img
              v-else
              :src="form.avatar"
              class="mb-2"
              alt="Фото профиля"
              style="height: 100px"
            />
            <p style="color: gray">Ваша фотография.</p>
            <p style="color: gray">
              Размер загружаемой фотографии <br />
              не должен быть более 10 МБ.
            </p>
            <!-- <button class="btn btn-outline-primary" style="margin-right: 10px;"
                            type="file">Загрузить</button> -->
            <button class="btn btn-outline-secondary" @click="deleteAvatar">
              Удалить
            </button>
          </div>
        </div>
      </div>
      <div class="info-block">
        <div class="row">
          <div class="col-6">
            <div>
              <h5>Имя</h5>
              <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="form.name" />
              </div>
            </div>
          </div>
          <div class="col-6">
            <div>
              <h5>Фамилия</h5>
              <div class="input-group mb-3">
                <input
                  type="text"
                  class="form-control"
                  v-model="form.surname"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <h5>Интересы</h5>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                aria-label="Interests"
                aria-describedby="basic-addon1"
                v-model="form.interestings"
              />
            </div>
            <div class="mb-3">
              <label for="exampleFormControlInput1" class="form-label"
                ><h5>Обновить фото</h5></label
              >
              <input
                type="file"
                class="form-control"
                id="exampleFormControlInput1"
                placeholder="name@example.com"
                @change="convertFileAvatar"
              />
            </div>

            
            <div class="mb-3" v-if="false">
              <label for="exampleFormControlInput1" class="form-label mt-3"
              ><h5>Загрузка данных на сервер...</h5></label
              >
              <progress
                max="100"
                :value="this.percentCompleted"
                v-if="this.isUploading"
              ></progress> <p>{{ this.percentCompleted }} %</p>
            </div>
          </div>
        </div>
        <hr />
        <div class="mb-3 actions">
          <label for="exampleFormControlInput1" class="form-label"
            ><h5>Действия с аккаунтом</h5></label
            >
            <button class="btn btn-primary" @click="des">
              Привязка Telegram <img src="../../assets/Footer/Telegram.png" class="tg-img"/>
            </button> 
          <button class="btn btn-danger logout" @click="logout">
            Выйти из аккаунта</button
          ><button class="btn btn-primary" @click="forgot">
            Забыли пароль?
          </button>
        </div>
        <hr/>
        <div class="row">
          <div class="col-12">
            <h5>О себе</h5>
            <div class="input-group mb-3">
              <textarea
                type="text"
                class="form-control"
                placeholder=""
                aria-label="About"
                aria-describedby="basic-addon1"
                style="height: 150px"
                v-model="form.about"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="row contact-container">
            <h5>Контакты</h5>
            <div class="col-12" style="display: flex">
              <div class="d-flex flex-column">
                <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                  <div class="border px-3 py-1 rounded-3 h-fit">Email</div>
                  <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.email"
                  />
                </div>
                <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                  <div class="border px-3 py-1 rounded-3 h-fit">GitHub</div>
                  <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.github"
                  />
                </div>
                <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                  <div class="border px-3 py-1 rounded-3 h-fit">Telegram</div>
                  <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.telegram"
                  />
                </div>
                <!-- <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                  <div class="border px-3 py-1 rounded-3 h-fit">Skype</div>
                <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.skype"
                  />
              </div> -->
              <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                <div class="border px-3 py-1 rounded-3 h-fit">Discord</div>
                <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.discord"
                />
              </div>
              <!-- <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                <div class="border px-3 py-1 rounded-3 h-fit">Facebook</div>
                <input
                type="text"
                class="form-control contact-input"
                style="margin-left: 30px"
                v-model="form.facebook"
                />
              </div> -->
              <div class="contact-plus d-flex align-items-center gap-0 mb-3">
                <div class="border px-3 py-1 rounded-3 h-fit">
                  Номер телефона:
                </div>
                <input
                  type="text"
                  class="form-control contact-input"
                  style="margin-left: 30px"
                  v-model="form.phonenumber"
                  />
                </div>
              </div>
          </div>
        </div>
        <div class="mt-3">
          <h5 class="location mb-3">Местоположение</h5>
          <div class="row place-container gap-3" style="display: flex">
            <select
            style="width: 350px"
            role="button"
            class="country-select form-select"
            v-model="form.country"
            >
            <option value="Belarus" selected>Страна невыбрана</option>
            <option value="Russia">Россия</option>
            <option value="Belarus">Белоруссия</option>
            <option value="Germany">Германия</option>
              <option value="China">Китай</option>
              <option value="Japan">Япония</option>
              <option value="USA">США</option>
              <option value="UK">Великобритания</option>
            </select>
            <input
            type="text"
            class="form-control"
            placeholder="Регион"
            v-model="form.region"
            />
            <input
              type="text"
              class="form-control"
              placeholder="Город"
              v-model="form.city"
            />
          </div>
        </div>
        <div class="d-flex justify-content-start mt-4 ms-0 mb-3">
          <button class="btn btn-success" type="submit">
            <b>Сохранить изменения</b>
          </button>
        </div>
      </div>
    </div>
  </form>
  <form class="co" v-else>
    <div class="load-item item1"></div>
    <div class="load-item item2"></div>
    <div class="load-item item3"></div>
    <div class="load-item item4"></div>
    <div class="load-item item5"></div>
  </form>
</template>
<style scoped>
.tg-img{
width: 25px;
height: 25px;
margin-left: 5px;
}
.actions{
display: flex;
gap: 8px;
flex-wrap: wrap
;
}
.location{
  margin-left: -11px;
}
.btn-success{
  margin-left: -11px;
}
  .country-select {
    width: 100% !important;
    border: solid 1px black;
    margin-left: -100px;
    padding-left: 10px;
    margin-left: 0px;
  }
.form-label {
  width: 100%;
}

.contact-plus div {
  width: 260px;
}
.logout {
  margin-right: 0px;
}
#download,
#save {
  background-color: white;
  color: #7ac97a;
  border-color: #90ee90;
  border-radius: 5px;
  padding-right: 15px;
  padding-left: 15px;
  text-align: center;
  transition: all 300ms;
  padding: 10px 25px;
}

#delete:hover {
  color: #000;
}

/* select {
  padding: 7.5px 15px 7.5px 2px;
  border-radius: 3px;
  transition: all 300ms;
} */

select:hover {
  border-color: blue;
}

@media (max-width: 1224px) {
  .place-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 15px !important;
  }

  .s-place {
    margin-left: 10px !important;
    width: 90% !important;
  }

  .country-select {
    width: 100% !important;
    border: solid 1px black;
  }

  .main-block {
    flex-direction: column !important;
  }

  .hr-down {
    display: none !important;
  }
}

@media (max-width: 540px) {
  .country-select {
    max-width: 90% !important;
  }

  .contact-input {
    margin-left: 12px !important;
  }
}

@media (max-width: 360px) {
  .country-select {
    max-width: 90% !important;
  }
}
</style>
