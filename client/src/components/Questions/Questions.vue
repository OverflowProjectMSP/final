<script>
import axios from "axios";
import VidQuetions from "../ReuseComponets/QuetionVid.vue";
import ModelWind from "../ReuseComponets/ModelWind.vue";
import NewqueVid from "../Edit/NewqueVid.vue";

export default {
  components: {
    VidQuetions,
    ModelWind,
    NewqueVid,
  },

  data() {
    return {
      quetions: [],

      tag: ``,
      dificulty: ``,
      title: ``,
      author: ``,
      Show: false,
      cnt: 0,
      isAllLoad: false,

      // Пагинация
      currentPage: 1, // Номер текущей страницы
      questionsPerPage: 5, // Количество вопросов на странице
      totalQuestions: 0, // Общее количество вопросов
      totalPages: 0, // Общее количество страниц
      maxVisiblePages: 4, // Максимальное количество отображаемых номеров страниц
    };
  },
  mounted() {
    this.loadQuestions(1);
  },
  methods: {
    loadQuestions(page) {
      this.currentPage = page;
      const start = page * this.questionsPerPage - this.questionsPerPage + 1; // Начало интервала
      const end = page * this.questionsPerPage; // Конец интервала
      // Отправка запроса на бекенд с интервалом start-end
      this.getQuestions(start, end);
    },
    async getQuestions(start, end) {
      console.log(start, end);
      try {
        const res = await axios.get(
          `https://api.upfollow.ru/get-questions?start=${start}&end=${end}`
        );
        this.quetions = res.data.res;
        console.log(this.quetions);
        this.totalQuestions = res.data.count; // Получение общего количества вопросов от бекенда
        this.totalPages = Math.ceil(
          this.totalQuestions / this.questionsPerPage
        ); // Обновление общего количества страниц
      } catch (err) {}
    },

    loadPage(page) {
      this.loadQuestions(page);
    },
    loadPreviousPage() {
      if (this.currentPage > 1) {
        this.loadQuestions(this.currentPage - 1);
      }
    },
    loadNextPage() {
      if (this.currentPage * this.questionsPerPage < this.totalQuestions) {
        this.loadQuestions(this.currentPage + 1);
      }
    },
    handleDotsClick(direction) {
      if (direction === "left") {
        this.loadPage(this.currentPage - this.maxVisiblePages); // Переход на первую страницу из видимого диапазона
      } else if (direction === "right") {
        this.loadPage(this.currentPage + this.maxVisiblePages); // Переход на последнюю страницу из видимого диапазона
      }
    },

    CloseModal(Show) {
      this.Show = false;
    },

    async filtre() {
      let res = await axios.get("/filtre-questions", {
        params: {
          title: this.title,
          author: this.author,
          tag: this.tag,
          dificulty: this.dificulty,
        },
      });
      this.quetions = res.data.all;
    },

  },
  computed: {
    visiblePages() {
      const pages = [];
      // Отображаем 4 страницы, но если меньше, то все
      const start = Math.max(1, this.currentPage - 1);
      const end = Math.min(this.totalPages, this.currentPage + 2);

      // Если общее количество страниц меньше, чем maxVisiblePages,
      // отображаем все страницы
      if (this.totalPages <= this.maxVisiblePages) {
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
      } else {
        for (let i = start; i <= end; i++) {
          pages.push(i);
        }
      }

      return pages;
    },
    showDotsLeft() {
      return this.currentPage > this.maxVisiblePages + 1;
    },
    showDotsRight() {
      return this.currentPage + this.maxVisiblePages < this.totalPages;
    },
  },
};
</script>

<template>
  <div>
    <div class="quest-menu mt-3">
      <div class="active-container d-flex flex-column p-2">
        <h2 class="mar">Активные вопросы</h2>
        <p class="mar">
          В данном разделе находятся вопросы, которые ждут именно
          <b>твоего</b> ответа!
        </p>
        <div class="all-inputs">
          <div class="inputs">
            <input
              v-model="title"
              type="search"
              class="form-control w-25"
              placeholder="Вопрос"
              aria-label="First name"
            />
            <input
              v-model="author"
              type="search"
              class="form-control w-25"
              placeholder="Автор вопроса"
              aria-label="Last name"
            />
            <div class="button-select">
              <div class="selects">
                <select class="form-select form-2 me-2" v-model="tag">
                  <option value="">Тема вопроса</option>
                  <option value="javascript">JavaScript</option>
                  <option value="ts">TS</option>
                  <option value="python">Python</option>
                  <option value="php">PHP</option>
                  <option value="cpp">C++</option>
                  <option value="java">Java</option>
                  <option value="cs">C#</option>
                  <option value="go">Golang</option>
                  <option value="IB">ИБ</option>
                </select>

                <div class="img-select">
                  <!-- <img class="border pe-2 ps-2" src="../../assets/States/image.png" alt="level"> -->
                  <select class="form-select form-1" v-model="dificulty">
                    <option value="">Степень сложности</option>
                    <option value="Простой" selected>Лёгкие</option>
                    <option value="Средний">Средние</option>
                    <option value="Сложный">Сложные</option>
                  </select>
                </div>
                <button
                  class="btn find-btn btn-outline-primary text-dark ms-4"
                  @click="filtre"
                >
                  Найти
                </button>
              </div>
              <!-- <div class="select-block d-flex border rounded-3 gap-1 py-0  me-2"> -->
              <!-- </div> -->
              <div class="down-menu d-flex align-items-center">
                <div class="d-flex align-items-center">
                  <!-- плюсик -->
                  <!-- <div class="contain" @click="OpenModal">
                                        <img src="../../assets/States/add.png" class="add">
                                    </div> -->
                </div>
              </div>
              <a href="/NewQuestion"
                ><button class="create-quetion">Создать вопрос</button></a
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="cont d-flex align-items-center">
      <div class="con" v-for="item in quetions" :key="item.id">
          <a :href="`/QuestionItem/` + item.id">
          <NewqueVid :data="item" :user="{}" />
        </a>
      </div>
    </div>
    <div class="content p-2" v-if="this.quetions.length == 0 && this.cnt == 1">
      <h2 class="d-flex justify-content-center my-5 user-select-none">
        Будь первым, кто даст ответ на этот вопрос!
      </h2>
    </div>
  </div>

  <!-- Пагинация -->

  <div class="pagination">
    <div class="pagination-controls">
      <button
        @click="loadPreviousPage"
        :disabled="currentPage === 1"
        class="todo"
        style="margin-right: 3px"
      >
        <
      </button>
      <span v-if="showDotsLeft" class="dots" @click="handleDotsClick('left')"
        >...</span
      >
      <div class="span-div">
        <button
          v-for="page in visiblePages"
          :key="page"
          :class="{ active: page === currentPage }"
          @click="loadPage(page)"
          class="span"
        >
          {{ page }}
        </button>
      </div>
      <span v-if="showDotsRight" class="dots" @click="handleDotsClick('right')"
        >...</span
      >
      <button
        @click="loadNextPage"
        :disabled="currentPage === totalPages"
        class="todo"
        style="margin-left: 3px"
      >
        >
      </button>
    </div>
  </div>
</template>

<style scoped>
/* Пагиинацииия */

.pagination {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 20px;
  gap: 50px;
}
.span-div {
  display: flex;
  gap: 5px;
}
.dots a {
  color: white;
}
.dots {
  display: grid;
  place-items: center;
  background-color: #629bf7;
  text-align: center;
  width: 41px;
  height: 41px;
  border: none;
  border-radius: 50% !important;
  color: white !important;
  font-weight: 500;
}
.span {
  display: grid;
  place-items: center;
  background-color: #629bf7;
  text-align: center;
  width: 41px;
  height: 41px;
  border: none;
  border-radius: 50% !important;
  color: white;
  font-weight: 500;
  cursor: poiner;
}
span {
  cursor: poiner;
}
.todo {
  display: grid;
  place-items: center;
  background-color: #629bf7;
  text-align: center;
  width: 41px;
  height: 41px;
  border: none;
  border-radius: 50% !important;
  color: white;
  font-weight: 500;
  cursor: poiner !important;
}

.pagination-controls {
  display: flex;
  margin-top: 10px;
}

.dots {
  margin: 0 5px;
  cursor: pointer;
  color: #333;
}

.dots:hover {
  text-decoration: underline;
}
.todo:disabled {
  font-weight: bold;
  background-color: #8a9096;
  color: white;
}
.active {
  font-weight: bold;
  background-color: #8a9096;
  color: white;
}

.mar {
  margin-left: 5px;
  color: #000;
}

.active-container h2 {
  font-size: 30px !important;
}

.find-btn {
  margin-left: 10px !important;
}

.cont {
  /* overflow: scroll; */

  width: auto;
  margin-left: auto;
  margin-right: auto;
  padding-top: 10px;

  gap: 5px;
}

a {
  text-decoration: none;
  color: #000;
}

.selects {
  display: flex;
  gap: 10px;
}

.img-select {
  display: flex;
}

.headernew {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-bottom: 0px !important;
  padding: 0 10px !important;
}

.form-select {
  width: 280px !important;
}

.selects img {
  border-radius: 10px 0 0 10px;
}

.form-1 {
  border-radius: 0 10px 10px 0;
}

.button-select {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  flex-wrap: wrap;
  width: 100%;
  margin-left: 5px;
  /* margin-right: 5px; */
}

.create-quetion {
  width: 280px;
  height: 37px;

  background-color: #3b82f6;
  color: #fff;
  border: none;
  border-radius: 5px;

  font-size: 20px;
  font-weight: 500;
  /* margin-left: 5px; */
  margin-top: 5px;

  transition: all 100ms;
}

.create-quetion:hover {
  background-color: #20498b;
}

.form-2 {
  border-radius: 10px;
}

.all-inputs {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-control {
  width: 800px !important;
}

.quest-menu {
  display: flex;
  justify-content: center;
  /* margin: 0 20% 15px 20%; */
  /* min-height: 57.5vh; Изменить на 52 */
}

@media (max-width: 500px) {
  /* .quest-menu {
        margin: 0;
        margin-bottom: 5px;
    } */

  .selects {
    flex-direction: column;
  }

  .img-select {
    display: flex;
    margin-right: 0;
  }

  .selects img {
    width: 50px;
  }
}

.select-block {
  width: fit-content;
}

.select-block img {
  background-color: #e7e7e7;
}

.active-container {
  margin-bottom: 40px;
}

h4 {
  margin-left: 20.5%;
  margin-top: 20px;
  font-size: 40px;
}

.image {
  margin-right: 10px;
  width: 25px;
}

.add {
  width: 25px;
  height: 25px;
  cursor: pointer;
}

.btn {
  width: 200px;
  font-size: 16px;
  font-weight: bold;
  color: blueviolet;
}

.content {
  margin: 10px;
  flex-wrap: wrap;
  margin-left: 20%;
}

.form-control {
  margin: 5px;
}

.dropdown-center {
  margin-left: 15px;
}

.content input {
  width: 300px;
  border-radius: 10px;
}

.con {
  justify-content: start;
}

.contain {
  width: 5%;
  height: 5%;
}

.plus {
  width: 30px;
  height: 30px;
  background-color: #e8e7ea;
  border-radius: 50%;
  border: 0.0001px solid;
}

.p {
  margin-left: 0.2px;
  margin-right: 1px;
}

.dropdown-center {
  margin-right: 10px;
}

@media (hover: hover) {
  .find-btn:hover {
    color: #fff !important;
  }
}

@media (max-width: 1200px) {
  .all-inputs {
    flex-direction: column !important;
    align-items: center;
  }

  .active-container {
    text-align: center;
  }

  .mar {
    margin: 0;
  }

  .form-control {
    width: 500px !important;
  }

  .button-select {
    flex-direction: column;
    align-items: center;
  }

  .selects {
    display: flex;
    gap: 20px;
    margin-left: -4px;
  }

  .selects {
    flex-direction: column;
    align-items: start;
    gap: 5px;
  }

  .form-select {
    width: 501px !important;
  }

  .btn {
    margin-top: 2px;
    width: 501px;
    margin-left: 0px !important;
  }

  .form-2 {
    width: 501px !important;
  }

  .create-quetion {
    width: 501px;
    margin-left: -10px;
  }
}

@media (max-width: 870px) {
  .active-container {
    align-items: center;
  }

  .mar {
    width: 300px;
  }
}

@media (max-width: 600px) {
  .selects {
    gap: 10px;
    align-items: center;
  }

  .form-select {
    width: 350px !important;
  }

  .form-1 {
    margin-left: -9px;
  }

  .form-2 {
    margin-left: 2px !important;
  }

  .button-select {
    align-items: center;
  }

  .btn {
    width: 350px;
    margin-left: -10px !important;
  }

  .create-quetion {
    width: 350px;
  }

  .selects img {
    margin-right: -10px;
  }

  .img-select {
    gap: 10px;
  }

  .form-control {
    width: 350px !important;
  }
}

@media (min-width: 2100px) {
  .cont {
    height: 700px;
  }

  .active-container h2 {
    font-size: 50px;
  }

  .active-container p {
    font-size: 24px;
  }

  .all-inputs {
    width: 1000px;
  }

  .form-control {
    width: 1000px !important;
    height: 50px;
    font-size: 18px;
  }

  .button-select {
    width: 1000px;
  }

  .form-select {
    width: 319px !important;
    height: 50px;
    font-size: 18px;
  }

  .find-btn {
    width: 318px;
    font-size: 18px;
    height: 50px;
  }

  .create-quetion {
    width: 319px;
    height: 50px;
    font-size: 22px;
  }
}

@media (min-width: 3200px) {
  .cont {
    height: 1200px;
  }

  .active-container h2 {
    font-size: 70px;
  }

  .active-container p {
    font-size: 36px;
  }

  .all-inputs {
    width: 1400px;
  }

  .form-control {
    width: 1300px !important;
    height: 60px;
    font-size: 26px;
  }

  .button-select {
    width: 1300px;
  }

  .form-select {
    width: 418px !important;
    height: 60px;
    font-size: 26px;
  }

  .find-btn {
    width: 419px;
    height: 60px;
    font-size: 26px;
  }

  .create-quetion {
    width: 418px;
    height: 60px;
    font-size: 30px;
  }
}

@media (min-width: 4500px) {
  .cont {
    height: 1600px;
  }

  .active-container h2 {
    font-size: 100px;
  }

  .active-container p {
    font-size: 50px;
  }

  .all-inputs {
    width: 1900px;
  }

  .form-control {
    width: 1800px !important;
    height: 90px;
    font-size: 45px;
  }

  .button-select {
    width: 1800px;
  }

  .form-select {
    width: 586px !important;
    height: 90px;
    font-size: 45px;
  }

  .find-btn {
    width: 586px;
    height: 90px;
    font-size: 45px;
  }

  .create-quetion {
    width: 586px;
    height: 90px;
    font-size: 50px;
  }
}

@media (min-width: 5800px) {
  .cont {
    height: 2400px;
  }

  .active-container h2 {
    font-size: 160px;
  }

  .active-container p {
    font-size: 70px;
  }

  .all-inputs {
    width: 2650px;
  }

  .form-control {
    width: 2500px !important;
    height: 120px;
    font-size: 60px;
  }

  .button-select {
    width: 2500px;
  }

  .form-select {
    width: 819px !important;
    height: 120px;
    font-size: 60px;
  }

  .find-btn {
    width: 819px;
    height: 120px;
    font-size: 60px;
  }

  .create-quetion {
    width: 819px;
    height: 120px;
    font-size: 65px;
  }
}
</style>
