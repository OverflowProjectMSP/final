<script>
import NewProfileVid from '../Edit/NewProfileVid.vue';
import NewqueVid from '../Edit/NewqueVid.vue';
import VidUserComp from './VidUserComp.vue';
import axios from 'axios';
import NewnavBar from '../ReuseComponets/NewnavBar.vue'

export default {
    components: {
        VidUserComp,
        NewqueVid,
        NewProfileVid,
        NewnavBar,
    },
    data() {
        return {
            questions: [],
            states: [],

            user: {},

            isCreator: false,

            isQ: true,

            isAllLoad: false,
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

            if (this.isQ) {
                this.questions = res.data.all.questions;
            } else {
                this.states = res.data.all.states;
            }

            this.preloader();
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
        },

        async preloader() {
            if (this.questions || this.states && this.user) {
                this.isAllLoad = true;
            }
        },
    },
}

</script>

<template>
<div v-if='this.isAllLoad'>
    <div class="window">
        
        <div class="prof-banner">
            <a v-if="this.isCreator == 'true'" class="set-link"  href="/NewSetting"><img src="../../assets/Profile/sh.svg"
                    alt="Настройки" class="il"></a>

            <div class="prof">
                <img class="ava" :src="user.avatar" alt="">
            </div>
            <div class="main-info">
                <h3>{{user.username}}</h3>
                <h5>Работяга</h5>
                <p>{{user.interestings}} </p>
                <p class="date">19.09.2024</p>
            </div>
        </div>
        <div class="count-all">
            <p>Вопросы: {{user.qcnt}}</p>
            <p>Статьи: {{user.scnt}}</p>
            <p>Ответы: {{user.acnt}}</p>
        </div>
        <div class="links-info">
            <div class="li-block">
                <p v-if='user.discord'>Discord: <span>{{user.discord}}</span></p>
                <p v-if='user.telegram'>Telegram: <span>{{user.telegram}}</span></p>
                <p v-if='user.github'>GitHub: <span>{{user.github}}</span></p>
            </div>
        </div>
        <textarea id="" name="" readonly class="aboutmee" >{{user.about}}</textarea>
        <div class="container d-flex align-items-center flex-column">
            <div class="q-user head-1 mb-3 mt-1 user-select-none">
                <div class="swit d-flex flex-row align-items-center gap-4">
                    <p role="button" class="q" :class="{ 'active-shose': isQ }" @click="allByHe(true)">Вопросы</p>/
                    <p role="button" class="q" :class="{ 'active-shose': !isQ }" @click="allByHe(false)">статьи</p>
                </div>
                <p class="vse" @click="Olezha">пользователя</p>
            </div>
            <div class="vids" v-if='this.isQ && this.questions.length && this.user'>
                <div class="scroll">
                    <div class="con" v-for="item in questions">
                        <a :href="`/QuestionItem/` + item.id">
                            <NewProfileVid :data="item" :user='user' />
                        </a>
                    </div>
                </div>
            </div>
            <div v-if="!this.isQ && this.states.length && this.user">
                <div class="scroll">
                    <div class="con" v-for="item in states">
                        <a :href="`/StateItem/` + item.id">
                            <NewProfileVid :data="item" :user='user' class="NewProf" />
                        </a>
                    </div>
                </div>
            </div>
            <div class="content p-2" v-if="this.states.length == 0 && !this.isQ">
                <h2 class="d-flex justify-content-center my-5 user-select-none">У пользователя нет статей</h2>
            </div>
            <div class="content p-2" v-if="this.questions.length == 0 && this.isQ">
                <h2 class="d-flex justify-content-center my-5 user-select-none">У пользователя нет вопросов</h2>
            </div>
        </div>

        

    </div>
</div>

</template>

<style scoped>

p {
    margin-bottom: 0;
}



.active-shose {
    text-decoration: underline;
    font-weight: 600;
}

.con {
    padding-top: 10px;
}

.window {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: auto;
}


.swit {
    color: #2b2b2b;
}


.head-1 {
    justify-content: space-around;
    align-items: center;
    margin-top: 50px !important;
    font-size: 30px;
}

.q {
    font-size: 30px;
}

.vse {
    font-size: 30px;
}

.container {
    margin-bottom: 50px !important;
}

.prof-banner {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;

    width: 64%;
    height: 400px;
    position: relative;
    
    border-radius: 30px !important;

    background-image: url(../../assets/Profile/profbag.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}


.set-link {
    position: absolute;
    top: 16px;
    right: 16px;
}

.set-link img {
    width: 50px;
    transition: all 200ms;
}

.set-link img:hover {
    transform: rotate(15deg); 
}

.scroll {
    overflow: scroll;
    max-height: 555px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
}

.prof {
    position: relative;
}

.ava {
    width: 160px;
    height: 160px;
    border-radius: 50% !important;
    display: block;
    /* overflow: visible; */
    object-fit: cover;
    position: absolute;
    top: 10px;
    left: 10px;
}

.prof::after{
    display: block;
    content: '';
    width: 180px;
    height: 180px;
    border: 2px dashed #fff;
    border-radius: 50% !important; /* для закругленных углов */ 
    z-index: 30; /* Псевдоэлемент за картинкой */
    animation: rotate-outline 45s linear infinite;
}

@keyframes rotate-outline {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.main-info {
    position: relative;

    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 10px;
    padding: 0 20px;

    width: 70%;
    height: 200px;
    border-radius: 15px;
    background-color: rgba(233, 233, 233, 0.5);
}

.main-info h3 {
    font-size: 34px;
    color: #212121;
    margin-bottom: 0;
}

.main-info h5 {
    margin-bottom: 0;
    font-size: 23px;
    color: #424242;
}

.main-info p {
    color: #212121;
    font-size: 26px;
    font-weight: 500;
    margin-bottom: 0;
    line-height: 42px;
    display: -webkit-box;             /* Используем флексбокс */
            -webkit-box-orient: vertical;      /* Устанавливаем вертикальную ориентацию */
            -webkit-line-clamp: 2;             /* Ограничиваем количество строк */
    overflow: hidden;                  /* Скрываем всё, что выходит за пределы блока */
    max-width: 110vh;                  /* Ширина блока для переноса */
    word-wrap: break-word;             /* Позволяет разрывать слова */
    white-space: normal;  ;  
}

.date {
    position: absolute;
    top: 20px;
    right: 50px;
    font-size: 26px !important;
}

.count-all {
    display: flex;
    gap: 80px;
    margin-top: 50px;
}

.count-all p {
    font-size: 27px;
    font-weight: 500;
    color: #757575;
    margin-bottom: 0;
    padding-right: 80px;
    border-right: 2px solid #757575;
}

.count-all p:last-child {
    padding-right: 0px;
    border: none;
}

.links-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 50px;

    border: 2px solid #757575;
    border-radius: 15px;

    width: 900px;
    height: 240px;
}

.links-info p {
    font-size: 27px;
    font-weight: 500;
    color: #757575;
    text-align: center;
}

.li-block {
    display: flex;
    flex-direction: column;
    align-items: start;
}

.li-block {
    width: 75ch;
    overflow: hidden;
    white-space: nowrap;
    /* V2 */
    /* white-space: wrap; */
    text-overflow: ellipsis;
}

.li-block span {
    color: #000;
}

.aboutmee {
    margin-top: 30px;
    
    width: 900px;
    height: 180px;
    border: 2px solid #757575;
    border-radius: 15px;
    padding: 10px;
    font-size: 20px;

    resize: none; 

    cursor: default;
}

.aboutmee:focus {
    outline: none;
}





@media (max-width: 1400px) {
    .prof-banner {
        width: 70%;
    }
}

@media (max-width: 1200px) {
    .prof-banner img {
        width: 160px;
        height: 160px;
    }

    .set-link {
        top: -40px;
    }

    .set-link img {
        width: 50px;
    }

    .prof-banner {
        gap: 20px;
        width: 70%;
    }

    .main-info {
        height: 200px;
    }

    .main-info h3 {
        font-size: 28px;
    }

    .main-info h5 {
        font-size: 18px;
    }

    .main-info p {
        font-size: 22px;
        line-height: 30px;
    }

    .main-info p {
         -webkit-line-clamp: 3; 
    }

    .date {
        font-size: 20px !important;
    }

    .count-all p {
        font-size: 24px;
    }

    .li-block {
        width: 60ch;
    }

    .li-block p {
        font-size: 24px;
    }

    .links-info {
        width: 90%;
    }

    .aboutmee {
        width: 90%;
    }
}

@media (max-width: 1000px) {
    .prof-banner {
        flex-direction: column;
        padding: 120px 0 0 0;
        width: 100%;
        border-radius: 0 0 50px 50px;
        margin-top: -140px;
        height: 700px;

        gap: 70px;

    }

    .set-link {
        top: 65px;
        right: 30px;
        
    }

    .set-link img {
        width: 50px !important;
    }

    .prof-banner img {
        width: 160px;
        height: 160px;
    }

    .RouterView {
    }

    /*.main-info {
        width: 60%;
        height: auto;
    }

    .main-info h3 {
        font-size: 22px;
    }

    .main-info h5 {
        font-size: 16px;
    }

    .main-info p {
        font-size: 22px;
        line-height: 30px;
    }*/

    .vse {
        margin-left: 10px;
    }
}

@media (max-width: 850px) {
    .count-all {
        gap: 10px;
    }

    .count-all p {
        padding-right: 10px;
        border-right: 2px solid #757575;
    }

    .head-1 {
        margin-left: 10px;
        margin-right: 10px;
    }
}

@media (max-width: 770px) {
    .vse {
        margin-left: 20px;
    }
}

@media (max-width: 730px) {
    .li-block {
        width: 40ch;
    }
}

@media (max-width: 720px) {
    .prof-banner {
        padding-top: 30px;
    }

    .set-link {
        top: 40px;
        right: 30px;
    }
}

@media (max-width: 600px) {
    .main-info {
        width: 96%;
    }

    .q {
        font-size: 20px;
    }

    .vse {
        font-size: 20px;
    }

    .head-1 {
        font-size: 20px;
    }
}

@media (max-width: 500px) {
    .li-block {
        width: 30ch;
    }

    .set-link {
        top: 30px;
        right: 15px;
    }

    .set-link img {
        width: 45px !important;
    }

    .date {
        right: 10px;
        font-size: 15px !important;
    }

    .li-block p {
        font-size: 20px;
    }

    .count-all p {
        font-size: 18px;
    }

    .links-info {
        height: 170px;
    }

    .q {
        font-size: 18px;
    }

    .vse {
        font-size: 18px;
    }

    .head-1 {
        font-size: 18px;
    }
}
    
</style>
