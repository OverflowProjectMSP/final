<script>
import axios from 'axios';

export default {
    data() {
        return {
            exPassword: '',
            exPassword2: ``,
            
            error: '',
            eyeOpen1: true,
            eyeOpen2: true,
            eyeImg1: '/src/assets/eye.svg',
            eyeImg2: '/src/assets/eye.svg',
            isShowPassword: false,
            showPassword: 'password',
            isShowExPassword: false,
            showExPassword: 'password',
        }
    },
    methods: {
        check() {
            if (this.exPassword != this.exPassword2) {
                this.error = '*Пароли не совпадают*'
            } else {
                this.newPassword();
            }
        },
        toggleVisibility1() {
            this.isShowPassword = !this.isShowPassword;
            this.eyeOpen1 = !this.eyeOpen1

            if (this.isShowPassword) {
                this.showPassword = 'text'
                this.eyeImg1 = '/src/assets/svg-editor-image2.svg'
            } else {
                this.showPassword = 'password'
                this.eyeImg1 = '/src/assets/eye.svg'
            }
        },
        toggleVisibility2() {
            this.isShowExPassword = !this.isShowExPassword;
            this.eyeOpen2 = !this.eyeOpen2

            if (this.isShowExPassword) {
                this.showExPassword = 'text'
                this.eyeImg2 = '/src/assets/svg-editor-image2.svg'
            } else {
                this.showExPassword = 'password'
                this.eyeImg2 = '/src/assets/eye.svg'
            }
        },
        
        async newPassword() {
            let res = await axios.put('/new-password-email', {
                password: this.exPassword,
            });
            if(res.data.res == 'Error') {
                this.error = '*Ошибка отправки*';
            } else if(res.data.res == 'True') {
                this.$router.push('/');
            } else {
                this.error = 'Хуйню делаешь брат';
            }
        },
    }
}

</script>

<template>
    <div class="tototocontainer">
        <div class="background"></div>
        <div class="content">
            <p>Смена пароля</p>
            <div class="regist">
                <form @submit.prevent="check">
                    <input v-model="exPassword" class="inp inp-rep-password" type="password" placeholder="Новый пароль">
                    <input v-model="exPassword2" class="inp inp-rep-password" type="password" placeholder="Повторите пароль">
                    <p class="error my-2">{{ error }}</p>
                    <button type="submit">Продолжить</button>
                </form>
                <div class="haveacc">
                    <p>У вас уже есть аккаунт?</p><a href="/Login">Войти -></a>
                </div>
            </div>
        </div>
    </div>
</template>
    
<style>
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

    .regist button {
        margin-top: 40px;
        margin-bottom: 15px;

        width: 320px;
        height: 50px;
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

    .regist p {
        font-size: 26px;
        margin: 0;
    }

    .regist a {
        font-size: 26px;
        color: #2D72D9;
        font-weight: 500;
    }

    
    .regist a:active {
        color: #114189;
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
    }

    @media (hover: hover) {
        .regist button:hover {
            background-color: #2D72D9;
            color: #fff;
        }
    
        .regist button:active {
            background-color: #1b54a9;
            color: #fff;
        }
        
        .regist a:hover {
            color: #1b54a9;
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
            width: 350px;
            margin-left: 0;
            margin-right: 0;
        }

        .regist button {
            width: 100%;
        }
    }

    @media (max-width: 440px) {
        .haveacc {
            flex-direction: column
        }

        .content p {
            text-align: center;
        }
    }
    
</style>