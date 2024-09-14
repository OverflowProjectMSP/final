<script>
import VidUserComp from './VidUserComp.vue';
import axios from 'axios';

export default {
    components: {
        VidUserComp
    },
    data() {
        return {
            questions: [],
            states: [],

            user: {},

            isCreator: false,

            isQ: true
        }
    },
    mounted() {
        this.allByHe();
        this.loadUser();
        this.check();
    },
    methods: {
        async allByHe(dick) {
            this.isQ = dick;
            let res = await axios.get('/show-all-by-user', {
                params: {
                    id: this.$route.params.id
                }
            });
            
            if(this.isQ) {
                this.questions = res.data.all.questions;
            } else {
                this.states = res.data.all.states;
            }
        },
        async loadUser() {
            let res = await axios.get(`/user-info`, {
                params: {
                    id: this.$route.params.id
                }
            });
            this.user = res.data.all;
        },
        async check() {
            let res = await axios.get('/check', {
                params: {
                    id: this.$route.params.id
                }
            });
            this.isCreator = res.data.isEdit;
        }
    },
}

</script>

<template>
    <div class="profile">
        <a v-if="this.isCreator == 'true'" href="/ProfileSettings"><img src="../../assets/Profile/sh.svg" 
            alt="Настройки" class="il"></a>
            <div class="head object-fit-cover">
                <div class="circle">
                    <img :src="user.avatar" class='object-fit-cover'
            </div>
            <p class="nikname t-alig-c">@{{ user.username }}</p>
            <div class="loc-tel">
                <p class="location">{{ user.city }}</p>
                <p class="telephone">{{ user.phonenumber }}</p>
            </div>
            <div class="table t-alig-c">
                <div class="cell">
                    <p class="num">{{ user.qcnt }}</p>
                    <p class="info">Вопросов</p>
                    </div>
                <div class="cell">
                    <p class="num">{{ user.scnt }}</p>
                    <p class="info">Статей</p>
                    </div>
                    <div class="cell dis-r">
                        <p class="num">{{ user.acnt }}</p>
                    <p class="info">Ответов</p>
                </div>
            </div>
            <p class="text-secondary il-2">Дата регистрации: {{ user.data_c }}</p>
            <div class="about rounded-5">
                <p v-if="this.user.name == ''"><img src="../../assets/Profile/User.svg" alt="">Привет, я {{ user.username }} </p>
                <p v-else><img src="../../assets/Profile/User.svg" alt="">Привет, я {{ user.name }}</p>
                <!-- <p v-if="asd"><img src="../../assets/Profile/SVGRepo_iconCarrier.svg" alt="">Я интересуюсь {{ user.lang }}</p> -->
                <p v-if="this.user.telegram != '' || this.user.skype != '' || this.user.discord != '' || this.user.facebook != ''"><img src="../../assets/Profile/Frame.svg"><span class="fw-bold">Как со мной связаться?</span></p>
                <ul class="fs-5">
                    <li v-if="user.telegram">Мой Telegram: {{ user.telegram }}</li>
                    <li v-if="user.skype">Мой Skype: {{ user.skype }}</li>
                    <li v-if="user.discord">Мой Discord: {{ user.discord }}</li>
                    <li v-if="user.facebook">Мой Facebook: {{ user.facebook }}</li>
                    <li v-if="user.github">Мой GitHub: <a class='text-info' :href='user.github' target="_blank">github.com</a></li>
                </ul>
                <p v-if="this.user.about != ''" class="fs-5 abobus"><img src="../../assets/Profile/ArrowDown.svg" alt="">{{ user.about }}</p>
                <p v-if="this.user.interesting != ''"><span  v-if="this.user.interestings != ''" class="fw-bold">Мои интересы: </span></p>
                <p class="fs-5 interes" v-if="this.user.interestings != ''">{{ user.interestings }}</p>
            </div>
        </div> 
    </div>

    <div class="container d-flex align-items-center flex-column">
        <div class="q-user head-1 mb-3 mt-1 user-select-none">
            <div class=" d-flex flex-row align-items-center gap-4">
                <p role="button" class="q" :class="{'active-shose': isQ}" @click="allByHe(true)">Вопросы</p>/
                <p role="button" class="q" :class="{'active-shose': !isQ}" @click="allByHe(false)">статьи</p>
            </div>
            <p class="vse" @click="Olezha">пользователя</p>
            </div>
        <div v-if='this.isQ && this.questions.length != 0'>
            <div class="scroll">
                <a :href="`/QuestionItem/${question.id}`" v-for="question in questions">
                    <VidUserComp :item="question" :type="question"/> 
                </a>
            </div>
        </div>
        <div v-if="!this.isQ && this.states.length != 0">
            <div class="scroll"> 
                <a :href="`/StateItem/${state.id}`" v-for="state in states">
                    <VidUserComp :item="state" :type="state"/>
                </a>
            </div>
        </div>
        <div class="content p-2" v-if="this.states.length == 0 && !this.isQ">
            <h2 class="d-flex justify-content-center my-5 user-select-none">У пользователя нет статей</h2>
        </div>
        <div class="content p-2" v-if="this.questions.length == 0 && this.isQ">
            <h2 class="d-flex justify-content-center my-5 user-select-none">У пользователя нет вопросов</h2>
        </div>
    </div>
</template>
<style scoped>
@import url('https://fonts.cdnfonts.com/css/rubik');

.active-shose {
    text-decoration: underline;
    font-weight: 600;
}

/* общее */
:root {
    --size-20: 20px;
    --size-26: 26px;
    --size-22: 22px;
    --size-18: 18px;
}

html {
    margin: 0;
    background-color: #EEF1F4;
}

main {
    margin: 10px
}

body {
    font-family: Rubik !important;
}

/*популярные классы */
.t-alig-c {
    text-align: center;
}

.scroll {
    overflow: scroll;
    max-height: 555px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
}

.interes {
    word-break: break-word !important;
}

/* профиль с картинкой */
.profile {
    background-image: url(../../assets/Profile/background.png);
    background-color: #ffffff;
    background-repeat: no-repeat;
    background-size: 1920px;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    padding: 10px;
    margin-bottom: 10px;
}

/* шесетренка */
.il {
    position: absolute;
    right: 30px;
    height: 25px;
    width: 25px;
    cursor: pointer;
}
.il-2 {
    /* position: absolute; */
    text-align: center;
    /* bottom: 10px; */
    font-size: 12px !important;
}

/* аватар + ник */
.circle {
    object-fit: cover !important;
    margin: auto;
    height: 180px;
    width: 180px;
    border-radius: 100%;
    border: 1px solid #000;
}

.circle img {
    height: 180px;
    width: 180px;
    border-radius: 100%;
}

.nikname {
    color: #000;
    font-size: 38px;
    font-style: normal;
    font-weight: 400;
}


.loc-tel {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.loc-tel p {
    margin: 0;
    font-size: 24px;
}

.telephone {
    margin-bottom: 40px !important;
}

/* табличка */
.table {
    display: flex;
    justify-content: center;
    margin-bottom: 0 !important;
}

.cell {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 25px;
    border-right: 1px solid #AEB8BC;
    border-bottom: 1px solid #AEB8BC;
    margin-bottom: 1rem;
    width: 33.33%;
}

.dis-r {
    border-right: none;
}

.num {
    font-size: 34px;
    margin: 0;
}

.info {
    font-size: 34px;
}

/* Описание */
.about {
    padding: 10px 60px;
    background: #FFF;
    box-shadow: 0px 4px 40px 5px rgba(45, 114, 217, 0.60);
    margin-bottom: 20px;
    max-width: 650px;
}

.about p {
    font-size: 26px;
    margin: 5px 0px;
    word-break: break-all !important;
}

.about img {
    width: 28px;
    height: 18px;
    vertical-align: middle;
    margin-right: 4px;
}

p .u {
    width: 38px;
    height: 22px;
}

/* Вопросы пользователя */
.quest {
    background-color: white;
    border-radius: 8px;
    padding: 10px;
    margin: 0 20%;
}

.q-user {
    display: flex;
    align-items: center;
    justify-content: center
}

/* До линии */
.head-1 {
    padding-bottom: 10px;
    height: 30px;
    display: flex;
    gap: 10px;
    margin: -15px;
    padding: 0 20px;
}

.vse {
    margin: 0;
    color: #2D72D9;
    font-size: 24px;
    text-decoration: none;
}

.q {
    font-size: 24px;
    margin: 0;
}

/* после линии */
.imp-1 {
    padding: 10px;
    padding-top: 15px;
    border-top: 1px solid #000000;
}

/* виджет с вопросами */
.vid {
    background-color: #EEF1F4;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    border-radius: 15px;
    margin-bottom: 15px;
}

/* общее расположение элементов */

.right {
    display: flex;
    align-items: center;
}


.right p {
    margin: 0;
    margin: 0;
    color: #AEB8BC;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

/* расцветовка */
.light {
    color: #488D57
}

.middle {
    color: #D8A326;
}

.hard {
    color: #D9382E;
}

/* левая чать виджета */

/* Верх */
.top-1 {
    display: flex;
    gap: 20px;
    margin-bottom: 10px;
}

.top-1 p {
    margin: 0;
}

.t {
    vertical-align: middle;
    width: 10px;
    height: 10px;
}

/* серидина */
.mid-1 {
    font-size: 28px;
}

.mid-1 p {
    margin: 0;
}

/* низ */
.bottom-1 {
    display: flex;
    font-size: 15px;
    color: #AEB8BC;
}

.el {
    border-right: 1px solid #AEB8BC;
    padding: 7px;
}

.el-d {
    border-right: none;
    padding: 7px;
}

.-d {
    border-right: none;
}

.el p {
    margin: 0;
}


/* анимация */





/* Адаптивка */
@media(max-width: 1200px) {
    .nikname {
        font-size: 30px;
    }

    .num {
        font-size: var(--size-26);
    }

    .info {
        font-size: var(--size-26);
    }

    .about p {
        font-size: var(--size-22);
    }

    .vse {
        font-size: var(--size-20);
    }

    .q {
        font-size: var(--size-20);
    }
}

@media(max-width: 992px) {
    .nikname {
        font-size: 28px;
    }

    .num {
        font-size: var(--size-22);
    }

    .info {
        font-size: var(--size-22);
    }

    .about p {
        font-size: var(--size-18);
    }

    .vse {
        font-size: var(--size-18);
    }

    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: 24px;
    }

}

@media(max-width: 576px) {
    .nikname {
        font-size: var(--size-26);
    }

    .q-user {
        flex-wrap: wrap;
        padding-bottom: 65px;
    }

    .num {
        font-size: var(--size-22);
    }

    .info {
        font-size: var(--size-22);
    }

    .about {
        padding: 10px 20px !important;
    }


    .interes {
        font-size: 16px;
    }

    .about p {
        font-size: var(--size-18);
    }

    .vse {
        font-size: var(--size-18);
    }

    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: var(--size-20);
    }

    .bottom-1 {
        font-size: 13px;
    }

    .right p {
        font-size: var(--size-18);
    }

    .imp-1 {
        padding-top: 13px;
    }
}

@media(max-width: 768px) {
    .nikname {
        font-size: 28px;
    }
    
    .num {
        font-size: var(--size-22);
    }

    .info {
        font-size: var(--size-22);
    }

    .about p {
        font-size: var(--size-18);
    }

    .vse {
        font-size: var(--size-18);
    }

    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: var(--size-20);
    }

    .bottom-1 {
        font-size: 13px;
    }

    .right p {
        font-size: var(--size-18);
    }

    .imp-1 {
        padding-top: 13px;
    }
}

</style>
