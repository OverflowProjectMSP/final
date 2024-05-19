<script>
import axios from 'axios';
import VidQuetions from '../ReuseComponets/QuetionVid.vue';
import ModelWind from '../ReuseComponets/ModelWind.vue';

export default {
    components: {
        VidQuetions,
        ModelWind
    },

    data() {
        return {
            quetions: [],

            tag: `false`,
            dificulty: `false`,
            title: ``,
            author: ``,

            Show: false,
        }
    },
    mounted() {
        this.loadQuestions();
    },
    methods: {
        async loadQuestions() {
            let res = await axios.get('/show-questions');
            this.quetions = res.data.all;
        },
        CloseModal(Show) {
            this.Show = false
        },

        async filtre() {
            let res = await axios.get('/filtre-states', {
                params: {
                    title: this.title,
                    author: this.author,
                    tag: this.tag,
                    dificulty: this.dificulty,
                }
            });
            this.quetions = res.data.all;
        },

        OpenModal() {
            this.Show = !this.Show
        },
        Close(Show) {
            this.Show = !this.Show
        }
    },
}
</script>

<template>
    <div class="quest-menu mt-3">
        <div class="active-container d-flex flex-column p-2">
            <h2>Активные вопросы</h2>
            <p>В данном разделе находятся вопросы, которые ждут именно <b>твоего</b> ответа!</p>
            <div class="all-inputs">
                <div class="inputs">
                    <input v-model="title" type="search" class="form-control w-25" placeholder="Вопрос" aria-label="First name">
                    <input v-model="author" type="search" class="form-control w-25" placeholder="Автор вопроса" aria-label="Last name">
                </div>
                <div class="button-select">
                    <div class="selects">
                        <div class="img-select">
                            <img class="border pe-2 ps-2" src="../../assets/States/image.png" alt="level">
                            <select class="form-select form-1 " v-model="dificulty">
                                <option value="Легкие" selected>Лёгкие</option>
                                <option value="Средние">Средние</option>
                                <option value="Сложные">Сложные</option>
                                <option value="false">Без фильтров</option>
                            </select>
                        </div>
    
                        <select class="form-select form-2 me-2" v-model="tag">
                            <option value="javascript"><img src="./assets/js.jpg" class="image">JavaScript</option>
                            <option value="ts"><img :src="'src/assets/js.jpg'" class="image">TS</option>
                            <option value="python"><img src="./assets/js.jpg" class="image">Python</option>
                            <option value="php"><img src="./assets/js.jpg" class="image">PHP</option>
                            <option value="cpp"><img src="./assets/js.jpg" class="image">C++</option>
                            <option value="java"><img src="./assets/js.jpg" class="image">Java</option>
                            <option value="cs"><img src="./assets/js.jpg" class="image">C#</option>
                            <option value="false"><img src="./assets/js.jpg" class="image">Без фильтров</option>
                        </select>
                    </div>
                    <div class="select-block d-flex border rounded-3 gap-1 py-0  me-2">
                    </div>
                    <div class="down-menu d-flex align-items-center">
                        <div class="d-flex align-items-center">
                            <!-- плюсик -->
                            <div class="contain" @click="OpenModal">
                                <img src="../../assets/States/add.png" class="add">
                            </div>
                            <button class="btn find-btn btn-outline-primary text-dark ms-4" @click="filtre">Найти</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="cont">
    <vid-quetions :quetion="quetion" role="button" v-for="quetion in quetions"></vid-quetions>
    <model-wind v-if="Show" @CloseModal="CloseModal" />
    </div>
</template>

<style scoped>
.cont{
    overflow: scroll;
    height: 555px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
}
a {
    text-decoration: none;
    color: #000;
}

.selects {
    display: flex;
    gap: 10px;
}

.img-select {
    display: flex;
    
}

.form-select {
    width: 280px !important;
}


.selects img {
    border-radius: 10px 0 0 10px;
}

.form-1 {

    border-radius: 0 10px 10px 0;
}

.button-select {
    display: flex;
}

.form-2 {

    border-radius: 10px;
}

.all-inputs {
    display: flex;
    flex-direction: column;
}

.form-control {
    width: 800px !important;
}

.quest-menu {
    margin: 0 20% 15px 20%;
    /* min-height: 57.5vh; Изменить на 52 */
}

@media(max-width: 500px) {
    /* .quest-menu {
        margin: 0;
        margin-bottom: 5px;
    } */

    .selects {
        flex-direction: column;
    }

    .img-select {
        display: flex;
        margin-right: 0;
    }

    .selects img {
        width: 50px;
    }
}

.select-block {
    width: fit-content;
}



.select-block img {
    background-color: #e7e7e7;
}

.active-container {
    margin-bottom: 40px;

}

h4 {
    margin-left: 20.5%;
    margin-top: 20px;
    font-size: 40px;

}

.image {
    margin-right: 10px;
    width: 25px;
}

.add {
    width: 25px;
    height: 25px;
    cursor: pointer
}

.btn {
    width: 133px;
    font-size: 16px;
    font-weight: bold;
    color: blueviolet;
}

.content {
    margin: 10px;
    flex-wrap: wrap;
    margin-left: 20%;
}

.form-control {
    margin: 5px;
}

.dropdown-center {
    margin-left: 15px;
}

.content input {
    width: 300px;
    border-radius: 10px;
}

.con {
    justify-content: start;
}

.contain {
    width: 5%;
    height: 5%;

}

.plus {
    width: 30px;
    height: 30px;
    background-color: #e8e7ea;
    border-radius: 50%;
    border: 0.0001px solid;
}

.p {
    margin-left: 0.2px;
    margin-right: 1px;
}

.dropdown-center {
    margin-right: 10px;
}

@media (hover: hover) {
    .find-btn:hover {
        color: #fff !important;
    }
}

@media(max-width: 1200px) {
    .all-inputs {
        flex-direction: column !important;
        align-items: center;
    }

    .form-control {
        width: 500px !important;
    }

    .button-select {
        flex-direction: column;
    }

    .selects {
        display: flex;
        gap: 20px;
    }

    .selects {
        flex-direction: column;
        align-items: start;
        gap: 5px;
    }

    .form-select {
        width: 455px !important;
    }

    .btn {
        margin-top: 2px;
        width: 450px;
    }

    .form-2 {
        width: 503px !important;
    }

    .selects img {
        /* margin-right: -20px; */
    }
}

@media(max-width: 600px) {
    .selects {
        gap: 10px;
        align-items: center;
    }

    .form-select {
        width: 300px !important;
    }
    
    .form-2 {
        margin-left: 5px;
        width: 350px !important;
    }

    .button-select {
        align-items: center;
    }

    .btn {
        width: 310px;
    }

    .selects img {
        margin-right: -10px;
    }

    .img-select {
        gap: 10px;
    }

    .form-control {
        width: 350px !important;
    }
}
</style>