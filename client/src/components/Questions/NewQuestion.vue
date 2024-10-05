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
                    this.$router.push('/Questions')
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

    mounted() {
        this.isUserSession();
    }
}

</script>
<template>
    <div class="a52">

        <div class="title">
            <h2>Новый вопрос</h2>
        </div>
        <hr>
        <div class="name">
            <h4>Суть вопроса</h4>
            <p class="transparent mb-0">Сформулируйте вопрос так, чтобы сразу было понятно, о чём речь.</p>
            <input type="text" class="form-control" id="inputlg" v-model="form.descriptions">
        </div>
        <div class="text">
            <h4>Детали вопроса</h4>
            <p class="transparent mb-2">Опишите в подробностях свой вопрос, чтобы получить более точный ответ.</p>
            <!-- <div class="d-flex justify-content-between align-items-center"> -->
                <div class="btn-group mb-3" role="group" aria-label="Basic example">
                    <div class="btns1">
                        <button @click="addTag('<b></b>', 3)" type="button" class="btn btn-primary" style="border-radius: 8px 0px 0px 8px"><b>B</b></button>
                        <button @click="addTag('<i></i>', 3)" type="button" class="btn btn-primary" style="border-radius: 0px"><i>i</i></button>
                        <button @click="addTag('<u></u>', 3)" type="button" class="btn btn-primary bord" style="border-radius: 0px"><u>U</u></button>
                    </div>
                    <div class="btns2">
                        <button @click="addTag(`<pre class='format-code'></pre>`, 25)" type="button" class="btn btn-primary bordCode" style="border-radius: 0px"><span>Вставить код</span></button>
                        <label class="input-file">
                            <input @change="convertFileAvatar" type="file"
                                name="file">
                            <span>Выберите файл</span>
                        </label>
                    </div>
                    
                </div>
                <div class="change-lang me-5 pe-5">
                    <select class="form-select one" v-model="form.dificulty">
                        <option value="">Сложность вопроса</option>
                        <option value="Простой">Простой</option>
                        <option value="Средний">Средний</option>
                        <option value="Сложный">Сложный</option>
                    </select>
                    <select class="form-select two" style="border-color: #B3B3  3;" aria-label="Default select example" v-model="form.tag">
                        <option selected value="">Выберите язык</option>
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
            <!-- </div> -->
            <div class="form-floating">
                <textarea ref="textArea" @input="multimethod" @click="updateCursor" 
                    class="text-area text-box multi-line yy form-control formchik" data-val="true"
                    data-val-length="Maximum = 20000 characters" data-val-length-max="10000" id="info"
                    name="info" cols="200" rows="7" style="border-color: #D3D3D3; border-radius: 5px;"
                    v-model="form.details" :maxlength="20000"></textarea>
            </div>
            <div class="mb-3">
            </div>
        </div>
    
        <div class="row  block">
            <div class="change-public">
                
                <div class="btn-error">
                    <button class="btn btn-public" @click="addQuestion"><b>Опубликовать</b></button>
                    <span class="text-danger" v-if="this.error">{{ error }}</span>
                </div>
            </div>
        </div>
    </div>
    <div v-if='this.isUserInSession'class='w-100 h-100 d-flex justify-content-center align-items-center'>
        <div class="bg-black"></div>
        <div class="modal-cenel d-flex flex-column align-items-center">
            <img src="../../assets/Lending/bookModal.png" alt="Грусть(">
            <h6>У вас недостаточно прав доступа, войдите в аккаунт</h6>
            <button @click='this.$router.push("/Login")'>Войти</button>
        </div>
    </div>
</template>

<style scoped>
.modal-cenel {
  opacity: 1 !important;
  position: fixed;
  top: calc(50% - 160px);
  z-index: 52 !important;
  background: rgba(59, 130, 246, 0.65);
  padding: 24px;
  border-radius: 10px;
  color: #fff;
  gap: 20px;
}

@media (max-width: 900px) {
    .modal-cenel {
        margin: 0 32px !important;
    }
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

/* стили кнопок */
.a52 {
    width: 100%;
    display: flex;
    flex-direction: column;
    overflow: hidden !important;
}

.title h2 {
    color: #000;
}

.change-lang {
    display: flex;
    gap: 60px;
    margin-left: 35px;
}

.form-select {
    margin: 0 !important;
}

.one {
    width: 230px !important;
}

.btn-public {
    background-color: rgb(255, 255, 255);
    color: #7ac97a;
    border: 2px solid #7ac97a;
    border-radius: 5px;
    width: 175px;
    padding: 5px 15px;
    text-align: center;
    transition: all 200ms;

    margin-left: 30px;
}


.title h2 {
    font-size: 30px !important;
}

.btn-public:hover {
    background-color: #7ac97a;
    color: #ffffff;
}

.btn-public:active {
    background-color: #5ba35b;
}

.btn-error {
    width: 700px;
    display: flex;
    align-items: center;
    gap: 20px;
}

#preview {
    background-color: rgb(255, 255, 255);
    color: #7ac97a;
    border-color: #90EE90;
    border-radius: 5px;
    padding-right: 15px;
    padding-left: 15px;
    text-align: center;
}

.block {
    margin-bottom: 10px;
}

.input-file span {
    line-height: 29px !important;
}



/* 1. Стили для шрифта и общего оформления страницы */
@import url('https://fonts.cdnfonts.com/css/rubik');

html {
    margin: 0;
    background-color: #EEF1F4;
    padding: 0;
    width: 100%;
    height: 100%;
}

main {
    margin: 10px;
}

body {
    font-family: Rubik !important;
}


/* 2. Стили для заголовка, разделителя и текста */
.title {
    font-size: 25px;
    margin-top: 20px;
    margin-left: 37px;
}

hr {
    width: 95%;
    margin: 20px 35px 0 25px;
}

.name h4 {
    margin: 20px 35px 0px;
}

.change-public {
    width: 200px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.form-select {
    margin-left: 30px;
    width: 200px;
}

.transparent {
    color: #B3B3B3;
    margin: 7px 36px 0px;
    margin-bottom: 40px;
}

.input-file span {
    height: 46px !important;
}

.btn-group {
    margin-left: 35px;
}

/* 3. Стили для ввода имени, текста и кнопок */
.name input {
    margin: 12px 35px 0px;
    width: 1850px;
    border-radius: 7px;
    border-color: #B3B3B3;
    width: calc(100% - 70px);
}

.text h4 {
    margin: 20px 35px 0px;
}

.btn-secondary {
    background-color: white;
    color: black;
    margin-left: 35px;
    padding: 10px;
}

textarea {
    resize: none;
}


/* 4. Стили для форм и кнопок */
.forms {
    display: flex;
    gap: 60px;
    align-items: center;
    margin-left: 35px;
}

.main {
    color: green;
}

.first {
    color: orange;
}

.second {
    color: red;
}

/* 5. Дополнительные стили для кнопочек и блока формы */
#inputlg {
    width: 80%;
}

.formchik {
    margin: 20px 35px 0px;
    border-radius: 7px;
    height: 400px;
}

.btn-wrapper button {
    font-size: 25px;
    margin: 20px 35px 0px;
    border-radius: 10px;
    display: flex;
}

.btn-wrapper {
    display: flex;
    flex-direction: row;
}

.btn-dark {
    border-color: #B3B3B3;
    color: #B3B3B3;
    background-color: white;
}

.btn-dark:hover {
    border-color: #B3B3B3;
    color: white;
    background-color: gray;
    transition: 0.2s;
}

.btn-dark:active {
    border-color: #B3B3B3;
    color: white;
    background-color: #565656;
}

.btn-success:active {
    color: white;
    background-color: #074B2A;
    border-color: #188755;
}


/* 6. Дополнительные стили для кнопочки и для форм*/
.btn {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
}

.form-control {
    width: 95%;
}

.form1,
.form2 {
    width: 75%;
    margin-right: 40px;
}



/* 8. Адаптивка */
@media only screen and (max-width:659px) {
    #inputlg {
        width: 85%;
    }

    .forms {
        gap: 1px;
        margin-left: 12%;
        margin-top: 15px;
        width: 80%;
    }

    .form-control {
        width: 85%;
    }

    /* .btn-group .btn {
        margin-left: 30px;
        padding: 1% 6%;
        font-size: 10px;
    } */

    hr {
        width: 85%;
    }

    .btn-wrapper {
        flex-direction: column;
    }

    .btn-success {
        width: 200px;
        padding-left: 14px;
    }

    .btn-dark {
        width: 200px;
        padding-left: 10px;
    }
}

@media only screen and (min-width: 250px) {
    /* .btn-group .btn {
        margin-left: 35px;
        padding: 1% 2%;
        font-size: 11px;
    } */

    .forms {
        width: 95%;
        margin-left: 14%
    }
}


@media only screen and (min-width: 310px) {
    /* .btn-group .btn {
        margin-left: 35px;
        padding: 1% 3.75%;
        font-size: 10px;
    } */

    .form-control {
        width: 80%;
    }

    .forms {
        width: 87%;
        margin-left: 12%;
    }
}

@media only screen and (min-width: 350px) {
    /* .btn-group .btn {
        margin-left: 35px;
        padding: 1% 4.5%;
        font-size: 10px;
    } */

    .form-control {
        width: 80%;
    }

    .forms {
        width: 87%;
        margin-left: 12%;
    }
}

@media only screen and (min-width: 380px) {
    .forms {
        width: 75%;
        margin-left: 15%;
    }

    /* .btn-group .btn {
        margin-left: 30px;
        padding: 1% 5.5%;
        font-size: 10px;
    } */
}

@media only screen and (min-width: 540px) {
    /* .btn-group .btn {
        margin-left: 30px;
        padding: 1% 9%;
        font-size: 10px;
    } */
}


@media only screen and (min-width: 660px) {
    hr {
        width: 95%;
    }

    #inputlg {
        width: 90%;
    }

    .form-control {
        width: 90%;
    }


    /* .btn-group .btn {
        margin-left: 40px;
        font-size: 15px;
        padding: 10px 4%;
    } */

    .forms {
        flex-direction: column;
        gap: 10px;
        margin-left: 70%;
        margin-top: -85px;
        width: 30%;
    }


}


@media only screen and (min-width: 800px) {
    hr {
        width: 95%;
    }

    #inputlg {
        width: 90%;
    }

    /* .btn-group .btn {
        margin-left: 40px;
        font-size: 15px;
        padding: 7px 6%;
    } */

    .forms {
        margin-top: -81.5px;
        gap: 5px;
        margin-left: 70%;
        width: 28%;
    }
}


@media only screen and (min-width: 1050px) {
    hr {
        width: 95%;
    }

    #inputlg {
        width: 90%;
    }

    /* .btn-group .btn {
        margin-left: 40px;
        font-size: 16px;
        padding: 10px 30px;
    } */

    .forms {
        margin-top: -70px;
        gap: 10px;
        margin-left: 77%;
        width: 20%;
    }
}


@media only screen and (min-width: 1200px) {
    hr {
        width: 95%;
    }

    #inputlg {
        width: 90%;
    }

    /* .btn-group .btn {
        margin-bottom: 4%;
        margin-left: 35px;
        font-size: 16px;
        padding: 10px 20px;
    } */

    .forms {
        gap: 1px;
        flex-direction: row;
        margin-left: 65%;
        width: 30%;
    }

    .forms .form-select {
        height: 45px;
    }
}


@media only screen and (min-width: 1400px) {
    hr {
        width: 95%;
    }

    #inputlg {
        width: 90%;
    }

    .forms {
        gap: 1px;
        flex-direction: row;
        margin-left: 73%;
        width: 20%;
    }

    /* .btn-group .btn {
        margin-bottom: 2.5%;
        margin-left: 35px;
        font-size: 16px;
        padding: 10px 40px;
    } */
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

/* @media only screen and (max-width: 768px) {
        .btn {
            padding: 8px 16px;
            font-size: 14px;
        }
    } */
/* @media only screen and (max-width: 1850px) {
        .forms {
            flex-direction: column;
            gap: 20px;
            margin-left: 0;
            margin-top: 40px;
            margin-left: -68%;
        }

    } */

@media (max-width: 700px) {
    .a52 {
        margin-top: -40px;
    }
}

@media (max-width: 615px) {
    .change-lang {
        gap: 10px;
    }
}

@media (max-width: 550px) {
    .change-lang {
        flex-direction: column;
    }

    .two {
        width: 230px !important;
    }
}

@media (max-width: 500px) {
    .btn-group {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
    .btns1 {
        display: flex;
    }

    .bord {
        border-radius: 0px 8px 8px 0px !important;
    }

    .bordCode {
        border-radius: 8px !important;
        width: 150px;
    }

    .btns2 {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .input-file span {
        border-radius: 8px !important;
    }

    .input-file span {
        width: 150px;
    }
}

@media (max-width: 350px) {
    .form-control {
    }
}
</style>
