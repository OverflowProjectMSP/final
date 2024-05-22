<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000';

export default {
    data() {
        return {
            posts: [],

            plusImg: 'src/assets/Forum/plus.svg',

            titleLang: ``,
            imageLang: ``,

            isQuestion: false,

            question: [],
            states: [],

            postUsers: [],

            title: ``,
            dificulty: 'false',
        }
    },
    mounted() {
        this.loadForum();
    },
    methods: {
        async loadForum() {
            this.lang();
            this.isQuestion = !this.isQuestion
            let res = await axios.get('/show-forum', {
                params: {
                    tag: this.$route.query.lang,
                }
            });
            if (this.isQuestion) {
                this.posts = res.data.all.questions;
            } else {
                this.posts = res.data.all.states;
            }
            this.loadAnswerUser()
        },

        async filtre() {
            if (this.isQuestion) {
                let res = await axios.get(`/filter-questions`, {
                    params: {
                        title: this.title,
                        tag: this.posts.tag,
                        dificulty: this.dificulty,
                        author: ``,
                    }
                });
                this.posts = res.data.all;
            } else {
                let res = await axios.get(`/filter-states`, {
                    params: {
                        title: this.title,
                        tag: this.posts.tag,
                        author: ``,
                    }
                });
                this.posts = res.data.all;
            }
        },

        async loadAnswerUser() {
            for (let i = 0; i < this.posts.length; i++) {
                let user = await this.loadUsers(this.posts[i]);
                this.postUsers.push(user)
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


        v_For1() {
            for (let i = 0; i < this.postUsers.length; i++) {
                this.posts[i].user = this.postUsers[i];
            }

            if (this.posts[this.answers.length - 1].user.avatar != `` || this.posts.length == 0) {
                this.loading = true;
            } else {
                this.loading = false;
            }
        },

        lang() {
            switch (this.$route.query.lang) {
                case 'go':
                    this.titleLang = 'Golang';
                    this.imageLang = 'golang';
                    break;
                case 'javascript':
                    this.titleLang = 'JavaScript';
                    this.imageLang = 'js';
                    break;
                case 'java':
                    this.titleLang = 'Java';
                    this.imageLang = 'java';
                    break;
                case 'cs':
                    this.titleLang = 'C#';
                    this.imageLang = 'cs';
                    break;
                case 'python':
                    this.titleLang = 'Python';
                    this.imageLang = 'python';
                    break;
                case 'php':
                    this.titleLang = 'PHP';
                    this.imageLang = 'php';
                    break;
                case 'cpp':
                    this.titleLang = 'C++';
                    this.imageLang = 'cpp';
                    break;
                case 'ruby':
                    this.titleLang = 'Ruby';
                    this.imageLang = 'ruby';
                    break;
                case 'kotlin':
                    this.titleLang = 'Kotlin';
                    this.imageLang = 'kotlin';
                    break;
                case 'typescript':
                    this.titleLang = 'TypeScript';
                    this.imageLang = 'ts';
                    break;
                default:
                    this.titleLang = this.$route.query.lang;
                    break;
            }
        }
    }
}
</script>

<template>
    <div class="contant-head mt-3">
        <div class="container-one">
            <div class="name-and-image">
                <img class="forum-image" :src="`src/assets/Forum/${this.imageLang}.jpg`" alt="">
                <p>{{ titleLang }}</p>
            </div>
            <button class="create-post" v-if="this.isQuestion"><img class="plus-icon" :src="plusImg"><a href="/Quetion">
                    Создать вопрос</a></button>
            <button class="create-post" v-else><img class="plus-icon" :src="plusImg"><a href="/NewState">
                    Создать статью</a></button>
        </div>
    </div>
    <div class="contant-post">
        <div class="sort-and-search d-flex flex-row gap-2 align-items-center">
            <div class="sort-inside d-flex flex-row gap-3 align-items-center">
                <div class="cont-search">
                    <img width="30" :src="'src/assets/Forum/search.svg'" alt=""><input class="search" type="search"
                        v-model="title">
                </div>
                <div class="d-flex">
                    <img class="border pe-2 ps-2" src="../../assets/States/image.png" alt="level">
                    <select class="form-select form-1 " v-model="dificulty">
                        <option value="Простой" selected>Лёгкие</option>
                        <option value="Средний">Средние</option>
                        <option value="Сложный">Сложные</option>
                        <option value="false">Без фильтров</option>
                    </select>
                </div>
            </div>
            <button class="btn btn-outline-primary px-4" @click="filtre">Найти</button>
        </div>
        <!-- <div class="hr"></div> -->
        <div class="ancet d-flex mb-3" style="display: flex; gap: 40px;">
            <h5 role="button" class="mb-0" :class="{ 'border-bottom border-2 border-dark fw-semibold': isQuestion }"
                @click="loadForum">Вопросы</h5>
            <h5 role="button" class="mb-0" :class="{ 'border-bottom border-2 border-dark fw-semibold': !isQuestion }"
                @click="loadForum">Статьи</h5>
        </div>

        <div class="post" v-for="post in posts">
            <div class="account">
                <a :href="`/Profile?id=${post.id_u}`">
                    <img class="account-img" :src="post.user.avatar" alt="">{{ post.user.username }}
                </a>
            </div>
            <div class="main-post-and-check">
                <div class="main-post">
                    <h2 class="title">{{ post.title }}</h2>
                    <p class="description">{{ post.descriptions }}</p>
                </div>
                <div class="decided" v-if="post.is_solved">
                    <div class="decid"><img width="60" class="decided-img" :src="'src/assets/decided.svg'"
                            alt="Решён"><span class="hover-hidden">Вопрос решён</span></div>
                </div>
            </div>
            <div class="answer">
                <a :href="`/QuestionItem?id=` + post.id + `&question=${post.question}`"><button><img
                            :src="'src/assets/comments.svg'" alt=""><span>{{ post.answers }}</span>Ответов</button></a>
            </div>
        </div>

    </div>
</template>

<style scoped>
a {
    text-decoration: none !important;
    color: #fff;
    transition: all 300ms;
}

.contant-head {
    margin-left: 30px;
    margin-right: 30px;
}

.container-one {
    display: flex;
    justify-content: space-between;
    align-items: center;

    /* border-bottom: 3px solid#1d1d1d; */

    width: 100%;
    height: 100px;
    margin-bottom: 50px;
    /* background-color: #b0b0b0; */
}

.name-and-image {
    display: flex;
    align-items: end;
    gap: 30px;
}

.name-and-image img {
    width: 70px;
    border-radius: 50px;
}

.name-and-image p {
    color: #1d1d1d;
    font-size: 30px;
    text-decoration: underline;
    margin: 0;
}

.plus-icon {
    width: 25px;
    margin-right: 10px;
}

.create-post {
    display: flex;
    justify-content: center;
    align-items: center;

    border: none;
    width: 240px;
    height: 55px;
    border-radius: 12px;
    background-color: #4200FF;
    color: #fff;

    font-size: 24px;
    font-weight: 500;

    transition: all 100ms;
}

.title {
    /* width: 55ch;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis; */
    margin: 0 !important;
}

.create-post:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.create-post:active {
    background-color: #240088;
}

.sort-and-search {
    width: 100%;
    height: 60px;

    display: flex;

    margin-bottom: 30px;

}

.cont-search {
    height: 30px;
    position: relative;

    display: flex;
    align-items: center;

}


.search {
    width: 350px;
    padding: 0 20px 0 45px;
    height: 40px;

    border: none;

    border: 2px solid #1d1d1d;
    border-radius: 50px
}

.cont-search img {
    position: absolute;
    margin-left: 10px;
}

.hr {
    width: 100%;
    height: 1px;
    background-color: #1d1d1d;
    border: none;

    margin-bottom: 30px;
}

.sort-select {
    width: 150px;
    height: 40px;
}

.contant-post {
    margin-left: 30px;
    margin-right: 30px;

}

.post {
    width: 100%;
    /* border: 2px solid #1d1d1d; */
    border-radius: 20px;

    background-color: #EEF1F4;




    padding: 10px;
    margin-bottom: 25px !important;

    /* background-color: #cdcdcd */
}




.account-img {
    width: 60px;
    height: 60px;
    border-radius: 50px;
    border: 3px solid #1d1d1d;
    background-color: #fff;
}

.account a {
    width: 200px;
    display: flex;
    align-items: end;
    gap: 15px;

    font-size: 20px;
    color: #1d1d1d;
}

.main-post-and-check {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 60px;
}

.main-post {
    margin-top: 20px;
    width: 90%;
    padding: 10px;

    border: 1px solid #1d1d1d;
    border-radius: 10px;

    /* background-color: #fff2dd; */

    /* background-color: #afafaf; */
}

.answer {
    margin-top: 10px;
}

.answer button {

    background-color: #4200FF;
    border-radius: 12px;
    border: none;
    width: 190px;
    height: 55px;

    color: #fff;
    font-size: 20px;

    transition: all 100ms;
}

.answer button:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.answer button:active {
    background-color: #240088;
}

.answer img {
    margin-right: 10px;
    width: 50px;
}

.answer a {
    text-decoration: none;

}


.answer span {
    font-weight: 700
}



.decid {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

.decid .hover-hidden {
    visibility: hidden;
    width: 120px;
    background-color: #4200FF;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: all 100ms;
}

.decid .hover-hidden::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #4200FF transparent transparent transparent;
}

.decid:hover .hover-hidden {
    visibility: visible;
    opacity: 1;
}

@media ((min-width: 100px) and (max-width: 600px)) {
    .title {
        text-align: start;
    }
}

@media (max-width: 700px) {

    .container-one {
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin-bottom: 80px;
    }

    .sort-and-search {
        flex-direction: column !important;
        justify-content: center;
        gap: 10px;

        margin-bottom: 70px;
    }

    .sort-inside {
        flex-direction: column !important;
        align-items: center;
        justify-content: center;
    }

    .sort-inside select {
        width: 100%;
    }

    .sort-inside input {
        width: 100%;
    }
}

@media (max-width: 550px) {
    .description {
        display: block;
        width: -webkit-min-content;
        width: -moz-min-content;
        width: min-content;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: clamp(300px, 100%, 600ch);
    }
}

@media (max-width: 549px) {
    .main-post-and-check {
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: start;

        margin-bottom: 20px;
    }

    .description {
        width: clamp(200px, 100%, 600ch);
    }

    .title {
        font-size: 23px !important;
        text-align: left;
    }
}
</style>