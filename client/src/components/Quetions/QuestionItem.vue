<script>

import UpdateQuestion from './UpdateQuestion.vue';

import axios from 'axios';

export default {
    components: { UpdateQuestion },
    data() {
        return {
            questionInfo: {}, //главная возня
            answers: [
            {
                data:"Sat, 11 May 2024 21:55:14 GMT",
                id:"9b129553-7f6e-4e35-aa66-3cf01a216043",
                id_q:"9b129553-7f6e-4e35-aa66-3cf01a216043",
                id_u:"f527d19a-f56b-4614-bab6-63800ed79825",
                text:"Абдурохман",
                user:{
                avatar:"http://127.0.0.1:5000/avatar/a_f527d19a-f56b-4614-bab6-63800ed79825.gif",
                id:"f527d19a-f56b-4614-bab6-63800ed79825",
                username:"febolo"
                }}
            ],
            answerUser: [],
            userCreater: {},
            userNow: {},
            text: ``,

            user: {},

            text: '',
            symbols: 0,
            symbCount: false,
            isBold: false,
            isItalic: false,

            count: 0,
            countmin: 0,

            isCheck: null,

            loading: true,

            updQ: false,
        }
    },

    // methods: {
    //     async loadQuestion() {
    //         let responce = await axios.get(`/show-one`, {
    //             params: {
    //                 id: this.$route.query.id,
    //                 q: true,
    //             }
    //         });
    //         this.questionInfo = responce.data.all.question;
    //         this.answers = responce.data.all.answers;
    //         this.loadAnswerUser();
    //     },

    //     async loadAnswerUser() {
    //         this.userCreater = await this.loadUsers(this.questionInfo);
    //         this.checkUser();
    //         for (let i = 0; i < this.answers.length; i++) {
    //             let user = await this.loadUsers(this.answers[i]);
    //             this.answerUser.push(user)
    //         };
    //         this.v_For1();
    //     },
        

    //     async loadUsers(item) {
    //         let res = await axios.get('/user-not-all', {
    //             params: {
    //                 id: item.id_u,
    //             }
    //         });
    //         return res.data.all;
    //     },

    //     symbolsCount() {
    //         this.symbols = this.text.length;
    //         if (this.symbols >= 2000) {
    //             this.symbCount = true;
    //         } else {
    //             this.symbCount = false;
    //         }
    //     },

    //     async addComment() {
    //         await axios.post(`/answers`, {
    //             id: this.$route.query.id,
    //             q: 'true',
    //             text: this.text,
    //         });
    //         this.text = ``;
    //     },
    //     async deleteQuestion() {
    //         await axios.delete('/delete', {
    //             params: {
    //                 id: this.$route.query.id,
    //                 q: true,
    //             }
    //         });
    //         this.$router.push(`/Quetions`)
    //     },
    //     async checkUser() {
    //         let res = await axios.get('/check', {
    //             params: {
    //                 id: this.userCreater.id
    //             }
    //         });
    //         this.isCheck = res.data.isEdit;
    //     },
    //     async getNowUser() {
    //         let res = await axios.get('/session');
    //         this.loadNowUser(res.data.id);
    //     },

    //     v_For1() {
    //         for (let i = 0; i < this.answerUser.length; i++) {
    //             this.answers[i].user = this.answerUser[i];
    //         }
    //         if (this.answers[this.answers.length - 1].user.avatar != `` || this.answers.length != 0) {
    //             this.loading = true;
    //         } else {
    //             this.loading = false;
    //         } 
    //     }, 

    //     async loadNowUser(id) {
    //         let res = await axios.get('/user-not-all', {
    //             params: {
    //                 id: id,
    //             }
    //         });
    //         this.userNow = res.data.all;
    //     },

    //     async solveQuestion(is) {
    //         await axios.put(`/is-solved`, {
    //             id: this.$route.query.id,
    //             is_solved: is,
    //         });
    //     },

    //     fixN(text) {
    //         return text
    //         // text.replaceAll("\n", '<br>')
    //     },
    // },
    // mounted() {
    //     this.loadQuestion();
    //     this.checkUser();
    //     this.getNowUser();
    // },
}

</script>

<template>
    <div class="content-2" v-for="answer in answers">
        <div class="account">
            <img class="accountIcon" :src="answer.user.avatar" width="70px" :alt="answer.user.username">
            <div class="name-ring">
                <a :href="`/Profile?id=${answer.user.id}`">
                    <p><span class="name" role="button">{{ answer.user.username }}</span></p>
                </a>
            </div>
                    </div>
                    <div class="description mt-3">
                        <p>fasldkfjlaksdjfkljasdf;lkadflkaf</p>
                    </div>
                    <!-- <div class="btn-group">
                        <div class="left">
                            <button class="comm-add btgr">Добавить комментарий</button>
                        </div>
                    </div> -->
                </div>
</template>

<style scoped>
img {
    user-select: none;
}


.description {

    margin-left: 75px;
}

.accountIcon {
    width: 60px;
    height: 60px;
    border-radius: 50px;
    border: 3px solid #1d1d1d;
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

.description {
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
