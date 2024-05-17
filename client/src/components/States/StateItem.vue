<script>
import axios, { all } from 'axios';

export default {
    data() {
        return {
            question: { //структура получения всех данных с сервера(УСТАРЕВШАЯ!!!);
                id: 123,
                accountInfo: {
                    accountIcon: 'person.svg',
                    accountName: 'Nick Endgy',
                },
                questionInfo: {
                    title: 'Как сделать регистрацию с использованием только JavaScript?',
                    description: `Подскажите, пожалуйста, как сделать регистрацию пользователя на сайте? Сайт у меня на node.js. Я первый раз такую форму делаю и не знаю какой путь выбрать. Какой вариант лучше? Просто к кнопке "зарегистрироваться" подвязать эвент и в нем делать функцию? Или как-то использовать method="post" у формы? 
                                <br>UPD:А как fetch() использовать? Я написал такой код, а что дальше с ним сделать - не знаю. Как я понял, на сервер запрос отправлен, а именно на сервер были отправлены данные формы. А что дальше с ними сделать? Обрабатывать форму в этом же коде? Моя цель - отправить запрос в базу данных sql, в которую внесется новый пользователь`,
                    level: `Лёгкий`,
                    imageInQuetion: 'test',
                    answer: 28,
                    views: 473,
                    data: `05.01.2024 12:31`,
                    Decided: true,
                },
                answers: [
                    {
                        answerUserInfo: {
                            accountIcon: 'ava.png',
                            accountName: 'JavaScriptPRO',
                            rang: `Решала`,
                        },
                        answerInfo: {
                            text: `123123123, а что дальше с ним сделать - не знаю. Как я понял, на сервер запрос отправлен, а именно на сервер были отправлены данные формы. А что дальше с ними сделать? Обрабатывать форму в этом же коде? Моя цель - отправить запрос в базу данных sql, в которую внесется новый пользователь`,
                            comment: 52,
                            likes: 52,
                            dislike: 36,
                        },
                    },
                ],
            },

            user: {},

            states: {}, //главная возня
            answers: [],
            commentUser: [],
            answerUser: [],
            userCreater: {},

            text: ``,
            
            id_: null,

            symbols: 0,
            symbCount: false,
            isBold: false,
            isItalic: false,

            count: 0,
            countmin: 0,

            isCheck: null,
            ava: ``,

            name: ``,


            avaComment: ``,
        }
    },

    mounted() {
        this.loadState();
        this.loadAnswerUser();
        this.checkUser();
        this.loadUserInfo();
    },
    
    methods: {
        async loadState() {
            let responce = await axios.get(`/show-one`, {
                params: {
                    id: this.$route.query.id,
                    q: false,
                }
            });
            this.states = responce.data.all.states;
            this.answers = responce.data.all.answers;
        },

        async loadUserInfo() {
            let res = await axios.get('/user', {
                params: {
                    id: this.states.id_u,
                }
            });
            this.user = res.data.all;
        },

        counterPlus(index) {
            if (this.count == 0 && this.countmin == 0) {
                this.question.answers[index].answerInfo.likes++;
                this.count++;
            } else if (this.count == 0 && this.countmin == 1) {
                return;
            } else if (this.count == 1) {
                this.question.answers[index].answerInfo.likes--;
                this.count--;
            }  
        },

        counterMinus(index) {
            if (this.countmin == 0 && this.countmin == 0) {
                this.question.answers[index].answerInfo.dislike++;
                this.countmin++;
            } else if (this.count == 1 && this.countmin == 0) {
                return;
            } else if (this.countmin == 1) {
                this.question.answers[index].answerInfo.dislike--;
                this.countmin--;
            }
        },

        breakLines(text) {
            return text.replace(/\n/g, "<br>");
        },

        symbolsCount() {
            this.question.symbols = this.question.text.length;
            if (this.question.symbols >= 2000) {
                this.question.symbCount = true;
            } else {
                this.question.symbCount = false;
            }
        },

        loadAnswerUser() {
            this.userCreater = this.loadUsers(this.states.id_u);

            this.answers.forEach((item) => {
                let user = this.loadUsers(item);
                this.answerUser.push(user)
            });
        },

        async loadUsers(item) {
            let res = await axios.get('/user-not-all', {
                params: {
                    id: item.id_user,
                }
            });
            return res.data.all;
        },

        async addComment() {
            await axios.post(`/answers`, {
                    id: this.$route.query.id,
                    q: false,
                    text: this.text,
                },
            );
            this.text = ``;
            this.loadState();
        },
        async deleteState() {
            await axios.delete('/delete', {
                params:{
                    id: this.$route.query.id,
                    q: 'false',
                }
            });
        },

        // async loadAvatar() {
        //     let res = await axios.get('/avatarka', {
        //         params: {
        //             id: this.$route.query.id,
        //         }
        //     });
        //     this.ava = res.data.link;
        // },

        async checkUser() {
            let res = await axios.get('/check', {
                params: {
                    id: this.states.id_u,
                }
            });
            this.isCheck = Boolean(res.data.isEdit);
        },

        // async loadAvatars() {
        //     let trertrestrestrestrestrestrestrestrestrestres = await axios.hui('beckend-vojna-ta-eche');
        // }
    },
}

</script>

<template>
    <div class="container mb-4">
        <div class="content-1">
            <div class="account justify-content-between">
                <div class="creator-info d-flex flex-row align-items-center gap-3">
                    <img class="accountIcon" :src="userCreater.avatar" :alt="userCreater.username" width="70px">
                    <div class="name-ring">
                        <div>
                            <a href="#!"><span class="name">{{ userCreater.username }}</span></a>
                        </div>
                    </div>
                </div>
                <div class="action-select" v-if="isCheck">
                    <div class="dropdown">
                        <button class="btn dropdown-toggle border">Дейсвие</button>
                        <ul class="dropdown-menu 52-da-sdravstvuet-sankt-piterburg-i-etot-gorod-nash-ya-kazhdiy">
                            <li><a class="dropdown-item" href="#/Quetion">Редактировать</a></li>
                            <li><a class="dropdown-item" href="#" @click="deleteState">Удалить</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="title">
                <h3>{{ states.discriptions }}</h3>
            </div>
            <div class="description">
                <p v-html="breakLines(states.details)"></p>
                <!-- <img class="user-select-none" :src="states.imageInQuetion" 
                    v-if="states.image"> -->
            </div>
            <div class="about">
                <p>{{ states.data }}</p>
            </div>
        </div>
        
        <div class="content-3">
            <div class="account" v-for="user in answerUser">
                <img class="accountIcon" :src="user.avatar" width="70px" alt="">
                <div class="name-ring">
                    <div>
                        <a href="#!"><span class="name">{{ user.username }}</span></a>
                    </div>
                </div>
            </div>
            <div class="content-3-without mb-3">
                <textarea v-model="text" @input="symbolsCount" maxlength="2000" class="comm-input border-0"
                placeholder="Оставь свой комментарий:"></textarea>
                <p :class="{ 'red-text': symbCount }">{{ symbols }} / 2000</p>
            </div>
            <div class="send-ans d-flex justify-content-end">
                <button @click="addComment()" type="submit" class="toMain btgr p-4 fs-4">Отправить!</button>
            </div>
        </div>
        
        <h3 class="answer-a user-select-none mb-0">Комментарии: </h3>
    
        <div class="content-2 mt-2" v-for="answer in answers" v-if="this.answers.length != 0">
            <div class="account" v-for="commUser in answerUser">
                <img class="accountIcon" :src="'src/assets/' + commUser.avatar" width="70px" alt="">
                <div class="name-ring">
                    <p><span class="name" role="button">{{ commUser.username }}</span></p>
                </div>
            </div>
            <div class="description mt-3">
                <p v-html="breakLines(answer.text)"></p>
            </div>
            <div class="btn-group">
                <div class="left">
                    <button class="comm-add btgr">Добавить комментарий</button>
                    <!-- <div class="like-bc bc">
                        <button @click="counterPlus(index)" class="like btgr"><img :src="'src/assets/Like.svg'" alt=""></button>
                        <p class="like-count user-select-none">{{ answer.likes }}</p>
                    </div>
                    <div class="dislike-bc bc">
                        <button @click="counterMinus(index)" class="dislike btgr"><img :src="'src/assets/Dislike.svg'" alt=""></button>
                        <p class="dislike-count user-select-none">{{ answer.dislike }}</p>
                    </div> -->
                </div>
                <div class="right">
                    <a href="/"><button class="toMain btgr">На главную</button></a>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
img {
    user-select: none;
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
    width: 100%;
    height: auto;

    padding: 19px;

    border: 1px solid #000;
    border-radius: 25px;
}

.account {
    display: flex;
    gap: 12px;
    align-items: center;
}

.accountIcon {
    border-radius: 50px;
    border: 2px solid #1d1d1d;
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

.description img {
    width: 100%;
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
    margin-top: 50px;
    width: 100%;
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
    background-color: #3B82F6;
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
    margin-top: 50px;
}

.content-3-without {
    margin-top: 13px;

    width: 100%;
    /* height: 100px !important; */

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

.red-text {
    color: #D20000 !important;
}

.comm-input {
    width: 100%;
    height: 100px !important;

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
}


@media (max-width: 460px) {
    .answer-btn {
        width: 100%;
    }

    .comm-add {
        width: 170%;
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
</style>