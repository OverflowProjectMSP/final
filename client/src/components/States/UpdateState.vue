<script>
import axios from 'axios';
export default {
    data() {
        return {
            Vid: false,
            sloz: ``,
            good: `Вопрос готов для предпросмотра.`,
            nogood: `Заполните все поля корректно`,
            greenlabel: true,
            color: `green`,
            language: ``,
            error: '',

            form: {
                descriptions: ``,
                details: ``,
                tag: ``,
            },

            isCheck: false,
        }
    },
    mounted() {
        this.loadQuestion();
        this.checkUser();
    },
    methods: {
        async addQuestion() {
            await axios.put('/change', {
                id: this.$route.query.id,
                all: this.form,
                q: 'false'
            });
        },

        async loadQuestion() {
            let res = await axios.get('/show-one', {
                params: {
                    q: 'true',
                    id: this.$route.query.id
                }
            });
            this.form = res.data.all.question;
        },

        async checkUser() {
            let res = await axios.get('/check', {
                params: {
                    id: this.$route.query.id
                }
            });
            this.isCheck = Boolean(res.data.isEdit);
        },
    }
}

</script>
<template>
    <main v-if="isCheck">

        <form class="container" @submit.prevent="addQuestion">
            <div class="row pt-4">
                <div class="col-12">
                    <h3>Новый вопрос</h3>
                </div>
            </div>
            <hr>
            <div class="row">
                <div class="col-12">
                    <h4>Суть вопроса</h4>
                </div>
            </div>
            <div class="row" style="display: flex; gap: 40px;">
                <div class="col-12">
                    <h5 style="color: gray; font-weight: 400;">Сформулируйте вопрос так, чтобы сразу было понятно, о чём
                        речь.</h5>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <div class="input-group mb-3">
                        <textarea class="text-area text-box multi-line" data-val="true"
                            data-val-length="Maximum = 2045 characters" data-val-length-max="10000" id="texting"
                            name="info" cols="200" rows="3" style="border-color: #D3D3D3; border-radius: 5px;"
                            v-model="form.descriptions" maxlength="35"></textarea>

                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <h4>Детали вопроса</h4>
                </div>
            </div>
            <div class="row" style="display: flex; gap: 40px;">
                <div class="col-12">
                    <h5 style="color: gray; font-weight: 400;">Опишите в подробностях свой вопрос, чтобы получить более
                        точный ответ.</h5>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <div class="input-group mb-3">
                        <textarea class="text-area text-box multi-line yy" data-val="true"
                            data-val-length="Maximum = 2045 characters" data-val-length-max="10000" id="info"
                            name="info" cols="200" rows="3"
                            style="border-color: #D3D3D3; border-radius: 5px;" v-model="form.details"></textarea>

                    </div>
                </div>
            </div>

            <div class="row pt-4">
                <div class="col-6">
                    <h4>Сложность вопроса</h4>
                </div>
                <div class="col-6">
                    <h4>Ваш язык программирования</h4>
                </div>

                <div class="row pt-1">
                    <div class="col-6">
                        <select class="form-select" v-model="form.tag">
                            <option value="python">Python</option>
                            <option value="java">Java</option>
                            <option value="php">PHP</option>
                            <option value="javascript">JavaScript</option>
                            <option value="cpp">C++</option>
                        </select>
                    </div>
                </div>
                <div class="row pt-5 block">
                    <div class="col-6">
                        <button id="save" type="submit"><b>Изменить</b></button>
                    </div>

                </div>
                
                <p class="error" :class="color">{{ error }}</p>
                <!-- виджет -->
                
            </div>
               
          
                
        </form>



    </main>
    <main v-else>
        <div class="d-flex justify-content-center align-items-center text-muted fs-2 mt-5 p-5">Произошла ошибка, невозможно изменить вопрос</div>
    </main>
</template>
<style scoped>
main {
    margin: 0 !important;
    width: 100%;
    min-height: 90vh;
}
#save {
    background-color: rgb(255, 255, 255);
    color: #7ac97a;
    border-color: #90EE90;
    border-radius: 5px;
    padding: 5px 15px;
    text-align: center;
    transition: all 300ms;
}

#preview {
    background-color: rgb(255, 255, 255);
    color: #7ac97a;
    border-color: #90EE90;
    border-radius: 5px;
    padding: 5px 15px;
    text-align: center;
    transition: all 300ms;
}



.block {
    margin-bottom: 50px;
}

.text-area {
    padding: 10px;

}

/* стили лейбла */

.green {
    color: green;
}

.red {
    color: red;
}


/* тут стили виджета */

:root {
    --size-20: 20px;
    --size-26: 26px;
    --size-22: 22px;
    --size-18: 18px;
}

.t-alig-c {
    text-align: center;
}

/* виджет с вопросами */
.vid {
    background-color: #EEF1F4;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    border-radius: 15px;
    margin-bottom: 50px;

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
div.vid {
    transition: all 0.5s;
}



/* Адаптивка */

@media (hover: hover) {
    div.vid:hover {
        transform: translateY(-10px);
        box-shadow: 10px 5px 5px rgb(0, 0, 0, 0.5);
    }

    #preview:hover {
        background-color: #90EE90 !important;
        color: #2c2c2c;
    }

    #save:hover {
        background-color: #90EE90 !important;
        color: #000;
    }
}

@media(max-width: 1200px) {
    .q {
        font-size: var(--size-20);
    }
}

@media(max-width: 992px) {
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