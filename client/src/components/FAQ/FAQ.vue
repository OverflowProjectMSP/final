<script>
import Form from './Form.vue';
export default {
    components: { Form },
    data() {
        return {
            faqs: [
                {
                    question: `Как работает проект UpFollow?`,
                    answer: `Если вам что-нибудь не понятно из курса в мшп, либо же вы создаёте свой проект и зашли 
                в тупик - UpFlow к вашим услугам! Здесь вы можете найти людей, готовых помочь вам в трудную минуту, 
                а если вопрос появится не у вас, то вы всегда можете помочь, ведь вы добрая душа)`,
                    isHide: true
                },
                {
                    question: `Что делать, если на ваш вопрос не дали ответ?`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
            ],
            isHide: true,

            imgClose: 'src/assets/FAQ/close.svg',
            Show: "",
        }
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
    }
    }
}
</script>

<template>
    <div class="faq-container d-flex flex-column align-items-center gap-2 px-4 py-2">
        <h1 class="mb-4 fw-bold">Часто задаваемые вопросы</h1>
        <div class="faq d-flex flex-column p-4 mx-5 transition-all"
            v-for="(faq, index) in faqs">
            <div class="quest-block d-flex flex-row justify-content-between p-1 gap-2 align-items-center user-select-none"
                @click="openAnswer(index)">
                <span class="fw-bold fs-3">{{ faq.question }}</span>
                <img :class="{ 'rotate-left': faq.isHide }" class="transition-all" :src="imgClose" alt="close">
            </div>
            <p class="fs-4" :class="{ 'd-none': faq.isHide }">
                {{ faq.answer }}
            </p>
        </div>
    </div>
    <Form  v-if="this.Show" />
</template>

<style scoped>
.faq-container {
    margin: 50px 200px 20px 200px;
}
.faq {
    width: 75%;
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