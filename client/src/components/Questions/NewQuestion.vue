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
            color: `red`,
            language: ``,
            error: '',

            form: {
                descriptions: ``,
                details: ``,
                dificulty: ``,
                tag: ``,
                imageBase64: [],
                links: [],
            },

            file: '',
            filename: '',
            avatar: '',
            imageLink: [],

            imagePast: '<img src=``>',
            isUserInSession: false,

        }
    },
    methods: {
        async addQuestion() {
            this.isUserSession();
            if (this.form.tag != `` && this.isUserInSession) {
                let res = await axios.post('/new-question', {
                    form: this.form,
                });
                if (res.data.res == 'Вопрос добавлен') {
                    this.error = '';
                    this.$router.push('/Quetions')
                    return;
                } else if(res.data.res.cd == true) {
                    this.error = `Вы недавно создавали вопрос. Вы можете создать новый примерно через ${Math.ceil(res.data.res.time / 60)} минут`;
                    return;
                }
                this.error = 'Такой вопрос уже существует'
                return;
            } else {
                this.error = 'Выберите язык программирования'
            }
        },

        updateCursor(event) {
            this.cursorPosition = event.target.selectionStart;
        },

        addTag(tags, number) {
            const beforeCursor = this.form.details.slice(0, this.cursorPosition);
            const afterCursor = this.form.details.slice(this.cursorPosition);

            this.form.details = beforeCursor + tags + afterCursor;
            this.$nextTick(() => {
                const newCursorPosition = this.cursorPosition + number;
                this.$refs.textArea.focus();
                this.$refs.textArea.setSelectionRange(newCursorPosition, newCursorPosition);
                this.updateCursor({ target: this.$refs.textArea });
            });
        },

        async convertFileAvatar(event) {
            const file = event.target.files[0];
            const reader = new FileReader();
            const filename = event.target.files[0].name;
            this.filename = filename;
            reader.onload = () => {
                this.addToString();
                this.form.imageBase64.push(reader.result);
            };
            reader.readAsDataURL(file);
        },

        async addToString() {
            let linka = await this.sendImage();
            this.form.links.push(linka);
            this.imagePast = `<img src="${linka}">`
            this.addTag(this.imagePast, linka.length);
        },
        
        async sendImage() {
            let res = await axios.post('/add-img', {
                name: this.filename
            });
            return res.data.link;
        },

        async isUserSession() {
            let res = await axios.get('/check-r');
            this.isUserInSession = res.data.all;
        }
    },
}

</script>
<template>
    <HeaderComp />
    <main>
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
                        <input class="text-area text-box multi-line w-100" data-val="true"
                            data-val-length="Maximum = 2045 characters" data-val-length-max="10000" id="texting"
                            name="info" cols="200" rows="3" style="border-color: #D3D3D3; border-radius: 5px;"
                            v-model="form.descriptions" maxlength="100">
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
            <div class="btn-group mb-3" role="group" aria-label="Basic example">
                <div class="btns1">
                    <button @click="addTag('<b></b>', 3)" type="button" class="btn btn-primary" style="border-radius: 8px 0 0 8px"><b>B</b></button>
                    <button @click="addTag('<i></i>', 3)" type="button" class="btn btn-primary" style="border-radius: 0"><i>i</i></button>
                    <button @click="addTag('<u></u>', 3)" type="button" class="btn btn-primary bord"><u>U</u></button>
                </div>
                <div class="btns2">
                    <button @click="addTag(`<pre class='format-code'></pre>`, 25)" type="button" class="btn btn-primary bordCode"><span>Вставить код</span></button>

                    <label class="input-file">
                        <input @change="convertFileAvatar" type="file"
                            name="file">
                        <span>Выберите файл</span>
                    </label>

                </div>
                    
                </div>

                <div class="sel-block">
                    <div class="diff-que">
                            <select class="form-select" v-model="form.dificulty">
                                <option value="">Сложность вопроса</option>
                                <option value="Простой">Простой</option>
                                <option value="Средний">Средний</option>
                                <option value="Сложный">Сложный</option>
                            </select>
                    </div>
                    <div class="yourlang">
                            <select class="form-select" v-model="form.tag">
                                <option value="">Ваш язык программирования</option>
                                <option value="javascript">JavaScript</option>
                                <option value="ts">TS</option>
                                <option value="python">Python</option>
                                <option value="php">PHP</option>
                                <option value="cpp">C++</option>
                                <option value="java">Java</option>
                                <option value="cs">C#</option>
                                <option value="go">Golang</option>
                                <option value="IB">ИБ</option>
                            </select>
                    </div>
                </div>
           
                <div class="row">
                    <div class="col-12">
                        <div class="input-group mb-3">
                            <textarea ref="textArea" @input="updateCursor" @click="updateCursor"
                                class="text-area text-box multi-line yy" data-val="true"
                                data-val-length="Maximum = 2045 characters" data-val-length-max="10000" id="info"
                                name="info" cols="200" rows="7" style="border-color: #D3D3D3; border-radius: 5px;"
                                v-model="form.details"></textarea>

                        </div>
                    </div>
                </div>

            
                <div class="row pt-5 block">
                    <div class="col-6 btn-error">
                        <button class="btn btn-public"type="submit"><b>Опубликовать</b></button>
                        <p v-if='error' class="error" :class="color">{{ error }}</p>
                    </div>
                </div>
        </form>

    </main>

    <div v-if='this.isUserInSession' class='w-100 h-100 d-flex justify-content-center align-items-center'>
        <div class="bg-black"></div>
        <div class="modal-cenel d-flex flex-column align-items-center">
        <img src="../../assets/Lending/bookModal.png" alt="Грусть(">
        <h6>Ввойдите в аккаунт, чтобы продолжить действие</h6>
        <button @click='this.$router.push("/Login")'>Войти</button>
        </div>
    </div>
</template>
<style scoped>
.modal-cenel {
  opacity: 1 !important;
  position: fixed;
  top: calc(50% - 260px);
  z-index: 52 !important;
  background: rgba(59, 130, 246, 0.65);
  padding: 24px;
  border-radius: 10px;
  color: #fff;
  gap: 20px;
}

.bord {
    border-radius: 0px;
}

.bordCode {
    border-radius: 0px;
}

.modal-cenel button {
  border-radius: 10px;
  border: 1px solid#fff;
  padding: 4px 24px;
  background: none;
  color: #fff;
  opacity: 1 !important;
}

.modal-cenel h6 {
  opacity: 1 !important;
}


.modal-cenel img {
  border-radius: 0% !important;
  width: 150px;
  opacity: 1 !important;
}

.bg-black {
  background: #000;
  opacity: 0.5;
  z-index: 1;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
}

.btn-public {
    background-color: rgb(255, 255, 255);
    color: #7ac97a;
    border: 2px solid #7ac97a;
    border-radius: 5px;
    width: 175px;
    height: 50px;
    padding: 5px 15px;
    text-align: center;
    transition: all 200ms;
}

.selects {
    margin-bottom: 30px;
}

.form-select {
    width: 500px;
}


.sel-block {
    display: flex;
    gap: 22%;
    width: 100%;
    margin-top: 30px;
    margin-bottom: 30px;
}


.btn-public:hover {
    background-color: #7ac97a;
    color: #ffffff;
}

.btn-public:active {
    background-color: #5ba35b;
}

.btn-error {
    display: flex;
    align-items: center;
    gap: 20px;
}

.error {
    margin: 0px;
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

@media (max-width: 1400px) {
    .sel-block {
        gap: 10%;
    }
}

@media(max-width: 1200px) {
    .q {
        font-size: var(--size-20);
    }

    .sel-block {
        gap: 5%;
    }

    .form-select {
        width: 445px;
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

    .form-select {
        width: 330px;
    }

    .sel-block {
        h4 {
            font-size: 20px;
        }
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

    .sel-block {
        flex-direction: column;
        gap: 20px;
    }

}

.input-file {
    position: relative;
    display: inline-block;
}

.input-file span {
    position: relative;
    display: inline-block;
    cursor: pointer;
    outline: none;
    text-decoration: none;
    font-size: 14px;
    vertical-align: middle;
    color: rgb(255 255 255);
    text-align: center;
    border-radius: 0 0.375rem 0.375rem 0;
    background-color: #0d6efd;
    line-height: 22px;
    height: 40px;
    padding: 10px 20px;
    box-sizing: border-box;
    border: none;
    margin: 0;
    transition: background-color 0.2s;
}

.input-file input[type=file] {
    position: absolute;
    z-index: -1;
    opacity: 0;
    display: block;
    width: 0;
    height: 0;
}

/* Focus */
.input-file input[type=file]:focus+span {
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, .25);
}

/* Hover/active */
.input-file:hover span {
    background-color: #0b5ed7;
}

.input-file:active span {
    background-color: rgb(23, 113, 247);
}

/* Disabled */
.input-file input[type=file]:disabled+span {
    background-color: #eee;
}

.btn-group {
    display: flex;
    align-items: center;
}

.input-file span {
    height: 38px;
}

textarea {
    width: 100%;
}

@media (max-width: 500px) {
    .btn-group {
        flex-direction: column;
        align-items: start;
        gap: 5px;
    }

    .btn-primary {
        width: 50px;
    }

    .btns1 {
    }

    .bord {
        border-radius: 0 8px 8px 0 !important;
    }
    
    .btns2 {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .btns2 button {
        width: 150px;
    }

    .bordCode {
        border-radius: 8px;
    }

    .btns2 span {
        width: 150px;
        border-radius: 8px !important;
    }
}

@media (max-width: 770px) {
    h4 {
        font-size: 16px !important;
    }

    .your {
        margin-left: -10px;
    }
}
</style>
