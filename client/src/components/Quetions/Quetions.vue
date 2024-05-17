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
            quetions: [
                {
                    discriptions: `VUE JS IS PARASHА??`,
                    tag: 'Js',
                    subscribers: 50,
                    date: `52.52.52`,
                    views: 43,
                    answers: 423,
                    complexity: 'Средне',
                    id: 0,
                    question: true,            
                },
                {
                    discriptions: `VUE IS PARASHА!!`,
                    tag: 'Python',
                    subscribers: 50,
                    date: `52.52.52`,
                    views: 43,
                    answers: 423,
                    complexity: 'Тяжело',
                    id: 1,
                    question: true,            
                },
            ],

            filters: {
                type: "false",
                dificulty: "false",
            },

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
            if (this.filters.type == 'false' && this.filters.dificulty == 'false') {
                this.filtrs = {
                    filtr: false
                }
            } else {
                this.filtrs = {
                    filtr: true,
                    tag: this.filters.type,
                    dificulty: this.filters.dificulty,
                };
            }
            let res = await axios.post('/filtre-questions', {
                body: {
                    filters: this.filtrs
                }
            });
            this.quetions = res.data;
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
            <div class="d-flex flex-row">
                <div class="select-block d-flex border rounded-3 gap-1 py-0  me-2">
                    <img class="border-end pe-2 ps-2" src="../../assets/States/image.png" alt="level">
                    <select class="form-select border-0" v-model="filters.dificulty">
                        <option value="Легкие" selected>Лёгкие</option>
                        <option value="Средние">Средние</option>
                        <option value="Сложные">Сложные</option>
                        <option value="false">Без фильтров</option>
                    </select>
                </div>
                <div class="down-menu d-flex align-items-center">
                    <div class="d-flex align-items-center">
                        <select class="form-select me-2" v-model="filters.type">
                            <option value="JavaScript"><img src="./assets/js.jpg" class="image">JavaScript</option>
                            <option value="TS"><img :src="'src/assets/js.jpg'" class="image">TS</option>
                            <option value="Python"><img src="./assets/js.jpg" class="image">Python</option>
                            <option value="PHP"><img src="./assets/js.jpg" class="image">PHP</option>
                            <option value="C++"><img src="./assets/js.jpg" class="image">C++</option>
                            <option value="Java"><img src="./assets/js.jpg" class="image">Java</option>
                            <option value="C#"><img src="./assets/js.jpg" class="image">C#</option>
                            <option value="false"><img src="./assets/js.jpg" class="image">Без фильтров</option>
                        </select>
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

.quest-menu {
    margin: 0 20% 15px 20%;
    /* min-height: 57.5vh; Изменить на 52 */
}

@media(max-width: 500px) {
    .quest-menu {
        margin: 0;
        margin-bottom: 5px;
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
</style>