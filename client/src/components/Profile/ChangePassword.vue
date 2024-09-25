<script>
import axios from 'axios';
export default {
    data() {
        return {
            oldPassword: ``,
            newPassword: ``,
            exPassword: ``,
            error: '',
            id:'',
            isInSession: false,
        }
    },

    methods: {
        check(){
            if (!this.newPassword.includes('~') && 
                !this.newPassword.includes('`') && 
                !this.newPassword.includes('!') && 
                !this.newPassword.includes('@') && 
                !this.newPassword.includes('#') && 
                !this.newPassword.includes('%') && 
                !this.newPassword.includes('^') && 
                !this.newPassword.includes('&') && 
                !this.newPassword.includes('*') && 
                !this.newPassword.includes('(') && 
                !this.newPassword.includes(')') && 
                !this.newPassword.includes('-') && 
                !this.newPassword.includes('_') && 
                !this.newPassword.includes('=') && 
                !this.newPassword.includes('+') && 
                !this.newPassword.includes('[') && 
                !this.newPassword.includes(']') && 
                !this.newPassword.includes('{') && 
                !this.newPassword.includes('}') && 
                !this.newPassword.includes('\\') && 
                !this.newPassword.includes('|') && 
                !this.newPassword.includes(';') && 
                !this.newPassword.includes(':') && 
                !this.newPassword.includes('"') && 
                !this.newPassword.includes(',') && 
                !this.newPassword.includes('<') && 
                !this.newPassword.includes('.') && 
                !this.newPassword.includes('>') && 
                !this.newPassword.includes('/') && 
                !this.newPassword.includes('?')) {
                    this.error = '*Пароль должен включать спец символ*';
                } else if (this.newPassword.includes('$')) {
                    this.error = '*Ты че, не патриот? Доллары всякие тут ставишь*';
                } else {
                    this.putInfo();
                }
        },
        async putInfo() {
            if (this.newPassword == this.exPassword ) {
                let res = await axios.put('/new-password-old', {
                    old_password: this.oldPassword,
                    new_password: this.newPassword,
                });
                if (res.data.res == 'Error') {
                    this.error = '*Ошибка отправки*';
                } else if (res.data.res == 'True') {
                    this.$router.push(`/Profile?id=${this.id}`);
                } else {
                    this.error = 'Неизветсная ошибка';
                }
            } else {
                this.error = 'Пароли не совпадают';
            }


        },
        async getId(){
            let res = await axios.get(`/session`);
            this.id = res.data.id;
            if(!this.id) {
                this.$router.push('/Login')
            }
        }
    },
    mounted(){
        this.getId()
    }
}
</script>
<template>
    <form class="container mb-3" @submit.prevent="check" v-if='this.id'>
        <div class="row pt-5">
            <div class="col-3">
                <h3>Настройки профиля</h3>
            </div>
        </div>
        <hr>
        <div class="ancet d-flex" style="display: flex; gap: 40px;">
            <h5 role="button" class="mb-0" style="color: gray; font-weight: 400;"><a href="/ProfileSettings">Анкета</a>
            </h5>
            <h5 role="button" class="mb-0 border-bottom border-2 border-dark"><a href="/ChangePassword">Аккаунт</a>
            </h5>
        </div>
        <hr>
        <h2 class="text-center mt-4 mb-3">Смена пароля</h2>
        <div class="password-container">
            <h5>Старый пароль</h5>
            <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="oldPassword">
            </div>
            <h5 class="mt-4">Новый пароль</h5>
            <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="newPassword">
            </div>
            <h5 class="mt-4">Повторите новый пароль</h5>
            <div class="input-group mb-5">
                <input type="text" class="form-control" v-model="exPassword">
            </div>
        </div>
        <div class="d-flex justify-content-start mt-5 ms-0">
            <button class="btn btn-outline-success w-fit ms-0" type="submit"><b>Сохранить изменения</b></button>
        </div>
        <span class="text-danger" v-if="this.error">{{ this.error }}</span>
    </form>
</template>
<style scoped>
select {
    padding: 7.5px 15px 7.5px 2px;
    border-radius: 3px;
    transition: all 300ms;
}

select:hover {
    border-color: blue;
}

@media (max-width: 960px) {
    .place-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px !important;
    }

    .s-place {
        margin-left: 0 !important;
        max-width: 100%;
    }

    .country-select {
        width: 100% !important;
    }
}

@media (max-width: 540px) {
    .place-container {
        align-items: center;
    }

    .save-btn-block {
        width: 100%;
        text-align: center
    }

    .acent {
        margin-right: 60px !important;
    }

    .contact-input {
        margin-left: 12px !important;
    }
}

@media (max-width: 360px) {
    .country-select {
        max-width: 310px !important;
    }

    .s-place {
        margin-left: 0 !important;
        max-width: 310px;
    }
}
</style>