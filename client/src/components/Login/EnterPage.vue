<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: '',
            exPassword: '',
            
            error: '',
            eyeOpen1: true,
            eyeOpen2: true,
            eyeImg1: '/src/assets/Login/eye-open.svg',
            eyeImg2: '/src/assets/Login/eye-open.svg',
            isShowPassword: false,
            showPassword: 'password',
            isShowExPassword: false,
            showExPassword: 'password',
            a: "",
        }
    },
    methods: {
        check() {
            if (this.email === '') {
                this.error = '*Вы не ввели Email*'
            } else if (this.password === '') {
                this.error = '*Вы не ввели пароль*'
            } else if (this.exPassword === '') {
                this.error = '*Вы не повторили пароль*'
            } else if (this.password !== this.exPassword) {
                this.error = '*Пароли не совпадают'
            }
            else {
                this.error = '';
                this.login();
            }


            if (this.password !== this.exPassword) {
                this.error = '*Пароли не совпадают'
            }
        },
        toggleVisibility1() {
            this.isShowPassword = !this.isShowPassword;
            this.eyeOpen1 = !this.eyeOpen1

            if (this.isShowPassword) {
                this.showPassword = 'text'
                this.eyeImg1 = '/src/assets/Login/eye-close.svg'
            } else {
                this.showPassword = 'password'
                this.eyeImg1 = '/src/assets/Login/eye-open.svg'
            }
        },
        toggleVisibility2() {
            this.isShowExPassword = !this.isShowExPassword;
            this.eyeOpen2 = !this.eyeOpen2

            if (this.isShowExPassword) {
                this.showExPassword = 'text'
                this.eyeImg2 = '/src/assets/Login/eye-close.svg'
            } else {
                this.showExPassword = 'password'
                this.eyeImg2 = '/src/assets/Login/eye-open.svg'
            }
        },
        
        async login() {
            let res = await axios.post('/login', {
                email: this.email,
                password: this.password
            });
            if(res.data.message == 'ok') {
                this.$router.push('/');
            } else if(res.data.message == 'wrong!') {
                this.error = 'Пароль и почта не совпадают!';
            } else {
                this.error = 'Неизвестная ошибка.';
            }

        },
    }
}

</script>

<template>
    <div class="tototocontainer">
        <div class="background"></div>
        <div class="content">
            <p>Войти</p>
            <div class="regist">
                <form @submit.prevent="check">
                    <input v-model="email" class="inp inp-email" type="email" placeholder="Почта">
                    <div class="password-container">
                        <input v-model="password" class="inp inp-password" :type="showPassword" placeholder="Пароль">
                        <img width="35" :src="eyeImg1" @click="toggleVisibility1" class="eye-icon" alt="">
                    </div>
                    <div class="password-container">
                        <input v-model="exPassword" class="inp inp-rep-password" :type="showExPassword" placeholder="Повторите пароль">
                        <img width="35" :src="eyeImg2" @click="toggleVisibility2" class="eye-icon" alt="">
                    </div>
                </form>
                <p class="error">{{ error }}</p>
                <button @click="check">Войти</button>
                <div class="haveacc">
                    <div class="forgot">
                        <p>Забыли</p><a href="/RecoveryPassPage">пароль</a><p>?</p>
                    </div>
                    <div class="noacc">
                        <p>Нет</p><a href="/SignUp">Аккаунта</a><p>?</p>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
    
<style>
.haveacc p{
    font-size: 26px;
}
    .tototocontainer {
        width: 100%;
        display: flex;
    }

    .background {
        width: 40%;
        height: 91vh;
        background: url(../../assets/Login/backgroundUp.png) center;
        background-repeat: no-repeat; 
    }

    .content p {
        font-size: 56px;
        margin-bottom: 12px;
    }

    .content {
        margin-top: 219px;
        margin-left: 128px;
    }

    .regist form {
        display: flex;
        flex-direction: column;
        gap: 30px;
        margin-bottom: 40px;
    }


    .inp {
        font-size: 18px;
        width: 750px;
        height: 35px;
        padding-left: 10px;
        border-radius: 12px !important;

        border: 1px solid #121212 !important;

        margin-right: 30px;
    }

    .password-container {
        display: flex;
        align-items: center;
        position: relative;
    }

    .eye-icon {
        position: absolute;
        right: 60px;
        cursor: pointer;
    }


    .regist button {
        margin-top: 40px;
        margin-bottom: 15px;

        width: 315px;
        height: 45px;
        font-size: 24px;
        background: none;

        border: 1px solid #2D72D9;
        border-radius: 8px;
        color: #2D72D9;

        transition: all 100ms;
    }

    
   

    .regist button:active {
        background-color: #2D72D9;
        color: #fff;
    }

    .regist .error {
        font-size: 20px;
        margin: 0;
    }
    .regist .haveacc p {
        font-size: 26px;
        margin: 0;
    }

    .regist a {
        font-size: 26px;
        color: #2D72D9;
        font-weight: 500;
    }

    .regist a:hover {
        color: #1b54a9;
    }

    .regist a:active {
        color: #114189;
    }

    .forgot {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .noacc {
        display: flex;
        align-items: center;
        gap: 10px
    }
    
    .haveacc {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .error {
        color: #ff1f1f;
        margin-bottom: -30px !important;
        margin-top: -30px !important;
        font-size: 10px;
    }
    
    .haveacc p:last-child {
        margin-left: -7px;
    }
    
    @media (hover: hover) {     
        .regist button:hover {
            background-color: #2D72D9;
            color: #fff;
        }

        .regist button:active {
            background-color: #1b54a9;
        }
    }
    
    @media (max-width: 1330px) {
        .content {
            margin-left: 50px;
        }
    }

    @media (max-width: 1140px) {
        .content p {
            font-size: 38px;
        }

        .inp {
            width: 550px;
        }

        .haveacc p {
            font-size: 22px;
        }

        .haveacc a {
            font-size: 22px;
        }
    }

    @media (max-width: 830px) {
        .background {
            background: none;
            width: 0%;
        }

        .tototocontainer {
            justify-content: center;
        }

        .content {
            margin-left: 10px;
            margin-right: 10px;
        }

        .inp {
            width: 550px;
        }
    }

    @media(max-width: 600px) {
        .content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .inp {
            width: 100%;
            margin-left: 0;
            margin-right: 0;
        }

        .regist button {
            width: 100%;
        }

        .eye-icon {
            right: 40px;
        }
    }

    @media (max-width: 440px) {
        .haveacc {
            flex-direction: column
        }

        .inp {
            width: 350px;
        }


        .eye-icon {
            right: 35px;
        }
    }
    
</style>