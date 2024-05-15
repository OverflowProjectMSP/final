<script>
import HeadComp from './HeadComp.vue';
import VidUserComp from './VidUserComp.vue';
import axios from 'axios';

export default {
    components: {
        HeadComp,
        VidUserComp
    },
    data() {
        return {
            quetionsUsers: [
                {
                    discriptions : `Как создать переменную?`,
                    subscribers: "NaN",
                    hours: "NaN",
                    views: "NaN",
                    answers: "NaN",
                    tag: 'Python',
                    complexity: 'Средне',
                    details: "Как создать атомный реактор?",
                    id: "",

                },
                // {
                //     title: `Как созопоодать переменную?`,
                //     subscribers: 50,
                //     hours: 43,
                //     views: 43,
                //     answers: 423,
                //     language: 'C++',
                //     complexity: 'Средне',
                //     id: 53
                // },
                // {
                //     title: `Как создать переменную?`,
                //     subscribers: 45,
                //     hours: 0,
                //     views: 43,
                //     answers: 423,
                //     language: 'Асембелер',
                //     complexity: 'Ебать тяжело',
                //     id: 54
                // },
            ],
            user: {},
        }
    }, 
    // methods: {
    //     async allByHe(){
    //         let res = await axios.get('/show-all-by-user', {
    //             params: {
    //                 id: this.$router.query.id
    //             }
    //         });
    //         this.quetionsUsers = res.data.all;
    //     },
    //     async loadUser() {
    //         let res = await axios.get(`/user-info?id=${this.$router.query.id}`);
    //         this.user = res.data.all;
    //     }
    // },
    // mounted() {
    //     this.allByHe();
    //     this.loadUser();
    //     setInterval(() => {
    //         this.allByHe();
    //         this.loadUser();
    //     }, 100900);
    // },
}

</script>

<template>
    <div class="profile" v-if="user">
        <a href="#/ProfileSettings"><img src="../../assets/Profile/sh.svg" alt="Настройки" class="il"></a>
        <div class="head">

            <div class="circle">
                <img :src="user.avatar"> <!-- :alt="`Аватар пользователя ` + user.username" -->
            </div>

            <p class="nikname t-alig-c">@{{ user.username }}</p>
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
                <div class="about rounded-5">
                    <p v-if="this.user.name"><img src="../../assets/Profile/User.svg" alt="">Привет, я {{ user.name }}</p>
                    <p v-else><img src="../../assets/Profile/User.svg" alt="">Привет, я {{ user.username }}</p>
                    <p v-if="asd"><img src="../../assets/Profile/SVGRepo_iconCarrier.svg" alt="">Я интересуюсь {{ user.lang }}</p>
                    <p><img src="../../assets/Profile/Frame.svg"><span class="fw-bold">Как со мной связаться?</span></p>
                    <ul class="fs-5">
                        <li v-if="user.email">Моя почта: {{ user.email }}</li>
                        <li v-if="user.telegram">Мой telegram: {{ user.telegram }}</li>
                        <li v-if="user.skype">Мой skype: {{ user.skype }}</li>
                        <li v-if="user.discord">Мой discord: {{ user.discord }}</li>
                        <li v-if="user.facebook">Мой facebook: {{ user.facebook }}</li>
                    </ul>
                    <p class="fs-5"><img src="../../assets/Profile/ArrowDown.svg" alt="">{{ user.about }}</p>
                    <p><span class="fw-bold">Мои интересы: </span></p>
                    <ul class="fs-5 interes">
                        <li class="interes" v-if="user.interestings">{{ user.interestings }}</li>
                    </ul>
                </div>
        </div>

    </div>

    <div class="container d-flex">
        <div class="item ">
            <img src="" alt="">
        </div>
        
        
    </div>
    <div class="container d-flex align-items-center flex-column">
        <HeadComp class="mb-3"/>
        <div class="scroll">
        <a :href="`/QuestionItem?id=${this.quetion.id}&question=true`" v-for="quetion in quetionsUsers">
        <VidUserComp  :quetion="quetion"/>
        </a>
        </div>
    </div>
</template>
<style scoped>
@import url('https://fonts.cdnfonts.com/css/rubik');

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
.scroll{
    overflow: scroll;
    height: 555px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
}
.interes {
    word-break: break-word !important;
}

/* профиль с картинкой */
.profile {
    background-image: url(../../assets/background.png);
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

/* аватар + ник */
.circle {
    margin: auto;
    height: 150px;
    width: 150px;
    border-radius: 100%;
    border: 1px solid #000;
}

.nikname {
    color: #000;
    font-size: 38px;
    font-style: normal;
    font-weight: 400;
}


/* табличка */
.table {
    display: flex;
    justify-content: center;
}

.cell {
    padding: 25px;
    border-right: 1px solid #AEB8BC;
    border-bottom: 1px solid #AEB8BC;
    margin-bottom: 30px;
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

/* До линии */
.head-1 {
    padding-bottom: 10px;
    height: 30px;
    display: flex;
    justify-content: space-between;
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

.right-in {
    display: flexbox;
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