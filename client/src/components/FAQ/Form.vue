<script>
import axios from 'axios';
export default {
    data() {
        return {
     
            phone: ``,
            email: ``,
            message: ``,
            userBase: [],
            invalid: ``,
            valid: ``
        }
    },

    methods: {
        addUser() {
            if ( this.phone == `` || this.email == `` || this.message == ``) {
                this.invalid = `Не все поля заполнены`;
                return;
            }
             else if (this.message.length <= 19) {
                this.invalid = `Сообщение должно включать не менее 20 символов`;
                return;
            } else if (this.phone.length <= 3) {
                this.invalid = `Неправильный номер телефона`;
                return;
            } else {
                this.invalid = ``;
                this.valid = `Отправляется...`;
                setTimeout(() => {
                    this.username = ``;
                    this.phone = ``;
                    this.email = ``;
                    this.message = ``;
                    this.valid = `Отправленно!`
                }, 1500);
                setTimeout(() => {
                    this.valid = ``
                }, 4500)
                this.SendHelp();
            }
        },
        async SendHelp() {
            await axios.post(`/help`, {
                phone: this.phone,
                email: this.email,
                message: this.message
            })
        }
    }
}
</script>


<template>
    <form class="form-container d-flex flex-column align-items-center justify-content-center gap-4 border
    border-black rounded-5 p-4 mx-5 my-1" @submit.prevent="addUser">
        <h2 v-if="this.username == ``" class="fw-bold text-2">Остались вопросы? Свяжитесь с нами!</h2>
        <h2 v-else class="fw-bold text-2 text-center">Остались вопросы? Свяжитесь с нами!</h2>
        <input type="tel" class="p-4 rounded-3 text-black bg-white border border-black" placeholder="Контактные данные (Discord, Tg...)"
            v-model="phone">
        <input type="email" class="p-4 rounded-3 text-black bg-white border border-black" placeholder="Email"
            v-model="email">
        <textarea type="text" class="p-3 rounded-3 text-black bg-white border border-black"
            placeholder="Ваше сообщение/предложение" v-model="message"></textarea>
        <span v-if="this.invalid != ``" class="text-danger text-4">{{ invalid }}</span>
        <span v-if="this.valid != ``" class="text-success text-4 fw-bold">{{ valid }}</span>
        <button class="btn btn-outline-primary fs-5" @click="addUser" type="button">Отправить</button>
        <a href="#">Уже писали? Нажмите сюда!</a>
    </form>
</template>


<style scoped>



.form-container {
    margin: 1rem 180px !important;
}

input {
    width: 300px;
    height: 30px;
}

textarea {
    width: 300px;
    height: 100px;
}

.btn {
    width: 12.5% !important;
    border-radius: 10px;
}

a {
    text-decoration: none;
    color: #099911;
    transition: color 400ms;
}


@media (hover: hover) {
    
    a:hover {
        color: #11c51a;
    }
}

@media (max-width: 950px) {
    .form-container {
        margin: 12px 10px !important;
        padding: 45px !important;
    }

    h2 {
        font-size: 25px;
    }

    input {
        width: 95% !important;
    }

    textarea {
        width: 95% !important;
    }

    .btn {
        width: 90% !important;
    }
}

@media (min-width: 950px) and (max-width: 1650px) {
    input {
        width: 45% !important;
    }

    textarea {
        width: 45% !important;
    }

    .btn {
        width: 45% !important;
    }
}
</style>