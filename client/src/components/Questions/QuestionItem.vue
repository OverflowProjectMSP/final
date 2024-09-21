<script>

import UpdateQuestion from './UpdateQuestion.vue';

import axios from 'axios';

export default {
  components: { UpdateQuestion },
  data() {
    return {
      questionInfo: {}, //главная возня
      answers: [],
      answerUser: [],
      userCreater: {},
      userNow: {},

      user: {},

      text: '',
      symbols: 0,
      symbCount: false,
      isBold: false,
      isItalic: false,

      count: 0,
      countmin: 0,

      isCheck: null,

      loading: false,

      updQ: false,
      ShowAdd: true,
      isAdmin: false,

      isAllLoad: false,

      isOpenDeleteAnswer: false,
    }
  },

  methods: {
    async loadQuestion() {
      let responce = await axios.get(`/show-one`, {
        params: {
          id: this.$route.params.id,
          q: true,
        }
      });
      this.questionInfo = responce.data.all.question;
      this.answers = responce.data.all.answers;
      const regex = /\\n|\\r\\n|\\n\\r|\\r/g;
      this.questionInfo.details = this.questionInfo.details.replaceAll(regex, '<br>')
      this.loadAnswerUser();
      this.preloader();
    },

    async loadAnswerUser() {
      this.userCreater = await this.loadUsers(this.questionInfo);
      this.CheckUserIsEdit()
      for (let i = 0; i < this.answers.length; i++) {
        let user = await this.loadUsers(this.answers[i]);
        this.answers[i].isOpenRemoved = false;
        this.answerUser.push(user)
      };
      this.v_For1();
    },


    async loadUsers(item) {
      let res = await axios.get('/user-not-all', {
        params: {
          id: item.id_u,
        }
      });
      return res.data.all;
    },

    symbolsCount() {
      this.symbols = this.text.length;
      if (this.symbols >= 2000) {
        this.symbCount = true;
      } else {
        this.symbCount = false;
      }
    },

    async addComment() {
      if (this.text.length >= 3) {
        await axios.post(`/answers`, {
          id: this.$route.params.id,
          q: 'true',
          text: this.text,
        });
        this.answers.push({
          id_u: this.userNow.id,
          text: this.text,
          user: this.userNow
        });

        this.text = ``;
        this.v_For1()
      }
    },
    async deleteQuestion() {
      await axios.delete('/delete', {
        params: {
          id: this.$route.params.id,
          q: true,
        }
      });
      this.$router.push(`/Quetions`)
    },
    // async checkUser() {
    //     let res = await axios.get('/check', {
    //         params: {
    //             id: this.userCreater.id
    //         }
    //     });
    //     this.isCheck = res.data.isEdit;
    // },
    async getNowUser() {
      let res = await axios.get('/session');
      this.loadNowUser(res.data.id);
    },

    v_For1() {
      if (this.answers.length != 0) {
        for (let i = 0; i < this.answerUser.length; i++) {
          this.answers[i].user = this.answerUser[i];
          const regex = /\\n|\\r\\n|\\n\\r|\\r/g;
          this.answers[i].text = this.answers[i].text.replaceAll(regex, '<br>')
        }
        if (this.answers[this.answers.length - 1].user.avatar != ``) {
          this.loading = true;
        } else {
          this.loading = false;
        }
      } else {
        this.loading = true;
      }
    },

    async loadNowUser(id) {

      let res = await axios.get('/user-not-all', {
        params: {
          id: id,
        }
      });
      this.userNow = res.data.all;
    },

    async solveQuestion(is) {
      await axios.put(`/is-solved`, {
        id: this.$route.params.id,
        is_solved: is,
      });
    },

    async CheckUserIsEdit() {
      let res = await axios.get('/check', {
        params: {
          id: this.userCreater.id,
        }
      });

      this.isCheck = res.data.isEdit

      this.checkIsAdmin()
    },

    fixN(text) {
      return text
    },

    async checkUser() {
      let res = await axios.get(`/check-r`);
      this.ShowAdd = res.data.all;
      if (this.ShowAdd == "true") {
        this.ShowAdd = true
        return

      }
      this.ShowAdd = false
    },

    async checkIsAdmin() {
      let res = await axios.get("check-for-admin")
      this.isAdmin = res.data.res
    },

    processHtml(text) {
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'text/html');
      const images = document.querySelectorAll('.description p img');

      images.forEach(img => {
        img.style.maxWidth = '100%'
        img.style.borderRadius = '10px'
        img.style.marginBottom = '20px'
      });

      const regex = /\\n|\\r\\n|\\n\\r|\\r/g;

      // doc.body.innerHTML = text.replace(regex, '<br>');

      return doc.body.innerHTML.replaceAll(regex, '<br>');
    },

    async deleteAnswer(id, index) {
      try {
        await axios.delete('/delete-ans', {
          params: {
            id: id,
            isQ: 'true',
          }
        });
        this.answers.splice(index, 1);
      } catch (error) {
        console.error(error)
      }
    },

    async preloader() {
      if (this.questionInfo && this.userCreater) {
        this.isAllLoad = true;
      }
    },

  },
  mounted() {
    this.loadQuestion();
    this.checkUser();
    this.getNowUser();
  },
}

</script>

<template>
  <div v-if='this.questionInfo && this.userCreater'>
    <div class="main-container mb-4" v-if='this.isAllLoad'>
      <div class="content-1">
        <div class="account justify-content-between">
          <a class="creator-info d-flex flex-row align-items-center gap-3" :href="`/Profile/${this.userCreater.id}`">
            <img class="accountIcon" :src="userCreater.avatar" width="70px" alt="">
            <div class="name-ring">
              <div>
                <span class="name">{{ userCreater.username }}</span>
              </div>
            </div>
          </a>
          <div class="action-select" v-if="this.isCheck == 'true' || this.isAdmin == true">
            <div class="dropdown">
              <button class="btn dropdown-toggle border" type="button" data-bs-toggle="dropdown"
                aria-expanded="false">Действие</button>
              <ul class="dropdown-menu">
                <li v-if="this.questionInfo.is_solved == true && this.isCheck == 'true'"><a class="dropdown-item"
                    @click="solveQuestion(false)">Вопрос решён!</a></li>
                <li v-else-if="this.isCheck == 'true'"><a class="dropdown-item" @click="solveQuestion(true)">Вопрос ещё
                    не
                    решён!</a></li>
                <li v-if="this.isCheck == 'true' || this.isAdmin == true"><a class="dropdown-item"
                    :href="`/UpdateQuestion/${this.$route.params.id}`">Редактировать</a></li>
                <li><a class="dropdown-item" href="#" @click="deleteQuestion">Удалить</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="title">
          <h3 v-html="fixN(questionInfo.descriptions)"></h3>
        </div>
        <div class="description">
          <p v-html="processHtml(questionInfo.details)"></p>
        </div>
        <div class="about">
          <p>{{ questionInfo.data }}</p>
        </div>
        <button class="answer-btn answer-a user-select-none">Ответов: {{ answers.length }}</button>
      </div>
      <div v-if="this.loading" class="ans-cont">
        <div class="container mt-5">
          <h4>Ответы:</h4>
        </div>
        <div class="answers-all" v-if="this.answers.length != 0">
          <div class="content-2" v-for="(answer, index) in answers">
            <div class="account">
              <a :href="`/Profile/${answer.user.id}`" class="creator-info d-flex flex-row align-items-center gap-3">
                <img class="accountIcon" :src="answer.user.avatar" width="70px" :alt="answer.user.username">
                <div class="name-ring">
                  <p><span class="name" role="button">{{ answer.user.username }}</span></p>
                </div>
              </a>
            </div>
            <div class="description my-1">
              <span style="word-break: break-all;" v-html="fixN(answer.text)"></span>
            </div>
            <div class="delete-btn" @click='answer.isOpenRemoved = true'
              v-if='(userNow.id == answer.id_u || isAdmin) && this.ShowAdd'>
              <button class="comm-add btgr">X</button>
            </div>
            <div v-if='answer.isOpenRemoved' class='w-100 h-100 d-flex justify-content-center align-items-center'>
              <div class="bg-black"></div>
              <div class="modal-cenel d-flex flex-column align-items-center">
                <img src="../../assets/Lending/bookModal.png" alt="Грусть(">
                <h6>Вы действительно хотите удалить комментарий?</h6>
                <div class="d-flex gap-2">
                  <button @click='deleteAnswer(answer.id, index)'>Да</button>
                  <button class='no-button' @click='answer.isOpenRemoved = false'>Нет</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="content p-2" v-if="this.answers.length == 0">
          <h2 class="d-flex justify-content-center my-5 user-select-none">Будь первым, кто даст ответ на этот вопрос!
          </h2>
        </div>
      </div>
      <div v-else>
        <div class="d-flex justify-content-center" v-if="this.answers.length != 0">
          <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden text-center">Loading...</span>
          </div>
        </div>
      </div>

      <form v-if="this.ShowAdd" class="content-3" @submit.prevent="addComment" id="iii">
        <div class="account">
          <a :href="`/Profile/${this.userNow.id}`" class="creator-info d-flex flex-row align-items-center gap-3">
            <img class="accountIcon" :src="userNow.avatar" width="70px" alt="">
            <div class="name-ring">
              <div>
                <span class="name">{{ userNow.username }}</span>
              </div>
            </div>
          </a>
        </div>
        <div class="mb-3">
          <div class="content-3-without mb-3">
            <textarea v-model="text" @input="symbolsCount" maxlength="2000" class="comm-input border-0"
              placeholder="Оставь свой комментарий:"></textarea>
            <p :class="{ 'red-text': symbCount }">{{ symbols }} / 2000</p>
          </div>
        </div>
        <div class="send-ans d-flex justify-content-end">
          <button type="submit" class="toMain btn btn-primary p-2 fs-5">Отправить!</button>
        </div>
      </form>
    </div>
    <div class="co" v-else>
      <div class="load-item item1"></div>
      <div class="load-item item2"></div>
      <div class="load-item item3"></div>
      <div class="load-item item4"></div>
      <div class="load-item item5"></div>
    </div>
  </div>
  <div v-else class='w-100 h-100 d-flex justify-content-center align-items-center'>
    <div class="bg-black"></div>
    <div class="modal-cenel d-flex flex-column align-items-center">
      <img src="../../assets/Lending/bookModal.png" alt="Грусть(">
      <h6>Данной страницы не существует, либо вопрос был удалён( </h6>
      <button @click='this.$router.push("/Quetions")'>Назад</button>
    </div>
  </div>

</template>

<style scoped>
.no-button {
  background-color: #D20000 !important;
  border-color: #D20000;
}

.modal-cenel {
  opacity: 1 !important;
  position: fixed;
  top: calc(50% - 260px);
  z-index: 52 !important;
  background: rgba(59, 130, 246, 0.65);
  padding: 24px;
  border-radius: 10px;
  color: #fff;
  gap: 20px;
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

.bg-black {
  background: #000;
  opacity: 0.5;
  z-index: 1;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
}

.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;

  height: auto;
}

.ans-cont {
  display: flex;
  flex-direction: column;
  align-items: start;
  width: 1000px;
}

.delete-btn {
  position: absolute;
  right: 10px;
  bottom: 10px
}

.link {
  font-size: 20px;
  color: #3B82F6;
  position: absolute;
  right: 140px;
}

img {
  user-select: none;
  border-radius: 100% !important;
  object-fit: cover !important;
  width: 50px;
  
}


.description span {
  margin-left: 75px;
}

.accountIcon {
  width: 60px;
  height: 60px;
  border-radius: 50px;
  -webkit-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
}

/* CONTENT-1 */

@media (max-width: 768px) {
  .wrapper {
    margin: 10px 0 !important;
  }

  .comment-container {
    margin: 5rem 1.5rem !important;
  }

  .info-block {
    flex-direction: column !important;
    align-items: start !important;
  }

  .word {
    padding: 6px 15px !important;
  }

  .send-btn {
    padding: 10px 10px !important;
    font-size: 20px !important;
  }

  .comment-container {
    margin: 0 !important;
    padding: 20px !important;
  }
}

.content-1 {
  /* background-color: rgb(225, 225, 225); */
  margin-top: 50px;
  width: 1000px;
  height: auto;
  padding: 19px;
  border-radius: 25px;
  -webkit-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);

}

.account {
  display: flex;
  gap: 12px;
  align-items: center;
}

.accountIcon {
  border-radius: 10px;
  -webkit-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
  box-shadow: 4px 1px 8px 2px rgba(34, 60, 80, 0.2);
}

.name {
  font-weight: 700;
  color: #8355E3;
  margin-right: 10px;
}


.name-ring {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.name-ring p {
  margin: 0;
}

.name-ring div {
  display: flex;
}

.more {
  color: #3B82F6;
}



.difficult {
  margin-left: 5px;
  color: #1E7200;
}

.title {
  margin: 0 !important;
  margin-top: 20px !important;

  display: flex;
  justify-content: space-between;
  align-items: center;

  text-align: start;
}

.name {
  transition: all 300ms;
}

img {
  max-width: 300px !important;

}

.imageinp {
  width: 52px !important;
  border-radius: 100%;
}


.answer-btn {
  width: 180px;
  height: 40px;
  background-color: #3B82F6;
  border: none;
  border-radius: 16px;
  color: #fff;

  margin-top: 18px;

  font-size: 20px;

  transition: all 200ms;
}



.about {
  margin-top: 20px;

  display: flex;
  align-items: center;
  gap: 10px;
}

.about p {
  border-right: 2px solid #3B82F6;
  padding-right: 16px;
  color: #3B82F6;
}

.about p:last-child {
  border: none;
}

/* CONTENT-2 */

.content-2 {
  position: relative;
  margin-top: 50px;
  width: 1000px;
  height: auto;

  padding: 19px;

  border: 1px solid #000;
  border-radius: 25px;
}

.difficult-ans {
  margin-left: 5px;
  color: #E65C00;
}

.btn-group {
  display: flex;
  align-items: center;
  gap: 21px;

  justify-content: space-between
}

.btn-group:last-child {
  gap: 0px;
}

.btn-group p {
  margin-bottom: 0;
  font-size: 18px;

}

.like-count {
  color: #299F00;
}

.dislike-count {
  color: #D20000;
}

.like {
  line-height: 21px;
}

.btgr {
  padding: 9px 26px;
  background-color: #f63b3b;
  color: #fff;
  user-select: none;

  border: none;
  border-radius: 16px;
  font-size: 22px;

  transition: all 200ms;
}



.left {
  display: flex;
  gap: 21px;
  align-items: center
}

.bc {
  display: flex;
  align-items: center;
  gap: 10px;
}

.bc button {
  width: 51px;
  height: 51px;

  padding: 0;

}


/* CONTENT-3 */

.content-3 {
  width: 1000px;
  margin-top: 50px;
  margin-bottom: 50px;

}

.content-3-without {
  margin-top: 13px;

  width: 100%;
  height: 250px;

  padding: 19px;

  border: 1px solid #000;
  border-radius: 25px;

  position: relative;
}

.content-3-without p {
  position: absolute;

  bottom: 0;
  right: 10px;

  color: #767676;
}

.container {
  margin-left: 0 !important;
}

.red-text {
  color: #D20000 !important;
}

.comm-input {
  width: 100%;
  height: 190px;

  border: none;
  resize: none;
  outline: none;
}

/* АДАПТИВКА */

@media (hover: hover) {
  .btgr:hover {
    background-color: #20498b
  }

  .answer-btn:hover {
    background-color: #20498b
  }

  .more:hover {
    color: #20498b;
  }

  .name:hover {
    color: #6140a7;
  }

}

@media (min-width: 1000px) {
  .description img {
    width: 700px;
  }
}

@media (max-width: 1000px) {
  .btn-group p {
    font-size: 16px;
  }

  .bc button {
    width: 42px;
    height: 42px;
  }

  .btgr {
    font-size: 16px;
  }

  .comm-input {
    height: 250px;
  }

  .content-3-without {
    height: 310px;
  }
}

@media (max-width: 770px) {
  .left {
    flex-direction: column;
    align-items: start;
    gap: 10px;
  }

  .btn-group {
    align-items: end;
  }

  .comm-input {
    height: 350px;
  }

  .content-3-without {
    height: 410px;
  }


}


@media (max-width: 460px) {
  .answer-btn {
    width: 100%;
  }

  .comm-add {
    width: 100%;
  }
}

@media (max-width: 400px) {
  .about {
    flex-direction: column;
  }

  .about p {
    border-right: none;
    border-bottom: 2px solid #3B82F6;
    padding: 0 0 16px 0;
    margin: 0;

  }
}

@media (min-width: 2300px) {
  .accountIcon {
    width: 80px;
    height: 80px;
  }

  .content-1,
  .content-2,
  .content-3,
  .ans-cont {
    width: 1400px;
  }

  .name {
    font-size: 22px;
  }

  .dropdown-toggle {
    font-size: 22px;
  }

  .dropdown-menu li {
    font-size: 22px
  }

  .title h3 {
    font-size: 36px;
  }

  .description p {
    font-size: 24px
  }

  .about p {
    font-size: 18px;
  }

  .answer-btn {
    width: 220px;
    font-size: 26px;
    height: 50px;
  }

  h4 {
    font-size: 30px
  }

  .description span {
    font-size: 28px;
  }

  textarea {
    font-size: 24px;
  }

  .content-3 p {
    font-size: 24px;
  }

  .toMain {
    font-size: 28px !important;
    width: 230px;
  }

}

@media (min-width: 3100px) {
  .accountIcon {
    width: 100px;
    height: 100px;
  }

  .content-1,
  .content-2,
  .content-3,
  .ans-cont {
    width: 1800px;
  }

  .name {
    font-size: 28px;
  }

  .dropdown-toggle {
    font-size: 28px;
  }

  .dropdown-menu li {
    font-size: 28px
  }

  .title h3 {
    font-size: 46px;
  }

  .description p {
    font-size: 30px
  }

  .about p {
    font-size: 24px;
  }

  .answer-btn {
    width: 280px;
    height: 60px;
    font-size: 32px;
    border-radius: 22px
  }

  h4 {
    font-size: 36px;
  }

  .description span {
    font-size: 34px;
  }

  .comm-add {
    font-size: 28px;
  }

  textarea {
    font-size: 30px;
  }

  .content-3 p {
    font-size: 28px;
  }

  .toMain {
    font-size: 34px !important;
    width: 260px;
    border-radius: 14px
  }
}

@media (min-width: 4600px) {

  .content-1,
  .content-2,
  .content-3,
  .ans-cont {
    width: 2600px;
  }

  .accountIcon {
    width: 140px;
    height: 140px;
  }

  .name {
    font-size: 38px;
  }

  .dropdown-toggle {
    font-size: 42px;
  }

  .dropdown-menu li {
    font-size: 42px
  }

  .title h3 {
    font-size: 64px;
  }

  .description p {
    font-size: 42px
  }

  .about p {
    font-size: 34px;
  }

  .answer-btn {
    width: 360px;
    height: 80px;
    font-size: 42px;
    border-radius: 30px
  }

  h4 {
    font-size: 54px
  }

  .description span {
    font-size: 46px;
  }

  .comm-add {
    font-size: 42px;
  }



  textarea {
    font-size: 42px;
    height: 340px !important;
  }

  .content-3 p {
    font-size: 38px;
  }

  .content-3-without {
    height: 450px !important;
  }

  .toMain {
    width: 340px;
    font-size: 45px !important;
    border-radius: 16px
  }
}

@media (min-width: 6200px) {

  .content-1,
  .content-2,
  .content-3,
  .ans-cont {
    width: 3400px;
    border-radius: 34px
  }

  .content-1 {
    padding: 40px;
  }

  .accountIcon {
    width: 180px;
    height: 180px;
  }

  .name {
    font-size: 54px;
  }

  .dropdown-toggle {
    font-size: 54px;
  }

  .dropdown-menu li {
    font-size: 54px
  }

  .title h3 {
    font-size: 86px;
  }

  .description p {
    font-size: 58px
  }

  .about p {
    font-size: 48px;
  }

  .answer-btn {
    width: 460px;
    height: 110px;
    font-size: 56px;
  }

  h4 {
    font-size: 64px
  }

  .description span {
    font-size: 58px;
    margin-left: 190px;
  }

  .comm-add {
    font-size: 54px;
  }



  textarea {
    font-size: 56px;
    height: 410px !important;
  }

  .content-3 p {
    font-size: 54px;
  }

  .content-3-without {
    height: 550px !important;
    border-radius: 34px;
  }

  .toMain {
    width: 420px;
    font-size: 56px !important;
    border-radius: 16px;

    margin-bottom: 450px;
  }
}
</style>