<script>
import Form from "./Form.vue";
import axios from "axios";
import close_img from "@/assets/FAQ/close.svg";

export default {
  components: { Form },
  data() {
    return {
      faqs: [
        {
          question: `Как работает проект UpFollow?`,
          answer: `Если вам что-нибудь не понятно из курса в мшп, либо же вы создаёте свой проект и зашли
                в тупик - UpFollow к вашим услугам! Здесь вы можете найти людей, готовых помочь вам в трудную минуту,
                а если вопрос появится не у вас, то вы всегда можете помочь, ведь вы добрая душа)`,
          isHide: true,
        },
        {
          question: `Что делать, если на почту не пришел код?`,
          answer: `Проверьте папку "Входящие" и "Спам" вашей почты. Если код не найден, попробуйте повторно отправить запрос на получение кода.`,
          isHide: true,
        },
        {
          question: `Как отредактировать свой вопрос на форуме?`,
          answer: `Для редактирования своего сообщения на форуме найдите кнопку "Редактировать" или "Изменить"
                рядом с вашим вопросом. Нажмите на нее, внесите необходимые изменения и сохраните отредактированное сообщение.`,
          isHide: true,
        },
        {
          question: `Как правильно задать вопрос на форуме, чтобы получить быстрый и точный ответ?`,
          answer: `Для того чтобы получить быстрый и точный ответ на форуме, сформулируйте ваш вопрос четко и ясно.
                    Укажите все необходимые детали и контекст, который поможет другим участникам понять суть вопроса и дать вам
                    наиболее подходящий ответ.`,
          isHide: true,
        },
        {
          question: `Как участвовать в обсуждениях и дискуссиях на форуме, соблюдая правила поведения?`,
          answer: `Вступая в обсуждения и дискуссии на форуме, важно соблюдать правила поведения и уважать мнения других
                    участников. Выражайте свое мнение аргументированно, избегайте оскорблений и несоблюдения правил форума.
                    В случае конфликтов, решайте их конструктивным образом или обращайтесь к модераторам.`,
          isHide: true,
        },
      ],
      isHide: true,

      imgClose: close_img,
      Show: true,
    };
  },
  methods: {
    openAnswer(index) {
      let faq = this.faqs[index];
      faq.isHide = !faq.isHide;

      // this.isHide = !this.isHide;
    },
    async loadLogin() {
      let res = await axios.get(`/check-r`);
      this.Show = res.data.all;
      if (this.Show == "true") {
        this.Show = true;
      } else if (this.ShowLogin == "false") {
        this.Show = false;
      }
    },
  },
  mounted() {
    this.loadLogin();
  },
};
</script>

<template>
  <div
    class="faq-container d-flex flex-column align-items-center gap-2 px-4 py-2"
  >
    <h1 class="mb-4 fw-bold">Часто задаваемые вопросы</h1>
    <div
      class="faq d-flex flex-column p-4 mx-5 transition-all"
      v-for="(faq, index) in faqs"
    >
      <div
        class="quest-block d-flex flex-row justify-content-between p-1 gap-2 align-items-center user-select-none"
        @click="openAnswer(index)"
      >
        <span class="fw-bold fs-4">{{ faq.question }}</span>
        <img
          :class="{ 'rotate-left': faq.isHide }"
          class="transition-all"
          :src="imgClose"
          alt="close"
        />
      </div>
      <p class="fs-5 po" :class="{ 'd-none': faq.isHide }">
        {{ faq.answer }}
      </p>
    </div>
    <div class="ques">
      <h2 class="pt-2">Хотите сообщить об ошибке?</h2>
      <a href="/abouterror"><button>Сообщить</button></a>
    </div>
  </div>
  <!-- <Form v-if="this.Show"/> -->
</template>

<style scoped>
.faq p{
  padding-left: 5px;
  padding-rigth: 5px;
  padding-top: 10px;
}
.faq-container {
  margin: 50px 200px 20px 200px;
}

.ques {
  margin-top: 50px;
  display: flex;
  width: 71%;
  justify-content: space-between;
  
}

.ques h2 {
  color: #5b5a5a;
  font-size: 24px;
  user-select: none;
  vertical-align: middle;
}

.ques button {
  color: #fff;
  background-color: #0d6efd;
  border: none;
  border-radius: 15px;
  font-size: 24px;
  font-weight: 500;
  padding: 5px 43px;
  transition: all 0.3s
}

.ques button:hover {
  background-color: #0360eb;
}

.ques button:active {
  background-color: #3e3d3d;
}

.faq {
  width: 75%;
  background-color: #eeebeb;
  border-radius: 20px;
  padding: 20px;
}

.faq .quest-block {
  cursor: pointer;
}

.quest-block img {
  transition: all 500ms;
}

.rotate-left {
  rotate: 45deg;
}

@media (max-width: 1024px) {
  .faq-container {
    margin: 17.5px 10px !important;
  }

  .faq {
    width: 100%;
    padding: 12px !important;
  }

  .quest-block span {
    font-size: 20px !important;
  }

  .faq p {
    font-size: 16px !important;
  }
}

@media (min-width: 1024px) and (max-width: 1650px) {
  .faq-container {
    margin: 50px 110px 20px 150px !important;
  }

  .faq {
    width: 80%;
    padding: 12px !important;
  }
}
</style>
