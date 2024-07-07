<script>
import axios, { all } from 'axios';

export default {
    data() {
        return {
        

            user: {},

            states: {}, //главная возня
            answers: [],
            commentUser: [],
            answerUser: [],
            userCreater: {},
            userNow: {},

            text: ``,

            symbols: 0,
            symbCount: false,

            isCheck: false,

            avaComment: ``,

            loading: false,
            a: '',
            ShowAdd: true
        }
    },

    mounted() {
        this.loadState();
        this.getNowUser();
        this.checkUser();
    },
    
    methods: {
        async loadState() {
            let responce = await axios.get(`/show-one`, {
                params: {
                    id: this.$route.query.id,
                    q: false,
                }
            });
            const regex = /\\n|\\r\\n|\\n\\r|\\r/g;

            this.states = responce.data.all.state;
            this.answers = responce.data.all.answers;
            this.states.details = this.states.details.replaceAll(regex, '<br>')
            this.loadAnswerUser();
            
        },

        async loadAnswerUser() {
            this.userCreater = await this.loadUsers(this.states);
            this.CheckUserIsEdit()
            if (this.answers.length!=0){
                for(let i = 0; i < this.answers.length; i++) {
                    let user = await this.loadUsers(this.answers[i]);
                    this.commentUser.push(user)
                };
                this.v_For1();
            }
        },

        async loadUsers(item) {
            let res = await axios.get('/user-not-all', {
                params: {
                    id: item.id_u,
                }
            });
            console.log(item)
            return res.data.all;
        },

        async getNowUser() {
            let res = await axios.get('/session');
            this.loadNowUser(res.data.id);
        },

        symbolsCount() {
            this.question.symbols = this.question.text.length;
            if (this.question.symbols >= 2000) {
                this.question.symbCount = true;
            } else {
                this.question.symbCount = false;
            }
        },

        async addComment() {
            if (this.text != ""){
                await axios.post(`/answers`, {
                    id: this.$route.query.id,
                    q: 'false',
                    text: this.text,
                });
                this.answers.push({
                    id_u: this.userNow.id,
                    text: this.text,
                    user: this.userNow
                });
                this.text = ``;
                this.v_For1();
            }
        },
        async deleteState() {
            await axios.delete('/delete', {
                params:{
                    id: this.$route.query.id,
                    q: 'false',
                }
            });
            this.$router.push('/States');
        },

        async CheckUserIsEdit() {
            let res = await axios.get('/check', {
                params: {
                    id: this.userCreater.id,
                }
            });

            this.isCheck = res.data.isEdit
        },

        v_For1() {
            if (this.answers.length != 0){
                for (let i = 0; i < this.commentUser.length; i++) {
                    this.answers[i].user = this.commentUser[i];
                    const regex = /\\n|\\r\\n|\\n\\r|\\r/g;
                    let e = this.answers[i].text.replaceAll(regex, '<br>')
                    this.answers[i].text = e
                    console.log(this.answers)
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
        async checkUser() {
            let res = await axios.get(`/check-r`);
            this.ShowAdd = res.data.all;
            if (this.ShowAdd == "true") {
                this.ShowAdd = true
                return
                
            }
            this.ShowAdd = false
        },

        fixN(text) {
            return text
            // }
        },
    },
}

</script>

<template>
    <div class="container mb-4">
        <div class="content-1">
            <div class="account justify-content-between">
                <a class="creator-info d-flex flex-row align-items-center gap-3" :href="`/Profile?id=${this.userCreater.id}`">
                    <img class="accountIcon" :src="userCreater.avatar" :alt="userCreater.username" width="70px">
                    <div class="name-ring">
                        <div>
                            <a :href="`/Profile?id=${this.userCreater.id}`"><span class="name">{{ userCreater.username }}</span></a>
                        </div>
                    </div>
                </a>
                <div class="action-select" v-if="this.isCheck == 'true'">
                    <div class="dropdown">
                        <button class="btn dropdown-toggle border" type="button" data-bs-toggle="dropdown" aria-expanded="false">Дейсвие</button>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" :href="`/UpdateState?id=${this.$route.query.id}&q=false`">Редактировать</a></li>
                            <li><a class="dropdown-item" href="#" @click="deleteState">Удалить</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="title">
                <h3 v-html="fixN(this.states.descriptions)"></h3>
            </div>
            <div class="description uy">
                <p v-html="fixN(this.states.details)"></p>
            </div>
            <div class="about">
                <p v-html="fixN(this.states.data)"></p>
            </div>
        </div>
        
        <form @submit.prevent="addComment" class="content-3" v-if="this.ShowAdd">
            <div class="account">
                 <a :href="`/Profile?id=${this.userNow.id}`" class="creator-info d-flex flex-row align-items-center gap-3">
                    <img class="accountIcon" :src="userNow.avatar" width="70px" alt="">
                    <div class="name-ring">
                        <div>
                           <span class="name">{{ userNow.username }}</span>
                        </div>
                    </div>
                    </a>
            </div>
            <div class="content-3-without mb-3">
                <textarea v-model="text" @input="symbolsCount" maxlength="2000" class="comm-input border-0"
                placeholder="Оставь свой комментарий:"></textarea>
                <p :class="{ 'red-text': symbCount }">{{ symbols }} / 2000</p>
            </div>
            <div class="send-ans d-flex justify-content-end">
                <button type="submit" class="toMain btn btn-primary p-2 fs-5">Отправить!</button>
                </div>
                </form>
            <div class="container mt-3" v-if="this.answers.length != 0"><h4>Комментарии:</h4></div>
        <div v-if="!this.loading && this.answers.length != 0">
            <h3 class="answer-a user-select-none mb-0">Комментарии: </h3>
            <div class="d-flex justify-content-center">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden text-center z-10">Loading...</span>
                </div>
            </div>
        </div>

        <div v-if="this.loading && this.answers.length != 0">
            <div class="content-2 mt-2" v-for="answer in answers">
                <div v-if="this.answers.length != 0">
                    <div class="account">
                        <a :href="`/Profile?id=${answer.user.id}`" class="creator-info d-flex flex-row align-items-center gap-3">
                            <img class="accountIcon" :src="answer.user.avatar" width="70px" :alt="answer.user.username">
                            <div class="name-ring">
                                <span class="name" role="button">{{ answer.user.username }}</span>
                            </div>
                        </a>
                    </div>
                    <div class="description-text mt-1">
                        <span style="word-break: break-all;" v-html="fixN(answer.text)"></span>
                    </div>
                </div>
            </div>
        </div>
        <div class="content p-2" v-if="this.answers.length == 0">
            <h2 class="d-flex justify-content-center my-5 user-select-none">Будь первым, кто оставит комментарий под этой статьей!</h2>
        </div>
    </div>
</template>

<style scoped>
.toMain{
    border-radius: 10px;
}
.uy{
    word-break: break-all !important;
}

.accountIcon {
    width: 60px;
    height: 60px;
    border-radius: 50px;
    border: 3px solid #1d1d1d;
}

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
/* 
.accountIcon {
    border-radius: 50px !important;
    border: 2px solid #1d1d1d;
} */

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

.description-text {
    margin-left: 72px !important;
    word-break: break-all;
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
